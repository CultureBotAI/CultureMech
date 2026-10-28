# Scientific review of capnocytophaga_medium

- Review: 20261028T071507Z-capnocytophaga-medium-batch059
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T06:48:40.437845Z
- Finished UTC: 2026-10-28T07:15:07.766158Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM 459 identity and the six declared provider rates are supported. The review preserves uncertainty about final solvent volume while identifying missing water/default preparation evidence and a deprecated potassium-nitrate secondary link.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch059 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002808 | data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml | generated | capnocytophaga_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002808 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:002808 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:002808 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:002808 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact JCM 459 identity

identity: supported. Targets: CultureMech:002808.

Current JCM 459 and APIJ459 identify the same complex liquid medium, with matching component identity and pH. The genus name alone is not evidence for a named strain or an experimentally demonstrated growth claim. No organism-specific claim is added.

### Historical source claims and denominator limits

evidence: concern. Targets: CultureMech:002808.

The four complete historical reports were read. Current API digest and exact row joins are checked separately. Earlier blanket conflict labels reflect unresolved glucose solvent accounting, not a contradicted mass: current provider g_l matches each local rate. The September recommendation to encode water per final litre is not adopted without an explicit final-volume basis. Its standalone4206 suggestion remains outside this target/owner review; no automatic transfer or recertification of that separate record is claimed.

### Current importer and conservative merger

provenance: supported. Targets: CultureMech:002808.

Current MediaDive importer deliberately omits water from composition edges, so the missing solvent should be preserved as preparation context. It keeps primary recipe rows and declared g_l; its API preparation cannot recover the JCM page-wide default absent from that payload. Current merger retains compatible scientific fields. Present code is not evidence of the old import execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:002808.

