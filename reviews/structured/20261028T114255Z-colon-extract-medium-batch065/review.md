# Scientific review of colon_extract_medium

- Review: 20261028T114255Z-colon-extract-medium-batch065
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T11:30:37.198640Z
- Finished UTC: 2026-10-28T11:42:55.669179Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The five main provider rates and retained preparation words are credited, while thirteen stock-strength rows, the vitamin K1 liquid dose and stock preparation boundaries require correction. Cheesecloth filtering is not sterilization, and the manganese hydrate remains unresolved.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch065 selection index 5 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003200 | data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml | generated | colon_extract_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003200 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:003200 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:003200 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:003200 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact J854 source identity and availability

identity: unknown. Targets: CultureMech:003200.

The selected target and sole maintained owner identify JCM854. The current MediaDive J854 recipe contains the same main ingredients and separate A/B/C/D/hemin structure. The exact JCM primary page returns HTTP200 with Nothing found, so the primary recipe is unavailable; the source review remains partial and no organism-specific association is inferred.

### Classification and source-specific controls

consistency: supported. Targets: CultureMech:003200.

Complex, undefined, liquid classification is consistent with yeast extract, peptone and colon extract. Main pH 7.0 is retained correctly. Solution D preparation temperatures and incubation/storage times are not general target-organism growth conditions.

### Chemical forms and source-side molarity

grounding: concern. Targets: CultureMech:003200.

Current labels and exact MIM identifier rows agree. Calcium dihydrate, magnesium hexahydrate, cobalt hexahydrate, ferrous heptahydrate and L-cysteine hydrochloride monohydrate are already represented by corresponding hydrate terms. MnSO4 x n H2O remains an unspecified hydrate while CHEBI:86360 encodes MnSO4 without water; do not infer n or use its anhydrous mass as exact supplied-form evidence. Generic source Resazurin is not automatically a sodium-salt claim. The provider cobalt mmol conversion conflicts with its named hydrate and mass.

### Historical assertions and current writers

provenance: unknown. Targets: CultureMech:003200.

All three historical reports were read in full. The current API bytes authenticate the exact quoted payload and objects when their historical digest matches, but the old blanket stock conflict does not apply to the five separately supported main rates. No formulation claims are attached in either selected document. Current one-owner merging carries existing content forward; it does not independently reconstruct missing stock boundaries. Historical events remain unchanged; future remediation appends actual verified context. Current conservative merging preserves scientific fields and rejects incompatible formulations. Inspected writer behavior is described separately by exact file and function; it does not prove historical execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:003200.

