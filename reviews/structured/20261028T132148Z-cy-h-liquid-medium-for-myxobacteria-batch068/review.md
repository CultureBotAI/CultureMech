# Scientific review of cy_h_liquid_medium_for_myxobacteria

- Review: 20261028T132148Z-cy-h-liquid-medium-for-myxobacteria-batch068
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T13:11:52.410675Z
- Finished UTC: 2026-10-28T13:21:48.356435Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact source and retained preparation are supported, but A/B/C stock stages are flattened and lack attached evidence. Eight basal values are supported only for solution A; two stock strengths conflict with their main-ingredient placement. HEPES has a bounded current secondary-linkage gap.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch068 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001020 | data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml | generated | cy_h_liquid_medium_for_myxobacteria |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001020 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:001020 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:001020 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:001020 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact source and existing scientific content

identity: supported. Targets: CultureMech:001020.

DSM1542 CY/H liquid medium is the exact source. Both selected layers retain liquid/complex/undefined classification, source pH and full staged preparation prose. The generic myxobacterial title does not identify one strain or constitute experimental growth evidence.

### Existing claims and historical stock interpretation

evidence: concern. Targets: CultureMech:001020.

Neither selected layer has attached formulation claims. The historical API raw digest and seventeen quoted source objects match current bytes, but the old blanket conflict labels are too broad for the eight source-A rates. Those eight numbers have supported A-stage values while their flat final-medium basis is unresolved; the two stock-strength main entries are distinct stage conflicts.

### Exact forms and current MIM distinction

grounding: concern. Targets: CultureMech:001020.

Calcium dihydrate, magnesium heptahydrate, D-glucose and starch labels agree with the source scope. Generic vitamin B12 is appropriately a class; do not infer cyanocobalamin or accept a unique molar mass from provider mmol_l. Fe(III)-EDTA resolves to the complex anion, without an established counterion or hydrate; no forced salt replacement. HEPES46756 is an active OLS class without a formula and is not an exact current MIM identifier key; the neutral acid 42334 is a verified candidate, not an automatic substitution.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:001020.

All three historical reports were fully read. Current API1542 exactly authenticates the cited old payload and seventeen source objects, without proving historical execution. The single-owner target retains the owner scientific fields. The current MediaDive importer separates main ingredients from referenced stock descriptors; its present behavior is credited and does not repair already flattened data or establish stock final-volume arithmetic. Current conservative merging preserves scientific fields and rejects incompatible formulations. Inspected writer behavior is described separately by exact file and function; it does not prove historical execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:001020.