All 12 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:002808", "selected_concentration_field_count": 12, "selected_concentration_fields_covered": 12, "decisions": [{"decision_id": "q1", "subject": "Trypticase peptone", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "17", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "17", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and explicit provider-normalized rate", "interpretation": "JCM 459 lists 17 g in the stated batch; current API explicitly declares 17 g/L, matching the local amount. Preserve that declared normalization with its provenance. separate glucose sterilization leaves its solvent accounting unspecified, so listed 1 L water alone is not proof of measured final volume. No numeric correction is inferred.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "apiJ459", "reference": "https://mediadive.dsmz.de/rest/medium/J459", "source_raw_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "source_text_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "accessed_at": "2026-10-28T06:49:23.766737Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\": 124,\n                        \"attribute\": \"BD-BBL\",\n                        \"amount\": 17,\n                        \"unit\": \"g\",\n                        \"g_l\": 17,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[0]", "source_key": "jcm459", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459", "source_raw_sha256": "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503", "source_text_sha256": "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f", "accessed_at": "2026-10-28T06:49:23.766409Z", "exact_source_quote": "Trypticase peptone (BD-BBL)\n17.0\ng", "quote_representation": "HTML tr[0] DOM text"}]}, {"decision_id": "q2", "subject": "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "3", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and explicit provider-normalized rate", "interpretation": "JCM 459 lists 3 g in the stated batch; current API explicitly declares 3 g/L, matching the local amount. Preserve that declared normalization with its provenance. separate glucose sterilization leaves its solvent accounting unspecified, so listed 1 L water alone is not proof of measured final volume. No numeric correction is inferred.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "apiJ459", "reference": "https://mediadive.dsmz.de/rest/medium/J459", "source_raw_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "source_text_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "accessed_at": "2026-10-28T06:49:23.766737Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[1]", "source_key": "jcm459", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459", "source_raw_sha256": "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503", "source_text_sha256": "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f", "accessed_at": "2026-10-28T06:49:23.766409Z", "exact_source_quote": "Yeast extract (BD-Difco)\n3.0\ng", "quote_representation": "HTML tr[1] DOM text"}]}, {"decision_id": "q3", "subject": "Glucose", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "3", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and explicit provider-normalized rate", "interpretation": "JCM 459 lists 3 g in the stated batch; current API explicitly declares 3 g/L, matching the local amount. Preserve that declared normalization with its provenance. separate glucose sterilization leaves its solvent accounting unspecified, so listed 1 L water alone is not proof of measured final volume. No numeric correction is inferred.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "apiJ459", "reference": "https://mediadive.dsmz.de/rest/medium/J459", "source_raw_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "source_text_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "accessed_at": "2026-10-28T06:49:23.766737Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 16.6519,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[2]", "source_key": "jcm459", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459", "source_raw_sha256": "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503", "source_text_sha256": "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f", "accessed_at": "2026-10-28T06:49:23.766409Z", "exact_source_quote": "Glucose\n3.0\ng", "quote_representation": "HTML tr[2] DOM text"}]}, {"decision_id": "q4", "subject": "NaCl", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "3", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and explicit provider-normalized rate", "interpretation": "JCM 459 lists 3 g in the stated batch; current API explicitly declares 3 g/L, matching the local amount. Preserve that declared normalization with its provenance. separate glucose sterilization leaves its solvent accounting unspecified, so listed 1 L water alone is not proof of measured final volume. No numeric correction is inferred.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key": "apiJ459", "reference": "https://mediadive.dsmz.de/rest/medium/J459", "source_raw_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "source_text_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "accessed_at": "2026-10-28T06:49:23.766737Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 51.3347,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[3]", "source_key": "jcm459", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459", "source_raw_sha256": "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503", "source_text_sha256": "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f", "accessed_at": "2026-10-28T06:49:23.766409Z", "exact_source_quote": "NaCl\n3.0\ng", "quote_representation": "HTML tr[3] DOM text"}]}, {"decision_id": "q5", "subject": "KNO3", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "3", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and explicit provider-normalized rate", "interpretation": "JCM 459 lists 3 g in the stated batch; current API explicitly declares 3 g/L, matching the local amount. Preserve that declared normalization with its provenance. separate glucose sterilization leaves its solvent accounting unspecified, so listed 1 L water alone is not proof of measured final volume. No numeric correction is inferred.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "apiJ459", "reference": "https://mediadive.dsmz.de/rest/medium/J459", "source_raw_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "source_text_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "accessed_at": "2026-10-28T06:49:23.766737Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KNO3\",\n                        \"compound_id\": 191,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 29.6727,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[4]", "source_key": "jcm459", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459", "source_raw_sha256": "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503", "source_text_sha256": "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f", "accessed_at": "2026-10-28T06:49:23.766409Z", "exact_source_quote": "KNO\n3\n3.0\ng", "quote_representation": "HTML tr[4] DOM text"}]}, {"decision_id": "q6", "subject": "Hemin", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and explicit provider-normalized rate", "interpretation": "JCM 459 lists 3 mg in the stated batch; current API explicitly declares 0.003 g/L, matching the local amount. Preserve that declared normalization with its provenance. The hemin mass conversion is 3 mg = 0.003 g; separate glucose sterilization leaves its solvent accounting unspecified, so listed 1 L water alone is not proof of measured final volume. No numeric correction is inferred.", "sources": [{"locator": "$.data.solutions[0].recipe[5]", "source_key": "apiJ459", "reference": "https://mediadive.dsmz.de/rest/medium/J459", "source_raw_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "source_text_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "accessed_at": "2026-10-28T06:49:23.766737Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Hemin\",\n                        \"compound_id\": 704,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.00460193,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[5]", "source_key": "jcm459", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459", "source_raw_sha256": "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503", "source_text_sha256": "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f", "accessed_at": "2026-10-28T06:49:23.766409Z", "exact_source_quote": "Hemin\n3.0\nmg", "quote_representation": "HTML tr[5] DOM text"}]}, {"decision_id": "q7", "subject": "Main preparation water", "local_fields": [], "decision": "evidence_only", "stage": "absolute solvent input", "interpretation": "JCM lists 1.0 L distilled water and API 1000 ml. Preserve the absolute preparation input; do not replace it by an unsupported 1000 ml per final litre or count it as a nutrient.", "sources": [{"locator": "$.data.solutions[0].recipe[6]", "source_key": "apiJ459", "reference": "https://mediadive.dsmz.de/rest/medium/J459", "source_raw_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "source_text_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "accessed_at": "2026-10-28T06:49:23.766737Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "HTML tr[6]", "source_key": "jcm459", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459", "source_raw_sha256": "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503", "source_text_sha256": "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f", "accessed_at": "2026-10-28T06:49:23.766409Z", "exact_source_quote": "Distilled water\n1.0\nL", "quote_representation": "HTML tr[6] DOM text"}]}, {"decision_id": "q8", "subject": "pH", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path": "ph_value", "original": 7.0}, {"record_path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path": "preparation_steps[0].description", "original": "Adjust pH to 7.0."}, {"record_path": "data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path": "preparation_steps[0].description", "original": "Adjust pH to 7.0."}], "decision": "verified", "stage": "medium pH adjustment", "interpretation": "Existing pH 7.0 and adjustment instruction match both sources.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "apiJ459", "reference": "https://mediadive.dsmz.de/rest/medium/J459", "source_raw_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "source_text_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "accessed_at": "2026-10-28T06:49:23.766737Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 7.0.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 28-28", "source_key": "jcm459", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459", "source_raw_sha256": "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503", "source_text_sha256": "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f", "accessed_at": "2026-10-28T06:49:23.766409Z", "exact_source_quote": "Adjust pH to 7.0.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject": "Separate glucose and incubation atmosphere", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path": "preparation_steps[1].description", "original": "Autoclave glucose solution separately. Incubate under an oxygen-free atmosphere containing 5-10% CO2."}, {"record_path": "data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path": "preparation_steps[1].description", "original": "Autoclave glucose solution separately. Incubate under an oxygen-free atmosphere containing 5-10% CO2."}], "decision": "verified", "stage": "distinct sterilization and incubation stages", "interpretation": "Retain separate glucose sterilization and oxygen-free atmosphere containing 5–10% CO2. The remaining gas identity, glucose stock strength/volume and organism-specific growth are not supplied and are not invented. Split the combined action into explicit stages when curating.", "sources": [{"locator": "$.data.solutions[0].steps[1]", "source_key": "apiJ459", "reference": "https://mediadive.dsmz.de/rest/medium/J459", "source_raw_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "source_text_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "accessed_at": "2026-10-28T06:49:23.766737Z", "exact_source_quote": "{\n                        \"step\": \"Autoclave glucose solution separately. Incubate under an oxygen-free atmosphere containing 5-10% CO2.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 29-31", "source_key": "jcm459", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459", "source_raw_sha256": "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503", "source_text_sha256": "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f", "accessed_at": "2026-10-28T06:49:23.766409Z", "exact_source_quote": "Autoclave glucose solution separately. Incubate under an oxygen-free atmosphere containing 5-10% CO\n2\n.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q10", "subject": "Source default sterilization", "local_fields": [], "decision": "evidence_only", "stage": "source-wide preparation default", "interpretation": "JCM explicitly supplies the default 121°C for 15 min unless otherwise stated; retain it at the appropriate preparation stage alongside the specific separate-glucose instruction. This is source guidance, not a measured growth result.", "sources": [{"locator": "extracted-text lines 4-4", "source_key": "jcm459", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459", "source_raw_sha256": "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503", "source_text_sha256": "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f", "accessed_at": "2026-10-28T06:49:23.766409Z", "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.", "quote_representation": "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch059/record04/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:002808.