All 38 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:003200", "selected_concentration_field_count": 38, "selected_concentration_fields_covered": 38, "decisions": [{"decision_id": "q1", "subject": "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "3.15657", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "3.15657", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main-recipe rate on the explicit provider basis", "interpretation": "The stored rate equals provider g_l=3.15657 for 5 g in the main recipe. The API metadata volume is 1584 ml; this is provider normalization, not independently established final volume. Five main rates are credited rather than repeated as blanket historical stock conflicts. No attached formulation evidence exists.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.15657,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q2", "subject": "Trypticase peptone", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "3.15657", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "3.15657", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main-recipe rate on the explicit provider basis", "interpretation": "The stored rate equals provider g_l=3.15657 for 5 g in the main recipe. The API metadata volume is 1584 ml; this is provider normalization, not independently established final volume. Five main rates are credited rather than repeated as blanket historical stock conflicts. No attached formulation evidence exists.", "sources": [{"locator": "$.data.solutions[0].recipe[5]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\": 124,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.15657,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q3", "subject": "NaHCO3", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "3.15657", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "3.15657", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main-recipe rate on the explicit provider basis", "interpretation": "The stored rate equals provider g_l=3.15657 for 5 g in the main recipe. The API metadata volume is 1584 ml; this is provider normalization, not independently established final volume. Five main rates are credited rather than repeated as blanket historical stock conflicts. No attached formulation evidence exists.", "sources": [{"locator": "$.data.solutions[0].recipe[6]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.15657,\n                        \"mmol_l\": 37.575,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q4", "subject": "Resazurin", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.000631313", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.000631313", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main-recipe rate on the explicit provider basis", "interpretation": "The stored rate equals provider g_l=0.000631313 for 1 mg in the main recipe. The API metadata volume is 1584 ml; this is provider normalization, not independently established final volume. Five main rates are credited rather than repeated as blanket historical stock conflicts. No attached formulation evidence exists.", "sources": [{"locator": "$.data.solutions[0].recipe[7]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.000631313,\n                        \"mmol_l\": 0.00275454,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q5", "subject": "L-Cysteine HCl x H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.631313", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.631313", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main-recipe rate on the explicit provider basis", "interpretation": "The stored rate equals provider g_l=0.631313 for 1 g in the main recipe. The API metadata volume is 1584 ml; this is provider normalization, not independently established final volume. Five main rates are credited rather than repeated as blanket historical stock conflicts. No attached formulation evidence exists.", "sources": [{"locator": "$.data.solutions[0].recipe[8]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.631313,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q6", "subject": "NaCl", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "5.4", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "5.4", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Composition of Solution A, separate from its receiving dose", "interpretation": "The stored 5.4 G_PER_L is the provider's stock strength, sourced from 5.4 g in the separate Solution A recipe. It is incorrectly placed in the main ingredient list. Preserve the exact stock component and its form; represent the separate 167 ml stock addition. Listed stock water and main volume metadata do not license an assumed final-medium dilution.", "sources": [{"locator": "$.data.solutions[1].recipe[0]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 5.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.4,\n                        \"mmol_l\": 92.4025,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 4830,\n                        \"amount\": 167,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q7", "subject": "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "2.7", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "2.7", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Composition of Solution A, separate from its receiving dose", "interpretation": "The stored 2.7 G_PER_L is the provider's stock strength, sourced from 2.7 g in the separate Solution A recipe. It is incorrectly placed in the main ingredient list. Preserve the exact stock component and its form; represent the separate 167 ml stock addition. Listed stock water and main volume metadata do not license an assumed final-medium dilution.", "sources": [{"locator": "$.data.solutions[1].recipe[1]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 2.7,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.7,\n                        \"mmol_l\": 19.8404,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 4830,\n                        \"amount\": 167,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q8", "subject": "CaCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.16", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.16", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Composition of Solution A, separate from its receiving dose", "interpretation": "The stored 0.16 G_PER_L is the provider's stock strength, sourced from 0.16 g in the separate Solution A recipe. It is incorrectly placed in the main ingredient list. Preserve the exact stock component and its form; represent the separate 167 ml stock addition. Listed stock water and main volume metadata do not license an assumed final-medium dilution.", "sources": [{"locator": "$.data.solutions[1].recipe[2]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.16,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.16,\n                        \"mmol_l\": 1.08832,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 4830,\n                        \"amount\": 167,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q9", "subject": "MgCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.12", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.12", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Composition of Solution A, separate from its receiving dose", "interpretation": "The stored 0.12 G_PER_L is the provider's stock strength, sourced from 0.12 g in the separate Solution A recipe. It is incorrectly placed in the main ingredient list. Preserve the exact stock component and its form; represent the separate 167 ml stock addition. Listed stock water and main volume metadata do not license an assumed final-medium dilution.", "sources": [{"locator": "$.data.solutions[1].recipe[3]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.12,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.12,\n                        \"mmol_l\": 0.590252,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 4830,\n                        \"amount\": 167,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q10", "subject": "MnSO4 x n H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Composition of Solution A, separate from its receiving dose", "interpretation": "The stored 0.07 G_PER_L is the provider's stock strength, sourced from 0.07 g in the separate Solution A recipe. It is incorrectly placed in the main ingredient list. Preserve the exact stock component and its form; represent the separate 167 ml stock addition. Listed stock water and main volume metadata do not license an assumed final-medium dilution.", "sources": [{"locator": "$.data.solutions[1].recipe[4]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MnSO4 x n H2O\",\n                        \"compound_id\": 1000,\n                        \"amount\": 0.07,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.07,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 4830,\n                        \"amount\": 167,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q11", "subject": "CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "0.06", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "0.06", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Composition of Solution A, separate from its receiving dose", "interpretation": "The stored 0.06 G_PER_L is the provider's stock strength, sourced from 0.06 g in the separate Solution A recipe. It is incorrectly placed in the main ingredient list. Preserve the exact stock component and its form; represent the separate 167 ml stock addition. Listed stock water and main volume metadata do not license an assumed final-medium dilution.", "sources": [{"locator": "$.data.solutions[1].recipe[5]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.06,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.06,\n                        \"mmol_l\": 0.462111,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 4830,\n                        \"amount\": 167,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q12", "subject": "(NH4)2SO4", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "5.4", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "5.4", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Composition of Solution A, separate from its receiving dose", "interpretation": "The stored 5.4 G_PER_L is the provider's stock strength, sourced from 5.4 g in the separate Solution A recipe. It is incorrectly placed in the main ingredient list. Preserve the exact stock component and its form; represent the separate 167 ml stock addition. Listed stock water and main volume metadata do not license an assumed final-medium dilution.", "sources": [{"locator": "$.data.solutions[1].recipe[6]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 5.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.4,\n                        \"mmol_l\": 40.8657,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 4830,\n                        \"amount\": 167,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q13", "subject": "FeSO4 x 7 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Composition of Solution A, separate from its receiving dose", "interpretation": "The stored 0.05 G_PER_L is the provider's stock strength, sourced from 0.05 g in the separate Solution A recipe. It is incorrectly placed in the main ingredient list. Preserve the exact stock component and its form; represent the separate 167 ml stock addition. Listed stock water and main volume metadata do not license an assumed final-medium dilution.", "sources": [{"locator": "$.data.solutions[1].recipe[7]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.179846,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 4830,\n                        \"amount\": 167,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q14", "subject": "K2HPO4", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "2.7", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "2.7", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Composition of Solution B, separate from its receiving dose", "interpretation": "The stored 2.7 G_PER_L is the provider's stock strength, sourced from 2.7 g in the separate Solution B recipe. It is incorrectly placed in the main ingredient list. Preserve the exact stock component and its form; represent the separate 167 ml stock addition. Listed stock water and main volume metadata do not license an assumed final-medium dilution.", "sources": [{"locator": "$.data.solutions[2].recipe[0]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 2.7,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.7,\n                        \"mmol_l\": 15.5016,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[1]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\": 4831,\n                        \"amount\": 167,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q15", "subject": "Glucose", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "50", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Composition of Solution C, separate from its receiving dose", "interpretation": "The stored 50 G_PER_L is the provider's stock strength, sourced from 50 g in the separate Solution C recipe. It is incorrectly placed in the main ingredient list. Preserve the exact stock component and its form; represent the separate 40 ml stock addition. Listed stock water and main volume metadata do not license an assumed final-medium dilution.", "sources": [{"locator": "$.data.solutions[3].recipe[0]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 50,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\": 277.531,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[2]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 4832,\n                        \"amount\": 40,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q16", "subject": "Maltose", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "50", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Composition of Solution C, separate from its receiving dose", "interpretation": "The stored 50 G_PER_L is the provider's stock strength, sourced from 50 g in the separate Solution C recipe. It is incorrectly placed in the main ingredient list. Preserve the exact stock component and its form; represent the separate 40 ml stock addition. Listed stock water and main volume metadata do not license an assumed final-medium dilution.", "sources": [{"locator": "$.data.solutions[3].recipe[1]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Maltose\",\n                        \"compound_id\": 171,\n                        \"amount\": 50,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\": 146.071,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[2]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 4832,\n                        \"amount\": 40,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q17", "subject": "Cellobiose", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "50", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Composition of Solution C, separate from its receiving dose", "interpretation": "The stored 50 G_PER_L is the provider's stock strength, sourced from 50 g in the separate Solution C recipe. It is incorrectly placed in the main ingredient list. Preserve the exact stock component and its form; represent the separate 40 ml stock addition. Listed stock water and main volume metadata do not license an assumed final-medium dilution.", "sources": [{"locator": "$.data.solutions[3].recipe[2]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Cellobiose\",\n                        \"compound_id\": 214,\n                        \"amount\": 50,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\": 146.071,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[2]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 4832,\n                        \"amount\": 40,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q18", "subject": "Xylose", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "50", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "50", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Composition of Solution C, separate from its receiving dose", "interpretation": "The stored 50 G_PER_L is the provider's stock strength, sourced from 50 g in the separate Solution C recipe. It is incorrectly placed in the main ingredient list. Preserve the exact stock component and its form; represent the separate 40 ml stock addition. Listed stock water and main volume metadata do not license an assumed final-medium dilution.", "sources": [{"locator": "$.data.solutions[3].recipe[3]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Xylose\",\n                        \"compound_id\": 1107,\n                        \"amount\": 50,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\": 333.045,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[2]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 4832,\n                        \"amount\": 40,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q19", "subject": "Vitamin K1", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Liquid addition of a percentage stock", "interpretation": "The source is 0.2 ml of Vitamin K1 with attribute 0.5%, not 0.2 G_PER_L phylloquinone. The percentage basis and stock solvent are not specified, so no mass concentration, density or final-medium rate is invented. Preserve the liquid dose and unresolved percent basis.", "sources": [{"locator": "$.data.solutions[0].recipe[9]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Vitamin K1\",\n                        \"compound_id\": 150,\n                        \"attribute\": \"0.5%\",\n                        \"amount\": 0.2,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q20", "subject": "Solution A receiving addition", "local_fields": [], "decision": "add", "stage": "Absolute main-recipe stock addition", "interpretation": "Represent the exact 167 ml of Solution A (provider solution 4830) with its own composition/preparation boundary. This dose is absent as a solution addition in both selected documents. Do not relabel it ml/L without an explicit final-volume basis.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 4830,\n                        \"amount\": 167,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q21", "subject": "Solution B receiving addition", "local_fields": [], "decision": "add", "stage": "Absolute main-recipe stock addition", "interpretation": "Represent the exact 167 ml of Solution B (provider solution 4831) with its own composition/preparation boundary. This dose is absent as a solution addition in both selected documents. Do not relabel it ml/L without an explicit final-volume basis.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\": 4831,\n                        \"amount\": 167,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q22", "subject": "Solution C receiving addition", "local_fields": [], "decision": "add", "stage": "Absolute main-recipe stock addition", "interpretation": "Represent the exact 40 ml of Solution C (provider solution 4832) with its own composition/preparation boundary. This dose is absent as a solution addition in both selected documents. Do not relabel it ml/L without an explicit final-volume basis.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 4832,\n                        \"amount\": 40,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q23", "subject": "Solution D receiving addition", "local_fields": [], "decision": "add", "stage": "Absolute main-recipe stock addition", "interpretation": "Represent the exact 200 ml of Solution D (provider solution 4833) with its own composition/preparation boundary. This dose is absent as a solution addition in both selected documents. Do not relabel it ml/L without an explicit final-volume basis.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\": 4833,\n                        \"amount\": 200,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q24", "subject": "Hemin solution receiving addition", "local_fields": [], "decision": "add", "stage": "Absolute main-recipe stock addition", "interpretation": "Represent the exact 10 ml of Hemin solution (provider solution 4218) with its own composition/preparation boundary. This dose is absent as a solution addition in both selected documents. Do not relabel it ml/L without an explicit final-volume basis.", "sources": [{"locator": "$.data.solutions[0].recipe[10]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"solution\": \"Hemin solution\",\n                        \"solution_id\": 4218,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q25", "subject": "Main sol. J854 water", "local_fields": [], "decision": "add", "stage": "Separate solvent input", "interpretation": "The source lists 1000 ml water in this specific recipe. Preserve each independently scoped solvent input; do not merge stock water with main water or treat listed water as an explicit make-up-to-final-volume instruction.", "sources": [{"locator": "$.data.solutions[0].recipe[11]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q26", "subject": "Solution A water", "local_fields": [], "decision": "add", "stage": "Separate solvent input", "interpretation": "The source lists 1000 ml water in this specific recipe. Preserve each independently scoped solvent input; do not merge stock water with main water or treat listed water as an explicit make-up-to-final-volume instruction.", "sources": [{"locator": "$.data.solutions[1].recipe[8]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q27", "subject": "Solution B water", "local_fields": [], "decision": "add", "stage": "Separate solvent input", "interpretation": "The source lists 1000 ml water in this specific recipe. Preserve each independently scoped solvent input; do not merge stock water with main water or treat listed water as an explicit make-up-to-final-volume instruction.", "sources": [{"locator": "$.data.solutions[2].recipe[1]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q28", "subject": "Solution C water", "local_fields": [], "decision": "add", "stage": "Separate solvent input", "interpretation": "The source lists 1000 ml water in this specific recipe. Preserve each independently scoped solvent input; do not merge stock water with main water or treat listed water as an explicit make-up-to-final-volume instruction.", "sources": [{"locator": "$.data.solutions[3].recipe[4]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q29", "subject": "Main pH", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "ph_value", "original": 7.0}, {"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "preparation_steps[0].description", "original": "Adjust pH to 7.0."}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "preparation_steps[0].description", "original": "Adjust pH to 7.0."}], "decision": "evidence_only", "stage": "Main-medium preparation", "interpretation": "The stored pH 7.0 and first preparation description match the source. This main control is distinct from the pH adjustment during preparation of Solution D.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 7.0.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q30", "subject": "Retained Solution D preparation quantities", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "preparation_steps[1].description", "original": "Dilute (1:1, w/v) the content of terminal pig colon with the following buffer: 167 ml Solution A (see above) and 167 ml Solution B (see above). Make up to 1.0 L with distilled water. Stomach the suspension and filter through a cheese cloth. Incubate at 37C for 48 h and adjust pH to 7.0. Centrifuge at 20,000 x g for 20 min. Retrieve the supernatant and store at -20C until use."}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "preparation_steps[1].description", "original": "Dilute (1:1, w/v) the content of terminal pig colon with the following buffer: 167 ml Solution A (see above) and 167 ml Solution B (see above). Make up to 1.0 L with distilled water. Stomach the suspension and filter through a cheese cloth. Incubate at 37C for 48 h and adjust pH to 7.0. Centrifuge at 20,000 x g for 20 min. Retrieve the supernatant and store at -20C until use."}], "decision": "evidence_only", "stage": "Preparation of the colon-extract stock, not main culture conditions", "interpretation": "The existing text faithfully retains 1:1 w/v extraction, 167 ml each of Solutions A/B, make-up to 1.0 L, cheesecloth filtration, 37 C for 48 h, pH 7.0, 20000 x g for 20 min and storage at -20 C. Credit those retained words while restoring their Solution D boundary. These are preparation/storage controls, not experimental organism-growth evidence.", "sources": [{"locator": "$.data.solutions[4].steps[0]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"step\": \"Dilute (1:1, w/v) the content of terminal pig colon with the following buffer: 167 ml Solution A (see above) and 167 ml Solution B (see above). Make up to 1.0 L with distilled water. Stomach the suspension and filter through a cheese cloth. Incubate at 37C for 48 h and adjust pH to 7.0. Centrifuge at 20,000 x g for 20 min. Retrieve the supernatant and store at -20C until use.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q31", "subject": "Cheesecloth action code", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "preparation_steps[1].action", "original": "FILTER_STERILIZE"}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "preparation_steps[1].action", "original": "FILTER_STERILIZE"}], "decision": "conflict", "stage": "Mechanical stock filtration", "interpretation": "FILTER_STERILIZE is not supported by filtering through cheesecloth. Preserve the actual extraction/filtration/centrifugation description and choose a non-sterilizing representation; neither sterility nor a membrane filter is specified.", "sources": [{"locator": "$.data.solutions[4].steps[0]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"step\": \"Dilute (1:1, w/v) the content of terminal pig colon with the following buffer: 167 ml Solution A (see above) and 167 ml Solution B (see above). Make up to 1.0 L with distilled water. Stomach the suspension and filter through a cheese cloth. Incubate at 37C for 48 h and adjust pH to 7.0. Centrifuge at 20,000 x g for 20 min. Retrieve the supernatant and store at -20C until use.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q32", "subject": "Retained hemin-stock preparation", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path": "preparation_steps[2].description", "original": "Dissolve 50 mg hemin first in 1 ml of 1 N NaOH. Then adjust volume to 100 ml."}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "preparation_steps[2].description", "original": "Dissolve 50 mg hemin first in 1 ml of 1 N NaOH. Then adjust volume to 100 ml."}], "decision": "evidence_only", "stage": "Separate hemin stock", "interpretation": "The existing words correctly state 50 mg hemin dissolved first in 1 ml of 1 N NaOH, then adjusted to 100 ml. This explicit final stock volume gives 0.5 mg/ml (0.5 g/L) stock, but the separate 10 ml receiving dose and main final volume must not be conflated. Restore the stock boundary and preserve the source NaOH normality without adding an unsupported final alkali rate.", "sources": [{"locator": "$.data.solutions[5].steps[0]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve 50 mg hemin first in 1 ml of 1 N NaOH. Then adjust volume to 100 ml.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[10]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"solution\": \"Hemin solution\",\n                        \"solution_id\": 4218,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q33", "subject": "Provider main volume metadata", "local_fields": [], "decision": "unsupported", "stage": "Provider denominator with an internal accounting limitation", "interpretation": "The API volume=1584 ml equals the listed 1000+167+167+40+200+10 ml additions and omits the separate 0.2 ml Vitamin K1. Neither that nominal sum nor the alternative 1584.2 ml sum establishes a measured final volume. Keep the five existing provider g_l rates explicitly qualified and preserve source batch quantities; do not change rates merely by choosing a new divisor.", "sources": [{"locator": "$.data.solutions[0]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                \"id\": 4829,\n                \"name\": \"Main sol. J854\",\n                \"volume\": 1584,\n                \"recipe\": [\n                    {\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 4830,\n                        \"amount\": 167,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\": 4831,\n                        \"amount\": 167,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 4832,\n                        \"amount\": 40,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 4,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\": 4833,\n                        \"amount\": 200,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 5,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.15657,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 6,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\": 124,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.15657,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 7,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.15657,\n                        \"mmol_l\": 37.575,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 8,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.000631313,\n                        \"mmol_l\": 0.00275454,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 9,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.631313,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 10,\n                        \"compound\": \"Vitamin K1\",\n                        \"compound_id\": 150,\n                        \"attribute\": \"0.5%\",\n                        \"amount\": 0.2,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 11,\n                        \"solution\": \"Hemin solution\",\n                        \"solution_id\": 4218,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 12,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }\n                ],\n                \"steps\": [\n                    {\n                        \"step\": \"Adjust pH to 7.0.\"\n                    }\n                ]\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q34", "subject": "Cobalt provider molar conversion", "local_fields": [], "decision": "conflict", "stage": "Source-side derived molarity of Solution A", "interpretation": "The source mass is 0.06 g with explicit CoCl2 x 6 H2O and the correct current local CHEBI:53503. Using the current authoritative mass 237.929 g/mol gives about 0.252175 mmol/L on the provider stock basis, whereas the API prints 0.462111 mmol/L. Preserve the mass and hydrate; do not transfer the inconsistent derived mmol value into the record or substitute an anhydrous mass.", "sources": [{"locator": "$.data.solutions[1].recipe[5]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.06,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.06,\n                        \"mmol_l\": 0.462111,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$._embedded.terms[0]", "source_key": "chebi53503", "reference": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503", "source_raw_sha256": "c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d", "source_text_sha256": "c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d", "accessed_at": "2026-10-28T11:31:06.208518Z", "exact_source_quote": "{\n      \"iri\" : \"http://purl.obolibrary.org/obo/CHEBI_53503\",\n      \"lang\" : \"en\",\n      \"description\" : [ \"A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride and water moieties in the ratio 1:2:6.\" ],\n      \"synonyms\" : [ \"Cobalt chloride hexahydrate\", \"Cobalt dichloride hexahydrate\", \"Cobalt(II) chloride hexahydrate\", \"Cobalt(II) chloride--water (1/7)\", \"Cobalt(II) chloride--water (1/7)\", \"cobalt (II) chloride hexahydrate\", \"cobalt chloride hydrate\", \"cobalt(2+) dichloride hexahydrate\", \"cobalt(2+) dichloride hexahydrate\" ],\n      \"annotation\" : {\n        \"charge\" : [ 0.0 ],\n        \"database_cross_reference\" : [ \"cas:7791-13-1\", \"gmelin:16833\", \"patent:CN101077120\", \"pubmed:11207315\", \"pubmed:16870561\", \"pubmed:2025398\", \"pubmed:21721333\", \"pubmed:8404951\", \"pubmed:8857117\", \"pubmed:9106780\", \"reaxys:11403444\" ],\n        \"generalized_empirical_formula\" : [ \"2Cl.Co.6H2O\" ],\n        \"has_obo_namespace\" : [ \"chebi_ontology\" ],\n        \"id\" : [ \"CHEBI:53503\" ],\n        \"inchi_key_string\" : [ \"GFHNAMRJFCEERV-UHFFFAOYSA-L\" ],\n        \"inchi_string\" : [ \"InChI=1S/2ClH.Co.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2\" ],\n        \"mass\" : [ \"237.929\" ],\n        \"monoisotopic_mass\" : [ \"236.93429\" ],\n        \"smiles_string\" : [ \"O.O.O.O.O.O.[Cl-].[Cl-].[Co+2]\" ]\n      },\n      \"label\" : \"cobalt chloride hexahydrate\",\n      \"ontology_name\" : \"chebi\",\n      \"ontology_prefix\" : \"CHEBI\",\n      \"ontology_iri\" : \"http://purl.obolibrary.org/obo/chebi.owl\",\n      \"is_obsolete\" : false,\n      \"term_replaced_by\" : null,\n      \"is_defining_ontology\" : true,\n      \"has_children\" : false,\n      \"is_root\" : false,\n      \"short_form\" : \"CHEBI_53503\",\n      \"obo_id\" : \"CHEBI:53503\",\n      \"in_subset\" : [ \"3_STAR\" ],\n      \"obo_definition_citation\" : null,\n      \"obo_xref\" : [ {\n        \"database\" : \"cas\",\n        \"id\" : \"7791-13-1\",\n        \"description\" : \"cas\",\n        \"url\" : \"https://commonchemistry.cas.org/detail?cas_rn=7791-13-1\"\n      }, {\n        \"database\" : \"gmelin\",\n        \"id\" : \"16833\",\n        \"description\" : \"gmelin\",\n        \"url\" : null\n      }, {\n        \"database\" : \"patent\",\n        \"id\" : \"CN101077120\",\n        \"description\" : \"patent\",\n        \"url\" : \"https://www.google.com/patents/CN101077120\"\n      }, {\n        \"database\" : \"pubmed\",\n        \"id\" : \"11207315\",\n        \"description\" : \"pubmed\",\n        \"url\" : \"https://pubmed.ncbi.nlm.nih.gov/11207315/\"\n      }, {\n        \"database\" : \"pubmed\",\n        \"id\" : \"16870561\",\n        \"description\" : \"pubmed\",\n        \"url\" : \"https://pubmed.ncbi.nlm.nih.gov/16870561/\"\n      }, {\n        \"database\" : \"pubmed\",\n        \"id\" : \"2025398\",\n        \"description\" : \"pubmed\",\n        \"url\" : \"https://pubmed.ncbi.nlm.nih.gov/2025398/\"\n      }, {\n        \"database\" : \"pubmed\",\n        \"id\" : \"21721333\",\n        \"description\" : \"pubmed\",\n        \"url\" : \"https://pubmed.ncbi.nlm.nih.gov/21721333/\"\n      }, {\n        \"database\" : \"pubmed\",\n        \"id\" : \"8404951\",\n        \"description\" : \"pubmed\",\n        \"url\" : \"https://pubmed.ncbi.nlm.nih.gov/8404951/\"\n      }, {\n        \"database\" : \"pubmed\",\n        \"id\" : \"8857117\",\n        \"description\" : \"pubmed\",\n        \"url\" : \"https://pubmed.ncbi.nlm.nih.gov/8857117/\"\n      }, {\n        \"database\" : \"pubmed\",\n        \"id\" : \"9106780\",\n        \"description\" : \"pubmed\",\n        \"url\" : \"https://pubmed.ncbi.nlm.nih.gov/9106780/\"\n      }, {\n        \"database\" : \"reaxys\",\n        \"id\" : \"11403444\",\n        \"description\" : \"reaxys\",\n        \"url\" : null\n      } ],\n      \"obo_synonym\" : [ {\n        \"name\" : \"Cobalt(II) chloride--water (1/7)\",\n        \"scope\" : \"hasExactSynonym\",\n        \"type\" : \"IUPAC NAME\",\n        \"xrefs\" : [ {\n          \"database\" : null,\n          \"id\" : \"IUPAC\",\n          \"description\" : null,\n          \"url\" : null\n        } ]\n      }, {\n        \"name\" : \"cobalt(2+) dichloride hexahydrate\",\n        \"scope\" : \"hasExactSynonym\",\n        \"type\" : \"IUPAC NAME\",\n        \"xrefs\" : [ {\n          \"database\" : null,\n          \"id\" : \"IUPAC\",\n          \"description\" : null,\n          \"url\" : null\n        } ]\n      }, {\n        \"name\" : \"Cobalt chloride hexahydrate\",\n        \"scope\" : \"hasRelatedSynonym\",\n        \"type\" : null,\n        \"xrefs\" : [ {\n          \"database\" : null,\n          \"id\" : \"chemidplus\",\n          \"description\" : null,\n          \"url\" : null\n        } ]\n      }, {\n        \"name\" : \"Cobalt dichloride hexahydrate\",\n        \"scope\" : \"hasRelatedSynonym\",\n        \"type\" : null,\n        \"xrefs\" : [ {\n          \"database\" : null,\n          \"id\" : \"chemidplus\",\n          \"description\" : null,\n          \"url\" : null\n        } ]\n      }, {\n        \"name\" : \"Cobalt(II) chloride hexahydrate\",\n        \"scope\" : \"hasRelatedSynonym\",\n        \"type\" : null,\n        \"xrefs\" : [ {\n          \"database\" : null,\n          \"id\" : \"chemidplus\",\n          \"description\" : null,\n          \"url\" : null\n        } ]\n      }, {\n        \"name\" : \"Cobalt(II) chloride--water (1/7)\",\n        \"scope\" : \"hasRelatedSynonym\",\n        \"type\" : \"IUPAC NAME\",\n        \"xrefs\" : [ {\n          \"database\" : null,\n          \"id\" : \"iupac\",\n          \"description\" : null,\n          \"url\" : null\n        } ]\n      }, {\n        \"name\" : \"cobalt (II) chloride hexahydrate\",\n        \"scope\" : \"hasRelatedSynonym\",\n        \"type\" : null,\n        \"xrefs\" : [ {\n          \"database\" : null,\n          \"id\" : \"chebi\",\n          \"description\" : null,\n          \"url\" : null\n        } ]\n      }, {\n        \"name\" : \"cobalt chloride hydrate\",\n        \"scope\" : \"hasRelatedSynonym\",\n        \"type\" : null,\n        \"xrefs\" : [ {\n          \"database\" : null,\n          \"id\" : \"chebi\",\n          \"description\" : null,\n          \"url\" : null\n        } ]\n      }, {\n        \"name\" : \"cobalt(2+) dichloride hexahydrate\",\n        \"scope\" : \"hasRelatedSynonym\",\n        \"type\" : \"IUPAC NAME\",\n        \"xrefs\" : [ {\n          \"database\" : null,\n          \"id\" : \"iupac\",\n          \"description\" : null,\n          \"url\" : null\n        } ]\n      } ],\n      \"is_preferred_root\" : false,\n      \"_links\" : {\n        \"self\" : {\n          \"href\" : \"http://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_53503?lang=en\"\n        },\n        \"parents\" : {\n          \"href\" : \"http://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_53503/parents\"\n        },\n        \"ancestors\" : {\n          \"href\" : \"http://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_53503/ancestors\"\n        },\n        \"hierarchicalParents\" : {\n          \"href\" : \"http://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_53503/hierarchicalParents\"\n        },\n        \"hierarchicalAncestors\" : {\n          \"href\" : \"http://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_53503/hierarchicalAncestors\"\n        },\n        \"jstree\" : {\n          \"href\" : \"http://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_53503/jstree\"\n        },\n        \"graph\" : {\n          \"href\" : \"http://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_53503/graph\"\n        },\n        \"has_part\" : {\n          \"href\" : \"http://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_53503/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBFO_0000051\"\n        },\n        \"has_role\" : {\n          \"href\" : \"http://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_53503/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FRO_0000087\"\n        }\n      }\n    }", "quote_representation": "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch065/record05/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:003200.

data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml: primary 17/19, secondary 16/19; data/normalized_yaml/bacterial/colon_extract_medium.yaml: primary 17/19, secondary 16/19. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:003200.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:003200.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Thirteen stock components have lost their preparation and dosing boundaries

major / open / confirmed; issue key: culturemech-003200-stock-components-flattened-as-main-rates.

Eight Solution A components, one Solution B component and four Solution C components appear as main-medium ingredients at full stock strength. Source A/B/C receiving doses are absent; Solution D and hemin receiving additions are also missing despite their preparation prose being retained. Five main provider g_l rates are separately supported.

### f2: Vitamin K1 liquid stock is represented as a mass concentration

major / open / confirmed; issue key: culturemech-003200-vitamin-k1-liquid-stock-as-mass-rate.

Both selected documents store 0.2 G_PER_L, while the exact source row is 0.2 ml of a 0.5% Vitamin K1 preparation. The absent percentage basis prevents an evidence-backed conversion to a mass dose or rate.

### f3: Stock preparation is flattened and cheesecloth filtration is labeled sterilization

major / open / confirmed; issue key: culturemech-003200-cheesecloth-misclassified-as-sterilization.

Solution D and hemin preparation are retained as consecutive main steps, but their boundaries are lost. FILTER_STERILIZE overstates a source instruction to filter through cheesecloth. Main and stock water inputs are missing. The current importer collects prose from all solution recipes and classifies a filter substring as sterilization; this is current behavior, not proof of the historical run.

### f4: Manganese hydrate specificity remains unresolved

minor / open / confirmed; issue key: culturemech-003200-manganese-unspecified-hydrate-form.

Both layers retain MnSO4 x n H2O but assert CHEBI:86360 manganese(II) sulfate, whose current formula is Mn.O4S. This is not an authenticated exact hydrate identity. The source does not supply n, so no specific hydrate or molecular weight can be safely substituted.

## Recommended Actions And Acceptance Checks

### action1

Restore explicitly scoped A/B/C stock compositions and all five receiving stock additions using exact source batch volumes. Credit retained D/hemin preparation text. Preserve the five supported provider main rates with their volume caveat; do not calculate a final dilution until a defensible final basis is available.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Represent the liquid stock addition and retain the literal percent with its unresolved basis. Resolve stock solvent and percent convention only from exact source evidence; do not invent w/v, v/v or a density.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Retain the complete original preparation text under its exact stock, distinguish extraction/cheesecloth filtration/centrifugation/storage from sterilization and restore the source solvent statements. Review the importer stage aggregation and action classifier, repair maintained input and regenerate without inventing processing conditions.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Retain the exact unresolved hydrate wording and source mass, document the mapping specificity limitation, and resolve the supplied form only with exact evidence. Do not invent a secondary link or calculate molarity from the anhydrous formula.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/colon_extract_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch065/record05/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch065/record05/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch065/record05/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch065/record05/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| jcm854 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=854; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | The exact official JCM854 page returned HTTP 200 but states Nothing found. This is an unusable primary formulation response; its status must not be promoted to recipe support. |
| apiJ854 | https://mediadive.dsmz.de/rest/medium/J854; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:131527 = dipotassium hydrogen phosphate; definition ['A potassium salt that is the dipotassium salt of phosphoric acid.']; formula ['HO4P.2K']; mass ['174.174']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17057 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17057 = cellobiose; definition ['A glycosylglucose consisting of two glucose units linked via a β(1→4) bond.']; formula ['C12H22O11']; mass ['342.297']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17234 = glucose; definition ['An aldohexose used as a source of energy and metabolic intermediate.']; formula ['C6H12O6']; mass ['180.156']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17306 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17306; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17306 = maltose; definition ['A glycosylglucose consisting of two &lt;small&gt;D&lt;/small&gt;-glucopyranose units connected by an α-(1→4)-linkage.']; formula ['C12H22O11']; mass ['342.297']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi18067 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18067; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:18067 = phylloquinone; definition ['A member of the class of phylloquinones that consists of 1,4-naphthoquinone having methyl and phytyl groups at positions 2 and 3 respectively. The parent of the class of phylloquinones.']; formula ['C31H46O2']; mass ['450.707']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi18222 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18222; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:18222 = xylose; definition ['An aldopentose, found in the embryos of most edible plants and used in medicine to test for malabsorption by administration in water to the patient.']; formula ['C5H10O5']; mass ['150.13']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32139 = sodium hydrogencarbonate; definition []; formula ['CHO3.Na']; mass ['84.006']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:62946 = ammonium sulfate; definition ['An inorganic sulfate salt obtained by reaction of sulfuric acid with two equivalents of ammonia. A high-melting (decomposes above 280°C) white solid which is very soluble in water (70.6 g/100 g water at 0°C; 103.8 g/100 g water at 100°C), it is widely used as a fertilizer for alkaline soils.']; formula ['2H4N.O4S']; mass ['132.141']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75836 = iron(2+) sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used).']; formula ['Fe.7H2O.O4S']; mass ['278.013']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O']; mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg']; mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86360 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86360 = manganese(II) sulfate; definition ['A metal sulfate in which the metal component is manganese in the +2 oxidation state.']; formula ['Mn.O4S']; mass ['151.001']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4']; mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:91248 = L-cysteine hydrochloride hydrate; definition ['A hydrate that is the monohydrate form of &lt;small&gt;L&lt;/small&gt;-cysteine hydrochloride.']; formula ['C3H7NO2S.H2O.HCl']; mass ['175.637']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch065/record05/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/colon_extract_medium.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current apiJ854 raw bytes exactly match the cited historical SHA, and 31 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/colon_extract_medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/COLON_EXTRACT_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch065/record05/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer30 | scripts/apply_mim_groundings.py; target_slot; groundable; apply_to_record | context_only | Current target_slot preserves existing CHEBI assertions; groundable excludes conflicting corpus opinions, and apply_to_record fills ungrounded entries from proposals. This writer does not authenticate source amounts or automatically repair an existing wrong supplied-form ID. |
| writer31 | scripts/assign_culturemech_ids.py; assign_ids; _assign_id_to_file | context_only | Current assign_ids selects records with missing IDs; _assign_id_to_file checks new-ID collisions and appends identifier provenance. Identifier assignment does not authenticate recipe content or demonstrate historical source access. |
| writer32 | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group collapses equal duplicate values without summing them and retains the first conflicting value with a flag. This behavior is distinct from historical summed-amount artifacts and does not authenticate source-specific stock or product structure. |
| writer33 | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients; merge_ingredient_group | context_only | Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group retains the first concentration, flags differing values and selects the first CHEBI. It cannot establish source stages or justify collapsing independent supplemental and product-contained components. |
| writer34 | scripts/enrich_with_chebi.py; RecipeEnricher.enrich_ingredient; enrich_recipe; enrich_file | context_only | Current RecipeEnricher.enrich_ingredient skips already grounded entries and delegates missing-term mapping to ChemicalMapper; enrich_recipe traverses ingredient and solution structure, and enrich_file writes results and history. Only the read wrapper behavior is claimed here; the mapper is not treated as an independent supplied-form authority. |
| writer35 | scripts/enrich_with_mediaingredientmech.py; main | context_only | Current main orchestrates a local or cloned MIM repository, its loader and ingredient linker. The CLI orchestration was read; it does not itself verify source recipe quantities, supplied chemical forms or the validity of historical MIM assertions. Linker internals are not claimed as separately audited scientific evidence. |
| writer36 | scripts/migrate_chebi_regrounding.py; rewrite_entry; migrate_file | context_only | Current rewrite_entry applies configured exact-ID/label remaps across primary and secondary slots; migrate_file records applied changes. A successful current mapping operation does not establish source-specific hydrate or stereochemical equivalence. |
| writer37 | scripts/migrate_legacy_mim_to_chebi.py; _resolve_chebi; _rewrite_entry | context_only | Current _resolve_chebi reuses current primary CHEBI where available and considers bounded exact-name/synonym matches with a stereo-prefix guard; _rewrite_entry retains unresolved links. Current-row presence is distinct from historical validity and from source-specific supplied-form equivalence. |
| writer38 | scripts/normalize_media_names_to_snake_case.py; process_file; add_curation_history | context_only | Current process_file preserves the original medium name while normalizing its machine name; add_curation_history appends a naming event. Name normalization does not prove equivalence of differently maintained source branches or recipe variants. |
| writer39 | scripts/refill_term_labels.py; refill_text | context_only | Current refill_text replaces term labels using the current exact identifier lookup while preserving other text. Canonical label correspondence is not an independent choice of the correct chemical form for the supplied source reagent. |
| writer40 | scripts/repair_komodo_strain_backlinks.py; PARENTS; CHILDREN; repair_parent; plan_repairs; _upsert_event | context_only | Current repair_parent and plan_repairs target only the explicitly listed 131/777 parents and their two strain children. They do not repair the selected records. _upsert_event replaces a matching curator/action event or appends it; this existing behavior is not permission to rewrite history during this review. |
| writer41 | scripts/repair_merged_duplicates.py; repair_ingredient; repair_record | context_only | Current repair_ingredient and repair_record act on parsed IDENTICAL_PARTS duplicate notes. This bounded repair is not a general solution for product decomposition, stock flattening or differing source formulations. |
| writer42 | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata | context_only | Current DSMZCompositionResolver.merge_composition copies ingredients and solutions, fills pH when absent and copies physical/medium type, but does not copy preparation steps. _add_enrichment_metadata records a naive current timestamp. This explains a present omission risk, not historical execution. |
| writer43 | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current _convert_to_culturemech constructs source notes and default LIQUID with empty ingredients. Its time.strftime format contains %f, which is unsupported here and is consistent with literal .fZ in stored import events. Current code does not authenticate the original retrieval or justify rewriting historical time. |
| writer44 | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps; _classify_preparation_action | context_only | Current _parse_api_composition considers the primary recipe, prefers provider g_l when available and excludes recognized solvents; _is_api_stock_addition distinguishes stock additions. _parse_api_solutions retains separate stock structure. _parse_preparation_steps collects solution prose. These present behaviors do not establish historical execution and cannot justify interpreting flattened stock rates as final-medium concentrations. _parse_preparation_steps collects all solution steps; _classify_preparation_action maps a filter substring to FILTER_STERILIZE. This can misclassify the actual cheesecloth instruction. |
| writer45 | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current formulation_content retains exact scientific quantities, preparation and other scientific fields; merge_formulation_evidence rejects incompatible projections and unions evidence at matching scopes. A source-equivalence claim is not established by shared ingredient identities. |
| writer46 | src/culturemech/merge/matcher.py; group_formulations; group_recipes | context_only | Current group_formulations calls group_recipes with fail_on_invalid=True and FormulationFingerprinter. Expected standalone or unfingerprintable records are excluded; malformed or unexpected inputs raise. Valid records are grouped by full scientific content. This guard does not retrieve or authenticate source recipes. |
| writer47 | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group routes a single maintained owner with merge metadata; multiple owners pass through conservative merge_formulation_evidence. Regenerating from an unrepaired owner retains its defects. Current conservative behavior is credited and does not establish how the old generated record was produced. |
| writer48 | src/culturemech/validation/schema_defaulter.py; apply_defaults; _fix_ingredient; _fix_solution | context_only | Current apply_defaults, _fix_ingredient and _fix_solution can insert VARIABLE amounts and placeholder names for structural completeness. A default is not evidence for a dose, composition, solution identity or denominator; existing default-history events remain contextual. |
| quantity-inventory | REVIEW_WORK/batch065/record05/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- The exact official JCM854 page returns Nothing found despite HTTP200. The complete current MediaDive recipe is the usable formulation evidence; no unavailable primary wording or organism claim is invented.
- The provider main volume 1584 ml omits the separate 0.2 ml stock addition from nominal accounting. Neither sum establishes measured final volume; supported provider rates remain explicitly qualified.
- The source leaves Vitamin K1 percent basis and manganese hydrate number unspecified. Cobalt derived mmol data conflict with its supplied hydrate; preserve masses and forms instead of copying that conversion.
- All preparation controls are scoped to their exact main or stock stage. Current writer inspection and matching historical raw bytes do not reconstruct historical execution or source access time.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T114255Z-colon-extract-medium-batch065
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of colon_extract_medium
started_at: '2026-10-28T11:30:37.198640Z'
finished_at: '2026-10-28T11:42:55.669179Z'
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
summary: The five main provider rates and retained preparation words are credited,
  while thirteen stock-strength rows, the vitamin K1 liquid dose and stock preparation
  boundaries require correction. Cheesecloth filtering is not sterilization, and the
  manganese hydrate remains unresolved.
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
  - path: data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml
    sha256: 377c3641932b1050f8c2a60e0bbcc860eb2eeaad9378c15f8e5d4bc24ffbeccb
    role: target
  - path: data/normalized_yaml/bacterial/colon_extract_medium.yaml
    sha256: fd1273d5cf2e60458926fa6592bcdb8ab16bad1b1d2f454c3f2c7b2436a33b79
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/colon_extract_medium.yaml.md
    sha256: 421fedec2e658a0f3858680d3b1395f625ad75346972f372aad4462751298aa1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/COLON_EXTRACT_MEDIUM.md
    sha256: 16be0603d9955454109761ad52cb693dc42697af2a8b0eaaca21c976cd55fecd
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/colon_extract_medium.md
    sha256: 680fdf8801fd4c255dddcd11cb18e94a60034a8b4ebbe47df28c8181bd434c74
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
  selection: Authoritative batch065 selection index 5 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003200
targets:
- target_id: CultureMech:003200
  path: data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml
  label: colon_extract_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/colon_extract_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:003200
  command: just validate-schema data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:003200
  command: just validate-strict data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml --workers
    1 --out REVIEW_WORK/batch065/record05/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:003200
  command: just validate-terms data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:003200
  command: just validate-references data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T11:42:55.653715Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 377c3641932b1050f8c2a60e0bbcc860eb2eeaad9378c15f8e5d4bc24ffbeccb
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/colon_extract_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T11:42:55.653866Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: fd1273d5cf2e60458926fa6592bcdb8ab16bad1b1d2f454c3f2c7b2436a33b79
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch065/record05/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T11:30:38.200554Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 5ac2023e68d8c25ab3d637fe9a9640ccec08d0934eea8ff961ae0a99cdf22ce4
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch065/record05/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T11:30:39.111516Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: b6b795b138ee7d28a6a91df1bcc23bd7cb46dc6e9c107a9f8e388c4d09792eea
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch065/record05/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T11:30:40.118407Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: b1b9331b791c17cb81133113bd0d702a3afd276b031aafb8c772f5a94084e230
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch065/record05/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T11:30:40.802246Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: a8c545bb59e2fcb1c8b071ebefa4bdc216de03bc694a6fc35dc03003a15853ad
- evidence_id: jcm854
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=854
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T11:31:07.364105Z'
  support: unknown
  summary: The exact official JCM854 page returned HTTP 200 but states Nothing found.
    This is an unusable primary formulation response; its status must not be promoted
    to recipe support.
  snapshot_sha256: da3a8390d8482d31d17d2afe02260b4e8219b5415295e0a3766f317211ce73ee
- evidence_id: apiJ854
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J854
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T11:31:06.839490Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T11:31:06.834305Z'
  support: supports
  summary: OLS current exact CHEBI:131527 = dipotassium hydrogen phosphate; definition
    ['A potassium salt that is the dipotassium salt of phosphoric acid.']; formula
    ['HO4P.2K']; mass ['174.174']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi17057
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T11:31:06.834240Z'
  support: supports
  summary: OLS current exact CHEBI:17057 = cellobiose; definition ['A glycosylglucose
    consisting of two glucose units linked via a β(1→4) bond.']; formula ['C12H22O11'];
    mass ['342.297']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 3548f79d3274a33683125152944998cffa00bd4fce774c8d872db9003222ed06
- evidence_id: chebi17234
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T11:31:06.827251Z'
  support: supports
  summary: OLS current exact CHEBI:17234 = glucose; definition ['An aldohexose used
    as a source of energy and metabolic intermediate.']; formula ['C6H12O6']; mass
    ['180.156']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi17306
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17306
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T11:31:06.749866Z'
  support: supports
  summary: OLS current exact CHEBI:17306 = maltose; definition ['A glycosylglucose
    consisting of two <small>D</small>-glucopyranose units connected by an α-(1→4)-linkage.'];
    formula ['C12H22O11']; mass ['342.297']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 3ce67048c1fb5137f13f7effdd8dcb3dee6224ee3886441aa45c873652c0ca66
- evidence_id: chebi18067
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18067
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T11:31:06.692333Z'
  support: supports
  summary: OLS current exact CHEBI:18067 = phylloquinone; definition ['A member of
    the class of phylloquinones that consists of 1,4-naphthoquinone having methyl
    and phytyl groups at positions 2 and 3 respectively. The parent of the class of
    phylloquinones.']; formula ['C31H46O2']; mass ['450.707']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: 8419c53a0b06459b563d1c89a1772f099cbe0832ddce3a851fd45ce133d75879
- evidence_id: chebi18222
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18222
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T11:31:06.228971Z'
  support: supports
  summary: OLS current exact CHEBI:18222 = xylose; definition ['An aldopentose, found
    in the embryos of most edible plants and used in medicine to test for malabsorption
    by administration in water to the patient.']; formula ['C5H10O5']; mass ['150.13'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: b2e6878b4d9f125bb7ef0379faa878c5ec4fde42d2c6333df7247d839ff7ff7a
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
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T11:31:06.217554Z'
  support: supports
  summary: OLS current exact CHEBI:32139 = sodium hydrogencarbonate; definition [];
    formula ['CHO3.Na']; mass ['84.006']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T11:31:06.208518Z'
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
  accessed_at: '2026-10-28T11:31:06.196908Z'
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
  accessed_at: '2026-10-28T11:31:05.999284Z'
  support: supports
  summary: OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition
    ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula
    ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T11:31:05.987860Z'
  support: supports
  summary: OLS current exact CHEBI:75836 = iron(2+) sulfate heptahydrate; definition
    ['A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a
    source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage
    treatments; for solid-dosage treatments, the monohydrate is normally used).'];
    formula ['Fe.7H2O.O4S']; mass ['278.013']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T11:31:05.215169Z'
  support: supports
  summary: OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O'];
    mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T11:31:05.215102Z'
  support: supports
  summary: OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition
    ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg'];
    mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86360
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T11:31:05.215030Z'
  support: supports
  summary: OLS current exact CHEBI:86360 = manganese(II) sulfate; definition ['A metal
    sulfate in which the metal component is manganese in the +2 oxidation state.'];
    formula ['Mn.O4S']; mass ['151.001']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: ee3b60385f389c4eeb301cfe59996112ffa9c3c135268559b79e91810a14932b
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T11:31:05.212601Z'
  support: supports
  summary: OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4'];
    mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi91248
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T11:31:04.906794Z'
  support: supports
  summary: OLS current exact CHEBI:91248 = L-cysteine hydrochloride hydrate; definition
    ['A hydrate that is the monohydrate form of <small>L</small>-cysteine hydrochloride.'];
    formula ['C3H7NO2S.H2O.HCl']; mass ['175.637']; obsolete=False. Literal label
    is distinct from supplied-form equivalence.
  snapshot_sha256: 7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch065/record05/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T11:42:55.661587Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 8b80fe249745bc22a99d24e1980f6fa7f33a589e1c54495fc47d561566510543
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/colon_extract_medium.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T11:42:55.662278Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current apiJ854 raw bytes exactly match the cited historical SHA, and 31
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 421fedec2e658a0f3858680d3b1395f625ad75346972f372aad4462751298aa1
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/colon_extract_medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T11:42:55.662299Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 680fdf8801fd4c255dddcd11cb18e94a60034a8b4ebbe47df28c8181bd434c74
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/COLON_EXTRACT_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T11:42:55.662322Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 16be0603d9955454109761ad52cb693dc42697af2a8b0eaaca21c976cd55fecd
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch065/record05/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T11:42:55.662343Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: 265c34bf209b38bfcf16eef133df295519f0b92d546c5ef1017e0815ad047bf3
- evidence_id: writer30
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: target_slot; groundable; apply_to_record
  accessed_at: '2026-10-28T11:42:55.662392Z'
  support: context_only
  summary: Current target_slot preserves existing CHEBI assertions; groundable excludes
    conflicting corpus opinions, and apply_to_record fills ungrounded entries from
    proposals. This writer does not authenticate source amounts or automatically repair
    an existing wrong supplied-form ID.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: writer31
  kind: record_content
  reference: scripts/assign_culturemech_ids.py
  locator: assign_ids; _assign_id_to_file
  accessed_at: '2026-10-28T11:42:55.662419Z'
  support: context_only
  summary: Current assign_ids selects records with missing IDs; _assign_id_to_file
    checks new-ID collisions and appends identifier provenance. Identifier assignment
    does not authenticate recipe content or demonstrate historical source access.
  snapshot_sha256: 81ed213c52804ae98a8add02730d757595e3287fa7b01bc88aee0e587bbb01e1
- evidence_id: writer32
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T11:42:55.662440Z'
  support: context_only
  summary: Current _merge_ingredient_group collapses equal duplicate values without
    summing them and retains the first conflicting value with a flag. This behavior
    is distinct from historical summed-amount artifacts and does not authenticate
    source-specific stock or product structure.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer33
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: merge_duplicate_ingredients; merge_ingredient_group
  accessed_at: '2026-10-28T11:42:55.662460Z'
  support: context_only
  summary: Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group
    retains the first concentration, flags differing values and selects the first
    CHEBI. It cannot establish source stages or justify collapsing independent supplemental
    and product-contained components.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer34
  kind: record_content
  reference: scripts/enrich_with_chebi.py
  locator: RecipeEnricher.enrich_ingredient; enrich_recipe; enrich_file
  accessed_at: '2026-10-28T11:42:55.662481Z'
  support: context_only
  summary: Current RecipeEnricher.enrich_ingredient skips already grounded entries
    and delegates missing-term mapping to ChemicalMapper; enrich_recipe traverses
    ingredient and solution structure, and enrich_file writes results and history.
    Only the read wrapper behavior is claimed here; the mapper is not treated as an
    independent supplied-form authority.
  snapshot_sha256: f18dd6e4317de76cb7379f6c9c6227f9af884c27a0761d7f64143aaf74d8e1dc
- evidence_id: writer35
  kind: record_content
  reference: scripts/enrich_with_mediaingredientmech.py
  locator: main
  accessed_at: '2026-10-28T11:42:55.662505Z'
  support: context_only
  summary: Current main orchestrates a local or cloned MIM repository, its loader
    and ingredient linker. The CLI orchestration was read; it does not itself verify
    source recipe quantities, supplied chemical forms or the validity of historical
    MIM assertions. Linker internals are not claimed as separately audited scientific
    evidence.
  snapshot_sha256: 6357c9d621c3d6e32b28b2982afedfaed384830cea1602a775b0a5f0852c015e
- evidence_id: writer36
  kind: record_content
  reference: scripts/migrate_chebi_regrounding.py
  locator: rewrite_entry; migrate_file
  accessed_at: '2026-10-28T11:42:55.662528Z'
  support: context_only
  summary: Current rewrite_entry applies configured exact-ID/label remaps across primary
    and secondary slots; migrate_file records applied changes. A successful current
    mapping operation does not establish source-specific hydrate or stereochemical
    equivalence.
  snapshot_sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
- evidence_id: writer37
  kind: record_content
  reference: scripts/migrate_legacy_mim_to_chebi.py
  locator: _resolve_chebi; _rewrite_entry
  accessed_at: '2026-10-28T11:42:55.662548Z'
  support: context_only
  summary: Current _resolve_chebi reuses current primary CHEBI where available and
    considers bounded exact-name/synonym matches with a stereo-prefix guard; _rewrite_entry
    retains unresolved links. Current-row presence is distinct from historical validity
    and from source-specific supplied-form equivalence.
  snapshot_sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
- evidence_id: writer38
  kind: record_content
  reference: scripts/normalize_media_names_to_snake_case.py
  locator: process_file; add_curation_history
  accessed_at: '2026-10-28T11:42:55.662567Z'
  support: context_only
  summary: Current process_file preserves the original medium name while normalizing
    its machine name; add_curation_history appends a naming event. Name normalization
    does not prove equivalence of differently maintained source branches or recipe
    variants.
  snapshot_sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
- evidence_id: writer39
  kind: record_content
  reference: scripts/refill_term_labels.py
  locator: refill_text
  accessed_at: '2026-10-28T11:42:55.662590Z'
  support: context_only
  summary: Current refill_text replaces term labels using the current exact identifier
    lookup while preserving other text. Canonical label correspondence is not an independent
    choice of the correct chemical form for the supplied source reagent.
  snapshot_sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
- evidence_id: writer40
  kind: record_content
  reference: scripts/repair_komodo_strain_backlinks.py
  locator: PARENTS; CHILDREN; repair_parent; plan_repairs; _upsert_event
  accessed_at: '2026-10-28T11:42:55.662613Z'
  support: context_only
  summary: Current repair_parent and plan_repairs target only the explicitly listed
    131/777 parents and their two strain children. They do not repair the selected
    records. _upsert_event replaces a matching curator/action event or appends it;
    this existing behavior is not permission to rewrite history during this review.
  snapshot_sha256: 06d56149f4e8333f31ae6dd7e4b9127881227810bc957429c849ba00de21c963
- evidence_id: writer41
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: repair_ingredient; repair_record
  accessed_at: '2026-10-28T11:42:55.662631Z'
  support: context_only
  summary: Current repair_ingredient and repair_record act on parsed IDENTICAL_PARTS
    duplicate notes. This bounded repair is not a general solution for product decomposition,
    stock flattening or differing source formulations.
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: writer42
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata
  accessed_at: '2026-10-28T11:42:55.662658Z'
  support: context_only
  summary: Current DSMZCompositionResolver.merge_composition copies ingredients and
    solutions, fills pH when absent and copies physical/medium type, but does not
    copy preparation steps. _add_enrichment_metadata records a naive current timestamp.
    This explains a present omission risk, not historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer43
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T11:42:55.662682Z'
  support: context_only
  summary: Current _convert_to_culturemech constructs source notes and default LIQUID
    with empty ingredients. Its time.strftime format contains %f, which is unsupported
    here and is consistent with literal .fZ in stored import events. Current code
    does not authenticate the original retrieval or justify rewriting historical time.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer44
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps;
    _classify_preparation_action
  accessed_at: '2026-10-28T11:42:55.662713Z'
  support: context_only
  summary: Current _parse_api_composition considers the primary recipe, prefers provider
    g_l when available and excludes recognized solvents; _is_api_stock_addition distinguishes
    stock additions. _parse_api_solutions retains separate stock structure. _parse_preparation_steps
    collects solution prose. These present behaviors do not establish historical execution
    and cannot justify interpreting flattened stock rates as final-medium concentrations.
    _parse_preparation_steps collects all solution steps; _classify_preparation_action
    maps a filter substring to FILTER_STERILIZE. This can misclassify the actual cheesecloth
    instruction.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer45
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T11:42:55.662736Z'
  support: context_only
  summary: Current formulation_content retains exact scientific quantities, preparation
    and other scientific fields; merge_formulation_evidence rejects incompatible projections
    and unions evidence at matching scopes. A source-equivalence claim is not established
    by shared ingredient identities.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer46
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations; group_recipes
  accessed_at: '2026-10-28T11:42:55.662755Z'
  support: context_only
  summary: Current group_formulations calls group_recipes with fail_on_invalid=True
    and FormulationFingerprinter. Expected standalone or unfingerprintable records
    are excluded; malformed or unexpected inputs raise. Valid records are grouped
    by full scientific content. This guard does not retrieve or authenticate source
    recipes.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer47
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T11:42:55.662776Z'
  support: context_only
  summary: Current merge_group routes a single maintained owner with merge metadata;
    multiple owners pass through conservative merge_formulation_evidence. Regenerating
    from an unrepaired owner retains its defects. Current conservative behavior is
    credited and does not establish how the old generated record was produced.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer48
  kind: record_content
  reference: src/culturemech/validation/schema_defaulter.py
  locator: apply_defaults; _fix_ingredient; _fix_solution
  accessed_at: '2026-10-28T11:42:55.662797Z'
  support: context_only
  summary: Current apply_defaults, _fix_ingredient and _fix_solution can insert VARIABLE
    amounts and placeholder names for structural completeness. A default is not evidence
    for a dose, composition, solution identity or denominator; existing default-history
    events remain contextual.
  snapshot_sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch065/record05/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T11:42:55.669011Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: a90ad5a78a0c360ac2a021f9a9e32f73e5a37a7b53b9aac247cdd2ffe726e28c
assessments:
- assessment_id: a1
  area: identity
  topic: Exact J854 source identity and availability
  outcome: unknown
  summary: The selected target and sole maintained owner identify JCM854. The current
    MediaDive J854 recipe contains the same main ingredients and separate A/B/C/D/hemin
    structure. The exact JCM primary page returns HTTP200 with Nothing found, so the
    primary recipe is unavailable; the source review remains partial and no organism-specific
    association is inferred.
  target_ids:
  - CultureMech:003200
  evidence_ids:
  - local0
  - local1
  - apiJ854
  - jcm854
- assessment_id: a2
  area: consistency
  topic: Classification and source-specific controls
  outcome: supported
  summary: Complex, undefined, liquid classification is consistent with yeast extract,
    peptone and colon extract. Main pH 7.0 is retained correctly. Solution D preparation
    temperatures and incubation/storage times are not general target-organism growth
    conditions.
  target_ids:
  - CultureMech:003200
  evidence_ids:
  - local0
  - apiJ854
- assessment_id: a3
  area: grounding
  topic: Chemical forms and source-side molarity
  outcome: concern
  summary: Current labels and exact MIM identifier rows agree. Calcium dihydrate,
    magnesium hexahydrate, cobalt hexahydrate, ferrous heptahydrate and L-cysteine
    hydrochloride monohydrate are already represented by corresponding hydrate terms.
    MnSO4 x n H2O remains an unspecified hydrate while CHEBI:86360 encodes MnSO4 without
    water; do not infer n or use its anhydrous mass as exact supplied-form evidence.
    Generic source Resazurin is not automatically a sodium-salt claim. The provider
    cobalt mmol conversion conflicts with its named hydrate and mass.
  target_ids:
  - CultureMech:003200
  evidence_ids:
  - grounding
  - chebi86360
  - chebi53503
  - apiJ854
- assessment_id: a4
  area: provenance
  topic: Historical assertions and current writers
  outcome: unknown
  summary: All three historical reports were read in full. The current API bytes authenticate
    the exact quoted payload and objects when their historical digest matches, but
    the old blanket stock conflict does not apply to the five separately supported
    main rates. No formulation claims are attached in either selected document. Current
    one-owner merging carries existing content forward; it does not independently
    reconstruct missing stock boundaries. Historical events remain unchanged; future
    remediation appends actual verified context. Current conservative merging preserves
    scientific fields and rejects incompatible formulations. Inspected writer behavior
    is described separately by exact file and function; it does not prove historical
    execution.
  target_ids:
  - CultureMech:003200
  evidence_ids:
  - history-auth
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
  - writer43
  - writer44
  - writer45
  - writer46
  - writer47
  - writer48
- assessment_id: a5
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 38 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:003200
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:003200",
    "selected_concentration_field_count": 38, "selected_concentration_fields_covered":
    38, "decisions": [{"decision_id": "q1", "subject": "Yeast extract", "local_fields":
    [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path":
    "ingredients[0].concentration", "original": {"value": "3.15657", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path":
    "ingredients[0].concentration", "original": {"value": "3.15657", "unit": "G_PER_L"}}],
    "decision": "evidence_only", "stage": "Main-recipe rate on the explicit provider
    basis", "interpretation": "The stored rate equals provider g_l=3.15657 for 5 g
    in the main recipe. The API metadata volume is 1584 ml; this is provider normalization,
    not independently established final volume. Five main rates are credited rather
    than repeated as blanket historical stock conflicts. No attached formulation evidence
    exists.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key":
    "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at":
    "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.15657,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q2", "subject": "Trypticase peptone", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "3.15657",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "3.15657",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main-recipe rate
    on the explicit provider basis", "interpretation": "The stored rate equals provider
    g_l=3.15657 for 5 g in the main recipe. The API metadata volume is 1584 ml; this
    is provider normalization, not independently established final volume. Five main
    rates are credited rather than repeated as blanket historical stock conflicts.
    No attached formulation evidence exists.", "sources": [{"locator": "$.data.solutions[0].recipe[5]",
    "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\":
    124,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.15657,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q3", "subject": "NaHCO3", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "3.15657",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "3.15657",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main-recipe rate
    on the explicit provider basis", "interpretation": "The stored rate equals provider
    g_l=3.15657 for 5 g in the main recipe. The API metadata volume is 1584 ml; this
    is provider normalization, not independently established final volume. Five main
    rates are credited rather than repeated as blanket historical stock conflicts.
    No attached formulation evidence exists.", "sources": [{"locator": "$.data.solutions[0].recipe[6]",
    "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.15657,\n                        \"mmol_l\":
    37.575,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q4", "subject": "Resazurin", "local_fields":
    [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path":
    "ingredients[3].concentration", "original": {"value": "0.000631313", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path":
    "ingredients[3].concentration", "original": {"value": "0.000631313", "unit": "G_PER_L"}}],
    "decision": "evidence_only", "stage": "Main-recipe rate on the explicit provider
    basis", "interpretation": "The stored rate equals provider g_l=0.000631313 for
    1 mg in the main recipe. The API metadata volume is 1584 ml; this is provider
    normalization, not independently established final volume. Five main rates are
    credited rather than repeated as blanket historical stock conflicts. No attached
    formulation evidence exists.", "sources": [{"locator": "$.data.solutions[0].recipe[7]",
    "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\":
    25,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.000631313,\n                        \"mmol_l\":
    0.00275454,\n                        \"optional\": 0\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q5", "subject":
    "L-Cysteine HCl x H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.631313",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.631313",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Main-recipe rate
    on the explicit provider basis", "interpretation": "The stored rate equals provider
    g_l=0.631313 for 1 g in the main recipe. The API metadata volume is 1584 ml; this
    is provider normalization, not independently established final volume. Five main
    rates are credited rather than repeated as blanket historical stock conflicts.
    No attached formulation evidence exists.", "sources": [{"locator": "$.data.solutions[0].recipe[8]",
    "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\":
    770,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.631313,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q6", "subject": "NaCl", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "5.4", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "5.4", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Composition of Solution A, separate
    from its receiving dose", "interpretation": "The stored 5.4 G_PER_L is the provider''s
    stock strength, sourced from 5.4 g in the separate Solution A recipe. It is incorrectly
    placed in the main ingredient list. Preserve the exact stock component and its
    form; represent the separate 167 ml stock addition. Listed stock water and main
    volume metadata do not license an assumed final-medium dilution.", "sources":
    [{"locator": "$.data.solutions[1].recipe[0]", "source_key": "apiJ854", "reference":
    "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 5.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5.4,\n                        \"mmol_l\":
    92.4025,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key":
    "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at":
    "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\":
    4830,\n                        \"amount\": 167,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q7", "subject": "KH2PO4", "local_fields":
    [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path":
    "ingredients[7].concentration", "original": {"value": "2.7", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path":
    "ingredients[7].concentration", "original": {"value": "2.7", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Composition of Solution A, separate from its
    receiving dose", "interpretation": "The stored 2.7 G_PER_L is the provider''s
    stock strength, sourced from 2.7 g in the separate Solution A recipe. It is incorrectly
    placed in the main ingredient list. Preserve the exact stock component and its
    form; represent the separate 167 ml stock addition. Listed stock water and main
    volume metadata do not license an assumed final-medium dilution.", "sources":
    [{"locator": "$.data.solutions[1].recipe[1]", "source_key": "apiJ854", "reference":
    "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 2.7,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.7,\n                        \"mmol_l\":
    19.8404,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key":
    "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at":
    "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\":
    4830,\n                        \"amount\": 167,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q8", "subject": "CaCl2 x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path":
    "ingredients[8].concentration", "original": {"value": "0.16", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path":
    "ingredients[8].concentration", "original": {"value": "0.16", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Composition of Solution A, separate from its
    receiving dose", "interpretation": "The stored 0.16 G_PER_L is the provider''s
    stock strength, sourced from 0.16 g in the separate Solution A recipe. It is incorrectly
    placed in the main ingredient list. Preserve the exact stock component and its
    form; represent the separate 167 ml stock addition. Listed stock water and main
    volume metadata do not license an assumed final-medium dilution.", "sources":
    [{"locator": "$.data.solutions[1].recipe[2]", "source_key": "apiJ854", "reference":
    "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.16,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.16,\n                        \"mmol_l\":
    1.08832,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key":
    "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at":
    "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\":
    4830,\n                        \"amount\": 167,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q9", "subject": "MgCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path":
    "ingredients[9].concentration", "original": {"value": "0.12", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path":
    "ingredients[9].concentration", "original": {"value": "0.12", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Composition of Solution A, separate from its
    receiving dose", "interpretation": "The stored 0.12 G_PER_L is the provider''s
    stock strength, sourced from 0.12 g in the separate Solution A recipe. It is incorrectly
    placed in the main ingredient list. Preserve the exact stock component and its
    form; represent the separate 167 ml stock addition. Listed stock water and main
    volume metadata do not license an assumed final-medium dilution.", "sources":
    [{"locator": "$.data.solutions[1].recipe[3]", "source_key": "apiJ854", "reference":
    "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.12,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.12,\n                        \"mmol_l\":
    0.590252,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key":
    "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at":
    "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\":
    4830,\n                        \"amount\": 167,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q10", "subject": "MnSO4 x n H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path":
    "ingredients[10].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path":
    "ingredients[10].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Composition of Solution A, separate from its
    receiving dose", "interpretation": "The stored 0.07 G_PER_L is the provider''s
    stock strength, sourced from 0.07 g in the separate Solution A recipe. It is incorrectly
    placed in the main ingredient list. Preserve the exact stock component and its
    form; represent the separate 167 ml stock addition. Listed stock water and main
    volume metadata do not license an assumed final-medium dilution.", "sources":
    [{"locator": "$.data.solutions[1].recipe[4]", "source_key": "apiJ854", "reference":
    "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"MnSO4 x n H2O\",\n                        \"compound_id\":
    1000,\n                        \"amount\": 0.07,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.07,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "$.data.solutions[0].recipe[0]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\":
    4830,\n                        \"amount\": 167,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q11", "subject": "CoCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path":
    "ingredients[11].concentration", "original": {"value": "0.06", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path":
    "ingredients[11].concentration", "original": {"value": "0.06", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Composition of Solution A, separate from its
    receiving dose", "interpretation": "The stored 0.06 G_PER_L is the provider''s
    stock strength, sourced from 0.06 g in the separate Solution A recipe. It is incorrectly
    placed in the main ingredient list. Preserve the exact stock component and its
    form; represent the separate 167 ml stock addition. Listed stock water and main
    volume metadata do not license an assumed final-medium dilution.", "sources":
    [{"locator": "$.data.solutions[1].recipe[5]", "source_key": "apiJ854", "reference":
    "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 0.06,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.06,\n                        \"mmol_l\":
    0.462111,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key":
    "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at":
    "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\":
    4830,\n                        \"amount\": 167,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q12", "subject": "(NH4)2SO4", "local_fields":
    [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path":
    "ingredients[12].concentration", "original": {"value": "5.4", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path":
    "ingredients[12].concentration", "original": {"value": "5.4", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Composition of Solution A, separate from its
    receiving dose", "interpretation": "The stored 5.4 G_PER_L is the provider''s
    stock strength, sourced from 5.4 g in the separate Solution A recipe. It is incorrectly
    placed in the main ingredient list. Preserve the exact stock component and its
    form; represent the separate 167 ml stock addition. Listed stock water and main
    volume metadata do not license an assumed final-medium dilution.", "sources":
    [{"locator": "$.data.solutions[1].recipe[6]", "source_key": "apiJ854", "reference":
    "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\":
    27,\n                        \"amount\": 5.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5.4,\n                        \"mmol_l\":
    40.8657,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key":
    "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at":
    "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\":
    4830,\n                        \"amount\": 167,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q13", "subject": "FeSO4 x 7 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path":
    "ingredients[13].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path":
    "ingredients[13].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Composition of Solution A, separate from its
    receiving dose", "interpretation": "The stored 0.05 G_PER_L is the provider''s
    stock strength, sourced from 0.05 g in the separate Solution A recipe. It is incorrectly
    placed in the main ingredient list. Preserve the exact stock component and its
    form; represent the separate 167 ml stock addition. Listed stock water and main
    volume metadata do not license an assumed final-medium dilution.", "sources":
    [{"locator": "$.data.solutions[1].recipe[7]", "source_key": "apiJ854", "reference":
    "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.05,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.179846,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[0]", "source_key":
    "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at":
    "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\":
    4830,\n                        \"amount\": 167,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q14", "subject": "K2HPO4", "local_fields":
    [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path":
    "ingredients[14].concentration", "original": {"value": "2.7", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path":
    "ingredients[14].concentration", "original": {"value": "2.7", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Composition of Solution B, separate from its
    receiving dose", "interpretation": "The stored 2.7 G_PER_L is the provider''s
    stock strength, sourced from 2.7 g in the separate Solution B recipe. It is incorrectly
    placed in the main ingredient list. Preserve the exact stock component and its
    form; represent the separate 167 ml stock addition. Listed stock water and main
    volume metadata do not license an assumed final-medium dilution.", "sources":
    [{"locator": "$.data.solutions[2].recipe[0]", "source_key": "apiJ854", "reference":
    "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 2.7,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.7,\n                        \"mmol_l\":
    15.5016,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[1]", "source_key":
    "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at":
    "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\":
    4831,\n                        \"amount\": 167,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q15", "subject": "Glucose", "local_fields":
    [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path":
    "ingredients[15].concentration", "original": {"value": "50", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path":
    "ingredients[15].concentration", "original": {"value": "50", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Composition of Solution C, separate from its
    receiving dose", "interpretation": "The stored 50 G_PER_L is the provider''s stock
    strength, sourced from 50 g in the separate Solution C recipe. It is incorrectly
    placed in the main ingredient list. Preserve the exact stock component and its
    form; represent the separate 40 ml stock addition. Listed stock water and main
    volume metadata do not license an assumed final-medium dilution.", "sources":
    [{"locator": "$.data.solutions[3].recipe[0]", "source_key": "apiJ854", "reference":
    "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\":
    5,\n                        \"amount\": 50,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\":
    277.531,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[2]", "source_key":
    "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at":
    "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\":
    4832,\n                        \"amount\": 40,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q16", "subject": "Maltose", "local_fields":
    [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path":
    "ingredients[16].concentration", "original": {"value": "50", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path":
    "ingredients[16].concentration", "original": {"value": "50", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Composition of Solution C, separate from its
    receiving dose", "interpretation": "The stored 50 G_PER_L is the provider''s stock
    strength, sourced from 50 g in the separate Solution C recipe. It is incorrectly
    placed in the main ingredient list. Preserve the exact stock component and its
    form; represent the separate 40 ml stock addition. Listed stock water and main
    volume metadata do not license an assumed final-medium dilution.", "sources":
    [{"locator": "$.data.solutions[3].recipe[1]", "source_key": "apiJ854", "reference":
    "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Maltose\",\n                        \"compound_id\":
    171,\n                        \"amount\": 50,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\":
    146.071,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[2]", "source_key":
    "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at":
    "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\":
    4832,\n                        \"amount\": 40,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q17", "subject": "Cellobiose", "local_fields":
    [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path":
    "ingredients[17].concentration", "original": {"value": "50", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path":
    "ingredients[17].concentration", "original": {"value": "50", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Composition of Solution C, separate from its
    receiving dose", "interpretation": "The stored 50 G_PER_L is the provider''s stock
    strength, sourced from 50 g in the separate Solution C recipe. It is incorrectly
    placed in the main ingredient list. Preserve the exact stock component and its
    form; represent the separate 40 ml stock addition. Listed stock water and main
    volume metadata do not license an assumed final-medium dilution.", "sources":
    [{"locator": "$.data.solutions[3].recipe[2]", "source_key": "apiJ854", "reference":
    "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Cellobiose\",\n                        \"compound_id\":
    214,\n                        \"amount\": 50,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\":
    146.071,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[2]", "source_key":
    "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at":
    "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\":
    4832,\n                        \"amount\": 40,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q18", "subject": "Xylose", "local_fields":
    [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path":
    "ingredients[18].concentration", "original": {"value": "50", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path":
    "ingredients[18].concentration", "original": {"value": "50", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Composition of Solution C, separate from its
    receiving dose", "interpretation": "The stored 50 G_PER_L is the provider''s stock
    strength, sourced from 50 g in the separate Solution C recipe. It is incorrectly
    placed in the main ingredient list. Preserve the exact stock component and its
    form; represent the separate 40 ml stock addition. Listed stock water and main
    volume metadata do not license an assumed final-medium dilution.", "sources":
    [{"locator": "$.data.solutions[3].recipe[3]", "source_key": "apiJ854", "reference":
    "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Xylose\",\n                        \"compound_id\":
    1107,\n                        \"amount\": 50,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\":
    333.045,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[2]", "source_key":
    "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at":
    "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\":
    4832,\n                        \"amount\": 40,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q19", "subject": "Vitamin K1", "local_fields":
    [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path":
    "ingredients[5].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path":
    "ingredients[5].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "Liquid addition of a percentage stock", "interpretation":
    "The source is 0.2 ml of Vitamin K1 with attribute 0.5%, not 0.2 G_PER_L phylloquinone.
    The percentage basis and stock solvent are not specified, so no mass concentration,
    density or final-medium rate is invented. Preserve the liquid dose and unresolved
    percent basis.", "sources": [{"locator": "$.data.solutions[0].recipe[9]", "source_key":
    "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "source_text_sha256":
    "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91", "accessed_at":
    "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Vitamin K1\",\n                        \"compound_id\":
    150,\n                        \"attribute\": \"0.5%\",\n                        \"amount\":
    0.2,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q20", "subject": "Solution A receiving addition", "local_fields": [], "decision":
    "add", "stage": "Absolute main-recipe stock addition", "interpretation": "Represent
    the exact 167 ml of Solution A (provider solution 4830) with its own composition/preparation
    boundary. This dose is absent as a solution addition in both selected documents.
    Do not relabel it ml/L without an explicit final-volume basis.", "sources": [{"locator":
    "$.data.solutions[0].recipe[0]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\":
    4830,\n                        \"amount\": 167,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q21", "subject": "Solution B receiving
    addition", "local_fields": [], "decision": "add", "stage": "Absolute main-recipe
    stock addition", "interpretation": "Represent the exact 167 ml of Solution B (provider
    solution 4831) with its own composition/preparation boundary. This dose is absent
    as a solution addition in both selected documents. Do not relabel it ml/L without
    an explicit final-volume basis.", "sources": [{"locator": "$.data.solutions[0].recipe[1]",
    "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\":
    4831,\n                        \"amount\": 167,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q22", "subject": "Solution C receiving
    addition", "local_fields": [], "decision": "add", "stage": "Absolute main-recipe
    stock addition", "interpretation": "Represent the exact 40 ml of Solution C (provider
    solution 4832) with its own composition/preparation boundary. This dose is absent
    as a solution addition in both selected documents. Do not relabel it ml/L without
    an explicit final-volume basis.", "sources": [{"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\":
    4832,\n                        \"amount\": 40,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q23", "subject": "Solution D receiving
    addition", "local_fields": [], "decision": "add", "stage": "Absolute main-recipe
    stock addition", "interpretation": "Represent the exact 200 ml of Solution D (provider
    solution 4833) with its own composition/preparation boundary. This dose is absent
    as a solution addition in both selected documents. Do not relabel it ml/L without
    an explicit final-volume basis.", "sources": [{"locator": "$.data.solutions[0].recipe[3]",
    "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\":
    4833,\n                        \"amount\": 200,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q24", "subject": "Hemin solution receiving
    addition", "local_fields": [], "decision": "add", "stage": "Absolute main-recipe
    stock addition", "interpretation": "Represent the exact 10 ml of Hemin solution
    (provider solution 4218) with its own composition/preparation boundary. This dose
    is absent as a solution addition in both selected documents. Do not relabel it
    ml/L without an explicit final-volume basis.", "sources": [{"locator": "$.data.solutions[0].recipe[10]",
    "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"solution\": \"Hemin solution\",\n                        \"solution_id\":
    4218,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q25", "subject": "Main sol. J854 water",
    "local_fields": [], "decision": "add", "stage": "Separate solvent input", "interpretation":
    "The source lists 1000 ml water in this specific recipe. Preserve each independently
    scoped solvent input; do not merge stock water with main water or treat listed
    water as an explicit make-up-to-final-volume instruction.", "sources": [{"locator":
    "$.data.solutions[0].recipe[11]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q26", "subject": "Solution A water", "local_fields":
    [], "decision": "add", "stage": "Separate solvent input", "interpretation": "The
    source lists 1000 ml water in this specific recipe. Preserve each independently
    scoped solvent input; do not merge stock water with main water or treat listed
    water as an explicit make-up-to-final-volume instruction.", "sources": [{"locator":
    "$.data.solutions[1].recipe[8]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q27", "subject": "Solution B water", "local_fields":
    [], "decision": "add", "stage": "Separate solvent input", "interpretation": "The
    source lists 1000 ml water in this specific recipe. Preserve each independently
    scoped solvent input; do not merge stock water with main water or treat listed
    water as an explicit make-up-to-final-volume instruction.", "sources": [{"locator":
    "$.data.solutions[2].recipe[1]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q28", "subject": "Solution C water", "local_fields":
    [], "decision": "add", "stage": "Separate solvent input", "interpretation": "The
    source lists 1000 ml water in this specific recipe. Preserve each independently
    scoped solvent input; do not merge stock water with main water or treat listed
    water as an explicit make-up-to-final-volume instruction.", "sources": [{"locator":
    "$.data.solutions[3].recipe[4]", "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q29", "subject": "Main pH", "local_fields":
    [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml", "field_path":
    "ph_value", "original": 7.0}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml",
    "field_path": "ph_value", "original": 7.0}, {"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml",
    "field_path": "preparation_steps[0].description", "original": "Adjust pH to 7.0."},
    {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path":
    "preparation_steps[0].description", "original": "Adjust pH to 7.0."}], "decision":
    "evidence_only", "stage": "Main-medium preparation", "interpretation": "The stored
    pH 7.0 and first preparation description match the source. This main control is
    distinct from the pH adjustment during preparation of Solution D.", "sources":
    [{"locator": "$.data.solutions[0].steps[0]", "source_key": "apiJ854", "reference":
    "https://mediadive.dsmz.de/rest/medium/J854", "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"step\":
    \"Adjust pH to 7.0.\"\n                    }", "quote_representation": "raw JSON
    object"}]}, {"decision_id": "q30", "subject": "Retained Solution D preparation
    quantities", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml",
    "field_path": "preparation_steps[1].description", "original": "Dilute (1:1, w/v)
    the content of terminal pig colon with the following buffer: 167 ml Solution A
    (see above) and 167 ml Solution B (see above). Make up to 1.0 L with distilled
    water. Stomach the suspension and filter through a cheese cloth. Incubate at 37C
    for 48 h and adjust pH to 7.0. Centrifuge at 20,000 x g for 20 min. Retrieve the
    supernatant and store at -20C until use."}, {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml",
    "field_path": "preparation_steps[1].description", "original": "Dilute (1:1, w/v)
    the content of terminal pig colon with the following buffer: 167 ml Solution A
    (see above) and 167 ml Solution B (see above). Make up to 1.0 L with distilled
    water. Stomach the suspension and filter through a cheese cloth. Incubate at 37C
    for 48 h and adjust pH to 7.0. Centrifuge at 20,000 x g for 20 min. Retrieve the
    supernatant and store at -20C until use."}], "decision": "evidence_only", "stage":
    "Preparation of the colon-extract stock, not main culture conditions", "interpretation":
    "The existing text faithfully retains 1:1 w/v extraction, 167 ml each of Solutions
    A/B, make-up to 1.0 L, cheesecloth filtration, 37 C for 48 h, pH 7.0, 20000 x
    g for 20 min and storage at -20 C. Credit those retained words while restoring
    their Solution D boundary. These are preparation/storage controls, not experimental
    organism-growth evidence.", "sources": [{"locator": "$.data.solutions[4].steps[0]",
    "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"step\":
    \"Dilute (1:1, w/v) the content of terminal pig colon with the following buffer:
    167 ml Solution A (see above) and 167 ml Solution B (see above). Make up to 1.0
    L with distilled water. Stomach the suspension and filter through a cheese cloth.
    Incubate at 37C for 48 h and adjust pH to 7.0. Centrifuge at 20,000 x g for 20
    min. Retrieve the supernatant and store at -20C until use.\"\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q31", "subject":
    "Cheesecloth action code", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml",
    "field_path": "preparation_steps[1].action", "original": "FILTER_STERILIZE"},
    {"record_path": "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path":
    "preparation_steps[1].action", "original": "FILTER_STERILIZE"}], "decision": "conflict",
    "stage": "Mechanical stock filtration", "interpretation": "FILTER_STERILIZE is
    not supported by filtering through cheesecloth. Preserve the actual extraction/filtration/centrifugation
    description and choose a non-sterilizing representation; neither sterility nor
    a membrane filter is specified.", "sources": [{"locator": "$.data.solutions[4].steps[0]",
    "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"step\":
    \"Dilute (1:1, w/v) the content of terminal pig colon with the following buffer:
    167 ml Solution A (see above) and 167 ml Solution B (see above). Make up to 1.0
    L with distilled water. Stomach the suspension and filter through a cheese cloth.
    Incubate at 37C for 48 h and adjust pH to 7.0. Centrifuge at 20,000 x g for 20
    min. Retrieve the supernatant and store at -20C until use.\"\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q32", "subject":
    "Retained hemin-stock preparation", "local_fields": [{"record_path": "data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml",
    "field_path": "preparation_steps[2].description", "original": "Dissolve 50 mg
    hemin first in 1 ml of 1 N NaOH. Then adjust volume to 100 ml."}, {"record_path":
    "data/normalized_yaml/bacterial/colon_extract_medium.yaml", "field_path": "preparation_steps[2].description",
    "original": "Dissolve 50 mg hemin first in 1 ml of 1 N NaOH. Then adjust volume
    to 100 ml."}], "decision": "evidence_only", "stage": "Separate hemin stock", "interpretation":
    "The existing words correctly state 50 mg hemin dissolved first in 1 ml of 1 N
    NaOH, then adjusted to 100 ml. This explicit final stock volume gives 0.5 mg/ml
    (0.5 g/L) stock, but the separate 10 ml receiving dose and main final volume must
    not be conflated. Restore the stock boundary and preserve the source NaOH normality
    without adding an unsupported final alkali rate.", "sources": [{"locator": "$.data.solutions[5].steps[0]",
    "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve 50 mg hemin first in 1 ml of 1 N NaOH. Then adjust volume to 100 ml.\"\n                    }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].recipe[10]",
    "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"solution\": \"Hemin solution\",\n                        \"solution_id\":
    4218,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q33", "subject": "Provider main volume
    metadata", "local_fields": [], "decision": "unsupported", "stage": "Provider denominator
    with an internal accounting limitation", "interpretation": "The API volume=1584
    ml equals the listed 1000+167+167+40+200+10 ml additions and omits the separate
    0.2 ml Vitamin K1. Neither that nominal sum nor the alternative 1584.2 ml sum
    establishes a measured final volume. Keep the five existing provider g_l rates
    explicitly qualified and preserve source batch quantities; do not change rates
    merely by choosing a new divisor.", "sources": [{"locator": "$.data.solutions[0]",
    "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                \"id\":
    4829,\n                \"name\": \"Main sol. J854\",\n                \"volume\":
    1584,\n                \"recipe\": [\n                    {\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\":
    4830,\n                        \"amount\": 167,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\":
    4831,\n                        \"amount\": 167,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\":
    4832,\n                        \"amount\": 40,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    4,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\":
    4833,\n                        \"amount\": 200,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.15657,\n                        \"optional\":
    0\n                    },\n                    {\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\":
    124,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.15657,\n                        \"optional\":
    0\n                    },\n                    {\n                        \"recipe_order\":
    7,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.15657,\n                        \"mmol_l\":
    37.575,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\":
    25,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.000631313,\n                        \"mmol_l\":
    0.00275454,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    9,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\":
    770,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.631313,\n                        \"optional\":
    0\n                    },\n                    {\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Vitamin K1\",\n                        \"compound_id\":
    150,\n                        \"attribute\": \"0.5%\",\n                        \"amount\":
    0.2,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    },\n                    {\n                        \"recipe_order\":
    11,\n                        \"solution\": \"Hemin solution\",\n                        \"solution_id\":
    4218,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }\n                ],\n                \"steps\":
    [\n                    {\n                        \"step\": \"Adjust pH to 7.0.\"\n                    }\n                ]\n            }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q34", "subject":
    "Cobalt provider molar conversion", "local_fields": [], "decision": "conflict",
    "stage": "Source-side derived molarity of Solution A", "interpretation": "The
    source mass is 0.06 g with explicit CoCl2 x 6 H2O and the correct current local
    CHEBI:53503. Using the current authoritative mass 237.929 g/mol gives about 0.252175
    mmol/L on the provider stock basis, whereas the API prints 0.462111 mmol/L. Preserve
    the mass and hydrate; do not transfer the inconsistent derived mmol value into
    the record or substitute an anhydrous mass.", "sources": [{"locator": "$.data.solutions[1].recipe[5]",
    "source_key": "apiJ854", "reference": "https://mediadive.dsmz.de/rest/medium/J854",
    "source_raw_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "source_text_sha256": "b2ef7d88933b5a9cca07f6df71db35a6e6e759c630babcd1c049ebcf88d09d91",
    "accessed_at": "2026-10-28T11:31:06.839490Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 0.06,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.06,\n                        \"mmol_l\":
    0.462111,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$._embedded.terms[0]", "source_key": "chebi53503",
    "reference": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503",
    "source_raw_sha256": "c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d",
    "source_text_sha256": "c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d",
    "accessed_at": "2026-10-28T11:31:06.208518Z", "exact_source_quote": "{\n      \"iri\"
    : \"http://purl.obolibrary.org/obo/CHEBI_53503\",\n      \"lang\" : \"en\",\n      \"description\"
    : [ \"A hydrate of cobalt chloride containing cobalt (in +2 oxidation state),
    chloride and water moieties in the ratio 1:2:6.\" ],\n      \"synonyms\" : [ \"Cobalt
    chloride hexahydrate\", \"Cobalt dichloride hexahydrate\", \"Cobalt(II) chloride
    hexahydrate\", \"Cobalt(II) chloride--water (1/7)\", \"Cobalt(II) chloride--water
    (1/7)\", \"cobalt (II) chloride hexahydrate\", \"cobalt chloride hydrate\", \"cobalt(2+)
    dichloride hexahydrate\", \"cobalt(2+) dichloride hexahydrate\" ],\n      \"annotation\"
    : {\n        \"charge\" : [ 0.0 ],\n        \"database_cross_reference\" : [ \"cas:7791-13-1\",
    \"gmelin:16833\", \"patent:CN101077120\", \"pubmed:11207315\", \"pubmed:16870561\",
    \"pubmed:2025398\", \"pubmed:21721333\", \"pubmed:8404951\", \"pubmed:8857117\",
    \"pubmed:9106780\", \"reaxys:11403444\" ],\n        \"generalized_empirical_formula\"
    : [ \"2Cl.Co.6H2O\" ],\n        \"has_obo_namespace\" : [ \"chebi_ontology\" ],\n        \"id\"
    : [ \"CHEBI:53503\" ],\n        \"inchi_key_string\" : [ \"GFHNAMRJFCEERV-UHFFFAOYSA-L\"
    ],\n        \"inchi_string\" : [ \"InChI=1S/2ClH.Co.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2\"
    ],\n        \"mass\" : [ \"237.929\" ],\n        \"monoisotopic_mass\" : [ \"236.93429\"
    ],\n        \"smiles_string\" : [ \"O.O.O.O.O.O.[Cl-].[Cl-].[Co+2]\" ]\n      },\n      \"label\"
    : \"cobalt chloride hexahydrate\",\n      \"ontology_name\" : \"chebi\",\n      \"ontology_prefix\"
    : \"CHEBI\",\n      \"ontology_iri\" : \"http://purl.obolibrary.org/obo/chebi.owl\",\n      \"is_obsolete\"
    : false,\n      \"term_replaced_by\" : null,\n      \"is_defining_ontology\" :
    true,\n      \"has_children\" : false,\n      \"is_root\" : false,\n      \"short_form\"
    : \"CHEBI_53503\",\n      \"obo_id\" : \"CHEBI:53503\",\n      \"in_subset\" :
    [ \"3_STAR\" ],\n      \"obo_definition_citation\" : null,\n      \"obo_xref\"
    : [ {\n        \"database\" : \"cas\",\n        \"id\" : \"7791-13-1\",\n        \"description\"
    : \"cas\",\n        \"url\" : \"https://commonchemistry.cas.org/detail?cas_rn=7791-13-1\"\n      },
    {\n        \"database\" : \"gmelin\",\n        \"id\" : \"16833\",\n        \"description\"
    : \"gmelin\",\n        \"url\" : null\n      }, {\n        \"database\" : \"patent\",\n        \"id\"
    : \"CN101077120\",\n        \"description\" : \"patent\",\n        \"url\" : \"https://www.google.com/patents/CN101077120\"\n      },
    {\n        \"database\" : \"pubmed\",\n        \"id\" : \"11207315\",\n        \"description\"
    : \"pubmed\",\n        \"url\" : \"https://pubmed.ncbi.nlm.nih.gov/11207315/\"\n      },
    {\n        \"database\" : \"pubmed\",\n        \"id\" : \"16870561\",\n        \"description\"
    : \"pubmed\",\n        \"url\" : \"https://pubmed.ncbi.nlm.nih.gov/16870561/\"\n      },
    {\n        \"database\" : \"pubmed\",\n        \"id\" : \"2025398\",\n        \"description\"
    : \"pubmed\",\n        \"url\" : \"https://pubmed.ncbi.nlm.nih.gov/2025398/\"\n      },
    {\n        \"database\" : \"pubmed\",\n        \"id\" : \"21721333\",\n        \"description\"
    : \"pubmed\",\n        \"url\" : \"https://pubmed.ncbi.nlm.nih.gov/21721333/\"\n      },
    {\n        \"database\" : \"pubmed\",\n        \"id\" : \"8404951\",\n        \"description\"
    : \"pubmed\",\n        \"url\" : \"https://pubmed.ncbi.nlm.nih.gov/8404951/\"\n      },
    {\n        \"database\" : \"pubmed\",\n        \"id\" : \"8857117\",\n        \"description\"
    : \"pubmed\",\n        \"url\" : \"https://pubmed.ncbi.nlm.nih.gov/8857117/\"\n      },
    {\n        \"database\" : \"pubmed\",\n        \"id\" : \"9106780\",\n        \"description\"
    : \"pubmed\",\n        \"url\" : \"https://pubmed.ncbi.nlm.nih.gov/9106780/\"\n      },
    {\n        \"database\" : \"reaxys\",\n        \"id\" : \"11403444\",\n        \"description\"
    : \"reaxys\",\n        \"url\" : null\n      } ],\n      \"obo_synonym\" : [ {\n        \"name\"
    : \"Cobalt(II) chloride--water (1/7)\",\n        \"scope\" : \"hasExactSynonym\",\n        \"type\"
    : \"IUPAC NAME\",\n        \"xrefs\" : [ {\n          \"database\" : null,\n          \"id\"
    : \"IUPAC\",\n          \"description\" : null,\n          \"url\" : null\n        }
    ]\n      }, {\n        \"name\" : \"cobalt(2+) dichloride hexahydrate\",\n        \"scope\"
    : \"hasExactSynonym\",\n        \"type\" : \"IUPAC NAME\",\n        \"xrefs\"
    : [ {\n          \"database\" : null,\n          \"id\" : \"IUPAC\",\n          \"description\"
    : null,\n          \"url\" : null\n        } ]\n      }, {\n        \"name\" :
    \"Cobalt chloride hexahydrate\",\n        \"scope\" : \"hasRelatedSynonym\",\n        \"type\"
    : null,\n        \"xrefs\" : [ {\n          \"database\" : null,\n          \"id\"
    : \"chemidplus\",\n          \"description\" : null,\n          \"url\" : null\n        }
    ]\n      }, {\n        \"name\" : \"Cobalt dichloride hexahydrate\",\n        \"scope\"
    : \"hasRelatedSynonym\",\n        \"type\" : null,\n        \"xrefs\" : [ {\n          \"database\"
    : null,\n          \"id\" : \"chemidplus\",\n          \"description\" : null,\n          \"url\"
    : null\n        } ]\n      }, {\n        \"name\" : \"Cobalt(II) chloride hexahydrate\",\n        \"scope\"
    : \"hasRelatedSynonym\",\n        \"type\" : null,\n        \"xrefs\" : [ {\n          \"database\"
    : null,\n          \"id\" : \"chemidplus\",\n          \"description\" : null,\n          \"url\"
    : null\n        } ]\n      }, {\n        \"name\" : \"Cobalt(II) chloride--water
    (1/7)\",\n        \"scope\" : \"hasRelatedSynonym\",\n        \"type\" : \"IUPAC
    NAME\",\n        \"xrefs\" : [ {\n          \"database\" : null,\n          \"id\"
    : \"iupac\",\n          \"description\" : null,\n          \"url\" : null\n        }
    ]\n      }, {\n        \"name\" : \"cobalt (II) chloride hexahydrate\",\n        \"scope\"
    : \"hasRelatedSynonym\",\n        \"type\" : null,\n        \"xrefs\" : [ {\n          \"database\"
    : null,\n          \"id\" : \"chebi\",\n          \"description\" : null,\n          \"url\"
    : null\n        } ]\n      }, {\n        \"name\" : \"cobalt chloride hydrate\",\n        \"scope\"
    : \"hasRelatedSynonym\",\n        \"type\" : null,\n        \"xrefs\" : [ {\n          \"database\"
    : null,\n          \"id\" : \"chebi\",\n          \"description\" : null,\n          \"url\"
    : null\n        } ]\n      }, {\n        \"name\" : \"cobalt(2+) dichloride hexahydrate\",\n        \"scope\"
    : \"hasRelatedSynonym\",\n        \"type\" : \"IUPAC NAME\",\n        \"xrefs\"
    : [ {\n          \"database\" : null,\n          \"id\" : \"iupac\",\n          \"description\"
    : null,\n          \"url\" : null\n        } ]\n      } ],\n      \"is_preferred_root\"
    : false,\n      \"_links\" : {\n        \"self\" : {\n          \"href\" : \"http://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_53503?lang=en\"\n        },\n        \"parents\"
    : {\n          \"href\" : \"http://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_53503/parents\"\n        },\n        \"ancestors\"
    : {\n          \"href\" : \"http://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_53503/ancestors\"\n        },\n        \"hierarchicalParents\"
    : {\n          \"href\" : \"http://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_53503/hierarchicalParents\"\n        },\n        \"hierarchicalAncestors\"
    : {\n          \"href\" : \"http://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_53503/hierarchicalAncestors\"\n        },\n        \"jstree\"
    : {\n          \"href\" : \"http://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_53503/jstree\"\n        },\n        \"graph\"
    : {\n          \"href\" : \"http://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_53503/graph\"\n        },\n        \"has_part\"
    : {\n          \"href\" : \"http://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_53503/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBFO_0000051\"\n        },\n        \"has_role\"
    : {\n          \"href\" : \"http://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_53503/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FRO_0000087\"\n        }\n      }\n    }",
    "quote_representation": "raw JSON object"}]}], "local_field_census_reference":
    "REVIEW_WORK/batch065/record05/grounding-inventory.json", "source_only_gaps_are_explicit":
    true, "note": "Batch amounts, provider normalization, stock composition, working
    dose and preparation controls are separate. No source edits or automatic curation
    performed."}'
- assessment_id: a6
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/COLON_EXTRACT_MEDIUM.yaml: primary 17/19, secondary
    16/19; data/normalized_yaml/bacterial/colon_extract_medium.yaml: primary 17/19,
    secondary 16/19. These are ingredient-instance linkage fractions, not accuracy
    scores. Solution terms are audited separately. Every actually asserted CHEBI term
    is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric
    legacy MediaIngredientMech mentions occur across the complete selected documents,
    with exact locators in the inventory; NNNNNN is a historical placeholder, not
    an ID. Complex commercial/product components are not forced to pure-compound IDs.'
  target_ids:
  - CultureMech:003200
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
  - CultureMech:003200
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
  - CultureMech:003200
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-003200-stock-components-flattened-as-main-rates
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Thirteen stock components have lost their preparation and dosing boundaries
  description: Eight Solution A components, one Solution B component and four Solution
    C components appear as main-medium ingredients at full stock strength. Source
    A/B/C receiving doses are absent; Solution D and hemin receiving additions are
    also missing despite their preparation prose being retained. Five main provider
    g_l rates are separately supported.
  target_ids:
  - CultureMech:003200
  field_paths:
  - ingredients[6].concentration
  - ingredients[7].concentration
  - ingredients[8].concentration
  - ingredients[9].concentration
  - ingredients[10].concentration
  - ingredients[11].concentration
  - ingredients[12].concentration
  - ingredients[13].concentration
  - ingredients[14].concentration
  - ingredients[15].concentration
  - ingredients[16].concentration
  - ingredients[17].concentration
  - ingredients[18].concentration
  - solutions
  - evidence
  evidence_ids:
  - apiJ854
  rule_id: review-ingredient-concentrations/stock-stage-preservation
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/colon_extract_medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-003200-vitamin-k1-liquid-stock-as-mass-rate
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Vitamin K1 liquid stock is represented as a mass concentration
  description: Both selected documents store 0.2 G_PER_L, while the exact source row
    is 0.2 ml of a 0.5% Vitamin K1 preparation. The absent percentage basis prevents
    an evidence-backed conversion to a mass dose or rate.
  target_ids:
  - CultureMech:003200
  field_paths:
  - ingredients[5].concentration
  evidence_ids:
  - apiJ854
  rule_id: review-ingredient-concentrations/stock-volume-versus-mass
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/colon_extract_medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-003200-cheesecloth-misclassified-as-sterilization
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Stock preparation is flattened and cheesecloth filtration is labeled sterilization
  description: Solution D and hemin preparation are retained as consecutive main steps,
    but their boundaries are lost. FILTER_STERILIZE overstates a source instruction
    to filter through cheesecloth. Main and stock water inputs are missing. The current
    importer collects prose from all solution recipes and classifies a filter substring
    as sterilization; this is current behavior, not proof of the historical run.
  target_ids:
  - CultureMech:003200
  field_paths:
  - preparation_steps[1].action
  - preparation_steps[1].description
  - preparation_steps[2].description
  - solutions
  - evidence
  evidence_ids:
  - apiJ854
  rule_id: review-yaml-record/preparation-stage-and-action-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/colon_extract_medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-003200-manganese-unspecified-hydrate-form
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Manganese hydrate specificity remains unresolved
  description: Both layers retain MnSO4 x n H2O but assert CHEBI:86360 manganese(II)
    sulfate, whose current formula is Mn.O4S. This is not an authenticated exact hydrate
    identity. The source does not supply n, so no specific hydrate or molecular weight
    can be safely substituted.
  target_ids:
  - CultureMech:003200
  field_paths:
  - ingredients[10].preferred_term
  - ingredients[10].term
  evidence_ids:
  - apiJ854
  - chebi86360
  - grounding
  rule_id: review-yaml-record/unspecified-hydrate-grounding
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/colon_extract_medium.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Restore explicitly scoped A/B/C stock compositions and all five receiving
    stock additions using exact source batch volumes. Credit retained D/hemin preparation
    text. Preserve the five supported provider main rates with their volume caveat;
    do not calculate a final dilution until a defensible final basis is available.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003200
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/colon_extract_medium.yaml
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
  description: Represent the liquid stock addition and retain the literal percent
    with its unresolved basis. Resolve stock solvent and percent convention only from
    exact source evidence; do not invent w/v, v/v or a density.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003200
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/colon_extract_medium.yaml
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
  description: Retain the complete original preparation text under its exact stock,
    distinguish extraction/cheesecloth filtration/centrifugation/storage from sterilization
    and restore the source solvent statements. Review the importer stage aggregation
    and action classifier, repair maintained input and regenerate without inventing
    processing conditions.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003200
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/colon_extract_medium.yaml
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
  description: Retain the exact unresolved hydrate wording and source mass, document
    the mapping specificity limitation, and resolve the supplied form only with exact
    evidence. Do not invent a secondary link or calculate molarity from the anhydrous
    formula.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:003200
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/colon_extract_medium.yaml
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
- The exact official JCM854 page returns Nothing found despite HTTP200. The complete
  current MediaDive recipe is the usable formulation evidence; no unavailable primary
  wording or organism claim is invented.
- The provider main volume 1584 ml omits the separate 0.2 ml stock addition from nominal
  accounting. Neither sum establishes measured final volume; supported provider rates
  remain explicitly qualified.
- The source leaves Vitamin K1 percent basis and manganese hydrate number unspecified.
  Cobalt derived mmol data conflict with its supplied hydrate; preserve masses and
  forms instead of copying that conversion.
- All preparation controls are scoped to their exact main or stock stage. Current
  writer inspection and matching historical raw bytes do not reconstruct historical
  execution or source access time.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