All 20 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:001020", "selected_concentration_field_count": 20, "selected_concentration_fields_covered": 20, "decisions": [{"decision_id": "q1", "subject": "Casitone", "local_fields": [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Supported solution A basis; unestablished final assembled-medium basis", "interpretation": "The current number and supplied form are supported as an explicit provider solution-A g_l and as the primary solution-A batch input. The flat final-medium placement loses that stage; it is not a demonstrated numerical contradiction. Source A lists 1000 ml water, then receives 1 ml each of B and C per liter A. No measured final mixture volume is specified, so neither 1 L nor 1.002 L final is inferred. Keep these amounts at their source A stage; no unsupported renormalization.", "sources": [{"locator": "$.data.solutions[1].recipe[0]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Casitone\",\n                        \"compound_id\": 84,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 4-4", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Casiton                                                            1.5       g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 12-12", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled water                                                 1000.0      ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution A.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q2", "subject": "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Supported solution A basis; unestablished final assembled-medium basis", "interpretation": "The current number and supplied form are supported as an explicit provider solution-A g_l and as the primary solution-A batch input. The flat final-medium placement loses that stage; it is not a demonstrated numerical contradiction. Source A lists 1000 ml water, then receives 1 ml each of B and C per liter A. No measured final mixture volume is specified, so neither 1 L nor 1.002 L final is inferred. Keep these amounts at their source A stage; no unsupported renormalization.", "sources": [{"locator": "$.data.solutions[1].recipe[1]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 5-5", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Yeast extract                                                      1.5       g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 12-12", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled water                                                 1000.0      ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution A.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q3", "subject": "Starch", "local_fields": [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "4", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "4", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Supported solution A basis; unestablished final assembled-medium basis", "interpretation": "The current number and supplied form are supported as an explicit provider solution-A g_l and as the primary solution-A batch input. The flat final-medium placement loses that stage; it is not a demonstrated numerical contradiction. Source A lists 1000 ml water, then receives 1 ml each of B and C per liter A. No measured final mixture volume is specified, so neither 1 L nor 1.002 L final is inferred. Keep these amounts at their source A stage; no unsupported renormalization.", "sources": [{"locator": "$.data.solutions[1].recipe[2]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Starch\",\n                        \"compound_id\": 199,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 4,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 6-6", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Starch                                                             4.0       g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 12-12", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled water                                                 1000.0      ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution A.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q4", "subject": "Soy flour", "local_fields": [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Supported solution A basis; unestablished final assembled-medium basis", "interpretation": "The current number and supplied form are supported as an explicit provider solution-A g_l and as the primary solution-A batch input. The flat final-medium placement loses that stage; it is not a demonstrated numerical contradiction. Source A lists 1000 ml water, then receives 1 ml each of B and C per liter A. No measured final mixture volume is specified, so neither 1 L nor 1.002 L final is inferred. Keep these amounts at their source A stage; no unsupported renormalization.", "sources": [{"locator": "$.data.solutions[1].recipe[3]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Soy flour\",\n                        \"compound_id\": 1405,\n                        \"condition\": \"defatted\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Soy flour, defatted                                                1.0       g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 12-12", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled water                                                 1000.0      ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution A.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q5", "subject": "D-Glucose", "local_fields": [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Supported solution A basis; unestablished final assembled-medium basis", "interpretation": "The current number and supplied form are supported as an explicit provider solution-A g_l and as the primary solution-A batch input. The flat final-medium placement loses that stage; it is not a demonstrated numerical contradiction. Source A lists 1000 ml water, then receives 1 ml each of B and C per liter A. No measured final mixture volume is specified, so neither 1 L nor 1.002 L final is inferred. Keep these amounts at their source A stage; no unsupported renormalization.", "sources": [{"locator": "$.data.solutions[1].recipe[4]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\": 211,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.55062,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 8-8", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "D-Glucose                                                          1.0       g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 12-12", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled water                                                 1000.0      ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution A.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q6", "subject": "CaCl 2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Supported solution A basis; unestablished final assembled-medium basis", "interpretation": "The current number and supplied form are supported as an explicit provider solution-A g_l and as the primary solution-A batch input. The flat final-medium placement loses that stage; it is not a demonstrated numerical contradiction. Source A lists 1000 ml water, then receives 1 ml each of B and C per liter A. No measured final mixture volume is specified, so neither 1 L nor 1.002 L final is inferred. Keep these amounts at their source A stage; no unsupported renormalization.", "sources": [{"locator": "$.data.solutions[1].recipe[5]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 6.80203,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 9-9", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "CaCl 2 X 2 H2O                                                     1.0       g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 12-12", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled water                                                 1000.0      ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution A.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q7", "subject": "MgSO4 x 7 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Supported solution A basis; unestablished final assembled-medium basis", "interpretation": "The current number and supplied form are supported as an explicit provider solution-A g_l and as the primary solution-A batch input. The flat final-medium placement loses that stage; it is not a demonstrated numerical contradiction. Source A lists 1000 ml water, then receives 1 ml each of B and C per liter A. No measured final mixture volume is specified, so neither 1 L nor 1.002 L final is inferred. Keep these amounts at their source A stage; no unsupported renormalization.", "sources": [{"locator": "$.data.solutions[1].recipe[6]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.02859,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 10-10", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "MgSO 4 x 7 H2O                                                     0.5       g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 12-12", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled water                                                 1000.0      ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution A.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q8", "subject": "HEPES", "local_fields": [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "11.9", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "11.9", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Supported solution A basis; unestablished final assembled-medium basis", "interpretation": "The current number and supplied form are supported as an explicit provider solution-A g_l and as the primary solution-A batch input. The flat final-medium placement loses that stage; it is not a demonstrated numerical contradiction. Source A lists 1000 ml water, then receives 1 ml each of B and C per liter A. No measured final mixture volume is specified, so neither 1 L nor 1.002 L final is inferred. Keep these amounts at their source A stage; no unsupported renormalization.", "sources": [{"locator": "$.data.solutions[1].recipe[7]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"HEPES\",\n                        \"compound_id\": 371,\n                        \"amount\": 11.9,\n                        \"unit\": \"g\",\n                        \"g_l\": 11.9,\n                        \"mmol_l\": 49.9371,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 11-11", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "HEPES                                                             11.9       g", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 12-12", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled water                                                 1000.0      ml", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution A.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q9", "subject": "Fe(III)-EDTA", "local_fields": [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "8", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "8", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate solution B stock", "interpretation": "The local 8 g/L iron complex or 0.5 g/L vitamin concentration belongs to the separate 100 ml provider stock, not a full-strength main ingredient. Primary stock inputs are 0.80 g iron complex or 0.05 g B12 with 100 ml water; preserve those batch inputs. API g_l 8/.5 are credited only as provider stock rates. Addition is 1 ml stock per liter A. On that declared stock-rate basis the inputs are 8 mg iron complex or 0.5 mg B12 per liter A, not a measured final-medium concentration; final volume remains unresolved.", "sources": [{"locator": "$.data.solutions[2].recipe[0]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Fe(III)-EDTA\",\n                        \"compound_id\": 952,\n                        \"amount\": 0.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 8,\n                        \"mmol_l\": 23.252,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 15-15", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "EDTA-iron                                                         0.80       g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[2].recipe[1]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution A.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q10", "subject": "Vitamin B12", "local_fields": [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Separate solution C stock", "interpretation": "The local 8 g/L iron complex or 0.5 g/L vitamin concentration belongs to the separate 100 ml provider stock, not a full-strength main ingredient. Primary stock inputs are 0.80 g iron complex or 0.05 g B12 with 100 ml water; preserve those batch inputs. API g_l 8/.5 are credited only as provider stock rates. Addition is 1 ml stock per liter A. On that declared stock-rate basis the inputs are 8 mg iron complex or 0.5 mg B12 per liter A, not a measured final-medium concentration; final volume remains unresolved.", "sources": [{"locator": "$.data.solutions[3].recipe[0]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 0.368895,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 19-19", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Vitamin B12                                                       0.05       g", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[1]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution A.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q11", "subject": "Solution A water", "local_fields": [], "decision": "add", "stage": "Stock/base batch solvent", "interpretation": "Preserve the explicit 1000 ml water input for A and 100 ml water inputs for each B/C stock as volume. Listed water is not an independently established final stock or mixture volume. The provider normalization is documented separately.", "sources": [{"locator": "$.data.solutions[1].recipe[8]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 12-12", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled water                                                 1000.0      ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q12", "subject": "Solution B water", "local_fields": [], "decision": "add", "stage": "Stock/base batch solvent", "interpretation": "Preserve the explicit 1000 ml water input for A and 100 ml water inputs for each B/C stock as volume. Listed water is not an independently established final stock or mixture volume. The provider normalization is documented separately.", "sources": [{"locator": "$.data.solutions[2].recipe[1]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 16-16", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled water                                                  100.0      ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q13", "subject": "Solution C water", "local_fields": [], "decision": "add", "stage": "Stock/base batch solvent", "interpretation": "Preserve the explicit 1000 ml water input for A and 100 ml water inputs for each B/C stock as volume. Listed water is not an independently established final stock or mixture volume. The provider normalization is documented separately.", "sources": [{"locator": "$.data.solutions[3].recipe[1]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 16-16", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled water                                                  100.0      ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q14", "subject": "Solution A assembly dose", "local_fields": [], "decision": "add", "stage": "Receiving mixture", "interpretation": "The API main assembly is 1000 ml A plus 1 ml B and 1 ml C; primary prose specifies each 1 ml addition per liter A. Represent each named solution and its receiving dose separately, with evidence at the enclosing recipe. Do not double-count the flattened stock constituents or treat a source solution volume as a universal dose.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 3195,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution A.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q15", "subject": "Solution B assembly dose", "local_fields": [], "decision": "add", "stage": "Receiving mixture", "interpretation": "The API main assembly is 1000 ml A plus 1 ml B and 1 ml C; primary prose specifies each 1 ml addition per liter A. Represent each named solution and its receiving dose separately, with evidence at the enclosing recipe. Do not double-count the flattened stock constituents or treat a source solution volume as a universal dose.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\": 3196,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution A.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q16", "subject": "Solution C assembly dose", "local_fields": [], "decision": "add", "stage": "Receiving mixture", "interpretation": "The API main assembly is 1000 ml A plus 1 ml B and 1 ml C; primary prose specifies each 1 ml addition per liter A. Represent each named solution and its receiving dose separately, with evidence at the enclosing recipe. Do not double-count the flattened stock constituents or treat a source solution volume as a universal dose.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 3197,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution A.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q17", "subject": "pH and full retained preparation", "local_fields": [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml", "field_path": "ph_value", "original": 7.4}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml", "field_path": "ph_value", "original": 7.4}, {"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml", "field_path": "preparation_steps[0].description", "original": "Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution A."}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml", "field_path": "preparation_steps[0].description", "original": "Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution A."}], "decision": "evidence_only", "stage": "Solution A adjustment; A/B heat and C filter stages", "interpretation": "pH7.4 belongs to solution A before assembly. The complete source description is retained in both target and owner and must be credited: A/B separately autoclaved, vitamin stock filtered, then additions after cooling. The single AUTOCLAVE action code captures only part of this compound procedure; the vitamin solution must not inherit that code as its sterilization method. No temperatures or times are supplied.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution A.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 24-26", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf", "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783", "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249", "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize\nvitamin solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution\nA.", "quote_representation": "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch068/record06/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:001020.

data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml: primary 7/10, secondary 7/10; data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml: primary 7/10, secondary 7/10. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:001020.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:001020.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Separate A/B/C formulations are flattened into main-medium rates

major / open / confirmed; issue key: culturemech-001020-source-stock-stage-collapse.

The source main assembly adds solution A with small B and C doses. Local iron-complex 8 g/L and B12 0.5 g/L are the provider stock rates, but appear as direct main ingredients. The other eight local values correspond to A and lack an established final-mixture denominator. The complete staged preparation prose is present and is credited.

### f2: Formulation and staged preparation lack attached source support

major / open / confirmed; issue key: culturemech-001020-source-claim-evidence-gap.

Current sources support exact batch amounts, named stocks and procedures, but neither target nor maintained owner carries claim-level formulation evidence or references. A source URL in notes does not explain the currently flattened quantity scope.

### f3: HEPES secondary linkage does not match the current MIM key

minor / open / confirmed; issue key: culturemech-001020-hepes-secondary-current-snapshot-gap.

Both layers assert CHEBI:46756 in primary and MIM-secondary slots. OLS confirms this active HEPES class, but the current packaged MIM index has no exact identifier-key row for 46756 and instead links the HEPES preferred term to 42334. This is a current correspondence gap, not an invalid ChEBI ID or historical-deprecation finding.

## Recommended Actions And Acceptance Checks

### action1

Represent the source A/B/C compositions, solvent volumes and receiving doses separately; retain correct A inputs and source stock rates only at their declared stages. Remove stock-strength claims from the final-medium ingredient interpretation without guessing final concentrations. Preserve the full existing preparation description and distinguish heat/filter/addition stages.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Attach exact source excerpts to the appropriate ingredient composition fields, and receiving-dose/preparation evidence at the enclosing recipe with explicit paths and stages. Preserve all unchanged source-supported content; regenerate after the maintained stage model is corrected.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Resolve the source HEPES form and current MIM mapping explicitly, retaining a class-level primary assertion if only that granularity is supported. Do not overwrite both slots automatically from a label match. Preserve prior mapping events and record current-snapshot evidence.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch068/record06/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch068/record06/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch068/record06/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch068/record06/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| dsm1542 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current primary captured text and available rendered PDF pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| api1542 | https://mediadive.dsmz.de/rest/medium/1542; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17634 = D-glucose; definition ['A glucose with &lt;small&gt;D&lt;/small&gt;-configuration.']; formula ['C6H12O6']; mass ['180.156']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi28017 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28017; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:28017 = starch; definition ['The most important reserve polysaccharide found in plants. It is a glucan consisting of amylose and amylopectin.']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30729 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30729; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30729 = ethylenediaminetetraacetatoferrate(1-); definition []; formula ['C10H12N2O8.Fe']; mass ['344.057']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S']; mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi46756 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_46756; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:46756 = HEPES; definition []; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O']; mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi42334 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_42334; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:42334 = 2-[4-(2-hydroxyethyl)piperazin-1-yl]ethanesulfonic acid; definition ["A HEPES that is ethanesulfonic acid in which one of the methyl hydrogens is replaced by a 4-(2-hydroxyethyl)piperazin-1-yl group. A Good's buffer substance, p&lt;em&gt;K&lt;/em&gt;&lt;small&gt;&lt;sub&gt;a&lt;/sub&gt;&lt;/small&gt; = 7.55 at 20 °C."]; formula ['C8H18N2O4S']; mass ['238.309']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch068/record06/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. Current api1542 raw bytes exactly match the cited historical SHA, and 17 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch068/record06/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer21 | scripts/apply_mim_groundings.py; target_slot; groundable; apply_to_record | context_only | Current target_slot preserves existing CHEBI assertions; groundable excludes conflicting corpus opinions, and apply_to_record fills ungrounded entries from proposals. This writer does not authenticate source amounts or automatically repair an existing wrong supplied-form ID. |
| writer22 | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata | context_only | Current DSMZCompositionResolver.merge_composition copies ingredients and solutions, fills pH when absent and copies physical/medium type, but does not copy preparation steps. _add_enrichment_metadata records a naive current timestamp. This explains a present omission risk, not historical execution. |
| writer23 | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current _convert_to_culturemech constructs source notes and default LIQUID with empty ingredients. Its time.strftime format contains %f, which is unsupported here and is consistent with literal .fZ in stored import events. Current code does not authenticate the original retrieval or justify rewriting historical time. |
| writer24 | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps | context_only | Current _parse_api_composition considers the primary recipe, prefers provider g_l when available and excludes four recognized water labels; tap water is not among those exclusions; _is_api_stock_addition distinguishes stock additions. _parse_api_solutions retains separate stock structure. _parse_preparation_steps collects solution prose. These present behaviors do not establish historical execution and cannot justify interpreting flattened stock rates as final-medium concentrations. |
| writer25 | src/culturemech/match/kg_media_matcher.py; extract_recipe_ingredients; find_matches; find_exact_match | context_only | Current extract_recipe_ingredients collects asserted CHEBI/FOODON IDs, find_matches compares set Jaccard and find_exact_match selects the first exact identifier set. Quantities, preparation and ungrounded ingredients are not compared, so an exact set match does not establish formulation identity. |
| writer26 | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current formulation_content retains exact scientific quantities, preparation and other scientific fields; merge_formulation_evidence rejects incompatible projections and unions evidence at matching scopes. A source-equivalence claim is not established by shared ingredient identities. |
| writer27 | src/culturemech/merge/matcher.py; group_formulations; group_recipes | context_only | Current group_formulations calls group_recipes with fail_on_invalid=True and FormulationFingerprinter. Expected standalone or unfingerprintable records are excluded; malformed or unexpected inputs raise. Valid records are grouped by full scientific content. This guard does not retrieve or authenticate source recipes. |
| writer28 | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group routes a single maintained owner with merge metadata; multiple owners pass through conservative merge_formulation_evidence. Regenerating from an unrepaired owner retains its defects. Current conservative behavior is credited and does not establish how the old generated record was produced. |
| hepes-current-mim | REVIEW_WORK/batch068/record06/hepes-mim-comparison.json; candidate_rows: CSV lines717,1140,1141,1154,4711-4715 | supports | Current exact MIM identifier-key search has no CHEBI:46756 row; the exact HEPES preferred-term rows instead point to CHEBI:42334, whose current OLS object identifies the neutral acid. This is a current-snapshot linkage distinction, not proof the historical assertion was invalid. |
| quantity-inventory | REVIEW_WORK/batch068/record06/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- Primary solution water inputs and provider volume metadata do not establish measured final stock or assembled-medium volumes. No 1.002 L denominator is inferred.
- Exact Fe-EDTA counterion/hydrate and vitamin B12 vitamer are not specified. Broad ontology classes are retained; no unsupported mass-to-molar conversion or forced supplied-form mapping.
- Current MIM identifier-key absence is bounded to the pinned snapshot and does not imply historical invalidity. No numerical legacy MIM identifiers occur in these complete selected documents.
- Native references checked zero objects. Current writers describe present behavior only; no source records were changed.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T132148Z-cy-h-liquid-medium-for-myxobacteria-batch068
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of cy_h_liquid_medium_for_myxobacteria
started_at: '2026-10-28T13:11:52.410675Z'
finished_at: '2026-10-28T13:21:48.356435Z'
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
summary: The exact source and retained preparation are supported, but A/B/C stock
  stages are flattened and lack attached evidence. Eight basal values are supported
  only for solution A; two stock strengths conflict with their main-ingredient placement.
  HEPES has a bounded current secondary-linkage gap.
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
  - path: data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml
    sha256: 646ebfa4438d0a9bdc7025c9a1c6eaf362a3391cdac0fe79b92fcb70e855d27d
    role: target
  - path: data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml
    sha256: 5e6cbe05b39408ba4854756168025f4e6a8efcd0057559fe32cc7020c072bbd7
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml.md
    sha256: 75d2eb48c4a887d253dbbc0b1f86e0518d843dc86150c39138faaffd00e15390
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.md
    sha256: 0484939b9bb7fb1120315e62d7d5f0b8d9033f373a86251bf5afd780f2fbfafb
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.md
    sha256: 595600d15ef95068073bf24a76aa653398d16b5d344c9d21a67290b6dfb588f1
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
  selection: Authoritative batch068 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001020
targets:
- target_id: CultureMech:001020
  path: data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml
  label: cy_h_liquid_medium_for_myxobacteria
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:001020
  command: just validate-schema data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:001020
  command: just validate-strict data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml
    --workers 1 --out REVIEW_WORK/batch068/record06/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:001020
  command: just validate-terms data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:001020
  command: just validate-references data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T13:21:00.071815Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 646ebfa4438d0a9bdc7025c9a1c6eaf362a3391cdac0fe79b92fcb70e855d27d
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T13:21:00.071972Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 5e6cbe05b39408ba4854756168025f4e6a8efcd0057559fe32cc7020c072bbd7
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch068/record06/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T13:11:53.462725Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: deca4384383ca0f23278d996f69ad3e66566550cb8e8b3934496d4fed443afe3
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch068/record06/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T13:11:54.415220Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 1de8dc2f0823ffe54b9d7b254749228794c08cfc06a1f83059125bd8543a4035
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch068/record06/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T13:11:55.481615Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 078b5ab19fe76883ac66f26481ef13f3b2313b395b381ea4d412e8b58a89132a
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch068/record06/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T13:11:56.157936Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: f3112548a65451458eded517415b536ae39908f0d51eeb4781366b8a4ee12882
- evidence_id: dsm1542
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T13:11:55.834453Z'
  support: supports
  summary: 'Complete current primary captured text and available rendered PDF pages
    read: exact main recipe, separate stock tables, preparation and any strain-specific
    prescriptions. A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: 12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783
- evidence_id: api1542
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1542
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T13:11:55.827403Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047
- evidence_id: chebi17634
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T13:11:55.821668Z'
  support: supports
  summary: OLS current exact CHEBI:17634 = D-glucose; definition ['A glucose with
    <small>D</small>-configuration.']; formula ['C6H12O6']; mass ['180.156']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d11b31a8e91c3fffe7744f612dab69cdb4e02f42068cd2eb1458acee4503a62f
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T13:11:55.076312Z'
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
- evidence_id: chebi28017
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28017
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T13:11:55.076274Z'
  support: supports
  summary: OLS current exact CHEBI:28017 = starch; definition ['The most important
    reserve polysaccharide found in plants. It is a glucan consisting of amylose and
    amylopectin.']; formula None; mass None; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 959b4330165a7ff12d2e464f4a7b44e148376624d04cf7764b6a8671c1c99204
- evidence_id: chebi30729
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30729
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T13:11:55.076222Z'
  support: supports
  summary: OLS current exact CHEBI:30729 = ethylenediaminetetraacetatoferrate(1-);
    definition []; formula ['C10H12N2O8.Fe']; mass ['344.057']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: e9163d86299489e8bf0a7c758ba8664b3643bb582761cd2fe670f96af028721c
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
- evidence_id: chebi46756
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_46756
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T13:11:55.076074Z'
  support: supports
  summary: OLS current exact CHEBI:46756 = HEPES; definition []; formula None; mass
    None; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 4270cc705078ff2f1787f98b7dbcf05c96b1eccd333801a00cff01b855298a69
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T13:11:55.075761Z'
  support: supports
  summary: OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O'];
    mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi42334
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_42334
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T13:14:47.811374Z'
  support: supports
  summary: OLS current exact CHEBI:42334 = 2-[4-(2-hydroxyethyl)piperazin-1-yl]ethanesulfonic
    acid; definition ["A HEPES that is ethanesulfonic acid in which one of the methyl
    hydrogens is replaced by a 4-(2-hydroxyethyl)piperazin-1-yl group. A Good's buffer
    substance, p<em>K</em><small><sub>a</sub></small> = 7.55 at 20 °C."]; formula
    ['C8H18N2O4S']; mass ['238.309']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 16649912180b1fd199fef763adad4095ac29eba1cae7685366c5ae82b83bed17
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch068/record06/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T13:21:00.075668Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 5b360343da3c8d0943ce632b912b21b4b070455294f3e3e139e22ac4f835a083
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T13:21:00.076195Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. Current
    api1542 raw bytes exactly match the cited historical SHA, and 17 quoted objects
    match both decoded locators and literal current raw substrings. This authenticates
    the cited API payload and excerpts, not the reported historical access time, execution
    or separate KOMODO catalogue/page.
  snapshot_sha256: 75d2eb48c4a887d253dbbc0b1f86e0518d843dc86150c39138faaffd00e15390
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T13:21:00.076216Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: 595600d15ef95068073bf24a76aa653398d16b5d344c9d21a67290b6dfb588f1
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T13:21:00.076235Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: 0484939b9bb7fb1120315e62d7d5f0b8d9033f373a86251bf5afd780f2fbfafb
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch068/record06/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T13:21:00.076255Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: d521931595979acea2add393174d56dd5881e9950385683cc65563064cca67aa
- evidence_id: writer21
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: target_slot; groundable; apply_to_record
  accessed_at: '2026-10-28T13:21:00.076307Z'
  support: context_only
  summary: Current target_slot preserves existing CHEBI assertions; groundable excludes
    conflicting corpus opinions, and apply_to_record fills ungrounded entries from
    proposals. This writer does not authenticate source amounts or automatically repair
    an existing wrong supplied-form ID.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: writer22
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata
  accessed_at: '2026-10-28T13:21:00.076352Z'
  support: context_only
  summary: Current DSMZCompositionResolver.merge_composition copies ingredients and
    solutions, fills pH when absent and copies physical/medium type, but does not
    copy preparation steps. _add_enrichment_metadata records a naive current timestamp.
    This explains a present omission risk, not historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer23
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T13:21:00.076375Z'
  support: context_only
  summary: Current _convert_to_culturemech constructs source notes and default LIQUID
    with empty ingredients. Its time.strftime format contains %f, which is unsupported
    here and is consistent with literal .fZ in stored import events. Current code
    does not authenticate the original retrieval or justify rewriting historical time.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer24
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps
  accessed_at: '2026-10-28T13:21:00.076404Z'
  support: context_only
  summary: Current _parse_api_composition considers the primary recipe, prefers provider
    g_l when available and excludes four recognized water labels; tap water is not
    among those exclusions; _is_api_stock_addition distinguishes stock additions.
    _parse_api_solutions retains separate stock structure. _parse_preparation_steps
    collects solution prose. These present behaviors do not establish historical execution
    and cannot justify interpreting flattened stock rates as final-medium concentrations.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer25
  kind: record_content
  reference: src/culturemech/match/kg_media_matcher.py
  locator: extract_recipe_ingredients; find_matches; find_exact_match
  accessed_at: '2026-10-28T13:21:00.076432Z'
  support: context_only
  summary: Current extract_recipe_ingredients collects asserted CHEBI/FOODON IDs,
    find_matches compares set Jaccard and find_exact_match selects the first exact
    identifier set. Quantities, preparation and ungrounded ingredients are not compared,
    so an exact set match does not establish formulation identity.
  snapshot_sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
- evidence_id: writer26
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T13:21:00.076454Z'
  support: context_only
  summary: Current formulation_content retains exact scientific quantities, preparation
    and other scientific fields; merge_formulation_evidence rejects incompatible projections
    and unions evidence at matching scopes. A source-equivalence claim is not established
    by shared ingredient identities.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer27
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations; group_recipes
  accessed_at: '2026-10-28T13:21:00.076476Z'
  support: context_only
  summary: Current group_formulations calls group_recipes with fail_on_invalid=True
    and FormulationFingerprinter. Expected standalone or unfingerprintable records
    are excluded; malformed or unexpected inputs raise. Valid records are grouped
    by full scientific content. This guard does not retrieve or authenticate source
    recipes.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer28
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T13:21:00.076501Z'
  support: context_only
  summary: Current merge_group routes a single maintained owner with merge metadata;
    multiple owners pass through conservative merge_formulation_evidence. Regenerating
    from an unrepaired owner retains its defects. Current conservative behavior is
    credited and does not establish how the old generated record was produced.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: hepes-current-mim
  kind: authority
  reference: REVIEW_WORK/batch068/record06/hepes-mim-comparison.json
  locator: 'candidate_rows: CSV lines717,1140,1141,1154,4711-4715'
  accessed_at: '2026-10-28T13:21:00.087688Z'
  support: supports
  summary: Current exact MIM identifier-key search has no CHEBI:46756 row; the exact
    HEPES preferred-term rows instead point to CHEBI:42334, whose current OLS object
    identifies the neutral acid. This is a current-snapshot linkage distinction, not
    proof the historical assertion was invalid.
  snapshot_sha256: d53f104fce7471599147f380ef4cde6fc9b65c15be8bc08c8fe78b9ad3e4f49f
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch068/record06/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T13:21:00.088046Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: a9e1fb9bed4465b4d95ee858b3fcde2727a9aa1925c8f585f73755b9982a67fe
assessments:
- assessment_id: a1
  area: identity
  topic: Exact source and existing scientific content
  outcome: supported
  summary: DSM1542 CY/H liquid medium is the exact source. Both selected layers retain
    liquid/complex/undefined classification, source pH and full staged preparation
    prose. The generic myxobacterial title does not identify one strain or constitute
    experimental growth evidence.
  target_ids:
  - CultureMech:001020
  evidence_ids:
  - local0
  - local1
  - dsm1542
  - api1542
- assessment_id: a2
  area: evidence
  topic: Existing claims and historical stock interpretation
  outcome: concern
  summary: Neither selected layer has attached formulation claims. The historical
    API raw digest and seventeen quoted source objects match current bytes, but the
    old blanket conflict labels are too broad for the eight source-A rates. Those
    eight numbers have supported A-stage values while their flat final-medium basis
    is unresolved; the two stock-strength main entries are distinct stage conflicts.
  target_ids:
  - CultureMech:001020
  evidence_ids:
  - local0
  - local1
  - history-auth
  - api1542
- assessment_id: a3
  area: grounding
  topic: Exact forms and current MIM distinction
  outcome: concern
  summary: Calcium dihydrate, magnesium heptahydrate, D-glucose and starch labels
    agree with the source scope. Generic vitamin B12 is appropriately a class; do
    not infer cyanocobalamin or accept a unique molar mass from provider mmol_l. Fe(III)-EDTA
    resolves to the complex anion, without an established counterion or hydrate; no
    forced salt replacement. HEPES46756 is an active OLS class without a formula and
    is not an exact current MIM identifier key; the neutral acid 42334 is a verified
    candidate, not an automatic substitution.
  target_ids:
  - CultureMech:001020
  evidence_ids:
  - grounding
  - chebi176843
  - chebi30729
  - chebi46756
  - chebi42334
  - hepes-current-mim
- assessment_id: a4
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: All three historical reports were fully read. Current API1542 exactly authenticates
    the cited old payload and seventeen source objects, without proving historical
    execution. The single-owner target retains the owner scientific fields. The current
    MediaDive importer separates main ingredients from referenced stock descriptors;
    its present behavior is credited and does not repair already flattened data or
    establish stock final-volume arithmetic. Current conservative merging preserves
    scientific fields and rejects incompatible formulations. Inspected writer behavior
    is described separately by exact file and function; it does not prove historical
    execution.
  target_ids:
  - CultureMech:001020
  evidence_ids:
  - history-auth
  - writer21
  - writer22
  - writer23
  - writer24
  - writer25
  - writer26
  - writer27
  - writer28
- assessment_id: a5
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 20 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:001020
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:001020",
    "selected_concentration_field_count": 20, "selected_concentration_fields_covered":
    20, "decisions": [{"decision_id": "q1", "subject": "Casitone", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Supported solution A basis;
    unestablished final assembled-medium basis", "interpretation": "The current number
    and supplied form are supported as an explicit provider solution-A g_l and as
    the primary solution-A batch input. The flat final-medium placement loses that
    stage; it is not a demonstrated numerical contradiction. Source A lists 1000 ml
    water, then receives 1 ml each of B and C per liter A. No measured final mixture
    volume is specified, so neither 1 L nor 1.002 L final is inferred. Keep these
    amounts at their source A stage; no unsupported renormalization.", "sources":
    [{"locator": "$.data.solutions[1].recipe[0]", "source_key": "api1542", "reference":
    "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Casitone\",\n                        \"compound_id\":
    84,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 4-4", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Casiton                                                            1.5       g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 12-12", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled
    water                                                 1000.0      ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at":
    "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter
    sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution
    C per liter solution A.\"\n                    }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q2", "subject": "Yeast extract", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Supported solution A basis;
    unestablished final assembled-medium basis", "interpretation": "The current number
    and supplied form are supported as an explicit provider solution-A g_l and as
    the primary solution-A batch input. The flat final-medium placement loses that
    stage; it is not a demonstrated numerical contradiction. Source A lists 1000 ml
    water, then receives 1 ml each of B and C per liter A. No measured final mixture
    volume is specified, so neither 1 L nor 1.002 L final is inferred. Keep these
    amounts at their source A stage; no unsupported renormalization.", "sources":
    [{"locator": "$.data.solutions[1].recipe[1]", "source_key": "api1542", "reference":
    "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 5-5", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Yeast extract                                                      1.5       g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 12-12", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled
    water                                                 1000.0      ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at":
    "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter
    sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution
    C per liter solution A.\"\n                    }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q3", "subject": "Starch", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml", "field_path":
    "ingredients[2].concentration", "original": {"value": "4", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "4", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Supported solution A basis;
    unestablished final assembled-medium basis", "interpretation": "The current number
    and supplied form are supported as an explicit provider solution-A g_l and as
    the primary solution-A batch input. The flat final-medium placement loses that
    stage; it is not a demonstrated numerical contradiction. Source A lists 1000 ml
    water, then receives 1 ml each of B and C per liter A. No measured final mixture
    volume is specified, so neither 1 L nor 1.002 L final is inferred. Keep these
    amounts at their source A stage; no unsupported renormalization.", "sources":
    [{"locator": "$.data.solutions[1].recipe[2]", "source_key": "api1542", "reference":
    "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Starch\",\n                        \"compound_id\":
    199,\n                        \"amount\": 4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 6-6", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Starch                                                             4.0       g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 12-12", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled
    water                                                 1000.0      ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at":
    "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter
    sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution
    C per liter solution A.\"\n                    }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q4", "subject": "Soy flour", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Supported solution A basis;
    unestablished final assembled-medium basis", "interpretation": "The current number
    and supplied form are supported as an explicit provider solution-A g_l and as
    the primary solution-A batch input. The flat final-medium placement loses that
    stage; it is not a demonstrated numerical contradiction. Source A lists 1000 ml
    water, then receives 1 ml each of B and C per liter A. No measured final mixture
    volume is specified, so neither 1 L nor 1.002 L final is inferred. Keep these
    amounts at their source A stage; no unsupported renormalization.", "sources":
    [{"locator": "$.data.solutions[1].recipe[3]", "source_key": "api1542", "reference":
    "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Soy flour\",\n                        \"compound_id\":
    1405,\n                        \"condition\": \"defatted\",\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsm1542",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Soy flour,
    defatted                                                1.0       g", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text lines 12-12", "source_key":
    "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled
    water                                                 1000.0      ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at":
    "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter
    sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution
    C per liter solution A.\"\n                    }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q5", "subject": "D-Glucose", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Supported solution A basis;
    unestablished final assembled-medium basis", "interpretation": "The current number
    and supplied form are supported as an explicit provider solution-A g_l and as
    the primary solution-A batch input. The flat final-medium placement loses that
    stage; it is not a demonstrated numerical contradiction. Source A lists 1000 ml
    water, then receives 1 ml each of B and C per liter A. No measured final mixture
    volume is specified, so neither 1 L nor 1.002 L final is inferred. Keep these
    amounts at their source A stage; no unsupported renormalization.", "sources":
    [{"locator": "$.data.solutions[1].recipe[4]", "source_key": "api1542", "reference":
    "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\":
    211,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    5.55062,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 8-8", "source_key": "dsm1542",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "D-Glucose                                                          1.0       g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 12-12", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled
    water                                                 1000.0      ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at":
    "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter
    sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution
    C per liter solution A.\"\n                    }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q6", "subject": "CaCl 2 x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Supported solution A basis;
    unestablished final assembled-medium basis", "interpretation": "The current number
    and supplied form are supported as an explicit provider solution-A g_l and as
    the primary solution-A batch input. The flat final-medium placement loses that
    stage; it is not a demonstrated numerical contradiction. Source A lists 1000 ml
    water, then receives 1 ml each of B and C per liter A. No measured final mixture
    volume is specified, so neither 1 L nor 1.002 L final is inferred. Keep these
    amounts at their source A stage; no unsupported renormalization.", "sources":
    [{"locator": "$.data.solutions[1].recipe[5]", "source_key": "api1542", "reference":
    "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    6.80203,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 9-9", "source_key": "dsm1542",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "CaCl 2 X
    2 H2O                                                     1.0       g", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text lines 12-12", "source_key":
    "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled
    water                                                 1000.0      ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at":
    "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter
    sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution
    C per liter solution A.\"\n                    }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q7", "subject": "MgSO4 x 7 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Supported solution A basis;
    unestablished final assembled-medium basis", "interpretation": "The current number
    and supplied form are supported as an explicit provider solution-A g_l and as
    the primary solution-A batch input. The flat final-medium placement loses that
    stage; it is not a demonstrated numerical contradiction. Source A lists 1000 ml
    water, then receives 1 ml each of B and C per liter A. No measured final mixture
    volume is specified, so neither 1 L nor 1.002 L final is inferred. Keep these
    amounts at their source A stage; no unsupported renormalization.", "sources":
    [{"locator": "$.data.solutions[1].recipe[6]", "source_key": "api1542", "reference":
    "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.02859,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 10-10", "source_key": "dsm1542",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "MgSO 4 x
    7 H2O                                                     0.5       g", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text lines 12-12", "source_key":
    "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled
    water                                                 1000.0      ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at":
    "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter
    sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution
    C per liter solution A.\"\n                    }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q8", "subject": "HEPES", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml", "field_path":
    "ingredients[7].concentration", "original": {"value": "11.9", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "11.9", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Supported solution A basis;
    unestablished final assembled-medium basis", "interpretation": "The current number
    and supplied form are supported as an explicit provider solution-A g_l and as
    the primary solution-A batch input. The flat final-medium placement loses that
    stage; it is not a demonstrated numerical contradiction. Source A lists 1000 ml
    water, then receives 1 ml each of B and C per liter A. No measured final mixture
    volume is specified, so neither 1 L nor 1.002 L final is inferred. Keep these
    amounts at their source A stage; no unsupported renormalization.", "sources":
    [{"locator": "$.data.solutions[1].recipe[7]", "source_key": "api1542", "reference":
    "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"HEPES\",\n                        \"compound_id\":
    371,\n                        \"amount\": 11.9,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 11.9,\n                        \"mmol_l\":
    49.9371,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 11-11", "source_key": "dsm1542",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "HEPES                                                             11.9       g",
    "quote_representation": "captured extracted text"}, {"locator": "extracted-text
    lines 12-12", "source_key": "dsm1542", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled
    water                                                 1000.0      ml", "quote_representation":
    "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at":
    "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter
    sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution
    C per liter solution A.\"\n                    }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q9", "subject": "Fe(III)-EDTA", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "8", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "8", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Separate solution B stock", "interpretation":
    "The local 8 g/L iron complex or 0.5 g/L vitamin concentration belongs to the
    separate 100 ml provider stock, not a full-strength main ingredient. Primary stock
    inputs are 0.80 g iron complex or 0.05 g B12 with 100 ml water; preserve those
    batch inputs. API g_l 8/.5 are credited only as provider stock rates. Addition
    is 1 ml stock per liter A. On that declared stock-rate basis the inputs are 8
    mg iron complex or 0.5 mg B12 per liter A, not a measured final-medium concentration;
    final volume remains unresolved.", "sources": [{"locator": "$.data.solutions[2].recipe[0]",
    "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542",
    "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Fe(III)-EDTA\",\n                        \"compound_id\":
    952,\n                        \"amount\": 0.8,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 8,\n                        \"mmol_l\":
    23.252,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 15-15", "source_key": "dsm1542",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "EDTA-iron                                                         0.80       g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[2].recipe[1]",
    "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542",
    "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 100,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at":
    "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter
    sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution
    C per liter solution A.\"\n                    }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q10", "subject": "Vitamin B12", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Separate solution C stock", "interpretation":
    "The local 8 g/L iron complex or 0.5 g/L vitamin concentration belongs to the
    separate 100 ml provider stock, not a full-strength main ingredient. Primary stock
    inputs are 0.80 g iron complex or 0.05 g B12 with 100 ml water; preserve those
    batch inputs. API g_l 8/.5 are credited only as provider stock rates. Addition
    is 1 ml stock per liter A. On that declared stock-rate basis the inputs are 8
    mg iron complex or 0.5 mg B12 per liter A, not a measured final-medium concentration;
    final volume remains unresolved.", "sources": [{"locator": "$.data.solutions[3].recipe[0]",
    "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542",
    "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 0.05,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    0.368895,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 19-19", "source_key": "dsm1542",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Vitamin B12                                                       0.05       g",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[3].recipe[1]",
    "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542",
    "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 100,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at":
    "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter
    sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution
    C per liter solution A.\"\n                    }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q11", "subject": "Solution A water", "local_fields":
    [], "decision": "add", "stage": "Stock/base batch solvent", "interpretation":
    "Preserve the explicit 1000 ml water input for A and 100 ml water inputs for each
    B/C stock as volume. Listed water is not an independently established final stock
    or mixture volume. The provider normalization is documented separately.", "sources":
    [{"locator": "$.data.solutions[1].recipe[8]", "source_key": "api1542", "reference":
    "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 12-12", "source_key": "dsm1542",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled
    water                                                 1000.0      ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q12", "subject": "Solution B water",
    "local_fields": [], "decision": "add", "stage": "Stock/base batch solvent", "interpretation":
    "Preserve the explicit 1000 ml water input for A and 100 ml water inputs for each
    B/C stock as volume. Listed water is not an independently established final stock
    or mixture volume. The provider normalization is documented separately.", "sources":
    [{"locator": "$.data.solutions[2].recipe[1]", "source_key": "api1542", "reference":
    "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 100,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 16-16", "source_key": "dsm1542",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled
    water                                                  100.0      ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q13", "subject": "Solution C water",
    "local_fields": [], "decision": "add", "stage": "Stock/base batch solvent", "interpretation":
    "Preserve the explicit 1000 ml water input for A and 100 ml water inputs for each
    B/C stock as volume. Listed water is not an independently established final stock
    or mixture volume. The provider normalization is documented separately.", "sources":
    [{"locator": "$.data.solutions[3].recipe[1]", "source_key": "api1542", "reference":
    "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 100,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 16-16", "source_key": "dsm1542",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Distilled
    water                                                  100.0      ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q14", "subject": "Solution A assembly
    dose", "local_fields": [], "decision": "add", "stage": "Receiving mixture", "interpretation":
    "The API main assembly is 1000 ml A plus 1 ml B and 1 ml C; primary prose specifies
    each 1 ml addition per liter A. Represent each named solution and its receiving
    dose separately, with evidence at the enclosing recipe. Do not double-count the
    flattened stock constituents or treat a source solution volume as a universal
    dose.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key":
    "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at":
    "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\":
    3195,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at":
    "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter
    sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution
    C per liter solution A.\"\n                    }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q15", "subject": "Solution B assembly dose",
    "local_fields": [], "decision": "add", "stage": "Receiving mixture", "interpretation":
    "The API main assembly is 1000 ml A plus 1 ml B and 1 ml C; primary prose specifies
    each 1 ml addition per liter A. Represent each named solution and its receiving
    dose separately, with evidence at the enclosing recipe. Do not double-count the
    flattened stock constituents or treat a source solution volume as a universal
    dose.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key":
    "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at":
    "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\":
    3196,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at":
    "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter
    sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution
    C per liter solution A.\"\n                    }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q16", "subject": "Solution C assembly dose",
    "local_fields": [], "decision": "add", "stage": "Receiving mixture", "interpretation":
    "The API main assembly is 1000 ml A plus 1 ml B and 1 ml C; primary prose specifies
    each 1 ml addition per liter A. Represent each named solution and its receiving
    dose separately, with evidence at the enclosing recipe. Do not double-count the
    flattened stock constituents or treat a source solution volume as a universal
    dose.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key":
    "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at":
    "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\":
    3197,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542", "source_raw_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "source_text_sha256":
    "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047", "accessed_at":
    "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter
    sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution
    C per liter solution A.\"\n                    }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q17", "subject": "pH and full retained preparation",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml",
    "field_path": "ph_value", "original": 7.4}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml",
    "field_path": "ph_value", "original": 7.4}, {"record_path": "data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml",
    "field_path": "preparation_steps[0].description", "original": "Adjust pH of solution
    A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize vitamin
    solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution
    A."}, {"record_path": "data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml",
    "field_path": "preparation_steps[0].description", "original": "Adjust pH of solution
    A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize vitamin
    solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution
    A."}], "decision": "evidence_only", "stage": "Solution A adjustment; A/B heat
    and C filter stages", "interpretation": "pH7.4 belongs to solution A before assembly.
    The complete source description is retained in both target and owner and must
    be credited: A/B separately autoclaved, vitamin stock filtered, then additions
    after cooling. The single AUTOCLAVE action code captures only part of this compound
    procedure; the vitamin solution must not inherit that code as its sterilization
    method. No temperatures or times are supplied.", "sources": [{"locator": "$.data.solutions[0].steps[0]",
    "source_key": "api1542", "reference": "https://mediadive.dsmz.de/rest/medium/1542",
    "source_raw_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "source_text_sha256": "bbab9f918b48b42bb053c3ce4b83bd96f3f8d4ba1bf491ce642345a59f301047",
    "accessed_at": "2026-10-28T13:11:55.827403Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH of solution A to pH 7.4. Autoclave solutions A and B separately. Filter
    sterilize vitamin solution. After cooling, add 1 ml solution B and 1 ml solution
    C per liter solution A.\"\n                    }", "quote_representation": "raw
    JSON object"}, {"locator": "extracted-text lines 24-26", "source_key": "dsm1542",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1542.pdf",
    "source_raw_sha256": "12c3837bf18ab14c253feebd8551c3525888fdf90532f9082662baa99a9a0783",
    "source_text_sha256": "1491e78a5e18b4158545f4890257bc03443f9608373d1886c55f6ae0695ab249",
    "accessed_at": "2026-10-28T13:11:55.834453Z", "exact_source_quote": "Adjust pH
    of solution A to pH 7.4. Autoclave solutions A and B separately. Filter sterilize\nvitamin
    solution. After cooling, add 1 ml solution B and 1 ml solution C per liter solution\nA.",
    "quote_representation": "captured extracted text"}]}], "local_field_census_reference":
    "REVIEW_WORK/batch068/record06/grounding-inventory.json", "source_only_gaps_are_explicit":
    true, "note": "Batch amounts, provider normalization, stock composition, working
    dose and preparation controls are separate. No source edits or automatic curation
    performed."}'
- assessment_id: a6
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/CY_H_LIQUID_MEDIUM_FOR_MYXOBACTERIA.yaml: primary
    7/10, secondary 7/10; data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml:
    primary 7/10, secondary 7/10. These are ingredient-instance linkage fractions,
    not accuracy scores. Solution terms are audited separately. Every actually asserted
    CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows.
    0 numeric legacy MediaIngredientMech mentions occur across the complete selected
    documents, with exact locators in the inventory; NNNNNN is a historical placeholder,
    not an ID. Complex commercial/product components are not forced to pure-compound
    IDs.'
  target_ids:
  - CultureMech:001020
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
  - CultureMech:001020
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
  - CultureMech:001020
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-001020-source-stock-stage-collapse
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Separate A/B/C formulations are flattened into main-medium rates
  description: The source main assembly adds solution A with small B and C doses.
    Local iron-complex 8 g/L and B12 0.5 g/L are the provider stock rates, but appear
    as direct main ingredients. The other eight local values correspond to A and lack
    an established final-mixture denominator. The complete staged preparation prose
    is present and is credited.
  target_ids:
  - CultureMech:001020
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  evidence_ids:
  - dsm1542
  - api1542
  - local0
  - local1
  rule_id: review-yaml-record/stock-stage-and-denominator-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-001020-source-claim-evidence-gap
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Formulation and staged preparation lack attached source support
  description: Current sources support exact batch amounts, named stocks and procedures,
    but neither target nor maintained owner carries claim-level formulation evidence
    or references. A source URL in notes does not explain the currently flattened
    quantity scope.
  target_ids:
  - CultureMech:001020
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
  - references
  - evidence
  evidence_ids:
  - local0
  - local1
  - dsm1542
  - api1542
  rule_id: review-yaml-record/claim-scoped-evidence
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-001020-hepes-secondary-current-snapshot-gap
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: HEPES secondary linkage does not match the current MIM key
  description: Both layers assert CHEBI:46756 in primary and MIM-secondary slots.
    OLS confirms this active HEPES class, but the current packaged MIM index has no
    exact identifier-key row for 46756 and instead links the HEPES preferred term
    to 42334. This is a current correspondence gap, not an invalid ChEBI ID or historical-deprecation
    finding.
  target_ids:
  - CultureMech:001020
  field_paths:
  - ingredients[7].mediaingredientmech_chebi_term
  - ingredients[7].term
  evidence_ids:
  - chebi46756
  - chebi42334
  - hepes-current-mim
  - grounding
  rule_id: review-yaml-record/current-secondary-correspondence
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Represent the source A/B/C compositions, solvent volumes and receiving
    doses separately; retain correct A inputs and source stock rates only at their
    declared stages. Remove stock-strength claims from the final-medium ingredient
    interpretation without guessing final concentrations. Preserve the full existing
    preparation description and distinguish heat/filter/addition stages.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001020
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml
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
  description: Attach exact source excerpts to the appropriate ingredient composition
    fields, and receiving-dose/preparation evidence at the enclosing recipe with explicit
    paths and stages. Preserve all unchanged source-supported content; regenerate
    after the maintained stage model is corrected.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001020
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml
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
  description: Resolve the source HEPES form and current MIM mapping explicitly, retaining
    a class-level primary assertion if only that granularity is supported. Do not
    overwrite both slots automatically from a label match. Preserve prior mapping
    events and record current-snapshot evidence.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001020
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cy_h_liquid_medium_for_myxobacteria.yaml
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
- Primary solution water inputs and provider volume metadata do not establish measured
  final stock or assembled-medium volumes. No 1.002 L denominator is inferred.
- Exact Fe-EDTA counterion/hydrate and vitamin B12 vitamer are not specified. Broad
  ontology classes are retained; no unsupported mass-to-molar conversion or forced
  supplied-form mapping.
- Current MIM identifier-key absence is bounded to the pinned snapshot and does not
  imply historical invalidity. No numerical legacy MIM identifiers occur in these
  complete selected documents.
- Native references checked zero objects. Current writers describe present behavior
  only; no source records were changed.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
