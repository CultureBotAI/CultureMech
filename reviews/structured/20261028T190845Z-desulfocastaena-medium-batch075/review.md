# Scientific review of desulfocastaena_medium

- Review: 20261028T190845Z-desulfocastaena-medium-batch075
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T18:55:59.671554Z
- Finished UTC: 2026-10-28T19:08:45.741811Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM385 identity, pH and much of its maintained preparation are supported, but the assembled recipe flattens numerous stocks and combines incompatible HCl quantities. Source-specific atmosphere, stock procedure placement, two supplied-form mappings and evidence provenance require curation.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch075 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001492 | data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml | generated | desulfocastaena_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001492 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:001492 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:001492 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:001492 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact source and maintained contributor boundaries

identity: concern. Targets: CultureMech:001492.

DSM385 current primary and API identify DESULFOCASTAENA. The maintained KOMODO385 contributor carries the older catecholicum label and explicitly cites DSM385, but its exact current historical endpoint is HTTP403. Same-label JCM1257 sibling reports refer to another source and are context-only. Equal ingredient arrays do not remove the contradictory aerobic note or missing preparation.

### Composition and physical classification

consistency: supported. Targets: CultureMech:001492.

DEFINED composition and LIQUID are consistent with the chemically specified source and current API complex_medium:no. These labels do not imply experimental growth or validate flattened stock quantities.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:001492.

Seven complete reports and two exact selected parent rows were read. Historical blanket concentration conflicts are refined by explicit current provider stage/basis; no attached claims are mistaken for the separate historical object matches. The two JCM1257 sibling reports are excluded from target formulation findings. Current conservative merging preserves scientific fields and rejects incompatible formulations. Inspected writer behavior is described separately by exact file and function; it does not prove historical execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:001492.

