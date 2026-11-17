# Scientific review of desulfonatronum_thiodismutans_medium

- Review: 20261028T204800Z-desulfonatronum-thiodismutans-medium-batch077
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T20:14:28.581336Z
- Finished UTC: 2026-10-28T20:48:00.905151Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated record combines DSM813a identity and preparation with DSM866 amounts. Exact primary evidence separates those recipes and identifies the missingDSM16529 substrate replacement. Stock flattening, several supplied-form IDs, preparation placement and provenance remain defective; correct current owner fields and repaired variant relationships are credited.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch077 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001959 | data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml | generated | desulfonatronum_thiodismutans_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001959 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:001959 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:001959 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:001959 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Distinct source and strain formulations

identity: concern. Targets: CultureMech:001959.

The generated record carries813a identity/pH/procedure but866 ingredient amounts. The maintained813a and866 owners are different recipes. Current relationship repair correctly distinguishes866 source duplicate from866.1 strain variant, but does not implement the primaryDSM16529 substrate replacement. Fresh catalogue identifies environmental Desulfohalovibrio alkalitolerans DSM16529 with riskgroup1 and modified866; no pathogen-specific scope or new growth assertion is inferred.

### Classification and current merger

consistency: supported. Targets: CultureMech:001959.

LIQUID and yeast-containing complex/undefined classification are compatible with both source families. Current full-formulation merge logic rejects incompatible scientific projections and preserves preparation/evidence at matching scopes. This current guard is credited; the old merged record still combines different formulations.

### Supplied forms and source specificity

grounding: concern. Targets: CultureMech:001959.

All five layers assert nickel dichloride34887 in primary and secondary slots for nickel chloride hexahydrate, and neutral resazurin8806 in the primary slot for sodium resazurin. Correct cobalt53503 and other hydrates remain credited. MIM spelling-specific REJECTED CoCl2 x6H2O is distinct from MAPPED Cobalt chloride hexahydrate for the same correct ID. B12 is a class; generic lipoic acid does not certify an enantiomer. The newDSM16529 L-lactate must not be assigned a generic stereochemical term without verification.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:001959.

Nine full reports and four exact parent-plan rows were read. All152 historical source objects match current raw/decoded API objects, and both cited API digests match present bytes; the280 planclaims include128 separate local unresolved rows. No attached formulation evidence exists. Earlier broad all-conflict/pH rules are reassessed per layer; current source equality does not authenticate old runs or dates. Stored KOMODO timestamps contain literal2026-01-27T01:15:03.fZ and resolver events lack offsets; current timestamp writers retain corresponding risks. Current fixed-signature866 relationship repair does not establish the missing strain recipe. Current conservative merging preserves scientific fields and rejects incompatible formulations. Inspected writer behavior is described separately by exact file and function; it does not prove historical execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:001959.