data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml: primary 4/6, secondary 3/6; data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml: primary 4/6, secondary 3/6. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 2 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:002808.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:002808.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Source water, sterilization default and claim-level evidence are incomplete

major / open / confirmed; issue key: culturemech-002808-missing-preparation-water-default-and-evidence.

The current JCM source and API retain the absolute water input, but both selected layers omit it. The JCM default sterilization conditions are absent; the present pH, separate-glucose and incubation atmosphere wording is supported. Neither selected layer attaches claim-level source evidence.

### f2: A deprecated secondary identifier remains on potassium nitrate

minor / open / confirmed; issue key: culturemech-002808-legacy-potassium-nitrate-secondary-link.

KNO3 primary CHEBI:63043 is correct and matches the source and current OLS potassium nitrate object. Its secondary MediaIngredientMech:000170 is absent from the complete current packaged label index. This current negative does not prove the old identifier never existed. Glucose, sodium chloride and hemin primary/secondary correspondences are supported.

## Recommended Actions And Acceptance Checks

### action1

Retain the absolute source water and appropriately scoped source default in maintained preparation, preserving the existing correct specific steps. Add short exact evidence at root for preparation and ingredient scope for quantities. Do not infer glucose stock strength or final solvent volume.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Resolve and replace the deprecated secondary linkage using the verified current CHEBI-keyed correspondence; preserve the correct primary ID, supported amount and original history. Append a new dated context event only when an actual correction is made.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch059/record04/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch059/record04/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch059/record04/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch059/record04/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| jcm459 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current official JCM page read, including the main and embedded stock tables, preparation and source-specific defaults. The page-wide default remains scoped to that source; named stock sections are separate from main-medium preparation. |
| apiJ459 | https://mediadive.dsmz.de/rest/medium/J459; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17234 = glucose; definition ['An aldohexose used as a source of energy and metabolic intermediate.']; formula ['C6H12O6']; mass ['180.156']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi50385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50385; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:50385 = hemin; definition ['It is used as a prescription medication to relieve repeated attacks of acute intermittent porphyria related to the menstrual cycle in affected women.']; formula ['C34H32ClFeN4O4']; mass ['651.952']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63043 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63043; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63043 = potassium nitrate; definition ['The inorganic nitrate salt of potassium.']; formula ['K.NO3']; mass ['101.102']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch059/record04/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/yaml_record_review/20260922T032851Z-CAPNOCYTOPHAGA_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history1 | reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current apiJ459 raw bytes exactly match the cited historical SHA, and 9 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history3 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch059/record04/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer18 | scripts/apply_mim_groundings.py; relevant functions named in summary | context_only | target_slot preserves existing CHEBI assertions, groundable excludes conflicting corpus opinions and apply_to_record fills only ungrounded names. This current CHEBI-only writer does not automatically replace deprecated secondary MIM links or authenticate quantities. |
| writer19 | src/culturemech/import/mediadive_importer.py; relevant functions named in summary | context_only | Current _parse_api_composition restricts direct ingredients to primary recipe, skips stock additions and water, and prefers provider g_l; _parse_api_solutions preserves referenced/percent stocks. This limits the old flattening attribution; water needs preparation-volume representation and historical run provenance remains separate. |
| writer20 | src/culturemech/merge/formulation.py; relevant functions named in summary | context_only | Current formulation_content retains scientific fields, quantities, notes and preparation; merge_formulation_evidence rejects incompatible scientific projections and unions scoped evidence. Ingredient-set similarity does not prove scientific equivalence. |
| writer21 | src/culturemech/merge/matcher.py; relevant functions named in summary | context_only | Current group_formulations uses full formulation fingerprints for compatible automatic merging; broader group_recipes discovers ingredient-set candidates only. Neither grouping path substitutes for source verification. |
| writer22 | src/culturemech/merge/merger.py; relevant functions named in summary | context_only | Current merge_group returns a single owner with routing metadata, and calls conservative merge_formulation_evidence for multiple owners. Current code supports regenerating stale content after owner repair but does not authenticate old generated outputs. |
| quantity-inventory | REVIEW_WORK/batch059/record04/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- No named strain or growth outcome is established by the recipe title. Collection instructions are formulation context only.
- Current MIM absence does not invalidate historical identifier use; complex commercial ingredients are not forced into pure-compound ontology terms.
- The separately autoclaved glucose solution has no stated strength or solvent volume. No measured final-volume denominator or unprovided gas identity is inferred.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T071507Z-capnocytophaga-medium-batch059
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of capnocytophaga_medium
started_at: '2026-10-28T06:48:40.437845Z'
finished_at: '2026-10-28T07:15:07.766158Z'
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
summary: JCM 459 identity and the six declared provider rates are supported. The review
  preserves uncertainty about final solvent volume while identifying missing water/default
  preparation evidence and a deprecated potassium-nitrate secondary link.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
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
  - path: data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml
    sha256: 70a6b2d3cb5ae8794c01b265a15f6c8407bde587a220b9caa6c709babb3bab57
    role: target
  - path: data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml
    sha256: 219987c0b1f67af1f2f0d3d0bdd6045769f7fc85d1ead4949aa210047b08fb7c
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml.md
    sha256: cd826d3f3c494c3946fe34377efc8403cac951b02a2e0fa708bdc94a152c04f8
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.md
    sha256: 54df28bca789eee4432647711d8ed0119773c9441ba305d52be49274b8774f77
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.md
    sha256: 419c8da1ee573ef88ac67ba27a4283d6316bb9306b1c0c744cb512337dcd5cbb
    role: context
  - path: reports/yaml_record_review/20260922T032851Z-CAPNOCYTOPHAGA_MEDIUM.md
    sha256: 24df1ec9964742890cc89ea1f4bb399f84d4192decf99360894e141e45dbca66
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
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
  description: Full selected target and maintained owners, every quantity and unchanged
    claim; separately scoped source dependencies and current writers.
  selection: Authoritative batch059 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:002808