All 102 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:001492", "selected_concentration_field_count": 102, "selected_concentration_fields_covered": 102, "decisions": [{"decision_id": "q1", "subject": "Na2SO4", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "3.15126", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "3.15126", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "3.15126", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Solution A, before B-F assembly", "interpretation": "The stored number agrees with the current provider g_l for solution A (declared 952 mL), but its unqualified placement in final-medium ingredients loses that stage. Retain the explicit primary batch amount and qualified provider A rate; do not turn it into a measured final-medium concentration. The sodium-resazurin row is 0.5 mL of an explicitly 0.1% w/v stock.", "sources": [{"locator": "extracted-text physical LF lines 26-26", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Na2SO4                                                   3.00        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[0]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.15126,\n                        \"mmol_l\": 22.1857,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q2", "subject": "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.210084", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.210084", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.210084", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Solution A, before B-F assembly", "interpretation": "The stored number agrees with the current provider g_l for solution A (declared 952 mL), but its unqualified placement in final-medium ingredients loses that stage. Retain the explicit primary batch amount and qualified provider A rate; do not turn it into a measured final-medium concentration. The sodium-resazurin row is 0.5 mL of an explicitly 0.1% w/v stock.", "sources": [{"locator": "extracted-text physical LF lines 27-27", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   KH2PO4                                                   0.20        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[1]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.210084,\n                        \"mmol_l\": 1.54377,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q3", "subject": "NH4Cl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.315126", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.315126", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.315126", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Solution A, before B-F assembly", "interpretation": "The stored number agrees with the current provider g_l for solution A (declared 952 mL), but its unqualified placement in final-medium ingredients loses that stage. Retain the explicit primary batch amount and qualified provider A rate; do not turn it into a measured final-medium concentration. The sodium-resazurin row is 0.5 mL of an explicitly 0.1% w/v stock.", "sources": [{"locator": "extracted-text physical LF lines 28-28", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   NH4Cl                                                    0.30        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[2]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.315126,\n                        \"mmol_l\": 5.89131,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q4", "subject": "NaCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "7.35294", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "7.35294", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "7.35294", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Solution A, before B-F assembly", "interpretation": "The stored number agrees with the current provider g_l for solution A (declared 952 mL), but its unqualified placement in final-medium ingredients loses that stage. Retain the explicit primary batch amount and qualified provider A rate; do not turn it into a measured final-medium concentration. The sodium-resazurin row is 0.5 mL of an explicitly 0.1% w/v stock.", "sources": [{"locator": "extracted-text physical LF lines 29-29", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   NaCl                                                     7.00        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[3]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 7,\n                        \"unit\": \"g\",\n                        \"g_l\": 7.35294,\n                        \"mmol_l\": 125.82,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q5", "subject": "MgCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "1.36555", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "1.36555", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "1.36555", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Solution A, before B-F assembly", "interpretation": "The stored number agrees with the current provider g_l for solution A (declared 952 mL), but its unqualified placement in final-medium ingredients loses that stage. Retain the explicit primary batch amount and qualified provider A rate; do not turn it into a measured final-medium concentration. The sodium-resazurin row is 0.5 mL of an explicitly 0.1% w/v stock.", "sources": [{"locator": "extracted-text physical LF lines 30-30", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   MgCl2 x 6 H2O                                            1.30        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[4]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 1.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.36555,\n                        \"mmol_l\": 6.7168,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q6", "subject": "KCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.52521", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.52521", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.52521", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Solution A, before B-F assembly", "interpretation": "The stored number agrees with the current provider g_l for solution A (declared 952 mL), but its unqualified placement in final-medium ingredients loses that stage. Retain the explicit primary batch amount and qualified provider A rate; do not turn it into a measured final-medium concentration. The sodium-resazurin row is 0.5 mL of an explicitly 0.1% w/v stock.", "sources": [{"locator": "extracted-text physical LF lines 31-31", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   KCl                                                      0.50        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[5]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.52521,\n                        \"mmol_l\": 7.04507,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q7", "subject": "CaCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.157563", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.157563", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.157563", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Solution A, before B-F assembly", "interpretation": "The stored number agrees with the current provider g_l for solution A (declared 952 mL), but its unqualified placement in final-medium ingredients loses that stage. Retain the explicit primary batch amount and qualified provider A rate; do not turn it into a measured final-medium concentration. The sodium-resazurin row is 0.5 mL of an explicitly 0.1% w/v stock.", "sources": [{"locator": "extracted-text physical LF lines 32-32", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   CaCl2 x 2 H2O                                            0.15        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[6]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.157563,\n                        \"mmol_l\": 1.07175,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q8", "subject": "Sodium resazurin", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.00052521", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.00052521", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.00052521", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Solution A, before B-F assembly", "interpretation": "The stored number agrees with the current provider g_l for solution A (declared 952 mL), but its unqualified placement in final-medium ingredients loses that stage. Retain the explicit primary batch amount and qualified provider A rate; do not turn it into a measured final-medium concentration. The sodium-resazurin row is 0.5 mL of an explicitly 0.1% w/v stock.", "sources": [{"locator": "extracted-text physical LF lines 35-35", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Sodium resazurin (0.1% w/v)                              0.50       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[9]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00052521,\n                        \"mmol_l\": 0.00209105,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q9", "subject": "Na2CO3", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "50", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separate solution B", "interpretation": "The numeric g_l is explicitly supported for this separate stock by the provider, not as a final-medium ingredient rate. Preserve the primary batch mass, its separately listed water and receiving aliquot; restore stock structure before any final-volume calculation.", "sources": [{"locator": "extracted-text physical LF lines 41-41", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Na2CO3                                                   1.00        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[2].recipe[0]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\": 471.752,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q10", "subject": "Na-benzoate", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "40", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "40", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "40", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separate solution C", "interpretation": "The numeric g_l is explicitly supported for this separate stock by the provider, not as a final-medium ingredient rate. Preserve the primary batch mass, its separately listed water and receiving aliquot; restore stock structure before any final-volume calculation.", "sources": [{"locator": "extracted-text physical LF lines 47-47", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Na-benzoate                                              0.40        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[0]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na-benzoate\",\n                        \"compound_id\": 295,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 40,\n                        \"mmol_l\": 277.579,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q11", "subject": "Pyrocatechol", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "6", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "6", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "6", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separate solution D", "interpretation": "The numeric g_l is explicitly supported for this separate stock by the provider, not as a final-medium ingredient rate. Preserve the primary batch mass, its separately listed water and receiving aliquot; restore stock structure before any final-volume calculation.", "sources": [{"locator": "extracted-text physical LF lines 61-61", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Pyrocatechol                                                0.06        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[4].recipe[0]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Pyrocatechol\",\n                        \"compound_id\": 439,\n                        \"amount\": 0.06,\n                        \"unit\": \"g\",\n                        \"g_l\": 6,\n                        \"mmol_l\": 54.491,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q12", "subject": "Na2S x 9 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "40", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "40", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "40", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Separate solution F", "interpretation": "The numeric g_l is explicitly supported for this separate stock by the provider, not as a final-medium ingredient rate. Preserve the primary batch mass, its separately listed water and receiving aliquot; restore stock structure before any final-volume calculation.", "sources": [{"locator": "extracted-text physical LF lines 73-73", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Na2S x 9 H2O                                                0.40        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[6].recipe[0]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 40,\n                        \"mmol_l\": 166.54,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q13", "subject": "HCl from two chemically distinct uses", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "2.56", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "2.56", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "2.56", "unit": "G_PER_L"}}, {"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[11].notes", "original": " [Merged 2 duplicates: 0.06, 2.5]"}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[11].notes", "original": " [Merged 2 duplicates: 0.06, 2.5]"}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[11].notes", "original": " [Merged 2 duplicates: 0.06, 2.5]"}], "decision": "correct", "stage": "Solution D acid dose versus SL-10 acid reagent", "interpretation": "The merged 2.56 G_PER_L is an invalid addition of the 0.06 mL 1 N HCl dose in solution D and the provider 2.5 g_l assigned to 10 mL of bare 25% HCl in SL-10. They are different units and stages. Retain two exact source amounts; bare 25% does not establish a mass basis or density. Do not use the summed artifact as either concentration.", "sources": [{"locator": "extracted-text physical LF lines 61-63", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Pyrocatechol                                                0.06        g\n   HCl (1 N)                                                   0.06       ml\n   Distilled water                                            10.00       ml", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 87-87", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   HCl (25%)                                                  10.00      ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[4].recipe[1]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"1 N\",\n                        \"amount\": 0.06,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[8].recipe[0]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q14", "subject": "NaOH", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Selenite-tungstate stock", "interpretation": "The provider explicitly reports this stock g_l and the primary gives the corresponding batch mass with 1000 mL water. The value is not the dose in the completed medium. Preserve stock identity and receiving dose; do not infer a measured final volume from a water charge.", "sources": [{"locator": "extracted-text physical LF lines 79-79", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   NaOH                                                       0.50        g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[7].recipe[0]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 82-82", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled water                                         1000.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q15", "subject": "Na2SeO3 x 5 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Selenite-tungstate stock", "interpretation": "The provider explicitly reports this stock g_l and the primary gives the corresponding batch mass with 1000 mL water. The value is not the dose in the completed medium. Preserve stock identity and receiving dose; do not infer a measured final volume from a water charge.", "sources": [{"locator": "extracted-text physical LF lines 80-80", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Na2SeO3 x 5 H2O                                            3.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[7].recipe[1]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 82-82", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled water                                         1000.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q16", "subject": "Na2WO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.004", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.004", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.004", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Selenite-tungstate stock", "interpretation": "The provider explicitly reports this stock g_l and the primary gives the corresponding batch mass with 1000 mL water. The value is not the dose in the completed medium. Preserve stock identity and receiving dose; do not infer a measured final volume from a water charge.", "sources": [{"locator": "extracted-text physical LF lines 81-81", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Na2WO4 x 2 H2O                                             4.00       mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[7].recipe[2]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 82-82", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled water                                         1000.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q17", "subject": "FeCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "correct", "stage": "SL-10 stock with explicit final 1000 mL", "interpretation": "The stock value is supported by its primary batch mass and explicit make-up to 1000 mL, but its flattened final-medium placement is wrong. Retain this stock basis and its 1 mL addition into A; supplied hydrate identity is assessed separately.", "sources": [{"locator": "extracted-text physical LF lines 88-88", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   FeCl2 x 4 H2O                                               1.50       g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 98-99", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[8].recipe[1]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q18", "subject": "ZnCl2", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}], "decision": "correct", "stage": "SL-10 stock with explicit final 1000 mL", "interpretation": "The stock value is supported by its primary batch mass and explicit make-up to 1000 mL, but its flattened final-medium placement is wrong. Retain this stock basis and its 1 mL addition into A; supplied hydrate identity is assessed separately.", "sources": [{"locator": "extracted-text physical LF lines 89-89", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   ZnCl2                                                      70.00      mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 98-99", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[8].recipe[2]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q19", "subject": "MnCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "SL-10 stock with explicit final 1000 mL", "interpretation": "The stock value is supported by its primary batch mass and explicit make-up to 1000 mL, but its flattened final-medium placement is wrong. Retain this stock basis and its 1 mL addition into A; supplied hydrate identity is assessed separately.", "sources": [{"locator": "extracted-text physical LF lines 90-90", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   MnCl2 x 4 H2O                                             100.00      mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 98-99", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[8].recipe[3]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q20", "subject": "H3BO3", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}], "decision": "correct", "stage": "SL-10 stock with explicit final 1000 mL", "interpretation": "The stock value is supported by its primary batch mass and explicit make-up to 1000 mL, but its flattened final-medium placement is wrong. Retain this stock basis and its 1 mL addition into A; supplied hydrate identity is assessed separately.", "sources": [{"locator": "extracted-text physical LF lines 91-91", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   H3BO3                                                       6.00      mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 98-99", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[8].recipe[4]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q21", "subject": "CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}], "decision": "correct", "stage": "SL-10 stock with explicit final 1000 mL", "interpretation": "The stock value is supported by its primary batch mass and explicit make-up to 1000 mL, but its flattened final-medium placement is wrong. Retain this stock basis and its 1 mL addition into A; supplied hydrate identity is assessed separately.", "sources": [{"locator": "extracted-text physical LF lines 92-92", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   CoCl2 x 6 H2O                                             190.00      mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 98-99", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[8].recipe[5]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q22", "subject": "CuCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}], "decision": "correct", "stage": "SL-10 stock with explicit final 1000 mL", "interpretation": "The stock value is supported by its primary batch mass and explicit make-up to 1000 mL, but its flattened final-medium placement is wrong. Retain this stock basis and its 1 mL addition into A; supplied hydrate identity is assessed separately.", "sources": [{"locator": "extracted-text physical LF lines 93-93", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   CuCl2 x 2 H2O                                               2.00      mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 98-99", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[8].recipe[6]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q23", "subject": "NiCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}], "decision": "correct", "stage": "SL-10 stock with explicit final 1000 mL", "interpretation": "The stock value is supported by its primary batch mass and explicit make-up to 1000 mL, but its flattened final-medium placement is wrong. Retain this stock basis and its 1 mL addition into A; supplied hydrate identity is assessed separately.", "sources": [{"locator": "extracted-text physical LF lines 94-94", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   NiCl2 x 6 H2O                                              24.00      mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 98-99", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[8].recipe[7]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q24", "subject": "Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}], "decision": "correct", "stage": "SL-10 stock with explicit final 1000 mL", "interpretation": "The stock value is supported by its primary batch mass and explicit make-up to 1000 mL, but its flattened final-medium placement is wrong. Retain this stock basis and its 1 mL addition into A; supplied hydrate identity is assessed separately.", "sources": [{"locator": "extracted-text physical LF lines 95-95", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Na2MoO4 x 2 H2O                                            36.00      mg", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 98-99", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[8].recipe[8]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q25", "subject": "Biotin", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x), received through solution E", "interpretation": "The provider explicitly supports this stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x identity and 1 mL receiving dose; this stock concentration is not a final-medium ingredient concentration. No unsupported final-volume or stereochemical conversion is made.", "sources": [{"locator": "extracted-text physical LF lines 104-104", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Biotin                                                     20.00      mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[9].recipe[0]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q26", "subject": "Folic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x), received through solution E", "interpretation": "The provider explicitly supports this stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x identity and 1 mL receiving dose; this stock concentration is not a final-medium ingredient concentration. No unsupported final-volume or stereochemical conversion is made.", "sources": [{"locator": "extracted-text physical LF lines 105-105", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Folic acid                                                 20.00      mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[9].recipe[1]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q27", "subject": "Pyridoxine hydrochloride", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x), received through solution E", "interpretation": "The provider explicitly supports this stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x identity and 1 mL receiving dose; this stock concentration is not a final-medium ingredient concentration. No unsupported final-volume or stereochemical conversion is made.", "sources": [{"locator": "extracted-text physical LF lines 106-106", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Pyridoxine hydrochloride                                  100.00      mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[9].recipe[2]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q28", "subject": "Thiamine HCl", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x), received through solution E", "interpretation": "The provider explicitly supports this stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x identity and 1 mL receiving dose; this stock concentration is not a final-medium ingredient concentration. No unsupported final-volume or stereochemical conversion is made.", "sources": [{"locator": "extracted-text physical LF lines 107-107", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Thiamine HCl                                               50.00      mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[9].recipe[3]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q29", "subject": "Riboflavin", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x), received through solution E", "interpretation": "The provider explicitly supports this stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x identity and 1 mL receiving dose; this stock concentration is not a final-medium ingredient concentration. No unsupported final-volume or stereochemical conversion is made.", "sources": [{"locator": "extracted-text physical LF lines 116-116", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Riboflavin                         50.00   mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[9].recipe[4]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q30", "subject": "Nicotinic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x), received through solution E", "interpretation": "The provider explicitly supports this stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x identity and 1 mL receiving dose; this stock concentration is not a final-medium ingredient concentration. No unsupported final-volume or stereochemical conversion is made.", "sources": [{"locator": "extracted-text physical LF lines 117-117", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Nicotinic acid                     50.00   mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[9].recipe[5]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q31", "subject": "Calcium D-(+)-pantothenate", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[30].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[30].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[30].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x), received through solution E", "interpretation": "The provider explicitly supports this stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x identity and 1 mL receiving dose; this stock concentration is not a final-medium ingredient concentration. No unsupported final-volume or stereochemical conversion is made.", "sources": [{"locator": "extracted-text physical LF lines 118-118", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Calcium D-(+)-pantothenate         50.00   mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[9].recipe[6]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q32", "subject": "Vitamin B12", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[31].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[31].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[31].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x), received through solution E", "interpretation": "The provider explicitly supports this stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x identity and 1 mL receiving dose; this stock concentration is not a final-medium ingredient concentration. No unsupported final-volume or stereochemical conversion is made.", "sources": [{"locator": "extracted-text physical LF lines 119-119", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Vitamin B12                         1.00   mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[9].recipe[7]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q33", "subject": "p-Aminobenzoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[32].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[32].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[32].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x), received through solution E", "interpretation": "The provider explicitly supports this stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x identity and 1 mL receiving dose; this stock concentration is not a final-medium ingredient concentration. No unsupported final-volume or stereochemical conversion is made.", "sources": [{"locator": "extracted-text physical LF lines 120-120", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   p-Aminobenzoic acid                50.00   mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[9].recipe[8]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q34", "subject": "(DL)-alpha-Lipoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ingredients[33].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ingredients[33].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ingredients[33].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x), received through solution E", "interpretation": "The provider explicitly supports this stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x identity and 1 mL receiving dose; this stock concentration is not a final-medium ingredient concentration. No unsupported final-volume or stereochemical conversion is made.", "sources": [{"locator": "extracted-text physical LF lines 121-121", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   (DL)-alpha-Lipoic acid             50.00   mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[9].recipe[9]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q35", "subject": "Receiving aliquot of solution A", "local_fields": [], "decision": "add", "stage": "Main assembly", "interpretation": "Preserve this exact A-F aliquot in its own receiving recipe. Their nominal sum is 1003 mL, agreeing with provider metadata; it is not an independent measurement of final volume and is not used to overwrite all rates.", "sources": [{"locator": "extracted-text physical LF lines 3-3", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Solution A                                             952.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 770,\n                        \"amount\": 952,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q36", "subject": "Receiving aliquot of solution B", "local_fields": [], "decision": "add", "stage": "Main assembly", "interpretation": "Preserve this exact A-F aliquot in its own receiving recipe. Their nominal sum is 1003 mL, agreeing with provider metadata; it is not an independent measurement of final volume and is not used to overwrite all rates.", "sources": [{"locator": "extracted-text physical LF lines 4-4", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Solution B                                              20.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[1]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\": 772,\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q37", "subject": "Receiving aliquot of solution C", "local_fields": [], "decision": "add", "stage": "Main assembly", "interpretation": "Preserve this exact A-F aliquot in its own receiving recipe. Their nominal sum is 1003 mL, agreeing with provider metadata; it is not an independent measurement of final volume and is not used to overwrite all rates.", "sources": [{"locator": "extracted-text physical LF lines 5-5", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Solution C                                              10.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[2]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 773,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q38", "subject": "Receiving aliquot of solution D", "local_fields": [], "decision": "add", "stage": "Main assembly", "interpretation": "Preserve this exact A-F aliquot in its own receiving recipe. Their nominal sum is 1003 mL, agreeing with provider metadata; it is not an independent measurement of final volume and is not used to overwrite all rates.", "sources": [{"locator": "extracted-text physical LF lines 6-6", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Solution D                                              10.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[3]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\": 774,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q39", "subject": "Receiving aliquot of solution E", "local_fields": [], "decision": "add", "stage": "Main assembly", "interpretation": "Preserve this exact A-F aliquot in its own receiving recipe. Their nominal sum is 1003 mL, agreeing with provider metadata; it is not an independent measurement of final volume and is not used to overwrite all rates.", "sources": [{"locator": "extracted-text physical LF lines 7-7", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Solution E                                               1.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[4]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Solution E\",\n                        \"solution_id\": 775,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q40", "subject": "Receiving aliquot of solution F", "local_fields": [], "decision": "add", "stage": "Main assembly", "interpretation": "Preserve this exact A-F aliquot in its own receiving recipe. Their nominal sum is 1003 mL, agreeing with provider metadata; it is not an independent measurement of final volume and is not used to overwrite all rates.", "sources": [{"locator": "extracted-text physical LF lines 8-8", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Solution F                                              10.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[5]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Solution F\",\n                        \"solution_id\": 776,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q41", "subject": "A water", "local_fields": [], "decision": "add", "stage": "Separate stock or batch solvent", "interpretation": "The explicit water charge belongs to this named preparation. Preserve it separately from receiving aliquots and from any positive make-up instruction; do not sum it into a single water G_PER_L.", "sources": [{"locator": "extracted-text physical LF lines 36-36", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled water                                        950.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[10]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 950,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q42", "subject": "B water", "local_fields": [], "decision": "add", "stage": "Separate stock or batch solvent", "interpretation": "The explicit water charge belongs to this named preparation. Preserve it separately from receiving aliquots and from any positive make-up instruction; do not sum it into a single water G_PER_L.", "sources": [{"locator": "extracted-text physical LF lines 42-42", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled water                                         20.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[2].recipe[1]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q43", "subject": "C water", "local_fields": [], "decision": "add", "stage": "Separate stock or batch solvent", "interpretation": "The explicit water charge belongs to this named preparation. Preserve it separately from receiving aliquots and from any positive make-up instruction; do not sum it into a single water G_PER_L.", "sources": [{"locator": "extracted-text physical LF lines 56-56", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled water                                            10.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[1]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q44", "subject": "D water", "local_fields": [], "decision": "add", "stage": "Separate stock or batch solvent", "interpretation": "The explicit water charge belongs to this named preparation. Preserve it separately from receiving aliquots and from any positive make-up instruction; do not sum it into a single water G_PER_L.", "sources": [{"locator": "extracted-text physical LF lines 63-63", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled water                                            10.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[4].recipe[2]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q45", "subject": "F water", "local_fields": [], "decision": "add", "stage": "Separate stock or batch solvent", "interpretation": "The explicit water charge belongs to this named preparation. Preserve it separately from receiving aliquots and from any positive make-up instruction; do not sum it into a single water G_PER_L.", "sources": [{"locator": "extracted-text physical LF lines 74-74", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled water                                            10.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[6].recipe[1]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q46", "subject": "Se/W water", "local_fields": [], "decision": "add", "stage": "Separate stock or batch solvent", "interpretation": "The explicit water charge belongs to this named preparation. Preserve it separately from receiving aliquots and from any positive make-up instruction; do not sum it into a single water G_PER_L.", "sources": [{"locator": "extracted-text physical LF lines 82-82", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled water                                         1000.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[7].recipe[3]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q47", "subject": "SL-10 water charge", "local_fields": [], "decision": "add", "stage": "Separate stock or batch solvent", "interpretation": "The explicit water charge belongs to this named preparation. Preserve it separately from receiving aliquots and from any positive make-up instruction; do not sum it into a single water G_PER_L.", "sources": [{"locator": "extracted-text physical LF lines 96-96", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled water                                           990.00      ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[8].recipe[9]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q48", "subject": "Wolin water", "local_fields": [], "decision": "add", "stage": "Separate stock or batch solvent", "interpretation": "The explicit water charge belongs to this named preparation. Preserve it separately from receiving aliquots and from any positive make-up instruction; do not sum it into a single water G_PER_L.", "sources": [{"locator": "extracted-text physical LF lines 122-122", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled water                  1000.00   ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[9].recipe[10]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q49", "subject": "SL-10 into A", "local_fields": [], "decision": "add", "stage": "Nested receiving dose", "interpretation": "Retain the exact millilitre dose and source stock identity, without transferring parent or stock concentrations to final-medium ingredients.", "sources": [{"locator": "extracted-text physical LF lines 33-33", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Trace element solution SL-10                             1.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[7]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q50", "subject": "Se/W into A", "local_fields": [], "decision": "add", "stage": "Nested receiving dose", "interpretation": "Retain the exact millilitre dose and source stock identity, without transferring parent or stock concentrations to final-medium ingredients.", "sources": [{"locator": "extracted-text physical LF lines 34-34", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Selenite-tungstate solution                              1.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[8]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q51", "subject": "Wolin10x into E", "local_fields": [], "decision": "add", "stage": "Nested receiving dose", "interpretation": "Retain the exact millilitre dose and source stock identity, without transferring parent or stock concentrations to final-medium ingredients.", "sources": [{"locator": "extracted-text physical LF lines 68-68", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Wolin's vitamin solution (10x)                              1.00       ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[5].recipe[0]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q52", "subject": "Final pH and main staged procedure", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "ph_range", "original": {"min": 6.9, "max": 7.1}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml", "field_path": "ph_range", "original": {"min": 6.9, "max": 7.1}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ph_range", "original": {"min": 6.9, "max": 7.1}}, {"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "preparation_steps[0].description", "original": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas.\r\nSolutions D and E are prepared under 100% N2 gas and sterilized by filtration. The pyrocatechol stock solution has to be prepared always freshly prior to use. To complete the medium appropriate amounts of the solutions B to F are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be at 6.9 - 7.1."}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "preparation_steps[0].description", "original": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas.\r\nSolutions D and E are prepared under 100% N2 gas and sterilized by filtration. The pyrocatechol stock solution has to be prepared always freshly prior to use. To complete the medium appropriate amounts of the solutions B to F are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be at 6.9 - 7.1."}], "decision": "evidence_only", "stage": "A-F assembly", "interpretation": "All three pH ranges and the DSM/generated main procedure are supported. Preserve A gas/pH preconditioning, separate B/C/F autoclaving, D/E filtration and order of addition; no temperature/time is invented where the DSM source does not specify one. KOMODO lacks this procedure and its aerobic note conflicts with the explicit anaerobic source.", "sources": [{"locator": "extracted-text physical LF lines 10-17", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "1. Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at\nleast 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type\ntubes or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2\nand 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas.\nSolutions D and E are prepared under 100% N2 gas and sterilized by filtration. The\npyrocatechol stock solution has to be prepared always freshly prior to use. To complete\nthe medium appropriate amounts of the solutions B to F are added to the sterile solution A\nin the sequence as indicated. Final pH of the medium should be at 6.9 - 7.1.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"step\": \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas.\\r\\nSolutions D and E are prepared under 100% N2 gas and sterilized by filtration. The pyrocatechol stock solution has to be prepared always freshly prior to use. To complete the medium appropriate amounts of the solutions B to F are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be at 6.9 - 7.1.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q53", "subject": "Optional dithionite and transfer inoculum", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "preparation_steps[1].description", "original": "Note: Addition of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v) solution, freshly prepared under N2 and filter-sterilized) may stimulate growth of some strains at the beginning. For transfers use 10 - 20% inoculum."}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "preparation_steps[1].description", "original": "Note: Addition of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v) solution, freshly prepared under N2 and filter-sterilized) may stimulate growth of some strains at the beginning. For transfers use 10 - 20% inoculum."}], "decision": "evidence_only", "stage": "Optional source instruction", "interpretation": "Existing DSM/generated wording faithfully retains optional 10-20 mg/L dithionite from explicit 5% w/v stock and 10-20% inoculum. These remain conditional source directions, not mandatory basal ingredients or new universal growth claims.", "sources": [{"locator": "extracted-text physical LF lines 18-20", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "2. Note: Addition of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v) solution,\nfreshly prepared under N2 and filter-sterilized) may stimulate growth of some strains at the\nbeginning. For transfers use 10 - 20% inoculum.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[1]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"step\": \"Note: Addition of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v) solution, freshly prepared under N2 and filter-sterilized) may stimulate growth of some strains at the beginning. For transfers use 10 - 20% inoculum.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q54", "subject": "SL-10 preparation and positive final-volume control", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "preparation_steps[2].description", "original": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "preparation_steps[2].description", "original": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}], "decision": "correct", "stage": "SL-10 only", "interpretation": "The exact existing instruction is supported but belongs to SL-10 rather than to a generic final-medium preparation step. Its make-up to 1000 mL establishes the SL-10 stock denominator, not the entire assembled medium volume.", "sources": [{"locator": "extracted-text physical LF lines 98-99", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[8].steps[0]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch075/record04/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:001492.

data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml: primary 34/34, secondary 32/34; data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml: primary 34/34, secondary 32/34; data/normalized_yaml/bacterial/desulfocastaena_medium.yaml: primary 34/34, secondary 32/34. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:001492.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:001492.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Separate stocks and receiving doses are flattened into final-medium rates

major / open / confirmed; issue key: culturemech-001492-flattened-stock-stages.

All 34 ingredient concentrations occur at the same root level, although they combine solution-A rates, B/C/D/F stocks, SL-10, Se/W and Wolin10x. The HCl row additionally sums an aliquot expressed in mL and a provider stock mass rate. Exact stock water charges and A-F/nested receiving doses are absent from structured formulation fields. Numeric agreement with provider stock g_l does not support final-medium placement.

### f2: KOMODO atmosphere conflicts and SL-10 preparation is placed at main level

major / open / confirmed; issue key: culturemech-001492-anaerobic-context-and-stock-preparation.

The KOMODO owner says Aerobic: Yes and lacks preparation, while exact DSM385 specifies anaerobic staged assembly. DSM/generated main preparation and pH are already substantially correct, but their third procedure is SL-10-specific. Existing SOURCE_DUPLICATE links should retain source boundaries until this discrepancy is resolved.

### f3: Nickel hydrate and sodium resazurin are linked to different supplied forms

major / open / confirmed; issue key: culturemech-001492-nickel-hydrate-and-sodium-resazurin-form.

Every selected layer names nickel chloride hexahydrate but asserts anhydrous nickel dichloride CHEBI:34887 in both primary and secondary slots. Sodium resazurin is linked through its primary slot to neutral Resazurin CHEBI:8806; there is no asserted resazurin secondary slot to correct. Exact labels pass native checks, but OLS formulas Cl2Ni and C12H7NO4 do not encode the supplied forms. Current MIM matches describe those asserted IDs, not hydrate or sodium-salt equivalence.

### f4: Current source claims are missing and historical timestamps need bounded follow-up

minor / open / confirmed; issue key: culturemech-001492-traceability-and-timestamp-writers.

No selected formulation layer carries claim-level evidence. Historical source objects may equal current provider bytes, but that does not authenticate old access dates. The KOMODO import event retains literal .fZ and the DSM resolver event has no offset. These old events must remain unchanged; current writer defects need separately owned follow-up.

## Recommended Actions And Acceptance Checks

### action1

Reconstruct the exact staged normalized formulation, preserving provider rates only on their explicitly named basis. Split both HCl uses, preserve normality and unresolved percentage basis, add scoped water/receiving doses, and avoid unsupported final-medium recalculation.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Preserve correct main preparation and pH. Correct source-scoped atmosphere metadata, place the SL-10 procedure with that stock, and verify relationship semantics before regeneration; do not copy JCM1257 or infer unavailable KOMODO source details.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Resolve the exact source hydrate and sodium-salt identities against authoritative ontology and MIM records. Use verified supplied-form mappings or retain precise source labels with unresolved mapping; preserve source masses and do not substitute anhydrous molar arithmetic.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Attach precise source claims at valid ingredient/root evidence locations. Preserve malformed historical events and append only verified context with the actual current curation date. Correct future timestamp formatting in the exact inspected import/enrichment writers; verify UTC-Z output and retained historical bytes.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.
- Verify future komodo_web_importer.py and dsmz_resolver.py timestamps use actual timezone-aware UTC-Z values; original historical events remain byte-preserved.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local2 | data/normalized_yaml/bacterial/desulfocastaena_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch075/record04/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch075/record04/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch075/record04/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch075/record04/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| dsm385 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete exact DSM primary PDF text and every rendered page read, including main recipe, separate stock tables and all staged procedures. Physical LF line locators refer to the preserved pdftotext output. |
| api385 | https://mediadive.dsmz.de/rest/medium/385; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current provider identity, solution tables and preparation read. Explicit g_l and declared volumes are credited only on their named provider stock or recipe basis; they are not independent measured final volumes. Provider mmol_l values are not adopted as chemical-form authority. |
| komodo385 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=385; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual HTTP 403 response, not formulation evidence. |
| komodo385list | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual HTTP 403 response, not formulation evidence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4']; mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16494 = lipoic acid; definition ['A heterocyclic thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the 5-position.']; formula ['C8H14O2S2']; mass ['206.332']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17015 = riboflavin; definition ['&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide.']; formula ['C17H20N4O6']; mass ['376.369']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17883 = hydrogen chloride; definition ['A mononuclear parent hydride consisting of covalently bonded hydrogen and chlorine atoms.']; formula ['HCl']; mass ['36.461']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi18135 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:18135; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:18135 = catechol; definition ['A  benzenediol comprising of a benzene core carrying two hydroxy substituents &lt;em&gt;ortho &lt;/em&gt; to each other.']; formula ['C6H6O2']; mass ['110.112']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:27470 = folic acid; definition ['An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6']; mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group.']; formula ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32145 = sodium hydroxide; definition []; formula ['HO.Na']; mass ['39.997']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32149 = sodium sulfate; definition []; formula ['2Na.O4S']; mass ['142.043']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
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
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg']; mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi113455 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:113455; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:113455 = sodium benzoate; definition ['An organic sodium salt resulting from the replacement of the proton from the carboxy group of benzoic acid by a sodium ion.']; formula ['C7H5O2.Na']; mass ['144.105']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131361; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:131361 = disodium selenite pentahydrate; definition ['A hydrate that is the pentahydrate form of disodium selenite.']; formula ['5H2O.2Na.O3Se']; mass ['263.012']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch075/record04/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected and dependency-context term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history1 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/desulfocastaena_medium.yaml.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfocastaena_medium.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history5 | reports/yaml_record_review/20260922T180503Z-desulfobacterium_catecholicum_medium__b7c6198a.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history6 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfobacterium_catecholicum_medium__b7c6198a.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history-auth | REVIEW_WORK/batch075/record04/historical-authentication.json; attached_claims; historical_plan_claims | supports | Actual attached claims in scoped stock sections and historical parent-plan claims are separate populations. Current raw-digest equality and literal or normalized-HTML excerpt equality are independently recorded. No attached formulation claims occur on the selected target or its maintained contributors. Current byte matches do not authenticate historical execution or access dates. |
| writer54 | scripts/apply_mim_groundings.py; target_slot; groundable; apply_to_record | context_only | Current target_slot preserves existing CHEBI assertions; groundable excludes conflicting corpus opinions, and apply_to_record fills ungrounded entries from proposals. This writer does not authenticate source amounts or automatically repair an existing wrong supplied-form ID. |
| writer55 | scripts/assign_culturemech_ids.py; assign_ids; _assign_id_to_file | context_only | Current assign_ids selects records with missing IDs; _assign_id_to_file checks new-ID collisions and appends identifier provenance. Identifier assignment does not authenticate recipe content or demonstrate historical source access. |
| writer56 | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group collapses equal duplicate values without summing them and retains the first conflicting value with a flag. This behavior is distinct from historical summed-amount artifacts and does not authenticate source-specific stock or product structure. |
| writer57 | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients; merge_ingredient_group | context_only | Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group retains the first concentration, flags differing values and selects the first CHEBI. It cannot establish source stages or justify collapsing independent supplemental and product-contained components. |
| writer58 | scripts/migrate_legacy_mim_to_chebi.py; _resolve_chebi; _rewrite_entry | context_only | Current _resolve_chebi reuses current primary CHEBI where available and considers bounded exact-name/synonym matches with a stereo-prefix guard; _rewrite_entry retains unresolved links. Current-row presence is distinct from historical validity and from source-specific supplied-form equivalence. |
| writer59 | scripts/migrate_ph_range.py; parse_ph_range; migrate_one | context_only | Current parse_ph_range retains qualifiers in notes and migrate_one converts only string-valued pH ranges, recording provenance. No particular source range is authenticated by this writer. |
| writer60 | scripts/refill_term_labels.py; refill_text | context_only | Current refill_text replaces term labels using the current exact identifier lookup while preserving other text. Canonical label correspondence is not an independent choice of the correct chemical form for the supplied source reagent. |
| writer61 | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata | context_only | Current DSMZCompositionResolver.merge_composition copies ingredients and solutions, fills pH when absent and copies physical/medium type, but does not copy preparation steps. _add_enrichment_metadata records a naive current timestamp. This explains a present omission risk, not historical execution. |
| writer62 | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current _convert_to_culturemech constructs source notes and default LIQUID with empty ingredients. Its time.strftime format contains %f, which is unsupported here and is consistent with literal .fZ in stored import events. Current code does not authenticate the original retrieval or justify rewriting historical time. |
| writer63 | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps | context_only | Current _parse_api_composition considers the primary recipe, prefers provider g_l when available and excludes four recognized water labels; tap water is not among those exclusions; _is_api_stock_addition distinguishes stock additions. _parse_api_solutions retains separate stock structure. _parse_preparation_steps collects solution prose. These present behaviors do not establish historical execution and cannot justify interpreting flattened stock rates as final-medium concentrations. |
| writer64 | src/culturemech/match/kg_media_matcher.py; extract_recipe_ingredients; find_matches; find_exact_match | context_only | Current extract_recipe_ingredients collects asserted CHEBI/FOODON IDs, find_matches compares set Jaccard and find_exact_match selects the first exact identifier set. Quantities, preparation and ungrounded ingredients are not compared, so an exact set match does not establish formulation identity. |
| writer65 | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current formulation_content retains exact scientific quantities, preparation and other scientific fields; merge_formulation_evidence rejects incompatible projections and unions evidence at matching scopes. A source-equivalence claim is not established by shared ingredient identities. |
| writer66 | src/culturemech/merge/matcher.py; group_formulations; group_recipes | context_only | Current group_formulations calls group_recipes with fail_on_invalid=True and FormulationFingerprinter. Expected standalone or unfingerprintable records are excluded; malformed or unexpected inputs raise. Valid records are grouped by full scientific content. This guard does not retrieve or authenticate source recipes. |
| writer67 | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group routes a single maintained owner with merge metadata; multiple owners pass through conservative merge_formulation_evidence. Regenerating from an unrepaired owner retains its defects. Current conservative behavior is credited and does not establish how the old generated record was produced. |
| writer68 | src/culturemech/validation/schema_defaulter.py; apply_defaults; _fix_ingredient; _fix_solution | context_only | Current apply_defaults, _fix_ingredient and _fix_solution can insert VARIABLE amounts and placeholder names for structural completeness. A default is not evidence for a dose, composition, solution identity or denominator; existing default-history events remain contextual. |
| quantity-inventory | REVIEW_WORK/batch075/record04/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- The exact historical KOMODO recipe and catalogue routes returned HTTP403; current KOMODO content could not be authenticated.
- Provider volumes and g_l are preserved on their declared basis; no measured final-medium volume or bare-percentage mass basis is inferred.
- No experimental growth claim, unrelated JCM1257 recipe transfer, historical execution or historic access-date authentication is made.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T190845Z-desulfocastaena-medium-batch075
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of desulfocastaena_medium
started_at: '2026-10-28T18:55:59.671554Z'
finished_at: '2026-10-28T19:08:45.741811Z'
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
summary: DSM385 identity, pH and much of its maintained preparation are supported,
  but the assembled recipe flattens numerous stocks and combines incompatible HCl
  quantities. Source-specific atmosphere, stock procedure placement, two supplied-form
  mappings and evidence provenance require curation.
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
  - path: data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml
    sha256: c4ecfa988a0841dcb4a08e2ea417942ee4e085777c87e8bd51608ea96f35bcc5
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml
    sha256: b10d1d071da188b10bf9bf13f15c7f599bbb10431d47c7c98ec705a6f26c3a6c
    role: context
  - path: data/normalized_yaml/bacterial/desulfocastaena_medium.yaml
    sha256: 236d1e380e24b99b7518b4750d2ea015aaef7927cc8ae0b92cee64f389dd17df
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json
    sha256: 5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml.md
    sha256: 36bd81e7b7298e3d1cf421aa7abe77a1e95e3114ad9ca779e84d13cd2d4f7e36
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
    sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/desulfocastaena_medium.yaml.md
    sha256: c00b3488492e113272a1041fa18b5a977e85c504832d79ee174dbff94acf41f3
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.md
    sha256: e320cecd4c3aa0e0b90710b30e1a81901669109f2a383e5dff505b3736c94ca9
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfobacterium_catecholicum_medium__b7c6198a.md
    sha256: 2aca7e8cbf740542525d4ab900a7b62c66e2b3ea8b2ec9c330d321c822043103
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.md
    sha256: daeea1bca872bbe12dd296c43074d10f69b03f0d98927df69a56f4d7155fe2e2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfocastaena_medium.md
    sha256: 168c2975a3388abda5177a4429c6e2cf5ef0c5968191cea603b9853cb015f4bb
    role: context
  - path: reports/yaml_record_review/20260922T180503Z-desulfobacterium_catecholicum_medium__b7c6198a.md
    sha256: 33ee9eac27dc59e9cceea998d5d19dcd3a0d6f7692a6380cdba5335278ecf41b
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
  selection: Authoritative batch075 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001492
targets:
- target_id: CultureMech:001492
  path: data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml
  label: desulfocastaena_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocastaena_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:001492
  command: just validate-schema data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:001492
  command: just validate-strict data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml
    --workers 1 --out REVIEW_WORK/batch075/record04/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:001492
  command: just validate-terms data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:001492
  command: just validate-references data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T19:08:45.650026Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: c4ecfa988a0841dcb4a08e2ea417942ee4e085777c87e8bd51608ea96f35bcc5
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T19:08:45.650188Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: b10d1d071da188b10bf9bf13f15c7f599bbb10431d47c7c98ec705a6f26c3a6c
- evidence_id: local2
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfocastaena_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T19:08:45.650220Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 236d1e380e24b99b7518b4750d2ea015aaef7927cc8ae0b92cee64f389dd17df
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch075/record04/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T18:56:00.989236Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 2412cddae5b802596629091265cee67ccc9fb7754f5193f4a6d9fb519d1f66cb
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch075/record04/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T18:56:02.115667Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 36fb82127d7f2ffdd639f7a0366bde37f69563771309a1f360fff6edb97c8dc8
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch075/record04/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T18:56:03.307451Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 7afd8655c86df7d4d29cd444314f01fa6d3851d8cc632eb3089579ba4891fc93
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch075/record04/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T18:56:04.194312Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 078195b1477df1018dea004df92226fe1fabfc8d244d1eb87ab2b86e583fbe9b
- evidence_id: dsm385
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T18:56:02.530917Z'
  support: supports
  summary: Complete exact DSM primary PDF text and every rendered page read, including
    main recipe, separate stock tables and all staged procedures. Physical LF line
    locators refer to the preserved pdftotext output.
  snapshot_sha256: d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22
- evidence_id: api385
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/385
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T18:56:02.531260Z'
  support: supports
  summary: Complete current provider identity, solution tables and preparation read.
    Explicit g_l and declared volumes are credited only on their named provider stock
    or recipe basis; they are not independent measured final volumes. Provider mmol_l
    values are not adopted as chemical-form authority.
  snapshot_sha256: 70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40
- evidence_id: komodo385
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=385
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T18:59:58.519988Z'
  support: unknown
  summary: Actual HTTP 403 response, not formulation evidence.
  snapshot_sha256: 870bb72d2af25226f38d73a8b09ddef881bd9a9811329a0ab5f9676fcc168a9e
- evidence_id: komodo385list
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T18:59:58.520389Z'
  support: unknown
  summary: Actual HTTP 403 response, not formulation evidence.
  snapshot_sha256: a27496573300d986fb5fc9a890834bd62b2f24eb472c278d0c9833c6e3058d75
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
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:59:58.520597Z'
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
  accessed_at: '2026-10-28T18:59:58.724462Z'
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
  accessed_at: '2026-10-28T18:59:58.750350Z'
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
  accessed_at: '2026-10-28T18:59:59.435946Z'
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
  accessed_at: '2026-10-28T18:59:59.480235Z'
  support: supports
  summary: OLS current exact CHEBI:17883 = hydrogen chloride; definition ['A mononuclear
    parent hydride consisting of covalently bonded hydrogen and chlorine atoms.'];
    formula ['HCl']; mass ['36.461']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: e5ab164ef9ff955da1a504ca34ab4d3b69539d9bf721936c9dd563ccbbd0e3b0
- evidence_id: chebi18135
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:18135
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T18:59:59.576662Z'
  support: supports
  summary: OLS current exact CHEBI:18135 = catechol; definition ['A  benzenediol comprising
    of a benzene core carrying two hydroxy substituents <em>ortho </em> to each other.'];
    formula ['C6H6O2']; mass ['110.112']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: d98946436bf9119d52fea3dfb730567656f7889898613b8395ac8247d5946dfa
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
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:00.119385Z'
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
  accessed_at: '2026-10-28T19:00:00.155193Z'
  support: supports
  summary: OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula
    ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: e0c2a85ab7be9313c564f96ee47b87e1bf3e01ad1e9fd627d1dbddced5d068c4
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:00.202203Z'
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
  accessed_at: '2026-10-28T19:00:00.699242Z'
  support: supports
  summary: OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The
    hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 855ea2cf0e89d25ab4a560ab1c2dab6ac861d215bc5473cb4d3a0a2d4cdff438
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
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:00.756219Z'
  support: supports
  summary: OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula
    ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: c3341e7cf8a7ea0768d505265376c1514f161c9048b6e878314e204341d702eb
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:00.993133Z'
  support: supports
  summary: OLS current exact CHEBI:32145 = sodium hydroxide; definition []; formula
    ['HO.Na']; mass ['39.997']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 089212e8c86e2d4a4b145366c8bc67e0056565ef6970dcdc3df63ad20dac234d
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
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:02.190278Z'
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
  accessed_at: '2026-10-28T19:00:02.509503Z'
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
- evidence_id: chebi63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63939
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:02.649044Z'
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
- evidence_id: chebi113455
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:113455
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:03.996799Z'
  support: supports
  summary: OLS current exact CHEBI:113455 = sodium benzoate; definition ['An organic
    sodium salt resulting from the replacement of the proton from the carboxy group
    of benzoic acid by a sodium ion.']; formula ['C7H5O2.Na']; mass ['144.105']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: f007a4cc80c91c67846af3a1ee1e7cbe0a464bf5df01519fcbcc7c77e2d7ae3f
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131361
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:04.329176Z'
  support: supports
  summary: OLS current exact CHEBI:131361 = disodium selenite pentahydrate; definition
    ['A hydrate that is the pentahydrate form of disodium selenite.']; formula ['5H2O.2Na.O3Se'];
    mass ['263.012']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: d88b30f797a300c3935e550a4770cb598bbed342a9c2a343f77bdce496e99db9
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:00:04.495305Z'
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
  reference: REVIEW_WORK/batch075/record04/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T19:08:45.655717Z'
  support: supports
  summary: Complete selected and dependency-context term slots and current packaged
    MIM CSV exact-identifier joins with row locators and metadata commit; includes
    separately scoped dependency context. No fuzzy mapping or historical-validity
    inference.
  snapshot_sha256: c307e33cc3407d784836e694d5a190f525f7d30b525e2b5aa1cf7c517dbc924d
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T19:08:45.696028Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: 36bd81e7b7298e3d1cf421aa7abe77a1e95e3114ad9ca779e84d13cd2d4f7e36
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/desulfocastaena_medium.yaml.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T19:08:45.696075Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: c00b3488492e113272a1041fa18b5a977e85c504832d79ee174dbff94acf41f3
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T19:08:45.696104Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: e320cecd4c3aa0e0b90710b30e1a81901669109f2a383e5dff505b3736c94ca9
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T19:08:45.696129Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: daeea1bca872bbe12dd296c43074d10f69b03f0d98927df69a56f4d7155fe2e2
- evidence_id: history4
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfocastaena_medium.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T19:08:45.696153Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: 168c2975a3388abda5177a4429c6e2cf5ef0c5968191cea603b9853cb015f4bb
- evidence_id: history5
  kind: prior_review
  reference: reports/yaml_record_review/20260922T180503Z-desulfobacterium_catecholicum_medium__b7c6198a.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T19:08:45.696174Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: 33ee9eac27dc59e9cceea998d5d19dcd3a0d6f7692a6380cdba5335278ecf41b
- evidence_id: history6
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfobacterium_catecholicum_medium__b7c6198a.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T19:08:45.696197Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: 2aca7e8cbf740542525d4ab900a7b62c66e2b3ea8b2ec9c330d321c822043103
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch075/record04/historical-authentication.json
  locator: attached_claims; historical_plan_claims
  accessed_at: '2026-10-28T19:08:45.696266Z'
  support: supports
  summary: Actual attached claims in scoped stock sections and historical parent-plan
    claims are separate populations. Current raw-digest equality and literal or normalized-HTML
    excerpt equality are independently recorded. No attached formulation claims occur
    on the selected target or its maintained contributors. Current byte matches do
    not authenticate historical execution or access dates.
  snapshot_sha256: 8402f8de3f3b2b42051aff5b7f110d0cb577a8c2ffd8cf0b21bd7d1a8918e705
- evidence_id: writer54
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: target_slot; groundable; apply_to_record
  accessed_at: '2026-10-28T19:08:45.696342Z'
  support: context_only
  summary: Current target_slot preserves existing CHEBI assertions; groundable excludes
    conflicting corpus opinions, and apply_to_record fills ungrounded entries from
    proposals. This writer does not authenticate source amounts or automatically repair
    an existing wrong supplied-form ID.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: writer55
  kind: record_content
  reference: scripts/assign_culturemech_ids.py
  locator: assign_ids; _assign_id_to_file
  accessed_at: '2026-10-28T19:08:45.696369Z'
  support: context_only
  summary: Current assign_ids selects records with missing IDs; _assign_id_to_file
    checks new-ID collisions and appends identifier provenance. Identifier assignment
    does not authenticate recipe content or demonstrate historical source access.
  snapshot_sha256: 81ed213c52804ae98a8add02730d757595e3287fa7b01bc88aee0e587bbb01e1
- evidence_id: writer56
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T19:08:45.696393Z'
  support: context_only
  summary: Current _merge_ingredient_group collapses equal duplicate values without
    summing them and retains the first conflicting value with a flag. This behavior
    is distinct from historical summed-amount artifacts and does not authenticate
    source-specific stock or product structure.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer57
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: merge_duplicate_ingredients; merge_ingredient_group
  accessed_at: '2026-10-28T19:08:45.696417Z'
  support: context_only
  summary: Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group
    retains the first concentration, flags differing values and selects the first
    CHEBI. It cannot establish source stages or justify collapsing independent supplemental
    and product-contained components.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer58
  kind: record_content
  reference: scripts/migrate_legacy_mim_to_chebi.py
  locator: _resolve_chebi; _rewrite_entry
  accessed_at: '2026-10-28T19:08:45.696447Z'
  support: context_only
  summary: Current _resolve_chebi reuses current primary CHEBI where available and
    considers bounded exact-name/synonym matches with a stereo-prefix guard; _rewrite_entry
    retains unresolved links. Current-row presence is distinct from historical validity
    and from source-specific supplied-form equivalence.
  snapshot_sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
- evidence_id: writer59
  kind: record_content
  reference: scripts/migrate_ph_range.py
  locator: parse_ph_range; migrate_one
  accessed_at: '2026-10-28T19:08:45.696467Z'
  support: context_only
  summary: Current parse_ph_range retains qualifiers in notes and migrate_one converts
    only string-valued pH ranges, recording provenance. No particular source range
    is authenticated by this writer.
  snapshot_sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
- evidence_id: writer60
  kind: record_content
  reference: scripts/refill_term_labels.py
  locator: refill_text
  accessed_at: '2026-10-28T19:08:45.696496Z'
  support: context_only
  summary: Current refill_text replaces term labels using the current exact identifier
    lookup while preserving other text. Canonical label correspondence is not an independent
    choice of the correct chemical form for the supplied source reagent.
  snapshot_sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
- evidence_id: writer61
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata
  accessed_at: '2026-10-28T19:08:45.696533Z'
  support: context_only
  summary: Current DSMZCompositionResolver.merge_composition copies ingredients and
    solutions, fills pH when absent and copies physical/medium type, but does not
    copy preparation steps. _add_enrichment_metadata records a naive current timestamp.
    This explains a present omission risk, not historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer62
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T19:08:45.696558Z'
  support: context_only
  summary: Current _convert_to_culturemech constructs source notes and default LIQUID
    with empty ingredients. Its time.strftime format contains %f, which is unsupported
    here and is consistent with literal .fZ in stored import events. Current code
    does not authenticate the original retrieval or justify rewriting historical time.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer63
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps
  accessed_at: '2026-10-28T19:08:45.696591Z'
  support: context_only
  summary: Current _parse_api_composition considers the primary recipe, prefers provider
    g_l when available and excludes four recognized water labels; tap water is not
    among those exclusions; _is_api_stock_addition distinguishes stock additions.
    _parse_api_solutions retains separate stock structure. _parse_preparation_steps
    collects solution prose. These present behaviors do not establish historical execution
    and cannot justify interpreting flattened stock rates as final-medium concentrations.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer64
  kind: record_content
  reference: src/culturemech/match/kg_media_matcher.py
  locator: extract_recipe_ingredients; find_matches; find_exact_match
  accessed_at: '2026-10-28T19:08:45.696620Z'
  support: context_only
  summary: Current extract_recipe_ingredients collects asserted CHEBI/FOODON IDs,
    find_matches compares set Jaccard and find_exact_match selects the first exact
    identifier set. Quantities, preparation and ungrounded ingredients are not compared,
    so an exact set match does not establish formulation identity.
  snapshot_sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
- evidence_id: writer65
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T19:08:45.696643Z'
  support: context_only
  summary: Current formulation_content retains exact scientific quantities, preparation
    and other scientific fields; merge_formulation_evidence rejects incompatible projections
    and unions evidence at matching scopes. A source-equivalence claim is not established
    by shared ingredient identities.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer66
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations; group_recipes
  accessed_at: '2026-10-28T19:08:45.696665Z'
  support: context_only
  summary: Current group_formulations calls group_recipes with fail_on_invalid=True
    and FormulationFingerprinter. Expected standalone or unfingerprintable records
    are excluded; malformed or unexpected inputs raise. Valid records are grouped
    by full scientific content. This guard does not retrieve or authenticate source
    recipes.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer67
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T19:08:45.696688Z'
  support: context_only
  summary: Current merge_group routes a single maintained owner with merge metadata;
    multiple owners pass through conservative merge_formulation_evidence. Regenerating
    from an unrepaired owner retains its defects. Current conservative behavior is
    credited and does not establish how the old generated record was produced.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer68
  kind: record_content
  reference: src/culturemech/validation/schema_defaulter.py
  locator: apply_defaults; _fix_ingredient; _fix_solution
  accessed_at: '2026-10-28T19:08:45.696713Z'
  support: context_only
  summary: Current apply_defaults, _fix_ingredient and _fix_solution can insert VARIABLE
    amounts and placeholder names for structural completeness. A default is not evidence
    for a dose, composition, solution identity or denominator; existing default-history
    events remain contextual.
  snapshot_sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch075/record04/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T19:08:45.741506Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: 404d8eaf8b31c2b7d4209774e3b133a8d7ee96e593c0aadac221183463b48661
assessments:
- assessment_id: a1
  area: identity
  topic: Exact source and maintained contributor boundaries
  outcome: concern
  summary: DSM385 current primary and API identify DESULFOCASTAENA. The maintained
    KOMODO385 contributor carries the older catecholicum label and explicitly cites
    DSM385, but its exact current historical endpoint is HTTP403. Same-label JCM1257
    sibling reports refer to another source and are context-only. Equal ingredient
    arrays do not remove the contradictory aerobic note or missing preparation.
  target_ids:
  - CultureMech:001492
  evidence_ids:
  - local0
  - local1
  - local2
  - dsm385
  - api385
  - komodo385
  - komodo385list
- assessment_id: a2
  area: consistency
  topic: Composition and physical classification
  outcome: supported
  summary: DEFINED composition and LIQUID are consistent with the chemically specified
    source and current API complex_medium:no. These labels do not imply experimental
    growth or validate flattened stock quantities.
  target_ids:
  - CultureMech:001492
  evidence_ids:
  - dsm385
  - api385
- assessment_id: a3
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: Seven complete reports and two exact selected parent rows were read. Historical
    blanket concentration conflicts are refined by explicit current provider stage/basis;
    no attached claims are mistaken for the separate historical object matches. The
    two JCM1257 sibling reports are excluded from target formulation findings. Current
    conservative merging preserves scientific fields and rejects incompatible formulations.
    Inspected writer behavior is described separately by exact file and function;
    it does not prove historical execution.
  target_ids:
  - CultureMech:001492
  evidence_ids:
  - history-auth
  - writer54
  - writer55
  - writer56
  - writer57
  - writer58
  - writer59
  - writer60
  - writer61
  - writer62
  - writer63
  - writer64
  - writer65
  - writer66
  - writer67
  - writer68
- assessment_id: a4
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 102 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:001492
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:001492",
    "selected_concentration_field_count": 102, "selected_concentration_fields_covered":
    102, "decisions": [{"decision_id": "q1", "subject": "Na2SO4", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[0].concentration", "original": {"value": "3.15126", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "3.15126",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "3.15126",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "Solution A, before B-F
    assembly", "interpretation": "The stored number agrees with the current provider
    g_l for solution A (declared 952 mL), but its unqualified placement in final-medium
    ingredients loses that stage. Retain the explicit primary batch amount and qualified
    provider A rate; do not turn it into a measured final-medium concentration. The
    sodium-resazurin row is 0.5 mL of an explicitly 0.1% w/v stock.", "sources": [{"locator":
    "extracted-text physical LF lines 26-26", "source_key": "dsm385", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256":
    "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256":
    "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at":
    "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Na2SO4                                                   3.00        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[0]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.15126,\n                        \"mmol_l\":
    22.1857,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q2", "subject": "KH2PO4", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[1].concentration", "original": {"value": "0.210084", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.210084",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.210084",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "Solution A, before B-F
    assembly", "interpretation": "The stored number agrees with the current provider
    g_l for solution A (declared 952 mL), but its unqualified placement in final-medium
    ingredients loses that stage. Retain the explicit primary batch amount and qualified
    provider A rate; do not turn it into a measured final-medium concentration. The
    sodium-resazurin row is 0.5 mL of an explicitly 0.1% w/v stock.", "sources": [{"locator":
    "extracted-text physical LF lines 27-27", "source_key": "dsm385", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256":
    "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256":
    "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at":
    "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   KH2PO4                                                   0.20        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[1]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.210084,\n                        \"mmol_l\":
    1.54377,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q3", "subject": "NH4Cl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[2].concentration", "original": {"value": "0.315126", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.315126",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.315126",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "Solution A, before B-F
    assembly", "interpretation": "The stored number agrees with the current provider
    g_l for solution A (declared 952 mL), but its unqualified placement in final-medium
    ingredients loses that stage. Retain the explicit primary batch amount and qualified
    provider A rate; do not turn it into a measured final-medium concentration. The
    sodium-resazurin row is 0.5 mL of an explicitly 0.1% w/v stock.", "sources": [{"locator":
    "extracted-text physical LF lines 28-28", "source_key": "dsm385", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256":
    "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256":
    "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at":
    "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   NH4Cl                                                    0.30        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[2]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.315126,\n                        \"mmol_l\":
    5.89131,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q4", "subject": "NaCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[3].concentration", "original": {"value": "7.35294", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "7.35294",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "7.35294",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "Solution A, before B-F
    assembly", "interpretation": "The stored number agrees with the current provider
    g_l for solution A (declared 952 mL), but its unqualified placement in final-medium
    ingredients loses that stage. Retain the explicit primary batch amount and qualified
    provider A rate; do not turn it into a measured final-medium concentration. The
    sodium-resazurin row is 0.5 mL of an explicitly 0.1% w/v stock.", "sources": [{"locator":
    "extracted-text physical LF lines 29-29", "source_key": "dsm385", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256":
    "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256":
    "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at":
    "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   NaCl                                                     7.00        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[3]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 7,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 7.35294,\n                        \"mmol_l\":
    125.82,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q5", "subject": "MgCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[4].concentration", "original": {"value": "1.36555", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "1.36555",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "1.36555",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "Solution A, before B-F
    assembly", "interpretation": "The stored number agrees with the current provider
    g_l for solution A (declared 952 mL), but its unqualified placement in final-medium
    ingredients loses that stage. Retain the explicit primary batch amount and qualified
    provider A rate; do not turn it into a measured final-medium concentration. The
    sodium-resazurin row is 0.5 mL of an explicitly 0.1% w/v stock.", "sources": [{"locator":
    "extracted-text physical LF lines 30-30", "source_key": "dsm385", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256":
    "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256":
    "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at":
    "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   MgCl2 x 6 H2O                                            1.30        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[4]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 1.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.36555,\n                        \"mmol_l\":
    6.7168,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q6", "subject": "KCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[5].concentration", "original": {"value": "0.52521", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.52521",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.52521",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "Solution A, before B-F
    assembly", "interpretation": "The stored number agrees with the current provider
    g_l for solution A (declared 952 mL), but its unqualified placement in final-medium
    ingredients loses that stage. Retain the explicit primary batch amount and qualified
    provider A rate; do not turn it into a measured final-medium concentration. The
    sodium-resazurin row is 0.5 mL of an explicitly 0.1% w/v stock.", "sources": [{"locator":
    "extracted-text physical LF lines 31-31", "source_key": "dsm385", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256":
    "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256":
    "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at":
    "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   KCl                                                      0.50        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[5]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.52521,\n                        \"mmol_l\":
    7.04507,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q7", "subject": "CaCl2 x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[6].concentration", "original": {"value": "0.157563", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.157563",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.157563",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "Solution A, before B-F
    assembly", "interpretation": "The stored number agrees with the current provider
    g_l for solution A (declared 952 mL), but its unqualified placement in final-medium
    ingredients loses that stage. Retain the explicit primary batch amount and qualified
    provider A rate; do not turn it into a measured final-medium concentration. The
    sodium-resazurin row is 0.5 mL of an explicitly 0.1% w/v stock.", "sources": [{"locator":
    "extracted-text physical LF lines 32-32", "source_key": "dsm385", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256":
    "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256":
    "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at":
    "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   CaCl2 x 2 H2O                                            0.15        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[6]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.157563,\n                        \"mmol_l\":
    1.07175,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q8", "subject": "Sodium resazurin", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[7].concentration", "original": {"value": "0.00052521", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "0.00052521",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "0.00052521",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "Solution A, before B-F
    assembly", "interpretation": "The stored number agrees with the current provider
    g_l for solution A (declared 952 mL), but its unqualified placement in final-medium
    ingredients loses that stage. Retain the explicit primary batch amount and qualified
    provider A rate; do not turn it into a measured final-medium concentration. The
    sodium-resazurin row is 0.5 mL of an explicitly 0.1% w/v stock.", "sources": [{"locator":
    "extracted-text physical LF lines 35-35", "source_key": "dsm385", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256":
    "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256":
    "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at":
    "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Sodium resazurin (0.1%
    w/v)                              0.50       ml", "quote_representation": "captured
    extracted text"}, {"locator": "$.data.solutions[1].recipe[9]", "source_key": "api385",
    "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at":
    "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.00052521,\n                        \"mmol_l\": 0.00209105,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q9", "subject": "Na2CO3", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Separate solution B", "interpretation":
    "The numeric g_l is explicitly supported for this separate stock by the provider,
    not as a final-medium ingredient rate. Preserve the primary batch mass, its separately
    listed water and receiving aliquot; restore stock structure before any final-volume
    calculation.", "sources": [{"locator": "extracted-text physical LF lines 41-41",
    "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Na2CO3                                                   1.00        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[2].recipe[0]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\":
    471.752,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q10", "subject": "Na-benzoate", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[9].concentration", "original": {"value": "40", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "40", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "40", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Separate solution C", "interpretation":
    "The numeric g_l is explicitly supported for this separate stock by the provider,
    not as a final-medium ingredient rate. Preserve the primary batch mass, its separately
    listed water and receiving aliquot; restore stock structure before any final-volume
    calculation.", "sources": [{"locator": "extracted-text physical LF lines 47-47",
    "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Na-benzoate                                              0.40        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[0]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na-benzoate\",\n                        \"compound_id\":
    295,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 40,\n                        \"mmol_l\":
    277.579,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q11", "subject": "Pyrocatechol", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[10].concentration", "original": {"value": "6", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "6", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "6", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Separate solution D", "interpretation":
    "The numeric g_l is explicitly supported for this separate stock by the provider,
    not as a final-medium ingredient rate. Preserve the primary batch mass, its separately
    listed water and receiving aliquot; restore stock structure before any final-volume
    calculation.", "sources": [{"locator": "extracted-text physical LF lines 61-61",
    "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Pyrocatechol                                                0.06        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[4].recipe[0]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Pyrocatechol\",\n                        \"compound_id\":
    439,\n                        \"amount\": 0.06,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 6,\n                        \"mmol_l\":
    54.491,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q12", "subject": "Na2S x 9 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[12].concentration", "original": {"value": "40", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "40", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "40", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Separate solution F", "interpretation":
    "The numeric g_l is explicitly supported for this separate stock by the provider,
    not as a final-medium ingredient rate. Preserve the primary batch mass, its separately
    listed water and receiving aliquot; restore stock structure before any final-volume
    calculation.", "sources": [{"locator": "extracted-text physical LF lines 73-73",
    "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Na2S x
    9 H2O                                                0.40        g", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[6].recipe[0]", "source_key":
    "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at":
    "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 40,\n                        \"mmol_l\":
    166.54,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q13", "subject": "HCl from two chemically
    distinct uses", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "2.56", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "2.56", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "2.56", "unit":
    "G_PER_L"}}, {"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml",
    "field_path": "ingredients[11].notes", "original": " [Merged 2 duplicates: 0.06,
    2.5]"}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[11].notes", "original": " [Merged 2 duplicates: 0.06,
    2.5]"}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[11].notes", "original": " [Merged 2 duplicates: 0.06,
    2.5]"}], "decision": "correct", "stage": "Solution D acid dose versus SL-10 acid
    reagent", "interpretation": "The merged 2.56 G_PER_L is an invalid addition of
    the 0.06 mL 1 N HCl dose in solution D and the provider 2.5 g_l assigned to 10
    mL of bare 25% HCl in SL-10. They are different units and stages. Retain two exact
    source amounts; bare 25% does not establish a mass basis or density. Do not use
    the summed artifact as either concentration.", "sources": [{"locator": "extracted-text
    physical LF lines 61-63", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Pyrocatechol                                                0.06        g\n   HCl
    (1 N)                                                   0.06       ml\n   Distilled
    water                                            10.00       ml", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 87-87",
    "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   HCl (25%)                                                  10.00      ml",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[4].recipe[1]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"1 N\",\n                        \"amount\":
    0.06,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "$.data.solutions[8].recipe[0]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q14", "subject": "NaOH", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Selenite-tungstate stock", "interpretation":
    "The provider explicitly reports this stock g_l and the primary gives the corresponding
    batch mass with 1000 mL water. The value is not the dose in the completed medium.
    Preserve stock identity and receiving dose; do not infer a measured final volume
    from a water charge.", "sources": [{"locator": "extracted-text physical LF lines
    79-79", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   NaOH                                                       0.50        g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[7].recipe[0]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    12.5009,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 82-82", "source_key":
    "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled
    water                                         1000.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q15", "subject": "Na2SeO3 x 5 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.003",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.003",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.003",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "Selenite-tungstate stock",
    "interpretation": "The provider explicitly reports this stock g_l and the primary
    gives the corresponding batch mass with 1000 mL water. The value is not the dose
    in the completed medium. Preserve stock identity and receiving dose; do not infer
    a measured final volume from a water charge.", "sources": [{"locator": "extracted-text
    physical LF lines 80-80", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Na2SeO3
    x 5 H2O                                            3.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[7].recipe[1]", "source_key":
    "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at":
    "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\":
    0.0114062,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 82-82", "source_key":
    "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled
    water                                         1000.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q16", "subject": "Na2WO4 x 2 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "0.004",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "0.004",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "0.004",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "Selenite-tungstate stock",
    "interpretation": "The provider explicitly reports this stock g_l and the primary
    gives the corresponding batch mass with 1000 mL water. The value is not the dose
    in the completed medium. Preserve stock identity and receiving dose; do not infer
    a measured final volume from a water charge.", "sources": [{"locator": "extracted-text
    physical LF lines 81-81", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Na2WO4
    x 2 H2O                                             4.00       mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[7].recipe[2]", "source_key":
    "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at":
    "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\":
    0.0121267,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 82-82", "source_key":
    "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled
    water                                         1000.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q17", "subject": "FeCl2 x 4 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "SL-10 stock with explicit final
    1000 mL", "interpretation": "The stock value is supported by its primary batch
    mass and explicit make-up to 1000 mL, but its flattened final-medium placement
    is wrong. Retain this stock basis and its 1 mL addition into A; supplied hydrate
    identity is assessed separately.", "sources": [{"locator": "extracted-text physical
    LF lines 88-88", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   FeCl2
    x 4 H2O                                               1.50       g", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 98-99",
    "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator":
    "$.data.solutions[8].recipe[1]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q18", "subject": "ZnCl2", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[17].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "SL-10 stock with explicit final
    1000 mL", "interpretation": "The stock value is supported by its primary batch
    mass and explicit make-up to 1000 mL, but its flattened final-medium placement
    is wrong. Retain this stock basis and its 1 mL addition into A; supplied hydrate
    identity is assessed separately.", "sources": [{"locator": "extracted-text physical
    LF lines 89-89", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   ZnCl2                                                      70.00      mg",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    physical LF lines 98-99", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator":
    "$.data.solutions[8].recipe[2]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q19", "subject": "MnCl2 x 4 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[18].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "SL-10 stock with explicit final
    1000 mL", "interpretation": "The stock value is supported by its primary batch
    mass and explicit make-up to 1000 mL, but its flattened final-medium placement
    is wrong. Retain this stock basis and its 1 mL addition into A; supplied hydrate
    identity is assessed separately.", "sources": [{"locator": "extracted-text physical
    LF lines 90-90", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   MnCl2
    x 4 H2O                                             100.00      mg", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 98-99",
    "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator":
    "$.data.solutions[8].recipe[3]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q20", "subject": "H3BO3", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[19].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.006",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.006",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "SL-10 stock with explicit
    final 1000 mL", "interpretation": "The stock value is supported by its primary
    batch mass and explicit make-up to 1000 mL, but its flattened final-medium placement
    is wrong. Retain this stock basis and its 1 mL addition into A; supplied hydrate
    identity is assessed separately.", "sources": [{"locator": "extracted-text physical
    LF lines 91-91", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   H3BO3                                                       6.00      mg",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    physical LF lines 98-99", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator":
    "$.data.solutions[8].recipe[4]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q21", "subject": "CoCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[20].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "SL-10 stock with explicit final
    1000 mL", "interpretation": "The stock value is supported by its primary batch
    mass and explicit make-up to 1000 mL, but its flattened final-medium placement
    is wrong. Retain this stock basis and its 1 mL addition into A; supplied hydrate
    identity is assessed separately.", "sources": [{"locator": "extracted-text physical
    LF lines 92-92", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   CoCl2
    x 6 H2O                                             190.00      mg", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 98-99",
    "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator":
    "$.data.solutions[8].recipe[5]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q22", "subject": "CuCl2 x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[21].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "0.002",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "0.002",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "SL-10 stock with explicit
    final 1000 mL", "interpretation": "The stock value is supported by its primary
    batch mass and explicit make-up to 1000 mL, but its flattened final-medium placement
    is wrong. Retain this stock basis and its 1 mL addition into A; supplied hydrate
    identity is assessed separately.", "sources": [{"locator": "extracted-text physical
    LF lines 93-93", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   CuCl2
    x 2 H2O                                               2.00      mg", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 98-99",
    "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator":
    "$.data.solutions[8].recipe[6]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q23", "subject": "NiCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[22].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "0.024",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "0.024",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "SL-10 stock with explicit
    final 1000 mL", "interpretation": "The stock value is supported by its primary
    batch mass and explicit make-up to 1000 mL, but its flattened final-medium placement
    is wrong. Retain this stock basis and its 1 mL addition into A; supplied hydrate
    identity is assessed separately.", "sources": [{"locator": "extracted-text physical
    LF lines 94-94", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   NiCl2
    x 6 H2O                                              24.00      mg", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 98-99",
    "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator":
    "$.data.solutions[8].recipe[7]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q24", "subject": "Na2MoO4 x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[23].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "0.036",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "0.036",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "SL-10 stock with explicit
    final 1000 mL", "interpretation": "The stock value is supported by its primary
    batch mass and explicit make-up to 1000 mL, but its flattened final-medium placement
    is wrong. Retain this stock basis and its 1 mL addition into A; supplied hydrate
    identity is assessed separately.", "sources": [{"locator": "extracted-text physical
    LF lines 95-95", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Na2MoO4
    x 2 H2O                                            36.00      mg", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 98-99",
    "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator":
    "$.data.solutions[8].recipe[8]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q25", "subject": "Biotin", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[24].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x), received
    through solution E", "interpretation": "The provider explicitly supports this
    stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x identity
    and 1 mL receiving dose; this stock concentration is not a final-medium ingredient
    concentration. No unsupported final-volume or stereochemical conversion is made.",
    "sources": [{"locator": "extracted-text physical LF lines 104-104", "source_key":
    "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Biotin                                                     20.00      mg",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[9].recipe[0]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q26", "subject": "Folic acid", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[25].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[25].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[25].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x), received
    through solution E", "interpretation": "The provider explicitly supports this
    stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x identity
    and 1 mL receiving dose; this stock concentration is not a final-medium ingredient
    concentration. No unsupported final-volume or stereochemical conversion is made.",
    "sources": [{"locator": "extracted-text physical LF lines 105-105", "source_key":
    "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Folic
    acid                                                 20.00      mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[9].recipe[1]", "source_key":
    "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at":
    "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q27", "subject": "Pyridoxine hydrochloride",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x), received
    through solution E", "interpretation": "The provider explicitly supports this
    stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x identity
    and 1 mL receiving dose; this stock concentration is not a final-medium ingredient
    concentration. No unsupported final-volume or stereochemical conversion is made.",
    "sources": [{"locator": "extracted-text physical LF lines 106-106", "source_key":
    "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Pyridoxine
    hydrochloride                                  100.00      mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[9].recipe[2]", "source_key":
    "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at":
    "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q28", "subject": "Thiamine HCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[27].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[27].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[27].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x), received
    through solution E", "interpretation": "The provider explicitly supports this
    stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x identity
    and 1 mL receiving dose; this stock concentration is not a final-medium ingredient
    concentration. No unsupported final-volume or stereochemical conversion is made.",
    "sources": [{"locator": "extracted-text physical LF lines 107-107", "source_key":
    "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Thiamine
    HCl                                               50.00      mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[9].recipe[3]", "source_key":
    "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at":
    "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q29", "subject": "Riboflavin", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[28].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[28].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[28].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x), received
    through solution E", "interpretation": "The provider explicitly supports this
    stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x identity
    and 1 mL receiving dose; this stock concentration is not a final-medium ingredient
    concentration. No unsupported final-volume or stereochemical conversion is made.",
    "sources": [{"locator": "extracted-text physical LF lines 116-116", "source_key":
    "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Riboflavin                         50.00   mg",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[9].recipe[4]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q30", "subject": "Nicotinic acid", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[29].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x), received
    through solution E", "interpretation": "The provider explicitly supports this
    stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x identity
    and 1 mL receiving dose; this stock concentration is not a final-medium ingredient
    concentration. No unsupported final-volume or stereochemical conversion is made.",
    "sources": [{"locator": "extracted-text physical LF lines 117-117", "source_key":
    "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Nicotinic
    acid                     50.00   mg", "quote_representation": "captured extracted
    text"}, {"locator": "$.data.solutions[9].recipe[5]", "source_key": "api385", "reference":
    "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q31", "subject": "Calcium D-(+)-pantothenate",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml",
    "field_path": "ingredients[30].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[30].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[30].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x), received
    through solution E", "interpretation": "The provider explicitly supports this
    stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x identity
    and 1 mL receiving dose; this stock concentration is not a final-medium ingredient
    concentration. No unsupported final-volume or stereochemical conversion is made.",
    "sources": [{"locator": "extracted-text physical LF lines 118-118", "source_key":
    "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Calcium
    D-(+)-pantothenate         50.00   mg", "quote_representation": "captured extracted
    text"}, {"locator": "$.data.solutions[9].recipe[6]", "source_key": "api385", "reference":
    "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q32", "subject": "Vitamin B12", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path":
    "ingredients[31].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[31].concentration", "original": {"value": "0.001",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[31].concentration", "original": {"value": "0.001",
    "unit": "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x),
    received through solution E", "interpretation": "The provider explicitly supports
    this stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x
    identity and 1 mL receiving dose; this stock concentration is not a final-medium
    ingredient concentration. No unsupported final-volume or stereochemical conversion
    is made.", "sources": [{"locator": "extracted-text physical LF lines 119-119",
    "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Vitamin
    B12                         1.00   mg", "quote_representation": "captured extracted
    text"}, {"locator": "$.data.solutions[9].recipe[7]", "source_key": "api385", "reference":
    "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q33", "subject":
    "p-Aminobenzoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml",
    "field_path": "ingredients[32].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[32].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[32].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x), received
    through solution E", "interpretation": "The provider explicitly supports this
    stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x identity
    and 1 mL receiving dose; this stock concentration is not a final-medium ingredient
    concentration. No unsupported final-volume or stereochemical conversion is made.",
    "sources": [{"locator": "extracted-text physical LF lines 120-120", "source_key":
    "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   p-Aminobenzoic
    acid                50.00   mg", "quote_representation": "captured extracted text"},
    {"locator": "$.data.solutions[9].recipe[8]", "source_key": "api385", "reference":
    "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q34", "subject": "(DL)-alpha-Lipoic acid",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml",
    "field_path": "ingredients[33].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ingredients[33].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "ingredients[33].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "Wolin vitamin stock (10x), received
    through solution E", "interpretation": "The provider explicitly supports this
    stock g_l and the primary batch mass with 1000 mL water. Preserve the 10x identity
    and 1 mL receiving dose; this stock concentration is not a final-medium ingredient
    concentration. No unsupported final-volume or stereochemical conversion is made.",
    "sources": [{"locator": "extracted-text physical LF lines 121-121", "source_key":
    "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   (DL)-alpha-Lipoic
    acid             50.00   mg", "quote_representation": "captured extracted text"},
    {"locator": "$.data.solutions[9].recipe[9]", "source_key": "api385", "reference":
    "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q35", "subject": "Receiving aliquot of
    solution A", "local_fields": [], "decision": "add", "stage": "Main assembly",
    "interpretation": "Preserve this exact A-F aliquot in its own receiving recipe.
    Their nominal sum is 1003 mL, agreeing with provider metadata; it is not an independent
    measurement of final volume and is not used to overwrite all rates.", "sources":
    [{"locator": "extracted-text physical LF lines 3-3", "source_key": "dsm385", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256":
    "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256":
    "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at":
    "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Solution A                                             952.00       ml",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[0]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\":
    770,\n                        \"amount\": 952,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q36", "subject": "Receiving aliquot of
    solution B", "local_fields": [], "decision": "add", "stage": "Main assembly",
    "interpretation": "Preserve this exact A-F aliquot in its own receiving recipe.
    Their nominal sum is 1003 mL, agreeing with provider metadata; it is not an independent
    measurement of final volume and is not used to overwrite all rates.", "sources":
    [{"locator": "extracted-text physical LF lines 4-4", "source_key": "dsm385", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256":
    "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256":
    "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at":
    "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Solution B                                              20.00       ml",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[1]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\":
    772,\n                        \"amount\": 20,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q37", "subject": "Receiving aliquot of
    solution C", "local_fields": [], "decision": "add", "stage": "Main assembly",
    "interpretation": "Preserve this exact A-F aliquot in its own receiving recipe.
    Their nominal sum is 1003 mL, agreeing with provider metadata; it is not an independent
    measurement of final volume and is not used to overwrite all rates.", "sources":
    [{"locator": "extracted-text physical LF lines 5-5", "source_key": "dsm385", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256":
    "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256":
    "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at":
    "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Solution C                                              10.00       ml",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\":
    773,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q38", "subject": "Receiving aliquot of
    solution D", "local_fields": [], "decision": "add", "stage": "Main assembly",
    "interpretation": "Preserve this exact A-F aliquot in its own receiving recipe.
    Their nominal sum is 1003 mL, agreeing with provider metadata; it is not an independent
    measurement of final volume and is not used to overwrite all rates.", "sources":
    [{"locator": "extracted-text physical LF lines 6-6", "source_key": "dsm385", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256":
    "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256":
    "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at":
    "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Solution D                                              10.00       ml",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[3]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\":
    774,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q39", "subject": "Receiving aliquot of
    solution E", "local_fields": [], "decision": "add", "stage": "Main assembly",
    "interpretation": "Preserve this exact A-F aliquot in its own receiving recipe.
    Their nominal sum is 1003 mL, agreeing with provider metadata; it is not an independent
    measurement of final volume and is not used to overwrite all rates.", "sources":
    [{"locator": "extracted-text physical LF lines 7-7", "source_key": "dsm385", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256":
    "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256":
    "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at":
    "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Solution E                                               1.00       ml",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[4]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Solution E\",\n                        \"solution_id\":
    775,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q40", "subject": "Receiving aliquot of
    solution F", "local_fields": [], "decision": "add", "stage": "Main assembly",
    "interpretation": "Preserve this exact A-F aliquot in its own receiving recipe.
    Their nominal sum is 1003 mL, agreeing with provider metadata; it is not an independent
    measurement of final volume and is not used to overwrite all rates.", "sources":
    [{"locator": "extracted-text physical LF lines 8-8", "source_key": "dsm385", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256":
    "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256":
    "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at":
    "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Solution F                                              10.00       ml",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[5]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Solution F\",\n                        \"solution_id\":
    776,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q41", "subject": "A water", "local_fields":
    [], "decision": "add", "stage": "Separate stock or batch solvent", "interpretation":
    "The explicit water charge belongs to this named preparation. Preserve it separately
    from receiving aliquots and from any positive make-up instruction; do not sum
    it into a single water G_PER_L.", "sources": [{"locator": "extracted-text physical
    LF lines 36-36", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled
    water                                        950.00       ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[10]", "source_key":
    "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at":
    "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 950,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q42", "subject": "B water", "local_fields":
    [], "decision": "add", "stage": "Separate stock or batch solvent", "interpretation":
    "The explicit water charge belongs to this named preparation. Preserve it separately
    from receiving aliquots and from any positive make-up instruction; do not sum
    it into a single water G_PER_L.", "sources": [{"locator": "extracted-text physical
    LF lines 42-42", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled
    water                                         20.00       ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[2].recipe[1]", "source_key":
    "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at":
    "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 20,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q43", "subject": "C water", "local_fields":
    [], "decision": "add", "stage": "Separate stock or batch solvent", "interpretation":
    "The explicit water charge belongs to this named preparation. Preserve it separately
    from receiving aliquots and from any positive make-up instruction; do not sum
    it into a single water G_PER_L.", "sources": [{"locator": "extracted-text physical
    LF lines 56-56", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled
    water                                            10.00       ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[1]", "source_key":
    "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at":
    "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q44", "subject": "D water", "local_fields":
    [], "decision": "add", "stage": "Separate stock or batch solvent", "interpretation":
    "The explicit water charge belongs to this named preparation. Preserve it separately
    from receiving aliquots and from any positive make-up instruction; do not sum
    it into a single water G_PER_L.", "sources": [{"locator": "extracted-text physical
    LF lines 63-63", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled
    water                                            10.00       ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[4].recipe[2]", "source_key":
    "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at":
    "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q45", "subject": "F water", "local_fields":
    [], "decision": "add", "stage": "Separate stock or batch solvent", "interpretation":
    "The explicit water charge belongs to this named preparation. Preserve it separately
    from receiving aliquots and from any positive make-up instruction; do not sum
    it into a single water G_PER_L.", "sources": [{"locator": "extracted-text physical
    LF lines 74-74", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled
    water                                            10.00       ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[6].recipe[1]", "source_key":
    "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at":
    "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q46", "subject": "Se/W water", "local_fields":
    [], "decision": "add", "stage": "Separate stock or batch solvent", "interpretation":
    "The explicit water charge belongs to this named preparation. Preserve it separately
    from receiving aliquots and from any positive make-up instruction; do not sum
    it into a single water G_PER_L.", "sources": [{"locator": "extracted-text physical
    LF lines 82-82", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled
    water                                         1000.00       ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[7].recipe[3]", "source_key":
    "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at":
    "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q47", "subject": "SL-10 water charge",
    "local_fields": [], "decision": "add", "stage": "Separate stock or batch solvent",
    "interpretation": "The explicit water charge belongs to this named preparation.
    Preserve it separately from receiving aliquots and from any positive make-up instruction;
    do not sum it into a single water G_PER_L.", "sources": [{"locator": "extracted-text
    physical LF lines 96-96", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled
    water                                           990.00      ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[8].recipe[9]", "source_key":
    "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at":
    "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 990,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q48", "subject": "Wolin water", "local_fields":
    [], "decision": "add", "stage": "Separate stock or batch solvent", "interpretation":
    "The explicit water charge belongs to this named preparation. Preserve it separately
    from receiving aliquots and from any positive make-up instruction; do not sum
    it into a single water G_PER_L.", "sources": [{"locator": "extracted-text physical
    LF lines 122-122", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Distilled
    water                  1000.00   ml", "quote_representation": "captured extracted
    text"}, {"locator": "$.data.solutions[9].recipe[10]", "source_key": "api385",
    "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at":
    "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q49", "subject": "SL-10 into A", "local_fields":
    [], "decision": "add", "stage": "Nested receiving dose", "interpretation": "Retain
    the exact millilitre dose and source stock identity, without transferring parent
    or stock concentrations to final-medium ingredients.", "sources": [{"locator":
    "extracted-text physical LF lines 33-33", "source_key": "dsm385", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256":
    "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256":
    "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at":
    "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Trace element solution
    SL-10                             1.00       ml", "quote_representation": "captured
    extracted text"}, {"locator": "$.data.solutions[1].recipe[7]", "source_key": "api385",
    "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at":
    "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q50", "subject": "Se/W into A", "local_fields":
    [], "decision": "add", "stage": "Nested receiving dose", "interpretation": "Retain
    the exact millilitre dose and source stock identity, without transferring parent
    or stock concentrations to final-medium ingredients.", "sources": [{"locator":
    "extracted-text physical LF lines 34-34", "source_key": "dsm385", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256":
    "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256":
    "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at":
    "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Selenite-tungstate solution                              1.00       ml",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[1].recipe[8]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q51", "subject": "Wolin10x into E", "local_fields":
    [], "decision": "add", "stage": "Nested receiving dose", "interpretation": "Retain
    the exact millilitre dose and source stock identity, without transferring parent
    or stock concentrations to final-medium ingredients.", "sources": [{"locator":
    "extracted-text physical LF lines 68-68", "source_key": "dsm385", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf", "source_raw_sha256":
    "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22", "source_text_sha256":
    "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018", "accessed_at":
    "2026-10-28T18:56:02.530917Z", "exact_source_quote": "   Wolin''s vitamin solution
    (10x)                              1.00       ml", "quote_representation": "captured
    extracted text"}, {"locator": "$.data.solutions[5].recipe[0]", "source_key": "api385",
    "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at":
    "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q52", "subject": "Final pH and main staged
    procedure", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml",
    "field_path": "ph_range", "original": {"min": 6.9, "max": 7.1}}, {"record_path":
    "data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml",
    "field_path": "ph_range", "original": {"min": 6.9, "max": 7.1}}, {"record_path":
    "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml", "field_path": "ph_range",
    "original": {"min": 6.9, "max": 7.1}}, {"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml",
    "field_path": "preparation_steps[0].description", "original": "Solution A is sparged
    with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then
    distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum
    vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20%
    CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas.\r\nSolutions
    D and E are prepared under 100% N2 gas and sterilized by filtration. The pyrocatechol
    stock solution has to be prepared always freshly prior to use. To complete the
    medium appropriate amounts of the solutions B to F are added to the sterile solution
    A in the sequence as indicated. Final pH of the medium should be at 6.9 - 7.1."},
    {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "preparation_steps[0].description", "original": "Solution A is sparged
    with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then
    distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum
    vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20%
    CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas.\r\nSolutions
    D and E are prepared under 100% N2 gas and sterilized by filtration. The pyrocatechol
    stock solution has to be prepared always freshly prior to use. To complete the
    medium appropriate amounts of the solutions B to F are added to the sterile solution
    A in the sequence as indicated. Final pH of the medium should be at 6.9 - 7.1."}],
    "decision": "evidence_only", "stage": "A-F assembly", "interpretation": "All three
    pH ranges and the DSM/generated main procedure are supported. Preserve A gas/pH
    preconditioning, separate B/C/F autoclaving, D/E filtration and order of addition;
    no temperature/time is invented where the DSM source does not specify one. KOMODO
    lacks this procedure and its aerobic note conflicts with the explicit anaerobic
    source.", "sources": [{"locator": "extracted-text physical LF lines 10-17", "source_key":
    "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "1. Solution
    A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at\nleast
    30 min), then distributed under the same gas atmosphere into anoxic Hungate-type\ntubes
    or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2\nand
    20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas.\nSolutions
    D and E are prepared under 100% N2 gas and sterilized by filtration. The\npyrocatechol
    stock solution has to be prepared always freshly prior to use. To complete\nthe
    medium appropriate amounts of the solutions B to F are added to the sterile solution
    A\nin the sequence as indicated. Final pH of the medium should be at 6.9 - 7.1.",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]",
    "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"step\":
    \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below
    6 (at least 30 min), then distributed under the same gas atmosphere into anoxic
    Hungate-type tubes or serum vials and autoclaved. Solution B is autoclaved separately
    under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under
    100% N2 gas.\\r\\nSolutions D and E are prepared under 100% N2 gas and sterilized
    by filtration. The pyrocatechol stock solution has to be prepared always freshly
    prior to use. To complete the medium appropriate amounts of the solutions B to
    F are added to the sterile solution A in the sequence as indicated. Final pH of
    the medium should be at 6.9 - 7.1.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q53", "subject": "Optional dithionite and
    transfer inoculum", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml",
    "field_path": "preparation_steps[1].description", "original": "Note: Addition
    of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v) solution, freshly
    prepared under N2 and filter-sterilized) may stimulate growth of some strains
    at the beginning. For transfers use 10 - 20% inoculum."}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "preparation_steps[1].description", "original": "Note: Addition
    of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v) solution, freshly
    prepared under N2 and filter-sterilized) may stimulate growth of some strains
    at the beginning. For transfers use 10 - 20% inoculum."}], "decision": "evidence_only",
    "stage": "Optional source instruction", "interpretation": "Existing DSM/generated
    wording faithfully retains optional 10-20 mg/L dithionite from explicit 5% w/v
    stock and 10-20% inoculum. These remain conditional source directions, not mandatory
    basal ingredients or new universal growth claims.", "sources": [{"locator": "extracted-text
    physical LF lines 18-20", "source_key": "dsm385", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "2. Note:
    Addition of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v) solution,\nfreshly
    prepared under N2 and filter-sterilized) may stimulate growth of some strains
    at the\nbeginning. For transfers use 10 - 20% inoculum.", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].steps[1]", "source_key":
    "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385", "source_raw_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "source_text_sha256":
    "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40", "accessed_at":
    "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"step\":
    \"Note: Addition of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v)
    solution, freshly prepared under N2 and filter-sterilized) may stimulate growth
    of some strains at the beginning. For transfers use 10 - 20% inoculum.\"\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q54", "subject":
    "SL-10 preparation and positive final-volume control", "local_fields": [{"record_path":
    "data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml", "field_path": "preparation_steps[2].description",
    "original": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve
    the other salts. Finally make up to 1000.00 ml."}, {"record_path": "data/normalized_yaml/bacterial/desulfocastaena_medium.yaml",
    "field_path": "preparation_steps[2].description", "original": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally
    make up to 1000.00 ml."}], "decision": "correct", "stage": "SL-10 only", "interpretation":
    "The exact existing instruction is supported but belongs to SL-10 rather than
    to a generic final-medium preparation step. Its make-up to 1000 mL establishes
    the SL-10 stock denominator, not the entire assembled medium volume.", "sources":
    [{"locator": "extracted-text physical LF lines 98-99", "source_key": "dsm385",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf",
    "source_raw_sha256": "d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22",
    "source_text_sha256": "f67179727b9e12fa545e5f3b3784796d2cb60fc293a9bacbfbd088eac78b6018",
    "accessed_at": "2026-10-28T18:56:02.530917Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}, {"locator":
    "$.data.solutions[8].steps[0]", "source_key": "api385", "reference": "https://mediadive.dsmz.de/rest/medium/385",
    "source_raw_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "source_text_sha256": "70c6499023b61a499ffbf43df57fe1f52903653e4b92d807fe78af187a5dec40",
    "accessed_at": "2026-10-28T18:56:02.531260Z", "exact_source_quote": "{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation":
    "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch075/record04/grounding-inventory.json",
    "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization,
    stock composition, working dose and preparation controls are separate. No source
    edits or automatic curation performed."}'
- assessment_id: a5
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/DESULFOCASTAENA_MEDIUM.yaml: primary 34/34, secondary
    32/34; data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml:
    primary 34/34, secondary 32/34; data/normalized_yaml/bacterial/desulfocastaena_medium.yaml:
    primary 34/34, secondary 32/34. These are ingredient-instance linkage fractions,
    not accuracy scores. Solution terms are audited separately. Every actually asserted
    CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows.
    0 numeric legacy MediaIngredientMech mentions occur across the complete selected
    documents, with exact locators in the inventory; NNNNNN is a historical placeholder,
    not an ID. Complex commercial/product components are not forced to pure-compound
    IDs.'
  target_ids:
  - CultureMech:001492
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
  - CultureMech:001492
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
  - CultureMech:001492
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-001492-flattened-stock-stages
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Separate stocks and receiving doses are flattened into final-medium rates
  description: All 34 ingredient concentrations occur at the same root level, although
    they combine solution-A rates, B/C/D/F stocks, SL-10, Se/W and Wolin10x. The HCl
    row additionally sums an aliquot expressed in mL and a provider stock mass rate.
    Exact stock water charges and A-F/nested receiving doses are absent from structured
    formulation fields. Numeric agreement with provider stock g_l does not support
    final-medium placement.
  target_ids:
  - CultureMech:001492
  field_paths:
  - ingredients
  - solutions
  - ingredients[11].notes
  evidence_ids:
  - dsm385
  - api385
  rule_id: review-yaml-record/source-stage-and-unit-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocastaena_medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-001492-anaerobic-context-and-stock-preparation
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: KOMODO atmosphere conflicts and SL-10 preparation is placed at main level
  description: 'The KOMODO owner says Aerobic: Yes and lacks preparation, while exact
    DSM385 specifies anaerobic staged assembly. DSM/generated main preparation and
    pH are already substantially correct, but their third procedure is SL-10-specific.
    Existing SOURCE_DUPLICATE links should retain source boundaries until this discrepancy
    is resolved.'
  target_ids:
  - CultureMech:001492
  field_paths:
  - data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml::notes
  - data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml::preparation_steps
  - data/normalized_yaml/bacterial/desulfocastaena_medium.yaml::preparation_steps[2]
  - preparation_steps[2]
  - data/normalized_yaml/bacterial/desulfocastaena_medium.yaml::parent_media
  - data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml::variant_children
  evidence_ids:
  - dsm385
  - api385
  - local1
  - local2
  rule_id: review-yaml-record/source-preparation-and-variant-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocastaena_medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-001492-nickel-hydrate-and-sodium-resazurin-form
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
  - CultureMech:001492
  field_paths:
  - ingredients[22].term
  - ingredients[22].mediaingredientmech_chebi_term
  - ingredients[7].term
  evidence_ids:
  - dsm385
  - chebi34887
  - chebi8806
  - grounding
  rule_id: supplied-chemical-form-correspondence
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocastaena_medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-001492-traceability-and-timestamp-writers
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Current source claims are missing and historical timestamps need bounded
    follow-up
  description: No selected formulation layer carries claim-level evidence. Historical
    source objects may equal current provider bytes, but that does not authenticate
    old access dates. The KOMODO import event retains literal .fZ and the DSM resolver
    event has no offset. These old events must remain unchanged; current writer defects
    need separately owned follow-up.
  target_ids:
  - CultureMech:001492
  field_paths:
  - evidence
  - data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml::curation_history
  - data/normalized_yaml/bacterial/desulfocastaena_medium.yaml::curation_history
  evidence_ids:
  - history-auth
  - grounding
  - dsm385
  - api385
  rule_id: review-yaml-record/evidence-and-timestamp-provenance
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocastaena_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: current import timestamp writer
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/enrich/dsmz_resolver.py
    role: current enrichment timestamp and preparation propagation writer
actions:
- action_id: action1
  description: Reconstruct the exact staged normalized formulation, preserving provider
    rates only on their explicitly named basis. Split both HCl uses, preserve normality
    and unresolved percentage basis, add scoped water/receiving doses, and avoid unsupported
    final-medium recalculation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001492
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocastaena_medium.yaml
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
  description: Preserve correct main preparation and pH. Correct source-scoped atmosphere
    metadata, place the SL-10 procedure with that stock, and verify relationship semantics
    before regeneration; do not copy JCM1257 or infer unavailable KOMODO source details.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001492
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocastaena_medium.yaml
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
  - CultureMech:001492
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocastaena_medium.yaml
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
  description: Attach precise source claims at valid ingredient/root evidence locations.
    Preserve malformed historical events and append only verified context with the
    actual current curation date. Correct future timestamp formatting in the exact
    inspected import/enrichment writers; verify UTC-Z output and retained historical
    bytes.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001492
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_385_DESULFOBACTERIUM_CATECHOLICUM_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocastaena_medium.yaml
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
  - Verify future komodo_web_importer.py and dsmz_resolver.py timestamps use actual
    timezone-aware UTC-Z values; original historical events remain byte-preserved.
limitations:
- The exact historical KOMODO recipe and catalogue routes returned HTTP403; current
  KOMODO content could not be authenticated.
- Provider volumes and g_l are preserved on their declared basis; no measured final-medium
  volume or bare-percentage mass basis is inferred.
- No experimental growth claim, unrelated JCM1257 recipe transfer, historical execution
  or historic access-date authentication is made.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