All 155 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema":"private explicit quantity decisions v1","target_id":"CultureMech:001959","selected_concentration_field_count":155,"selected_concentration_fields_covered":155,"decisions":[{"decision_id":"q1","subject":"KH2PO4 generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[0].concentration","original":{"value":"0.199601","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass0.2g /1.002L = 0.1996007984031936127744510978g/L. The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text physical LF lines 7-7","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   KH2PO4                                                     0.20         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[0]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\": 1.46674,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q2","subject":"KH2PO4 maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[0].concentration","original":{"value":"0.199601","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass0.2g /1.002L = 0.1996007984031936127744510978g/L. The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text physical LF lines 7-7","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   KH2PO4                                                     0.20         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[0]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\": 1.46674,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q3","subject":"MgCl2 x 6 H2O generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[1].concentration","original":{"value":"0.0998004","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass0.1g /1.002L = 0.09980039920159680638722554890g/L. The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text physical LF lines 8-8","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   MgCl2 x 6 H2O                                              0.10         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[1]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0998004,\n                        \"mmol_l\": 0.490895,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q4","subject":"MgCl2 x 6 H2O maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[1].concentration","original":{"value":"0.0998004","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass0.1g /1.002L = 0.09980039920159680638722554890g/L. The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text physical LF lines 8-8","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   MgCl2 x 6 H2O                                              0.10         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[1]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0998004,\n                        \"mmol_l\": 0.490895,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q5","subject":"KCl generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[2].concentration","original":{"value":"0.199601","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass0.2g /1.002L = 0.1996007984031936127744510978g/L. The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text physical LF lines 10-10","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   KCl                                                        0.20         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[3]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\": 2.67741,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q6","subject":"KCl maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[3].concentration","original":{"value":"0.199601","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass0.2g /1.002L = 0.1996007984031936127744510978g/L. The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text physical LF lines 10-10","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   KCl                                                        0.20         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[3]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\": 2.67741,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q7","subject":"NH4Cl generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[3].concentration","original":{"value":"0.998004","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass1g /1.002L = 0.9980039920159680638722554890g/L. The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text physical LF lines 9-9","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   NH4Cl                                                      1.00         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[2]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.998004,\n                        \"mmol_l\": 18.6578,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q8","subject":"NH4Cl maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[2].concentration","original":{"value":"0.998004","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass1g /1.002L = 0.9980039920159680638722554890g/L. The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text physical LF lines 9-9","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   NH4Cl                                                      1.00         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[2]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.998004,\n                        \"mmol_l\": 18.6578,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q9","subject":"Na2SO4 generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[4].concentration","original":{"value":"4.99002","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass3g /1.002L = 2.994011976047904191616766467g/L. Existing value conflicts with this exact source basis; correct only the813a layer. Current API813a is internally inconsistent: sulfate3g hasg_l4.99002, carbonate3g hasg_l3.49301, and bicarbonate24g lacksg_l. Do not promote those fields over the primary denominator.","sources":[{"locator":"extracted-text physical LF lines 11-11","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Na2SO4                                                     3.00         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[4]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.99002,\n                        \"mmol_l\": 35.1311,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q10","subject":"Na2SO4 maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[4].concentration","original":{"value":"4.99002","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass3g /1.002L = 2.994011976047904191616766467g/L. Existing value conflicts with this exact source basis; correct only the813a layer. Current API813a is internally inconsistent: sulfate3g hasg_l4.99002, carbonate3g hasg_l3.49301, and bicarbonate24g lacksg_l. Do not promote those fields over the primary denominator.","sources":[{"locator":"extracted-text physical LF lines 11-11","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Na2SO4                                                     3.00         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[4]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.99002,\n                        \"mmol_l\": 35.1311,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q11","subject":"NaCl generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[5].concentration","original":{"value":"4.99002","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass30g /1.002L = 29.94011976047904191616766467g/L. Existing value conflicts with this exact source basis; correct only the813a layer.","sources":[{"locator":"extracted-text physical LF lines 12-12","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   NaCl                                                      30.00         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[5]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 29.9401,\n                        \"mmol_l\": 512.322,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q12","subject":"NaCl maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[5].concentration","original":{"value":"29.9401","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass30g /1.002L = 29.94011976047904191616766467g/L. The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text physical LF lines 12-12","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   NaCl                                                      30.00         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[5]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 29.9401,\n                        \"mmol_l\": 512.322,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q13","subject":"Yeast extract generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[6].concentration","original":{"value":"1.49701","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass1g /1.002L = 0.9980039920159680638722554890g/L. Existing value conflicts with this exact source basis; correct only the813a layer.","sources":[{"locator":"extracted-text physical LF lines 14-14","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Yeast extract                                              1.00         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[7]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.998004,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q14","subject":"Yeast extract maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[6].concentration","original":{"value":"0.998004","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass1g /1.002L = 0.9980039920159680638722554890g/L. The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text physical LF lines 14-14","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Yeast extract                                              1.00         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[7]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.998004,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q15","subject":"Sodium resazurin generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[7].concentration","original":{"value":"0.000499002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass0.0005g /1.002L = 0.0004990019960079840319361277445g/L. The existing value agrees at its recorded precision; retain it and add exact evidence. Source0.5ml of0.1%w/v resazurin contributes0.0005g; the explicit w/v basis permits this calculation.","sources":[{"locator":"extracted-text physical LF lines 15-15","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Sodium resazurin (0.1% w/v)                                0.50        ml","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[8]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000499002,\n                        \"mmol_l\": 0.00198671,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q16","subject":"Sodium resazurin maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[7].concentration","original":{"value":"0.000499002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass0.0005g /1.002L = 0.0004990019960079840319361277445g/L. The existing value agrees at its recorded precision; retain it and add exact evidence. Source0.5ml of0.1%w/v resazurin contributes0.0005g; the explicit w/v basis permits this calculation.","sources":[{"locator":"extracted-text physical LF lines 15-15","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Sodium resazurin (0.1% w/v)                                0.50        ml","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[8]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000499002,\n                        \"mmol_l\": 0.00198671,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q17","subject":"Na2CO3 generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[8].concentration","original":{"value":"0.499002","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass3g /1.002L = 2.994011976047904191616766467g/L. Existing value conflicts with this exact source basis; correct only the813a layer. Current API813a is internally inconsistent: sulfate3g hasg_l4.99002, carbonate3g hasg_l3.49301, and bicarbonate24g lacksg_l. Do not promote those fields over the primary denominator.","sources":[{"locator":"extracted-text physical LF lines 16-16","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Na2CO3                                                     3.00         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[9]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.49301,\n                        \"mmol_l\": 32.9567,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q18","subject":"Na2CO3 maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[8].concentration","original":{"value":"3.49301","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass3g /1.002L = 2.994011976047904191616766467g/L. Existing value conflicts with this exact source basis; correct only the813a layer. Current API813a is internally inconsistent: sulfate3g hasg_l4.99002, carbonate3g hasg_l3.49301, and bicarbonate24g lacksg_l. Do not promote those fields over the primary denominator.","sources":[{"locator":"extracted-text physical LF lines 16-16","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Na2CO3                                                     3.00         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[9]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.49301,\n                        \"mmol_l\": 32.9567,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q19","subject":"NaHCO3 generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[9].concentration","original":{"value":"7.98403","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass24g /1.002L = 23.95209580838323353293413174g/L. Existing value conflicts with this exact source basis; correct only the813a layer. Current API813a is internally inconsistent: sulfate3g hasg_l4.99002, carbonate3g hasg_l3.49301, and bicarbonate24g lacksg_l. Do not promote those fields over the primary denominator.","sources":[{"locator":"extracted-text physical LF lines 17-17","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   NaHCO3                                                    24.00         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[10]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 24,\n                        \"unit\": \"g\",\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q20","subject":"NaHCO3 maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[9].concentration","original":{"value":"24","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass24g /1.002L = 23.95209580838323353293413174g/L. Existing value conflicts with this exact source basis; correct only the813a layer. Current API813a is internally inconsistent: sulfate3g hasg_l4.99002, carbonate3g hasg_l3.49301, and bicarbonate24g lacksg_l. Do not promote those fields over the primary denominator.","sources":[{"locator":"extracted-text physical LF lines 17-17","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   NaHCO3                                                    24.00         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[10]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 24,\n                        \"unit\": \"g\",\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q21","subject":"Na-formate generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[10].concentration","original":{"value":"4.99002","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass4g /1.002L = 3.992015968063872255489021956g/L. Existing value conflicts with this exact source basis; correct only the813a layer.","sources":[{"locator":"extracted-text physical LF lines 19-19","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Na-formate                                                 4.00         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[12]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na-formate\",\n                        \"compound_id\": 144,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.99202,\n                        \"mmol_l\": 58.6999,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q22","subject":"Na-formate maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[11].concentration","original":{"value":"3.99202","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass4g /1.002L = 3.992015968063872255489021956g/L. The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text physical LF lines 19-19","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Na-formate                                                 4.00         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[12]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na-formate\",\n                        \"compound_id\": 144,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.99202,\n                        \"mmol_l\": 58.6999,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q23","subject":"Na2S x 9 H2O generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[11].concentration","original":{"value":"0.499002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass0.5g /1.002L = 0.4990019960079840319361277445g/L. The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text physical LF lines 18-18","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Na2S x 9 H2O                                               0.50         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[11]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\": 2.0776,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q24","subject":"Na2S x 9 H2O maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[10].concentration","original":{"value":"0.499002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a main medium","interpretation":"The primary DSM813a explicitly declares1002ml final volume. Its source batch mass0.5g /1.002L = 0.4990019960079840319361277445g/L. The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text physical LF lines 18-18","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Na2S x 9 H2O                                               0.50         g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[11]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\": 2.0776,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q25","subject":"KH2PO4 DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[0].concentration","original":{"value":"0.199601","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[0].concentration","original":{"value":"0.199601","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[0].concentration","original":{"value":"0.199601","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866 provider main basis","interpretation":"Current DSM866 primary supports the quoted basal batch amount and API866 explicitly reports this nominal main g_l. Credit that provider basis without asserting independently measured final volume. The KOMODO routes are403, so no historical or unobserved source version is certified. The current strain-specific substitution is assessed separately; unrelated813a amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines 3-3","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   KH2PO4                                                     0.20         g","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\": 1.46674,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q26","subject":"MgCl2 x 6 H2O DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[1].concentration","original":{"value":"0.0998004","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[1].concentration","original":{"value":"0.0998004","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[1].concentration","original":{"value":"0.0998004","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866 provider main basis","interpretation":"Current DSM866 primary supports the quoted basal batch amount and API866 explicitly reports this nominal main g_l. Credit that provider basis without asserting independently measured final volume. The KOMODO routes are403, so no historical or unobserved source version is certified. The current strain-specific substitution is assessed separately; unrelated813a amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   MgCl2 x 6 H2O                                              0.10         g","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[1]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0998004,\n                        \"mmol_l\": 0.490895,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q27","subject":"KCl DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[2].concentration","original":{"value":"0.199601","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[2].concentration","original":{"value":"0.199601","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[2].concentration","original":{"value":"0.199601","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866 provider main basis","interpretation":"Current DSM866 primary supports the quoted basal batch amount and API866 explicitly reports this nominal main g_l. Credit that provider basis without asserting independently measured final volume. The KOMODO routes are403, so no historical or unobserved source version is certified. The current strain-specific substitution is assessed separately; unrelated813a amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines 5-5","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   KCl                                                        0.20         g","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[2]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\": 2.67741,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q28","subject":"NH4Cl DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[3].concentration","original":{"value":"0.998004","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[3].concentration","original":{"value":"0.998004","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[3].concentration","original":{"value":"0.998004","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866 provider main basis","interpretation":"Current DSM866 primary supports the quoted basal batch amount and API866 explicitly reports this nominal main g_l. Credit that provider basis without asserting independently measured final volume. The KOMODO routes are403, so no historical or unobserved source version is certified. The current strain-specific substitution is assessed separately; unrelated813a amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines 6-6","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   NH4Cl                                                      1.00         g","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[3]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.998004,\n                        \"mmol_l\": 18.6578,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q29","subject":"Na2SO4 DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[4].concentration","original":{"value":"4.99002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[4].concentration","original":{"value":"4.99002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[4].concentration","original":{"value":"4.99002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866 provider main basis","interpretation":"Current DSM866 primary supports the quoted basal batch amount and API866 explicitly reports this nominal main g_l. Credit that provider basis without asserting independently measured final volume. The KOMODO routes are403, so no historical or unobserved source version is certified. The current strain-specific substitution is assessed separately; unrelated813a amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines 7-7","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Na2SO4                                                     5.00         g","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[4]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.99002,\n                        \"mmol_l\": 35.1311,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q30","subject":"NaCl DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[5].concentration","original":{"value":"4.99002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[5].concentration","original":{"value":"4.99002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[5].concentration","original":{"value":"4.99002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866 provider main basis","interpretation":"Current DSM866 primary supports the quoted basal batch amount and API866 explicitly reports this nominal main g_l. Credit that provider basis without asserting independently measured final volume. The KOMODO routes are403, so no historical or unobserved source version is certified. The current strain-specific substitution is assessed separately; unrelated813a amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines 8-8","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   NaCl                                                       5.00         g","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[5]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.99002,\n                        \"mmol_l\": 85.3871,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q31","subject":"Yeast extract DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[6].concentration","original":{"value":"1.49701","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[6].concentration","original":{"value":"1.49701","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[6].concentration","original":{"value":"1.49701","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866 provider main basis","interpretation":"Current DSM866 primary supports the quoted basal batch amount and API866 explicitly reports this nominal main g_l. Credit that provider basis without asserting independently measured final volume. The KOMODO routes are403, so no historical or unobserved source version is certified. The current strain-specific substitution is assessed separately; unrelated813a amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines 10-10","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Yeast extract                                              1.50         g","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[7]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.49701,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q32","subject":"Sodium resazurin DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[7].concentration","original":{"value":"0.000499002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[7].concentration","original":{"value":"0.000499002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[7].concentration","original":{"value":"0.000499002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866 provider main basis","interpretation":"Current DSM866 primary supports the quoted basal batch amount and API866 explicitly reports this nominal main g_l. Credit that provider basis without asserting independently measured final volume. The KOMODO routes are403, so no historical or unobserved source version is certified. The current strain-specific substitution is assessed separately; unrelated813a amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines 11-11","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Sodium resazurin (0.1% w/v)                                0.50        ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[8]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000499002,\n                        \"mmol_l\": 0.00198671,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q33","subject":"Na2CO3 DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[8].concentration","original":{"value":"0.499002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[8].concentration","original":{"value":"0.499002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[8].concentration","original":{"value":"0.499002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866 provider main basis","interpretation":"Current DSM866 primary supports the quoted basal batch amount and API866 explicitly reports this nominal main g_l. Credit that provider basis without asserting independently measured final volume. The KOMODO routes are403, so no historical or unobserved source version is certified. The current strain-specific substitution is assessed separately; unrelated813a amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines 12-12","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Na2CO3                                                     0.50         g","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[9]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\": 4.7081,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q34","subject":"NaHCO3 DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[9].concentration","original":{"value":"7.98403","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[9].concentration","original":{"value":"7.98403","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[9].concentration","original":{"value":"7.98403","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866 provider main basis","interpretation":"Current DSM866 primary supports the quoted basal batch amount and API866 explicitly reports this nominal main g_l. Credit that provider basis without asserting independently measured final volume. The KOMODO routes are403, so no historical or unobserved source version is certified. The current strain-specific substitution is assessed separately; unrelated813a amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines 13-13","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   NaHCO3                                                     8.00         g","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[10]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 8,\n                        \"unit\": \"g\",\n                        \"g_l\": 7.98403,\n                        \"mmol_l\": 95.0401,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q35","subject":"Na-formate DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[10].concentration","original":{"value":"4.99002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[10].concentration","original":{"value":"4.99002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866 provider main basis","interpretation":"Current DSM866 primary supports the quoted basal batch amount and API866 explicitly reports this nominal main g_l. Credit that provider basis without asserting independently measured final volume. The KOMODO routes are403, so no historical or unobserved source version is certified. The current strain-specific substitution is assessed separately; unrelated813a amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines 14-14","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Na-formate                                                 5.00         g","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[11]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na-formate\",\n                        \"compound_id\": 144,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.99002,\n                        \"mmol_l\": 73.3749,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q36","subject":"Na2S x 9 H2O DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[11].concentration","original":{"value":"0.499002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[11].concentration","original":{"value":"0.499002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[11].concentration","original":{"value":"0.499002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866 provider main basis","interpretation":"Current DSM866 primary supports the quoted basal batch amount and API866 explicitly reports this nominal main g_l. Credit that provider basis without asserting independently measured final volume. The KOMODO routes are403, so no historical or unobserved source version is certified. The current strain-specific substitution is assessed separately; unrelated813a amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines 16-16","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Na2S x 9 H2O                                               0.50         g","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[13]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\": 2.0776,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q37","subject":"DSM16529 substrate replacement","local_fields":[{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[10].concentration","original":{"value":"4.99002","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM16529-specific variant","interpretation":"Current primary DSM866 explicitly replaces sodium formate with2.5g/L sodium L-lactate forDSM16529. The wrapper retains basal formate and lacks lactate. The catalogue confirms current identity and modified medium866 association; it does not justify changing the generic866 or813a recipes.","sources":[{"locator":"extracted-text physical LF lines 27-27","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"For DSM 16529: Replace Na-formate with 2.5 g/l Na-L-lactate as substrate.","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 199-199","source_key":"dsm16529Identity","reference":"https://www.dsmz.de/collection/catalogue/details/culture/DSM-16529","source_raw_sha256":"08e4dba4a2f52396cd2d62b1ca21e72e766eb347dc8c6f08b303d1703fb51d72","source_text_sha256":"1effe70237ed96eeaec6534cb56c2cbdb98da370246d87ca3e01a94b339a6807","accessed_at":"2026-10-28T20:14:20.082451Z","exact_source_quote":"Medium 866 with strain-specific modifications","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 208-208","source_key":"dsm16529Identity","reference":"https://www.dsmz.de/collection/catalogue/details/culture/DSM-16529","source_raw_sha256":"08e4dba4a2f52396cd2d62b1ca21e72e766eb347dc8c6f08b303d1703fb51d72","source_text_sha256":"1effe70237ed96eeaec6534cb56c2cbdb98da370246d87ca3e01a94b339a6807","accessed_at":"2026-10-28T20:14:20.082451Z","exact_source_quote":"Taxonomy/description (10394, 32582, 33859). Sequence accession no. 16S rRNA gene: AY649785, draft genome: ATHI01000000. (Medium 866 with strain-specific modifications, 40°C, anaerobic).","quote_representation":"captured extracted text"}]},{"decision_id":"q38","subject":"HCl SL10","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[12].concentration","original":{"value":"2.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[12].concentration","original":{"value":"2.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[12].concentration","original":{"value":"2.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[12].concentration","original":{"value":"2.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[12].concentration","original":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","stage":"SL10 stock","interpretation":"The source specifies10ml of25% HCl reagent, with no percent basis. Provider2.5g/L does not establish that mass concentration; restore the volume and retain the bare strength label without density inference. Keep the separate1ml receiving dose and stock preparation.","sources":[{"locator":"extracted-text physical LF lines 33-33","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   HCl (25%)                                                  10.00      ml","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[0]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 33-33","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   HCl (25%)                                                  10.00      ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q39","subject":"FeCl2 x 4 H2O SL10","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[13].concentration","original":{"value":"1.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[13].concentration","original":{"value":"1.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[13].concentration","original":{"value":"1.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[13].concentration","original":{"value":"1.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[13].concentration","original":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","stage":"SL10 stock","interpretation":"Both primary SL10 tables explicitly make up to1000ml, so the quoted stock batch mass supports its stock g/L. The existing root placement is wrong: retain the valid stock strength insideSL10, not as main-medium concentration. Keep the separate1ml receiving dose and stock preparation.","sources":[{"locator":"extracted-text physical LF lines 34-34","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   FeCl2 x 4 H2O                                               1.50       g","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[1]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 34-34","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   FeCl2 x 4 H2O                                               1.50       g","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q40","subject":"ZnCl2 SL10","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[14].concentration","original":{"value":"0.07","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[14].concentration","original":{"value":"0.07","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[14].concentration","original":{"value":"0.07","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[14].concentration","original":{"value":"0.07","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[14].concentration","original":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","stage":"SL10 stock","interpretation":"Both primary SL10 tables explicitly make up to1000ml, so the quoted stock batch mass supports its stock g/L. The existing root placement is wrong: retain the valid stock strength insideSL10, not as main-medium concentration. Keep the separate1ml receiving dose and stock preparation.","sources":[{"locator":"extracted-text physical LF lines 35-35","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   ZnCl2                                                      70.00      mg","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[2]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 35-35","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   ZnCl2                                                      70.00      mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q41","subject":"MnCl2 x 4 H2O SL10","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[15].concentration","original":{"value":"0.1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[15].concentration","original":{"value":"0.1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[15].concentration","original":{"value":"0.1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[15].concentration","original":{"value":"0.1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[15].concentration","original":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","stage":"SL10 stock","interpretation":"Both primary SL10 tables explicitly make up to1000ml, so the quoted stock batch mass supports its stock g/L. The existing root placement is wrong: retain the valid stock strength insideSL10, not as main-medium concentration. Keep the separate1ml receiving dose and stock preparation.","sources":[{"locator":"extracted-text physical LF lines 36-36","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   MnCl2 x 4 H2O                                             100.00      mg","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[3]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 36-36","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   MnCl2 x 4 H2O                                             100.00      mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q42","subject":"H3BO3 SL10","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[16].concentration","original":{"value":"0.006","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[16].concentration","original":{"value":"0.006","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[16].concentration","original":{"value":"0.006","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[16].concentration","original":{"value":"0.006","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[16].concentration","original":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","stage":"SL10 stock","interpretation":"Both primary SL10 tables explicitly make up to1000ml, so the quoted stock batch mass supports its stock g/L. The existing root placement is wrong: retain the valid stock strength insideSL10, not as main-medium concentration. Keep the separate1ml receiving dose and stock preparation.","sources":[{"locator":"extracted-text physical LF lines 37-37","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   H3BO3                                                       6.00      mg","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[4]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 37-37","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   H3BO3                                                       6.00      mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q43","subject":"CoCl2 x 6 H2O SL10","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[17].concentration","original":{"value":"0.19","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[17].concentration","original":{"value":"0.19","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[17].concentration","original":{"value":"0.19","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[17].concentration","original":{"value":"0.19","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[17].concentration","original":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","stage":"SL10 stock","interpretation":"Both primary SL10 tables explicitly make up to1000ml, so the quoted stock batch mass supports its stock g/L. The existing root placement is wrong: retain the valid stock strength insideSL10, not as main-medium concentration. Keep the separate1ml receiving dose and stock preparation.","sources":[{"locator":"extracted-text physical LF lines 38-38","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   CoCl2 x 6 H2O                                             190.00      mg","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[5]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 38-38","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   CoCl2 x 6 H2O                                             190.00      mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q44","subject":"CuCl2 x 2 H2O SL10","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[18].concentration","original":{"value":"0.002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[18].concentration","original":{"value":"0.002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[18].concentration","original":{"value":"0.002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[18].concentration","original":{"value":"0.002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[18].concentration","original":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","stage":"SL10 stock","interpretation":"Both primary SL10 tables explicitly make up to1000ml, so the quoted stock batch mass supports its stock g/L. The existing root placement is wrong: retain the valid stock strength insideSL10, not as main-medium concentration. Keep the separate1ml receiving dose and stock preparation.","sources":[{"locator":"extracted-text physical LF lines 39-39","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   CuCl2 x 2 H2O                                               2.00      mg","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[6]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 39-39","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   CuCl2 x 2 H2O                                               2.00      mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q45","subject":"NiCl2 x 6 H2O SL10","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[19].concentration","original":{"value":"0.024","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[19].concentration","original":{"value":"0.024","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[19].concentration","original":{"value":"0.024","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[19].concentration","original":{"value":"0.024","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[19].concentration","original":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","stage":"SL10 stock","interpretation":"Both primary SL10 tables explicitly make up to1000ml, so the quoted stock batch mass supports its stock g/L. The existing root placement is wrong: retain the valid stock strength insideSL10, not as main-medium concentration. Keep the separate1ml receiving dose and stock preparation.","sources":[{"locator":"extracted-text physical LF lines 40-40","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   NiCl2 x 6 H2O                                              24.00      mg","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[7]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 40-40","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   NiCl2 x 6 H2O                                              24.00      mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q46","subject":"Na2MoO4 x 2 H2O SL10","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[20].concentration","original":{"value":"0.036","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[20].concentration","original":{"value":"0.036","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[20].concentration","original":{"value":"0.036","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[20].concentration","original":{"value":"0.036","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[20].concentration","original":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","stage":"SL10 stock","interpretation":"Both primary SL10 tables explicitly make up to1000ml, so the quoted stock batch mass supports its stock g/L. The existing root placement is wrong: retain the valid stock strength insideSL10, not as main-medium concentration. Keep the separate1ml receiving dose and stock preparation.","sources":[{"locator":"extracted-text physical LF lines 41-41","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Na2MoO4 x 2 H2O                                            36.00      mg","quote_representation":"captured extracted text"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[8]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 41-41","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Na2MoO4 x 2 H2O                                            36.00      mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q47","subject":"Biotin Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[21].concentration","original":{"value":"0.02","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[21].concentration","original":{"value":"0.02","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[21].concentration","original":{"value":"0.02","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[21].concentration","original":{"value":"0.02","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[21].concentration","original":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x stock","interpretation":"The exact primary table supports this separate vitamin-stock batch amount and current APIs explicitly declare the stored g_l on that stock basis. It is not a main-medium concentration. Restore the ten-component stock and1ml addition; listed1000ml water does not independently establish a measured final stock volume.","sources":[{"locator":"extracted-text physical LF lines 57-57","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Biotin                                     20.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[0]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 57-57","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Biotin                                     20.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q48","subject":"Folic acid Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[22].concentration","original":{"value":"0.02","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[22].concentration","original":{"value":"0.02","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[22].concentration","original":{"value":"0.02","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[22].concentration","original":{"value":"0.02","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[22].concentration","original":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x stock","interpretation":"The exact primary table supports this separate vitamin-stock batch amount and current APIs explicitly declare the stored g_l on that stock basis. It is not a main-medium concentration. Restore the ten-component stock and1ml addition; listed1000ml water does not independently establish a measured final stock volume.","sources":[{"locator":"extracted-text physical LF lines 58-58","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Folic acid                                 20.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[1]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 58-58","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Folic acid                                 20.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[1]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q49","subject":"Pyridoxine hydrochloride Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[23].concentration","original":{"value":"0.1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[23].concentration","original":{"value":"0.1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[23].concentration","original":{"value":"0.1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[23].concentration","original":{"value":"0.1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[23].concentration","original":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x stock","interpretation":"The exact primary table supports this separate vitamin-stock batch amount and current APIs explicitly declare the stored g_l on that stock basis. It is not a main-medium concentration. Restore the ten-component stock and1ml addition; listed1000ml water does not independently establish a measured final stock volume.","sources":[{"locator":"extracted-text physical LF lines 59-59","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Pyridoxine hydrochloride                  100.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[2]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 59-59","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Pyridoxine hydrochloride                  100.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[2]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q50","subject":"Thiamine HCl Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[24].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[24].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[24].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[24].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[24].concentration","original":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x stock","interpretation":"The exact primary table supports this separate vitamin-stock batch amount and current APIs explicitly declare the stored g_l on that stock basis. It is not a main-medium concentration. Restore the ten-component stock and1ml addition; listed1000ml water does not independently establish a measured final stock volume.","sources":[{"locator":"extracted-text physical LF lines 60-60","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Thiamine HCl                               50.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[3]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 60-60","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Thiamine HCl                               50.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[3]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q51","subject":"Riboflavin Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[25].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[25].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[25].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[25].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[25].concentration","original":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x stock","interpretation":"The exact primary table supports this separate vitamin-stock batch amount and current APIs explicitly declare the stored g_l on that stock basis. It is not a main-medium concentration. Restore the ten-component stock and1ml addition; listed1000ml water does not independently establish a measured final stock volume.","sources":[{"locator":"extracted-text physical LF lines 61-61","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Riboflavin                                 50.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[4]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 61-61","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Riboflavin                                 50.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[4]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q52","subject":"Nicotinic acid Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[26].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[26].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[26].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[26].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[26].concentration","original":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x stock","interpretation":"The exact primary table supports this separate vitamin-stock batch amount and current APIs explicitly declare the stored g_l on that stock basis. It is not a main-medium concentration. Restore the ten-component stock and1ml addition; listed1000ml water does not independently establish a measured final stock volume.","sources":[{"locator":"extracted-text physical LF lines 62-62","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Nicotinic acid                             50.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[5]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 62-62","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Nicotinic acid                             50.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[5]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q53","subject":"Calcium D-(+)-pantothenate Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[27].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[27].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[27].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[27].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[27].concentration","original":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x stock","interpretation":"The exact primary table supports this separate vitamin-stock batch amount and current APIs explicitly declare the stored g_l on that stock basis. It is not a main-medium concentration. Restore the ten-component stock and1ml addition; listed1000ml water does not independently establish a measured final stock volume.","sources":[{"locator":"extracted-text physical LF lines 63-63","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Calcium D-(+)-pantothenate                 50.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[6]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 63-63","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Calcium D-(+)-pantothenate                 50.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[6]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q54","subject":"Vitamin B12 Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[28].concentration","original":{"value":"0.001","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[28].concentration","original":{"value":"0.001","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[28].concentration","original":{"value":"0.001","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[28].concentration","original":{"value":"0.001","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[28].concentration","original":{"value":"0.001","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x stock","interpretation":"The exact primary table supports this separate vitamin-stock batch amount and current APIs explicitly declare the stored g_l on that stock basis. It is not a main-medium concentration. Restore the ten-component stock and1ml addition; listed1000ml water does not independently establish a measured final stock volume.","sources":[{"locator":"extracted-text physical LF lines 64-64","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Vitamin B12                                 1.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[7]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 64-64","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Vitamin B12                                 1.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[7]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q55","subject":"p-Aminobenzoic acid Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[29].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[29].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[29].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[29].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[29].concentration","original":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x stock","interpretation":"The exact primary table supports this separate vitamin-stock batch amount and current APIs explicitly declare the stored g_l on that stock basis. It is not a main-medium concentration. Restore the ten-component stock and1ml addition; listed1000ml water does not independently establish a measured final stock volume.","sources":[{"locator":"extracted-text physical LF lines 65-65","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   p-Aminobenzoic acid                        50.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[8]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 65-65","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   p-Aminobenzoic acid                        50.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[8]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q56","subject":"(DL)-alpha-Lipoic acid Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[30].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[30].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[30].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[30].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[30].concentration","original":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x stock","interpretation":"The exact primary table supports this separate vitamin-stock batch amount and current APIs explicitly declare the stored g_l on that stock basis. It is not a main-medium concentration. Restore the ten-component stock and1ml addition; listed1000ml water does not independently establish a measured final stock volume.","sources":[{"locator":"extracted-text physical LF lines 66-66","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   (DL)-alpha-Lipoic acid                     50.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[9]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 66-66","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   (DL)-alpha-Lipoic acid                     50.00   mg","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[9]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q57","subject":"dsm813a Trace element solution SL-10 dose","local_fields":[],"decision":"add","stage":"exact source receiving dose","interpretation":"Restore the distinct1ml addition in this exact source branch; do not place stock component rates at root or transfer a strain alternative.","sources":[{"locator":"extracted-text physical LF lines 13-13","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Trace element solution SL-10                               1.00        ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[6]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q58","subject":"dsm813a Wolin's vitamin solution (10x) dose","local_fields":[],"decision":"add","stage":"exact source receiving dose","interpretation":"Restore the distinct1ml addition in this exact source branch; do not place stock component rates at root or transfer a strain alternative.","sources":[{"locator":"extracted-text physical LF lines 20-20","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Wolin's vitamin solution (10x)                             1.00        ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[13]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 14,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q59","subject":"dsm813a Main sol. 813a water","local_fields":[],"decision":"add","stage":"separate source water input","interpretation":"Preserve main1000ml, SL10 initial990ml and Wolin1000ml water as distinct inputs. SL10 separately makes up to1000ml; DSM813a separately declares mainfinal1002ml. Do not sum preparation waters or infer a primary866 final volume.","sources":[{"locator":"extracted-text physical LF lines 21-21","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Distilled water                                         1000.00        ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[14]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q60","subject":"dsm813a Trace element solution SL-10 water","local_fields":[],"decision":"add","stage":"separate source water input","interpretation":"Preserve main1000ml, SL10 initial990ml and Wolin1000ml water as distinct inputs. SL10 separately makes up to1000ml; DSM813a separately declares mainfinal1002ml. Do not sum preparation waters or infer a primary866 final volume.","sources":[{"locator":"extracted-text physical LF lines 42-42","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Distilled water                                           990.00      ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[9]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q61","subject":"dsm813a Wolin's vitamin solution (10x) water","local_fields":[],"decision":"add","stage":"separate source water input","interpretation":"Preserve main1000ml, SL10 initial990ml and Wolin1000ml water as distinct inputs. SL10 separately makes up to1000ml; DSM813a separately declares mainfinal1002ml. Do not sum preparation waters or infer a primary866 final volume.","sources":[{"locator":"extracted-text physical LF lines 67-67","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Distilled water                          1000.00   ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[10]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q62","subject":"dsm866 Trace element solution SL-10 dose","local_fields":[],"decision":"add","stage":"exact source receiving dose","interpretation":"Restore the distinct1ml addition in this exact source branch; do not place stock component rates at root or transfer a strain alternative.","sources":[{"locator":"extracted-text physical LF lines 9-9","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Trace element solution SL-10                               1.00        ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[6]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q63","subject":"dsm866 Wolin's vitamin solution (10x) dose","local_fields":[],"decision":"add","stage":"exact source receiving dose","interpretation":"Restore the distinct1ml addition in this exact source branch; do not place stock component rates at root or transfer a strain alternative.","sources":[{"locator":"extracted-text physical LF lines 15-15","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Wolin's vitamin solution (10x)                             1.00        ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[12]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q64","subject":"dsm866 Main sol. 866 water","local_fields":[],"decision":"add","stage":"separate source water input","interpretation":"Preserve main1000ml, SL10 initial990ml and Wolin1000ml water as distinct inputs. SL10 separately makes up to1000ml; DSM813a separately declares mainfinal1002ml. Do not sum preparation waters or infer a primary866 final volume.","sources":[{"locator":"extracted-text physical LF lines 17-17","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Distilled water                                         1000.00        ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[14]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q65","subject":"dsm866 Trace element solution SL-10 water","local_fields":[],"decision":"add","stage":"separate source water input","interpretation":"Preserve main1000ml, SL10 initial990ml and Wolin1000ml water as distinct inputs. SL10 separately makes up to1000ml; DSM813a separately declares mainfinal1002ml. Do not sum preparation waters or infer a primary866 final volume.","sources":[{"locator":"extracted-text physical LF lines 42-42","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Distilled water                                           990.00      ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[9]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q66","subject":"dsm866 Wolin's vitamin solution (10x) water","local_fields":[],"decision":"add","stage":"separate source water input","interpretation":"Preserve main1000ml, SL10 initial990ml and Wolin1000ml water as distinct inputs. SL10 separately makes up to1000ml; DSM813a separately declares mainfinal1002ml. Do not sum preparation waters or infer a primary866 final volume.","sources":[{"locator":"extracted-text physical LF lines 67-67","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Distilled water                          1000.00   ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[2].recipe[10]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q67","subject":"DSM813a explicit final denominator","local_fields":[],"decision":"add","stage":"DSM813a main denominator","interpretation":"Record positive primary final1002ml at the813a layer. This denominator supports its main arithmetic and does not independently validate other source versions.","sources":[{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final volume: 1002 ml","quote_representation":"captured extracted text"}]},{"decision_id":"q68","subject":"DSM813a retained pH and main sequence","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ph_range","original":{"min":9.0,"max":9.5}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ph_range","original":{"min":9.0,"max":9.5}},{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"preparation_steps[0].description","original":"Dissolve the ingredients (except carbonates, sulfide, formate, and vitamins) and sparge medium with 100% N2 gas for 30 - 45 min. to make it anoxic. Add and dissolve carbonates and sulfide, then adjust pH to 9.0 - 9.5, dispense under 100% N2 gas atmosphere into Hungate-type tubes or serum vials and autoclave. Before use add formate and vitamins (sterilized by filtration) from sterile anoxic stock solutions prepared under 100% N2 gas."},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"preparation_steps[0].description","original":"Dissolve the ingredients (except carbonates, sulfide, formate, and vitamins) and sparge medium with 100% N2 gas for 30 - 45 min. to make it anoxic. Add and dissolve carbonates and sulfide, then adjust pH to 9.0 - 9.5, dispense under 100% N2 gas atmosphere into Hungate-type tubes or serum vials and autoclave. Before use add formate and vitamins (sterilized by filtration) from sterile anoxic stock solutions prepared under 100% N2 gas."}],"decision":"evidence_only","stage":"DSM813a main preparation","interpretation":"Retain pH9–9.5 and the source30–45min100%N2 sequence, carbonates/sulfide before autoclaving, and later sterile formate and filtered vitamins. These correct813a fields do not validate the generated866 ingredient amounts.","sources":[{"locator":"extracted-text physical LF lines 23-27","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Dissolve the ingredients (except carbonates, sulfide, formate, and vitamins) and sparge\nmedium with 100% N2 gas for 30 - 45 min. to make it anoxic. Add and dissolve carbonates\nand sulfide, then adjust pH to 9.0 - 9.5, dispense under 100% N2 gas atmosphere into\nHungate-type tubes or serum vials and autoclave. Before use add formate and vitamins\n(sterilized by filtration) from sterile anoxic stock solutions prepared under 100% N2 gas.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].steps[0]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"step\": \"Dissolve the ingredients (except carbonates, sulfide, formate, and vitamins) and sparge medium with 100% N2 gas for 30 - 45 min. to make it anoxic. Add and dissolve carbonates and sulfide, then adjust pH to 9.0 - 9.5, dispense under 100% N2 gas atmosphere into Hungate-type tubes or serum vials and autoclave. Before use add formate and vitamins (sterilized by filtration) from sterile anoxic stock solutions prepared under 100% N2 gas.\"\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q69","subject":"KOMODO866 pH source reconciliation","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ph_range","original":{"min":8.7,"max":9.0}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ph_range","original":{"min":8.7,"max":9.0}}],"decision":"correct","stage":"DSM866 main preparation","interpretation":"The two KOMODO ranges 8.7–9.0 have a different lower bound and omit the main preparation; the current DSM866 primary requires 8.8–9.0 and 100% N2, with sulfide added after sterilization. Restore only with exact current branch evidence; DSM813a sulfide timing and pH are distinct. Already-correct DSM866 owner fields are credited separately in q71.","sources":[{"locator":"extracted-text physical LF lines 19-24","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"Dissolve the ingredients (except carbonate, bicarbonate, vitamins, formate and sulfide,)\nand sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\ncarbonate and bicarbonate, adjust pH to 8.8 - 9.0, then dispense under 100% N2 gas\natmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add\nvitamins (sterilized by filtration), formate and sulfide from sterile anoxic stock solutions\nprepared under 100% N2 gas.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\": \"Dissolve the ingredients (except carbonate, bicarbonate, vitamins, formate and sulfide,) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate and bicarbonate, adjust pH to 8.8 - 9.0, then dispense under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add vitamins (sterilized by filtration), formate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas.\"\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q70","subject":"SL10 makeup instruction placement","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"preparation_steps[1].description","original":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"preparation_steps[1].description","original":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"preparation_steps[1].description","original":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}],"decision":"correct","stage":"SL10 preparation","interpretation":"Existing dissolve/make-up-to1000ml text is correct source content but wrongly stored as a main-medium step. Relocate it withSL10 and add it at stock scope in the two KOMODO contributors; do not alter its positive final-volume evidence.","sources":[{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q71","subject":"Existing DSM866 pH and main procedure","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ph_range","original":{"min":8.8,"max":9.0}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"preparation_steps[0].description","original":"Dissolve the ingredients (except carbonate, bicarbonate, vitamins, formate and sulfide,) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate and bicarbonate, adjust pH to 8.8 - 9.0, then dispense under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add vitamins (sterilized by filtration), formate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas."}],"decision":"evidence_only","stage":"DSM866 main preparation","interpretation":"The existing DSM866 owner ph_range 8.8–9.0 and retained main preparation match the exact current DSM866 source. Retain both unchanged and attach supporting evidence. The differing KOMODO lower bounds remain scoped separately in q69; no DSM813a conditions are transferred.","sources":[{"locator":"extracted-text physical LF lines 19-24","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"Dissolve the ingredients (except carbonate, bicarbonate, vitamins, formate and sulfide,)\nand sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\ncarbonate and bicarbonate, adjust pH to 8.8 - 9.0, then dispense under 100% N2 gas\natmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add\nvitamins (sterilized by filtration), formate and sulfide from sterile anoxic stock solutions\nprepared under 100% N2 gas.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\": \"Dissolve the ingredients (except carbonate, bicarbonate, vitamins, formate and sulfide,) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate and bicarbonate, adjust pH to 8.8 - 9.0, then dispense under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add vitamins (sterilized by filtration), formate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas.\"\n                    }","quote_representation":"raw JSON object"}]}],"local_field_census_reference":"REVIEW_WORK/batch077/record06/grounding-inventory.json","source_only_gaps_are_explicit":true,"note":"Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:001959.

data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml: primary 30/31, secondary 28/31; data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml: primary 30/31, secondary 28/31; data/normalized_yaml/bacterial/desulfofalx_medium.yaml: primary 30/31, secondary 28/31; data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml: primary 30/31, secondary 28/31; data/normalized_yaml/bacterial/for_dsm_16529.yaml: primary 30/31, secondary 28/31. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:001959.

Complete selected target and all exact maintained contributors reviewed. Stocks are embedded in the named DSM source recipes; no external dependency parent recipe is transferred. Named strain alternatives remain distinct from the generic basal formulation.

### Native structural checks

schema: supported. Targets: CultureMech:001959.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Generated813a record combines different source recipes

major / open / confirmed; issue key: culturemech-001959-variant-merge.

The generated identity and procedure are813a, but six main amounts are866 values. The maintained813a owner also inherits API sulfate/carbonate inconsistency and unnormalized bicarbonate. Distinct866 andDSM16529 relationships must not be treated as identical scientific formulations.

### f2: DSM16529 wrapper omits its explicit substrate substitution

major / open / confirmed; issue key: culturemech-001959-strain-substrate.

The strain-specific contributor retains basal formate despite the exact current866 primary requiring sodiumL-lactate instead. Existing STRAIN_SPECIFIC_VARIANT topology is correct but scientifically incomplete.

### f3: Embedded stock quantities occupy main ingredients

major / open / confirmed; issue key: culturemech-001959-stocks.

All five layers flattenSL10 andWolin10x components at root. HCl2.5g/L lacks a verified percent basis; the validSL10 stock mass rates require their own explicit1000ml makeup, and vitamin rates remain provider stock values. Receiving doses and separate water inputs are missing.

### f4: Stock steps and KOMODO atmosphere metadata are inconsistent

major / open / confirmed; issue key: culturemech-001959-preparation.

The threeDSM/generated documents placeSL10 makeup at root. BothKOMODO contributors omit preparation and store Aerobic: Yes in notes, contradicting the exact current anaerobic source. Their pH lower bound also differs. Preserve the correct, different813a and866 main sequences.

### f5: Nickel hydrate and sodium resazurin are linked to different supplied forms

major / open / confirmed; issue key: culturemech-001959-nickel-hydrate-and-sodium-resazurin-form.

Every selected layer names nickel chloride hexahydrate but asserts anhydrous nickel dichloride CHEBI:34887 in both primary and secondary slots. Sodium resazurin is linked through its primary slot to neutral Resazurin CHEBI:8806; there is no asserted resazurin secondary slot to correct. Exact labels pass native checks, but OLS formulas Cl2Ni and C12H7NO4 do not encode the supplied forms. Current MIM matches describe those asserted IDs, not hydrate or sodium-salt equivalence.

### f6: Historical timestamps and absent claim evidence need bounded follow-up

minor / open / confirmed; issue key: culturemech-001959-provenance.

Selected records have no attached formulation excerpts. KOMODO events store literal.fZ and resolver events lack offsets. Current code behavior and historical report byte matches cannot recover those original instants or authenticate historical execution.

## Recommended Actions And Acceptance Checks

### action1

Separate exact source formulations before regeneration; correct813a using its primary1002ml basis, retain supported values and reject cross-variant ingredient-set merging.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Represent the exactDSM16529 source modification within that maintained variant only; preserve generic866 and813a recipes and avoid treating catalogue association as an experimental growth measurement.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Restore each exact stock and receiving dose with separate batch/final-volume evidence. Retain positiveSL10 makeup and supported main rates; do not convert bare25% acid by guessed density or promote provider stock rates to the medium.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Scope stock preparation insideSL10 and restore exact current branch pH/anaerobic preparation while retaining historical source notes as provenance rather than active cultivation assertions.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action5

Resolve the exact source hydrate and sodium-salt identities against authoritative ontology and MIM records. Use verified supplied-form mappings or retain precise source labels with unresolved mapping; preserve source masses and do not substitute anhydrous molar arithmetic.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action6

Preserve all original events and append actual verified source context; repair the exact current timestamp writers for future events without inventing old timestamps. Attach excerpts only at schema-supported scopes.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.
- Verify komodo_web_importer.py and DSMZCompositionResolver future events use valid timezone-aware UTC timestamps; retain all original historical event bytes and distinguish stored.fZ from the current%f format token.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local2 | data/normalized_yaml/bacterial/desulfofalx_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local3 | data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local4 | data/normalized_yaml/bacterial/for_dsm_16529.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch077/record06/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch077/record06/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch077/record06/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch077/record06/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| dsm813a | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete exact DSM primary PDF text and every rendered page read, including main recipe, separate stock tables and all staged procedures. Physical LF line locators refer to the preserved pdftotext output. |
| api813a | https://mediadive.dsmz.de/rest/medium/813a; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current provider identity, solution tables and preparation read. Explicit g_l and declared volumes are credited only on their named provider stock or recipe basis; they are not independent measured final volumes. Provider mmol_l values are not adopted as chemical-form authority. |
| dsm866 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete exact DSM primary PDF text and every rendered page read, including main recipe, separate stock tables and all staged procedures. Physical LF line locators refer to the preserved pdftotext output. |
| api866 | https://mediadive.dsmz.de/rest/medium/866; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current provider identity, solution tables and preparation read. Explicit g_l and declared volumes are credited only on their named provider stock or recipe basis; they are not independent measured final volumes. Provider mmol_l values are not adopted as chemical-form authority. |
| komodo866 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=866; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual HTTP 403 response, not formulation evidence. |
| komodo866.1 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=866.1; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual HTTP 403 response, not formulation evidence. |
| dsm16529Identity | https://www.dsmz.de/collection/catalogue/details/culture/DSM-16529; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Current collection identity and strain-specific medium association only. DSM16529 is listed as Desulfohalovibrio alkalitolerans, risk group 1, with modified medium866; this page is not a substitute recipe or new experimental growth assertion. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4']; mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16494 = lipoic acid; definition ['A heterocyclic thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the 5-position.']; formula ['C8H14O2S2']; mass ['206.332']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17015 = riboflavin; definition ['&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide.']; formula ['C17H20N4O6']; mass ['376.369']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17883 = hydrogen chloride; definition ['A mononuclear parent hydride consisting of covalently bonded hydrogen and chlorine atoms.']; formula ['HCl']; mass ['36.461']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:27470 = folic acid; definition ['An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6']; mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group.']; formula ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32139 = sodium hydrogencarbonate; definition []; formula ['CHO3.Na']; mass ['84.006']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32149 = sodium sulfate; definition []; formula ['2Na.O4S']; mass ['142.043']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3']; mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49105 = thiamine hydrochloride; definition ['A hydrochloride obtained by combining thiamine chloride with one molar equivalent of hydrochloric acid.']; formula ['C12H17N4OS.Cl.HCl']; mass ['337.276']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49976 = zinc dichloride; definition ['A compound of zinc and chloride ions in the ratio 1:2. It exists in four crystalline forms, in each of which the Zn&lt;small&gt;&lt;sup&gt;2+&lt;/small&gt;&lt;/sup&gt; ions are trigonal planar coordinated to four chloride ions.']; formula ['2Cl.Zn']; mass ['136.296']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi62965 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:62965; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:62965 = sodium formate; definition ['An organic sodium salt which is the monosodium salt of formic acid.']; formula ['CHO2.Na']; mass ['68.007']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na']; mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:76209 = sodium sulfide nonahydrate; definition ['A hydrate with formula Na&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;S·9H&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;O.']; formula ['9H2O.2Na.S']; mass ['240.182']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86249 = iron dichloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of iron dichloride.']; formula ['Cl2Fe.4H2O']; mass ['198.811']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg']; mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch077/record06/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected and dependency-context term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/desulfotomaculum_alkaliphilum_medium.yaml.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history1 | reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/for_dsm_16529.yaml.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history2 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfofalx_medium.yaml.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history3 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfonatronum_thiodismutans_medium.yaml.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history4 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history5 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfofalx_medium.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history6 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history7 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history8 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_16529.md; entire report; lossless historical reader; exact selected parent rows | supports | Complete report body read and losslessly retained. Zero-source-check diagnostics are historical structure only. Exact selected historical parent rows and current byte matches are separately joined; same-label unselected siblings and unrelated dependency parent recipes remain context-only. Old report conclusions are reassessed against the exact current source rather than automatically adopted; dates and historical execution are not authenticated. |
| history-auth | REVIEW_WORK/batch077/record06/historical-authentication.json; attached_claims; historical_plan_claims | supports | Actual attached claims in scoped stock sections and historical parent-plan claims are separate populations. Current raw-digest equality and literal or normalized-HTML excerpt equality are independently recorded. No attached formulation claims occur on the selected target or its maintained contributors. Current byte matches do not authenticate historical execution or access dates. |
| historical-current-joins | REVIEW_WORK/batch077/record06/historical-current-joins.json; all selected parents and claims | supports | Exact selected historical parent rows, source raw digest and all literal/decoded source-object joins. These are separate from absent attached formulation evidence and do not authenticate historical dates. |
| writer58 | scripts/apply_mim_groundings.py; target_slot; groundable; apply_to_record | context_only | Current target_slot preserves existing CHEBI assertions; groundable excludes conflicting corpus opinions, and apply_to_record fills ungrounded entries from proposals. This writer does not authenticate source amounts or automatically repair an existing wrong supplied-form ID. |
| writer59 | scripts/assign_culturemech_ids.py; assign_ids; _assign_id_to_file | context_only | Current assign_ids selects records with missing IDs; _assign_id_to_file checks new-ID collisions and appends identifier provenance. Identifier assignment does not authenticate recipe content or demonstrate historical source access. |
| writer60 | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group collapses equal duplicate values without summing them and retains the first conflicting value with a flag. This behavior is distinct from historical summed-amount artifacts and does not authenticate source-specific stock or product structure. |
| writer61 | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients; merge_ingredient_group | context_only | Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group retains the first concentration, flags differing values and selects the first CHEBI. It cannot establish source stages or justify collapsing independent supplemental and product-contained components. |
| writer62 | scripts/migrate_legacy_mim_to_chebi.py; _resolve_chebi; _rewrite_entry | context_only | Current _resolve_chebi reuses current primary CHEBI where available and considers bounded exact-name/synonym matches with a stereo-prefix guard; _rewrite_entry retains unresolved links. Current-row presence is distinct from historical validity and from source-specific supplied-form equivalence. |
| writer63 | scripts/migrate_ph_range.py; parse_ph_range; migrate_one | context_only | Current parse_ph_range retains qualifiers in notes and migrate_one converts only string-valued pH ranges, recording provenance. No particular source range is authenticated by this writer. |
| writer64 | scripts/refill_term_labels.py; refill_text | context_only | Current refill_text replaces term labels using the current exact identifier lookup while preserving other text. Canonical label correspondence is not an independent choice of the correct chemical form for the supplied source reagent. |
| writer65 | scripts/repair_komodo_866_desulfofalx_score10.py; _require_record; repair_parent; repair_child; _upsert_event; TIMESTAMP | context_only | Current _require_record checks exact IDs, source terms and a fixed 31-ingredient signature. repair_parent and repair_child set SOURCE_DUPLICATE for866 and STRAIN_SPECIFIC_VARIANT for866.1 and preserve existing quantities; they do not reconstruct the DSM16529 substrate replacement. _upsert_event replaces an event with the same curator/action or appends it; TIMESTAMP is a hardcoded historical date. Current relationship repair is credited without authenticating original execution or strain-specific composition. |
| writer66 | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata | context_only | Current DSMZCompositionResolver.merge_composition copies ingredients and solutions, fills pH when absent and copies physical/medium type, but does not copy preparation steps. _add_enrichment_metadata records a naive current timestamp. This explains a present omission risk, not historical execution. |
| writer67 | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current _convert_to_culturemech constructs source notes and default LIQUID with empty ingredients. Its time.strftime format contains %f, which is unsupported here and is consistent with literal .fZ in stored import events. Current code does not authenticate the original retrieval or justify rewriting historical time. |
| writer68 | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps | context_only | Current _parse_api_composition considers the primary recipe, prefers provider g_l when available and excludes four recognized water labels; tap water is not among those exclusions; _is_api_stock_addition distinguishes stock additions. _parse_api_solutions retains separate stock structure. _parse_preparation_steps collects solution prose. These present behaviors do not establish historical execution and cannot justify interpreting flattened stock rates as final-medium concentrations. |
| writer69 | src/culturemech/match/kg_media_matcher.py; extract_recipe_ingredients; find_matches; find_exact_match | context_only | Current extract_recipe_ingredients collects asserted CHEBI/FOODON IDs, find_matches compares set Jaccard and find_exact_match selects the first exact identifier set. Quantities, preparation and ungrounded ingredients are not compared, so an exact set match does not establish formulation identity. |
| writer70 | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current formulation_content retains exact scientific quantities, preparation and other scientific fields; merge_formulation_evidence rejects incompatible projections and unions evidence at matching scopes. A source-equivalence claim is not established by shared ingredient identities. |
| writer71 | src/culturemech/merge/matcher.py; group_formulations; group_recipes | context_only | Current group_formulations calls group_recipes with fail_on_invalid=True and FormulationFingerprinter. Expected standalone or unfingerprintable records are excluded; malformed or unexpected inputs raise. Valid records are grouped by full scientific content. This guard does not retrieve or authenticate source recipes. |
| writer72 | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group routes a single maintained owner with merge metadata; multiple owners pass through conservative merge_formulation_evidence. Regenerating from an unrepaired owner retains its defects. Current conservative behavior is credited and does not establish how the old generated record was produced. |
| writer73 | src/culturemech/validation/schema_defaulter.py; apply_defaults; _fix_ingredient; _fix_solution | context_only | Current apply_defaults, _fix_ingredient and _fix_solution can insert VARIABLE amounts and placeholder names for structural completeness. A default is not evidence for a dose, composition, solution identity or denominator; existing default-history events remain contextual. |
| quantity-inventory | REVIEW_WORK/batch077/record06/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- Exact historical KOMODO866/866.1 routes returned403 and are preserved; currentDSM sources and catalogue support bounded conclusions without authenticating inaccessible historical versions.
- OnlyDSM813a explicitly declares main final1002ml; DSM866 g_l values remain qualified provider normalization. BareHCl25% has no established basis.
- Current exact API digest/object equality does not authenticate historical access dates or execution. Named source variants remain distinct; no experimental growth claim or record edit was made.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T204800Z-desulfonatronum-thiodismutans-medium-batch077
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of desulfonatronum_thiodismutans_medium
started_at: '2026-10-28T20:14:28.581336Z'
finished_at: '2026-10-28T20:48:00.905151Z'
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
summary: The generated record combines DSM813a identity and preparation with DSM866
  amounts. Exact primary evidence separates those recipes and identifies the missingDSM16529
  substrate replacement. Stock flattening, several supplied-form IDs, preparation
  placement and provenance remain defective; correct current owner fields and repaired
  variant relationships are credited.
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
  - path: data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml
    sha256: 80832874fc1b18fb83bddfcb7b8a69a7f4b6c8b55f0512b3493d36f4d5224332
    role: target
  - path: data/normalized_yaml/bacterial/desulfofalx_medium.yaml
    sha256: 22d685e662302d9cec1efa62ebd4c1c6f8b5fa7a5a9a8003ab2ad18eddd68034
    role: context
  - path: data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml
    sha256: b97f8782c23e921d83f92cfa9fdd71da0951a5591cd5fbb53f38505f59b5c720
    role: context
  - path: data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml
    sha256: f952c4614804082275ecd1c5e27f1d51ee0f0bbdb34556e289a18384ccb96e2a
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_16529.yaml
    sha256: 06e3f49f89034fb04da976e4c9095e8f154ea40d9321c9a0908d6a29b37b61c4
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/inspected-candidate-context.json
    sha256: 0bb2da58a82dc2b4a90beef1224a7355fd5632db772be0ef053bde40754ded87
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json
    sha256: 1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/desulfotomaculum_alkaliphilum_medium.yaml.md
    sha256: 544f07f8771fa2ab667cedf1bc2b2eb709b0f87b5175e46604e0cdeb011c6b2d
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/for_dsm_16529.yaml.md
    sha256: 305aa881f4d20fa939db9aab0060f42bfe57feb910ae682bdde7e1f5960758af
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
    sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfofalx_medium.yaml.md
    sha256: 08e759efbd1e911ce9a765da3fef882554b586245add66507752c4d24bcd8142
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfonatronum_thiodismutans_medium.yaml.md
    sha256: c5c2d04ad59bbf637294b56e250851bbff5cb8abe19fb6c355ca811c1d2d62dd
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.md
    sha256: d87a0bc2d7a6a6477f55aa47c82b272fb060249c38f0ba111912b4c4adc044f1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfofalx_medium.md
    sha256: ff5a3bed0867d9b32c7319fb613458a7827061a7a437d8c84ef2e6a324e9d620
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.md
    sha256: d12e282df34ce5493d8ed4f6f7fa69ae06565ecafdcdc637854d529abf97c840
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.md
    sha256: 623989d27923b2980a6e7710063a88efafe43a0307f7bd89402c0579c24815a8
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_16529.md
    sha256: 8ab7395954627f968dd68fb1f8fa38a2c78ae3ed4037742aaee2735079ffa731
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
  - path: scripts/repair_komodo_866_desulfofalx_score10.py
    sha256: 126756b83c092c41786d0381fdb2d6d3bd609f4d85df14ecaadbd1f72a196319
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
  selection: Authoritative batch077 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001959
targets:
- target_id: CultureMech:001959
  path: data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml
  label: desulfonatronum_thiodismutans_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfofalx_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16529.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:001959
  command: just validate-schema data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:001959
  command: just validate-strict data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml
    --workers 1 --out REVIEW_WORK/batch077/record06/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:001959
  command: just validate-terms data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:001959
  command: just validate-references data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T20:25:38.829558Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 80832874fc1b18fb83bddfcb7b8a69a7f4b6c8b55f0512b3493d36f4d5224332
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T20:25:38.829711Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: b97f8782c23e921d83f92cfa9fdd71da0951a5591cd5fbb53f38505f59b5c720
- evidence_id: local2
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfofalx_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T20:25:38.829741Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 22d685e662302d9cec1efa62ebd4c1c6f8b5fa7a5a9a8003ab2ad18eddd68034
- evidence_id: local3
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T20:25:38.829776Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: f952c4614804082275ecd1c5e27f1d51ee0f0bbdb34556e289a18384ccb96e2a
- evidence_id: local4
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_16529.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T20:25:38.829804Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 06e3f49f89034fb04da976e4c9095e8f154ea40d9321c9a0908d6a29b37b61c4
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch077/record06/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T20:14:29.660230Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 390108bd034fec786ab0934ba0360c407f58c8ddfdfc87102141c7192f4da470
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch077/record06/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T20:14:30.588007Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: fdb5a43542b6999e37f944d6adff6adb03731d4ba69d2929332b38245aae47d1
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch077/record06/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T20:14:31.618579Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: b958ab4a1b990916fc3a6f23b58445c09420e673c2406c2b1cc391ab3218149e
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch077/record06/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T20:14:32.357169Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: d0d5af9fbfd0d146a7d6d50c9db07cec3bbe8a742e5bb626f3a2fab210f9ac43
- evidence_id: dsm813a
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T20:14:19.748215Z'
  support: supports
  summary: Complete exact DSM primary PDF text and every rendered page read, including
    main recipe, separate stock tables and all staged procedures. Physical LF line
    locators refer to the preserved pdftotext output.
  snapshot_sha256: 54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9
- evidence_id: api813a
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/813a
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T20:14:19.333712Z'
  support: supports
  summary: Complete current provider identity, solution tables and preparation read.
    Explicit g_l and declared volumes are credited only on their named provider stock
    or recipe basis; they are not independent measured final volumes. Provider mmol_l
    values are not adopted as chemical-form authority.
  snapshot_sha256: a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1
- evidence_id: dsm866
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T20:14:19.999222Z'
  support: supports
  summary: Complete exact DSM primary PDF text and every rendered page read, including
    main recipe, separate stock tables and all staged procedures. Physical LF line
    locators refer to the preserved pdftotext output.
  snapshot_sha256: 441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79
- evidence_id: api866
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/866
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T20:14:19.706329Z'
  support: supports
  summary: Complete current provider identity, solution tables and preparation read.
    Explicit g_l and declared volumes are credited only on their named provider stock
    or recipe basis; they are not independent measured final volumes. Provider mmol_l
    values are not adopted as chemical-form authority.
  snapshot_sha256: 8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148
- evidence_id: komodo866
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=866
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T20:14:20.013050Z'
  support: unknown
  summary: Actual HTTP 403 response, not formulation evidence.
  snapshot_sha256: 0f68d0d5565c09dc5f5416f09b9846fe4758053dacca4136e9d37c5e20557409
- evidence_id: komodo866.1
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=866.1
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T20:14:20.057253Z'
  support: unknown
  summary: Actual HTTP 403 response, not formulation evidence.
  snapshot_sha256: f012acdbc274708e35667f4e6e30de3caae3ec6fdbd52e6ad05d0b1d40febe99
- evidence_id: dsm16529Identity
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-16529
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T20:14:20.082451Z'
  support: supports
  summary: Current collection identity and strain-specific medium association only.
    DSM16529 is listed as Desulfohalovibrio alkalitolerans, risk group 1, with modified
    medium866; this page is not a substitute recipe or new experimental growth assertion.
  snapshot_sha256: 08e4dba4a2f52396cd2d62b1ca21e72e766eb347dc8c6f08b303d1703fb51d72
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:15:01.281303Z'
  support: supports
  summary: OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4'];
    mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f2530ec9c15f59a3d132a466c9c3a899497bab0f85b996d3e27bef8612f89982
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:15:01.281454Z'
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
  accessed_at: '2026-10-28T20:15:01.281499Z'
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
  accessed_at: '2026-10-28T20:15:01.281533Z'
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
  accessed_at: '2026-10-28T20:15:02.065073Z'
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
  accessed_at: '2026-10-28T20:15:02.097390Z'
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
  accessed_at: '2026-10-28T20:15:02.274845Z'
  support: supports
  summary: OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic
    chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass
    ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:15:02.726179Z'
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
  accessed_at: '2026-10-28T20:15:02.739188Z'
  support: supports
  summary: OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula
    ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: e0c2a85ab7be9313c564f96ee47b87e1bf3e01ad1e9fd627d1dbddced5d068c4
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:15:02.780668Z'
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
  accessed_at: '2026-10-28T20:15:02.806234Z'
  support: supports
  summary: OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The
    hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 855ea2cf0e89d25ab4a560ab1c2dab6ac861d215bc5473cb4d3a0a2d4cdff438
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:15:02.893597Z'
  support: supports
  summary: OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic
    chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:15:03.310016Z'
  support: supports
  summary: OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula
    ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: c3341e7cf8a7ea0768d505265376c1514f161c9048b6e878314e204341d702eb
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:15:03.326142Z'
  support: supports
  summary: OLS current exact CHEBI:32139 = sodium hydrogencarbonate; definition [];
    formula ['CHO3.Na']; mass ['84.006']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 51709e2510736d0b63369147b10ec6ffe80d5d5c3a40605381de9b3ed78634c3
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:15:03.407187Z'
  support: supports
  summary: OLS current exact CHEBI:32149 = sodium sulfate; definition []; formula
    ['2Na.O4S']; mass ['142.043']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 96b73aef765e4edc893460a376cfedd136930f253bbeac639827b1daddb65d71
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:15:03.920879Z'
  support: supports
  summary: OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal
    chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:15:03.927796Z'
  support: supports
  summary: OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3'];
    mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:15:04.008587Z'
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
  accessed_at: '2026-10-28T20:15:04.094217Z'
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
  accessed_at: '2026-10-28T20:15:04.540243Z'
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
  accessed_at: '2026-10-28T20:15:04.634394Z'
  support: supports
  summary: OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition
    ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride
    and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: a626d2aa210aafd9572221d4893cd206310d5df507e474e1528997048f522250
- evidence_id: chebi62965
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:62965
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:15:04.665145Z'
  support: supports
  summary: OLS current exact CHEBI:62965 = sodium formate; definition ['An organic
    sodium salt which is the monosodium salt of formic acid.']; formula ['CHO2.Na'];
    mass ['68.007']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: cfd1c5de376b9874afbc0c231dfd94f0b4954f4b69c40062783876093e7f0354
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:15:04.714216Z'
  support: supports
  summary: OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition
    ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula
    ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:15:05.177449Z'
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
  accessed_at: '2026-10-28T20:15:05.234850Z'
  support: supports
  summary: OLS current exact CHEBI:76209 = sodium sulfide nonahydrate; definition
    ['A hydrate with formula Na<small><sub>2</sub></small>S·9H<small><sub>2</sub></small>O.'];
    formula ['9H2O.2Na.S']; mass ['240.182']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 4896ec517123ebeb1afcbac7bc30a7103976f03891af0c86c992196b5f0db969
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:15:05.318552Z'
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
  accessed_at: '2026-10-28T20:15:05.779017Z'
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
  accessed_at: '2026-10-28T20:15:05.786454Z'
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
  accessed_at: '2026-10-28T20:15:05.814155Z'
  support: supports
  summary: OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula
    ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T20:15:06.035535Z'
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
  reference: REVIEW_WORK/batch077/record06/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T20:25:38.840912Z'
  support: supports
  summary: Complete selected and dependency-context term slots and current packaged
    MIM CSV exact-identifier joins with row locators and metadata commit; includes
    separately scoped dependency context. No fuzzy mapping or historical-validity
    inference.
  snapshot_sha256: a4a6b95adb0ea87466058ffc6d38074727cff106be24c228bd8557dc5e514993
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/desulfotomaculum_alkaliphilum_medium.yaml.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T20:25:38.908167Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: 544f07f8771fa2ab667cedf1bc2b2eb709b0f87b5175e46604e0cdeb011c6b2d
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/for_dsm_16529.yaml.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T20:25:38.908221Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: 305aa881f4d20fa939db9aab0060f42bfe57feb910ae682bdde7e1f5960758af
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfofalx_medium.yaml.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T20:25:38.908267Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: 08e759efbd1e911ce9a765da3fef882554b586245add66507752c4d24bcd8142
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfonatronum_thiodismutans_medium.yaml.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T20:25:38.908305Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: c5c2d04ad59bbf637294b56e250851bbff5cb8abe19fb6c355ca811c1d2d62dd
- evidence_id: history4
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T20:25:38.908344Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: d87a0bc2d7a6a6477f55aa47c82b272fb060249c38f0ba111912b4c4adc044f1
- evidence_id: history5
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfofalx_medium.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T20:25:38.908374Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: ff5a3bed0867d9b32c7319fb613458a7827061a7a437d8c84ef2e6a324e9d620
- evidence_id: history6
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T20:25:38.908400Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: d12e282df34ce5493d8ed4f6f7fa69ae06565ecafdcdc637854d529abf97c840
- evidence_id: history7
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T20:25:38.908425Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: 623989d27923b2980a6e7710063a88efafe43a0307f7bd89402c0579c24815a8
- evidence_id: history8
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_16529.md
  locator: entire report; lossless historical reader; exact selected parent rows
  accessed_at: '2026-10-28T20:25:38.908450Z'
  support: supports
  summary: Complete report body read and losslessly retained. Zero-source-check diagnostics
    are historical structure only. Exact selected historical parent rows and current
    byte matches are separately joined; same-label unselected siblings and unrelated
    dependency parent recipes remain context-only. Old report conclusions are reassessed
    against the exact current source rather than automatically adopted; dates and
    historical execution are not authenticated.
  snapshot_sha256: 8ab7395954627f968dd68fb1f8fa38a2c78ae3ed4037742aaee2735079ffa731
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch077/record06/historical-authentication.json
  locator: attached_claims; historical_plan_claims
  accessed_at: '2026-10-28T20:25:38.908543Z'
  support: supports
  summary: Actual attached claims in scoped stock sections and historical parent-plan
    claims are separate populations. Current raw-digest equality and literal or normalized-HTML
    excerpt equality are independently recorded. No attached formulation claims occur
    on the selected target or its maintained contributors. Current byte matches do
    not authenticate historical execution or access dates.
  snapshot_sha256: 37951f46e307dc6ea183f2fe94a0a6763c8d479e87154afb34b6c31d78da73e1
- evidence_id: historical-current-joins
  kind: record_content
  reference: REVIEW_WORK/batch077/record06/historical-current-joins.json
  locator: all selected parents and claims
  accessed_at: '2026-10-28T20:25:38.908843Z'
  support: supports
  summary: Exact selected historical parent rows, source raw digest and all literal/decoded
    source-object joins. These are separate from absent attached formulation evidence
    and do not authenticate historical dates.
  snapshot_sha256: 0e317a135f83057f95cffda9bf558cc3f1e5d3043082809f4a5cf5faff5856f6
- evidence_id: writer58
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: target_slot; groundable; apply_to_record
  accessed_at: '2026-10-28T20:25:38.908943Z'
  support: context_only
  summary: Current target_slot preserves existing CHEBI assertions; groundable excludes
    conflicting corpus opinions, and apply_to_record fills ungrounded entries from
    proposals. This writer does not authenticate source amounts or automatically repair
    an existing wrong supplied-form ID.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: writer59
  kind: record_content
  reference: scripts/assign_culturemech_ids.py
  locator: assign_ids; _assign_id_to_file
  accessed_at: '2026-10-28T20:25:38.908974Z'
  support: context_only
  summary: Current assign_ids selects records with missing IDs; _assign_id_to_file
    checks new-ID collisions and appends identifier provenance. Identifier assignment
    does not authenticate recipe content or demonstrate historical source access.
  snapshot_sha256: 81ed213c52804ae98a8add02730d757595e3287fa7b01bc88aee0e587bbb01e1
- evidence_id: writer60
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T20:25:38.909003Z'
  support: context_only
  summary: Current _merge_ingredient_group collapses equal duplicate values without
    summing them and retains the first conflicting value with a flag. This behavior
    is distinct from historical summed-amount artifacts and does not authenticate
    source-specific stock or product structure.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer61
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: merge_duplicate_ingredients; merge_ingredient_group
  accessed_at: '2026-10-28T20:25:38.909031Z'
  support: context_only
  summary: Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group
    retains the first concentration, flags differing values and selects the first
    CHEBI. It cannot establish source stages or justify collapsing independent supplemental
    and product-contained components.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer62
  kind: record_content
  reference: scripts/migrate_legacy_mim_to_chebi.py
  locator: _resolve_chebi; _rewrite_entry
  accessed_at: '2026-10-28T20:25:38.909065Z'
  support: context_only
  summary: Current _resolve_chebi reuses current primary CHEBI where available and
    considers bounded exact-name/synonym matches with a stereo-prefix guard; _rewrite_entry
    retains unresolved links. Current-row presence is distinct from historical validity
    and from source-specific supplied-form equivalence.
  snapshot_sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
- evidence_id: writer63
  kind: record_content
  reference: scripts/migrate_ph_range.py
  locator: parse_ph_range; migrate_one
  accessed_at: '2026-10-28T20:25:38.909090Z'
  support: context_only
  summary: Current parse_ph_range retains qualifiers in notes and migrate_one converts
    only string-valued pH ranges, recording provenance. No particular source range
    is authenticated by this writer.
  snapshot_sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
- evidence_id: writer64
  kind: record_content
  reference: scripts/refill_term_labels.py
  locator: refill_text
  accessed_at: '2026-10-28T20:25:38.909122Z'
  support: context_only
  summary: Current refill_text replaces term labels using the current exact identifier
    lookup while preserving other text. Canonical label correspondence is not an independent
    choice of the correct chemical form for the supplied source reagent.
  snapshot_sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
- evidence_id: writer65
  kind: record_content
  reference: scripts/repair_komodo_866_desulfofalx_score10.py
  locator: _require_record; repair_parent; repair_child; _upsert_event; TIMESTAMP
  accessed_at: '2026-10-28T20:25:38.909149Z'
  support: context_only
  summary: Current _require_record checks exact IDs, source terms and a fixed 31-ingredient
    signature. repair_parent and repair_child set SOURCE_DUPLICATE for866 and STRAIN_SPECIFIC_VARIANT
    for866.1 and preserve existing quantities; they do not reconstruct the DSM16529
    substrate replacement. _upsert_event replaces an event with the same curator/action
    or appends it; TIMESTAMP is a hardcoded historical date. Current relationship
    repair is credited without authenticating original execution or strain-specific
    composition.
  snapshot_sha256: 126756b83c092c41786d0381fdb2d6d3bd609f4d85df14ecaadbd1f72a196319
- evidence_id: writer66
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata
  accessed_at: '2026-10-28T20:25:38.909188Z'
  support: context_only
  summary: Current DSMZCompositionResolver.merge_composition copies ingredients and
    solutions, fills pH when absent and copies physical/medium type, but does not
    copy preparation steps. _add_enrichment_metadata records a naive current timestamp.
    This explains a present omission risk, not historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer67
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T20:25:38.909220Z'
  support: context_only
  summary: Current _convert_to_culturemech constructs source notes and default LIQUID
    with empty ingredients. Its time.strftime format contains %f, which is unsupported
    here and is consistent with literal .fZ in stored import events. Current code
    does not authenticate the original retrieval or justify rewriting historical time.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer68
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps
  accessed_at: '2026-10-28T20:25:38.909256Z'
  support: context_only
  summary: Current _parse_api_composition considers the primary recipe, prefers provider
    g_l when available and excludes four recognized water labels; tap water is not
    among those exclusions; _is_api_stock_addition distinguishes stock additions.
    _parse_api_solutions retains separate stock structure. _parse_preparation_steps
    collects solution prose. These present behaviors do not establish historical execution
    and cannot justify interpreting flattened stock rates as final-medium concentrations.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer69
  kind: record_content
  reference: src/culturemech/match/kg_media_matcher.py
  locator: extract_recipe_ingredients; find_matches; find_exact_match
  accessed_at: '2026-10-28T20:25:38.909290Z'
  support: context_only
  summary: Current extract_recipe_ingredients collects asserted CHEBI/FOODON IDs,
    find_matches compares set Jaccard and find_exact_match selects the first exact
    identifier set. Quantities, preparation and ungrounded ingredients are not compared,
    so an exact set match does not establish formulation identity.
  snapshot_sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
- evidence_id: writer70
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T20:25:38.909316Z'
  support: context_only
  summary: Current formulation_content retains exact scientific quantities, preparation
    and other scientific fields; merge_formulation_evidence rejects incompatible projections
    and unions evidence at matching scopes. A source-equivalence claim is not established
    by shared ingredient identities.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer71
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations; group_recipes
  accessed_at: '2026-10-28T20:25:38.909343Z'
  support: context_only
  summary: Current group_formulations calls group_recipes with fail_on_invalid=True
    and FormulationFingerprinter. Expected standalone or unfingerprintable records
    are excluded; malformed or unexpected inputs raise. Valid records are grouped
    by full scientific content. This guard does not retrieve or authenticate source
    recipes.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer72
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T20:25:38.909370Z'
  support: context_only
  summary: Current merge_group routes a single maintained owner with merge metadata;
    multiple owners pass through conservative merge_formulation_evidence. Regenerating
    from an unrepaired owner retains its defects. Current conservative behavior is
    credited and does not establish how the old generated record was produced.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer73
  kind: record_content
  reference: src/culturemech/validation/schema_defaulter.py
  locator: apply_defaults; _fix_ingredient; _fix_solution
  accessed_at: '2026-10-28T20:25:38.909402Z'
  support: context_only
  summary: Current apply_defaults, _fix_ingredient and _fix_solution can insert VARIABLE
    amounts and placeholder names for structural completeness. A default is not evidence
    for a dose, composition, solution identity or denominator; existing default-history
    events remain contextual.
  snapshot_sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch077/record06/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T20:48:00.905151Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: 1f2fad228a28c82b4ac6cb70196ea2e9749b1774872ed41dfc4a61252c310ef3
assessments:
- assessment_id: a1
  area: identity
  topic: Distinct source and strain formulations
  outcome: concern
  summary: The generated record carries813a identity/pH/procedure but866 ingredient
    amounts. The maintained813a and866 owners are different recipes. Current relationship
    repair correctly distinguishes866 source duplicate from866.1 strain variant, but
    does not implement the primaryDSM16529 substrate replacement. Fresh catalogue
    identifies environmental Desulfohalovibrio alkalitolerans DSM16529 with riskgroup1
    and modified866; no pathogen-specific scope or new growth assertion is inferred.
  target_ids:
  - CultureMech:001959
  evidence_ids:
  - dsm813a
  - dsm866
  - dsm16529Identity
  - local0
- assessment_id: a2
  area: consistency
  topic: Classification and current merger
  outcome: supported
  summary: LIQUID and yeast-containing complex/undefined classification are compatible
    with both source families. Current full-formulation merge logic rejects incompatible
    scientific projections and preserves preparation/evidence at matching scopes.
    This current guard is credited; the old merged record still combines different
    formulations.
  target_ids:
  - CultureMech:001959
  evidence_ids:
  - dsm813a
  - dsm866
  - writer69
  - writer70
  - writer71
  - writer72
- assessment_id: a3
  area: grounding
  topic: Supplied forms and source specificity
  outcome: concern
  summary: All five layers assert nickel dichloride34887 in primary and secondary
    slots for nickel chloride hexahydrate, and neutral resazurin8806 in the primary
    slot for sodium resazurin. Correct cobalt53503 and other hydrates remain credited.
    MIM spelling-specific REJECTED CoCl2 x6H2O is distinct from MAPPED Cobalt chloride
    hexahydrate for the same correct ID. B12 is a class; generic lipoic acid does
    not certify an enantiomer. The newDSM16529 L-lactate must not be assigned a generic
    stereochemical term without verification.
  target_ids:
  - CultureMech:001959
  evidence_ids:
  - grounding
  - chebi34887
  - chebi8806
  - chebi53503
- assessment_id: a4
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: Nine full reports and four exact parent-plan rows were read. All152 historical
    source objects match current raw/decoded API objects, and both cited API digests
    match present bytes; the280 planclaims include128 separate local unresolved rows.
    No attached formulation evidence exists. Earlier broad all-conflict/pH rules are
    reassessed per layer; current source equality does not authenticate old runs or
    dates. Stored KOMODO timestamps contain literal2026-01-27T01:15:03.fZ and resolver
    events lack offsets; current timestamp writers retain corresponding risks. Current
    fixed-signature866 relationship repair does not establish the missing strain recipe.
    Current conservative merging preserves scientific fields and rejects incompatible
    formulations. Inspected writer behavior is described separately by exact file
    and function; it does not prove historical execution.
  target_ids:
  - CultureMech:001959
  evidence_ids:
  - history-auth
  - historical-current-joins
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
  - writer70
  - writer71
  - writer72
  - writer73
- assessment_id: a5
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 155 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:001959
  evidence_ids:
  - quantity-inventory
  details: '{"schema":"private explicit quantity decisions v1","target_id":"CultureMech:001959","selected_concentration_field_count":155,"selected_concentration_fields_covered":155,"decisions":[{"decision_id":"q1","subject":"KH2PO4
    generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[0].concentration","original":{"value":"0.199601","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass0.2g /1.002L = 0.1996007984031936127744510978g/L.
    The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text
    physical LF lines 7-7","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   KH2PO4                                                     0.20         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[0]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\":
    1.46674,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q2","subject":"KH2PO4 maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[0].concentration","original":{"value":"0.199601","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass0.2g /1.002L = 0.1996007984031936127744510978g/L.
    The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text
    physical LF lines 7-7","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   KH2PO4                                                     0.20         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[0]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\":
    1.46674,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q3","subject":"MgCl2 x 6 H2O generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[1].concentration","original":{"value":"0.0998004","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass0.1g /1.002L = 0.09980039920159680638722554890g/L.
    The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text
    physical LF lines 8-8","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   MgCl2
    x 6 H2O                                              0.10         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[1]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0998004,\n                        \"mmol_l\":
    0.490895,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q4","subject":"MgCl2 x 6 H2O maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[1].concentration","original":{"value":"0.0998004","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass0.1g /1.002L = 0.09980039920159680638722554890g/L.
    The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text
    physical LF lines 8-8","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   MgCl2
    x 6 H2O                                              0.10         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[1]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0998004,\n                        \"mmol_l\":
    0.490895,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q5","subject":"KCl generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[2].concentration","original":{"value":"0.199601","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass0.2g /1.002L = 0.1996007984031936127744510978g/L.
    The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text
    physical LF lines 10-10","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   KCl                                                        0.20         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[3]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\":
    2.67741,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q6","subject":"KCl maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[3].concentration","original":{"value":"0.199601","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass0.2g /1.002L = 0.1996007984031936127744510978g/L.
    The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text
    physical LF lines 10-10","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   KCl                                                        0.20         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[3]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\":
    2.67741,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q7","subject":"NH4Cl generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[3].concentration","original":{"value":"0.998004","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass1g /1.002L = 0.9980039920159680638722554890g/L. The
    existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text
    physical LF lines 9-9","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   NH4Cl                                                      1.00         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[2]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.998004,\n                        \"mmol_l\":
    18.6578,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q8","subject":"NH4Cl maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[2].concentration","original":{"value":"0.998004","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass1g /1.002L = 0.9980039920159680638722554890g/L. The
    existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text
    physical LF lines 9-9","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   NH4Cl                                                      1.00         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[2]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.998004,\n                        \"mmol_l\":
    18.6578,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q9","subject":"Na2SO4 generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[4].concentration","original":{"value":"4.99002","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass3g /1.002L = 2.994011976047904191616766467g/L. Existing
    value conflicts with this exact source basis; correct only the813a layer. Current
    API813a is internally inconsistent: sulfate3g hasg_l4.99002, carbonate3g hasg_l3.49301,
    and bicarbonate24g lacksg_l. Do not promote those fields over the primary denominator.","sources":[{"locator":"extracted-text
    physical LF lines 11-11","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Na2SO4                                                     3.00         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[4]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4.99002,\n                        \"mmol_l\":
    35.1311,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q10","subject":"Na2SO4 maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[4].concentration","original":{"value":"4.99002","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass3g /1.002L = 2.994011976047904191616766467g/L. Existing
    value conflicts with this exact source basis; correct only the813a layer. Current
    API813a is internally inconsistent: sulfate3g hasg_l4.99002, carbonate3g hasg_l3.49301,
    and bicarbonate24g lacksg_l. Do not promote those fields over the primary denominator.","sources":[{"locator":"extracted-text
    physical LF lines 11-11","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Na2SO4                                                     3.00         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[4]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4.99002,\n                        \"mmol_l\":
    35.1311,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q11","subject":"NaCl generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[5].concentration","original":{"value":"4.99002","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass30g /1.002L = 29.94011976047904191616766467g/L. Existing
    value conflicts with this exact source basis; correct only the813a layer.","sources":[{"locator":"extracted-text
    physical LF lines 12-12","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   NaCl                                                      30.00         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[5]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 30,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 29.9401,\n                        \"mmol_l\":
    512.322,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q12","subject":"NaCl maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[5].concentration","original":{"value":"29.9401","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass30g /1.002L = 29.94011976047904191616766467g/L. The
    existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text
    physical LF lines 12-12","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   NaCl                                                      30.00         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[5]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 30,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 29.9401,\n                        \"mmol_l\":
    512.322,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q13","subject":"Yeast extract generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[6].concentration","original":{"value":"1.49701","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass1g /1.002L = 0.9980039920159680638722554890g/L. Existing
    value conflicts with this exact source basis; correct only the813a layer.","sources":[{"locator":"extracted-text
    physical LF lines 14-14","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Yeast
    extract                                              1.00         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[7]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.998004,\n                        \"optional\":
    0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q14","subject":"Yeast
    extract maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[6].concentration","original":{"value":"0.998004","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass1g /1.002L = 0.9980039920159680638722554890g/L. The
    existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text
    physical LF lines 14-14","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Yeast
    extract                                              1.00         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[7]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.998004,\n                        \"optional\":
    0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q15","subject":"Sodium
    resazurin generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[7].concentration","original":{"value":"0.000499002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass0.0005g /1.002L = 0.0004990019960079840319361277445g/L.
    The existing value agrees at its recorded precision; retain it and add exact evidence.
    Source0.5ml of0.1%w/v resazurin contributes0.0005g; the explicit w/v basis permits
    this calculation.","sources":[{"locator":"extracted-text physical LF lines 15-15","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Sodium
    resazurin (0.1% w/v)                                0.50        ml","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[8]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000499002,\n                        \"mmol_l\": 0.00198671,\n                        \"optional\":
    0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q16","subject":"Sodium
    resazurin maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[7].concentration","original":{"value":"0.000499002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass0.0005g /1.002L = 0.0004990019960079840319361277445g/L.
    The existing value agrees at its recorded precision; retain it and add exact evidence.
    Source0.5ml of0.1%w/v resazurin contributes0.0005g; the explicit w/v basis permits
    this calculation.","sources":[{"locator":"extracted-text physical LF lines 15-15","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Sodium
    resazurin (0.1% w/v)                                0.50        ml","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[8]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000499002,\n                        \"mmol_l\": 0.00198671,\n                        \"optional\":
    0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q17","subject":"Na2CO3
    generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[8].concentration","original":{"value":"0.499002","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass3g /1.002L = 2.994011976047904191616766467g/L. Existing
    value conflicts with this exact source basis; correct only the813a layer. Current
    API813a is internally inconsistent: sulfate3g hasg_l4.99002, carbonate3g hasg_l3.49301,
    and bicarbonate24g lacksg_l. Do not promote those fields over the primary denominator.","sources":[{"locator":"extracted-text
    physical LF lines 16-16","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Na2CO3                                                     3.00         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[9]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.49301,\n                        \"mmol_l\":
    32.9567,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q18","subject":"Na2CO3 maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[8].concentration","original":{"value":"3.49301","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass3g /1.002L = 2.994011976047904191616766467g/L. Existing
    value conflicts with this exact source basis; correct only the813a layer. Current
    API813a is internally inconsistent: sulfate3g hasg_l4.99002, carbonate3g hasg_l3.49301,
    and bicarbonate24g lacksg_l. Do not promote those fields over the primary denominator.","sources":[{"locator":"extracted-text
    physical LF lines 16-16","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Na2CO3                                                     3.00         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[9]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.49301,\n                        \"mmol_l\":
    32.9567,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q19","subject":"NaHCO3 generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[9].concentration","original":{"value":"7.98403","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass24g /1.002L = 23.95209580838323353293413174g/L. Existing
    value conflicts with this exact source basis; correct only the813a layer. Current
    API813a is internally inconsistent: sulfate3g hasg_l4.99002, carbonate3g hasg_l3.49301,
    and bicarbonate24g lacksg_l. Do not promote those fields over the primary denominator.","sources":[{"locator":"extracted-text
    physical LF lines 17-17","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   NaHCO3                                                    24.00         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[10]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"amount\": 24,\n                        \"unit\":
    \"g\",\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q20","subject":"NaHCO3 maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[9].concentration","original":{"value":"24","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass24g /1.002L = 23.95209580838323353293413174g/L. Existing
    value conflicts with this exact source basis; correct only the813a layer. Current
    API813a is internally inconsistent: sulfate3g hasg_l4.99002, carbonate3g hasg_l3.49301,
    and bicarbonate24g lacksg_l. Do not promote those fields over the primary denominator.","sources":[{"locator":"extracted-text
    physical LF lines 17-17","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   NaHCO3                                                    24.00         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[10]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"amount\": 24,\n                        \"unit\":
    \"g\",\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q21","subject":"Na-formate generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[10].concentration","original":{"value":"4.99002","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass4g /1.002L = 3.992015968063872255489021956g/L. Existing
    value conflicts with this exact source basis; correct only the813a layer.","sources":[{"locator":"extracted-text
    physical LF lines 19-19","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Na-formate                                                 4.00         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[12]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Na-formate\",\n                        \"compound_id\":
    144,\n                        \"amount\": 4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.99202,\n                        \"mmol_l\":
    58.6999,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q22","subject":"Na-formate maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[11].concentration","original":{"value":"3.99202","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass4g /1.002L = 3.992015968063872255489021956g/L. The
    existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text
    physical LF lines 19-19","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Na-formate                                                 4.00         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[12]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Na-formate\",\n                        \"compound_id\":
    144,\n                        \"amount\": 4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.99202,\n                        \"mmol_l\":
    58.6999,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q23","subject":"Na2S x 9 H2O generated813a","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[11].concentration","original":{"value":"0.499002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass0.5g /1.002L = 0.4990019960079840319361277445g/L.
    The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text
    physical LF lines 18-18","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Na2S
    x 9 H2O                                               0.50         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[11]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\":
    2.0776,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q24","subject":"Na2S x 9 H2O maintained813a","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[10].concentration","original":{"value":"0.499002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM813a
    main medium","interpretation":"The primary DSM813a explicitly declares1002ml final
    volume. Its source batch mass0.5g /1.002L = 0.4990019960079840319361277445g/L.
    The existing value agrees at its recorded precision; retain it and add exact evidence.","sources":[{"locator":"extracted-text
    physical LF lines 18-18","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Na2S
    x 9 H2O                                               0.50         g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].recipe[11]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\":
    2.0776,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q25","subject":"KH2PO4 DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[0].concentration","original":{"value":"0.199601","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[0].concentration","original":{"value":"0.199601","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[0].concentration","original":{"value":"0.199601","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866
    provider main basis","interpretation":"Current DSM866 primary supports the quoted
    basal batch amount and API866 explicitly reports this nominal main g_l. Credit
    that provider basis without asserting independently measured final volume. The
    KOMODO routes are403, so no historical or unobserved source version is certified.
    The current strain-specific substitution is assessed separately; unrelated813a
    amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines
    3-3","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   KH2PO4                                                     0.20         g","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[0].recipe[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\":
    1.46674,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q26","subject":"MgCl2 x 6 H2O DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[1].concentration","original":{"value":"0.0998004","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[1].concentration","original":{"value":"0.0998004","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[1].concentration","original":{"value":"0.0998004","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866
    provider main basis","interpretation":"Current DSM866 primary supports the quoted
    basal batch amount and API866 explicitly reports this nominal main g_l. Credit
    that provider basis without asserting independently measured final volume. The
    KOMODO routes are403, so no historical or unobserved source version is certified.
    The current strain-specific substitution is assessed separately; unrelated813a
    amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines
    4-4","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   MgCl2
    x 6 H2O                                              0.10         g","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[0].recipe[1]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0998004,\n                        \"mmol_l\":
    0.490895,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q27","subject":"KCl DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[2].concentration","original":{"value":"0.199601","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[2].concentration","original":{"value":"0.199601","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[2].concentration","original":{"value":"0.199601","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866
    provider main basis","interpretation":"Current DSM866 primary supports the quoted
    basal batch amount and API866 explicitly reports this nominal main g_l. Credit
    that provider basis without asserting independently measured final volume. The
    KOMODO routes are403, so no historical or unobserved source version is certified.
    The current strain-specific substitution is assessed separately; unrelated813a
    amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines
    5-5","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   KCl                                                        0.20         g","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[0].recipe[2]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\":
    2.67741,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q28","subject":"NH4Cl DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[3].concentration","original":{"value":"0.998004","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[3].concentration","original":{"value":"0.998004","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[3].concentration","original":{"value":"0.998004","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866
    provider main basis","interpretation":"Current DSM866 primary supports the quoted
    basal batch amount and API866 explicitly reports this nominal main g_l. Credit
    that provider basis without asserting independently measured final volume. The
    KOMODO routes are403, so no historical or unobserved source version is certified.
    The current strain-specific substitution is assessed separately; unrelated813a
    amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines
    6-6","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   NH4Cl                                                      1.00         g","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[0].recipe[3]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.998004,\n                        \"mmol_l\":
    18.6578,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q29","subject":"Na2SO4 DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[4].concentration","original":{"value":"4.99002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[4].concentration","original":{"value":"4.99002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[4].concentration","original":{"value":"4.99002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866
    provider main basis","interpretation":"Current DSM866 primary supports the quoted
    basal batch amount and API866 explicitly reports this nominal main g_l. Credit
    that provider basis without asserting independently measured final volume. The
    KOMODO routes are403, so no historical or unobserved source version is certified.
    The current strain-specific substitution is assessed separately; unrelated813a
    amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines
    7-7","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Na2SO4                                                     5.00         g","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[0].recipe[4]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4.99002,\n                        \"mmol_l\":
    35.1311,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q30","subject":"NaCl DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[5].concentration","original":{"value":"4.99002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[5].concentration","original":{"value":"4.99002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[5].concentration","original":{"value":"4.99002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866
    provider main basis","interpretation":"Current DSM866 primary supports the quoted
    basal batch amount and API866 explicitly reports this nominal main g_l. Credit
    that provider basis without asserting independently measured final volume. The
    KOMODO routes are403, so no historical or unobserved source version is certified.
    The current strain-specific substitution is assessed separately; unrelated813a
    amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines
    8-8","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   NaCl                                                       5.00         g","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[0].recipe[5]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4.99002,\n                        \"mmol_l\":
    85.3871,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q31","subject":"Yeast extract DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[6].concentration","original":{"value":"1.49701","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[6].concentration","original":{"value":"1.49701","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[6].concentration","original":{"value":"1.49701","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866
    provider main basis","interpretation":"Current DSM866 primary supports the quoted
    basal batch amount and API866 explicitly reports this nominal main g_l. Credit
    that provider basis without asserting independently measured final volume. The
    KOMODO routes are403, so no historical or unobserved source version is certified.
    The current strain-specific substitution is assessed separately; unrelated813a
    amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines
    10-10","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Yeast
    extract                                              1.50         g","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[0].recipe[7]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.49701,\n                        \"optional\":
    0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q32","subject":"Sodium
    resazurin DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[7].concentration","original":{"value":"0.000499002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[7].concentration","original":{"value":"0.000499002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[7].concentration","original":{"value":"0.000499002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866
    provider main basis","interpretation":"Current DSM866 primary supports the quoted
    basal batch amount and API866 explicitly reports this nominal main g_l. Credit
    that provider basis without asserting independently measured final volume. The
    KOMODO routes are403, so no historical or unobserved source version is certified.
    The current strain-specific substitution is assessed separately; unrelated813a
    amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines
    11-11","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Sodium
    resazurin (0.1% w/v)                                0.50        ml","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[0].recipe[8]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000499002,\n                        \"mmol_l\": 0.00198671,\n                        \"optional\":
    0\n                    }","quote_representation":"raw JSON object"}]},{"decision_id":"q33","subject":"Na2CO3
    DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[8].concentration","original":{"value":"0.499002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[8].concentration","original":{"value":"0.499002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[8].concentration","original":{"value":"0.499002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866
    provider main basis","interpretation":"Current DSM866 primary supports the quoted
    basal batch amount and API866 explicitly reports this nominal main g_l. Credit
    that provider basis without asserting independently measured final volume. The
    KOMODO routes are403, so no historical or unobserved source version is certified.
    The current strain-specific substitution is assessed separately; unrelated813a
    amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines
    12-12","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Na2CO3                                                     0.50         g","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[0].recipe[9]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\":
    4.7081,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q34","subject":"NaHCO3 DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[9].concentration","original":{"value":"7.98403","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[9].concentration","original":{"value":"7.98403","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[9].concentration","original":{"value":"7.98403","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866
    provider main basis","interpretation":"Current DSM866 primary supports the quoted
    basal batch amount and API866 explicitly reports this nominal main g_l. Credit
    that provider basis without asserting independently measured final volume. The
    KOMODO routes are403, so no historical or unobserved source version is certified.
    The current strain-specific substitution is assessed separately; unrelated813a
    amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines
    13-13","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   NaHCO3                                                     8.00         g","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[0].recipe[10]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"amount\": 8,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 7.98403,\n                        \"mmol_l\":
    95.0401,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q35","subject":"Na-formate DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[10].concentration","original":{"value":"4.99002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[10].concentration","original":{"value":"4.99002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866
    provider main basis","interpretation":"Current DSM866 primary supports the quoted
    basal batch amount and API866 explicitly reports this nominal main g_l. Credit
    that provider basis without asserting independently measured final volume. The
    KOMODO routes are403, so no historical or unobserved source version is certified.
    The current strain-specific substitution is assessed separately; unrelated813a
    amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines
    14-14","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Na-formate                                                 5.00         g","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[0].recipe[11]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na-formate\",\n                        \"compound_id\":
    144,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4.99002,\n                        \"mmol_l\":
    73.3749,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q36","subject":"Na2S x 9 H2O DSM866 family","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[11].concentration","original":{"value":"0.499002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[11].concentration","original":{"value":"0.499002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[11].concentration","original":{"value":"0.499002","unit":"G_PER_L"}}],"decision":"evidence_only","stage":"DSM866
    provider main basis","interpretation":"Current DSM866 primary supports the quoted
    basal batch amount and API866 explicitly reports this nominal main g_l. Credit
    that provider basis without asserting independently measured final volume. The
    KOMODO routes are403, so no historical or unobserved source version is certified.
    The current strain-specific substitution is assessed separately; unrelated813a
    amounts do not transfer.","sources":[{"locator":"extracted-text physical LF lines
    16-16","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Na2S
    x 9 H2O                                               0.50         g","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[0].recipe[13]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\":
    2.0776,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q37","subject":"DSM16529 substrate replacement","local_fields":[{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[10].concentration","original":{"value":"4.99002","unit":"G_PER_L"}}],"decision":"correct","stage":"DSM16529-specific
    variant","interpretation":"Current primary DSM866 explicitly replaces sodium formate
    with2.5g/L sodium L-lactate forDSM16529. The wrapper retains basal formate and
    lacks lactate. The catalogue confirms current identity and modified medium866
    association; it does not justify changing the generic866 or813a recipes.","sources":[{"locator":"extracted-text
    physical LF lines 27-27","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"For
    DSM 16529: Replace Na-formate with 2.5 g/l Na-L-lactate as substrate.","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 199-199","source_key":"dsm16529Identity","reference":"https://www.dsmz.de/collection/catalogue/details/culture/DSM-16529","source_raw_sha256":"08e4dba4a2f52396cd2d62b1ca21e72e766eb347dc8c6f08b303d1703fb51d72","source_text_sha256":"1effe70237ed96eeaec6534cb56c2cbdb98da370246d87ca3e01a94b339a6807","accessed_at":"2026-10-28T20:14:20.082451Z","exact_source_quote":"Medium
    866 with strain-specific modifications","quote_representation":"captured extracted
    text"},{"locator":"extracted-text physical LF lines 208-208","source_key":"dsm16529Identity","reference":"https://www.dsmz.de/collection/catalogue/details/culture/DSM-16529","source_raw_sha256":"08e4dba4a2f52396cd2d62b1ca21e72e766eb347dc8c6f08b303d1703fb51d72","source_text_sha256":"1effe70237ed96eeaec6534cb56c2cbdb98da370246d87ca3e01a94b339a6807","accessed_at":"2026-10-28T20:14:20.082451Z","exact_source_quote":"Taxonomy/description
    (10394, 32582, 33859). Sequence accession no. 16S rRNA gene: AY649785, draft genome:
    ATHI01000000. (Medium 866 with strain-specific modifications, 40°C, anaerobic).","quote_representation":"captured
    extracted text"}]},{"decision_id":"q38","subject":"HCl SL10","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[12].concentration","original":{"value":"2.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[12].concentration","original":{"value":"2.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[12].concentration","original":{"value":"2.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[12].concentration","original":{"value":"2.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[12].concentration","original":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","stage":"SL10
    stock","interpretation":"The source specifies10ml of25% HCl reagent, with no percent
    basis. Provider2.5g/L does not establish that mass concentration; restore the
    volume and retain the bare strength label without density inference. Keep the
    separate1ml receiving dose and stock preparation.","sources":[{"locator":"extracted-text
    physical LF lines 33-33","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   HCl
    (25%)                                                  10.00      ml","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[0]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }","quote_representation":"raw JSON object"},{"locator":"extracted-text
    physical LF lines 33-33","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   HCl
    (25%)                                                  10.00      ml","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q39","subject":"FeCl2 x 4 H2O SL10","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[13].concentration","original":{"value":"1.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[13].concentration","original":{"value":"1.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[13].concentration","original":{"value":"1.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[13].concentration","original":{"value":"1.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[13].concentration","original":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","stage":"SL10
    stock","interpretation":"Both primary SL10 tables explicitly make up to1000ml,
    so the quoted stock batch mass supports its stock g/L. The existing root placement
    is wrong: retain the valid stock strength insideSL10, not as main-medium concentration.
    Keep the separate1ml receiving dose and stock preparation.","sources":[{"locator":"extracted-text
    physical LF lines 34-34","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   FeCl2
    x 4 H2O                                               1.50       g","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[1]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text physical LF lines 34-34","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   FeCl2
    x 4 H2O                                               1.50       g","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q40","subject":"ZnCl2 SL10","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[14].concentration","original":{"value":"0.07","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[14].concentration","original":{"value":"0.07","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[14].concentration","original":{"value":"0.07","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[14].concentration","original":{"value":"0.07","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[14].concentration","original":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","stage":"SL10
    stock","interpretation":"Both primary SL10 tables explicitly make up to1000ml,
    so the quoted stock batch mass supports its stock g/L. The existing root placement
    is wrong: retain the valid stock strength insideSL10, not as main-medium concentration.
    Keep the separate1ml receiving dose and stock preparation.","sources":[{"locator":"extracted-text
    physical LF lines 35-35","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   ZnCl2                                                      70.00      mg","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[2]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text physical LF lines 35-35","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   ZnCl2                                                      70.00      mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q41","subject":"MnCl2 x 4 H2O SL10","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[15].concentration","original":{"value":"0.1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[15].concentration","original":{"value":"0.1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[15].concentration","original":{"value":"0.1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[15].concentration","original":{"value":"0.1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[15].concentration","original":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","stage":"SL10
    stock","interpretation":"Both primary SL10 tables explicitly make up to1000ml,
    so the quoted stock batch mass supports its stock g/L. The existing root placement
    is wrong: retain the valid stock strength insideSL10, not as main-medium concentration.
    Keep the separate1ml receiving dose and stock preparation.","sources":[{"locator":"extracted-text
    physical LF lines 36-36","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   MnCl2
    x 4 H2O                                             100.00      mg","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[3]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text physical LF lines 36-36","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   MnCl2
    x 4 H2O                                             100.00      mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q42","subject":"H3BO3 SL10","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[16].concentration","original":{"value":"0.006","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[16].concentration","original":{"value":"0.006","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[16].concentration","original":{"value":"0.006","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[16].concentration","original":{"value":"0.006","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[16].concentration","original":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","stage":"SL10
    stock","interpretation":"Both primary SL10 tables explicitly make up to1000ml,
    so the quoted stock batch mass supports its stock g/L. The existing root placement
    is wrong: retain the valid stock strength insideSL10, not as main-medium concentration.
    Keep the separate1ml receiving dose and stock preparation.","sources":[{"locator":"extracted-text
    physical LF lines 37-37","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   H3BO3                                                       6.00      mg","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[4]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text physical LF lines 37-37","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   H3BO3                                                       6.00      mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q43","subject":"CoCl2 x 6 H2O SL10","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[17].concentration","original":{"value":"0.19","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[17].concentration","original":{"value":"0.19","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[17].concentration","original":{"value":"0.19","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[17].concentration","original":{"value":"0.19","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[17].concentration","original":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","stage":"SL10
    stock","interpretation":"Both primary SL10 tables explicitly make up to1000ml,
    so the quoted stock batch mass supports its stock g/L. The existing root placement
    is wrong: retain the valid stock strength insideSL10, not as main-medium concentration.
    Keep the separate1ml receiving dose and stock preparation.","sources":[{"locator":"extracted-text
    physical LF lines 38-38","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   CoCl2
    x 6 H2O                                             190.00      mg","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[5]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text physical LF lines 38-38","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   CoCl2
    x 6 H2O                                             190.00      mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q44","subject":"CuCl2 x 2 H2O SL10","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[18].concentration","original":{"value":"0.002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[18].concentration","original":{"value":"0.002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[18].concentration","original":{"value":"0.002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[18].concentration","original":{"value":"0.002","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[18].concentration","original":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","stage":"SL10
    stock","interpretation":"Both primary SL10 tables explicitly make up to1000ml,
    so the quoted stock batch mass supports its stock g/L. The existing root placement
    is wrong: retain the valid stock strength insideSL10, not as main-medium concentration.
    Keep the separate1ml receiving dose and stock preparation.","sources":[{"locator":"extracted-text
    physical LF lines 39-39","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   CuCl2
    x 2 H2O                                               2.00      mg","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[6]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text physical LF lines 39-39","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   CuCl2
    x 2 H2O                                               2.00      mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q45","subject":"NiCl2 x 6 H2O SL10","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[19].concentration","original":{"value":"0.024","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[19].concentration","original":{"value":"0.024","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[19].concentration","original":{"value":"0.024","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[19].concentration","original":{"value":"0.024","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[19].concentration","original":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","stage":"SL10
    stock","interpretation":"Both primary SL10 tables explicitly make up to1000ml,
    so the quoted stock batch mass supports its stock g/L. The existing root placement
    is wrong: retain the valid stock strength insideSL10, not as main-medium concentration.
    Keep the separate1ml receiving dose and stock preparation.","sources":[{"locator":"extracted-text
    physical LF lines 40-40","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   NiCl2
    x 6 H2O                                              24.00      mg","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[7]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text physical LF lines 40-40","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   NiCl2
    x 6 H2O                                              24.00      mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q46","subject":"Na2MoO4 x 2 H2O SL10","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[20].concentration","original":{"value":"0.036","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[20].concentration","original":{"value":"0.036","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[20].concentration","original":{"value":"0.036","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[20].concentration","original":{"value":"0.036","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[20].concentration","original":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","stage":"SL10
    stock","interpretation":"Both primary SL10 tables explicitly make up to1000ml,
    so the quoted stock batch mass supports its stock g/L. The existing root placement
    is wrong: retain the valid stock strength insideSL10, not as main-medium concentration.
    Keep the separate1ml receiving dose and stock preparation.","sources":[{"locator":"extracted-text
    physical LF lines 41-41","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Na2MoO4
    x 2 H2O                                            36.00      mg","quote_representation":"captured
    extracted text"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].recipe[8]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text physical LF lines 41-41","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Na2MoO4
    x 2 H2O                                            36.00      mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q47","subject":"Biotin Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[21].concentration","original":{"value":"0.02","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[21].concentration","original":{"value":"0.02","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[21].concentration","original":{"value":"0.02","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[21].concentration","original":{"value":"0.02","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[21].concentration","original":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x
    stock","interpretation":"The exact primary table supports this separate vitamin-stock
    batch amount and current APIs explicitly declare the stored g_l on that stock
    basis. It is not a main-medium concentration. Restore the ten-component stock
    and1ml addition; listed1000ml water does not independently establish a measured
    final stock volume.","sources":[{"locator":"extracted-text physical LF lines 57-57","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Biotin                                     20.00   mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[2].recipe[0]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text physical LF lines 57-57","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Biotin                                     20.00   mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[2].recipe[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q48","subject":"Folic acid Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[22].concentration","original":{"value":"0.02","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[22].concentration","original":{"value":"0.02","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[22].concentration","original":{"value":"0.02","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[22].concentration","original":{"value":"0.02","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[22].concentration","original":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x
    stock","interpretation":"The exact primary table supports this separate vitamin-stock
    batch amount and current APIs explicitly declare the stored g_l on that stock
    basis. It is not a main-medium concentration. Restore the ten-component stock
    and1ml addition; listed1000ml water does not independently establish a measured
    final stock volume.","sources":[{"locator":"extracted-text physical LF lines 58-58","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Folic
    acid                                 20.00   mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[2].recipe[1]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text physical LF lines 58-58","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Folic
    acid                                 20.00   mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[2].recipe[1]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q49","subject":"Pyridoxine hydrochloride Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[23].concentration","original":{"value":"0.1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[23].concentration","original":{"value":"0.1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[23].concentration","original":{"value":"0.1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[23].concentration","original":{"value":"0.1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[23].concentration","original":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x
    stock","interpretation":"The exact primary table supports this separate vitamin-stock
    batch amount and current APIs explicitly declare the stored g_l on that stock
    basis. It is not a main-medium concentration. Restore the ten-component stock
    and1ml addition; listed1000ml water does not independently establish a measured
    final stock volume.","sources":[{"locator":"extracted-text physical LF lines 59-59","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Pyridoxine
    hydrochloride                  100.00   mg","quote_representation":"captured extracted
    text"},{"locator":"$.data.solutions[2].recipe[2]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text physical LF lines 59-59","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Pyridoxine
    hydrochloride                  100.00   mg","quote_representation":"captured extracted
    text"},{"locator":"$.data.solutions[2].recipe[2]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q50","subject":"Thiamine HCl Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[24].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[24].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[24].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[24].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[24].concentration","original":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x
    stock","interpretation":"The exact primary table supports this separate vitamin-stock
    batch amount and current APIs explicitly declare the stored g_l on that stock
    basis. It is not a main-medium concentration. Restore the ten-component stock
    and1ml addition; listed1000ml water does not independently establish a measured
    final stock volume.","sources":[{"locator":"extracted-text physical LF lines 60-60","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Thiamine
    HCl                               50.00   mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[2].recipe[3]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text physical LF lines 60-60","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Thiamine
    HCl                               50.00   mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[2].recipe[3]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q51","subject":"Riboflavin Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[25].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[25].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[25].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[25].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[25].concentration","original":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x
    stock","interpretation":"The exact primary table supports this separate vitamin-stock
    batch amount and current APIs explicitly declare the stored g_l on that stock
    basis. It is not a main-medium concentration. Restore the ten-component stock
    and1ml addition; listed1000ml water does not independently establish a measured
    final stock volume.","sources":[{"locator":"extracted-text physical LF lines 61-61","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Riboflavin                                 50.00   mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[2].recipe[4]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text physical LF lines 61-61","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Riboflavin                                 50.00   mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[2].recipe[4]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q52","subject":"Nicotinic acid Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[26].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[26].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[26].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[26].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[26].concentration","original":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x
    stock","interpretation":"The exact primary table supports this separate vitamin-stock
    batch amount and current APIs explicitly declare the stored g_l on that stock
    basis. It is not a main-medium concentration. Restore the ten-component stock
    and1ml addition; listed1000ml water does not independently establish a measured
    final stock volume.","sources":[{"locator":"extracted-text physical LF lines 62-62","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Nicotinic
    acid                             50.00   mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[2].recipe[5]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text physical LF lines 62-62","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Nicotinic
    acid                             50.00   mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[2].recipe[5]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q53","subject":"Calcium D-(+)-pantothenate Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[27].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[27].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[27].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[27].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[27].concentration","original":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x
    stock","interpretation":"The exact primary table supports this separate vitamin-stock
    batch amount and current APIs explicitly declare the stored g_l on that stock
    basis. It is not a main-medium concentration. Restore the ten-component stock
    and1ml addition; listed1000ml water does not independently establish a measured
    final stock volume.","sources":[{"locator":"extracted-text physical LF lines 63-63","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Calcium
    D-(+)-pantothenate                 50.00   mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[2].recipe[6]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text physical LF lines 63-63","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Calcium
    D-(+)-pantothenate                 50.00   mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[2].recipe[6]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q54","subject":"Vitamin B12 Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[28].concentration","original":{"value":"0.001","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[28].concentration","original":{"value":"0.001","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[28].concentration","original":{"value":"0.001","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[28].concentration","original":{"value":"0.001","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[28].concentration","original":{"value":"0.001","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x
    stock","interpretation":"The exact primary table supports this separate vitamin-stock
    batch amount and current APIs explicitly declare the stored g_l on that stock
    basis. It is not a main-medium concentration. Restore the ten-component stock
    and1ml addition; listed1000ml water does not independently establish a measured
    final stock volume.","sources":[{"locator":"extracted-text physical LF lines 64-64","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Vitamin
    B12                                 1.00   mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[2].recipe[7]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text physical LF lines 64-64","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Vitamin
    B12                                 1.00   mg","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[2].recipe[7]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q55","subject":"p-Aminobenzoic acid Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[29].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[29].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[29].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[29].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[29].concentration","original":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x
    stock","interpretation":"The exact primary table supports this separate vitamin-stock
    batch amount and current APIs explicitly declare the stored g_l on that stock
    basis. It is not a main-medium concentration. Restore the ten-component stock
    and1ml addition; listed1000ml water does not independently establish a measured
    final stock volume.","sources":[{"locator":"extracted-text physical LF lines 65-65","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   p-Aminobenzoic
    acid                        50.00   mg","quote_representation":"captured extracted
    text"},{"locator":"$.data.solutions[2].recipe[8]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text physical LF lines 65-65","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   p-Aminobenzoic
    acid                        50.00   mg","quote_representation":"captured extracted
    text"},{"locator":"$.data.solutions[2].recipe[8]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q56","subject":"(DL)-alpha-Lipoic acid Wolin10x","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ingredients[30].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ingredients[30].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ingredients[30].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ingredients[30].concentration","original":{"value":"0.05","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ingredients[30].concentration","original":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","stage":"Wolin10x
    stock","interpretation":"The exact primary table supports this separate vitamin-stock
    batch amount and current APIs explicitly declare the stored g_l on that stock
    basis. It is not a main-medium concentration. Restore the ten-component stock
    and1ml addition; listed1000ml water does not independently establish a measured
    final stock volume.","sources":[{"locator":"extracted-text physical LF lines 66-66","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   (DL)-alpha-Lipoic
    acid                     50.00   mg","quote_representation":"captured extracted
    text"},{"locator":"$.data.solutions[2].recipe[9]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text physical LF lines 66-66","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   (DL)-alpha-Lipoic
    acid                     50.00   mg","quote_representation":"captured extracted
    text"},{"locator":"$.data.solutions[2].recipe[9]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q57","subject":"dsm813a Trace element solution
    SL-10 dose","local_fields":[],"decision":"add","stage":"exact source receiving
    dose","interpretation":"Restore the distinct1ml addition in this exact source
    branch; do not place stock component rates at root or transfer a strain alternative.","sources":[{"locator":"extracted-text
    physical LF lines 13-13","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Trace
    element solution SL-10                               1.00        ml","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[0].recipe[6]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q58","subject":"dsm813a Wolin''s vitamin solution
    (10x) dose","local_fields":[],"decision":"add","stage":"exact source receiving
    dose","interpretation":"Restore the distinct1ml addition in this exact source
    branch; do not place stock component rates at root or transfer a strain alternative.","sources":[{"locator":"extracted-text
    physical LF lines 20-20","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Wolin''s
    vitamin solution (10x)                             1.00        ml","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[0].recipe[13]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    14,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q59","subject":"dsm813a Main sol. 813a water","local_fields":[],"decision":"add","stage":"separate
    source water input","interpretation":"Preserve main1000ml, SL10 initial990ml and
    Wolin1000ml water as distinct inputs. SL10 separately makes up to1000ml; DSM813a
    separately declares mainfinal1002ml. Do not sum preparation waters or infer a
    primary866 final volume.","sources":[{"locator":"extracted-text physical LF lines
    21-21","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Distilled
    water                                         1000.00        ml","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[0].recipe[14]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q60","subject":"dsm813a Trace element solution
    SL-10 water","local_fields":[],"decision":"add","stage":"separate source water
    input","interpretation":"Preserve main1000ml, SL10 initial990ml and Wolin1000ml
    water as distinct inputs. SL10 separately makes up to1000ml; DSM813a separately
    declares mainfinal1002ml. Do not sum preparation waters or infer a primary866
    final volume.","sources":[{"locator":"extracted-text physical LF lines 42-42","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Distilled
    water                                           990.00      ml","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[1].recipe[9]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 990,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q61","subject":"dsm813a Wolin''s vitamin solution
    (10x) water","local_fields":[],"decision":"add","stage":"separate source water
    input","interpretation":"Preserve main1000ml, SL10 initial990ml and Wolin1000ml
    water as distinct inputs. SL10 separately makes up to1000ml; DSM813a separately
    declares mainfinal1002ml. Do not sum preparation waters or infer a primary866
    final volume.","sources":[{"locator":"extracted-text physical LF lines 67-67","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"   Distilled
    water                          1000.00   ml","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[2].recipe[10]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q62","subject":"dsm866 Trace element solution
    SL-10 dose","local_fields":[],"decision":"add","stage":"exact source receiving
    dose","interpretation":"Restore the distinct1ml addition in this exact source
    branch; do not place stock component rates at root or transfer a strain alternative.","sources":[{"locator":"extracted-text
    physical LF lines 9-9","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Trace
    element solution SL-10                               1.00        ml","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[0].recipe[6]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q63","subject":"dsm866 Wolin''s vitamin solution
    (10x) dose","local_fields":[],"decision":"add","stage":"exact source receiving
    dose","interpretation":"Restore the distinct1ml addition in this exact source
    branch; do not place stock component rates at root or transfer a strain alternative.","sources":[{"locator":"extracted-text
    physical LF lines 15-15","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Wolin''s
    vitamin solution (10x)                             1.00        ml","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[0].recipe[12]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q64","subject":"dsm866 Main sol. 866 water","local_fields":[],"decision":"add","stage":"separate
    source water input","interpretation":"Preserve main1000ml, SL10 initial990ml and
    Wolin1000ml water as distinct inputs. SL10 separately makes up to1000ml; DSM813a
    separately declares mainfinal1002ml. Do not sum preparation waters or infer a
    primary866 final volume.","sources":[{"locator":"extracted-text physical LF lines
    17-17","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Distilled
    water                                         1000.00        ml","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[0].recipe[14]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q65","subject":"dsm866 Trace element solution
    SL-10 water","local_fields":[],"decision":"add","stage":"separate source water
    input","interpretation":"Preserve main1000ml, SL10 initial990ml and Wolin1000ml
    water as distinct inputs. SL10 separately makes up to1000ml; DSM813a separately
    declares mainfinal1002ml. Do not sum preparation waters or infer a primary866
    final volume.","sources":[{"locator":"extracted-text physical LF lines 42-42","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Distilled
    water                                           990.00      ml","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[1].recipe[9]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 990,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q66","subject":"dsm866 Wolin''s vitamin solution
    (10x) water","local_fields":[],"decision":"add","stage":"separate source water
    input","interpretation":"Preserve main1000ml, SL10 initial990ml and Wolin1000ml
    water as distinct inputs. SL10 separately makes up to1000ml; DSM813a separately
    declares mainfinal1002ml. Do not sum preparation waters or infer a primary866
    final volume.","sources":[{"locator":"extracted-text physical LF lines 67-67","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"   Distilled
    water                          1000.00   ml","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[2].recipe[10]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q67","subject":"DSM813a explicit final denominator","local_fields":[],"decision":"add","stage":"DSM813a
    main denominator","interpretation":"Record positive primary final1002ml at the813a
    layer. This denominator supports its main arithmetic and does not independently
    validate other source versions.","sources":[{"locator":"extracted-text physical
    LF lines 4-4","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Final
    volume: 1002 ml","quote_representation":"captured extracted text"}]},{"decision_id":"q68","subject":"DSM813a
    retained pH and main sequence","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"ph_range","original":{"min":9.0,"max":9.5}},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"ph_range","original":{"min":9.0,"max":9.5}},{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"preparation_steps[0].description","original":"Dissolve
    the ingredients (except carbonates, sulfide, formate, and vitamins) and sparge
    medium with 100% N2 gas for 30 - 45 min. to make it anoxic. Add and dissolve carbonates
    and sulfide, then adjust pH to 9.0 - 9.5, dispense under 100% N2 gas atmosphere
    into Hungate-type tubes or serum vials and autoclave. Before use add formate and
    vitamins (sterilized by filtration) from sterile anoxic stock solutions prepared
    under 100% N2 gas."},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"preparation_steps[0].description","original":"Dissolve
    the ingredients (except carbonates, sulfide, formate, and vitamins) and sparge
    medium with 100% N2 gas for 30 - 45 min. to make it anoxic. Add and dissolve carbonates
    and sulfide, then adjust pH to 9.0 - 9.5, dispense under 100% N2 gas atmosphere
    into Hungate-type tubes or serum vials and autoclave. Before use add formate and
    vitamins (sterilized by filtration) from sterile anoxic stock solutions prepared
    under 100% N2 gas."}],"decision":"evidence_only","stage":"DSM813a main preparation","interpretation":"Retain
    pH9–9.5 and the source30–45min100%N2 sequence, carbonates/sulfide before autoclaving,
    and later sterile formate and filtered vitamins. These correct813a fields do not
    validate the generated866 ingredient amounts.","sources":[{"locator":"extracted-text
    physical LF lines 23-27","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"Dissolve
    the ingredients (except carbonates, sulfide, formate, and vitamins) and sparge\nmedium
    with 100% N2 gas for 30 - 45 min. to make it anoxic. Add and dissolve carbonates\nand
    sulfide, then adjust pH to 9.0 - 9.5, dispense under 100% N2 gas atmosphere into\nHungate-type
    tubes or serum vials and autoclave. Before use add formate and vitamins\n(sterilized
    by filtration) from sterile anoxic stock solutions prepared under 100% N2 gas.","quote_representation":"captured
    extracted text"},{"locator":"$.data.solutions[0].steps[0]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"step\":
    \"Dissolve the ingredients (except carbonates, sulfide, formate, and vitamins)
    and sparge medium with 100% N2 gas for 30 - 45 min. to make it anoxic. Add and
    dissolve carbonates and sulfide, then adjust pH to 9.0 - 9.5, dispense under 100%
    N2 gas atmosphere into Hungate-type tubes or serum vials and autoclave. Before
    use add formate and vitamins (sterilized by filtration) from sterile anoxic stock
    solutions prepared under 100% N2 gas.\"\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q69","subject":"KOMODO866 pH source reconciliation","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml","field_path":"ph_range","original":{"min":8.7,"max":9.0}},{"record_path":"data/normalized_yaml/bacterial/for_dsm_16529.yaml","field_path":"ph_range","original":{"min":8.7,"max":9.0}}],"decision":"correct","stage":"DSM866
    main preparation","interpretation":"The two KOMODO ranges 8.7–9.0 have a different
    lower bound and omit the main preparation; the current DSM866 primary requires
    8.8–9.0 and 100% N2, with sulfide added after sterilization. Restore only with
    exact current branch evidence; DSM813a sulfide timing and pH are distinct. Already-correct
    DSM866 owner fields are credited separately in q71.","sources":[{"locator":"extracted-text
    physical LF lines 19-24","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"Dissolve
    the ingredients (except carbonate, bicarbonate, vitamins, formate and sulfide,)\nand
    sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\ncarbonate
    and bicarbonate, adjust pH to 8.8 - 9.0, then dispense under 100% N2 gas\natmosphere
    into anoxic Hungate-type tubes or serum vials and autoclave. Before use add\nvitamins
    (sterilized by filtration), formate and sulfide from sterile anoxic stock solutions\nprepared
    under 100% N2 gas.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\":
    \"Dissolve the ingredients (except carbonate, bicarbonate, vitamins, formate and
    sulfide,) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic.
    Add and dissolve carbonate and bicarbonate, adjust pH to 8.8 - 9.0, then dispense
    under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and
    autoclave. Before use add vitamins (sterilized by filtration), formate and sulfide
    from sterile anoxic stock solutions prepared under 100% N2 gas.\"\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q70","subject":"SL10 makeup instruction placement","local_fields":[{"record_path":"data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml","field_path":"preparation_steps[1].description","original":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally make up to 1000.00 ml."},{"record_path":"data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml","field_path":"preparation_steps[1].description","original":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally make up to 1000.00 ml."},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"preparation_steps[1].description","original":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally make up to 1000.00 ml."}],"decision":"correct","stage":"SL10 preparation","interpretation":"Existing
    dissolve/make-up-to1000ml text is correct source content but wrongly stored as
    a main-medium step. Relocate it withSL10 and add it at stock scope in the two
    KOMODO contributors; do not alter its positive final-volume evidence.","sources":[{"locator":"extracted-text
    physical LF lines 44-45","source_key":"dsm813a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813a.pdf","source_raw_sha256":"54dc800305928952d1447f3c46c21f4b5bc2988744e727cede70573a565ba9d9","source_text_sha256":"70eb2157f295d5a65f796b85f883ee00de1d61d4b79da4d97bcf2e2059b09e3e","accessed_at":"2026-10-28T20:14:19.748215Z","exact_source_quote":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api813a","reference":"https://mediadive.dsmz.de/rest/medium/813a","source_raw_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","source_text_sha256":"a802b869a7dc4992ce8abe024f4ce9370b05bdbe9864a4aeadcc9d827dbe98c1","accessed_at":"2026-10-28T20:14:19.333712Z","exact_source_quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text physical LF lines 44-45","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally\nmake up to 1000.00 ml.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[1].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q71","subject":"Existing DSM866 pH and main procedure","local_fields":[{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"ph_range","original":{"min":8.8,"max":9.0}},{"record_path":"data/normalized_yaml/bacterial/desulfofalx_medium.yaml","field_path":"preparation_steps[0].description","original":"Dissolve
    the ingredients (except carbonate, bicarbonate, vitamins, formate and sulfide,)
    and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and
    dissolve carbonate and bicarbonate, adjust pH to 8.8 - 9.0, then dispense under
    100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.
    Before use add vitamins (sterilized by filtration), formate and sulfide from sterile
    anoxic stock solutions prepared under 100% N2 gas."}],"decision":"evidence_only","stage":"DSM866
    main preparation","interpretation":"The existing DSM866 owner ph_range 8.8–9.0
    and retained main preparation match the exact current DSM866 source. Retain both
    unchanged and attach supporting evidence. The differing KOMODO lower bounds remain
    scoped separately in q69; no DSM813a conditions are transferred.","sources":[{"locator":"extracted-text
    physical LF lines 19-24","source_key":"dsm866","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium866.pdf","source_raw_sha256":"441cbdf93cbb55b8602b42e66d9e5bf8394f99611c6c275c9173431f7c3f3f79","source_text_sha256":"6bc4b62d41fe425fe6b1b9647e65bb00b1a7736069d59902ede4631de5146bb2","accessed_at":"2026-10-28T20:14:19.999222Z","exact_source_quote":"Dissolve
    the ingredients (except carbonate, bicarbonate, vitamins, formate and sulfide,)\nand
    sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve\ncarbonate
    and bicarbonate, adjust pH to 8.8 - 9.0, then dispense under 100% N2 gas\natmosphere
    into anoxic Hungate-type tubes or serum vials and autoclave. Before use add\nvitamins
    (sterilized by filtration), formate and sulfide from sterile anoxic stock solutions\nprepared
    under 100% N2 gas.","quote_representation":"captured extracted text"},{"locator":"$.data.solutions[0].steps[0]","source_key":"api866","reference":"https://mediadive.dsmz.de/rest/medium/866","source_raw_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","source_text_sha256":"8fd24a3b7cd60246495a400acf31e3866c110f2b94719150069a5a2d757ff148","accessed_at":"2026-10-28T20:14:19.706329Z","exact_source_quote":"{\n                        \"step\":
    \"Dissolve the ingredients (except carbonate, bicarbonate, vitamins, formate and
    sulfide,) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic.
    Add and dissolve carbonate and bicarbonate, adjust pH to 8.8 - 9.0, then dispense
    under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and
    autoclave. Before use add vitamins (sterilized by filtration), formate and sulfide
    from sterile anoxic stock solutions prepared under 100% N2 gas.\"\n                    }","quote_representation":"raw
    JSON object"}]}],"local_field_census_reference":"REVIEW_WORK/batch077/record06/grounding-inventory.json","source_only_gaps_are_explicit":true,"note":"Batch
    amounts, provider normalization, stock composition, working dose and preparation
    controls are separate. No source edits or automatic curation performed."}'
- assessment_id: a6
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/DESULFONATRONUM_THIODISMUTANS_MEDIUM.yaml: primary
    30/31, secondary 28/31; data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml:
    primary 30/31, secondary 28/31; data/normalized_yaml/bacterial/desulfofalx_medium.yaml:
    primary 30/31, secondary 28/31; data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml:
    primary 30/31, secondary 28/31; data/normalized_yaml/bacterial/for_dsm_16529.yaml:
    primary 30/31, secondary 28/31. These are ingredient-instance linkage fractions,
    not accuracy scores. Solution terms are audited separately. Every actually asserted
    CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows.
    0 numeric legacy MediaIngredientMech mentions occur across the complete selected
    documents, with exact locators in the inventory; NNNNNN is a historical placeholder,
    not an ID. Complex commercial/product components are not forced to pure-compound
    IDs.'
  target_ids:
  - CultureMech:001959
  evidence_ids:
  - grounding
- assessment_id: a7
  area: scope
  topic: Scope and source limits
  outcome: supported
  summary: Complete selected target and all exact maintained contributors reviewed.
    Stocks are embedded in the named DSM source recipes; no external dependency parent
    recipe is transferred. Named strain alternatives remain distinct from the generic
    basal formulation.
  target_ids:
  - CultureMech:001959
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
  - CultureMech:001959
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-001959-variant-merge
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Generated813a record combines different source recipes
  description: The generated identity and procedure are813a, but six main amounts
    are866 values. The maintained813a owner also inherits API sulfate/carbonate inconsistency
    and unnormalized bicarbonate. Distinct866 andDSM16529 relationships must not be
    treated as identical scientific formulations.
  target_ids:
  - CultureMech:001959
  field_paths:
  - merged_from
  - ingredients[4].concentration
  - ingredients[5].concentration
  - ingredients[6].concentration
  - ingredients[8].concentration
  - ingredients[9].concentration
  - ingredients[10].concentration
  evidence_ids:
  - dsm813a
  - dsm866
  - api813a
  rule_id: source-variant-formulation-identity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfofalx_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16529.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-001959-strain-substrate
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: DSM16529 wrapper omits its explicit substrate substitution
  description: The strain-specific contributor retains basal formate despite the exact
    current866 primary requiring sodiumL-lactate instead. Existing STRAIN_SPECIFIC_VARIANT
    topology is correct but scientifically incomplete.
  target_ids:
  - CultureMech:001959
  field_paths:
  - data/normalized_yaml/bacterial/for_dsm_16529.yaml::ingredients[10].concentration
  - data/normalized_yaml/bacterial/for_dsm_16529.yaml::variant_modifications
  evidence_ids:
  - dsm866
  - dsm16529Identity
  rule_id: strain-specific-source-modification
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfofalx_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16529.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-001959-stocks
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Embedded stock quantities occupy main ingredients
  description: All five layers flattenSL10 andWolin10x components at root. HCl2.5g/L
    lacks a verified percent basis; the validSL10 stock mass rates require their own
    explicit1000ml makeup, and vitamin rates remain provider stock values. Receiving
    doses and separate water inputs are missing.
  target_ids:
  - CultureMech:001959
  field_paths:
  - ingredients[12].concentration
  - ingredients[30].concentration
  - solutions
  evidence_ids:
  - dsm813a
  - dsm866
  - api813a
  - api866
  rule_id: source-specific-formulation-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfofalx_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16529.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-001959-preparation
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Stock steps and KOMODO atmosphere metadata are inconsistent
  description: 'The threeDSM/generated documents placeSL10 makeup at root. BothKOMODO
    contributors omit preparation and store Aerobic: Yes in notes, contradicting the
    exact current anaerobic source. Their pH lower bound also differs. Preserve the
    correct, different813a and866 main sequences.'
  target_ids:
  - CultureMech:001959
  field_paths:
  - preparation_steps[1].description
  - data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml::notes
  - data/normalized_yaml/bacterial/for_dsm_16529.yaml::notes
  - data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml::ph_range
  - data/normalized_yaml/bacterial/for_dsm_16529.yaml::ph_range
  evidence_ids:
  - dsm813a
  - dsm866
  rule_id: source-preparation-stage-consistency
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfofalx_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16529.yaml
    role: maintained normalized contributor
- finding_id: f5
  issue_key: culturemech-001959-nickel-hydrate-and-sodium-resazurin-form
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
  - CultureMech:001959
  field_paths:
  - ingredients[19].term
  - ingredients[19].mediaingredientmech_chebi_term
  - ingredients[7].term
  evidence_ids:
  - dsm813a
  - chebi34887
  - chebi8806
  - grounding
  rule_id: supplied-chemical-form-correspondence
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfofalx_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16529.yaml
    role: maintained normalized contributor
- finding_id: f6
  issue_key: culturemech-001959-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical timestamps and absent claim evidence need bounded follow-up
  description: Selected records have no attached formulation excerpts. KOMODO events
    store literal.fZ and resolver events lack offsets. Current code behavior and historical
    report byte matches cannot recover those original instants or authenticate historical
    execution.
  target_ids:
  - CultureMech:001959
  field_paths:
  - curation_history
  - ingredients[*]
  evidence_ids:
  - history-auth
  - historical-current-joins
  rule_id: claim-and-timestamp-provenance
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfofalx_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16529.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: current import timestamp writer
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/enrich/dsmz_resolver.py
    role: current enrichment timestamp and preparation propagation writer
actions:
- action_id: action1
  description: Separate exact source formulations before regeneration; correct813a
    using its primary1002ml basis, retain supported values and reject cross-variant
    ingredient-set merging.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001959
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfofalx_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16529.yaml
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
  description: Represent the exactDSM16529 source modification within that maintained
    variant only; preserve generic866 and813a recipes and avoid treating catalogue
    association as an experimental growth measurement.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001959
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfofalx_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16529.yaml
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
  description: Restore each exact stock and receiving dose with separate batch/final-volume
    evidence. Retain positiveSL10 makeup and supported main rates; do not convert
    bare25% acid by guessed density or promote provider stock rates to the medium.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001959
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfofalx_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16529.yaml
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
  description: Scope stock preparation insideSL10 and restore exact current branch
    pH/anaerobic preparation while retaining historical source notes as provenance
    rather than active cultivation assertions.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001959
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfofalx_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16529.yaml
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
  description: Resolve the exact source hydrate and sodium-salt identities against
    authoritative ontology and MIM records. Use verified supplied-form mappings or
    retain precise source labels with unresolved mapping; preserve source masses and
    do not substitute anhydrous molar arithmetic.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:001959
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfofalx_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16529.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action6
  description: Preserve all original events and append actual verified source context;
    repair the exact current timestamp writers for future events without inventing
    old timestamps. Attach excerpts only at schema-supported scopes.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:001959
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_thiodismutans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfofalx_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfotomaculum_alkaliphilum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16529.yaml
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
  - Verify komodo_web_importer.py and DSMZCompositionResolver future events use valid
    timezone-aware UTC timestamps; retain all original historical event bytes and
    distinguish stored.fZ from the current%f format token.
limitations:
- Exact historical KOMODO866/866.1 routes returned403 and are preserved; currentDSM
  sources and catalogue support bounded conclusions without authenticating inaccessible
  historical versions.
- OnlyDSM813a explicitly declares main final1002ml; DSM866 g_l values remain qualified
  provider normalization. BareHCl25% has no established basis.
- Current exact API digest/object equality does not authenticate historical access
  dates or execution. Named source variants remain distinct; no experimental growth
  claim or record edit was made.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