targets:
- target_id: CultureMech:002808
  path: data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml
  label: capnocytophaga_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:002808
  command: just validate-schema data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:002808
  command: just validate-strict data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml
    --workers 1 --out REVIEW_WORK/batch059/record04/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:002808
  command: just validate-terms data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:002808
  command: just validate-references data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T06:52:38.109751Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 70a6b2d3cb5ae8794c01b265a15f6c8407bde587a220b9caa6c709babb3bab57
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T06:52:38.109905Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 219987c0b1f67af1f2f0d3d0bdd6045769f7fc85d1ead4949aa210047b08fb7c
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch059/record04/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T06:48:41.490057Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: f2d4536f758029e5d1c58764a59c03451db50ce783bf9862284d61ce10cba225
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch059/record04/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T06:48:42.459715Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: a4e20c96a7351d269c2f3a0e5d675438f9a060429127026fce8881c4fc186d36
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch059/record04/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T06:48:43.523164Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: abf405831fa0eac1e7a2d79fddecea8792c1a347045b1234d802afb794801a93
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch059/record04/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T06:48:44.210493Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: fcd0d585ee11303393ea65427a172866c92b2169dd1aeaead4d9a5682be9cf5f
- evidence_id: jcm459
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:49:23.766409Z'
  support: supports
  summary: Complete current official JCM page read, including the main and embedded
    stock tables, preparation and source-specific defaults. The page-wide default
    remains scoped to that source; named stock sections are separate from main-medium
    preparation.
  snapshot_sha256: fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503
