# Scientific review of desulfolutivibrio_medium

- Review: 20261028T200326Z-desulfolutivibrio-medium-batch076
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T19:41:00.946512Z
- Finished UTC: 2026-10-28T20:03:26.132461Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The selected record flattens separate DSM386 A–F and stock bases, loses partial owner nesting, and conflates historical386a identity with a distinct current recipe. Correct retained preparation, five nested owner values and supplied hydrates are credited. Remaining preparation/form/provenance defects require scoped curation; current KOMODO and386a API limits prevent full identity authentication.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch076 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001493 | data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml | generated | desulfolutivibrio_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001493 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:001493 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:001493 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:001493 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Distinct DSM386 and historical/current386a identities

identity: concern. Targets: CultureMech:001493.

The DSM386 primary and API agree on a staged Desulfolutivibrio recipe. Historical KOMODO386 is named Desulfovibrio sulfodismutans;386a is named Sulforhabdus, but the current official386a PDF is THIOVIBRIO with a different formulation. Current KOMODO routes are403 and API386a is404. Local SOURCE_DUPLICATE relationships and copied values do not establish equivalence.

### Classification and precise form limits

consistency: supported. Targets: CultureMech:001493.

DEFINED and LIQUID are supported for the chemically specified DSM386 source, whose API says complex_medium no. That is source classification, not experimental growth evidence or proof of historical386a equivalence. Correct hydrate IDs for magnesium, acetate, sulfide, selenite, tungstate and thiamine remain credited. Calcium pantothenate31345 encodes D stereochemistry while the recipe names generic calcium pantothenate; its exact MIM preferred row is MAPPED but D,L and unrelated capsaicin-like synonyms in the index cannot establish source stereochemistry. Preserve that bounded unresolved specificity.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:001493.

Seven complete historical reports and three exact selected plan rows were read. Historical blanket main-rate conflicts are refined by actual source-stage joins, while the386a404 limitation remains. All102 non-null historical API object quotes and corresponding decoded objects match current386 bytes. Two parent digests authenticate the successful386 payload; the third authenticates only an unchanged386a404 payload. Partial stock nesting and retained procedures are credited, without treating composition agreement as independent identity or volume evidence. Current conservative merging preserves scientific fields and rejects incompatible formulations. Inspected writer behavior is described separately by exact file and function; it does not prove historical execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:001493.

