# Scientific review of desulfacinum_medium

- Review: 20261028T172611Z-desulfacinum-medium-batch073
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T17:16:22.522916Z
- Finished UTC: 2026-10-28T17:26:11.109594Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The main DSM1100 provider rates mostly agree with the record, but stock flattening, unsupported calcium mass units, contradicted aerobic context and two supplied-form mappings require curation. Existing pH and correct main values are explicitly credited; exact KOMODO source access remains unavailable.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch073 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003800 | data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml | generated | desulfacinum_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003800 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:003800 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:003800 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:003800 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact source and maintained ownership

identity: supported. Targets: CultureMech:003800.

The generated DESULFACINUM record has exactly one maintained KOMODO1100 contributor. Historical mapping explicitly links DSM1100, and its current primary/API identities agree. Separate DSM and older generated-branch reports are comparison-only; no experimental growth assertion follows from this recipe identity.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:003800.

Five complete historical reports and the exact selected KOMODO plan row were read. No attached evidence exists in either current layer. Individual current API matches are credited without claiming full old-payload equality, historical access time or current KOMODO catalogue authentication. Current conservative merging preserves scientific fields and rejects incompatible formulations. Inspected writer behavior is described separately by exact file and function; it does not prove historical execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:003800.

All 50 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:003800", "selected_concentration_field_count": 50, "selected_concentration_fields_covered": 50, "decisions": [{"decision_id": "q1", "subject": "Na2SO4", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "2.94695", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "2.94695", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe; provider normalization", "interpretation": "The current API explicitly supplies g_l=2.94695, matching the existing value. Credit this as provider-normalized main-recipe evidence; the PDF supplies the quoted batch amount. API volume=1018 ml and 1000 ml listed water do not establish a measured final-volume claim.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.94695,\n                        \"mmol_l\": 20.7474,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 3-3", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Na2SO4                                                   3.00        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject": "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.196464", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.196464", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe; provider normalization", "interpretation": "The current API explicitly supplies g_l=0.196464, matching the existing value. Credit this as provider-normalized main-recipe evidence; the PDF supplies the quoted batch amount. API volume=1018 ml and 1000 ml listed water do not establish a measured final-volume claim.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.196464,\n                        \"mmol_l\": 1.44368,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 4-4", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   KH2PO4                                                   0.20        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject": "NH4Cl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.294695", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.294695", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe; provider normalization", "interpretation": "The current API explicitly supplies g_l=0.294695, matching the existing value. Credit this as provider-normalized main-recipe evidence; the PDF supplies the quoted batch amount. API volume=1018 ml and 1000 ml listed water do not establish a measured final-volume claim.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.294695,\n                        \"mmol_l\": 5.50936,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 5-5", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   NH4Cl                                                    0.30        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject": "NaCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "6.87623", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "6.87623", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe; provider normalization", "interpretation": "The current API explicitly supplies g_l=6.87623, matching the existing value. Credit this as provider-normalized main-recipe evidence; the PDF supplies the quoted batch amount. API volume=1018 ml and 1000 ml listed water do not establish a measured final-volume claim.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 7,\n                        \"unit\": \"g\",\n                        \"g_l\": 6.87623,\n                        \"mmol_l\": 117.663,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 6-6", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   NaCl                                                     7.00        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q5", "subject": "MgCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "3.04519", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "3.04519", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe; provider normalization", "interpretation": "The current API explicitly supplies g_l=3.04519, matching the existing value. Credit this as provider-normalized main-recipe evidence; the PDF supplies the quoted batch amount. API volume=1018 ml and 1000 ml listed water do not establish a measured final-volume claim.", "sources": [{"locator": "$.data.solutions[0].recipe[6]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 3.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.04519,\n                        \"mmol_l\": 14.9786,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 9-9", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   MgCl2 x 6 H2O                                            3.10        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q6", "subject": "KCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.491159", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.491159", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe; provider normalization", "interpretation": "The current API explicitly supplies g_l=0.491159, matching the existing value. Credit this as provider-normalized main-recipe evidence; the PDF supplies the quoted batch amount. API volume=1018 ml and 1000 ml listed water do not establish a measured final-volume claim.", "sources": [{"locator": "$.data.solutions[0].recipe[7]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.491159,\n                        \"mmol_l\": 6.58832,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 10-10", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   KCl                                                      0.50        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q7", "subject": "CaCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.15", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.15", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Main DSM1100 recipe; provider normalization", "interpretation": "Both current PDF and API explicitly give 0.15 ml, without solution strength or g_l. The local 0.15 G_PER_L is dimensionally unsupported. Preserve the source inconsistency and request source clarification; do not silently change ml to g or infer density.", "sources": [{"locator": "$.data.solutions[0].recipe[8]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 11-11", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   CaCl2 x 2 H2O                                            0.15       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q8", "subject": "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.491159", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.491159", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe; provider normalization", "interpretation": "The current API explicitly supplies g_l=0.491159, matching the existing value. Credit this as provider-normalized main-recipe evidence; the PDF supplies the quoted batch amount. API volume=1018 ml and 1000 ml listed water do not establish a measured final-volume claim.", "sources": [{"locator": "$.data.solutions[0].recipe[9]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.491159,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 12-12", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Yeast extract                                            0.50        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject": "Sodium resazurin", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.000491159", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.000491159", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe; provider normalization", "interpretation": "The current API explicitly supplies g_l=0.000491159, matching the existing value. Credit this as provider-normalized main-recipe evidence; the PDF supplies the quoted batch amount. API volume=1018 ml and 1000 ml listed water do not establish a measured final-volume claim. The primary 0.5 ml of 0.1% w/v is a separate stock addition; retain that dose and strength rather than replacing it solely with the derived rate.", "sources": [{"locator": "$.data.solutions[0].recipe[10]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000491159,\n                        \"mmol_l\": 0.00195548,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 13-13", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Sodium resazurin (0.1% w/v)                              0.50       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q10", "subject": "NaHCO3", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "1.47348", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "1.47348", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe; provider normalization", "interpretation": "The current API explicitly supplies g_l=1.47348, matching the existing value. Credit this as provider-normalized main-recipe evidence; the PDF supplies the quoted batch amount. API volume=1018 ml and 1000 ml listed water do not establish a measured final-volume claim.", "sources": [{"locator": "$.data.solutions[0].recipe[11]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.47348,\n                        \"mmol_l\": 17.5399,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 14-14", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   NaHCO3                                                   1.50        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q11", "subject": "Na-L-lactate", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "1.96464", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "1.96464", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe; provider normalization", "interpretation": "The current API explicitly supplies g_l=1.96464, matching the existing value. Credit this as provider-normalized main-recipe evidence; the PDF supplies the quoted batch amount. API volume=1018 ml and 1000 ml listed water do not establish a measured final-volume claim.", "sources": [{"locator": "$.data.solutions[0].recipe[12]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na-L-lactate\",\n                        \"compound_id\": 265,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.96464,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 15-15", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Na-L-lactate                                             2.00        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q12", "subject": "Na2-EDTA x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "5.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "5.2", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly as main ingredient", "interpretation": "The existing 5.2 G_PER_L is supported only within Trace element solution SL-11, not as an undiluted main-medium concentration. Preserve the source amount/form and reconstruct the stock with its separately quoted receiving dose. The source explicitly brings this stock to 1000 ml; mg-to-g conversion is therefore supported at stock scope.", "sources": [{"locator": "$.data.solutions[1].recipe[0]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\": 676,\n                        \"amount\": 5.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\": 15.4667,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 30-30", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Na2-EDTA x 2 H2O                                         5.20       g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q13", "subject": "FeCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly as main ingredient", "interpretation": "The existing 1.5 G_PER_L is supported only within Trace element solution SL-11, not as an undiluted main-medium concentration. Preserve the source amount/form and reconstruct the stock with its separately quoted receiving dose. The source explicitly brings this stock to 1000 ml; mg-to-g conversion is therefore supported at stock scope.", "sources": [{"locator": "$.data.solutions[1].recipe[1]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 31-31", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   FeCl2 x 4 H2O                                            1.50       g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q14", "subject": "ZnCl2", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly as main ingredient", "interpretation": "The existing 0.07 G_PER_L is supported only within Trace element solution SL-11, not as an undiluted main-medium concentration. Preserve the source amount/form and reconstruct the stock with its separately quoted receiving dose. The source explicitly brings this stock to 1000 ml; mg-to-g conversion is therefore supported at stock scope.", "sources": [{"locator": "$.data.solutions[1].recipe[2]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 32-32", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   ZnCl2                                                   70.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q15", "subject": "MnCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly as main ingredient", "interpretation": "The existing 0.1 G_PER_L is supported only within Trace element solution SL-11, not as an undiluted main-medium concentration. Preserve the source amount/form and reconstruct the stock with its separately quoted receiving dose. The source explicitly brings this stock to 1000 ml; mg-to-g conversion is therefore supported at stock scope.", "sources": [{"locator": "$.data.solutions[1].recipe[3]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 33-33", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   MnCl2 x 4 H2O                                          100.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q16", "subject": "H3BO3", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly as main ingredient", "interpretation": "The existing 0.006 G_PER_L is supported only within Trace element solution SL-11, not as an undiluted main-medium concentration. Preserve the source amount/form and reconstruct the stock with its separately quoted receiving dose. The source explicitly brings this stock to 1000 ml; mg-to-g conversion is therefore supported at stock scope.", "sources": [{"locator": "$.data.solutions[1].recipe[4]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 34-34", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   H3BO3                                                    6.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q17", "subject": "CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly as main ingredient", "interpretation": "The existing 0.19 G_PER_L is supported only within Trace element solution SL-11, not as an undiluted main-medium concentration. Preserve the source amount/form and reconstruct the stock with its separately quoted receiving dose. The source explicitly brings this stock to 1000 ml; mg-to-g conversion is therefore supported at stock scope.", "sources": [{"locator": "$.data.solutions[1].recipe[5]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 35-35", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   CoCl2 x 6 H2O                                          190.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q18", "subject": "CuCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly as main ingredient", "interpretation": "The existing 0.002 G_PER_L is supported only within Trace element solution SL-11, not as an undiluted main-medium concentration. Preserve the source amount/form and reconstruct the stock with its separately quoted receiving dose. The source explicitly brings this stock to 1000 ml; mg-to-g conversion is therefore supported at stock scope.", "sources": [{"locator": "$.data.solutions[1].recipe[6]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 36-36", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   CuCl2 x 2 H2O                                            2.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q19", "subject": "NiCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly as main ingredient", "interpretation": "The existing 0.024 G_PER_L is supported only within Trace element solution SL-11, not as an undiluted main-medium concentration. Preserve the source amount/form and reconstruct the stock with its separately quoted receiving dose. The source explicitly brings this stock to 1000 ml; mg-to-g conversion is therefore supported at stock scope.", "sources": [{"locator": "$.data.solutions[1].recipe[7]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 37-37", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   NiCl2 x 6 H2O                                           24.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q20", "subject": "Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly as main ingredient", "interpretation": "The existing 0.036 G_PER_L is supported only within Trace element solution SL-11, not as an undiluted main-medium concentration. Preserve the source amount/form and reconstruct the stock with its separately quoted receiving dose. The source explicitly brings this stock to 1000 ml; mg-to-g conversion is therefore supported at stock scope.", "sources": [{"locator": "$.data.solutions[1].recipe[8]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 38-38", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Na2MoO4 x 2 H2O                                         36.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q21", "subject": "NaOH", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly as main ingredient", "interpretation": "The existing 0.5 G_PER_L is supported only within Selenite-tungstate solution, not as an undiluted main-medium concentration. Preserve the source amount/form and reconstruct the stock with its separately quoted receiving dose. The source lists 1000 ml water and the API explicitly supplies this stock rate; it does not state a main-medium final volume.", "sources": [{"locator": "$.data.solutions[2].recipe[0]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 55-55", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   NaOH                                                    0.50       g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q22", "subject": "Na2SeO3 x 5 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly as main ingredient", "interpretation": "The existing 0.003 G_PER_L is supported only within Selenite-tungstate solution, not as an undiluted main-medium concentration. Preserve the source amount/form and reconstruct the stock with its separately quoted receiving dose. The source lists 1000 ml water and the API explicitly supplies this stock rate; it does not state a main-medium final volume.", "sources": [{"locator": "$.data.solutions[2].recipe[1]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 56-56", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Na2SeO3 x 5 H2O                                         3.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q23", "subject": "Na2WO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.004", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.004", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly as main ingredient", "interpretation": "The existing 0.004 G_PER_L is supported only within Selenite-tungstate solution, not as an undiluted main-medium concentration. Preserve the source amount/form and reconstruct the stock with its separately quoted receiving dose. The source lists 1000 ml water and the API explicitly supplies this stock rate; it does not state a main-medium final volume.", "sources": [{"locator": "$.data.solutions[2].recipe[2]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 57-57", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Na2WO4 x 2 H2O                                          4.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q24", "subject": "Na2S x 9 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "30", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "30", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly as main ingredient", "interpretation": "The existing 30 G_PER_L is supported only within Neutralized sulfide solution 3% (w/v), not as an undiluted main-medium concentration. Preserve the source amount/form and reconstruct the stock with its separately quoted receiving dose. The primary explicitly labels this stock 3% (w/v); current API has added g_l=30 to the historical object. The receiving dose is 15 ml, not the entire stock.", "sources": [{"locator": "$.data.solutions[3].recipe[0]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 124.905,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 63-63", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Na2S x 9 H2O                                            3.00        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q25", "subject": "HCl placeholder", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "variable", "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "Imported pH-buffer annotation", "interpretation": "The unquantified placeholder does not supply a dose. The historical KOMODO mapping mentions HCl, but its current exact endpoint is inaccessible and DSM1100 only says adjust main pH as necessary. Do not promote the historical buffer name to a verified source reagent; the sulfide stock instead explicitly uses 2 M H2SO4.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve ingredients (except bicarbonate, lactate and sulfide) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add lactate and sulfide form sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Adjust pH of the complete medium to 7.2, if necessary.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[3].steps[0]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"step\": \"The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at 121\\u00b0C. After cooling to room temperature the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q26", "subject": "Trace element solution SL-11", "local_fields": [], "decision": "add", "stage": "Main receiving dose or batch water", "interpretation": "This exact source batch input is absent from the structured record. Preserve its absolute unit and stage; do not rename it as a measured per-litre final amount.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\": 1474,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 7-7", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Trace element solution SL-11                             1.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q27", "subject": "Selenite-tungstate solution", "local_fields": [], "decision": "add", "stage": "Main receiving dose or batch water", "interpretation": "This exact source batch input is absent from the structured record. Preserve its absolute unit and stage; do not rename it as a measured per-litre final amount.", "sources": [{"locator": "$.data.solutions[0].recipe[5]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 8-8", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Selenite-tungstate solution                              1.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q28", "subject": "Neutralized sulfide solution 3% (w/v)", "local_fields": [], "decision": "add", "stage": "Main receiving dose or batch water", "interpretation": "This exact source batch input is absent from the structured record. Preserve its absolute unit and stage; do not rename it as a measured per-litre final amount.", "sources": [{"locator": "$.data.solutions[0].recipe[13]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"solution\": \"Neutralized sulfide solution 3% (w/v)\",\n                        \"solution_id\": 34,\n                        \"amount\": 15,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 16-16", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Neutralized sulfide solution 3% (w/v)                   15.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q29", "subject": "Distilled water", "local_fields": [], "decision": "add", "stage": "Main receiving dose or batch water", "interpretation": "This exact source batch input is absent from the structured record. Preserve its absolute unit and stage; do not rename it as a measured per-litre final amount.", "sources": [{"locator": "$.data.solutions[0].recipe[14]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 17-17", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Distilled water                                       1000.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q30", "subject": "Stock water Trace element solution SL-11", "local_fields": [], "decision": "add", "stage": "Stock solvent", "interpretation": "Retain this stock-specific solvent input separately. SL-11 additionally has an explicit final make-up instruction; the other listed water volumes are not by themselves measured final volumes.", "sources": [{"locator": "$.data.solutions[1].recipe[9]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 39-39", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Distilled water                                       1000.00      ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q31", "subject": "Stock water Selenite-tungstate solution", "local_fields": [], "decision": "add", "stage": "Stock solvent", "interpretation": "Retain this stock-specific solvent input separately. SL-11 additionally has an explicit final make-up instruction; the other listed water volumes are not by themselves measured final volumes.", "sources": [{"locator": "$.data.solutions[2].recipe[3]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 58-58", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Distilled water                                      1000.00      ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q32", "subject": "Stock water Neutralized sulfide solution 3% (w/v)", "local_fields": [], "decision": "add", "stage": "Stock solvent", "interpretation": "Retain this stock-specific solvent input separately. SL-11 additionally has an explicit final make-up instruction; the other listed water volumes are not by themselves measured final volumes.", "sources": [{"locator": "$.data.solutions[3].recipe[1]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 64-64", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Distilled water                                       100.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q33", "subject": "Main pH and anaerobic preparation", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ph_value", "original": 7.2}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml", "field_path": "ph_value", "original": 7.2}], "decision": "evidence_only", "stage": "Main preparation", "interpretation": "The retained pH 7.2 matches current source. Restore the missing staged preparation: 100% N2 for 30–45 min, anoxic dispensing/autoclaving, separate sterile lactate/sulfide additions under N2 and bicarbonate under 80% N2/20% CO2. The source does not specify a main autoclave duration or temperature here.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve ingredients (except bicarbonate, lactate and sulfide) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add lactate and sulfide form sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Adjust pH of the complete medium to 7.2, if necessary.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 19-24", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "Dissolve ingredients (except bicarbonate, lactate and sulfide) and sparge medium with\n100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas\natmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add lactate and\nsulfide form sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate\nfrom a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture.\nAdjust pH of the complete medium to 7.2, if necessary.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q34", "subject": "SL-11 preparation controls", "local_fields": [], "decision": "add", "stage": "SL-11 stock only", "interpretation": "Preserve initial 800 ml water, pH 7 with 2 N NaOH, sequential dissolution, final pH 6.0 and make-up to 1000 ml. The NaOH titration volume is unquantified; no extra main-medium dose is inferred.", "sources": [{"locator": "$.data.solutions[1].steps[0]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0 and bring volume to 1000 ml. \"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 41-43", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q35", "subject": "Neutralized sulfide preparation controls", "local_fields": [], "decision": "add", "stage": "Sulfide stock only", "interpretation": "Preserve 250 ml vessel capacity separately from the 100 ml water batch, N2 treatment, 15 min at 121°C, cooling and pH about 7 with sterile 2 M H2SO4. Acid addition is dropwise and unquantified. These stock controls do not establish main-medium autoclave settings.", "sources": [{"locator": "$.data.solutions[3].steps[0]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"step\": \"The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at 121\\u00b0C. After cooling to room temperature the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 66-70", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber\nseptum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and\nautoclaved for 15 min. at 121°C. After cooling to room temperature the pH is adjusted to\nabout 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the\nbottle.", "quote_representation": "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch073/record04/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:003800.

data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml: primary 24/25, secondary 23/25; data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml: primary 24/25, secondary 23/25. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:003800.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:003800.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Stock composition and unsupported calcium units obscure the main recipe

major / open / confirmed; issue key: culturemech-003800-flattened-stocks-and-unit-basis.

Thirteen stock-component rates are flattened into main ingredients. The SL-11, selenite-tungstate and neutralized sulfide receiving doses, stock solvents and preparation are missing. Main provider rates are credited individually; the historical blanket conflict classification is too broad. Calcium is specifically unsupported because both current primary and API say 0.15 ml without stock strength, whereas the record says 0.15 G_PER_L.

### f2: Aerobic annotation contradicts the primary anaerobic preparation

major / open / confirmed; issue key: culturemech-003800-anoxic-preparation-context.

Both selected layers retain Aerobic: Yes but lack the source anoxic preparation and its separate supplementation stages. The existing pH 7.2 is correct. Stock-specific acid, vessel and autoclave controls must not be transferred to the main medium.

### f3: Nickel hydrate and sodium resazurin are linked to different supplied forms

major / open / confirmed; issue key: culturemech-003800-nickel-hydrate-and-sodium-resazurin-form.

Every selected layer names nickel chloride hexahydrate but asserts anhydrous nickel dichloride CHEBI:34887 in both primary and secondary slots. Sodium resazurin is linked through its primary slot to neutral Resazurin CHEBI:8806; there is no asserted resazurin secondary slot to correct. Exact labels pass native checks, but OLS formulas Cl2Ni and C12H7NO4 do not encode the supplied forms. Current MIM matches describe those asserted IDs, not hydrate or sodium-salt equivalence.

### f4: Historical source annotations need bounded authentication and valid future timestamps

minor / open / confirmed; issue key: culturemech-003800-append-only-provenance-and-writers.

The current record has no attached formulation claims despite prior review narratives. Stored KOMODO import history contains literal .fZ and enrichment timestamps lack timezone; preserve those historical bytes. Current API objects are compared individually because its sulfide object now includes g_l/mmol_l absent from the older payload. Current exact KOMODO access is HTTP 403; historical catalogue bytes and execution times remain unverified.

## Recommended Actions And Acceptance Checks

### action1

Reconstruct source-specific stocks and receiving doses, retain all directly supported main provider rates with their stated basis, and preserve the unresolved calcium volume/unit issue for source clarification. Do not infer final concentrations from listed water or silently replace ml with g.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Preserve the correct pH, replace the contradicted atmosphere annotation with source-scoped preparation and attach stage-specific root evidence. Keep unquantified titrants unresolved.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Resolve the exact source hydrate and sodium-salt identities against authoritative ontology and MIM records. Use verified supplied-form mappings or retain precise source labels with unresolved mapping; preserve source masses and do not substitute anhydrous molar arithmetic.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Attach fresh claim-scoped evidence and append a new verified corrective event with the actual current date. Preserve malformed historical events unchanged; fix future timestamp generation in the exact inspected writers and retain the current conservative merge safeguards.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.
- Verify future KOMODO importer and DSMZ enrichment events use actual UTC timestamps with timezone, while original historical event bytes remain unchanged.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch073/record04/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch073/record04/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch073/record04/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch073/record04/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| dsm1100 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current primary captured text and available rendered PDF pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| api1100 | https://mediadive.dsmz.de/api/medium/1100; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 404, error &lt;HTTPError 404: 'Not Found'&gt;. This response does not authenticate a recipe. |
| komodo1100 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1100; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:131361 = disodium selenite pentahydrate; definition ['A hydrate that is the pentahydrate form of disodium selenite.']; formula ['5H2O.2Na.O3Se']; mass ['263.012']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi132194 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132194; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | context_only | Excluded candidate lead: current OLS identifies CHEBI:132194 as glycine-d5. It is unrelated to sodium resazurin and supplies no replacement mapping. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17883 = hydrogen chloride; definition ['A mononuclear parent hydride consisting of covalently bonded hydrogen and chlorine atoms.']; formula ['HCl']; mass ['36.461']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi232798 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_232798; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:232798 = sodium L-lactate; definition []; formula ['C3H5O3.Na']; mass ['112.06']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32139 = sodium hydrogencarbonate; definition []; formula ['CHO3.Na']; mass ['84.006']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
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
| chebi64758 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64758; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:64758 = EDTA disodium salt dihydrate; definition ['A hydrate that is the dihydrate form of EDTA disodium salt.']; formula ['C10H14N2O8.2H2O.2Na']; mass ['372.238']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na']; mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:76209 = sodium sulfide nonahydrate; definition ['A hydrate with formula Na&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;S·9H&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;O.']; formula ['9H2O.2Na.S']; mass ['240.182']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O']; mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86249 = iron dichloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of iron dichloride.']; formula ['Cl2Fe.4H2O']; mass ['198.811']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg']; mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4']; mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| api1100Rest | https://mediadive.dsmz.de/rest/medium/1100; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| grounding | REVIEW_WORK/batch073/record04/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. The complete current raw digest does not match the cited historical digest (or no digest is supplied). 33 of 34 individually quoted objects match decoded current locators and literal raw bytes; this narrower match is credited separately. A narrative or zero-source-check report alone is derivative evidence. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfacinum_medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. The complete current raw digest does not match the cited historical digest (or no digest is supplied). 0 of 0 individually quoted objects match decoded current locators and literal raw bytes; this narrower match is credited separately. A narrative or zero-source-check report alone is derivative evidence. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. The complete current raw digest does not match the cited historical digest (or no digest is supplied). 0 of 0 individually quoted objects match decoded current locators and literal raw bytes; this narrower match is credited separately. A narrative or zero-source-check report alone is derivative evidence. |
| history3 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfacinum_medium__82d8912a.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. The complete current raw digest does not match the cited historical digest (or no digest is supplied). 0 of 0 individually quoted objects match decoded current locators and literal raw bytes; this narrower match is credited separately. A narrative or zero-source-check report alone is derivative evidence. |
| history4 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFACINUM_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. The complete current raw digest does not match the cited historical digest (or no digest is supplied). 0 of 0 individually quoted objects match decoded current locators and literal raw bytes; this narrower match is credited separately. A narrative or zero-source-check report alone is derivative evidence. |
| history-auth | REVIEW_WORK/batch073/record04/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer43 | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group collapses equal duplicate values without summing them and retains the first conflicting value with a flag. This behavior is distinct from historical summed-amount artifacts and does not authenticate source-specific stock or product structure. |
| writer44 | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients; merge_ingredient_group | context_only | Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group retains the first concentration, flags differing values and selects the first CHEBI. It cannot establish source stages or justify collapsing independent supplemental and product-contained components. |
| writer45 | scripts/repair_merged_duplicates.py; repair_ingredient; repair_record | context_only | Current repair_ingredient and repair_record act on parsed IDENTICAL_PARTS duplicate notes. This bounded repair is not a general solution for product decomposition, stock flattening or differing source formulations. |
| writer46 | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata | context_only | Current DSMZCompositionResolver.merge_composition copies ingredients and solutions, fills pH when absent and copies physical/medium type, but does not copy preparation steps. _add_enrichment_metadata records a naive current timestamp. This explains a present omission risk, not historical execution. |
| writer47 | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current _convert_to_culturemech constructs source notes and default LIQUID with empty ingredients. Its time.strftime format contains %f, which is unsupported here and is consistent with literal .fZ in stored import events. Current code does not authenticate the original retrieval or justify rewriting historical time. |
| writer48 | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps | context_only | Current _parse_api_composition considers the primary recipe, prefers provider g_l when available and excludes four recognized water labels; tap water is not among those exclusions; _is_api_stock_addition distinguishes stock additions. _parse_api_solutions retains separate stock structure. _parse_preparation_steps collects solution prose. These present behaviors do not establish historical execution and cannot justify interpreting flattened stock rates as final-medium concentrations. |
| writer49 | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current formulation_content retains exact scientific quantities, preparation and other scientific fields; merge_formulation_evidence rejects incompatible projections and unions evidence at matching scopes. A source-equivalence claim is not established by shared ingredient identities. |
| writer50 | src/culturemech/merge/matcher.py; group_formulations; group_recipes | context_only | Current group_formulations calls group_recipes with fail_on_invalid=True and FormulationFingerprinter. Expected standalone or unfingerprintable records are excluded; malformed or unexpected inputs raise. Valid records are grouped by full scientific content. This guard does not retrieve or authenticate source recipes. |
| writer51 | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group routes a single maintained owner with merge metadata; multiple owners pass through conservative merge_formulation_evidence. Regenerating from an unrepaired owner retains its defects. Current conservative behavior is credited and does not establish how the old generated record was produced. |
| quantity-inventory | REVIEW_WORK/batch073/record04/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- Exact historical KOMODO MediaInfo=1100 returned HTTP 403. Failed guessed /api/medium routes are preserved separately from successful official /rest/medium captures.
- The PDF and API both label calcium as 0.15 ml without a strength; no mass, density or corrected source unit is invented.
- Listed 1000 ml main water and API volume metadata do not establish an explicit final medium volume.
- CHEBI:132194 was an unrelated discovery lead (glycine-d5), explicitly excluded. CHEBI:53542 supports nickel chloride hexahydrate; the exact sodium-resazurin replacement remains unresolved.
- Current code behavior and individually matching historical objects do not authenticate historical execution or separately cited KOMODO catalogue bytes.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T172611Z-desulfacinum-medium-batch073
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of desulfacinum_medium
started_at: '2026-10-28T17:16:22.522916Z'
finished_at: '2026-10-28T17:26:11.109594Z'
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
summary: The main DSM1100 provider rates mostly agree with the record, but stock flattening,
  unsupported calcium mass units, contradicted aerobic context and two supplied-form
  mappings require curation. Existing pH and correct main values are explicitly credited;
  exact KOMODO source access remains unavailable.
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
  - path: data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml
    sha256: 9bba2a59c73202535e2fc43c52721475ea88d338d4e7929305af8a25181e9c2c
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml
    sha256: 694dbcf90c8a99d9b2ac4a15c91c81a92a4ed7da489978b3ab95c822399a62d2
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
  - path: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/plan.json
    sha256: 0fc7158ec48d1b0c75efa149070b46b677bb3389d969a1440267f43e21b3d3c8
    role: context
  - path: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml.md
    sha256: 00254b00d60dd6de56d7c2c454f26867273f67a1ba66d5b60faced4a841d3800
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFACINUM_MEDIUM.md
    sha256: c5361dd8d68fab84db2cc721c192093fdb008a5d9b96a6a3926547575dbfd3d4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfacinum_medium__82d8912a.md
    sha256: 7f6287840f4380e823048721f59cd949aa7233fe32dfe5195f7668b2ccfd64a5
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.md
    sha256: 30d22769ef2a6ed7d97de61af779b82fd90db1e1dca1601f172ca0eda82ebc11
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfacinum_medium.md
    sha256: 836c2b60a96611f4ca2349ad073ea95861890c1249979f1e6d4e7890e2a13ef6
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
  selection: Authoritative batch073 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003800
targets:
- target_id: CultureMech:003800
  path: data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml
  label: desulfacinum_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:003800
  command: just validate-schema data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:003800
  command: just validate-strict data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml --workers
    1 --out REVIEW_WORK/batch073/record04/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:003800
  command: just validate-terms data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:003800
  command: just validate-references data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T17:26:11.081882Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 9bba2a59c73202535e2fc43c52721475ea88d338d4e7929305af8a25181e9c2c
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T17:26:11.082062Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 694dbcf90c8a99d9b2ac4a15c91c81a92a4ed7da489978b3ab95c822399a62d2
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch073/record04/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T17:16:23.882037Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 0bfd3bc1e333572de512455660cb51913166e84db56a25bbc084bd2640af2f78
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch073/record04/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T17:16:24.809963Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 97e1d607c4f7394e825815d35db2ea11e7f556de2499d02eb6c9aeab03717ff4
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch073/record04/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T17:16:26.302745Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 7a311ab0e0ad966e297db33037b39c89b8fddd896c6752f500e41183dc839b0a
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch073/record04/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T17:16:27.130733Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 4389885555afb38890ab2379d10e051a599ba20f1618d690941fa8a614c86de0
- evidence_id: dsm1100
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T17:17:09.159454Z'
  support: supports
  summary: 'Complete current primary captured text and available rendered PDF pages
    read: exact main recipe, separate stock tables, preparation and any strain-specific
    prescriptions. A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a
- evidence_id: api1100
  kind: database
  reference: https://mediadive.dsmz.de/api/medium/1100
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T17:17:09.159710Z'
  support: unknown
  summary: 'Actual retrieval HTTP 404, error <HTTPError 404: ''Not Found''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: 7b338109162cb392abfc13810679839927f91564c68b550c34747a4fda1900cb
- evidence_id: komodo1100
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1100
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T17:17:09.159783Z'
  support: unknown
  summary: 'Actual retrieval HTTP 403, error <HTTPError 403: ''Forbidden''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: 3fdc480c66e8a6847f3ab17f33f294f63ade4b0ea9375b6b1dd71665f271c674
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
- evidence_id: chebi232798
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_232798
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:09.548063Z'
  support: supports
  summary: OLS current exact CHEBI:232798 = sodium L-lactate; definition []; formula
    ['C3H5O3.Na']; mass ['112.06']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 9babe942a39eb91a513ec202dbae4289fda9f5586836aaee58192b4795ce7344
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
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:09.921368Z'
  support: supports
  summary: OLS current exact CHEBI:32139 = sodium hydrogencarbonate; definition [];
    formula ['CHO3.Na']; mass ['84.006']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
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
- evidence_id: chebi64758
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64758
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T17:17:11.164753Z'
  support: supports
  summary: OLS current exact CHEBI:64758 = EDTA disodium salt dihydrate; definition
    ['A hydrate that is the dihydrate form of EDTA disodium salt.']; formula ['C10H14N2O8.2H2O.2Na'];
    mass ['372.238']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 5432921ff4fea3479e93ce6392a2654e3d5560255beb96022793102e776d9647
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
- evidence_id: api1100Rest
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1100
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T17:17:36.912797Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: 1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch073/record04/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T17:26:11.085005Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 2b623d040794911cf2d9827d6e963db020883f9c2881148bc8269f9bbe1dc229
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T17:26:11.085985Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. The
    complete current raw digest does not match the cited historical digest (or no
    digest is supplied). 33 of 34 individually quoted objects match decoded current
    locators and literal raw bytes; this narrower match is credited separately. A
    narrative or zero-source-check report alone is derivative evidence.
  snapshot_sha256: 00254b00d60dd6de56d7c2c454f26867273f67a1ba66d5b60faced4a841d3800
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfacinum_medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T17:26:11.086007Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. The
    complete current raw digest does not match the cited historical digest (or no
    digest is supplied). 0 of 0 individually quoted objects match decoded current
    locators and literal raw bytes; this narrower match is credited separately. A
    narrative or zero-source-check report alone is derivative evidence.
  snapshot_sha256: 836c2b60a96611f4ca2349ad073ea95861890c1249979f1e6d4e7890e2a13ef6
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T17:26:11.086027Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. The
    complete current raw digest does not match the cited historical digest (or no
    digest is supplied). 0 of 0 individually quoted objects match decoded current
    locators and literal raw bytes; this narrower match is credited separately. A
    narrative or zero-source-check report alone is derivative evidence.
  snapshot_sha256: 30d22769ef2a6ed7d97de61af779b82fd90db1e1dca1601f172ca0eda82ebc11
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfacinum_medium__82d8912a.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T17:26:11.086046Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. The
    complete current raw digest does not match the cited historical digest (or no
    digest is supplied). 0 of 0 individually quoted objects match decoded current
    locators and literal raw bytes; this narrower match is credited separately. A
    narrative or zero-source-check report alone is derivative evidence.
  snapshot_sha256: 7f6287840f4380e823048721f59cd949aa7233fe32dfe5195f7668b2ccfd64a5
- evidence_id: history4
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFACINUM_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T17:26:11.086064Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. The
    complete current raw digest does not match the cited historical digest (or no
    digest is supplied). 0 of 0 individually quoted objects match decoded current
    locators and literal raw bytes; this narrower match is credited separately. A
    narrative or zero-source-check report alone is derivative evidence.
  snapshot_sha256: c5361dd8d68fab84db2cc721c192093fdb008a5d9b96a6a3926547575dbfd3d4
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch073/record04/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T17:26:11.086186Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: 86c90c57fe3081e5f71ab7a4d55588503d9a7706c0cc40415a0cd1808229e0d2
- evidence_id: writer43
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T17:26:11.086252Z'
  support: context_only
  summary: Current _merge_ingredient_group collapses equal duplicate values without
    summing them and retains the first conflicting value with a flag. This behavior
    is distinct from historical summed-amount artifacts and does not authenticate
    source-specific stock or product structure.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer44
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: merge_duplicate_ingredients; merge_ingredient_group
  accessed_at: '2026-10-28T17:26:11.086274Z'
  support: context_only
  summary: Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group
    retains the first concentration, flags differing values and selects the first
    CHEBI. It cannot establish source stages or justify collapsing independent supplemental
    and product-contained components.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer45
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: repair_ingredient; repair_record
  accessed_at: '2026-10-28T17:26:11.086309Z'
  support: context_only
  summary: Current repair_ingredient and repair_record act on parsed IDENTICAL_PARTS
    duplicate notes. This bounded repair is not a general solution for product decomposition,
    stock flattening or differing source formulations.
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: writer46
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata
  accessed_at: '2026-10-28T17:26:11.086335Z'
  support: context_only
  summary: Current DSMZCompositionResolver.merge_composition copies ingredients and
    solutions, fills pH when absent and copies physical/medium type, but does not
    copy preparation steps. _add_enrichment_metadata records a naive current timestamp.
    This explains a present omission risk, not historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer47
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T17:26:11.086356Z'
  support: context_only
  summary: Current _convert_to_culturemech constructs source notes and default LIQUID
    with empty ingredients. Its time.strftime format contains %f, which is unsupported
    here and is consistent with literal .fZ in stored import events. Current code
    does not authenticate the original retrieval or justify rewriting historical time.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer48
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps
  accessed_at: '2026-10-28T17:26:11.086384Z'
  support: context_only
  summary: Current _parse_api_composition considers the primary recipe, prefers provider
    g_l when available and excludes four recognized water labels; tap water is not
    among those exclusions; _is_api_stock_addition distinguishes stock additions.
    _parse_api_solutions retains separate stock structure. _parse_preparation_steps
    collects solution prose. These present behaviors do not establish historical execution
    and cannot justify interpreting flattened stock rates as final-medium concentrations.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer49
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T17:26:11.086406Z'
  support: context_only
  summary: Current formulation_content retains exact scientific quantities, preparation
    and other scientific fields; merge_formulation_evidence rejects incompatible projections
    and unions evidence at matching scopes. A source-equivalence claim is not established
    by shared ingredient identities.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer50
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations; group_recipes
  accessed_at: '2026-10-28T17:26:11.086425Z'
  support: context_only
  summary: Current group_formulations calls group_recipes with fail_on_invalid=True
    and FormulationFingerprinter. Expected standalone or unfingerprintable records
    are excluded; malformed or unexpected inputs raise. Valid records are grouped
    by full scientific content. This guard does not retrieve or authenticate source
    recipes.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer51
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T17:26:11.086445Z'
  support: context_only
  summary: Current merge_group routes a single maintained owner with merge metadata;
    multiple owners pass through conservative merge_formulation_evidence. Regenerating
    from an unrepaired owner retains its defects. Current conservative behavior is
    credited and does not establish how the old generated record was produced.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch073/record04/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T17:26:11.109421Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: 296608807dfbedc88d850cff779ace889fdd8503115f6b88b86d17d3d3183d72
assessments:
- assessment_id: a1
  area: identity
  topic: Exact source and maintained ownership
  outcome: supported
  summary: The generated DESULFACINUM record has exactly one maintained KOMODO1100
    contributor. Historical mapping explicitly links DSM1100, and its current primary/API
    identities agree. Separate DSM and older generated-branch reports are comparison-only;
    no experimental growth assertion follows from this recipe identity.
  target_ids:
  - CultureMech:003800
  evidence_ids:
  - local0
  - local1
  - dsm1100
  - api1100Rest
  - history-auth
- assessment_id: a2
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: Five complete historical reports and the exact selected KOMODO plan row
    were read. No attached evidence exists in either current layer. Individual current
    API matches are credited without claiming full old-payload equality, historical
    access time or current KOMODO catalogue authentication. Current conservative merging
    preserves scientific fields and rejects incompatible formulations. Inspected writer
    behavior is described separately by exact file and function; it does not prove
    historical execution.
  target_ids:
  - CultureMech:003800
  evidence_ids:
  - history-auth
  - writer43
  - writer44
  - writer45
  - writer46
  - writer47
  - writer48
  - writer49
  - writer50
  - writer51
- assessment_id: a3
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 50 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:003800
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:003800",
    "selected_concentration_field_count": 50, "selected_concentration_fields_covered":
    50, "decisions": [{"decision_id": "q1", "subject": "Na2SO4", "local_fields": [{"record_path":
    "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path": "ingredients[0].concentration",
    "original": {"value": "2.94695", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "2.94695",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe;
    provider normalization", "interpretation": "The current API explicitly supplies
    g_l=2.94695, matching the existing value. Credit this as provider-normalized main-recipe
    evidence; the PDF supplies the quoted batch amount. API volume=1018 ml and 1000
    ml listed water do not establish a measured final-volume claim.", "sources": [{"locator":
    "$.data.solutions[0].recipe[0]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.94695,\n                        \"mmol_l\":
    20.7474,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 3-3", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Na2SO4                                                   3.00        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject":
    "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.196464",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.196464",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe;
    provider normalization", "interpretation": "The current API explicitly supplies
    g_l=0.196464, matching the existing value. Credit this as provider-normalized
    main-recipe evidence; the PDF supplies the quoted batch amount. API volume=1018
    ml and 1000 ml listed water do not establish a measured final-volume claim.",
    "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api1100Rest",
    "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256":
    "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256":
    "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at":
    "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.196464,\n                        \"mmol_l\":
    1.44368,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 4-4", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   KH2PO4                                                   0.20        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject":
    "NH4Cl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.294695",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.294695",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe;
    provider normalization", "interpretation": "The current API explicitly supplies
    g_l=0.294695, matching the existing value. Credit this as provider-normalized
    main-recipe evidence; the PDF supplies the quoted batch amount. API volume=1018
    ml and 1000 ml listed water do not establish a measured final-volume claim.",
    "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api1100Rest",
    "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256":
    "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256":
    "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at":
    "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.294695,\n                        \"mmol_l\":
    5.50936,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 5-5", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   NH4Cl                                                    0.30        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject":
    "NaCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "6.87623",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "6.87623",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe;
    provider normalization", "interpretation": "The current API explicitly supplies
    g_l=6.87623, matching the existing value. Credit this as provider-normalized main-recipe
    evidence; the PDF supplies the quoted batch amount. API volume=1018 ml and 1000
    ml listed water do not establish a measured final-volume claim.", "sources": [{"locator":
    "$.data.solutions[0].recipe[3]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 7,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 6.87623,\n                        \"mmol_l\":
    117.663,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 6-6", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   NaCl                                                     7.00        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q5", "subject":
    "MgCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "3.04519",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "3.04519",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe;
    provider normalization", "interpretation": "The current API explicitly supplies
    g_l=3.04519, matching the existing value. Credit this as provider-normalized main-recipe
    evidence; the PDF supplies the quoted batch amount. API volume=1018 ml and 1000
    ml listed water do not establish a measured final-volume claim.", "sources": [{"locator":
    "$.data.solutions[0].recipe[6]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 3.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.04519,\n                        \"mmol_l\":
    14.9786,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 9-9", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   MgCl2
    x 6 H2O                                            3.10        g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q6", "subject": "KCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path":
    "ingredients[5].concentration", "original": {"value": "0.491159", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.491159",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe;
    provider normalization", "interpretation": "The current API explicitly supplies
    g_l=0.491159, matching the existing value. Credit this as provider-normalized
    main-recipe evidence; the PDF supplies the quoted batch amount. API volume=1018
    ml and 1000 ml listed water do not establish a measured final-volume claim.",
    "sources": [{"locator": "$.data.solutions[0].recipe[7]", "source_key": "api1100Rest",
    "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256":
    "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256":
    "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at":
    "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.491159,\n                        \"mmol_l\":
    6.58832,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 10-10", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   KCl                                                      0.50        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q7", "subject":
    "CaCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.15", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.15", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Main DSM1100 recipe; provider
    normalization", "interpretation": "Both current PDF and API explicitly give 0.15
    ml, without solution strength or g_l. The local 0.15 G_PER_L is dimensionally
    unsupported. Preserve the source inconsistency and request source clarification;
    do not silently change ml to g or infer density.", "sources": [{"locator": "$.data.solutions[0].recipe[8]",
    "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.15,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 11-11", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   CaCl2
    x 2 H2O                                            0.15       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q8", "subject": "Yeast extract",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "0.491159",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "0.491159",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe;
    provider normalization", "interpretation": "The current API explicitly supplies
    g_l=0.491159, matching the existing value. Credit this as provider-normalized
    main-recipe evidence; the PDF supplies the quoted batch amount. API volume=1018
    ml and 1000 ml listed water do not establish a measured final-volume claim.",
    "sources": [{"locator": "$.data.solutions[0].recipe[9]", "source_key": "api1100Rest",
    "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256":
    "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256":
    "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at":
    "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.491159,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text physical LF lines 12-12", "source_key": "dsm1100", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256":
    "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256":
    "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at":
    "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Yeast extract                                            0.50        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject":
    "Sodium resazurin", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.000491159",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.000491159",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe;
    provider normalization", "interpretation": "The current API explicitly supplies
    g_l=0.000491159, matching the existing value. Credit this as provider-normalized
    main-recipe evidence; the PDF supplies the quoted batch amount. API volume=1018
    ml and 1000 ml listed water do not establish a measured final-volume claim. The
    primary 0.5 ml of 0.1% w/v is a separate stock addition; retain that dose and
    strength rather than replacing it solely with the derived rate.", "sources": [{"locator":
    "$.data.solutions[0].recipe[10]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000491159,\n                        \"mmol_l\": 0.00195548,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text physical LF lines 13-13", "source_key": "dsm1100", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256":
    "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256":
    "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at":
    "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Sodium resazurin (0.1%
    w/v)                              0.50       ml", "quote_representation": "captured
    extracted text"}]}, {"decision_id": "q10", "subject": "NaHCO3", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path":
    "ingredients[9].concentration", "original": {"value": "1.47348", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "1.47348",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe;
    provider normalization", "interpretation": "The current API explicitly supplies
    g_l=1.47348, matching the existing value. Credit this as provider-normalized main-recipe
    evidence; the PDF supplies the quoted batch amount. API volume=1018 ml and 1000
    ml listed water do not establish a measured final-volume claim.", "sources": [{"locator":
    "$.data.solutions[0].recipe[11]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.47348,\n                        \"mmol_l\":
    17.5399,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 14-14", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   NaHCO3                                                   1.50        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q11", "subject":
    "Na-L-lactate", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "1.96464",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "1.96464",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main DSM1100 recipe;
    provider normalization", "interpretation": "The current API explicitly supplies
    g_l=1.96464, matching the existing value. Credit this as provider-normalized main-recipe
    evidence; the PDF supplies the quoted batch amount. API volume=1018 ml and 1000
    ml listed water do not establish a measured final-volume claim.", "sources": [{"locator":
    "$.data.solutions[0].recipe[12]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Na-L-lactate\",\n                        \"compound_id\":
    265,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.96464,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text physical LF lines 15-15", "source_key": "dsm1100", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf", "source_raw_sha256":
    "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a", "source_text_sha256":
    "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278", "accessed_at":
    "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Na-L-lactate                                             2.00        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q12", "subject":
    "Na2-EDTA x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "5.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "5.2", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly
    as main ingredient", "interpretation": "The existing 5.2 G_PER_L is supported
    only within Trace element solution SL-11, not as an undiluted main-medium concentration.
    Preserve the source amount/form and reconstruct the stock with its separately
    quoted receiving dose. The source explicitly brings this stock to 1000 ml; mg-to-g
    conversion is therefore supported at stock scope.", "sources": [{"locator": "$.data.solutions[1].recipe[0]",
    "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\":
    676,\n                        \"amount\": 5.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\":
    15.4667,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 30-30", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Na2-EDTA
    x 2 H2O                                         5.20       g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q13", "subject": "FeCl2 x 4 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly
    as main ingredient", "interpretation": "The existing 1.5 G_PER_L is supported
    only within Trace element solution SL-11, not as an undiluted main-medium concentration.
    Preserve the source amount/form and reconstruct the stock with its separately
    quoted receiving dose. The source explicitly brings this stock to 1000 ml; mg-to-g
    conversion is therefore supported at stock scope.", "sources": [{"locator": "$.data.solutions[1].recipe[1]",
    "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 31-31", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   FeCl2
    x 4 H2O                                            1.50       g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q14", "subject": "ZnCl2", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path":
    "ingredients[13].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly
    as main ingredient", "interpretation": "The existing 0.07 G_PER_L is supported
    only within Trace element solution SL-11, not as an undiluted main-medium concentration.
    Preserve the source amount/form and reconstruct the stock with its separately
    quoted receiving dose. The source explicitly brings this stock to 1000 ml; mg-to-g
    conversion is therefore supported at stock scope.", "sources": [{"locator": "$.data.solutions[1].recipe[2]",
    "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 32-32", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   ZnCl2                                                   70.00      mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q15", "subject":
    "MnCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly
    as main ingredient", "interpretation": "The existing 0.1 G_PER_L is supported
    only within Trace element solution SL-11, not as an undiluted main-medium concentration.
    Preserve the source amount/form and reconstruct the stock with its separately
    quoted receiving dose. The source explicitly brings this stock to 1000 ml; mg-to-g
    conversion is therefore supported at stock scope.", "sources": [{"locator": "$.data.solutions[1].recipe[3]",
    "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 33-33", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   MnCl2
    x 4 H2O                                          100.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q16", "subject": "H3BO3", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path":
    "ingredients[15].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "0.006",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented
    incorrectly as main ingredient", "interpretation": "The existing 0.006 G_PER_L
    is supported only within Trace element solution SL-11, not as an undiluted main-medium
    concentration. Preserve the source amount/form and reconstruct the stock with
    its separately quoted receiving dose. The source explicitly brings this stock
    to 1000 ml; mg-to-g conversion is therefore supported at stock scope.", "sources":
    [{"locator": "$.data.solutions[1].recipe[4]", "source_key": "api1100Rest", "reference":
    "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 34-34", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   H3BO3                                                    6.00      mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q17", "subject":
    "CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly
    as main ingredient", "interpretation": "The existing 0.19 G_PER_L is supported
    only within Trace element solution SL-11, not as an undiluted main-medium concentration.
    Preserve the source amount/form and reconstruct the stock with its separately
    quoted receiving dose. The source explicitly brings this stock to 1000 ml; mg-to-g
    conversion is therefore supported at stock scope.", "sources": [{"locator": "$.data.solutions[1].recipe[5]",
    "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 35-35", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   CoCl2
    x 6 H2O                                          190.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q18", "subject": "CuCl2 x 2 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.002",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.002",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented
    incorrectly as main ingredient", "interpretation": "The existing 0.002 G_PER_L
    is supported only within Trace element solution SL-11, not as an undiluted main-medium
    concentration. Preserve the source amount/form and reconstruct the stock with
    its separately quoted receiving dose. The source explicitly brings this stock
    to 1000 ml; mg-to-g conversion is therefore supported at stock scope.", "sources":
    [{"locator": "$.data.solutions[1].recipe[6]", "source_key": "api1100Rest", "reference":
    "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 36-36", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   CuCl2
    x 2 H2O                                            2.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q19", "subject": "NiCl2 x 6 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.024",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.024",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented
    incorrectly as main ingredient", "interpretation": "The existing 0.024 G_PER_L
    is supported only within Trace element solution SL-11, not as an undiluted main-medium
    concentration. Preserve the source amount/form and reconstruct the stock with
    its separately quoted receiving dose. The source explicitly brings this stock
    to 1000 ml; mg-to-g conversion is therefore supported at stock scope.", "sources":
    [{"locator": "$.data.solutions[1].recipe[7]", "source_key": "api1100Rest", "reference":
    "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 37-37", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   NiCl2
    x 6 H2O                                           24.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q20", "subject": "Na2MoO4 x 2 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.036",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.036",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented
    incorrectly as main ingredient", "interpretation": "The existing 0.036 G_PER_L
    is supported only within Trace element solution SL-11, not as an undiluted main-medium
    concentration. Preserve the source amount/form and reconstruct the stock with
    its separately quoted receiving dose. The source explicitly brings this stock
    to 1000 ml; mg-to-g conversion is therefore supported at stock scope.", "sources":
    [{"locator": "$.data.solutions[1].recipe[8]", "source_key": "api1100Rest", "reference":
    "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 38-38", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Na2MoO4
    x 2 H2O                                         36.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q21", "subject": "NaOH", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml", "field_path":
    "ingredients[20].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly
    as main ingredient", "interpretation": "The existing 0.5 G_PER_L is supported
    only within Selenite-tungstate solution, not as an undiluted main-medium concentration.
    Preserve the source amount/form and reconstruct the stock with its separately
    quoted receiving dose. The source lists 1000 ml water and the API explicitly supplies
    this stock rate; it does not state a main-medium final volume.", "sources": [{"locator":
    "$.data.solutions[2].recipe[0]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    12.5009,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 55-55", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   NaOH                                                    0.50       g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q22", "subject":
    "Na2SeO3 x 5 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "0.003",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "0.003",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented
    incorrectly as main ingredient", "interpretation": "The existing 0.003 G_PER_L
    is supported only within Selenite-tungstate solution, not as an undiluted main-medium
    concentration. Preserve the source amount/form and reconstruct the stock with
    its separately quoted receiving dose. The source lists 1000 ml water and the API
    explicitly supplies this stock rate; it does not state a main-medium final volume.",
    "sources": [{"locator": "$.data.solutions[2].recipe[1]", "source_key": "api1100Rest",
    "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256":
    "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256":
    "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at":
    "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\":
    0.0114062,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 56-56", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Na2SeO3
    x 5 H2O                                         3.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q23", "subject": "Na2WO4 x 2 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "0.004",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "0.004",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented
    incorrectly as main ingredient", "interpretation": "The existing 0.004 G_PER_L
    is supported only within Selenite-tungstate solution, not as an undiluted main-medium
    concentration. Preserve the source amount/form and reconstruct the stock with
    its separately quoted receiving dose. The source lists 1000 ml water and the API
    explicitly supplies this stock rate; it does not state a main-medium final volume.",
    "sources": [{"locator": "$.data.solutions[2].recipe[2]", "source_key": "api1100Rest",
    "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256":
    "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256":
    "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at":
    "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\":
    0.0121267,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 57-57", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Na2WO4
    x 2 H2O                                          4.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q24", "subject": "Na2S x 9 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "30", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "30", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Separate stock represented incorrectly
    as main ingredient", "interpretation": "The existing 30 G_PER_L is supported only
    within Neutralized sulfide solution 3% (w/v), not as an undiluted main-medium
    concentration. Preserve the source amount/form and reconstruct the stock with
    its separately quoted receiving dose. The primary explicitly labels this stock
    3% (w/v); current API has added g_l=30 to the historical object. The receiving
    dose is 15 ml, not the entire stock.", "sources": [{"locator": "$.data.solutions[3].recipe[0]",
    "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\":
    124.905,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 63-63", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Na2S x
    9 H2O                                            3.00        g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q25", "subject": "HCl placeholder",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "variable",
    "unit": "VARIABLE"}}], "decision": "unsupported", "stage": "Imported pH-buffer
    annotation", "interpretation": "The unquantified placeholder does not supply a
    dose. The historical KOMODO mapping mentions HCl, but its current exact endpoint
    is inaccessible and DSM1100 only says adjust main pH as necessary. Do not promote
    the historical buffer name to a verified source reagent; the sulfide stock instead
    explicitly uses 2 M H2SO4.", "sources": [{"locator": "$.data.solutions[0].steps[0]",
    "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve ingredients (except bicarbonate, lactate and sulfide) and sparge medium
    with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same
    gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add
    lactate and sulfide form sterile anoxic stock solutions prepared under 100% N2
    gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2
    and 20% CO2 gas mixture. Adjust pH of the complete medium to 7.2, if necessary.\"\n                    }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[3].steps[0]",
    "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"step\":
    \"The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl
    rubber septum and a magnetic stirrer. The solution is bubbled with nitrogen gas,
    closed and autoclaved for 15 min. at 121\\u00b0C. After cooling to room temperature
    the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with
    a syringe without opening the bottle.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q26", "subject": "Trace element solution
    SL-11", "local_fields": [], "decision": "add", "stage": "Main receiving dose or
    batch water", "interpretation": "This exact source batch input is absent from
    the structured record. Preserve its absolute unit and stage; do not rename it
    as a measured per-litre final amount.", "sources": [{"locator": "$.data.solutions[0].recipe[4]",
    "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\":
    1474,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 7-7", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Trace
    element solution SL-11                             1.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q27", "subject": "Selenite-tungstate
    solution", "local_fields": [], "decision": "add", "stage": "Main receiving dose
    or batch water", "interpretation": "This exact source batch input is absent from
    the structured record. Preserve its absolute unit and stage; do not rename it
    as a measured per-litre final amount.", "sources": [{"locator": "$.data.solutions[0].recipe[5]",
    "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 8-8", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Selenite-tungstate
    solution                              1.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q28", "subject": "Neutralized sulfide
    solution 3% (w/v)", "local_fields": [], "decision": "add", "stage": "Main receiving
    dose or batch water", "interpretation": "This exact source batch input is absent
    from the structured record. Preserve its absolute unit and stage; do not rename
    it as a measured per-litre final amount.", "sources": [{"locator": "$.data.solutions[0].recipe[13]",
    "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    14,\n                        \"solution\": \"Neutralized sulfide solution 3% (w/v)\",\n                        \"solution_id\":
    34,\n                        \"amount\": 15,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 16-16", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Neutralized
    sulfide solution 3% (w/v)                   15.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q29", "subject": "Distilled water",
    "local_fields": [], "decision": "add", "stage": "Main receiving dose or batch
    water", "interpretation": "This exact source batch input is absent from the structured
    record. Preserve its absolute unit and stage; do not rename it as a measured per-litre
    final amount.", "sources": [{"locator": "$.data.solutions[0].recipe[14]", "source_key":
    "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256":
    "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256":
    "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at":
    "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 17-17", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Distilled
    water                                       1000.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q30", "subject": "Stock water Trace
    element solution SL-11", "local_fields": [], "decision": "add", "stage": "Stock
    solvent", "interpretation": "Retain this stock-specific solvent input separately.
    SL-11 additionally has an explicit final make-up instruction; the other listed
    water volumes are not by themselves measured final volumes.", "sources": [{"locator":
    "$.data.solutions[1].recipe[9]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 39-39", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Distilled
    water                                       1000.00      ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q31", "subject": "Stock water Selenite-tungstate
    solution", "local_fields": [], "decision": "add", "stage": "Stock solvent", "interpretation":
    "Retain this stock-specific solvent input separately. SL-11 additionally has an
    explicit final make-up instruction; the other listed water volumes are not by
    themselves measured final volumes.", "sources": [{"locator": "$.data.solutions[2].recipe[3]",
    "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 58-58", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Distilled
    water                                      1000.00      ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q32", "subject": "Stock water Neutralized
    sulfide solution 3% (w/v)", "local_fields": [], "decision": "add", "stage": "Stock
    solvent", "interpretation": "Retain this stock-specific solvent input separately.
    SL-11 additionally has an explicit final make-up instruction; the other listed
    water volumes are not by themselves measured final volumes.", "sources": [{"locator":
    "$.data.solutions[3].recipe[1]", "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 100,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 64-64", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "   Distilled
    water                                       100.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q33", "subject": "Main pH and anaerobic
    preparation", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml",
    "field_path": "ph_value", "original": 7.2}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml",
    "field_path": "ph_value", "original": 7.2}], "decision": "evidence_only", "stage":
    "Main preparation", "interpretation": "The retained pH 7.2 matches current source.
    Restore the missing staged preparation: 100% N2 for 30–45 min, anoxic dispensing/autoclaving,
    separate sterile lactate/sulfide additions under N2 and bicarbonate under 80%
    N2/20% CO2. The source does not specify a main autoclave duration or temperature
    here.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100", "source_raw_sha256":
    "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "source_text_sha256":
    "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884", "accessed_at":
    "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve ingredients (except bicarbonate, lactate and sulfide) and sparge medium
    with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same
    gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add
    lactate and sulfide form sterile anoxic stock solutions prepared under 100% N2
    gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2
    and 20% CO2 gas mixture. Adjust pH of the complete medium to 7.2, if necessary.\"\n                    }",
    "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical
    LF lines 19-24", "source_key": "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "Dissolve
    ingredients (except bicarbonate, lactate and sulfide) and sparge medium with\n100%
    N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas\natmosphere
    into anoxic Hungate-type tubes or serum vials and autoclave. Add lactate and\nsulfide
    form sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate\nfrom
    a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture.\nAdjust
    pH of the complete medium to 7.2, if necessary.", "quote_representation": "captured
    extracted text"}]}, {"decision_id": "q34", "subject": "SL-11 preparation controls",
    "local_fields": [], "decision": "add", "stage": "SL-11 stock only", "interpretation":
    "Preserve initial 800 ml water, pH 7 with 2 N NaOH, sequential dissolution, final
    pH 6.0 and make-up to 1000 ml. The NaOH titration volume is unquantified; no extra
    main-medium dose is inferred.", "sources": [{"locator": "$.data.solutions[1].steps[0]",
    "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add
    ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally
    adjust pH to 6.0 and bring volume to 1000 ml. \"\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 41-43", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "Dissolve
    EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride.
    After ferrous chloride has dissolved add other compounds. Finally adjust pH to
    6.0\nand bring volume to 1000 ml.", "quote_representation": "captured extracted
    text"}]}, {"decision_id": "q35", "subject": "Neutralized sulfide preparation controls",
    "local_fields": [], "decision": "add", "stage": "Sulfide stock only", "interpretation":
    "Preserve 250 ml vessel capacity separately from the 100 ml water batch, N2 treatment,
    15 min at 121°C, cooling and pH about 7 with sterile 2 M H2SO4. Acid addition
    is dropwise and unquantified. These stock controls do not establish main-medium
    autoclave settings.", "sources": [{"locator": "$.data.solutions[3].steps[0]",
    "source_key": "api1100Rest", "reference": "https://mediadive.dsmz.de/rest/medium/1100",
    "source_raw_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "source_text_sha256": "1a533084f98fb4b1c974f1a91fd09ffdc91d7d29001fc4f018f1307a9bfa0884",
    "accessed_at": "2026-10-28T17:17:36.912797Z", "exact_source_quote": "{\n                        \"step\":
    \"The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl
    rubber septum and a magnetic stirrer. The solution is bubbled with nitrogen gas,
    closed and autoclaved for 15 min. at 121\\u00b0C. After cooling to room temperature
    the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with
    a syringe without opening the bottle.\"\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 66-70", "source_key":
    "dsm1100", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1100.pdf",
    "source_raw_sha256": "dcff812ce2ebf2a596ee62e8d73bd5426c26440b00244a42a8b77c36be34185a",
    "source_text_sha256": "2153ff36a627f6dfb62b3c7ccb3c0a98abf46b3c99af0a056cfb26ec59645278",
    "accessed_at": "2026-10-28T17:17:09.159454Z", "exact_source_quote": "The sulfide
    solution is prepared in a 250 ml screw-capped bottle with a butyl rubber\nseptum
    and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and\nautoclaved
    for 15 min. at 121°C. After cooling to room temperature the pH is adjusted to\nabout
    7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the\nbottle.",
    "quote_representation": "captured extracted text"}]}], "local_field_census_reference":
    "REVIEW_WORK/batch073/record04/grounding-inventory.json", "source_only_gaps_are_explicit":
    true, "note": "Batch amounts, provider normalization, stock composition, working
    dose and preparation controls are separate. No source edits or automatic curation
    performed."}'
- assessment_id: a4
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/DESULFACINUM_MEDIUM.yaml: primary 24/25, secondary
    23/25; data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml: primary
    24/25, secondary 23/25. These are ingredient-instance linkage fractions, not accuracy
    scores. Solution terms are audited separately. Every actually asserted CHEBI term
    is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric
    legacy MediaIngredientMech mentions occur across the complete selected documents,
    with exact locators in the inventory; NNNNNN is a historical placeholder, not
    an ID. Complex commercial/product components are not forced to pure-compound IDs.'
  target_ids:
  - CultureMech:003800
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
  - CultureMech:003800
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
  - CultureMech:003800
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-003800-flattened-stocks-and-unit-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Stock composition and unsupported calcium units obscure the main recipe
  description: Thirteen stock-component rates are flattened into main ingredients.
    The SL-11, selenite-tungstate and neutralized sulfide receiving doses, stock solvents
    and preparation are missing. Main provider rates are credited individually; the
    historical blanket conflict classification is too broad. Calcium is specifically
    unsupported because both current primary and API say 0.15 ml without stock strength,
    whereas the record says 0.15 G_PER_L.
  target_ids:
  - CultureMech:003800
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  - evidence
  evidence_ids:
  - dsm1100
  - api1100Rest
  - history-auth
  rule_id: source-stage-and-dimensional-basis
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-003800-anoxic-preparation-context
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Aerobic annotation contradicts the primary anaerobic preparation
  description: 'Both selected layers retain Aerobic: Yes but lack the source anoxic
    preparation and its separate supplementation stages. The existing pH 7.2 is correct.
    Stock-specific acid, vessel and autoclave controls must not be transferred to
    the main medium.'
  target_ids:
  - CultureMech:003800
  field_paths:
  - notes
  - preparation_steps
  - evidence
  evidence_ids:
  - dsm1100
  - api1100Rest
  rule_id: source-preparation-and-atmosphere-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-003800-nickel-hydrate-and-sodium-resazurin-form
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
  - CultureMech:003800
  field_paths:
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  - ingredients[8].term
  evidence_ids:
  - dsm1100
  - chebi34887
  - chebi8806
  - grounding
  rule_id: supplied-chemical-form-correspondence
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-003800-append-only-provenance-and-writers
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical source annotations need bounded authentication and valid future
    timestamps
  description: The current record has no attached formulation claims despite prior
    review narratives. Stored KOMODO import history contains literal .fZ and enrichment
    timestamps lack timezone; preserve those historical bytes. Current API objects
    are compared individually because its sulfide object now includes g_l/mmol_l absent
    from the older payload. Current exact KOMODO access is HTTP 403; historical catalogue
    bytes and execution times remain unverified.
  target_ids:
  - CultureMech:003800
  field_paths:
  - evidence
  - curation_history
  evidence_ids:
  - history-auth
  - komodo1100
  rule_id: append-only-source-provenance
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: current import timestamp writer
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/enrich/dsmz_resolver.py
    role: current enrichment timestamp and preparation propagation writer
actions:
- action_id: action1
  description: Reconstruct source-specific stocks and receiving doses, retain all
    directly supported main provider rates with their stated basis, and preserve the
    unresolved calcium volume/unit issue for source clarification. Do not infer final
    concentrations from listed water or silently replace ml with g.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003800
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml
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
  description: Preserve the correct pH, replace the contradicted atmosphere annotation
    with source-scoped preparation and attach stage-specific root evidence. Keep unquantified
    titrants unresolved.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003800
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml
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
  - CultureMech:003800
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml
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
  description: Attach fresh claim-scoped evidence and append a new verified corrective
    event with the actual current date. Preserve malformed historical events unchanged;
    fix future timestamp generation in the exact inspected writers and retain the
    current conservative merge safeguards.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:003800
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1100_DESULFACINUM_medium.yaml
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
  - Verify future KOMODO importer and DSMZ enrichment events use actual UTC timestamps
    with timezone, while original historical event bytes remain unchanged.
limitations:
- Exact historical KOMODO MediaInfo=1100 returned HTTP 403. Failed guessed /api/medium
  routes are preserved separately from successful official /rest/medium captures.
- The PDF and API both label calcium as 0.15 ml without a strength; no mass, density
  or corrected source unit is invented.
- Listed 1000 ml main water and API volume metadata do not establish an explicit final
  medium volume.
- CHEBI:132194 was an unrelated discovery lead (glycine-d5), explicitly excluded.
  CHEBI:53542 supports nickel chloride hexahydrate; the exact sodium-resazurin replacement
  remains unresolved.
- Current code behavior and individually matching historical objects do not authenticate
  historical execution or separately cited KOMODO catalogue bytes.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