- evidence_id: apiJ459
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J459
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T06:49:23.766737Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: 0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865
- evidence_id: chebi17234
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:23.766821Z'
  support: supports
  summary: OLS current exact CHEBI:17234 = glucose; definition ['An aldohexose used
    as a source of energy and metabolic intermediate.']; formula ['C6H12O6']; mass
    ['180.156']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:23.766880Z'
  support: supports
  summary: OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic
    chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass
    ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi50385
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50385
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:23.766925Z'
  support: supports
  summary: OLS current exact CHEBI:50385 = hemin; definition ['It is used as a prescription
    medication to relieve repeated attacks of acute intermittent porphyria related
    to the menstrual cycle in affected women.']; formula ['C34H32ClFeN4O4']; mass
    ['651.952']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: b989203634707b89526a8664c8fa65cb4976c4cdd791427218cf01b37d17356e
- evidence_id: chebi63043
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63043
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T06:49:23.766959Z'
  support: supports
  summary: OLS current exact CHEBI:63043 = potassium nitrate; definition ['The inorganic
    nitrate salt of potassium.']; formula ['K.NO3']; mass ['101.102']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: c324450e6330a169c708c32a7908b6df0276f4dc76da413e473b563928f61c13
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch059/record04/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T06:52:38.110737Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 09e2c4e4ef4440c4063828c497f92ae5322be51ddd7ef815ef9860ce6cf59891
- evidence_id: history0
  kind: prior_review
  reference: reports/yaml_record_review/20260922T032851Z-CAPNOCYTOPHAGA_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T06:52:38.111286Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 24df1ec9964742890cc89ea1f4bb399f84d4192decf99360894e141e45dbca66
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T06:52:38.111312Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current apiJ459 raw bytes exactly match the cited historical SHA, and 9
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: cd826d3f3c494c3946fe34377efc8403cac951b02a2e0fa708bdc94a152c04f8
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T06:52:38.111332Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 419c8da1ee573ef88ac67ba27a4283d6316bb9306b1c0c744cb512337dcd5cbb
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T06:52:38.111351Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 54df28bca789eee4432647711d8ed0119773c9441ba305d52be49274b8774f77
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch059/record04/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T06:52:38.111372Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: b6935bf7f5c8886ace3a8a20bcf9788569579bc669fe958bc4d833f9434c13dd
- evidence_id: writer18
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T06:52:38.111394Z'
  support: context_only
  summary: target_slot preserves existing CHEBI assertions, groundable excludes conflicting
    corpus opinions and apply_to_record fills only ungrounded names. This current
    CHEBI-only writer does not automatically replace deprecated secondary MIM links
    or authenticate quantities.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: writer19
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T06:52:38.111430Z'
  support: context_only
  summary: Current _parse_api_composition restricts direct ingredients to primary
    recipe, skips stock additions and water, and prefers provider g_l; _parse_api_solutions
    preserves referenced/percent stocks. This limits the old flattening attribution;
    water needs preparation-volume representation and historical run provenance remains
    separate.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer20
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T06:52:38.111449Z'
  support: context_only
  summary: Current formulation_content retains scientific fields, quantities, notes
    and preparation; merge_formulation_evidence rejects incompatible scientific projections
    and unions scoped evidence. Ingredient-set similarity does not prove scientific
    equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer21
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T06:52:38.111469Z'
  support: context_only
  summary: Current group_formulations uses full formulation fingerprints for compatible
    automatic merging; broader group_recipes discovers ingredient-set candidates only.
    Neither grouping path substitutes for source verification.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer22
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T06:52:38.111489Z'
  support: context_only
  summary: Current merge_group returns a single owner with routing metadata, and calls
    conservative merge_formulation_evidence for multiple owners. Current code supports
    regenerating stale content after owner repair but does not authenticate old generated
    outputs.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch059/record04/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T06:52:38.113581Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: df5958f9ab462440290f8dc60fa0122012406fe73ee81663c184179ce27cb394
assessments:
- assessment_id: a1
  area: identity
  topic: Exact JCM 459 identity
  outcome: supported
  summary: Current JCM 459 and APIJ459 identify the same complex liquid medium, with
    matching component identity and pH. The genus name alone is not evidence for a
    named strain or an experimentally demonstrated growth claim. No organism-specific
    claim is added.
  target_ids:
  - CultureMech:002808
  evidence_ids:
  - jcm459
  - apiJ459
  - local0
- assessment_id: a2
  area: evidence
  topic: Historical source claims and denominator limits
  outcome: concern
  summary: 'The four complete historical reports were read. Current API digest and
    exact row joins are checked separately. Earlier blanket conflict labels reflect
    unresolved glucose solvent accounting, not a contradicted mass: current provider
    g_l matches each local rate. The September recommendation to encode water per
    final litre is not adopted without an explicit final-volume basis. Its standalone4206
    suggestion remains outside this target/owner review; no automatic transfer or
    recertification of that separate record is claimed.'
  target_ids:
  - CultureMech:002808
  evidence_ids:
  - history-auth
  - jcm459
  - apiJ459
- assessment_id: a3
  area: provenance
  topic: Current importer and conservative merger
  outcome: supported
  summary: Current MediaDive importer deliberately omits water from composition edges,
    so the missing solvent should be preserved as preparation context. It keeps primary
    recipe rows and declared g_l; its API preparation cannot recover the JCM page-wide
    default absent from that payload. Current merger retains compatible scientific
    fields. Present code is not evidence of the old import execution.
  target_ids:
  - CultureMech:002808
  evidence_ids:
  - local0
  - writer18
  - writer19
  - writer20
  - writer21
  - writer22
- assessment_id: a4
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 12 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:002808
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:002808",
    "selected_concentration_field_count": 12, "selected_concentration_fields_covered":
    12, "decisions": [{"decision_id": "q1", "subject": "Trypticase peptone", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path":
    "ingredients[0].concentration", "original": {"value": "17", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "17", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and explicit provider-normalized
    rate", "interpretation": "JCM 459 lists 17 g in the stated batch; current API
    explicitly declares 17 g/L, matching the local amount. Preserve that declared
    normalization with its provenance. separate glucose sterilization leaves its solvent
    accounting unspecified, so listed 1 L water alone is not proof of measured final
    volume. No numeric correction is inferred.", "sources": [{"locator": "$.data.solutions[0].recipe[0]",
    "source_key": "apiJ459", "reference": "https://mediadive.dsmz.de/rest/medium/J459",
    "source_raw_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865",
    "source_text_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865",
    "accessed_at": "2026-10-28T06:49:23.766737Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\":
    124,\n                        \"attribute\": \"BD-BBL\",\n                        \"amount\":
    17,\n                        \"unit\": \"g\",\n                        \"g_l\":
    17,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[0]", "source_key": "jcm459", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459", "source_raw_sha256":
    "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503", "source_text_sha256":
    "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f", "accessed_at":
    "2026-10-28T06:49:23.766409Z", "exact_source_quote": "Trypticase peptone (BD-BBL)\n17.0\ng",
    "quote_representation": "HTML tr[0] DOM text"}]}, {"decision_id": "q2", "subject":
    "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and explicit provider-normalized
    rate", "interpretation": "JCM 459 lists 3 g in the stated batch; current API explicitly
    declares 3 g/L, matching the local amount. Preserve that declared normalization
    with its provenance. separate glucose sterilization leaves its solvent accounting
    unspecified, so listed 1 L water alone is not proof of measured final volume.
    No numeric correction is inferred.", "sources": [{"locator": "$.data.solutions[0].recipe[1]",
    "source_key": "apiJ459", "reference": "https://mediadive.dsmz.de/rest/medium/J459",
    "source_raw_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865",
    "source_text_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865",
    "accessed_at": "2026-10-28T06:49:23.766737Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\":
    3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    3,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[1]", "source_key": "jcm459", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459", "source_raw_sha256":
    "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503", "source_text_sha256":
    "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f", "accessed_at":
    "2026-10-28T06:49:23.766409Z", "exact_source_quote": "Yeast extract (BD-Difco)\n3.0\ng",
    "quote_representation": "HTML tr[1] DOM text"}]}, {"decision_id": "q3", "subject":
    "Glucose", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and explicit provider-normalized
    rate", "interpretation": "JCM 459 lists 3 g in the stated batch; current API explicitly
    declares 3 g/L, matching the local amount. Preserve that declared normalization
    with its provenance. separate glucose sterilization leaves its solvent accounting
    unspecified, so listed 1 L water alone is not proof of measured final volume.
    No numeric correction is inferred.", "sources": [{"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "apiJ459", "reference": "https://mediadive.dsmz.de/rest/medium/J459",
    "source_raw_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865",
    "source_text_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865",
    "accessed_at": "2026-10-28T06:49:23.766737Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\":
    5,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    16.6519,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[2]", "source_key": "jcm459", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459", "source_raw_sha256":
    "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503", "source_text_sha256":
    "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f", "accessed_at":
    "2026-10-28T06:49:23.766409Z", "exact_source_quote": "Glucose\n3.0\ng", "quote_representation":
    "HTML tr[2] DOM text"}]}, {"decision_id": "q4", "subject": "NaCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path":
    "ingredients[3].concentration", "original": {"value": "3", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and explicit provider-normalized
    rate", "interpretation": "JCM 459 lists 3 g in the stated batch; current API explicitly
    declares 3 g/L, matching the local amount. Preserve that declared normalization
    with its provenance. separate glucose sterilization leaves its solvent accounting
    unspecified, so listed 1 L water alone is not proof of measured final volume.
    No numeric correction is inferred.", "sources": [{"locator": "$.data.solutions[0].recipe[3]",
    "source_key": "apiJ459", "reference": "https://mediadive.dsmz.de/rest/medium/J459",
    "source_raw_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865",
    "source_text_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865",
    "accessed_at": "2026-10-28T06:49:23.766737Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    51.3347,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[3]", "source_key": "jcm459", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459", "source_raw_sha256":
    "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503", "source_text_sha256":
    "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f", "accessed_at":
    "2026-10-28T06:49:23.766409Z", "exact_source_quote": "NaCl\n3.0\ng", "quote_representation":
    "HTML tr[3] DOM text"}]}, {"decision_id": "q5", "subject": "KNO3", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path":
    "ingredients[4].concentration", "original": {"value": "3", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "3", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and explicit provider-normalized
    rate", "interpretation": "JCM 459 lists 3 g in the stated batch; current API explicitly
    declares 3 g/L, matching the local amount. Preserve that declared normalization
    with its provenance. separate glucose sterilization leaves its solvent accounting
    unspecified, so listed 1 L water alone is not proof of measured final volume.
    No numeric correction is inferred.", "sources": [{"locator": "$.data.solutions[0].recipe[4]",
    "source_key": "apiJ459", "reference": "https://mediadive.dsmz.de/rest/medium/J459",
    "source_raw_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865",
    "source_text_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865",
    "accessed_at": "2026-10-28T06:49:23.766737Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"KNO3\",\n                        \"compound_id\":
    191,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    29.6727,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[4]", "source_key": "jcm459", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459", "source_raw_sha256":
    "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503", "source_text_sha256":
    "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f", "accessed_at":
    "2026-10-28T06:49:23.766409Z", "exact_source_quote": "KNO\n3\n3.0\ng", "quote_representation":
    "HTML tr[4] DOM text"}]}, {"decision_id": "q6", "subject": "Hemin", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml", "field_path":
    "ingredients[5].concentration", "original": {"value": "0.003", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.003", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "main batch and explicit provider-normalized
    rate", "interpretation": "JCM 459 lists 3 mg in the stated batch; current API
    explicitly declares 0.003 g/L, matching the local amount. Preserve that declared
    normalization with its provenance. The hemin mass conversion is 3 mg = 0.003 g;
    separate glucose sterilization leaves its solvent accounting unspecified, so listed
    1 L water alone is not proof of measured final volume. No numeric correction is
    inferred.", "sources": [{"locator": "$.data.solutions[0].recipe[5]", "source_key":
    "apiJ459", "reference": "https://mediadive.dsmz.de/rest/medium/J459", "source_raw_sha256":
    "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "source_text_sha256":
    "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865", "accessed_at":
    "2026-10-28T06:49:23.766737Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Hemin\",\n                        \"compound_id\":
    704,\n                        \"amount\": 3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\":
    0.00460193,\n                        \"optional\": 0\n                    }",
    "quote_representation": "raw JSON object"}, {"locator": "HTML tr[5]", "source_key":
    "jcm459", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459",
    "source_raw_sha256": "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503",
    "source_text_sha256": "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f",
    "accessed_at": "2026-10-28T06:49:23.766409Z", "exact_source_quote": "Hemin\n3.0\nmg",
    "quote_representation": "HTML tr[5] DOM text"}]}, {"decision_id": "q7", "subject":
    "Main preparation water", "local_fields": [], "decision": "evidence_only", "stage":
    "absolute solvent input", "interpretation": "JCM lists 1.0 L distilled water and
    API 1000 ml. Preserve the absolute preparation input; do not replace it by an
    unsupported 1000 ml per final litre or count it as a nutrient.", "sources": [{"locator":
    "$.data.solutions[0].recipe[6]", "source_key": "apiJ459", "reference": "https://mediadive.dsmz.de/rest/medium/J459",
    "source_raw_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865",
    "source_text_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865",
    "accessed_at": "2026-10-28T06:49:23.766737Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "HTML tr[6]", "source_key": "jcm459", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459", "source_raw_sha256":
    "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503", "source_text_sha256":
    "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f", "accessed_at":
    "2026-10-28T06:49:23.766409Z", "exact_source_quote": "Distilled water\n1.0\nL",
    "quote_representation": "HTML tr[6] DOM text"}]}, {"decision_id": "q8", "subject":
    "pH", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml",
    "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml",
    "field_path": "ph_value", "original": 7.0}, {"record_path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml",
    "field_path": "preparation_steps[0].description", "original": "Adjust pH to 7.0."},
    {"record_path": "data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml",
    "field_path": "preparation_steps[0].description", "original": "Adjust pH to 7.0."}],
    "decision": "verified", "stage": "medium pH adjustment", "interpretation": "Existing
    pH 7.0 and adjustment instruction match both sources.", "sources": [{"locator":
    "$.data.solutions[0].steps[0]", "source_key": "apiJ459", "reference": "https://mediadive.dsmz.de/rest/medium/J459",
    "source_raw_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865",
    "source_text_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865",
    "accessed_at": "2026-10-28T06:49:23.766737Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH to 7.0.\"\n                    }", "quote_representation": "raw JSON
    object"}, {"locator": "extracted-text lines 28-28", "source_key": "jcm459", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459", "source_raw_sha256":
    "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503", "source_text_sha256":
    "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f", "accessed_at":
    "2026-10-28T06:49:23.766409Z", "exact_source_quote": "Adjust pH to 7.0.", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q9", "subject": "Separate glucose
    and incubation atmosphere", "local_fields": [{"record_path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml",
    "field_path": "preparation_steps[1].description", "original": "Autoclave glucose
    solution separately. Incubate under an oxygen-free atmosphere containing 5-10%
    CO2."}, {"record_path": "data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml",
    "field_path": "preparation_steps[1].description", "original": "Autoclave glucose
    solution separately. Incubate under an oxygen-free atmosphere containing 5-10%
    CO2."}], "decision": "verified", "stage": "distinct sterilization and incubation
    stages", "interpretation": "Retain separate glucose sterilization and oxygen-free
    atmosphere containing 5–10% CO2. The remaining gas identity, glucose stock strength/volume
    and organism-specific growth are not supplied and are not invented. Split the
    combined action into explicit stages when curating.", "sources": [{"locator":
    "$.data.solutions[0].steps[1]", "source_key": "apiJ459", "reference": "https://mediadive.dsmz.de/rest/medium/J459",
    "source_raw_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865",
    "source_text_sha256": "0e7fc88c6f0fc50222300a64918c6abd93e858d83d677813afbc402919bc3865",
    "accessed_at": "2026-10-28T06:49:23.766737Z", "exact_source_quote": "{\n                        \"step\":
    \"Autoclave glucose solution separately. Incubate under an oxygen-free atmosphere
    containing 5-10% CO2.\"\n                    }", "quote_representation": "raw
    JSON object"}, {"locator": "extracted-text lines 29-31", "source_key": "jcm459",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459", "source_raw_sha256":
    "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503", "source_text_sha256":
    "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f", "accessed_at":
    "2026-10-28T06:49:23.766409Z", "exact_source_quote": "Autoclave glucose solution
    separately. Incubate under an oxygen-free atmosphere containing 5-10% CO\n2\n.",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q10", "subject":
    "Source default sterilization", "local_fields": [], "decision": "evidence_only",
    "stage": "source-wide preparation default", "interpretation": "JCM explicitly
    supplies the default 121°C for 15 min unless otherwise stated; retain it at the
    appropriate preparation stage alongside the specific separate-glucose instruction.
    This is source guidance, not a measured growth result.", "sources": [{"locator":
    "extracted-text lines 4-4", "source_key": "jcm459", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=459",
    "source_raw_sha256": "fd0df9aaa5fc1dbaf975880537589ecc69947127dd7e0ebd41bf55078e138503",
    "source_text_sha256": "394a8b7e865c6ba2540f621860e0bf3a3ef0507764aeab51fffe92166cc9598f",
    "accessed_at": "2026-10-28T06:49:23.766409Z", "exact_source_quote": "Unless otherwise
    stated, sterilize media by autoclaving at 121°C for 15 min.", "quote_representation":
    "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch059/record04/grounding-inventory.json",
    "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization,
    stock composition, working dose and preparation controls are separate. No source
    edits or automatic curation performed."}'