All 124 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:001493", "selected_concentration_field_count": 124, "selected_concentration_fields_covered": 124, "decisions": [{"decision_id": "q1", "subject": "KH2PO4 root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "0.212314", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "0.212314", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "0.212314", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "0.212314", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Solution A flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Solution A, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. Provider Solution A volume is 942 ml; its listed rate is distinct from the 1006 ml sum of A–F additions. ", "sources": [{"locator": "$.data.solutions[1].recipe[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.212314,\n                        \"mmol_l\": 1.56016,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 28-28", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   KH2PO4                                                 0.20        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject": "NH4Cl root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.265393", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.265393", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.265393", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.265393", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Solution A flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Solution A, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. Provider Solution A volume is 942 ml; its listed rate is distinct from the 1006 ml sum of A–F additions. ", "sources": [{"locator": "$.data.solutions[1].recipe[1]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.265393,\n                        \"mmol_l\": 4.96154,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 29-29", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   NH4Cl                                                  0.25        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject": "NaCl root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1.06157", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1.06157", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1.06157", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1.06157", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Solution A flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Solution A, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. Provider Solution A volume is 942 ml; its listed rate is distinct from the 1006 ml sum of A–F additions. ", "sources": [{"locator": "$.data.solutions[1].recipe[2]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.06157,\n                        \"mmol_l\": 18.1651,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 30-30", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   NaCl                                                   1.00        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject": "MgCl2 x 6 H2O root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.424628", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.424628", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.424628", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.424628", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Solution A flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Solution A, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. Provider Solution A volume is 942 ml; its listed rate is distinct from the 1006 ml sum of A–F additions. ", "sources": [{"locator": "$.data.solutions[1].recipe[3]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.424628,\n                        \"mmol_l\": 2.08865,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 31-31", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   MgCl2 x 6 H2O                                          0.40        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q5", "subject": "KCl root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.530786", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.530786", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.530786", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.530786", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Solution A flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Solution A, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. Provider Solution A volume is 942 ml; its listed rate is distinct from the 1006 ml sum of A–F additions. ", "sources": [{"locator": "$.data.solutions[1].recipe[4]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.530786,\n                        \"mmol_l\": 7.11986,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 32-32", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   KCl                                                    0.50        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q6", "subject": "CaCl2 x 2 H2O root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.159236", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.159236", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.159236", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.159236", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Solution A flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Solution A, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. Provider Solution A volume is 942 ml; its listed rate is distinct from the 1006 ml sum of A–F additions. ", "sources": [{"locator": "$.data.solutions[1].recipe[5]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.159236,\n                        \"mmol_l\": 1.08313,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 33-33", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   CaCl2 x 2 H2O                                          0.15        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q7", "subject": "Sodium resazurin root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.000530786", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.000530786", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.000530786", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.000530786", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Solution A flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Solution A, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. Provider Solution A volume is 942 ml; its listed rate is distinct from the 1006 ml sum of A–F additions. The 0.50 ml of 0.1% w/v contains 0.00050 g; division by provider 0.942 L gives the listed 0.000530786 g/L on its A basis only. ", "sources": [{"locator": "$.data.solutions[1].recipe[8]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000530786,\n                        \"mmol_l\": 0.00211325,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 36-36", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Sodium resazurin (0.1% w/v)                            0.50       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q8", "subject": "Na2CO3 root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "50", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Solution B flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Solution B, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. Provider 50 g/L comes from 1.50 g in Solution B with 30 ml water. ", "sources": [{"locator": "$.data.solutions[2].recipe[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\": 471.752,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 42-42", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Na2CO3                                                  1.50       g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject": "Na-acetate x 3 H2O root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "30", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "30", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "30", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "30", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Solution C flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Solution C, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. Provider 30 g/L comes from 0.30 g in Solution C with 10 ml water. ", "sources": [{"locator": "$.data.solutions[3].recipe[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na-acetate x 3 H2O\",\n                        \"compound_id\": 294,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 48-48", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Na-acetate x 3 H2O                                      0.30       g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q10", "subject": "Na2S2O5 root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "95", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "95", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "95", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "95", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Solution E flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Solution E, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. Provider 95 g/L belongs to Solution E, 0.95 g with 10 ml water; repeated feeding is a separate procedure. ", "sources": [{"locator": "$.data.solutions[5].recipe[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2S2O5\",\n                        \"compound_id\": 440,\n                        \"attribute\": \"sodium pyrosulfite\",\n                        \"amount\": 0.95,\n                        \"unit\": \"g\",\n                        \"g_l\": 95,\n                        \"mmol_l\": 499.711,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 64-64", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Na2S2O5 (sodium pyrosulfite)                                0.95        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q11", "subject": "Na2S x 9 H2O root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "30.7692", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "30.7692", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "30.7692", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "30.7692", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Solution F flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Solution F, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. Provider 30.7692 g/L belongs to Solution F, 0.40 g with 13 ml water. ", "sources": [{"locator": "$.data.solutions[6].recipe[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 30.7692,\n                        \"mmol_l\": 128.108,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 72-72", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Na2S x 9 H2O                                                0.40        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q12", "subject": "HCl root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "2.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Trace element solution SL-10 flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Trace element solution SL-10, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. HCl is 10 ml of 25% with unspecified percentage basis; 2.5 g/L is explicit provider metadata, not a mass derived independently from that percentage. SL-10 has an explicit 1000 ml makeup, supporting its stock basis. ", "sources": [{"locator": "$.data.solutions[7].recipe[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 78-78", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   HCl (25%)                                                  10.00      ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q13", "subject": "FeCl2 x 4 H2O root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Trace element solution SL-10 flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Trace element solution SL-10, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. SL-10 has an explicit 1000 ml makeup, supporting its stock basis. ", "sources": [{"locator": "$.data.solutions[7].recipe[1]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 79-79", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   FeCl2 x 4 H2O                                               1.50       g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q14", "subject": "FeCl2 x 4 H2O retained nested stock value", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "solutions[0].composition[0].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "solutions[0].composition[0].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Trace element solution SL-10", "interpretation": "Already nested component has the correct explicit provider stock rate and supplied batch amount. This newly attached review evidence supports that stock layer only; the partial stock membership, receiving dose and unverified KOMODO identity remain separate concerns.", "sources": [{"locator": "$.data.solutions[7].recipe[1]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 79-79", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   FeCl2 x 4 H2O                                               1.50       g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q15", "subject": "ZnCl2 root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Trace element solution SL-10 flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Trace element solution SL-10, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. SL-10 has an explicit 1000 ml makeup, supporting its stock basis. ", "sources": [{"locator": "$.data.solutions[7].recipe[2]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 80-80", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   ZnCl2                                                      70.00      mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q16", "subject": "MnCl2 x 4 H2O root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Trace element solution SL-10 flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Trace element solution SL-10, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. SL-10 has an explicit 1000 ml makeup, supporting its stock basis. ", "sources": [{"locator": "$.data.solutions[7].recipe[3]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 81-81", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   MnCl2 x 4 H2O                                             100.00      mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q17", "subject": "H3BO3 root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Trace element solution SL-10 flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Trace element solution SL-10, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. SL-10 has an explicit 1000 ml makeup, supporting its stock basis. ", "sources": [{"locator": "$.data.solutions[7].recipe[4]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 82-82", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   H3BO3                                                       6.00      mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q18", "subject": "CoCl2 x 6 H2O root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Trace element solution SL-10 flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Trace element solution SL-10, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. SL-10 has an explicit 1000 ml makeup, supporting its stock basis. ", "sources": [{"locator": "$.data.solutions[7].recipe[5]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 83-83", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   CoCl2 x 6 H2O                                             190.00      mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q19", "subject": "CuCl2 x 2 H2O root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Trace element solution SL-10 flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Trace element solution SL-10, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. SL-10 has an explicit 1000 ml makeup, supporting its stock basis. ", "sources": [{"locator": "$.data.solutions[7].recipe[6]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 84-84", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   CuCl2 x 2 H2O                                               2.00      mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q20", "subject": "NiCl2 x 6 H2O root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Trace element solution SL-10 flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Trace element solution SL-10, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. SL-10 has an explicit 1000 ml makeup, supporting its stock basis. ", "sources": [{"locator": "$.data.solutions[7].recipe[7]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 85-85", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   NiCl2 x 6 H2O                                              24.00      mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q21", "subject": "Na2MoO4 x 2 H2O root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Trace element solution SL-10 flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Trace element solution SL-10, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. SL-10 has an explicit 1000 ml makeup, supporting its stock basis. ", "sources": [{"locator": "$.data.solutions[7].recipe[8]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 86-86", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Na2MoO4 x 2 H2O                                            36.00      mg", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q22", "subject": "NaOH root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Selenite-tungstate solution flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Selenite-tungstate solution, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. The source gives 1000 ml stock water and the provider declares 1000 ml; these support the qualified provider stock rate, not a measured final volume. ", "sources": [{"locator": "$.data.solutions[8].recipe[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 95-95", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   NaOH                                                       0.50        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q23", "subject": "Na2SeO3 x 5 H2O root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Selenite-tungstate solution flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Selenite-tungstate solution, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. The source gives 1000 ml stock water and the provider declares 1000 ml; these support the qualified provider stock rate, not a measured final volume. ", "sources": [{"locator": "$.data.solutions[8].recipe[1]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 96-96", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Na2SeO3 x 5 H2O                                            3.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q24", "subject": "Na2WO4 x 2 H2O root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.004", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.004", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.004", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.004", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Selenite-tungstate solution flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Selenite-tungstate solution, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. The source gives 1000 ml stock water and the provider declares 1000 ml; these support the qualified provider stock rate, not a measured final volume. ", "sources": [{"locator": "$.data.solutions[8].recipe[2]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 97-97", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Na2WO4 x 2 H2O                                             4.00       mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q25", "subject": "Vitamin B12 root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Seven vitamins solution flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Seven vitamins solution, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. The source gives 1000 ml stock water and the provider declares 1000 ml; these support the qualified provider stock rate, not a measured final volume. ", "sources": [{"locator": "$.data.solutions[9].recipe[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.073779,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 103-103", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Vitamin B12                                               100.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q26", "subject": "Vitamin B12 retained nested stock value", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "solutions[1].composition[0].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "solutions[1].composition[0].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Seven vitamins solution", "interpretation": "Already nested component has the correct explicit provider stock rate and supplied batch amount. This newly attached review evidence supports that stock layer only; the partial stock membership, receiving dose and unverified KOMODO identity remain separate concerns.", "sources": [{"locator": "$.data.solutions[9].recipe[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.073779,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 103-103", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Vitamin B12                                               100.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q27", "subject": "p-Aminobenzoic acid root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.08", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.08", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.08", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.08", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Seven vitamins solution flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Seven vitamins solution, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. The source gives 1000 ml stock water and the provider declares 1000 ml; these support the qualified provider stock rate, not a measured final volume. ", "sources": [{"locator": "$.data.solutions[9].recipe[1]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 80,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\": 0.583345,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 104-104", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   p-Aminobenzoic acid                                        80.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q28", "subject": "D-(+)-biotin root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Seven vitamins solution flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Seven vitamins solution, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. The source gives 1000 ml stock water and the provider declares 1000 ml; these support the qualified provider stock rate, not a measured final volume. ", "sources": [{"locator": "$.data.solutions[9].recipe[2]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\": 1359,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 105-105", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   D-(+)-biotin                                               20.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q29", "subject": "Nicotinic acid root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Seven vitamins solution flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Seven vitamins solution, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. The source gives 1000 ml stock water and the provider declares 1000 ml; these support the qualified provider stock rate, not a measured final volume. ", "sources": [{"locator": "$.data.solutions[9].recipe[3]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.62456,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 106-106", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Nicotinic acid                                            200.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q30", "subject": "Nicotinic acid retained nested stock value", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "solutions[1].composition[1].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "solutions[1].composition[1].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Seven vitamins solution", "interpretation": "Already nested component has the correct explicit provider stock rate and supplied batch amount. This newly attached review evidence supports that stock layer only; the partial stock membership, receiving dose and unverified KOMODO identity remain separate concerns.", "sources": [{"locator": "$.data.solutions[9].recipe[3]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.62456,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 106-106", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Nicotinic acid                                            200.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q31", "subject": "Calcium pantothenate root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Seven vitamins solution flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Seven vitamins solution, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. The source gives 1000 ml stock water and the provider declares 1000 ml; these support the qualified provider stock rate, not a measured final volume. ", "sources": [{"locator": "$.data.solutions[9].recipe[4]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.209849,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 107-107", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Calcium pantothenate                                      100.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q32", "subject": "Pyridoxine hydrochloride root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Seven vitamins solution flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Seven vitamins solution, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. The source gives 1000 ml stock water and the provider declares 1000 ml; these support the qualified provider stock rate, not a measured final volume. ", "sources": [{"locator": "$.data.solutions[9].recipe[5]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 300,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.45886,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 108-108", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Pyridoxine hydrochloride                                  300.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q33", "subject": "Pyridoxine hydrochloride retained nested stock value", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "solutions[1].composition[2].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "solutions[1].composition[2].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Seven vitamins solution", "interpretation": "Already nested component has the correct explicit provider stock rate and supplied batch amount. This newly attached review evidence supports that stock layer only; the partial stock membership, receiving dose and unverified KOMODO identity remain separate concerns.", "sources": [{"locator": "$.data.solutions[9].recipe[5]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 300,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.45886,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 108-108", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Pyridoxine hydrochloride                                  300.00      mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q34", "subject": "Thiamine-HCl x 2 H2O root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Seven vitamins solution flattened to main recipe", "interpretation": "The printed batch amount and explicit provider g_l belong to Seven vitamins solution, not the assembled main medium. The selected root/main placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different recipe, so matching copied values cannot authenticate those branches. The source gives 1000 ml stock water and the provider declares 1000 ml; these support the qualified provider stock rate, not a measured final volume. ", "sources": [{"locator": "$.data.solutions[9].recipe[6]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\": 77,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.535761,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 116-116", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Thiamine-HCl x 2 H2O              200.00   mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q35", "subject": "Thiamine-HCl x 2 H2O retained nested stock value", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "solutions[1].composition[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "solutions[1].composition[3].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Seven vitamins solution", "interpretation": "Already nested component has the correct explicit provider stock rate and supplied batch amount. This newly attached review evidence supports that stock layer only; the partial stock membership, receiving dose and unverified KOMODO identity remain separate concerns.", "sources": [{"locator": "$.data.solutions[9].recipe[6]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\": 77,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.535761,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 116-116", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Thiamine-HCl x 2 H2O              200.00   mg", "quote_representation": "captured extracted text"}]}, {"decision_id": "q36", "subject": "desulfolutivibrio_medium stock 0 receiving dose", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "solutions[0].concentration", "original": {"value": "1", "unit": "ML_PER_L"}}], "decision": "unsupported", "stage": "receiving dose versus per-litre rate", "interpretation": "The source specifies a 1 ml batch addition, not an unqualified 1 ml per litre. SL-10 enters Solution A; vitamins enter as Solution D. The A–F additions sum to 1006 ml on the declared provider basis, with no measured assembled final volume. Preserve exact batch stages and qualify any derived rate; a composition-match promotion does not establish this denominator.", "sources": [{"locator": "$.data.solutions[1].recipe[6]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 34-34", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Trace element solution SL-10                           1.00       ml", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 3-8", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution A                                           942.00       ml\n   Solution B                                            30.00       ml\n   Solution C                                            10.00       ml\n   Solution D                                             1.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            13.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q37", "subject": "desulfolutivibrio_medium stock 0 preparation note", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "solutions[0].preparation_notes", "original": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."}], "decision": "unsupported", "stage": "retained numeric stock note", "interpretation": "The retained 1000 ml stock basis is supported: explicit makeup for SL-10, declared water/provider volume for vitamins. The added per-litre claim is unsupported and must retain the distinct batch-dose limit.", "sources": [{"locator": "$.data.solutions[7].steps[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q38", "subject": "desulfolutivibrio_medium stock 1 receiving dose", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "solutions[1].concentration", "original": {"value": "1", "unit": "ML_PER_L"}}], "decision": "unsupported", "stage": "receiving dose versus per-litre rate", "interpretation": "The source specifies a 1 ml batch addition, not an unqualified 1 ml per litre. SL-10 enters Solution A; vitamins enter as Solution D. The A–F additions sum to 1006 ml on the declared provider basis, with no measured assembled final volume. Preserve exact batch stages and qualify any derived rate; a composition-match promotion does not establish this denominator.", "sources": [{"locator": "$.data.solutions[4].recipe[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\": 1038,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 59-59", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Seven vitamins solution                                     1.00       ml", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 3-8", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution A                                           942.00       ml\n   Solution B                                            30.00       ml\n   Solution C                                            10.00       ml\n   Solution D                                             1.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            13.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q39", "subject": "desulfolutivibrio_medium stock 1 preparation note", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "solutions[1].preparation_notes", "original": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."}], "decision": "unsupported", "stage": "retained numeric stock note", "interpretation": "The retained 1000 ml stock basis is supported: explicit makeup for SL-10, declared water/provider volume for vitamins. The added per-litre claim is unsupported and must retain the distinct batch-dose limit.", "sources": [{"locator": "$.data.solutions[9].recipe[7]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 117-117", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled water                  1000.00   ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q40", "subject": "desulfovibrio_sulfodismutans_medium stock 0 receiving dose", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "solutions[0].concentration", "original": {"value": "1", "unit": "ML_PER_L"}}], "decision": "unsupported", "stage": "receiving dose versus per-litre rate", "interpretation": "The source specifies a 1 ml batch addition, not an unqualified 1 ml per litre. SL-10 enters Solution A; vitamins enter as Solution D. The A–F additions sum to 1006 ml on the declared provider basis, with no measured assembled final volume. Preserve exact batch stages and qualify any derived rate; a composition-match promotion does not establish this denominator.", "sources": [{"locator": "$.data.solutions[1].recipe[6]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 34-34", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Trace element solution SL-10                           1.00       ml", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 3-8", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution A                                           942.00       ml\n   Solution B                                            30.00       ml\n   Solution C                                            10.00       ml\n   Solution D                                             1.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            13.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q41", "subject": "desulfovibrio_sulfodismutans_medium stock 0 preparation note", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "solutions[0].preparation_notes", "original": "Stock prepared in 1000 ml. Composition and volume from medium 386's own MediaDive recipe, identified by this record reproducing that medium's composition exactly (30/30 shared compounds at identical values) despite the upstream rename to 'DESULFOLUTIVIBRIO MEDIUM' (#262)."}], "decision": "evidence_only", "stage": "retained numeric stock note", "interpretation": "The retained 1000 ml stock basis is supported: explicit makeup for SL-10, declared water/provider volume for vitamins. The note accurately records a historical 30/30 numerical comparison, which is not independent current identity or receiving-volume proof; do not transfer that inference beyond its scope.", "sources": [{"locator": "$.data.solutions[7].steps[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q42", "subject": "desulfovibrio_sulfodismutans_medium stock 1 receiving dose", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "solutions[1].concentration", "original": {"value": "1", "unit": "ML_PER_L"}}], "decision": "unsupported", "stage": "receiving dose versus per-litre rate", "interpretation": "The source specifies a 1 ml batch addition, not an unqualified 1 ml per litre. SL-10 enters Solution A; vitamins enter as Solution D. The A–F additions sum to 1006 ml on the declared provider basis, with no measured assembled final volume. Preserve exact batch stages and qualify any derived rate; a composition-match promotion does not establish this denominator.", "sources": [{"locator": "$.data.solutions[4].recipe[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\": 1038,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 59-59", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Seven vitamins solution                                     1.00       ml", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 3-8", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution A                                           942.00       ml\n   Solution B                                            30.00       ml\n   Solution C                                            10.00       ml\n   Solution D                                             1.00       ml\n   Solution E                                            10.00       ml\n   Solution F                                            13.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q43", "subject": "desulfovibrio_sulfodismutans_medium stock 1 preparation note", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "solutions[1].preparation_notes", "original": "Stock prepared in 1000 ml. Composition and volume from medium 386's own MediaDive recipe, identified by this record reproducing that medium's composition exactly (30/30 shared compounds at identical values) despite the upstream rename to 'DESULFOLUTIVIBRIO MEDIUM' (#262)."}], "decision": "evidence_only", "stage": "retained numeric stock note", "interpretation": "The retained 1000 ml stock basis is supported: explicit makeup for SL-10, declared water/provider volume for vitamins. The note accurately records a historical 30/30 numerical comparison, which is not independent current identity or receiving-volume proof; do not transfer that inference beyond its scope.", "sources": [{"locator": "$.data.solutions[9].recipe[7]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 117-117", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled water                  1000.00   ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q44", "subject": "Source A–F addition Solution A", "local_fields": [], "decision": "add", "stage": "assembled DSM386 batch", "interpretation": "Preserve this exact staged batch addition. The six values total 1006 ml; their sum is provider bookkeeping, not an independently measured final volume. No automatic conversion into local final-medium rates is proposed.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 779,\n                        \"amount\": 942,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 3-3", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution A                                           942.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q45", "subject": "Source A–F addition Solution B", "local_fields": [], "decision": "add", "stage": "assembled DSM386 batch", "interpretation": "Preserve this exact staged batch addition. The six values total 1006 ml; their sum is provider bookkeeping, not an independently measured final volume. No automatic conversion into local final-medium rates is proposed.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\": 783,\n                        \"amount\": 30,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 4-4", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution B                                            30.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q46", "subject": "Source A–F addition Solution C", "local_fields": [], "decision": "add", "stage": "assembled DSM386 batch", "interpretation": "Preserve this exact staged batch addition. The six values total 1006 ml; their sum is provider bookkeeping, not an independently measured final volume. No automatic conversion into local final-medium rates is proposed.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 782,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 5-5", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution C                                            10.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q47", "subject": "Source A–F addition Solution D", "local_fields": [], "decision": "add", "stage": "assembled DSM386 batch", "interpretation": "Preserve this exact staged batch addition. The six values total 1006 ml; their sum is provider bookkeeping, not an independently measured final volume. No automatic conversion into local final-medium rates is proposed.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\": 784,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 6-6", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution D                                             1.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q48", "subject": "Source A–F addition Solution E", "local_fields": [], "decision": "add", "stage": "assembled DSM386 batch", "interpretation": "Preserve this exact staged batch addition. The six values total 1006 ml; their sum is provider bookkeeping, not an independently measured final volume. No automatic conversion into local final-medium rates is proposed.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"solution\": \"Solution E\",\n                        \"solution_id\": 786,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 7-7", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution E                                            10.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q49", "subject": "Source A–F addition Solution F", "local_fields": [], "decision": "add", "stage": "assembled DSM386 batch", "interpretation": "Preserve this exact staged batch addition. The six values total 1006 ml; their sum is provider bookkeeping, not an independently measured final volume. No automatic conversion into local final-medium rates is proposed.", "sources": [{"locator": "$.data.solutions[0].recipe[5]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Solution F\",\n                        \"solution_id\": 785,\n                        \"amount\": 13,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 8-8", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution F                                            13.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q50", "subject": "Solution A water", "local_fields": [], "decision": "add", "stage": "source-only solvent", "interpretation": "Retain the exact source solvent quantity at this solution stage. Except the explicit SL-10 makeup, a water input is not a measured final solution volume; preserve the separately stated provider basis.", "sources": [{"locator": "$.data.solutions[1].recipe[9]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 940,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 37-37", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled water                                      940.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q51", "subject": "Solution B water", "local_fields": [], "decision": "add", "stage": "source-only solvent", "interpretation": "Retain the exact source solvent quantity at this solution stage. Except the explicit SL-10 makeup, a water input is not a measured final solution volume; preserve the separately stated provider basis.", "sources": [{"locator": "$.data.solutions[2].recipe[1]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 30,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 43-43", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled water                                        30.00      ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q52", "subject": "Solution C water", "local_fields": [], "decision": "add", "stage": "source-only solvent", "interpretation": "Retain the exact source solvent quantity at this solution stage. Except the explicit SL-10 makeup, a water input is not a measured final solution volume; preserve the separately stated provider basis.", "sources": [{"locator": "$.data.solutions[3].recipe[1]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 49-49", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled water                                        10.00      ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q53", "subject": "Solution E water", "local_fields": [], "decision": "add", "stage": "source-only solvent", "interpretation": "Retain the exact source solvent quantity at this solution stage. Except the explicit SL-10 makeup, a water input is not a measured final solution volume; preserve the separately stated provider basis.", "sources": [{"locator": "$.data.solutions[5].recipe[1]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 65-65", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled water                                            10.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q54", "subject": "Solution F water", "local_fields": [], "decision": "add", "stage": "source-only solvent", "interpretation": "Retain the exact source solvent quantity at this solution stage. Except the explicit SL-10 makeup, a water input is not a measured final solution volume; preserve the separately stated provider basis.", "sources": [{"locator": "$.data.solutions[6].recipe[1]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 13,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 73-73", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled water                                            13.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q55", "subject": "Trace element solution SL-10 water", "local_fields": [], "decision": "add", "stage": "source-only solvent", "interpretation": "Retain the exact source solvent quantity at this solution stage. Except the explicit SL-10 makeup, a water input is not a measured final solution volume; preserve the separately stated provider basis.", "sources": [{"locator": "$.data.solutions[7].recipe[9]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 87-87", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled water                                           990.00      ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q56", "subject": "Selenite-tungstate solution water", "local_fields": [], "decision": "add", "stage": "source-only solvent", "interpretation": "Retain the exact source solvent quantity at this solution stage. Except the explicit SL-10 makeup, a water input is not a measured final solution volume; preserve the separately stated provider basis.", "sources": [{"locator": "$.data.solutions[8].recipe[3]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 98-98", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled water                                         1000.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q57", "subject": "Seven vitamins solution water", "local_fields": [], "decision": "add", "stage": "source-only solvent", "interpretation": "Retain the exact source solvent quantity at this solution stage. Except the explicit SL-10 makeup, a water input is not a measured final solution volume; preserve the separately stated provider basis.", "sources": [{"locator": "$.data.solutions[9].recipe[7]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 117-117", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled water                  1000.00   ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q58", "subject": "Missing structured selenite-tungstate addition", "local_fields": [], "decision": "add", "stage": "Solution A receiving stock", "interpretation": "The source adds 1 ml of its separate selenite-tungstate solution to A. Its three compound stock rates remain root-level locally; retain this dose distinctly from a per-litre or final-medium concentration.", "sources": [{"locator": "$.data.solutions[1].recipe[7]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 35-35", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Selenite-tungstate solution                            1.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q59", "subject": "Retained staged preparation", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "preparation_steps[0].description", "original": "Solution A is sparged 80% N2 and 20% CO2 gas mixture for 30 – 45 min to make it anoxic, then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas mixture. Solutions C and F are autoclaved under 100% N2 gas. \r\nSolutions D and E are prepared under 100% N2 gas atmosphere and sterilized by filtration. To complete the medium appropriate amounts of the solutions B to F are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be at 7.1 - 7.4."}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "preparation_steps[0].description", "original": "Solution A is sparged 80% N2 and 20% CO2 gas mixture for 30 – 45 min to make it anoxic, then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas mixture. Solutions C and F are autoclaved under 100% N2 gas. \r\nSolutions D and E are prepared under 100% N2 gas atmosphere and sterilized by filtration. To complete the medium appropriate amounts of the solutions B to F are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be at 7.1 - 7.4."}], "decision": "evidence_only", "stage": "DSM386 preparation", "interpretation": "The target and DSM owner retain the complete 80/20 gas mixture, 30–45 minutes, separate 100% N2 branches, filtration and ordered additions. Preserve this text; its single AUTOCLAVE action cannot represent the distinct filtration steps, and the KOMODO owner lacks the procedure.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\": \"Solution A is sparged 80% N2 and 20% CO2 gas mixture for 30 \\u2013 45 min to make it anoxic, then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas mixture. Solutions C and F are autoclaved under 100% N2 gas. \\r\\nSolutions D and E are prepared under 100% N2 gas atmosphere and sterilized by filtration. To complete the medium appropriate amounts of the solutions B to F are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be at 7.1 - 7.4.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 10-16", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "1. Solution A is sparged 80% N2 and 20% CO2 gas mixture for 30 – 45 min to make it\nanoxic, then distributed under the same gas atmosphere into anoxic Hungate-type tubes\nor serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20%\nCO2 gas mixture. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E\nare prepared under 100% N2 gas atmosphere and sterilized by filtration. To complete the\nmedium appropriate amounts of the solutions B to F are added to the sterile solution A in\nthe sequence as indicated. Final pH of the medium should be at 7.1 - 7.4.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q60", "subject": "Retained staged action", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "preparation_steps[0].action", "original": "AUTOCLAVE"}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "preparation_steps[0].action", "original": "AUTOCLAVE"}], "decision": "unsupported", "stage": "mixed preparation operations", "interpretation": "AUTOCLAVE applies to only part of the retained paragraph; D/E require filtration. Split the supported operations without inventing autoclave temperature or duration.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\": \"Solution A is sparged 80% N2 and 20% CO2 gas mixture for 30 \\u2013 45 min to make it anoxic, then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas mixture. Solutions C and F are autoclaved under 100% N2 gas. \\r\\nSolutions D and E are prepared under 100% N2 gas atmosphere and sterilized by filtration. To complete the medium appropriate amounts of the solutions B to F are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be at 7.1 - 7.4.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q61", "subject": "Retained subsequent pyrosulfite feed", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "preparation_steps[1].description", "original": "Note: When growth has started feed culture again with same amount of pyrosulfite. After a further two days repeat feeding once more."}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "preparation_steps[1].description", "original": "Note: When growth has started feed culture again with same amount of pyrosulfite. After a further two days repeat feeding once more."}], "decision": "evidence_only", "stage": "post-growth source procedure", "interpretation": "The exact same-amount feed and further-two-days repeat are already retained. Preserve their stage; do not sum them into the initial recipe concentration.", "sources": [{"locator": "$.data.solutions[0].steps[1]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\": \"Note: When growth has started feed culture again with same amount of pyrosulfite. After a further two days repeat feeding once more.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 17-18", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "2. Note: When growth has started feed culture again with same amount of pyrosulfite.\nAfter a further two days repeat feeding once more.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q62", "subject": "Stock procedure at main scope 2", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "preparation_steps[2].description", "original": "Adjust pH to 7.5-8.0 with NaOH."}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "preparation_steps[2].description", "original": "Adjust pH to 7.5-8.0 with NaOH."}], "decision": "unsupported", "stage": "stock-specific procedure", "interpretation": "The correct existing procedure belongs only to Solution E. Preserve its numeric control while relocating its scope; it is not a second final-medium pH or final-medium makeup.", "sources": [{"locator": "$.data.solutions[5].steps[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 7.5-8.0 with NaOH.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 67-67", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "Adjust pH to 7.5-8.0 with NaOH.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q63", "subject": "Stock procedure at main scope 3", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "preparation_steps[3].description", "original": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "preparation_steps[3].description", "original": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}], "decision": "unsupported", "stage": "stock-specific procedure", "interpretation": "The correct existing procedure belongs only to Trace element solution SL-10. Preserve its numeric control while relocating its scope; it is not a second final-medium pH or final-medium makeup.", "sources": [{"locator": "$.data.solutions[7].steps[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical LF lines 89-90", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q64", "subject": "DSM386 final pH ranges", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "ph_range", "original": {"min": 7.1, "max": 7.4}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path": "ph_range", "original": {"min": 7.1, "max": 7.4}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml", "field_path": "ph_range", "original": {"min": 7.1, "max": 7.4}}], "decision": "evidence_only", "stage": "complete DSM386 medium", "interpretation": "The retained 7.1–7.4 range is supported by the DSM386 primary/API. The copied KOMODO value remains a historical match, not fresh authentication of its inaccessible route.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\": \"Solution A is sparged 80% N2 and 20% CO2 gas mixture for 30 \\u2013 45 min to make it anoxic, then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas mixture. Solutions C and F are autoclaved under 100% N2 gas. \\r\\nSolutions D and E are prepared under 100% N2 gas atmosphere and sterilized by filtration. To complete the medium appropriate amounts of the solutions B to F are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be at 7.1 - 7.4.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q65", "subject": "Historical Sulforhabdus pH", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml", "field_path": "ph_range", "original": {"min": 7.2, "max": 7.5}}], "decision": "unsupported", "stage": "unresolved386a identity", "interpretation": "The local 7.2–7.5 is historical Sulforhabdus metadata. Current DSM386a is THIOVIBRIO with pH7.0, so preserve the conflict without automatically substituting another recipe or its pH.", "sources": [{"locator": "extracted-text physical LF lines 1-1", "source_key": "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf", "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d", "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801", "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "386a: THIOVIBRIO MEDIUM", "quote_representation": "captured extracted text"}, {"locator": "extracted-text physical LF lines 9-17", "source_key": "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf", "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d", "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801", "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture for 30 – 45 min to make it\nanoxic, then distributed under the same gas atmosphere into anoxic Hungate-type tubes\nor serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20%\nCO2 gas mixture. Solutions C and D are prepared under a 100% N2 gas atmosphere and\nsterilized by filtration. To complete the medium solutions B to D are added to the sterile\nsolution A in the sequence as indicated. Before inoculation, appropriate amounts of sterile\nsulfur are added to the vials with the medium. Sulfur is sterilized by steaming for 3 hours\non each of 3 successive days (see medium 35) and added aseptically to the sterile\nmedium while retaining anoxic conditions. The final pH of the medium should be at 7.0.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q66", "subject": "DSM7269-only alternative", "local_fields": [], "decision": "not_assessed", "stage": "strain-specific source override", "interpretation": "The exact source-only 2.50 g/L thiosulfate pentahydrate replacement and post-autoclave stock addition apply only to named DSM7269. They are retained as excluded variant context, not proposed for the generic selected medium.", "sources": [{"locator": "extracted-text physical LF lines 21-22", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "For DSM 7269: Replace pyrosulfite with 2.50 g/l Na2S2O3 x 5 H2O added to the medium\nafter autoclaving from a sterile anoxic stock solution.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q67", "subject": "Current386a Main staged additions and sulfur", "local_fields": [], "decision": "not_assessed", "stage": "distinct current THIOVIBRIO recipe", "interpretation": "All printed amounts and controls in this source section are retained as exact identity/comparison evidence only. They cannot be transferred to historical Sulforhabdus or generic DSM386. For the washed Fe(OH)3 precipitate, discarded supernatant and unspecified resuspension preclude final suspension mass-balance inference.", "sources": [{"locator": "extracted-text physical LF lines 3-7", "source_key": "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf", "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d", "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801", "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "   Solution A                                             967.00       ml\n   Solution B                                              30.00       ml\n   Solution C                                               1.00       ml\n   Solution D                                              10.00       ml\n   Sulfur (powdered)                                       10.00        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q68", "subject": "Current386a Main atmosphere, sulfur sterilization and pH controls", "local_fields": [], "decision": "not_assessed", "stage": "distinct current THIOVIBRIO recipe", "interpretation": "All printed amounts and controls in this source section are retained as exact identity/comparison evidence only. They cannot be transferred to historical Sulforhabdus or generic DSM386. For the washed Fe(OH)3 precipitate, discarded supernatant and unspecified resuspension preclude final suspension mass-balance inference.", "sources": [{"locator": "extracted-text physical LF lines 9-17", "source_key": "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf", "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d", "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801", "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture for 30 – 45 min to make it\nanoxic, then distributed under the same gas atmosphere into anoxic Hungate-type tubes\nor serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20%\nCO2 gas mixture. Solutions C and D are prepared under a 100% N2 gas atmosphere and\nsterilized by filtration. To complete the medium solutions B to D are added to the sterile\nsolution A in the sequence as indicated. Before inoculation, appropriate amounts of sterile\nsulfur are added to the vials with the medium. Sulfur is sterilized by steaming for 3 hours\non each of 3 successive days (see medium 35) and added aseptically to the sterile\nmedium while retaining anoxic conditions. The final pH of the medium should be at 7.0.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q69", "subject": "Current386a Solution A complete batch", "local_fields": [], "decision": "not_assessed", "stage": "distinct current THIOVIBRIO recipe", "interpretation": "All printed amounts and controls in this source section are retained as exact identity/comparison evidence only. They cannot be transferred to historical Sulforhabdus or generic DSM386. For the washed Fe(OH)3 precipitate, discarded supernatant and unspecified resuspension preclude final suspension mass-balance inference.", "sources": [{"locator": "extracted-text physical LF lines 22-32", "source_key": "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf", "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d", "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801", "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Solution A\n   KH2PO4                                                   0.20        g\n   NH4Cl                                                    0.25        g\n   NaCl                                                     1.00        g\n   MgCl2 x 6 H2O                                            0.40        g\n   KCl                                                      0.50        g\n   CaCl2 x 2 H2O                                            0.15        g\n   Trace element solution SL-10                             1.00       ml\n   Selenite-tungstate solution                              1.00       ml\n   Amorphous Fe(OH)3                                       25.00       ml\n   Distilled water                                        940.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q70", "subject": "Current386a Solution B", "local_fields": [], "decision": "not_assessed", "stage": "distinct current THIOVIBRIO recipe", "interpretation": "All printed amounts and controls in this source section are retained as exact identity/comparison evidence only. They cannot be transferred to historical Sulforhabdus or generic DSM386. For the washed Fe(OH)3 precipitate, discarded supernatant and unspecified resuspension preclude final suspension mass-balance inference.", "sources": [{"locator": "extracted-text physical LF lines 36-38", "source_key": "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf", "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d", "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801", "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Solution B (from medium 386)\n   Na2CO3                                                   1.50        g\n   Distilled water                                         30.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q71", "subject": "Current386a Solution C vitamins dose", "local_fields": [], "decision": "not_assessed", "stage": "distinct current THIOVIBRIO recipe", "interpretation": "All printed amounts and controls in this source section are retained as exact identity/comparison evidence only. They cannot be transferred to historical Sulforhabdus or generic DSM386. For the washed Fe(OH)3 precipitate, discarded supernatant and unspecified resuspension preclude final suspension mass-balance inference.", "sources": [{"locator": "extracted-text physical LF lines 42-43", "source_key": "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf", "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d", "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801", "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Solution C\n   Seven vitamins solution                                  1.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q72", "subject": "Current386a Solution D", "local_fields": [], "decision": "not_assessed", "stage": "distinct current THIOVIBRIO recipe", "interpretation": "All printed amounts and controls in this source section are retained as exact identity/comparison evidence only. They cannot be transferred to historical Sulforhabdus or generic DSM386. For the washed Fe(OH)3 precipitate, discarded supernatant and unspecified resuspension preclude final suspension mass-balance inference.", "sources": [{"locator": "extracted-text physical LF lines 47-49", "source_key": "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf", "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d", "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801", "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Solution D\n   DL-Dithiothreitol                                        0.30        g\n   Distilled water                                         10.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q73", "subject": "Current386a SL-10 full batch and makeup", "local_fields": [], "decision": "not_assessed", "stage": "distinct current THIOVIBRIO recipe", "interpretation": "All printed amounts and controls in this source section are retained as exact identity/comparison evidence only. They cannot be transferred to historical Sulforhabdus or generic DSM386. For the washed Fe(OH)3 precipitate, discarded supernatant and unspecified resuspension preclude final suspension mass-balance inference.", "sources": [{"locator": "extracted-text physical LF lines 58-71", "source_key": "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf", "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d", "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801", "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                                  10.00      ml\n   FeCl2 x 4 H2O                                               1.50       g\n   ZnCl2                                                      70.00      mg\n   MnCl2 x 4 H2O                                             100.00      mg\n   H3BO3                                                       6.00      mg\n   CoCl2 x 6 H2O                                             190.00      mg\n   CuCl2 x 2 H2O                                               2.00      mg\n   NiCl2 x 6 H2O                                              24.00      mg\n   Na2MoO4 x 2 H2O                                            36.00      mg\n   Distilled water                                           990.00      ml\n\nFirst dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q74", "subject": "Current386a Selenite-tungstate batch", "local_fields": [], "decision": "not_assessed", "stage": "distinct current THIOVIBRIO recipe", "interpretation": "All printed amounts and controls in this source section are retained as exact identity/comparison evidence only. They cannot be transferred to historical Sulforhabdus or generic DSM386. For the washed Fe(OH)3 precipitate, discarded supernatant and unspecified resuspension preclude final suspension mass-balance inference.", "sources": [{"locator": "extracted-text physical LF lines 75-79", "source_key": "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf", "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d", "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801", "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Selenite-tungstate solution (from medium 385)\n   NaOH                                                       0.50        g\n   Na2SeO3 x 5 H2O                                            3.00       mg\n   Na2WO4 x 2 H2O                                             4.00       mg\n   Distilled water                                         1000.00       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q75", "subject": "Current386a Ferric-hydroxide precipitation inputs and controls", "local_fields": [], "decision": "not_assessed", "stage": "distinct current THIOVIBRIO recipe", "interpretation": "All printed amounts and controls in this source section are retained as exact identity/comparison evidence only. They cannot be transferred to historical Sulforhabdus or generic DSM386. For the washed Fe(OH)3 precipitate, discarded supernatant and unspecified resuspension preclude final suspension mass-balance inference.", "sources": [{"locator": "extracted-text physical LF lines 83-92", "source_key": "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf", "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d", "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801", "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Amorphous Fe(OH)3 (from medium 1210)\n   FeCl3 x 6 H2O (60.00 g/l)                                 320.00       ml\n   NaOH (10% w/v), adjust if required                         80.00       ml\n\nSlowly titrate 320 ml of a FeCl3 x 6 H2O stock solution (60.00 g/l) with 10% (w/v) NaOH to\npH 8.0-8.5 under agitation (use magnetic stirrer). Total amount of added NaOH approx. 80\n- 100 ml. The precipitated Fe(OH)3 should be stored at room temperature overnight with\nsurface covered with water. Thereafter, centrifuge at 2000 rpm for 5 min and discard the\nsupernatant. Wash several times with distilled water. Resuspend the pellet in medium as\ndescribed above. For storage autoclave under 100% N2 atmosphere.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q76", "subject": "Current386a Seven-vitamin stock", "local_fields": [], "decision": "not_assessed", "stage": "distinct current THIOVIBRIO recipe", "interpretation": "All printed amounts and controls in this source section are retained as exact identity/comparison evidence only. They cannot be transferred to historical Sulforhabdus or generic DSM386. For the washed Fe(OH)3 precipitate, discarded supernatant and unspecified resuspension preclude final suspension mass-balance inference.", "sources": [{"locator": "extracted-text physical LF lines 96-104", "source_key": "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf", "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d", "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801", "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Seven vitamins solution (from medium 503)\n   Vitamin B12                                              100.00       mg\n   p-Aminobenzoic acid                                       80.00       mg\n   D-(+)-biotin                                              20.00       mg\n   Nicotinic acid                                           200.00       mg\n   Calcium pantothenate                                     100.00       mg\n   Pyridoxine hydrochloride                                 300.00       mg\n   Thiamine-HCl x 2 H2O                                     200.00       mg\n   Distilled water                                         1000.00       ml", "quote_representation": "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch076/record06/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:001493.

data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml: primary 30/30, secondary 28/30; data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml: primary 25/25, secondary 23/25; data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml: primary 25/25, secondary 23/25; data/normalized_yaml/bacterial/sulforhabdus_medium.yaml: primary 30/30, secondary 28/30. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:001493.

Complete selected generated target and all three exact maintained contributors reviewed. The assessed stock definitions are embedded in DSM386. Current DSM386a is comparison-only and does not establish the historical KOMODO386a formulation. No external dependency formulation is transferred; source prescriptions and medium names are not strain-growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:001493.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Separate A–F and stock rates are presented at main-medium scope

major / open / confirmed; issue key: culturemech-001493-source-stage-denominators.

All 30 target concentrations come from separate A–F or embedded stock bases. Maintained DSM/KOMODO386 owners partially nest five stock compounds, which are credited, but most remain flat and both receiving doses are unqualified ML_PER_L. Main batch additions, water and distinct stock structure are missing.

### f2: Stored duplicate relationships conflate distinct source identities

major / open / confirmed; issue key: culturemech-001493-current-source-variant-equivalence.

The selected merge and both386 owners point to historical Sulforhabdus386a as SOURCE_DUPLICATE. The exact current386a primary identifies THIOVIBRIO and materially differs. Historical mapping and identical copied numeric signatures support ancestry, not interchangeable recipes.

### f3: Correct retained preparation needs staged structure and owner reconciliation

major / open / confirmed; issue key: culturemech-001493-preparation-stage-and-atmosphere.

The target and DSM owner retain complete anoxic preparation and feeding prose. Their combined AUTOCLAVE action includes filtration, and Solution E pH/SL-10 makeup are root steps. The KOMODO386 owner has no procedure and notes says Aerobic: Yes despite the DSM anoxic source; historical386a has no supported current procedure.

### f4: Nickel hydrate and sodium resazurin use different supplied-form IDs

major / open / confirmed; issue key: culturemech-001493-exact-supplied-form.

All selected layers assert anhydrous nickel chloride34887 for named hexahydrate in both slots, and neutral resazurin8806 for sodium resazurin in the primary slot. OLS formulas confirm those are different forms. Other correct hydrate mappings and source masses are retained; generic calcium pantothenate stereochemistry remains explicitly unresolved.

### f5: Historical matches do not supply attached claim evidence or valid timestamps

minor / open / confirmed; issue key: culturemech-001493-append-only-evidence-provenance.

No selected layer has attached formulation claims. Stored KOMODO dates contain literal .fZ and resolver events lack offsets. Current writer formats explain present risks but do not prove historical execution. The386a historical digest matches an error body, not a recipe.

## Recommended Actions And Acceptance Checks

### action1

Reconstruct exact A–F stages and complete stock membership in maintained owners. Preserve supported existing nested values and source batch amounts; distinguish provider942/1006ml bases from measured final volumes. Correct only demonstrated placement/dose-basis claims and keep unresolved KOMODO variants separate.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Resolve the historical accession/name transition and source relationship before regenerating the selected merge. Preserve all historical names and source mappings, avoid replacing Sulforhabdus with current Thiovibrio automatically, and split distinct variants when identity evidence warrants it.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Preserve correct existing descriptions while structuring each operation at its exact source stage. Resolve the KOMODO source identity and atmosphere contradiction before any propagation; do not overwrite historical source notes. Regenerate only through the current compatible-formulation guard.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Resolve exact source hydrate and sodium-salt mappings against authoritative ontology/MIM records; retain precise source labels if unresolved. Do not derive molarity using the wrong hydrate or force a D/L choice from noisy synonyms.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action5

Preserve all original events unchanged. Append new verified claim/context evidence with actual current UTC dates, explicitly retaining failure-body scope. Correct future KOMODO/resolver timestamp formatting; never rewrite guessed historical instants.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.
- Confirm new timestamps are parseable UTC Z and prior curation-history event bytes remain unchanged.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local2 | data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local3 | data/normalized_yaml/bacterial/sulforhabdus_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch076/record06/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch076/record06/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch076/record06/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch076/record06/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| dsm386 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete exact DSM primary PDF text and every rendered page read, including main recipe, separate stock tables and all staged procedures. Physical LF line locators refer to the preserved pdftotext output. |
| dsm386a | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete exact DSM primary PDF text and every rendered page read, including main recipe, separate stock tables and all staged procedures. Physical LF line locators refer to the preserved pdftotext output. |
| api386 | https://mediadive.dsmz.de/rest/medium/386; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current provider identity, solution tables and preparation read. Explicit g_l and declared volumes are credited only on their named provider stock or recipe basis; they are not independent measured final volumes. Provider mmol_l values are not adopted as chemical-form authority. |
| api386a | https://mediadive.dsmz.de/rest/medium/386a; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual HTTP 404 response, not formulation evidence. |
| komodo386 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=386; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual HTTP 403 response, not formulation evidence. |
| komodo386a | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=386a; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual HTTP 403 response, not formulation evidence. |
| komodoList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual HTTP 403 response, not formulation evidence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4']; mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17883 = hydrogen chloride; definition ['A mononuclear parent hydride consisting of covalently bonded hydrogen and chlorine atoms.']; formula ['HCl']; mass ['36.461']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group.']; formula ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32138 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32138; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32138 = sodium acetate trihydrate; definition []; formula ['C2H3O2.3H2O.Na']; mass ['136.079']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32145 = sodium hydroxide; definition []; formula ['HO.Na']; mass ['39.997']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3']; mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
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
| chebi114786 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:114786; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:114786 = sodium disulfite; definition ['An inorganic sodium salt composed of sodium and disulfite ions in a 2:1 ratio.']; formula ['2Na.O5S2']; mass ['190.109']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131361; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:131361 = disodium selenite pentahydrate; definition ['A hydrate that is the pentahydrate form of disodium selenite.']; formula ['5H2O.2Na.O3Se']; mass ['263.012']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi132751 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:132751; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:132751 = thiamine hydrochloride dihydrate; definition ['A hydrate that is the dihydrate form of thiamine hydrochloride.']; formula ['C12H18N4OS.2Cl.2H2O']; mass ['373.306']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch076/record06/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected and dependency-context term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/desulfovibrio_sulfodismutans_medium.yaml.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history1 | reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/sulforhabdus_medium.yaml.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history2 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/desulfolutivibrio_medium.yaml.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history3 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfolutivibrio_medium.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history5 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history6 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/sulforhabdus_medium.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history-auth | REVIEW_WORK/batch076/record06/historical-authentication.json; attached_claims; historical_plan_claims | supports | Actual attached claims in scoped stock sections and historical parent-plan claims are separate populations. Current raw-digest equality and literal or normalized-HTML excerpt equality are independently recorded. No attached formulation claims occur on the selected target or its maintained contributors. Current byte matches do not authenticate historical execution or access dates. |
| writer54 | scripts/apply_mim_groundings.py; target_slot; groundable; apply_to_record | context_only | Current target_slot preserves existing CHEBI assertions; groundable excludes conflicting corpus opinions, and apply_to_record fills ungrounded entries from proposals. This writer does not authenticate source amounts or automatically repair an existing wrong supplied-form ID. |
| writer55 | scripts/assign_culturemech_ids.py; assign_ids; _assign_id_to_file | context_only | Current assign_ids selects records with missing IDs; _assign_id_to_file checks new-ID collisions and appends identifier provenance. Identifier assignment does not authenticate recipe content or demonstrate historical source access. |
| writer56 | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group collapses equal duplicate values without summing them and retains the first conflicting value with a flag. This behavior is distinct from historical summed-amount artifacts and does not authenticate source-specific stock or product structure. |
| writer57 | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients; merge_ingredient_group | context_only | Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group retains the first concentration, flags differing values and selects the first CHEBI. It cannot establish source stages or justify collapsing independent supplemental and product-contained components. |
| writer58 | scripts/migrate_legacy_mim_to_chebi.py; _resolve_chebi; _rewrite_entry | context_only | Current _resolve_chebi reuses current primary CHEBI where available and considers bounded exact-name/synonym matches with a stereo-prefix guard; _rewrite_entry retains unresolved links. Current-row presence is distinct from historical validity and from source-specific supplied-form equivalence. |
| writer59 | scripts/migrate_ph_range.py; parse_ph_range; migrate_one | context_only | Current parse_ph_range retains qualifiers in notes and migrate_one converts only string-valued pH ranges, recording provenance. No particular source range is authenticated by this writer. |
| writer60 | scripts/promote_komodo_volume_candidates.py; promote_doc; main | context_only | Current promote_doc uses imported composition_confirms, fills only absent solution concentrations from CROSS_MEDIUM_INFERENCE candidates and records composition-match provenance. main retrieves the resolved provider source and computes agreement through imported helpers. Matching copied composition does not independently authenticate source identity or an assembled-medium denominator; those helper internals are separately scoped if inspected. |
| writer61 | scripts/refill_term_labels.py; refill_text | context_only | Current refill_text replaces term labels using the current exact identifier lookup while preserving other text. Canonical label correspondence is not an independent choice of the correct chemical form for the supplied source reagent. |
| writer62 | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata | context_only | Current DSMZCompositionResolver.merge_composition copies ingredients and solutions, fills pH when absent and copies physical/medium type, but does not copy preparation steps. _add_enrichment_metadata records a naive current timestamp. This explains a present omission risk, not historical execution. |
| writer63 | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current _convert_to_culturemech constructs source notes and default LIQUID with empty ingredients. Its time.strftime format contains %f, which is unsupported here and is consistent with literal .fZ in stored import events. Current code does not authenticate the original retrieval or justify rewriting historical time. |
| writer64 | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps | context_only | Current _parse_api_composition considers the primary recipe, prefers provider g_l when available and excludes four recognized water labels; tap water is not among those exclusions; _is_api_stock_addition distinguishes stock additions. _parse_api_solutions retains separate stock structure. _parse_preparation_steps collects solution prose. These present behaviors do not establish historical execution and cannot justify interpreting flattened stock rates as final-medium concentrations. |
| writer65 | src/culturemech/match/kg_media_matcher.py; extract_recipe_ingredients; find_matches; find_exact_match | context_only | Current extract_recipe_ingredients collects asserted CHEBI/FOODON IDs, find_matches compares set Jaccard and find_exact_match selects the first exact identifier set. Quantities, preparation and ungrounded ingredients are not compared, so an exact set match does not establish formulation identity. |
| writer66 | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current formulation_content retains exact scientific quantities, preparation and other scientific fields; merge_formulation_evidence rejects incompatible projections and unions evidence at matching scopes. A source-equivalence claim is not established by shared ingredient identities. |
| writer67 | src/culturemech/merge/matcher.py; group_formulations; group_recipes | context_only | Current group_formulations calls group_recipes with fail_on_invalid=True and FormulationFingerprinter. Expected standalone or unfingerprintable records are excluded; malformed or unexpected inputs raise. Valid records are grouped by full scientific content. This guard does not retrieve or authenticate source recipes. |
| writer68 | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group routes a single maintained owner with merge metadata; multiple owners pass through conservative merge_formulation_evidence. Regenerating from an unrepaired owner retains its defects. Current conservative behavior is credited and does not establish how the old generated record was produced. |
| writer69 | src/culturemech/validation/schema_defaulter.py; apply_defaults; _fix_ingredient; _fix_solution | context_only | Current apply_defaults, _fix_ingredient and _fix_solution can insert VARIABLE amounts and placeholder names for structural completeness. A default is not evidence for a dose, composition, solution identity or denominator; existing default-history events remain contextual. |
| historical-current-joins | REVIEW_WORK/batch076/record06/historical-current-joins.json; complete selected metadata and claims | supports | Three exact selected historical plan rows contain 200 claim entries. 102 literal and decoded API386 objects match current bytes; two parent digests match the current successful API386 capture. The third digest matches the API386a 404 error body, which authenticates that failure payload only. No attached formulation claims exist; neither match proves historical dates or execution. |
| composition-helper | scripts/fetch_komodo_base_volumes.py; record_composition; medium_composition; composition_agreement; composition_confirms; resolve_base; classify; main | supports | Full current module read. record_composition ignores units and stage while collecting ingredient and nested values; medium_composition optionally excludes cocktail-named stocks. composition_agreement accepts values within 0.1 percent, and composition_confirms requires all shared values to agree, at least eight shared and five non-cocktail compounds. resolve_base requires tracked and structural accession agreement. Those guards trace numeric copying but do not independently establish current taxonomy, variant identity or a final-medium denominator. No helper was executed. |
| quantity-inventory | REVIEW_WORK/batch076/record06/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- Exact current KOMODO386/386a/list access returned403; API386a returned404. Current386a PDF evidence does not resolve its historical Sulforhabdus identity.
- Provider942ml A and1006ml assembled sums are explicit bookkeeping, not independent final-volume measurements. HCl percentage basis and calcium pantothenate stereochemistry remain unresolved.
- DSM7269 override and current THIOVIBRIO386a quantities are context-only; no recipe transfer, source edit, historical timestamp rewrite or native formal save occurred.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T200326Z-desulfolutivibrio-medium-batch076
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of desulfolutivibrio_medium
started_at: '2026-10-28T19:41:00.946512Z'
finished_at: '2026-10-28T20:03:26.132461Z'
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
summary: The selected record flattens separate DSM386 A–F and stock bases, loses partial
  owner nesting, and conflates historical386a identity with a distinct current recipe.
  Correct retained preparation, five nested owner values and supplied hydrates are
  credited. Remaining preparation/form/provenance defects require scoped curation;
  current KOMODO and386a API limits prevent full identity authentication.
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
  - path: data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml
    sha256: dc3c79258641321ca3e5622c523a7b35a8ca0c6af4b0139f4f8f2e7fd2f041e6
    role: target
  - path: data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml
    sha256: 13b8fbb91bc0eb193927e85a3c7c211ad83d225379c234f7a3c462dd51aa5229
    role: context
  - path: data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml
    sha256: 77233b4862535fef0bbcc5bf2b245c64a978ccc58805203d949740f609851084
    role: context
  - path: data/normalized_yaml/bacterial/sulforhabdus_medium.yaml
    sha256: a1b9e697762097fe164c1273ebeefab75a49ad3e03865f99bb97e34729cc015b
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/inspected-candidate-context.json
    sha256: bea184ce1f011e5714cef082c0341aaf001d16024ef7935d004cbc8899f74fd5
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json
    sha256: 5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/desulfovibrio_sulfodismutans_medium.yaml.md
    sha256: ae20ec95ec58a1450196c83d494393c6213eca531f0ae84c7c9a8f5e3c51fe6f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/sulforhabdus_medium.yaml.md
    sha256: fb188cb74f11f17c77385fb0f165b66cf6115b03b20bf6fda98f3b294c88e031
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
    sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/desulfolutivibrio_medium.yaml.md
    sha256: 2a577eb33d737027eec8f24ebe5c08c0743878d8e84b6ca4155b2a7070c387fe
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.md
    sha256: 2969e2bcd8a064bf0cf6975bfa1e9547dedffc74f9d288c14fb0d124455c5d3a
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfolutivibrio_medium.md
    sha256: 393df8e06411b75c8307253e4806446e7ff58b219370739b316f39f4761603d3
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.md
    sha256: 02682d11e42a96dac2f773c581309d8d0142f9a72ad2e528f5db2e86dc442cae
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/sulforhabdus_medium.md
    sha256: d3a17a03ab901e14978365188d329ae627540f5e11b5bebec5c6c4a0c1036c20
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
  - path: scripts/fetch_komodo_base_volumes.py
    sha256: 9dad49c380422b2e7d3f40b4ff713d59360d22f6eec9b55068e050099cb9cffa
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
    claim; separately scoped source dependencies and current writers.
  selection: Authoritative batch076 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001493
targets:
- target_id: CultureMech:001493
  path: data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml
  label: desulfolutivibrio_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/sulforhabdus_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:001493
  command: just validate-schema data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:001493
  command: just validate-strict data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml
    --workers 1 --out REVIEW_WORK/batch076/record06/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:001493
  command: just validate-terms data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:001493
  command: just validate-references data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T19:51:11.459152Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: dc3c79258641321ca3e5622c523a7b35a8ca0c6af4b0139f4f8f2e7fd2f041e6
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T19:51:11.459351Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 13b8fbb91bc0eb193927e85a3c7c211ad83d225379c234f7a3c462dd51aa5229
- evidence_id: local2
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T19:51:11.459381Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 77233b4862535fef0bbcc5bf2b245c64a978ccc58805203d949740f609851084
- evidence_id: local3
  kind: record_content
  reference: data/normalized_yaml/bacterial/sulforhabdus_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T19:51:11.459406Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: a1b9e697762097fe164c1273ebeefab75a49ad3e03865f99bb97e34729cc015b
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch076/record06/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T19:41:02.229904Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: c071938a4b62d6eb014e1b425869b98b0c32a7d2791f71de54684c16dc8fb210
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch076/record06/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T19:41:03.240542Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: bdfa32edf8782f4b389814a659676e2e1f28de71f8369d7a3e5a9d59f29c08ea
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch076/record06/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T19:41:04.727946Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 193678cfaff8966a908ae654b3c9cbbbede169904edefcf7855ff767f47224f8
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch076/record06/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T19:41:05.639645Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: bdfd8053bf729148dc74543820c1c399b56bd3fa8b18a639d1e5992467309345
- evidence_id: dsm386
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T19:40:51.089581Z'
  support: supports
  summary: Complete exact DSM primary PDF text and every rendered page read, including
    main recipe, separate stock tables and all staged procedures. Physical LF line
    locators refer to the preserved pdftotext output.
  snapshot_sha256: d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7
- evidence_id: dsm386a
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T19:40:51.630425Z'
  support: supports
  summary: Complete exact DSM primary PDF text and every rendered page read, including
    main recipe, separate stock tables and all staged procedures. Physical LF line
    locators refer to the preserved pdftotext output.
  snapshot_sha256: 31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d
- evidence_id: api386
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/386
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T19:40:51.496406Z'
  support: supports
  summary: Complete current provider identity, solution tables and preparation read.
    Explicit g_l and declared volumes are credited only on their named provider stock
    or recipe basis; they are not independent measured final volumes. Provider mmol_l
    values are not adopted as chemical-form authority.
  snapshot_sha256: cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce
- evidence_id: api386a
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/386a
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T19:40:51.656680Z'
  support: unknown
  summary: Actual HTTP 404 response, not formulation evidence.
  snapshot_sha256: b5c9493e66496fb2c5d5e64c4bcf9675dd01382531706e8697e6092dc99dd8f1
- evidence_id: komodo386
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=386
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T19:40:51.505117Z'
  support: unknown
  summary: Actual HTTP 403 response, not formulation evidence.
  snapshot_sha256: b12dbd71902c6a39cb13b900bdff8d3e38ca2da025b347453f4a946f63f6985e
- evidence_id: komodo386a
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=386a
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T19:40:51.706054Z'
  support: unknown
  summary: Actual HTTP 403 response, not formulation evidence.
  snapshot_sha256: d4af9924c322255832f859e319bc42cd8b714c5e784c1bf82eda8efb774946c8
- evidence_id: komodoList
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T19:40:51.897243Z'
  support: unknown
  summary: Actual HTTP 403 response, not formulation evidence.
  snapshot_sha256: 279396e9ee39442de0eb68d6c966af8bef6a3896513379e1a2029d1257626d6d
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:41:44.457767Z'
  support: supports
  summary: OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4'];
    mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f2530ec9c15f59a3d132a466c9c3a899497bab0f85b996d3e27bef8612f89982
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:41:44.458106Z'
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
  accessed_at: '2026-10-28T19:41:44.458163Z'
  support: supports
  summary: OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic
    compound that consists of 2-oxohexahydro-1<em>H</em>-thieno[3,4-<em>d</em>]imidazole
    having a valeric acid substituent attached to the tetrahydrothiophene ring. The
    parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 5135a39e8b52c878896db22443f00507125db80e5ce4bb1dcc97914b9bdd7316
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:41:44.458220Z'
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
  accessed_at: '2026-10-28T19:41:45.214675Z'
  support: supports
  summary: OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic
    chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass
    ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:41:45.224872Z'
  support: supports
  summary: OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula
    ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: e0c2a85ab7be9313c564f96ee47b87e1bf3e01ad1e9fd627d1dbddced5d068c4
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:41:45.263161Z'
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
  accessed_at: '2026-10-28T19:41:45.299635Z'
  support: supports
  summary: OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The
    hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 855ea2cf0e89d25ab4a560ab1c2dab6ac861d215bc5473cb4d3a0a2d4cdff438
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:41:45.361734Z'
  support: supports
  summary: OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic
    chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:41:45.813904Z'
  support: supports
  summary: OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula
    ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: c3341e7cf8a7ea0768d505265376c1514f161c9048b6e878314e204341d702eb
- evidence_id: chebi32138
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32138
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:41:45.827742Z'
  support: supports
  summary: OLS current exact CHEBI:32138 = sodium acetate trihydrate; definition [];
    formula ['C2H3O2.3H2O.Na']; mass ['136.079']; obsolete=False. Literal label is
    distinct from supplied-form equivalence.
  snapshot_sha256: a85623bd501ec509db74e3ec861994a6e2b3c99b2542468162f19ec72891787d
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:41:45.907606Z'
  support: supports
  summary: OLS current exact CHEBI:32145 = sodium hydroxide; definition []; formula
    ['HO.Na']; mass ['39.997']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 089212e8c86e2d4a4b145366c8bc67e0056565ef6970dcdc3df63ad20dac234d
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:41:46.422823Z'
  support: supports
  summary: OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal
    chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:41:46.449313Z'
  support: supports
  summary: OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3'];
    mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:41:46.498559Z'
  support: supports
  summary: OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound
    of nickel and chloride in which the ratio of nickel (in the +2 oxidation state)
    to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: 3a37ef35991d24faf578286a7d7557ee1b0646c286dd3f8a555d833e6bf82a57
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:41:46.522826Z'
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
  accessed_at: '2026-10-28T19:41:46.574454Z'
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
  accessed_at: '2026-10-28T19:41:47.016490Z'
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
  accessed_at: '2026-10-28T19:41:47.016568Z'
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
  accessed_at: '2026-10-28T19:41:47.055757Z'
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
  accessed_at: '2026-10-28T19:41:47.177888Z'
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
  accessed_at: '2026-10-28T19:41:47.625700Z'
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
  accessed_at: '2026-10-28T19:41:47.629077Z'
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
  accessed_at: '2026-10-28T19:41:47.648768Z'
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
  accessed_at: '2026-10-28T19:41:47.703299Z'
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
  accessed_at: '2026-10-28T19:41:47.740457Z'
  support: supports
  summary: OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula
    ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi114786
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:114786
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:41:48.218849Z'
  support: supports
  summary: OLS current exact CHEBI:114786 = sodium disulfite; definition ['An inorganic
    sodium salt composed of sodium and disulfite ions in a 2:1 ratio.']; formula ['2Na.O5S2'];
    mass ['190.109']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: d6bfbf1a32be207566dd06d617593886daebf942281e7813b4c88a1dbbc5ff8a
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131361
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:41:48.219848Z'
  support: supports
  summary: OLS current exact CHEBI:131361 = disodium selenite pentahydrate; definition
    ['A hydrate that is the pentahydrate form of disodium selenite.']; formula ['5H2O.2Na.O3Se'];
    mass ['263.012']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: d88b30f797a300c3935e550a4770cb598bbed342a9c2a343f77bdce496e99db9
- evidence_id: chebi132751
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:132751
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:41:48.266670Z'
  support: supports
  summary: OLS current exact CHEBI:132751 = thiamine hydrochloride dihydrate; definition
    ['A hydrate that is the dihydrate form of thiamine hydrochloride.']; formula ['C12H18N4OS.2Cl.2H2O'];
    mass ['373.306']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 1d5eefc753b4fbbffd69d169aa7ca7be16df737b6c8c0e1833917806ac0607e5
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T19:41:48.303751Z'
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
  reference: REVIEW_WORK/batch076/record06/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T19:51:11.472130Z'
  support: supports
  summary: Complete selected and dependency-context term slots and current packaged
    MIM CSV exact-identifier joins with row locators and metadata commit; includes
    separately scoped dependency context. No fuzzy mapping or historical-validity
    inference.
  snapshot_sha256: b5b05e59ca4d0c70a0235e7d5f8586d47b06f2adfe56a03d0449971920c0009c
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/desulfovibrio_sulfodismutans_medium.yaml.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T19:51:11.528051Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: ae20ec95ec58a1450196c83d494393c6213eca531f0ae84c7c9a8f5e3c51fe6f
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/sulforhabdus_medium.yaml.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T19:51:11.528085Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: fb188cb74f11f17c77385fb0f165b66cf6115b03b20bf6fda98f3b294c88e031
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/desulfolutivibrio_medium.yaml.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T19:51:11.528132Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: 2a577eb33d737027eec8f24ebe5c08c0743878d8e84b6ca4155b2a7070c387fe
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T19:51:11.528161Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: 2969e2bcd8a064bf0cf6975bfa1e9547dedffc74f9d288c14fb0d124455c5d3a
- evidence_id: history4
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfolutivibrio_medium.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T19:51:11.528187Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: 393df8e06411b75c8307253e4806446e7ff58b219370739b316f39f4761603d3
- evidence_id: history5
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T19:51:11.528208Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: 02682d11e42a96dac2f773c581309d8d0142f9a72ad2e528f5db2e86dc442cae
- evidence_id: history6
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/sulforhabdus_medium.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T19:51:11.528233Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: d3a17a03ab901e14978365188d329ae627540f5e11b5bebec5c6c4a0c1036c20
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch076/record06/historical-authentication.json
  locator: attached_claims; historical_plan_claims
  accessed_at: '2026-10-28T19:51:11.528302Z'
  support: supports
  summary: Actual attached claims in scoped stock sections and historical parent-plan
    claims are separate populations. Current raw-digest equality and literal or normalized-HTML
    excerpt equality are independently recorded. No attached formulation claims occur
    on the selected target or its maintained contributors. Current byte matches do
    not authenticate historical execution or access dates.
  snapshot_sha256: 81d5f9335fd7498c972d8c3eea97ccd324bbc724ee952e40e16d634830d3ab4f
- evidence_id: writer54
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: target_slot; groundable; apply_to_record
  accessed_at: '2026-10-28T19:51:11.528381Z'
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
  accessed_at: '2026-10-28T19:51:11.528408Z'
  support: context_only
  summary: Current assign_ids selects records with missing IDs; _assign_id_to_file
    checks new-ID collisions and appends identifier provenance. Identifier assignment
    does not authenticate recipe content or demonstrate historical source access.
  snapshot_sha256: 81ed213c52804ae98a8add02730d757595e3287fa7b01bc88aee0e587bbb01e1
- evidence_id: writer56
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T19:51:11.528432Z'
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
  accessed_at: '2026-10-28T19:51:11.528455Z'
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
  accessed_at: '2026-10-28T19:51:11.528486Z'
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
  accessed_at: '2026-10-28T19:51:11.528511Z'
  support: context_only
  summary: Current parse_ph_range retains qualifiers in notes and migrate_one converts
    only string-valued pH ranges, recording provenance. No particular source range
    is authenticated by this writer.
  snapshot_sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
- evidence_id: writer60
  kind: record_content
  reference: scripts/promote_komodo_volume_candidates.py
  locator: promote_doc; main
  accessed_at: '2026-10-28T19:51:11.528537Z'
  support: context_only
  summary: Current promote_doc uses imported composition_confirms, fills only absent
    solution concentrations from CROSS_MEDIUM_INFERENCE candidates and records composition-match
    provenance. main retrieves the resolved provider source and computes agreement
    through imported helpers. Matching copied composition does not independently authenticate
    source identity or an assembled-medium denominator; those helper internals are
    separately scoped if inspected.
  snapshot_sha256: 2423b7e2e04011b31d21eac939714a2db4380f033a69094325dc567e44929cd2
- evidence_id: writer61
  kind: record_content
  reference: scripts/refill_term_labels.py
  locator: refill_text
  accessed_at: '2026-10-28T19:51:11.528563Z'
  support: context_only
  summary: Current refill_text replaces term labels using the current exact identifier
    lookup while preserving other text. Canonical label correspondence is not an independent
    choice of the correct chemical form for the supplied source reagent.
  snapshot_sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
- evidence_id: writer62
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata
  accessed_at: '2026-10-28T19:51:11.528599Z'
  support: context_only
  summary: Current DSMZCompositionResolver.merge_composition copies ingredients and
    solutions, fills pH when absent and copies physical/medium type, but does not
    copy preparation steps. _add_enrichment_metadata records a naive current timestamp.
    This explains a present omission risk, not historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer63
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T19:51:11.528626Z'
  support: context_only
  summary: Current _convert_to_culturemech constructs source notes and default LIQUID
    with empty ingredients. Its time.strftime format contains %f, which is unsupported
    here and is consistent with literal .fZ in stored import events. Current code
    does not authenticate the original retrieval or justify rewriting historical time.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer64
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps
  accessed_at: '2026-10-28T19:51:11.528656Z'
  support: context_only
  summary: Current _parse_api_composition considers the primary recipe, prefers provider
    g_l when available and excludes four recognized water labels; tap water is not
    among those exclusions; _is_api_stock_addition distinguishes stock additions.
    _parse_api_solutions retains separate stock structure. _parse_preparation_steps
    collects solution prose. These present behaviors do not establish historical execution
    and cannot justify interpreting flattened stock rates as final-medium concentrations.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer65
  kind: record_content
  reference: src/culturemech/match/kg_media_matcher.py
  locator: extract_recipe_ingredients; find_matches; find_exact_match
  accessed_at: '2026-10-28T19:51:11.528685Z'
  support: context_only
  summary: Current extract_recipe_ingredients collects asserted CHEBI/FOODON IDs,
    find_matches compares set Jaccard and find_exact_match selects the first exact
    identifier set. Quantities, preparation and ungrounded ingredients are not compared,
    so an exact set match does not establish formulation identity.
  snapshot_sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
- evidence_id: writer66
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T19:51:11.528709Z'
  support: context_only
  summary: Current formulation_content retains exact scientific quantities, preparation
    and other scientific fields; merge_formulation_evidence rejects incompatible projections
    and unions evidence at matching scopes. A source-equivalence claim is not established
    by shared ingredient identities.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer67
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations; group_recipes
  accessed_at: '2026-10-28T19:51:11.528729Z'
  support: context_only
  summary: Current group_formulations calls group_recipes with fail_on_invalid=True
    and FormulationFingerprinter. Expected standalone or unfingerprintable records
    are excluded; malformed or unexpected inputs raise. Valid records are grouped
    by full scientific content. This guard does not retrieve or authenticate source
    recipes.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer68
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T19:51:11.528751Z'
  support: context_only
  summary: Current merge_group routes a single maintained owner with merge metadata;
    multiple owners pass through conservative merge_formulation_evidence. Regenerating
    from an unrepaired owner retains its defects. Current conservative behavior is
    credited and does not establish how the old generated record was produced.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer69
  kind: record_content
  reference: src/culturemech/validation/schema_defaulter.py
  locator: apply_defaults; _fix_ingredient; _fix_solution
  accessed_at: '2026-10-28T19:51:11.528777Z'
  support: context_only
  summary: Current apply_defaults, _fix_ingredient and _fix_solution can insert VARIABLE
    amounts and placeholder names for structural completeness. A default is not evidence
    for a dose, composition, solution identity or denominator; existing default-history
    events remain contextual.
  snapshot_sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
- evidence_id: historical-current-joins
  kind: record_content
  reference: REVIEW_WORK/batch076/record06/historical-current-joins.json
  locator: complete selected metadata and claims
  accessed_at: '2026-10-28T19:51:11.529049Z'
  support: supports
  summary: Three exact selected historical plan rows contain 200 claim entries. 102
    literal and decoded API386 objects match current bytes; two parent digests match
    the current successful API386 capture. The third digest matches the API386a 404
    error body, which authenticates that failure payload only. No attached formulation
    claims exist; neither match proves historical dates or execution.
  snapshot_sha256: 1760489eccf605306fc3d8180a0d1544e7faf75c0f2d9ae13996fc72036e930b
- evidence_id: composition-helper
  kind: record_content
  reference: scripts/fetch_komodo_base_volumes.py
  locator: record_composition; medium_composition; composition_agreement; composition_confirms;
    resolve_base; classify; main
  accessed_at: '2026-10-28T19:51:11.529086Z'
  support: supports
  summary: Full current module read. record_composition ignores units and stage while
    collecting ingredient and nested values; medium_composition optionally excludes
    cocktail-named stocks. composition_agreement accepts values within 0.1 percent,
    and composition_confirms requires all shared values to agree, at least eight shared
    and five non-cocktail compounds. resolve_base requires tracked and structural
    accession agreement. Those guards trace numeric copying but do not independently
    establish current taxonomy, variant identity or a final-medium denominator. No
    helper was executed.
  snapshot_sha256: 9dad49c380422b2e7d3f40b4ff713d59360d22f6eec9b55068e050099cb9cffa
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch076/record06/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T19:51:11.579909Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: 486c9f430672a3d4c5b5f1d5d3105a232479924ea73d91909d07513a0a1b22e2
assessments:
- assessment_id: a1
  area: identity
  topic: Distinct DSM386 and historical/current386a identities
  outcome: concern
  summary: The DSM386 primary and API agree on a staged Desulfolutivibrio recipe.
    Historical KOMODO386 is named Desulfovibrio sulfodismutans;386a is named Sulforhabdus,
    but the current official386a PDF is THIOVIBRIO with a different formulation. Current
    KOMODO routes are403 and API386a is404. Local SOURCE_DUPLICATE relationships and
    copied values do not establish equivalence.
  target_ids:
  - CultureMech:001493
  evidence_ids:
  - local0
  - local1
  - local2
  - local3
  - dsm386
  - dsm386a
  - komodo386
  - komodo386a
  - api386a
  - historical-current-joins
- assessment_id: a2
  area: consistency
  topic: Classification and precise form limits
  outcome: supported
  summary: DEFINED and LIQUID are supported for the chemically specified DSM386 source,
    whose API says complex_medium no. That is source classification, not experimental
    growth evidence or proof of historical386a equivalence. Correct hydrate IDs for
    magnesium, acetate, sulfide, selenite, tungstate and thiamine remain credited.
    Calcium pantothenate31345 encodes D stereochemistry while the recipe names generic
    calcium pantothenate; its exact MIM preferred row is MAPPED but D,L and unrelated
    capsaicin-like synonyms in the index cannot establish source stereochemistry.
    Preserve that bounded unresolved specificity.
  target_ids:
  - CultureMech:001493
  evidence_ids:
  - dsm386
  - api386
  - grounding
  - chebi31345
- assessment_id: a3
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: Seven complete historical reports and three exact selected plan rows were
    read. Historical blanket main-rate conflicts are refined by actual source-stage
    joins, while the386a404 limitation remains. All102 non-null historical API object
    quotes and corresponding decoded objects match current386 bytes. Two parent digests
    authenticate the successful386 payload; the third authenticates only an unchanged386a404
    payload. Partial stock nesting and retained procedures are credited, without treating
    composition agreement as independent identity or volume evidence. Current conservative
    merging preserves scientific fields and rejects incompatible formulations. Inspected
    writer behavior is described separately by exact file and function; it does not
    prove historical execution.
  target_ids:
  - CultureMech:001493
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
  - writer69
  - historical-current-joins
  - composition-helper
- assessment_id: a4
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 124 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:001493
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:001493",
    "selected_concentration_field_count": 124, "selected_concentration_fields_covered":
    124, "decisions": [{"decision_id": "q1", "subject": "KH2PO4 root placement", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path":
    "ingredients[0].concentration", "original": {"value": "0.212314", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "0.212314",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "0.212314",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "0.212314",
    "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Solution A flattened
    to main recipe", "interpretation": "The printed batch amount and explicit provider
    g_l belong to Solution A, not the assembled main medium. The selected root/main
    placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a
    are inaccessible and the current386a PDF identifies a different recipe, so matching
    copied values cannot authenticate those branches. Provider Solution A volume is
    942 ml; its listed rate is distinct from the 1006 ml sum of A–F additions. ",
    "sources": [{"locator": "$.data.solutions[1].recipe[0]", "source_key": "api386",
    "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.212314,\n                        \"mmol_l\":
    1.56016,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 28-28", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   KH2PO4                                                 0.20        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject":
    "NH4Cl root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.265393",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.265393",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.265393",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.265393",
    "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Solution A flattened
    to main recipe", "interpretation": "The printed batch amount and explicit provider
    g_l belong to Solution A, not the assembled main medium. The selected root/main
    placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a
    are inaccessible and the current386a PDF identifies a different recipe, so matching
    copied values cannot authenticate those branches. Provider Solution A volume is
    942 ml; its listed rate is distinct from the 1006 ml sum of A–F additions. ",
    "sources": [{"locator": "$.data.solutions[1].recipe[1]", "source_key": "api386",
    "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.265393,\n                        \"mmol_l\":
    4.96154,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 29-29", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   NH4Cl                                                  0.25        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject":
    "NaCl root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1.06157",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1.06157",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1.06157",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1.06157",
    "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Solution A flattened
    to main recipe", "interpretation": "The printed batch amount and explicit provider
    g_l belong to Solution A, not the assembled main medium. The selected root/main
    placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a
    are inaccessible and the current386a PDF identifies a different recipe, so matching
    copied values cannot authenticate those branches. Provider Solution A volume is
    942 ml; its listed rate is distinct from the 1006 ml sum of A–F additions. ",
    "sources": [{"locator": "$.data.solutions[1].recipe[2]", "source_key": "api386",
    "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.06157,\n                        \"mmol_l\":
    18.1651,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 30-30", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   NaCl                                                   1.00        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject":
    "MgCl2 x 6 H2O root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.424628",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.424628",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.424628",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.424628",
    "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Solution A flattened
    to main recipe", "interpretation": "The printed batch amount and explicit provider
    g_l belong to Solution A, not the assembled main medium. The selected root/main
    placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a
    are inaccessible and the current386a PDF identifies a different recipe, so matching
    copied values cannot authenticate those branches. Provider Solution A volume is
    942 ml; its listed rate is distinct from the 1006 ml sum of A–F additions. ",
    "sources": [{"locator": "$.data.solutions[1].recipe[3]", "source_key": "api386",
    "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.424628,\n                        \"mmol_l\":
    2.08865,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 31-31", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   MgCl2
    x 6 H2O                                          0.40        g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q5", "subject": "KCl root placement",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.530786",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.530786",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.530786",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.530786",
    "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Solution A flattened
    to main recipe", "interpretation": "The printed batch amount and explicit provider
    g_l belong to Solution A, not the assembled main medium. The selected root/main
    placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a
    are inaccessible and the current386a PDF identifies a different recipe, so matching
    copied values cannot authenticate those branches. Provider Solution A volume is
    942 ml; its listed rate is distinct from the 1006 ml sum of A–F additions. ",
    "sources": [{"locator": "$.data.solutions[1].recipe[4]", "source_key": "api386",
    "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.530786,\n                        \"mmol_l\":
    7.11986,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 32-32", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   KCl                                                    0.50        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q6", "subject":
    "CaCl2 x 2 H2O root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.159236",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.159236",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.159236",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.159236",
    "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Solution A flattened
    to main recipe", "interpretation": "The printed batch amount and explicit provider
    g_l belong to Solution A, not the assembled main medium. The selected root/main
    placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a
    are inaccessible and the current386a PDF identifies a different recipe, so matching
    copied values cannot authenticate those branches. Provider Solution A volume is
    942 ml; its listed rate is distinct from the 1006 ml sum of A–F additions. ",
    "sources": [{"locator": "$.data.solutions[1].recipe[5]", "source_key": "api386",
    "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.159236,\n                        \"mmol_l\":
    1.08313,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 33-33", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   CaCl2
    x 2 H2O                                          0.15        g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q7", "subject": "Sodium resazurin
    root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.000530786",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.000530786",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.000530786",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.000530786",
    "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Solution A flattened
    to main recipe", "interpretation": "The printed batch amount and explicit provider
    g_l belong to Solution A, not the assembled main medium. The selected root/main
    placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a
    are inaccessible and the current386a PDF identifies a different recipe, so matching
    copied values cannot authenticate those branches. Provider Solution A volume is
    942 ml; its listed rate is distinct from the 1006 ml sum of A–F additions. The
    0.50 ml of 0.1% w/v contains 0.00050 g; division by provider 0.942 L gives the
    listed 0.000530786 g/L on its A basis only. ", "sources": [{"locator": "$.data.solutions[1].recipe[8]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000530786,\n                        \"mmol_l\": 0.00211325,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text physical LF lines 36-36", "source_key": "dsm386", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256":
    "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256":
    "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at":
    "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Sodium resazurin (0.1%
    w/v)                            0.50       ml", "quote_representation": "captured
    extracted text"}]}, {"decision_id": "q8", "subject": "Na2CO3 root placement",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Solution B flattened to main
    recipe", "interpretation": "The printed batch amount and explicit provider g_l
    belong to Solution B, not the assembled main medium. The selected root/main placement
    therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a
    are inaccessible and the current386a PDF identifies a different recipe, so matching
    copied values cannot authenticate those branches. Provider 50 g/L comes from 1.50
    g in Solution B with 30 ml water. ", "sources": [{"locator": "$.data.solutions[2].recipe[0]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\":
    471.752,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 42-42", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Na2CO3                                                  1.50       g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject":
    "Na-acetate x 3 H2O root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "30", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "30", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "30", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "30", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Solution C flattened to main
    recipe", "interpretation": "The printed batch amount and explicit provider g_l
    belong to Solution C, not the assembled main medium. The selected root/main placement
    therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a
    are inaccessible and the current386a PDF identifies a different recipe, so matching
    copied values cannot authenticate those branches. Provider 30 g/L comes from 0.30
    g in Solution C with 10 ml water. ", "sources": [{"locator": "$.data.solutions[3].recipe[0]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na-acetate x 3 H2O\",\n                        \"compound_id\":
    294,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 30,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text physical LF lines 48-48", "source_key": "dsm386", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256":
    "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256":
    "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at":
    "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Na-acetate x 3 H2O                                      0.30       g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q10", "subject":
    "Na2S2O5 root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "95", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "95", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "95", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "95", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Solution E flattened to main
    recipe", "interpretation": "The printed batch amount and explicit provider g_l
    belong to Solution E, not the assembled main medium. The selected root/main placement
    therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a
    are inaccessible and the current386a PDF identifies a different recipe, so matching
    copied values cannot authenticate those branches. Provider 95 g/L belongs to Solution
    E, 0.95 g with 10 ml water; repeated feeding is a separate procedure. ", "sources":
    [{"locator": "$.data.solutions[5].recipe[0]", "source_key": "api386", "reference":
    "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2S2O5\",\n                        \"compound_id\":
    440,\n                        \"attribute\": \"sodium pyrosulfite\",\n                        \"amount\":
    0.95,\n                        \"unit\": \"g\",\n                        \"g_l\":
    95,\n                        \"mmol_l\": 499.711,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text physical LF lines 64-64", "source_key": "dsm386", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256":
    "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256":
    "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at":
    "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Na2S2O5 (sodium pyrosulfite)                                0.95        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q11", "subject":
    "Na2S x 9 H2O root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "30.7692",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "30.7692",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "30.7692",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "30.7692",
    "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Solution F flattened
    to main recipe", "interpretation": "The printed batch amount and explicit provider
    g_l belong to Solution F, not the assembled main medium. The selected root/main
    placement therefore lacks a supported receiving-medium denominator. Current KOMODO386/386a
    are inaccessible and the current386a PDF identifies a different recipe, so matching
    copied values cannot authenticate those branches. Provider 30.7692 g/L belongs
    to Solution F, 0.40 g with 13 ml water. ", "sources": [{"locator": "$.data.solutions[6].recipe[0]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 30.7692,\n                        \"mmol_l\":
    128.108,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 72-72", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Na2S x
    9 H2O                                                0.40        g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q12", "subject": "HCl root placement",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "2.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "2.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "2.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "2.5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Trace element solution SL-10
    flattened to main recipe", "interpretation": "The printed batch amount and explicit
    provider g_l belong to Trace element solution SL-10, not the assembled main medium.
    The selected root/main placement therefore lacks a supported receiving-medium
    denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies
    a different recipe, so matching copied values cannot authenticate those branches.
    HCl is 10 ml of 25% with unspecified percentage basis; 2.5 g/L is explicit provider
    metadata, not a mass derived independently from that percentage. SL-10 has an
    explicit 1000 ml makeup, supporting its stock basis. ", "sources": [{"locator":
    "$.data.solutions[7].recipe[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text physical LF lines 78-78", "source_key": "dsm386", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256":
    "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256":
    "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at":
    "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   HCl (25%)                                                  10.00      ml",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q13", "subject": "FeCl2 x 4 H2O root placement",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Trace element solution SL-10
    flattened to main recipe", "interpretation": "The printed batch amount and explicit
    provider g_l belong to Trace element solution SL-10, not the assembled main medium.
    The selected root/main placement therefore lacks a supported receiving-medium
    denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies
    a different recipe, so matching copied values cannot authenticate those branches.
    SL-10 has an explicit 1000 ml makeup, supporting its stock basis. ", "sources":
    [{"locator": "$.data.solutions[7].recipe[1]", "source_key": "api386", "reference":
    "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 79-79", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   FeCl2
    x 4 H2O                                               1.50       g", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]", "source_key":
    "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q14", "subject": "FeCl2 x 4 H2O retained
    nested stock value", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "solutions[0].composition[0].concentration", "original": {"value":
    "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "solutions[0].composition[0].concentration", "original": {"value":
    "1.5", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Trace element
    solution SL-10", "interpretation": "Already nested component has the correct explicit
    provider stock rate and supplied batch amount. This newly attached review evidence
    supports that stock layer only; the partial stock membership, receiving dose and
    unverified KOMODO identity remain separate concerns.", "sources": [{"locator":
    "$.data.solutions[7].recipe[1]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 79-79", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   FeCl2
    x 4 H2O                                               1.50       g", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]", "source_key":
    "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q15", "subject": "ZnCl2 root placement",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Trace element solution SL-10
    flattened to main recipe", "interpretation": "The printed batch amount and explicit
    provider g_l belong to Trace element solution SL-10, not the assembled main medium.
    The selected root/main placement therefore lacks a supported receiving-medium
    denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies
    a different recipe, so matching copied values cannot authenticate those branches.
    SL-10 has an explicit 1000 ml makeup, supporting its stock basis. ", "sources":
    [{"locator": "$.data.solutions[7].recipe[2]", "source_key": "api386", "reference":
    "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 80-80", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   ZnCl2                                                      70.00      mg",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q16", "subject": "MnCl2 x 4 H2O root placement",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Trace element solution SL-10
    flattened to main recipe", "interpretation": "The printed batch amount and explicit
    provider g_l belong to Trace element solution SL-10, not the assembled main medium.
    The selected root/main placement therefore lacks a supported receiving-medium
    denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies
    a different recipe, so matching copied values cannot authenticate those branches.
    SL-10 has an explicit 1000 ml makeup, supporting its stock basis. ", "sources":
    [{"locator": "$.data.solutions[7].recipe[3]", "source_key": "api386", "reference":
    "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 81-81", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   MnCl2
    x 4 H2O                                             100.00      mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]", "source_key":
    "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q17", "subject": "H3BO3 root placement",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "0.006",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.006",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.006",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "0.006",
    "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Trace element solution
    SL-10 flattened to main recipe", "interpretation": "The printed batch amount and
    explicit provider g_l belong to Trace element solution SL-10, not the assembled
    main medium. The selected root/main placement therefore lacks a supported receiving-medium
    denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies
    a different recipe, so matching copied values cannot authenticate those branches.
    SL-10 has an explicit 1000 ml makeup, supporting its stock basis. ", "sources":
    [{"locator": "$.data.solutions[7].recipe[4]", "source_key": "api386", "reference":
    "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 82-82", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   H3BO3                                                       6.00      mg",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q18", "subject": "CoCl2 x 6 H2O root placement",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Trace element solution SL-10
    flattened to main recipe", "interpretation": "The printed batch amount and explicit
    provider g_l belong to Trace element solution SL-10, not the assembled main medium.
    The selected root/main placement therefore lacks a supported receiving-medium
    denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies
    a different recipe, so matching copied values cannot authenticate those branches.
    SL-10 has an explicit 1000 ml makeup, supporting its stock basis. ", "sources":
    [{"locator": "$.data.solutions[7].recipe[5]", "source_key": "api386", "reference":
    "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 83-83", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   CoCl2
    x 6 H2O                                             190.00      mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]", "source_key":
    "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q19", "subject": "CuCl2 x 2 H2O root placement",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.002",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.002",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.002",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.002",
    "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Trace element solution
    SL-10 flattened to main recipe", "interpretation": "The printed batch amount and
    explicit provider g_l belong to Trace element solution SL-10, not the assembled
    main medium. The selected root/main placement therefore lacks a supported receiving-medium
    denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies
    a different recipe, so matching copied values cannot authenticate those branches.
    SL-10 has an explicit 1000 ml makeup, supporting its stock basis. ", "sources":
    [{"locator": "$.data.solutions[7].recipe[6]", "source_key": "api386", "reference":
    "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 84-84", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   CuCl2
    x 2 H2O                                               2.00      mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]", "source_key":
    "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q20", "subject": "NiCl2 x 6 H2O root placement",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.024",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.024",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.024",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.024",
    "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Trace element solution
    SL-10 flattened to main recipe", "interpretation": "The printed batch amount and
    explicit provider g_l belong to Trace element solution SL-10, not the assembled
    main medium. The selected root/main placement therefore lacks a supported receiving-medium
    denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies
    a different recipe, so matching copied values cannot authenticate those branches.
    SL-10 has an explicit 1000 ml makeup, supporting its stock basis. ", "sources":
    [{"locator": "$.data.solutions[7].recipe[7]", "source_key": "api386", "reference":
    "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 85-85", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   NiCl2
    x 6 H2O                                              24.00      mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]", "source_key":
    "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q21", "subject": "Na2MoO4 x 2 H2O root
    placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.036",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.036",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.036",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.036",
    "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Trace element solution
    SL-10 flattened to main recipe", "interpretation": "The printed batch amount and
    explicit provider g_l belong to Trace element solution SL-10, not the assembled
    main medium. The selected root/main placement therefore lacks a supported receiving-medium
    denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies
    a different recipe, so matching copied values cannot authenticate those branches.
    SL-10 has an explicit 1000 ml makeup, supporting its stock basis. ", "sources":
    [{"locator": "$.data.solutions[7].recipe[8]", "source_key": "api386", "reference":
    "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 86-86", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Na2MoO4
    x 2 H2O                                            36.00      mg", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[7].steps[0]", "source_key":
    "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q22", "subject": "NaOH root placement",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Selenite-tungstate solution
    flattened to main recipe", "interpretation": "The printed batch amount and explicit
    provider g_l belong to Selenite-tungstate solution, not the assembled main medium.
    The selected root/main placement therefore lacks a supported receiving-medium
    denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies
    a different recipe, so matching copied values cannot authenticate those branches.
    The source gives 1000 ml stock water and the provider declares 1000 ml; these
    support the qualified provider stock rate, not a measured final volume. ", "sources":
    [{"locator": "$.data.solutions[8].recipe[0]", "source_key": "api386", "reference":
    "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    12.5009,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 95-95", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   NaOH                                                       0.50        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q23", "subject":
    "Na2SeO3 x 5 H2O root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "0.003",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.003",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.003",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "0.003",
    "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Selenite-tungstate
    solution flattened to main recipe", "interpretation": "The printed batch amount
    and explicit provider g_l belong to Selenite-tungstate solution, not the assembled
    main medium. The selected root/main placement therefore lacks a supported receiving-medium
    denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies
    a different recipe, so matching copied values cannot authenticate those branches.
    The source gives 1000 ml stock water and the provider declares 1000 ml; these
    support the qualified provider stock rate, not a measured final volume. ", "sources":
    [{"locator": "$.data.solutions[8].recipe[1]", "source_key": "api386", "reference":
    "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\":
    0.0114062,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 96-96", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Na2SeO3
    x 5 H2O                                            3.00       mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q24", "subject": "Na2WO4 x 2 H2O
    root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "0.004",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "0.004",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "0.004",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "0.004",
    "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Selenite-tungstate
    solution flattened to main recipe", "interpretation": "The printed batch amount
    and explicit provider g_l belong to Selenite-tungstate solution, not the assembled
    main medium. The selected root/main placement therefore lacks a supported receiving-medium
    denominator. Current KOMODO386/386a are inaccessible and the current386a PDF identifies
    a different recipe, so matching copied values cannot authenticate those branches.
    The source gives 1000 ml stock water and the provider declares 1000 ml; these
    support the qualified provider stock rate, not a measured final volume. ", "sources":
    [{"locator": "$.data.solutions[8].recipe[2]", "source_key": "api386", "reference":
    "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\":
    0.0121267,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 97-97", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Na2WO4
    x 2 H2O                                             4.00       mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q25", "subject": "Vitamin B12 root
    placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Seven vitamins solution flattened
    to main recipe", "interpretation": "The printed batch amount and explicit provider
    g_l belong to Seven vitamins solution, not the assembled main medium. The selected
    root/main placement therefore lacks a supported receiving-medium denominator.
    Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different
    recipe, so matching copied values cannot authenticate those branches. The source
    gives 1000 ml stock water and the provider declares 1000 ml; these support the
    qualified provider stock rate, not a measured final volume. ", "sources": [{"locator":
    "$.data.solutions[9].recipe[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.073779,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 103-103", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Vitamin
    B12                                               100.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q26", "subject": "Vitamin B12 retained
    nested stock value", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "solutions[1].composition[0].concentration", "original": {"value":
    "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "solutions[1].composition[0].concentration", "original": {"value":
    "0.1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Seven vitamins
    solution", "interpretation": "Already nested component has the correct explicit
    provider stock rate and supplied batch amount. This newly attached review evidence
    supports that stock layer only; the partial stock membership, receiving dose and
    unverified KOMODO identity remain separate concerns.", "sources": [{"locator":
    "$.data.solutions[9].recipe[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.073779,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 103-103", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Vitamin
    B12                                               100.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q27", "subject": "p-Aminobenzoic
    acid root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "0.08", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "0.08", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "0.08", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "0.08", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Seven vitamins solution flattened
    to main recipe", "interpretation": "The printed batch amount and explicit provider
    g_l belong to Seven vitamins solution, not the assembled main medium. The selected
    root/main placement therefore lacks a supported receiving-medium denominator.
    Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different
    recipe, so matching copied values cannot authenticate those branches. The source
    gives 1000 ml stock water and the provider declares 1000 ml; these support the
    qualified provider stock rate, not a measured final volume. ", "sources": [{"locator":
    "$.data.solutions[9].recipe[1]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 80,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\":
    0.583345,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 104-104", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   p-Aminobenzoic
    acid                                        80.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q28", "subject": "D-(+)-biotin
    root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[25].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[25].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Seven vitamins solution flattened
    to main recipe", "interpretation": "The printed batch amount and explicit provider
    g_l belong to Seven vitamins solution, not the assembled main medium. The selected
    root/main placement therefore lacks a supported receiving-medium denominator.
    Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different
    recipe, so matching copied values cannot authenticate those branches. The source
    gives 1000 ml stock water and the provider declares 1000 ml; these support the
    qualified provider stock rate, not a measured final volume. ", "sources": [{"locator":
    "$.data.solutions[9].recipe[2]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\":
    1359,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 105-105", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   D-(+)-biotin                                               20.00      mg",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q29", "subject":
    "Nicotinic acid root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Seven vitamins solution flattened
    to main recipe", "interpretation": "The printed batch amount and explicit provider
    g_l belong to Seven vitamins solution, not the assembled main medium. The selected
    root/main placement therefore lacks a supported receiving-medium denominator.
    Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different
    recipe, so matching copied values cannot authenticate those branches. The source
    gives 1000 ml stock water and the provider declares 1000 ml; these support the
    qualified provider stock rate, not a measured final volume. ", "sources": [{"locator":
    "$.data.solutions[9].recipe[3]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.62456,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 106-106", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Nicotinic
    acid                                            200.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q30", "subject": "Nicotinic acid
    retained nested stock value", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "solutions[1].composition[1].concentration", "original": {"value":
    "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "solutions[1].composition[1].concentration", "original": {"value":
    "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Seven vitamins
    solution", "interpretation": "Already nested component has the correct explicit
    provider stock rate and supplied batch amount. This newly attached review evidence
    supports that stock layer only; the partial stock membership, receiving dose and
    unverified KOMODO identity remain separate concerns.", "sources": [{"locator":
    "$.data.solutions[9].recipe[3]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.62456,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 106-106", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Nicotinic
    acid                                            200.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q31", "subject": "Calcium pantothenate
    root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[27].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[27].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Seven vitamins solution flattened
    to main recipe", "interpretation": "The printed batch amount and explicit provider
    g_l belong to Seven vitamins solution, not the assembled main medium. The selected
    root/main placement therefore lacks a supported receiving-medium denominator.
    Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different
    recipe, so matching copied values cannot authenticate those branches. The source
    gives 1000 ml stock water and the provider declares 1000 ml; these support the
    qualified provider stock rate, not a measured final volume. ", "sources": [{"locator":
    "$.data.solutions[9].recipe[4]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\":
    518,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.209849,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 107-107", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Calcium
    pantothenate                                      100.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q32", "subject": "Pyridoxine hydrochloride
    root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[28].concentration", "original": {"value": "0.3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[28].concentration", "original": {"value": "0.3", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Seven vitamins solution flattened
    to main recipe", "interpretation": "The printed batch amount and explicit provider
    g_l belong to Seven vitamins solution, not the assembled main medium. The selected
    root/main placement therefore lacks a supported receiving-medium denominator.
    Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different
    recipe, so matching copied values cannot authenticate those branches. The source
    gives 1000 ml stock water and the provider declares 1000 ml; these support the
    qualified provider stock rate, not a measured final volume. ", "sources": [{"locator":
    "$.data.solutions[9].recipe[5]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 300,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    1.45886,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 108-108", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Pyridoxine
    hydrochloride                                  300.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q33", "subject": "Pyridoxine hydrochloride
    retained nested stock value", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "solutions[1].composition[2].concentration", "original": {"value":
    "0.3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "solutions[1].composition[2].concentration", "original": {"value":
    "0.3", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Seven vitamins
    solution", "interpretation": "Already nested component has the correct explicit
    provider stock rate and supplied batch amount. This newly attached review evidence
    supports that stock layer only; the partial stock membership, receiving dose and
    unverified KOMODO identity remain separate concerns.", "sources": [{"locator":
    "$.data.solutions[9].recipe[5]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 300,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    1.45886,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 108-108", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Pyridoxine
    hydrochloride                                  300.00      mg", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q34", "subject": "Thiamine-HCl
    x 2 H2O root placement", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[29].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ingredients[29].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Seven vitamins solution flattened
    to main recipe", "interpretation": "The printed batch amount and explicit provider
    g_l belong to Seven vitamins solution, not the assembled main medium. The selected
    root/main placement therefore lacks a supported receiving-medium denominator.
    Current KOMODO386/386a are inaccessible and the current386a PDF identifies a different
    recipe, so matching copied values cannot authenticate those branches. The source
    gives 1000 ml stock water and the provider declares 1000 ml; these support the
    qualified provider stock rate, not a measured final volume. ", "sources": [{"locator":
    "$.data.solutions[9].recipe[6]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\":
    77,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    0.535761,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 116-116", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Thiamine-HCl
    x 2 H2O              200.00   mg", "quote_representation": "captured extracted
    text"}]}, {"decision_id": "q35", "subject": "Thiamine-HCl x 2 H2O retained nested
    stock value", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "solutions[1].composition[3].concentration", "original": {"value":
    "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "solutions[1].composition[3].concentration", "original": {"value":
    "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Seven vitamins
    solution", "interpretation": "Already nested component has the correct explicit
    provider stock rate and supplied batch amount. This newly attached review evidence
    supports that stock layer only; the partial stock membership, receiving dose and
    unverified KOMODO identity remain separate concerns.", "sources": [{"locator":
    "$.data.solutions[9].recipe[6]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\":
    77,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    0.535761,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 116-116", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Thiamine-HCl
    x 2 H2O              200.00   mg", "quote_representation": "captured extracted
    text"}]}, {"decision_id": "q36", "subject": "desulfolutivibrio_medium stock 0
    receiving dose", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "solutions[0].concentration", "original": {"value": "1", "unit":
    "ML_PER_L"}}], "decision": "unsupported", "stage": "receiving dose versus per-litre
    rate", "interpretation": "The source specifies a 1 ml batch addition, not an unqualified
    1 ml per litre. SL-10 enters Solution A; vitamins enter as Solution D. The A–F
    additions sum to 1006 ml on the declared provider basis, with no measured assembled
    final volume. Preserve exact batch stages and qualify any derived rate; a composition-match
    promotion does not establish this denominator.", "sources": [{"locator": "$.data.solutions[1].recipe[6]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 34-34", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Trace
    element solution SL-10                           1.00       ml", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 3-8",
    "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution
    A                                           942.00       ml\n   Solution B                                            30.00       ml\n   Solution
    C                                            10.00       ml\n   Solution D                                             1.00       ml\n   Solution
    E                                            10.00       ml\n   Solution F                                            13.00       ml",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q37", "subject":
    "desulfolutivibrio_medium stock 0 preparation note", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path":
    "solutions[0].preparation_notes", "original": "Stock prepared in 1000 ml; added
    at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."}],
    "decision": "unsupported", "stage": "retained numeric stock note", "interpretation":
    "The retained 1000 ml stock basis is supported: explicit makeup for SL-10, declared
    water/provider volume for vitamins. The added per-litre claim is unsupported and
    must retain the distinct batch-dose limit.", "sources": [{"locator": "$.data.solutions[7].steps[0]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q38", "subject": "desulfolutivibrio_medium
    stock 1 receiving dose", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "solutions[1].concentration", "original": {"value": "1", "unit":
    "ML_PER_L"}}], "decision": "unsupported", "stage": "receiving dose versus per-litre
    rate", "interpretation": "The source specifies a 1 ml batch addition, not an unqualified
    1 ml per litre. SL-10 enters Solution A; vitamins enter as Solution D. The A–F
    additions sum to 1006 ml on the declared provider basis, with no measured assembled
    final volume. Preserve exact batch stages and qualify any derived rate; a composition-match
    promotion does not establish this denominator.", "sources": [{"locator": "$.data.solutions[4].recipe[0]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\":
    1038,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 59-59", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Seven
    vitamins solution                                     1.00       ml", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 3-8",
    "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution
    A                                           942.00       ml\n   Solution B                                            30.00       ml\n   Solution
    C                                            10.00       ml\n   Solution D                                             1.00       ml\n   Solution
    E                                            10.00       ml\n   Solution F                                            13.00       ml",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q39", "subject":
    "desulfolutivibrio_medium stock 1 preparation note", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path":
    "solutions[1].preparation_notes", "original": "Stock prepared in 1000 ml; added
    at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."}],
    "decision": "unsupported", "stage": "retained numeric stock note", "interpretation":
    "The retained 1000 ml stock basis is supported: explicit makeup for SL-10, declared
    water/provider volume for vitamins. The added per-litre claim is unsupported and
    must retain the distinct batch-dose limit.", "sources": [{"locator": "$.data.solutions[9].recipe[7]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 117-117", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled
    water                  1000.00   ml", "quote_representation": "captured extracted
    text"}]}, {"decision_id": "q40", "subject": "desulfovibrio_sulfodismutans_medium
    stock 0 receiving dose", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "solutions[0].concentration", "original": {"value": "1", "unit":
    "ML_PER_L"}}], "decision": "unsupported", "stage": "receiving dose versus per-litre
    rate", "interpretation": "The source specifies a 1 ml batch addition, not an unqualified
    1 ml per litre. SL-10 enters Solution A; vitamins enter as Solution D. The A–F
    additions sum to 1006 ml on the declared provider basis, with no measured assembled
    final volume. Preserve exact batch stages and qualify any derived rate; a composition-match
    promotion does not establish this denominator.", "sources": [{"locator": "$.data.solutions[1].recipe[6]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 34-34", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Trace
    element solution SL-10                           1.00       ml", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 3-8",
    "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution
    A                                           942.00       ml\n   Solution B                                            30.00       ml\n   Solution
    C                                            10.00       ml\n   Solution D                                             1.00       ml\n   Solution
    E                                            10.00       ml\n   Solution F                                            13.00       ml",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q41", "subject":
    "desulfovibrio_sulfodismutans_medium stock 0 preparation note", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "solutions[0].preparation_notes", "original": "Stock prepared in
    1000 ml. Composition and volume from medium 386''s own MediaDive recipe, identified
    by this record reproducing that medium''s composition exactly (30/30 shared compounds
    at identical values) despite the upstream rename to ''DESULFOLUTIVIBRIO MEDIUM''
    (#262)."}], "decision": "evidence_only", "stage": "retained numeric stock note",
    "interpretation": "The retained 1000 ml stock basis is supported: explicit makeup
    for SL-10, declared water/provider volume for vitamins. The note accurately records
    a historical 30/30 numerical comparison, which is not independent current identity
    or receiving-volume proof; do not transfer that inference beyond its scope.",
    "sources": [{"locator": "$.data.solutions[7].steps[0]", "source_key": "api386",
    "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q42", "subject": "desulfovibrio_sulfodismutans_medium
    stock 1 receiving dose", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "solutions[1].concentration", "original": {"value": "1", "unit":
    "ML_PER_L"}}], "decision": "unsupported", "stage": "receiving dose versus per-litre
    rate", "interpretation": "The source specifies a 1 ml batch addition, not an unqualified
    1 ml per litre. SL-10 enters Solution A; vitamins enter as Solution D. The A–F
    additions sum to 1006 ml on the declared provider basis, with no measured assembled
    final volume. Preserve exact batch stages and qualify any derived rate; a composition-match
    promotion does not establish this denominator.", "sources": [{"locator": "$.data.solutions[4].recipe[0]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\":
    1038,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 59-59", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Seven
    vitamins solution                                     1.00       ml", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text physical LF lines 3-8",
    "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution
    A                                           942.00       ml\n   Solution B                                            30.00       ml\n   Solution
    C                                            10.00       ml\n   Solution D                                             1.00       ml\n   Solution
    E                                            10.00       ml\n   Solution F                                            13.00       ml",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q43", "subject":
    "desulfovibrio_sulfodismutans_medium stock 1 preparation note", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "solutions[1].preparation_notes", "original": "Stock prepared in
    1000 ml. Composition and volume from medium 386''s own MediaDive recipe, identified
    by this record reproducing that medium''s composition exactly (30/30 shared compounds
    at identical values) despite the upstream rename to ''DESULFOLUTIVIBRIO MEDIUM''
    (#262)."}], "decision": "evidence_only", "stage": "retained numeric stock note",
    "interpretation": "The retained 1000 ml stock basis is supported: explicit makeup
    for SL-10, declared water/provider volume for vitamins. The note accurately records
    a historical 30/30 numerical comparison, which is not independent current identity
    or receiving-volume proof; do not transfer that inference beyond its scope.",
    "sources": [{"locator": "$.data.solutions[9].recipe[7]", "source_key": "api386",
    "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 117-117", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled
    water                  1000.00   ml", "quote_representation": "captured extracted
    text"}]}, {"decision_id": "q44", "subject": "Source A–F addition Solution A",
    "local_fields": [], "decision": "add", "stage": "assembled DSM386 batch", "interpretation":
    "Preserve this exact staged batch addition. The six values total 1006 ml; their
    sum is provider bookkeeping, not an independently measured final volume. No automatic
    conversion into local final-medium rates is proposed.", "sources": [{"locator":
    "$.data.solutions[0].recipe[0]", "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\":
    779,\n                        \"amount\": 942,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 3-3", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution
    A                                           942.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q45", "subject": "Source A–F addition
    Solution B", "local_fields": [], "decision": "add", "stage": "assembled DSM386
    batch", "interpretation": "Preserve this exact staged batch addition. The six
    values total 1006 ml; their sum is provider bookkeeping, not an independently
    measured final volume. No automatic conversion into local final-medium rates is
    proposed.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key":
    "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\":
    783,\n                        \"amount\": 30,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 4-4", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution
    B                                            30.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q46", "subject": "Source A–F addition
    Solution C", "local_fields": [], "decision": "add", "stage": "assembled DSM386
    batch", "interpretation": "Preserve this exact staged batch addition. The six
    values total 1006 ml; their sum is provider bookkeeping, not an independently
    measured final volume. No automatic conversion into local final-medium rates is
    proposed.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key":
    "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\":
    782,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 5-5", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution
    C                                            10.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q47", "subject": "Source A–F addition
    Solution D", "local_fields": [], "decision": "add", "stage": "assembled DSM386
    batch", "interpretation": "Preserve this exact staged batch addition. The six
    values total 1006 ml; their sum is provider bookkeeping, not an independently
    measured final volume. No automatic conversion into local final-medium rates is
    proposed.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key":
    "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\":
    784,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 6-6", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution
    D                                             1.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q48", "subject": "Source A–F addition
    Solution E", "local_fields": [], "decision": "add", "stage": "assembled DSM386
    batch", "interpretation": "Preserve this exact staged batch addition. The six
    values total 1006 ml; their sum is provider bookkeeping, not an independently
    measured final volume. No automatic conversion into local final-medium rates is
    proposed.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key":
    "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"solution\": \"Solution E\",\n                        \"solution_id\":
    786,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 7-7", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution
    E                                            10.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q49", "subject": "Source A–F addition
    Solution F", "local_fields": [], "decision": "add", "stage": "assembled DSM386
    batch", "interpretation": "Preserve this exact staged batch addition. The six
    values total 1006 ml; their sum is provider bookkeeping, not an independently
    measured final volume. No automatic conversion into local final-medium rates is
    proposed.", "sources": [{"locator": "$.data.solutions[0].recipe[5]", "source_key":
    "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Solution F\",\n                        \"solution_id\":
    785,\n                        \"amount\": 13,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 8-8", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Solution
    F                                            13.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q50", "subject": "Solution A water",
    "local_fields": [], "decision": "add", "stage": "source-only solvent", "interpretation":
    "Retain the exact source solvent quantity at this solution stage. Except the explicit
    SL-10 makeup, a water input is not a measured final solution volume; preserve
    the separately stated provider basis.", "sources": [{"locator": "$.data.solutions[1].recipe[9]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 940,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 37-37", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled
    water                                      940.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q51", "subject": "Solution B water",
    "local_fields": [], "decision": "add", "stage": "source-only solvent", "interpretation":
    "Retain the exact source solvent quantity at this solution stage. Except the explicit
    SL-10 makeup, a water input is not a measured final solution volume; preserve
    the separately stated provider basis.", "sources": [{"locator": "$.data.solutions[2].recipe[1]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 30,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 43-43", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled
    water                                        30.00      ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q52", "subject": "Solution C water",
    "local_fields": [], "decision": "add", "stage": "source-only solvent", "interpretation":
    "Retain the exact source solvent quantity at this solution stage. Except the explicit
    SL-10 makeup, a water input is not a measured final solution volume; preserve
    the separately stated provider basis.", "sources": [{"locator": "$.data.solutions[3].recipe[1]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 49-49", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled
    water                                        10.00      ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q53", "subject": "Solution E water",
    "local_fields": [], "decision": "add", "stage": "source-only solvent", "interpretation":
    "Retain the exact source solvent quantity at this solution stage. Except the explicit
    SL-10 makeup, a water input is not a measured final solution volume; preserve
    the separately stated provider basis.", "sources": [{"locator": "$.data.solutions[5].recipe[1]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 65-65", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled
    water                                            10.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q54", "subject": "Solution F water",
    "local_fields": [], "decision": "add", "stage": "source-only solvent", "interpretation":
    "Retain the exact source solvent quantity at this solution stage. Except the explicit
    SL-10 makeup, a water input is not a measured final solution volume; preserve
    the separately stated provider basis.", "sources": [{"locator": "$.data.solutions[6].recipe[1]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 13,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 73-73", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled
    water                                            13.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q55", "subject": "Trace element
    solution SL-10 water", "local_fields": [], "decision": "add", "stage": "source-only
    solvent", "interpretation": "Retain the exact source solvent quantity at this
    solution stage. Except the explicit SL-10 makeup, a water input is not a measured
    final solution volume; preserve the separately stated provider basis.", "sources":
    [{"locator": "$.data.solutions[7].recipe[9]", "source_key": "api386", "reference":
    "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 990,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 87-87", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled
    water                                           990.00      ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q56", "subject": "Selenite-tungstate
    solution water", "local_fields": [], "decision": "add", "stage": "source-only
    solvent", "interpretation": "Retain the exact source solvent quantity at this
    solution stage. Except the explicit SL-10 makeup, a water input is not a measured
    final solution volume; preserve the separately stated provider basis.", "sources":
    [{"locator": "$.data.solutions[8].recipe[3]", "source_key": "api386", "reference":
    "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 98-98", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled
    water                                         1000.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q57", "subject": "Seven vitamins
    solution water", "local_fields": [], "decision": "add", "stage": "source-only
    solvent", "interpretation": "Retain the exact source solvent quantity at this
    solution stage. Except the explicit SL-10 makeup, a water input is not a measured
    final solution volume; preserve the separately stated provider basis.", "sources":
    [{"locator": "$.data.solutions[9].recipe[7]", "source_key": "api386", "reference":
    "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 117-117", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Distilled
    water                  1000.00   ml", "quote_representation": "captured extracted
    text"}]}, {"decision_id": "q58", "subject": "Missing structured selenite-tungstate
    addition", "local_fields": [], "decision": "add", "stage": "Solution A receiving
    stock", "interpretation": "The source adds 1 ml of its separate selenite-tungstate
    solution to A. Its three compound stock rates remain root-level locally; retain
    this dose distinctly from a per-litre or final-medium concentration.", "sources":
    [{"locator": "$.data.solutions[1].recipe[7]", "source_key": "api386", "reference":
    "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 35-35", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "   Selenite-tungstate
    solution                            1.00       ml", "quote_representation": "captured
    extracted text"}]}, {"decision_id": "q59", "subject": "Retained staged preparation",
    "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "preparation_steps[0].description", "original": "Solution A is sparged
    80% N2 and 20% CO2 gas mixture for 30 – 45 min to make it anoxic, then distributed
    under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and
    autoclaved. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas mixture.
    Solutions C and F are autoclaved under 100% N2 gas. \r\nSolutions D and E are
    prepared under 100% N2 gas atmosphere and sterilized by filtration. To complete
    the medium appropriate amounts of the solutions B to F are added to the sterile
    solution A in the sequence as indicated. Final pH of the medium should be at 7.1
    - 7.4."}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "preparation_steps[0].description", "original": "Solution A is sparged
    80% N2 and 20% CO2 gas mixture for 30 – 45 min to make it anoxic, then distributed
    under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and
    autoclaved. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas mixture.
    Solutions C and F are autoclaved under 100% N2 gas. \r\nSolutions D and E are
    prepared under 100% N2 gas atmosphere and sterilized by filtration. To complete
    the medium appropriate amounts of the solutions B to F are added to the sterile
    solution A in the sequence as indicated. Final pH of the medium should be at 7.1
    - 7.4."}], "decision": "evidence_only", "stage": "DSM386 preparation", "interpretation":
    "The target and DSM owner retain the complete 80/20 gas mixture, 30–45 minutes,
    separate 100% N2 branches, filtration and ordered additions. Preserve this text;
    its single AUTOCLAVE action cannot represent the distinct filtration steps, and
    the KOMODO owner lacks the procedure.", "sources": [{"locator": "$.data.solutions[0].steps[0]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\":
    \"Solution A is sparged 80% N2 and 20% CO2 gas mixture for 30 \\u2013 45 min to
    make it anoxic, then distributed under the same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclaved. Solution B is autoclaved separately under
    80% N2 and 20% CO2 gas mixture. Solutions C and F are autoclaved under 100% N2
    gas. \\r\\nSolutions D and E are prepared under 100% N2 gas atmosphere and sterilized
    by filtration. To complete the medium appropriate amounts of the solutions B to
    F are added to the sterile solution A in the sequence as indicated. Final pH of
    the medium should be at 7.1 - 7.4.\"\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 10-16", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "1. Solution
    A is sparged 80% N2 and 20% CO2 gas mixture for 30 – 45 min to make it\nanoxic,
    then distributed under the same gas atmosphere into anoxic Hungate-type tubes\nor
    serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and
    20%\nCO2 gas mixture. Solutions C and F are autoclaved under 100% N2 gas. Solutions
    D and E\nare prepared under 100% N2 gas atmosphere and sterilized by filtration.
    To complete the\nmedium appropriate amounts of the solutions B to F are added
    to the sterile solution A in\nthe sequence as indicated. Final pH of the medium
    should be at 7.1 - 7.4.", "quote_representation": "captured extracted text"}]},
    {"decision_id": "q60", "subject": "Retained staged action", "local_fields": [{"record_path":
    "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path": "preparation_steps[0].action",
    "original": "AUTOCLAVE"}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "preparation_steps[0].action", "original": "AUTOCLAVE"}], "decision":
    "unsupported", "stage": "mixed preparation operations", "interpretation": "AUTOCLAVE
    applies to only part of the retained paragraph; D/E require filtration. Split
    the supported operations without inventing autoclave temperature or duration.",
    "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api386",
    "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\":
    \"Solution A is sparged 80% N2 and 20% CO2 gas mixture for 30 \\u2013 45 min to
    make it anoxic, then distributed under the same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclaved. Solution B is autoclaved separately under
    80% N2 and 20% CO2 gas mixture. Solutions C and F are autoclaved under 100% N2
    gas. \\r\\nSolutions D and E are prepared under 100% N2 gas atmosphere and sterilized
    by filtration. To complete the medium appropriate amounts of the solutions B to
    F are added to the sterile solution A in the sequence as indicated. Final pH of
    the medium should be at 7.1 - 7.4.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q61", "subject": "Retained subsequent pyrosulfite
    feed", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "preparation_steps[1].description", "original": "Note: When growth
    has started feed culture again with same amount of pyrosulfite. After a further
    two days repeat feeding once more."}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "preparation_steps[1].description", "original": "Note: When growth
    has started feed culture again with same amount of pyrosulfite. After a further
    two days repeat feeding once more."}], "decision": "evidence_only", "stage": "post-growth
    source procedure", "interpretation": "The exact same-amount feed and further-two-days
    repeat are already retained. Preserve their stage; do not sum them into the initial
    recipe concentration.", "sources": [{"locator": "$.data.solutions[0].steps[1]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\":
    \"Note: When growth has started feed culture again with same amount of pyrosulfite.
    After a further two days repeat feeding once more.\"\n                    }",
    "quote_representation": "raw JSON object"}, {"locator": "extracted-text physical
    LF lines 17-18", "source_key": "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "2. Note:
    When growth has started feed culture again with same amount of pyrosulfite.\nAfter
    a further two days repeat feeding once more.", "quote_representation": "captured
    extracted text"}]}, {"decision_id": "q62", "subject": "Stock procedure at main
    scope 2", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "preparation_steps[2].description", "original": "Adjust pH to 7.5-8.0
    with NaOH."}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "preparation_steps[2].description", "original": "Adjust pH to 7.5-8.0
    with NaOH."}], "decision": "unsupported", "stage": "stock-specific procedure",
    "interpretation": "The correct existing procedure belongs only to Solution E.
    Preserve its numeric control while relocating its scope; it is not a second final-medium
    pH or final-medium makeup.", "sources": [{"locator": "$.data.solutions[5].steps[0]",
    "source_key": "api386", "reference": "https://mediadive.dsmz.de/rest/medium/386",
    "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH to 7.5-8.0 with NaOH.\"\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 67-67", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "Adjust pH
    to 7.5-8.0 with NaOH.", "quote_representation": "captured extracted text"}]},
    {"decision_id": "q63", "subject": "Stock procedure at main scope 3", "local_fields":
    [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml", "field_path":
    "preparation_steps[3].description", "original": "First dissolve FeCl2 in the HCl,
    then dilute in water, add and dissolve the other salts. Finally make up to 1000.00
    ml."}, {"record_path": "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml",
    "field_path": "preparation_steps[3].description", "original": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally
    make up to 1000.00 ml."}], "decision": "unsupported", "stage": "stock-specific
    procedure", "interpretation": "The correct existing procedure belongs only to
    Trace element solution SL-10. Preserve its numeric control while relocating its
    scope; it is not a second final-medium pH or final-medium makeup.", "sources":
    [{"locator": "$.data.solutions[7].steps[0]", "source_key": "api386", "reference":
    "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "source_text_sha256": "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce",
    "accessed_at": "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text physical LF lines 89-90", "source_key":
    "dsm386", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf",
    "source_raw_sha256": "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7",
    "source_text_sha256": "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4",
    "accessed_at": "2026-10-28T19:40:51.089581Z", "exact_source_quote": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake
    up to 1000.00 ml.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q64", "subject": "DSM386 final pH ranges", "local_fields": [{"record_path": "data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml",
    "field_path": "ph_range", "original": {"min": 7.1, "max": 7.4}}, {"record_path":
    "data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml", "field_path":
    "ph_range", "original": {"min": 7.1, "max": 7.4}}, {"record_path": "data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml",
    "field_path": "ph_range", "original": {"min": 7.1, "max": 7.4}}], "decision":
    "evidence_only", "stage": "complete DSM386 medium", "interpretation": "The retained
    7.1–7.4 range is supported by the DSM386 primary/API. The copied KOMODO value
    remains a historical match, not fresh authentication of its inaccessible route.",
    "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api386",
    "reference": "https://mediadive.dsmz.de/rest/medium/386", "source_raw_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "source_text_sha256":
    "cc870fc1967609d94d52b3beab5af49d253c1bf4ee14d25dd6471e1d713bacce", "accessed_at":
    "2026-10-28T19:40:51.496406Z", "exact_source_quote": "{\n                        \"step\":
    \"Solution A is sparged 80% N2 and 20% CO2 gas mixture for 30 \\u2013 45 min to
    make it anoxic, then distributed under the same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclaved. Solution B is autoclaved separately under
    80% N2 and 20% CO2 gas mixture. Solutions C and F are autoclaved under 100% N2
    gas. \\r\\nSolutions D and E are prepared under 100% N2 gas atmosphere and sterilized
    by filtration. To complete the medium appropriate amounts of the solutions B to
    F are added to the sterile solution A in the sequence as indicated. Final pH of
    the medium should be at 7.1 - 7.4.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q65", "subject": "Historical Sulforhabdus
    pH", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/sulforhabdus_medium.yaml",
    "field_path": "ph_range", "original": {"min": 7.2, "max": 7.5}}], "decision":
    "unsupported", "stage": "unresolved386a identity", "interpretation": "The local
    7.2–7.5 is historical Sulforhabdus metadata. Current DSM386a is THIOVIBRIO with
    pH7.0, so preserve the conflict without automatically substituting another recipe
    or its pH.", "sources": [{"locator": "extracted-text physical LF lines 1-1", "source_key":
    "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf",
    "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d",
    "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801",
    "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "386a: THIOVIBRIO
    MEDIUM", "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    physical LF lines 9-17", "source_key": "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf",
    "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d",
    "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801",
    "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Solution
    A is sparged with 80% N2 and 20% CO2 gas mixture for 30 – 45 min to make it\nanoxic,
    then distributed under the same gas atmosphere into anoxic Hungate-type tubes\nor
    serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and
    20%\nCO2 gas mixture. Solutions C and D are prepared under a 100% N2 gas atmosphere
    and\nsterilized by filtration. To complete the medium solutions B to D are added
    to the sterile\nsolution A in the sequence as indicated. Before inoculation, appropriate
    amounts of sterile\nsulfur are added to the vials with the medium. Sulfur is sterilized
    by steaming for 3 hours\non each of 3 successive days (see medium 35) and added
    aseptically to the sterile\nmedium while retaining anoxic conditions. The final
    pH of the medium should be at 7.0.", "quote_representation": "captured extracted
    text"}]}, {"decision_id": "q66", "subject": "DSM7269-only alternative", "local_fields":
    [], "decision": "not_assessed", "stage": "strain-specific source override", "interpretation":
    "The exact source-only 2.50 g/L thiosulfate pentahydrate replacement and post-autoclave
    stock addition apply only to named DSM7269. They are retained as excluded variant
    context, not proposed for the generic selected medium.", "sources": [{"locator":
    "extracted-text physical LF lines 21-22", "source_key": "dsm386", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386.pdf", "source_raw_sha256":
    "d7ff555e0475f73f90e82b3f65796465c71139bb3a1fb58cf4658269b13654f7", "source_text_sha256":
    "1909e3056693b629b4e2d648277deabeec3cea2a38bcab69f497e89c48b2d5b4", "accessed_at":
    "2026-10-28T19:40:51.089581Z", "exact_source_quote": "For DSM 7269: Replace pyrosulfite
    with 2.50 g/l Na2S2O3 x 5 H2O added to the medium\nafter autoclaving from a sterile
    anoxic stock solution.", "quote_representation": "captured extracted text"}]},
    {"decision_id": "q67", "subject": "Current386a Main staged additions and sulfur",
    "local_fields": [], "decision": "not_assessed", "stage": "distinct current THIOVIBRIO
    recipe", "interpretation": "All printed amounts and controls in this source section
    are retained as exact identity/comparison evidence only. They cannot be transferred
    to historical Sulforhabdus or generic DSM386. For the washed Fe(OH)3 precipitate,
    discarded supernatant and unspecified resuspension preclude final suspension mass-balance
    inference.", "sources": [{"locator": "extracted-text physical LF lines 3-7", "source_key":
    "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf",
    "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d",
    "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801",
    "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "   Solution
    A                                             967.00       ml\n   Solution B                                              30.00       ml\n   Solution
    C                                               1.00       ml\n   Solution D                                              10.00       ml\n   Sulfur
    (powdered)                                       10.00        g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q68", "subject": "Current386a Main
    atmosphere, sulfur sterilization and pH controls", "local_fields": [], "decision":
    "not_assessed", "stage": "distinct current THIOVIBRIO recipe", "interpretation":
    "All printed amounts and controls in this source section are retained as exact
    identity/comparison evidence only. They cannot be transferred to historical Sulforhabdus
    or generic DSM386. For the washed Fe(OH)3 precipitate, discarded supernatant and
    unspecified resuspension preclude final suspension mass-balance inference.", "sources":
    [{"locator": "extracted-text physical LF lines 9-17", "source_key": "dsm386a",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf",
    "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d",
    "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801",
    "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Solution
    A is sparged with 80% N2 and 20% CO2 gas mixture for 30 – 45 min to make it\nanoxic,
    then distributed under the same gas atmosphere into anoxic Hungate-type tubes\nor
    serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and
    20%\nCO2 gas mixture. Solutions C and D are prepared under a 100% N2 gas atmosphere
    and\nsterilized by filtration. To complete the medium solutions B to D are added
    to the sterile\nsolution A in the sequence as indicated. Before inoculation, appropriate
    amounts of sterile\nsulfur are added to the vials with the medium. Sulfur is sterilized
    by steaming for 3 hours\non each of 3 successive days (see medium 35) and added
    aseptically to the sterile\nmedium while retaining anoxic conditions. The final
    pH of the medium should be at 7.0.", "quote_representation": "captured extracted
    text"}]}, {"decision_id": "q69", "subject": "Current386a Solution A complete batch",
    "local_fields": [], "decision": "not_assessed", "stage": "distinct current THIOVIBRIO
    recipe", "interpretation": "All printed amounts and controls in this source section
    are retained as exact identity/comparison evidence only. They cannot be transferred
    to historical Sulforhabdus or generic DSM386. For the washed Fe(OH)3 precipitate,
    discarded supernatant and unspecified resuspension preclude final suspension mass-balance
    inference.", "sources": [{"locator": "extracted-text physical LF lines 22-32",
    "source_key": "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf",
    "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d",
    "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801",
    "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Solution
    A\n   KH2PO4                                                   0.20        g\n   NH4Cl                                                    0.25        g\n   NaCl                                                     1.00        g\n   MgCl2
    x 6 H2O                                            0.40        g\n   KCl                                                      0.50        g\n   CaCl2
    x 2 H2O                                            0.15        g\n   Trace element
    solution SL-10                             1.00       ml\n   Selenite-tungstate
    solution                              1.00       ml\n   Amorphous Fe(OH)3                                       25.00       ml\n   Distilled
    water                                        940.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q70", "subject": "Current386a Solution
    B", "local_fields": [], "decision": "not_assessed", "stage": "distinct current
    THIOVIBRIO recipe", "interpretation": "All printed amounts and controls in this
    source section are retained as exact identity/comparison evidence only. They cannot
    be transferred to historical Sulforhabdus or generic DSM386. For the washed Fe(OH)3
    precipitate, discarded supernatant and unspecified resuspension preclude final
    suspension mass-balance inference.", "sources": [{"locator": "extracted-text physical
    LF lines 36-38", "source_key": "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf",
    "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d",
    "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801",
    "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Solution
    B (from medium 386)\n   Na2CO3                                                   1.50        g\n   Distilled
    water                                         30.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q71", "subject": "Current386a Solution
    C vitamins dose", "local_fields": [], "decision": "not_assessed", "stage": "distinct
    current THIOVIBRIO recipe", "interpretation": "All printed amounts and controls
    in this source section are retained as exact identity/comparison evidence only.
    They cannot be transferred to historical Sulforhabdus or generic DSM386. For the
    washed Fe(OH)3 precipitate, discarded supernatant and unspecified resuspension
    preclude final suspension mass-balance inference.", "sources": [{"locator": "extracted-text
    physical LF lines 42-43", "source_key": "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf",
    "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d",
    "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801",
    "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Solution
    C\n   Seven vitamins solution                                  1.00       ml",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q72", "subject":
    "Current386a Solution D", "local_fields": [], "decision": "not_assessed", "stage":
    "distinct current THIOVIBRIO recipe", "interpretation": "All printed amounts and
    controls in this source section are retained as exact identity/comparison evidence
    only. They cannot be transferred to historical Sulforhabdus or generic DSM386.
    For the washed Fe(OH)3 precipitate, discarded supernatant and unspecified resuspension
    preclude final suspension mass-balance inference.", "sources": [{"locator": "extracted-text
    physical LF lines 47-49", "source_key": "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf",
    "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d",
    "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801",
    "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Solution
    D\n   DL-Dithiothreitol                                        0.30        g\n   Distilled
    water                                         10.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q73", "subject": "Current386a SL-10
    full batch and makeup", "local_fields": [], "decision": "not_assessed", "stage":
    "distinct current THIOVIBRIO recipe", "interpretation": "All printed amounts and
    controls in this source section are retained as exact identity/comparison evidence
    only. They cannot be transferred to historical Sulforhabdus or generic DSM386.
    For the washed Fe(OH)3 precipitate, discarded supernatant and unspecified resuspension
    preclude final suspension mass-balance inference.", "sources": [{"locator": "extracted-text
    physical LF lines 58-71", "source_key": "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf",
    "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d",
    "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801",
    "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Trace element
    solution SL-10 (from medium 320)\n   HCl (25%)                                                  10.00      ml\n   FeCl2
    x 4 H2O                                               1.50       g\n   ZnCl2                                                      70.00      mg\n   MnCl2
    x 4 H2O                                             100.00      mg\n   H3BO3                                                       6.00      mg\n   CoCl2
    x 6 H2O                                             190.00      mg\n   CuCl2 x
    2 H2O                                               2.00      mg\n   NiCl2 x 6
    H2O                                              24.00      mg\n   Na2MoO4 x 2
    H2O                                            36.00      mg\n   Distilled water                                           990.00      ml\n\nFirst
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally\nmake up to 1000.00 ml.", "quote_representation": "captured extracted
    text"}]}, {"decision_id": "q74", "subject": "Current386a Selenite-tungstate batch",
    "local_fields": [], "decision": "not_assessed", "stage": "distinct current THIOVIBRIO
    recipe", "interpretation": "All printed amounts and controls in this source section
    are retained as exact identity/comparison evidence only. They cannot be transferred
    to historical Sulforhabdus or generic DSM386. For the washed Fe(OH)3 precipitate,
    discarded supernatant and unspecified resuspension preclude final suspension mass-balance
    inference.", "sources": [{"locator": "extracted-text physical LF lines 75-79",
    "source_key": "dsm386a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf",
    "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d",
    "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801",
    "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Selenite-tungstate
    solution (from medium 385)\n   NaOH                                                       0.50        g\n   Na2SeO3
    x 5 H2O                                            3.00       mg\n   Na2WO4 x
    2 H2O                                             4.00       mg\n   Distilled
    water                                         1000.00       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q75", "subject": "Current386a Ferric-hydroxide
    precipitation inputs and controls", "local_fields": [], "decision": "not_assessed",
    "stage": "distinct current THIOVIBRIO recipe", "interpretation": "All printed
    amounts and controls in this source section are retained as exact identity/comparison
    evidence only. They cannot be transferred to historical Sulforhabdus or generic
    DSM386. For the washed Fe(OH)3 precipitate, discarded supernatant and unspecified
    resuspension preclude final suspension mass-balance inference.", "sources": [{"locator":
    "extracted-text physical LF lines 83-92", "source_key": "dsm386a", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf", "source_raw_sha256":
    "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d", "source_text_sha256":
    "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801", "accessed_at":
    "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Amorphous Fe(OH)3 (from
    medium 1210)\n   FeCl3 x 6 H2O (60.00 g/l)                                 320.00       ml\n   NaOH
    (10% w/v), adjust if required                         80.00       ml\n\nSlowly
    titrate 320 ml of a FeCl3 x 6 H2O stock solution (60.00 g/l) with 10% (w/v) NaOH
    to\npH 8.0-8.5 under agitation (use magnetic stirrer). Total amount of added NaOH
    approx. 80\n- 100 ml. The precipitated Fe(OH)3 should be stored at room temperature
    overnight with\nsurface covered with water. Thereafter, centrifuge at 2000 rpm
    for 5 min and discard the\nsupernatant. Wash several times with distilled water.
    Resuspend the pellet in medium as\ndescribed above. For storage autoclave under
    100% N2 atmosphere.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q76", "subject": "Current386a Seven-vitamin stock", "local_fields": [], "decision":
    "not_assessed", "stage": "distinct current THIOVIBRIO recipe", "interpretation":
    "All printed amounts and controls in this source section are retained as exact
    identity/comparison evidence only. They cannot be transferred to historical Sulforhabdus
    or generic DSM386. For the washed Fe(OH)3 precipitate, discarded supernatant and
    unspecified resuspension preclude final suspension mass-balance inference.", "sources":
    [{"locator": "extracted-text physical LF lines 96-104", "source_key": "dsm386a",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium386a.pdf",
    "source_raw_sha256": "31055c92e250c4dbd6115cfbbf35a93c8195df92df7d95d710d9ac931d50e63d",
    "source_text_sha256": "b5fbfb446615fdccb48495d484abff53bf6320178f48bff2cbaa823fb179b801",
    "accessed_at": "2026-10-28T19:40:51.630425Z", "exact_source_quote": "Seven vitamins
    solution (from medium 503)\n   Vitamin B12                                              100.00       mg\n   p-Aminobenzoic
    acid                                       80.00       mg\n   D-(+)-biotin                                              20.00       mg\n   Nicotinic
    acid                                           200.00       mg\n   Calcium pantothenate                                     100.00       mg\n   Pyridoxine
    hydrochloride                                 300.00       mg\n   Thiamine-HCl
    x 2 H2O                                     200.00       mg\n   Distilled water                                         1000.00       ml",
    "quote_representation": "captured extracted text"}]}], "local_field_census_reference":
    "REVIEW_WORK/batch076/record06/grounding-inventory.json", "source_only_gaps_are_explicit":
    true, "note": "Batch amounts, provider normalization, stock composition, working
    dose and preparation controls are separate. No source edits or automatic curation
    performed."}'
- assessment_id: a5
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml: primary 30/30, secondary
    28/30; data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml: primary 25/25,
    secondary 23/25; data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml:
    primary 25/25, secondary 23/25; data/normalized_yaml/bacterial/sulforhabdus_medium.yaml:
    primary 30/30, secondary 28/30. These are ingredient-instance linkage fractions,
    not accuracy scores. Solution terms are audited separately. Every actually asserted
    CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows.
    0 numeric legacy MediaIngredientMech mentions occur across the complete selected
    documents, with exact locators in the inventory; NNNNNN is a historical placeholder,
    not an ID. Complex commercial/product components are not forced to pure-compound
    IDs.'
  target_ids:
  - CultureMech:001493
  evidence_ids:
  - grounding
- assessment_id: a6
  area: scope
  topic: Scope and source limits
  outcome: supported
  summary: Complete selected generated target and all three exact maintained contributors
    reviewed. The assessed stock definitions are embedded in DSM386. Current DSM386a
    is comparison-only and does not establish the historical KOMODO386a formulation.
    No external dependency formulation is transferred; source prescriptions and medium
    names are not strain-growth evidence.
  target_ids:
  - CultureMech:001493
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
  - CultureMech:001493
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-001493-source-stage-denominators
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Separate A–F and stock rates are presented at main-medium scope
  description: All 30 target concentrations come from separate A–F or embedded stock
    bases. Maintained DSM/KOMODO386 owners partially nest five stock compounds, which
    are credited, but most remain flat and both receiving doses are unqualified ML_PER_L.
    Main batch additions, water and distinct stock structure are missing.
  target_ids:
  - CultureMech:001493
  field_paths:
  - ingredients[*].concentration
  - solutions
  evidence_ids:
  - dsm386
  - api386
  - quantity-inventory
  - composition-helper
  rule_id: review-yaml-record/stage-and-denominator-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/sulforhabdus_medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-001493-current-source-variant-equivalence
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Stored duplicate relationships conflate distinct source identities
  description: The selected merge and both386 owners point to historical Sulforhabdus386a
    as SOURCE_DUPLICATE. The exact current386a primary identifies THIOVIBRIO and materially
    differs. Historical mapping and identical copied numeric signatures support ancestry,
    not interchangeable recipes.
  target_ids:
  - CultureMech:001493
  field_paths:
  - parent_media
  - merged_from
  - data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml::parent_media
  - data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml::parent_media
  - data/normalized_yaml/bacterial/sulforhabdus_medium.yaml::variant_children
  evidence_ids:
  - historical-current-joins
  - dsm386
  - dsm386a
  - local0
  - local1
  - local2
  - local3
  rule_id: review-yaml-record/source-variant-identity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/sulforhabdus_medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-001493-preparation-stage-and-atmosphere
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Correct retained preparation needs staged structure and owner reconciliation
  description: 'The target and DSM owner retain complete anoxic preparation and feeding
    prose. Their combined AUTOCLAVE action includes filtration, and Solution E pH/SL-10
    makeup are root steps. The KOMODO386 owner has no procedure and notes says Aerobic:
    Yes despite the DSM anoxic source; historical386a has no supported current procedure.'
  target_ids:
  - CultureMech:001493
  field_paths:
  - preparation_steps
  - data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml::notes
  - data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml::preparation_steps
  evidence_ids:
  - dsm386
  - api386
  - local0
  - local1
  - local2
  rule_id: review-yaml-record/preparation-stage-completeness
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/sulforhabdus_medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-001493-exact-supplied-form
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hydrate and sodium resazurin use different supplied-form IDs
  description: All selected layers assert anhydrous nickel chloride34887 for named
    hexahydrate in both slots, and neutral resazurin8806 for sodium resazurin in the
    primary slot. OLS formulas confirm those are different forms. Other correct hydrate
    mappings and source masses are retained; generic calcium pantothenate stereochemistry
    remains explicitly unresolved.
  target_ids:
  - CultureMech:001493
  field_paths:
  - data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml::ingredients[6].term
  - data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml::ingredients[18].term
  - data/merge_yaml/merged/DESULFOLUTIVIBRIO_MEDIUM.yaml::ingredients[18].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml::ingredients[6].term
  - data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml::ingredients[17].term
  - data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml::ingredients[17].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml::ingredients[6].term
  - data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml::ingredients[17].term
  - data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml::ingredients[17].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/sulforhabdus_medium.yaml::ingredients[6].term
  - data/normalized_yaml/bacterial/sulforhabdus_medium.yaml::ingredients[18].term
  - data/normalized_yaml/bacterial/sulforhabdus_medium.yaml::ingredients[18].mediaingredientmech_chebi_term
  evidence_ids:
  - dsm386
  - dsm386a
  - chebi34887
  - chebi8806
  - grounding
  rule_id: review-yaml-record/exact-supplied-form
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/sulforhabdus_medium.yaml
    role: maintained normalized contributor
- finding_id: f5
  issue_key: culturemech-001493-append-only-evidence-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical matches do not supply attached claim evidence or valid timestamps
  description: No selected layer has attached formulation claims. Stored KOMODO dates
    contain literal .fZ and resolver events lack offsets. Current writer formats explain
    present risks but do not prove historical execution. The386a historical digest
    matches an error body, not a recipe.
  target_ids:
  - CultureMech:001493
  field_paths:
  - evidence
  - curation_history
  evidence_ids:
  - history-auth
  - historical-current-joins
  - local2
  - local3
  rule_id: review-yaml-record/append-only-provenance
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/sulforhabdus_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: current import timestamp writer
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/enrich/dsmz_resolver.py
    role: current enrichment timestamp and preparation propagation writer
actions:
- action_id: action1
  description: Reconstruct exact A–F stages and complete stock membership in maintained
    owners. Preserve supported existing nested values and source batch amounts; distinguish
    provider942/1006ml bases from measured final volumes. Correct only demonstrated
    placement/dose-basis claims and keep unresolved KOMODO variants separate.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001493
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/sulforhabdus_medium.yaml
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
  description: Resolve the historical accession/name transition and source relationship
    before regenerating the selected merge. Preserve all historical names and source
    mappings, avoid replacing Sulforhabdus with current Thiovibrio automatically,
    and split distinct variants when identity evidence warrants it.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001493
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/sulforhabdus_medium.yaml
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
  description: Preserve correct existing descriptions while structuring each operation
    at its exact source stage. Resolve the KOMODO source identity and atmosphere contradiction
    before any propagation; do not overwrite historical source notes. Regenerate only
    through the current compatible-formulation guard.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001493
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/sulforhabdus_medium.yaml
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
  description: Resolve exact source hydrate and sodium-salt mappings against authoritative
    ontology/MIM records; retain precise source labels if unresolved. Do not derive
    molarity using the wrong hydrate or force a D/L choice from noisy synonyms.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001493
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/sulforhabdus_medium.yaml
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
  description: Preserve all original events unchanged. Append new verified claim/context
    evidence with actual current UTC dates, explicitly retaining failure-body scope.
    Correct future KOMODO/resolver timestamp formatting; never rewrite guessed historical
    instants.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:001493
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfolutivibrio_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfovibrio_sulfodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/sulforhabdus_medium.yaml
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
  - Confirm new timestamps are parseable UTC Z and prior curation-history event bytes
    remain unchanged.
limitations:
- Exact current KOMODO386/386a/list access returned403; API386a returned404. Current386a
  PDF evidence does not resolve its historical Sulforhabdus identity.
- Provider942ml A and1006ml assembled sums are explicit bookkeeping, not independent
  final-volume measurements. HCl percentage basis and calcium pantothenate stereochemistry
  remain unresolved.
- DSM7269 override and current THIOVIBRIO386a quantities are context-only; no recipe
  transfer, source edit, historical timestamp rewrite or native formal save occurred.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