- assessment_id: a5
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/CAPNOCYTOPHAGA_MEDIUM.yaml: primary 4/6, secondary
    3/6; data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml: primary
    4/6, secondary 3/6. These are ingredient-instance linkage fractions, not accuracy
    scores. Solution terms are audited separately. Every actually asserted CHEBI term
    is joined to its exact current OLS object and packaged MIM CSV rows. 2 numeric
    legacy MediaIngredientMech mentions occur across the complete selected documents,
    with exact locators in the inventory; NNNNNN is a historical placeholder, not
    an ID. Complex commercial/product components are not forced to pure-compound IDs.'
  target_ids:
  - CultureMech:002808
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
  - CultureMech:002808
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
  - CultureMech:002808
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-002808-missing-preparation-water-default-and-evidence
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source water, sterilization default and claim-level evidence are incomplete
  description: The current JCM source and API retain the absolute water input, but
    both selected layers omit it. The JCM default sterilization conditions are absent;
    the present pH, separate-glucose and incubation atmosphere wording is supported.
    Neither selected layer attaches claim-level source evidence.
  target_ids:
  - CultureMech:002808
  field_paths:
  - preparation_steps
  - evidence
  evidence_ids:
  - jcm459
  - apiJ459
  - local0
  - local1
  rule_id: source-preparation-completeness
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-002808-legacy-potassium-nitrate-secondary-link
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: A deprecated secondary identifier remains on potassium nitrate
  description: KNO3 primary CHEBI:63043 is correct and matches the source and current
    OLS potassium nitrate object. Its secondary MediaIngredientMech:000170 is absent
    from the complete current packaged label index. This current negative does not
    prove the old identifier never existed. Glucose, sodium chloride and hemin primary/secondary
    correspondences are supported.
  target_ids:
  - CultureMech:002808
  field_paths:
  - ingredients[4].mediaingredientmech_term
  evidence_ids:
  - grounding
  - chebi63043
  rule_id: P2.1
  native_severity: P2
  normalization_reason: The obsolete secondary linkage is normalized to minor despite
    native P2.1 because the correct current primary potassium-nitrate identity remains
    intact; no ingredient substitution or amount error is established.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Retain the absolute source water and appropriately scoped source default
    in maintained preparation, preserving the existing correct specific steps. Add
    short exact evidence at root for preparation and ingredient scope for quantities.
    Do not infer glucose stock strength or final solvent volume.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002808
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml
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
  description: Resolve and replace the deprecated secondary linkage using the verified
    current CHEBI-keyed correspondence; preserve the correct primary ID, supported
    amount and original history. Append a new dated context event only when an actual
    correction is made.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002808
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J459_CAPNOCYTOPHAGA_MEDIUM.yaml
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
- No named strain or growth outcome is established by the recipe title. Collection
  instructions are formulation context only.
- Current MIM absence does not invalidate historical identifier use; complex commercial
  ingredients are not forced into pure-compound ontology terms.
- The separately autoclaved glucose solution has no stated strength or solvent volume.
  No measured final-volume denominator or unprovided gas identity is inferred.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
