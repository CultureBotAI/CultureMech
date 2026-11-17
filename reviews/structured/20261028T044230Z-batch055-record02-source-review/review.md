# Basic mineral medium: restore source stock boundaries and conflicting vitamin doses

- Review: 20261028T044230Z-batch055-record02-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T04:31:44.522101Z
- Finished UTC: 2026-10-28T04:42:30.212534Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current DSM1615 and its provider separate buffer, trace elements and four vitamin stocks. Local direct ingredients mix receiving-medium rates with stock strengths and a sodium-hydroxide solvent volume. Existing preparation is substantial but over-scoped. The primary main-table vitamin dose conflicts with its footer and is retained as unresolved.

## Scope And Provenance

Full selected record and exact maintained contributors; external source limits explicitly retained.

Selection: Actual batch055 native selection index 02.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001096 | data/merge_yaml/merged/Basic_mineral_medium.yaml | generated | basic_mineral_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001096 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:001096 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:001096 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:001096 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Exact DSM1615 identity and unchanged supported claims

identity: supported. Targets: CultureMech:001096.

The selected record and its sole maintained owner are DSM1615. Main pH, all nine existing preparation statements and direct provider rate correspondences are explicitly credited within their source scopes. No external strain or growth claim is added.

### Hydrates, generic names and current legacy status

grounding: concern. Targets: CultureMech:001096.

CuCl2 x 5 H2O is literally printed and CHEBI:91245 matches that pentahydrate. Nickel chloride hexahydrate is broader/mismatched against CHEBI:34887, whose formula lacks waters. Source EDTA and thiamine do not warrant inventing salts; Na-aspartate and B12 remain chemically underspecified. MediaIngredientMech:000898 has no row in the current packaged catalog, without proving historical invalidity. All other asserted primary/secondary labels are current OLS labels.

### Complete quantity and numeric preparation audit

quantity: concern. Targets: CultureMech:001096.

Every local concentration field has an explicit disposition; source-only doses, batch volumes and conditional preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "MgSO4 x 7 H2O", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"attribute\": \"1 M\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.246476,\n                        \"mmol_l\": 1,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "evidence_only", "rationale": "The current provider explicitly declares this g_l value on Main sol.1615, and the primary specifies its stock dose and strength. Retain the provider-supported numerical correspondence while adding the missing stock/addition context; it is not an independently measured additive final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.246476", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current provider explicitly declares this g_l value on Main sol.1615, and the primary specifies its stock dose and strength. Retain the provider-supported numerical correspondence while adding the missing stock/addition context; it is not an independently measured additive final volume."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.246476", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current provider explicitly declares this g_l value on Main sol.1615, and the primary specifies its stock dose and strength. Retain the provider-supported numerical correspondence while adding the missing stock/addition context; it is not an independently measured additive final volume."}]}, {"quantity_id": "q2", "topic": "Sodium acetate", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Sodium acetate\",\n                        \"compound_id\": 731,\n                        \"attribute\": \"1 M\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.8203,\n                        \"mmol_l\": 10,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "evidence_only", "rationale": "The current provider explicitly declares this g_l value on Main sol.1615, and the primary specifies its stock dose and strength. Retain the provider-supported numerical correspondence while adding the missing stock/addition context; it is not an independently measured additive final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.8203", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current provider explicitly declares this g_l value on Main sol.1615, and the primary specifies its stock dose and strength. Retain the provider-supported numerical correspondence while adding the missing stock/addition context; it is not an independently measured additive final volume."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.8203", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current provider explicitly declares this g_l value on Main sol.1615, and the primary specifies its stock dose and strength. Retain the provider-supported numerical correspondence while adding the missing stock/addition context; it is not an independently measured additive final volume."}]}, {"quantity_id": "q3", "topic": "CaCl2 x 2 H2O", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"condition\": \"\",\n                        \"attribute\": \"5%\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.340101,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "evidence_only", "rationale": "The current provider explicitly declares this g_l value on Main sol.1615, and the primary specifies its stock dose and strength. Retain the provider-supported numerical correspondence while adding the missing stock/addition context; it is not an independently measured additive final volume. The primary 5% calcium stock does not state a mass/volume percentage basis; the provider 0.05 g/L is credited as its own assertion, not independently derived from that bare percentage.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current provider explicitly declares this g_l value on Main sol.1615, and the primary specifies its stock dose and strength. Retain the provider-supported numerical correspondence while adding the missing stock/addition context; it is not an independently measured additive final volume. The primary 5% calcium stock does not state a mass/volume percentage basis; the provider 0.05 g/L is credited as its own assertion, not independently derived from that bare percentage."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current provider explicitly declares this g_l value on Main sol.1615, and the primary specifies its stock dose and strength. Retain the provider-supported numerical correspondence while adding the missing stock/addition context; it is not an independently measured additive final volume. The primary 5% calcium stock does not state a mass/volume percentage basis; the provider 0.05 g/L is credited as its own assertion, not independently derived from that bare percentage."}]}, {"quantity_id": "q4", "topic": "Na-aspartate", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na-aspartate\",\n                        \"compound_id\": 228,\n                        \"attribute\": \"2 M\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.35414,\n                        \"mmol_l\": 2,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "evidence_only", "rationale": "The current provider explicitly declares this g_l value on Main sol.1615, and the primary specifies its stock dose and strength. Retain the provider-supported numerical correspondence while adding the missing stock/addition context; it is not an independently measured additive final volume. Sodium aspartate form/stereochemistry is not resolved from this name; no ontology or molecular-weight-based replacement is guessed.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.35414", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current provider explicitly declares this g_l value on Main sol.1615, and the primary specifies its stock dose and strength. Retain the provider-supported numerical correspondence while adding the missing stock/addition context; it is not an independently measured additive final volume. Sodium aspartate form/stereochemistry is not resolved from this name; no ontology or molecular-weight-based replacement is guessed."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.35414", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current provider explicitly declares this g_l value on Main sol.1615, and the primary specifies its stock dose and strength. Retain the provider-supported numerical correspondence while adding the missing stock/addition context; it is not an independently measured additive final volume. Sodium aspartate form/stereochemistry is not resolved from this name; no ontology or molecular-weight-based replacement is guessed."}]}, {"quantity_id": "q5", "topic": "L-Methionine", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"L-Methionine\",\n                        \"compound_id\": 1330,\n                        \"attribute\": \"50 mM, filter sterilized, neutralised\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0074605,\n                        \"mmol_l\": 0.05,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "evidence_only", "rationale": "The current provider explicitly declares this g_l value on Main sol.1615, and the primary specifies its stock dose and strength. Retain the provider-supported numerical correspondence while adding the missing stock/addition context; it is not an independently measured additive final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.0074605", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current provider explicitly declares this g_l value on Main sol.1615, and the primary specifies its stock dose and strength. Retain the provider-supported numerical correspondence while adding the missing stock/addition context; it is not an independently measured additive final volume."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.0074605", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current provider explicitly declares this g_l value on Main sol.1615, and the primary specifies its stock dose and strength. Retain the provider-supported numerical correspondence while adding the missing stock/addition context; it is not an independently measured additive final volume."}]}, {"quantity_id": "q6", "topic": "EDTA", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"EDTA\",\n                        \"compound_id\": 271,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 17.1092,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume."}]}, {"quantity_id": "q7", "topic": "FeSO4 x 7 H2O", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 7.19386,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume."}]}, {"quantity_id": "q8", "topic": "ZnSO4", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnSO4\",\n                        \"compound_id\": 441,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.619579,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume."}]}, {"quantity_id": "q9", "topic": "MnCl2", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[1].recipe[3]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2\",\n                        \"compound_id\": 980,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.238398,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume."}]}, {"quantity_id": "q10", "topic": "H3BO3", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[1].recipe[4]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume."}]}, {"quantity_id": "q11", "topic": "CoCl2 x 6 H2O", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[1].recipe[5]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume."}]}, {"quantity_id": "q12", "topic": "CuCl2 x 5 H2O", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 5 H2O\",\n                        \"compound_id\": 838,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0445379,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume. CuCl2 x 5 H2O is literal in the primary; its pentahydrate identity must not be silently changed to a more familiar hydrate.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume. CuCl2 x 5 H2O is literal in the primary; its pentahydrate identity must not be silently changed to a more familiar hydrate."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume. CuCl2 x 5 H2O is literal in the primary; its pentahydrate identity must not be silently changed to a more familiar hydrate."}]}, {"quantity_id": "q13", "topic": "NiCl2 x 6 H2O", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[1].recipe[7]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume. The source names nickel chloride hexahydrate, whereas the local CHEBI object denotes nickel dichloride without those waters.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume. The source names nickel chloride hexahydrate, whereas the local CHEBI object denotes nickel dichloride without those waters."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume. The source names nickel chloride hexahydrate, whereas the local CHEBI object denotes nickel dichloride without those waters."}]}, {"quantity_id": "q14", "topic": "Na2MoO4 x 2 H2O", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[1].recipe[8]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0826617,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared trace-stock g/L value, matching the primary batch mass and its listed 1000 mL water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather than flattening or silently asserting a measured final volume."}]}, {"quantity_id": "q15", "topic": "K2HPO4", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"attribute\": \"0.1 M\",\n                        \"amount\": 130,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.26429,\n                        \"mmol_l\": 13,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "The current rate is explicitly declared on the 1000 mL K-P buffer object. The primary gives the corresponding 0.1 M stock volume, plus 800 mL water, before post-sterilization additions. Preserve this buffer-basis rate and make its stage explicit; do not silently treat pre-addition buffer volume as measured final-medium volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "2.26429", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current rate is explicitly declared on the 1000 mL K-P buffer object. The primary gives the corresponding 0.1 M stock volume, plus 800 mL water, before post-sterilization additions. Preserve this buffer-basis rate and make its stage explicit; do not silently treat pre-addition buffer volume as measured final-medium volume."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "2.26429", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current rate is explicitly declared on the 1000 mL K-P buffer object. The primary gives the corresponding 0.1 M stock volume, plus 800 mL water, before post-sterilization additions. Preserve this buffer-basis rate and make its stage explicit; do not silently treat pre-addition buffer volume as measured final-medium volume."}]}, {"quantity_id": "q16", "topic": "KH2PO4", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[2].recipe[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"attribute\": \"0.1 M\",\n                        \"amount\": 70,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.952595,\n                        \"mmol_l\": 7,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "The current rate is explicitly declared on the 1000 mL K-P buffer object. The primary gives the corresponding 0.1 M stock volume, plus 800 mL water, before post-sterilization additions. Preserve this buffer-basis rate and make its stage explicit; do not silently treat pre-addition buffer volume as measured final-medium volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.952595", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current rate is explicitly declared on the 1000 mL K-P buffer object. The primary gives the corresponding 0.1 M stock volume, plus 800 mL water, before post-sterilization additions. Preserve this buffer-basis rate and make its stage explicit; do not silently treat pre-addition buffer volume as measured final-medium volume."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.952595", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current rate is explicitly declared on the 1000 mL K-P buffer object. The primary gives the corresponding 0.1 M stock volume, plus 800 mL water, before post-sterilization additions. Preserve this buffer-basis rate and make its stage explicit; do not silently treat pre-addition buffer volume as measured final-medium volume."}]}, {"quantity_id": "q17", "topic": "Thiamine", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[4].recipe[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Thiamine\",\n                        \"compound_id\": 666,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.188423,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration."}]}, {"quantity_id": "q18", "topic": "Calcium pantothenate", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[4].recipe[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.104925,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration."}]}, {"quantity_id": "q19", "topic": "Biotin", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[5].recipe[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration."}]}, {"quantity_id": "q20", "topic": "PABA", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[5].recipe[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"PABA\",\n                        \"compound_id\": 1309,\n                        \"attribute\": \"p-aminobenzoic acid\",\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration."}]}, {"quantity_id": "q21", "topic": "Nicotinic acid", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[5].recipe[2]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration."}]}, {"quantity_id": "q22", "topic": "Pyridoxine", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[5].recipe[3]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Pyridoxine\",\n                        \"compound_id\": 637,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.591086,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration."}]}, {"quantity_id": "q23", "topic": "NaOH", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[5].recipe[4]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"attribute\": \"0.1N\",\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "The source specifies 100 mL of 0.1 N NaOH as the solvent of the basic vitamin stock. Local 100 G_PER_L changes liquid volume into an unsupported mass rate. Preserve normality, volume and stock scope; do not retain or reinterpret 100 g/L as a supported concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "100", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source specifies 100 mL of 0.1 N NaOH as the solvent of the basic vitamin stock. Local 100 G_PER_L changes liquid volume into an unsupported mass rate. Preserve normality, volume and stock scope; do not retain or reinterpret 100 g/L as a supported concentration."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "100", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source specifies 100 mL of 0.1 N NaOH as the solvent of the basic vitamin stock. Local 100 G_PER_L changes liquid volume into an unsupported mass rate. Preserve normality, volume and stock scope; do not retain or reinterpret 100 g/L as a supported concentration."}]}, {"quantity_id": "q24", "topic": "Folic acid", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[6].recipe[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration."}]}, {"quantity_id": "q25", "topic": "Riboflavin", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[6].recipe[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration."}]}, {"quantity_id": "q26", "topic": "B12", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[7].recipe[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"B12\",\n                        \"compound_id\": 1238,\n                        \"amount\": 0.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.00368895,\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration. Generic B12 does not identify a particular cobalamin species; no chemical identity or molar conversion is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration. Generic B12 does not identify a particular cobalamin species; no chemical identity or molar conversion is inferred."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input and the provider explicitly declares this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium concentration. Generic B12 does not identify a particular cobalamin species; no chemical identity or molar conversion is inferred."}]}, {"quantity_id": "q27", "topic": "Existing preparation step 1", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"step\": \"pH 7.0-7.2\"\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "evidence_only", "rationale": "The existing pH 7.0–7.2 is the buffer/main medium scope, not the acidic trace-stock pH.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "preparation_steps[0].description", "stored_value": "pH 7.0-7.2", "decision": "evidence_only", "rationale": "The existing pH 7.0–7.2 is the buffer/main medium scope, not the acidic trace-stock pH."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "preparation_steps[0].description", "stored_value": "pH 7.0-7.2", "decision": "evidence_only", "rationale": "The existing pH 7.0–7.2 is the buffer/main medium scope, not the acidic trace-stock pH."}]}, {"quantity_id": "q28", "topic": "Existing preparation step 2", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[0].steps[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 2,\n                        \"step\": \"After sterilization add from sterile stock solutions:\"\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "evidence_only", "rationale": "Preserve the existing instruction to add sterile stocks after sterilization; attach the corresponding stock objects and doses.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "preparation_steps[1].description", "stored_value": "After sterilization add from sterile stock solutions:", "decision": "evidence_only", "rationale": "Preserve the existing instruction to add sterile stocks after sterilization; attach the corresponding stock objects and doses."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "preparation_steps[1].description", "stored_value": "After sterilization add from sterile stock solutions:", "decision": "evidence_only", "rationale": "Preserve the existing instruction to add sterile stocks after sterilization; attach the corresponding stock objects and doses."}]}, {"quantity_id": "q29", "topic": "Existing preparation step 3", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[0].steps[2]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 5,\n                        \"step\": \"might result in colloid formation, especially when added into\\r\\nhot medium, but dissolves after vigorous shaking\"\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "evidence_only", "rationale": "Preserve the existing calcium-stock colloid warning and its hot-medium/shaking context; it is not a new quantity.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "preparation_steps[2].description", "stored_value": "might result in colloid formation, especially when added into\r\nhot medium, but dissolves after vigorous shaking", "decision": "evidence_only", "rationale": "Preserve the existing calcium-stock colloid warning and its hot-medium/shaking context; it is not a new quantity."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "preparation_steps[2].description", "stored_value": "might result in colloid formation, especially when added into\r\nhot medium, but dissolves after vigorous shaking", "decision": "evidence_only", "rationale": "Preserve the existing calcium-stock colloid warning and its hot-medium/shaking context; it is not a new quantity."}]}, {"quantity_id": "q30", "topic": "Existing preparation step 4", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"step\": \"Adjust pH to 3.0-4.0 with HCl.\"\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "The existing pH 3.0–4.0 instruction belongs only to the trace stock. It must not override main pH 7.0–7.2.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "preparation_steps[3].description", "stored_value": "Adjust pH to 3.0-4.0 with HCl.", "decision": "correct", "rationale": "The existing pH 3.0–4.0 instruction belongs only to the trace stock. It must not override main pH 7.0–7.2."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "preparation_steps[3].description", "stored_value": "Adjust pH to 3.0-4.0 with HCl.", "decision": "correct", "rationale": "The existing pH 3.0–4.0 instruction belongs only to the trace stock. It must not override main pH 7.0–7.2."}]}, {"quantity_id": "q31", "topic": "Existing preparation step 5", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[1].steps[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"step\": \"Autoclave at 121 \\u00b0C for 15 min.\"\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "The existing 121 °C/15 min cycle is explicitly present in the current provider trace-stock steps. The primary PDF does not specify this trace cycle; preserve provider attribution and do not transfer it to the main buffer.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "preparation_steps[4].description", "stored_value": "Autoclave at 121 °C for 15 min.", "decision": "correct", "rationale": "The existing 121 °C/15 min cycle is explicitly present in the current provider trace-stock steps. The primary PDF does not specify this trace cycle; preserve provider attribution and do not transfer it to the main buffer."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "preparation_steps[4].description", "stored_value": "Autoclave at 121 °C for 15 min.", "decision": "correct", "rationale": "The existing 121 °C/15 min cycle is explicitly present in the current provider trace-stock steps. The primary PDF does not specify this trace cycle; preserve provider attribution and do not transfer it to the main buffer."}]}, {"quantity_id": "q32", "topic": "Existing preparation step 6", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[1].steps[2]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"step\": \"Note: autoclave in closed bottles\"\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "Closed-bottle autoclaving is a current provider trace-stock instruction, not a universal medium condition.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "preparation_steps[5].description", "stored_value": "Note: autoclave in closed bottles", "decision": "correct", "rationale": "Closed-bottle autoclaving is a current provider trace-stock instruction, not a universal medium condition."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "preparation_steps[5].description", "stored_value": "Note: autoclave in closed bottles", "decision": "correct", "rationale": "Closed-bottle autoclaving is a current provider trace-stock instruction, not a universal medium condition."}]}, {"quantity_id": "q33", "topic": "Existing preparation step 7", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[2].steps[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"step\": \"Sterilize at 121\\u00b0C for 20 minutes in 1L Schott bottle\"\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "The existing 121 °C/20 min and 1 L Schott bottle instruction belongs to the K-P buffer. Both primary and provider support it.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "preparation_steps[6].description", "stored_value": "Sterilize at 121°C for 20 minutes in 1L Schott bottle", "decision": "correct", "rationale": "The existing 121 °C/20 min and 1 L Schott bottle instruction belongs to the K-P buffer. Both primary and provider support it."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "preparation_steps[6].description", "stored_value": "Sterilize at 121°C for 20 minutes in 1L Schott bottle", "decision": "correct", "rationale": "The existing 121 °C/20 min and 1 L Schott bottle instruction belongs to the K-P buffer. Both primary and provider support it."}]}, {"quantity_id": "q34", "topic": "Existing preparation step 8", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[3].steps[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"step\": \"Sterilize by filtration.\"\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "Existing filtration belongs to the vitamin solutions. Do not extend it to every ingredient or invent a pore size.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "preparation_steps[7].description", "stored_value": "Sterilize by filtration.", "decision": "correct", "rationale": "Existing filtration belongs to the vitamin solutions. Do not extend it to every ingredient or invent a pore size."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "preparation_steps[7].description", "stored_value": "Sterilize by filtration.", "decision": "correct", "rationale": "Existing filtration belongs to the vitamin solutions. Do not extend it to every ingredient or invent a pore size."}, {"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "preparation_steps[7].action", "stored_value": "MIX", "decision": "correct", "rationale": "The literal instruction is filtration, but the existing action is MIX. Use a filtration action within the vitamin-stock scope while retaining the source text."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "preparation_steps[7].action", "stored_value": "MIX", "decision": "correct", "rationale": "The literal instruction is filtration, but the existing action is MIX. Use a filtration action within the vitamin-stock scope while retaining the source text."}]}, {"quantity_id": "q35", "topic": "Existing preparation step 9", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[3].steps[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"step\": \"Mix the four solutions in the ratio 1:1:1:1.\"\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "correct", "rationale": "Existing 1:1:1:1 mixing is supported for the four vitamin stocks; the receiving dose still conflicts between the primary main list and footer.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "preparation_steps[8].description", "stored_value": "Mix the four solutions in the ratio 1:1:1:1.", "decision": "correct", "rationale": "Existing 1:1:1:1 mixing is supported for the four vitamin stocks; the receiving dose still conflicts between the primary main list and footer."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "preparation_steps[8].description", "stored_value": "Mix the four solutions in the ratio 1:1:1:1.", "decision": "correct", "rationale": "Existing 1:1:1:1 mixing is supported for the four vitamin stocks; the receiving dose still conflicts between the primary main list and footer."}]}, {"quantity_id": "q36", "topic": "Existing main pH range", "source": {"evidence_id": "dsm1615", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1615.pdf", "raw_path": "REVIEW_WORK/batch055/source01-03/dsm1615.bin", "raw_sha256": "67c48c0397fbb5add36f04d2995f30ca93ba57daac554c5603cca65fddb1ce05", "locator": "Page1 K-P buffer", "accessed_at": "2026-10-28T04:32:46.058756+00:00", "quote": "pH 7.0-7.2"}, "decision": "evidence_only", "rationale": "The acidic stock pH values must not replace this main pH range.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ph_range", "stored_value": {"min": 7.0, "max": 7.2}, "decision": "evidence_only", "rationale": "Retain the explicitly supported main/buffer pH range, distinct from trace and acidic-vitamin pH."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ph_range", "stored_value": {"min": 7.0, "max": 7.2}, "decision": "evidence_only", "rationale": "Retain the explicitly supported main/buffer pH range, distinct from trace and acidic-vitamin pH."}]}, {"quantity_id": "q37", "topic": "Source-only Main sol. 1615: 20 mM K-P-Buffer", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"20 mM K-P-Buffer\",\n                        \"solution_id\": 5756,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "add", "rationale": "Add this explicit stock-addition edge to the missing solution topology. Preserve its exact source solution identity, dose and provider main-volume basis. The vitamin 0.5 mL dose is one side of the primary conflict, not a resolved universal dose.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Add this explicit stock-addition edge to the missing solution topology. Preserve its exact source solution identity, dose and provider main-volume basis. The vitamin 0.5 mL dose is one side of the primary conflict, not a resolved universal dose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Add this explicit stock-addition edge to the missing solution topology. Preserve its exact source solution identity, dose and provider main-volume basis. The vitamin 0.5 mL dose is one side of the primary conflict, not a resolved universal dose.", "missing": true}]}, {"quantity_id": "q38", "topic": "Source-only Main sol. 1615: Trace element solution", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 3027,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "add", "rationale": "Add this explicit stock-addition edge to the missing solution topology. Preserve its exact source solution identity, dose and provider main-volume basis. The vitamin 0.5 mL dose is one side of the primary conflict, not a resolved universal dose.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Add this explicit stock-addition edge to the missing solution topology. Preserve its exact source solution identity, dose and provider main-volume basis. The vitamin 0.5 mL dose is one side of the primary conflict, not a resolved universal dose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Add this explicit stock-addition edge to the missing solution topology. Preserve its exact source solution identity, dose and provider main-volume basis. The vitamin 0.5 mL dose is one side of the primary conflict, not a resolved universal dose.", "missing": true}]}, {"quantity_id": "q39", "topic": "Source-only Main sol. 1615: Vitamine mixture", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Vitamine mixture\",\n                        \"solution_id\": 5757,\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "add", "rationale": "Add this explicit stock-addition edge to the missing solution topology. Preserve its exact source solution identity, dose and provider main-volume basis. The vitamin 0.5 mL dose is one side of the primary conflict, not a resolved universal dose.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Add this explicit stock-addition edge to the missing solution topology. Preserve its exact source solution identity, dose and provider main-volume basis. The vitamin 0.5 mL dose is one side of the primary conflict, not a resolved universal dose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Add this explicit stock-addition edge to the missing solution topology. Preserve its exact source solution identity, dose and provider main-volume basis. The vitamin 0.5 mL dose is one side of the primary conflict, not a resolved universal dose.", "missing": true}]}, {"quantity_id": "q40", "topic": "Source-only Trace element solution: Distilled water", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[1].recipe[9]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "add", "rationale": "Retain 1000 mL distilled water as the listed trace-stock solvent. The provider separately declares a 1000 mL stock volume; do not describe the primary solvent listing as an explicit final-makeup instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain 1000 mL distilled water as the listed trace-stock solvent. The provider separately declares a 1000 mL stock volume; do not describe the primary solvent listing as an explicit final-makeup instruction.", "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain 1000 mL distilled water as the listed trace-stock solvent. The provider separately declares a 1000 mL stock volume; do not describe the primary solvent listing as an explicit final-makeup instruction.", "missing": true}]}, {"quantity_id": "q41", "topic": "Source-only 20 mM K-P-Buffer: Distilled water", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[2].recipe[2]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 800,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "add", "rationale": "Retain 800 mL distilled water in the buffer alongside the two 0.1 M phosphate stock volumes. This is separate from subsequent medium additions.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain 800 mL distilled water in the buffer alongside the two 0.1 M phosphate stock volumes. This is separate from subsequent medium additions.", "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain 800 mL distilled water in the buffer alongside the two 0.1 M phosphate stock volumes. This is separate from subsequent medium additions.", "missing": true}]}, {"quantity_id": "q42", "topic": "Source-only Vitamine mixture: Acidic thiamine / Ca pantothenate solution", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[3].recipe[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Acidic thiamine / Ca pantothenate solution\",\n                        \"solution_id\": 5758,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "add", "rationale": "Retain the provider 100 mL contribution of this named vitamin stock to its declared 400 mL mixture; the primary independently specifies the equal-volume 1:1:1:1 ratio.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain the provider 100 mL contribution of this named vitamin stock to its declared 400 mL mixture; the primary independently specifies the equal-volume 1:1:1:1 ratio.", "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain the provider 100 mL contribution of this named vitamin stock to its declared 400 mL mixture; the primary independently specifies the equal-volume 1:1:1:1 ratio.", "missing": true}]}, {"quantity_id": "q43", "topic": "Source-only Vitamine mixture: Basic vitamin solution", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[3].recipe[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Basic vitamin solution\",\n                        \"solution_id\": 5759,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "add", "rationale": "Retain the provider 100 mL contribution of this named vitamin stock to its declared 400 mL mixture; the primary independently specifies the equal-volume 1:1:1:1 ratio.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain the provider 100 mL contribution of this named vitamin stock to its declared 400 mL mixture; the primary independently specifies the equal-volume 1:1:1:1 ratio.", "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain the provider 100 mL contribution of this named vitamin stock to its declared 400 mL mixture; the primary independently specifies the equal-volume 1:1:1:1 ratio.", "missing": true}]}, {"quantity_id": "q44", "topic": "Source-only Vitamine mixture: Neutral folic acid / riboflavin solution", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[3].recipe[2]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Neutral folic acid / riboflavin solution\",\n                        \"solution_id\": 5760,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "add", "rationale": "Retain the provider 100 mL contribution of this named vitamin stock to its declared 400 mL mixture; the primary independently specifies the equal-volume 1:1:1:1 ratio.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain the provider 100 mL contribution of this named vitamin stock to its declared 400 mL mixture; the primary independently specifies the equal-volume 1:1:1:1 ratio.", "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain the provider 100 mL contribution of this named vitamin stock to its declared 400 mL mixture; the primary independently specifies the equal-volume 1:1:1:1 ratio.", "missing": true}]}, {"quantity_id": "q45", "topic": "Source-only Vitamine mixture: Neutral B12 solution 0.005 g/L", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[3].recipe[3]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\": \"Neutral B12 solution 0.005 g/L\",\n                        \"solution_id\": 5761,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "add", "rationale": "Retain the provider 100 mL contribution of this named vitamin stock to its declared 400 mL mixture; the primary independently specifies the equal-volume 1:1:1:1 ratio.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain the provider 100 mL contribution of this named vitamin stock to its declared 400 mL mixture; the primary independently specifies the equal-volume 1:1:1:1 ratio.", "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain the provider 100 mL contribution of this named vitamin stock to its declared 400 mL mixture; the primary independently specifies the equal-volume 1:1:1:1 ratio.", "missing": true}]}, {"quantity_id": "q46", "topic": "Source-only Acidic thiamine / Ca pantothenate solution: Distilled water", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[4].recipe[2]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"attribute\": \"acidified to pH 3.0 with HCl\",\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "add", "rationale": "Retain 100 mL water acidified to pH 3 with HCl for this vitamin stock. HCl concentration and amount are not given; do not invent them or treat this as main-medium pH.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain 100 mL water acidified to pH 3 with HCl for this vitamin stock. HCl concentration and amount are not given; do not invent them or treat this as main-medium pH.", "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain 100 mL water acidified to pH 3 with HCl for this vitamin stock. HCl concentration and amount are not given; do not invent them or treat this as main-medium pH.", "missing": true}]}, {"quantity_id": "q47", "topic": "Source-only Neutral folic acid / riboflavin solution: Distilled water", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[6].recipe[2]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "add", "rationale": "Retain this 100 mL water input in its specific vitamin stock. The provider stock volume is explicit, whereas the primary describes solvent input; no receiving-medium amount is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain this 100 mL water input in its specific vitamin stock. The provider stock volume is explicit, whereas the primary describes solvent input; no receiving-medium amount is inferred.", "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain this 100 mL water input in its specific vitamin stock. The provider stock volume is explicit, whereas the primary describes solvent input; no receiving-medium amount is inferred.", "missing": true}]}, {"quantity_id": "q48", "topic": "Source-only Neutral B12 solution 0.005 g/L: Distilled water", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[7].recipe[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "Literal raw JSON substring, independently decoded to the located object"}, "decision": "add", "rationale": "Retain this 100 mL water input in its specific vitamin stock. The provider stock volume is explicit, whereas the primary describes solvent input; no receiving-medium amount is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain this 100 mL water input in its specific vitamin stock. The provider stock volume is explicit, whereas the primary describes solvent input; no receiving-medium amount is inferred.", "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain this 100 mL water input in its specific vitamin stock. The provider stock volume is explicit, whereas the primary describes solvent input; no receiving-medium amount is inferred.", "missing": true}]}, {"quantity_id": "q49", "topic": "Provider solution basis: Main sol. 1615", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[0].volume", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "\"volume\": 1000"}, "decision": "evidence_only", "rationale": "Preserve the provider-declared volume at this exact solution object. It is not a license to sum or transfer rates between buffer, trace stock, individual vitamin stocks, mixture and finished medium.", "layer_assessments": []}, {"quantity_id": "q50", "topic": "Provider solution basis: Trace element solution", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[1].volume", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "\"volume\": 1000"}, "decision": "evidence_only", "rationale": "Preserve the provider-declared volume at this exact solution object. It is not a license to sum or transfer rates between buffer, trace stock, individual vitamin stocks, mixture and finished medium.", "layer_assessments": []}, {"quantity_id": "q51", "topic": "Provider solution basis: 20 mM K-P-Buffer", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[2].volume", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "\"volume\": 1000"}, "decision": "evidence_only", "rationale": "Preserve the provider-declared volume at this exact solution object. It is not a license to sum or transfer rates between buffer, trace stock, individual vitamin stocks, mixture and finished medium.", "layer_assessments": []}, {"quantity_id": "q52", "topic": "Provider solution basis: Vitamine mixture", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[3].volume", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "\"volume\": 400"}, "decision": "evidence_only", "rationale": "Preserve the provider-declared volume at this exact solution object. It is not a license to sum or transfer rates between buffer, trace stock, individual vitamin stocks, mixture and finished medium.", "layer_assessments": []}, {"quantity_id": "q53", "topic": "Provider solution basis: Acidic thiamine / Ca pantothenate solution", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[4].volume", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "\"volume\": 100"}, "decision": "evidence_only", "rationale": "Preserve the provider-declared volume at this exact solution object. It is not a license to sum or transfer rates between buffer, trace stock, individual vitamin stocks, mixture and finished medium.", "layer_assessments": []}, {"quantity_id": "q54", "topic": "Provider solution basis: Basic vitamin solution", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[5].volume", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "\"volume\": 100"}, "decision": "evidence_only", "rationale": "Preserve the provider-declared volume at this exact solution object. It is not a license to sum or transfer rates between buffer, trace stock, individual vitamin stocks, mixture and finished medium.", "layer_assessments": []}, {"quantity_id": "q55", "topic": "Provider solution basis: Neutral folic acid / riboflavin solution", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[6].volume", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "\"volume\": 100"}, "decision": "evidence_only", "rationale": "Preserve the provider-declared volume at this exact solution object. It is not a license to sum or transfer rates between buffer, trace stock, individual vitamin stocks, mixture and finished medium.", "layer_assessments": []}, {"quantity_id": "q56", "topic": "Provider solution basis: Neutral B12 solution 0.005 g/L", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29", "locator": "$.data.solutions[7].volume", "accessed_at": "2026-10-28T04:32:45.964892+00:00", "quote": "\"volume\": 100"}, "decision": "evidence_only", "rationale": "Preserve the provider-declared volume at this exact solution object. It is not a license to sum or transfer rates between buffer, trace stock, individual vitamin stocks, mixture and finished medium.", "layer_assessments": []}, {"quantity_id": "q57", "topic": "Conflicting vitamin mixture addition doses", "source": [{"evidence_id": "dsm1615", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1615.pdf", "raw_path": "REVIEW_WORK/batch055/source01-03/dsm1615.bin", "raw_sha256": "67c48c0397fbb5add36f04d2995f30ca93ba57daac554c5603cca65fddb1ce05", "locator": "Page1 post-sterilization additions", "accessed_at": "2026-10-28T04:32:46.058756+00:00", "quote": "0.5 ml/l Vitamins"}, {"evidence_id": "dsm1615", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1615.pdf", "raw_path": "REVIEW_WORK/batch055/source01-03/dsm1615.bin", "raw_sha256": "67c48c0397fbb5add36f04d2995f30ca93ba57daac554c5603cca65fddb1ce05", "locator": "Page2 final vitamin instruction", "accessed_at": "2026-10-28T04:32:46.058756+00:00", "quote": "Mix the four solutions in the ratio1:1:1:1 and 1.0 ml/L or separately add 250 µl/L. of\neach solution."}], "decision": "unsupported", "rationale": "The primary main recipe gives 0.5 mL/L, but the footer gives 1 mL/L mixed stock or 250 µL/L of each. The current provider follows 0.5 mL in its main object. Do not select a convenient version or silently average the doses.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Represent both source-located dose statements as an unresolved conflict, not interchangeable resolved values.", "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Represent both source-located dose statements as an unresolved conflict, not interchangeable resolved values.", "missing": true}]}, {"quantity_id": "q58", "topic": "Main stock strengths and methionine processing", "source": {"evidence_id": "dsm1615", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1615.pdf", "raw_path": "REVIEW_WORK/batch055/source01-03/dsm1615.bin", "raw_sha256": "67c48c0397fbb5add36f04d2995f30ca93ba57daac554c5603cca65fddb1ce05", "locator": "Page1 complete post-sterilization list", "accessed_at": "2026-10-28T04:32:46.058756+00:00", "quote": "1.0 ml/l 50 mM L-methionine, filter sterilized, neutralised (50 µM)."}, "decision": "add", "rationale": "All primary stock strengths and parenthetical receiving-molarity statements are recorded distinctly from source solution volumes and provider g_l. Neutralisation details and bare percentage basis remain unknown.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Preserve 1 M magnesium and acetate, 5% calcium of unspecified basis, 2 M sodium aspartate and 50 mM methionine stocks with their stated addition volumes. Methionine is filter sterilized and neutralised; no pore size or neutralizer amount is stated.", "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Preserve 1 M magnesium and acetate, 5% calcium of unspecified basis, 2 M sodium aspartate and 50 mM methionine stocks with their stated addition volumes. Methionine is filter sterilized and neutralised; no pore size or neutralizer amount is stated.", "missing": true}]}]

### Current ontology and MIM correspondence

grounding: supported. Targets: CultureMech:001096.

The grounding inventory enumerates every asserted identifier and exact preferred label. Exact identifier rows and ontology-linked rows are recorded separately, including mapping_status. Present catalog membership does not validate supplied hydrate form or historical identity; specific limits are assessed separately.

### History and evidence scope

provenance: supported. Targets: CultureMech:001096.

Complete owner and target histories were read. Current source bytes and inspected code are independent evidence; historical timestamps remain historical claims unless an exact cited raw digest is recovered.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:001096.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:001096.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Trace and vitamin stocks are flattened into direct ingredients

major / open / confirmed; issue key: culturemech-001096-trace-and-vitamin-stocks-are-flattened-into-direct-ingredients.

The local ingredients include nine trace-stock g/L values and individual vitamin-stock strengths as if they were direct medium concentrations. Source buffer, trace stock, four vitamin stocks and mixed vitamin assembly are absent as solution topology. Current importer stock-separation safeguards already exist.

### f2: Basic-vitamin solvent volume is stored as a mass rate

major / open / confirmed; issue key: culturemech-001096-basic-vitamin-solvent-volume-is-stored-as-a-mass-rate.

ingredients[22] is 100 G_PER_L NaOH, while both exact sources specify 100 mL of 0.1 N NaOH as the basic vitamin stock solvent. The local number preserves a volume magnitude with an unsupported mass dimension.

### f3: Primary vitamin addition doses conflict

major / open / confirmed; issue key: culturemech-001096-primary-vitamin-addition-doses-conflict.

The primary main list says 0.5 mL/L vitamins; its footer says 1 mL/L mixed solution or 250 µL/L of each stock. Current API follows the first value. Stock restoration must retain this source-internal conflict instead of choosing or averaging one dose.

### f4: Existing preparation loses stock-specific conditions

major / open / confirmed; issue key: culturemech-001096-existing-preparation-loses-stock-specific-conditions.

Trace pH 3–4, provider trace autoclaving at 121 °C for 15 min, buffer autoclaving at 121 °C for 20 min in a 1 L bottle, and vitamin filtration/mixing appear in one unscoped top-level sequence. The existing prose is supported in those distinct objects and should be preserved with correct ownership. The vitamin filtration description is additionally classified as MIX and needs a filtration action.

### f5: Nickel chloride hexahydrate is grounded without its waters

major / open / confirmed; issue key: culturemech-001096-nickel-chloride-hexahydrate-is-grounded-without-its-waters.

The source and preferred name specify NiCl2 x 6 H2O, but primary and secondary CHEBI:34887 identify nickel dichloride with formula Cl2Ni. Current MIM ontology-linked hydrate rows do not validate an exact six-water form.

### f6: Legacy thiamine linkage has no current catalog row

minor / open / confirmed; issue key: culturemech-001096-legacy-thiamine-linkage-has-no-current-catalog-row.

MediaIngredientMech:000898 is absent from the complete current packaged label index. CHEBI:18385 remains a verified thiamine(1+) object, but current catalog absence does not establish historical invalidity or specify a thiamine salt.

## Recommended Actions And Acceptance Checks

### action1

Curate the maintained owner with explicit stock composition, solvent, preparation and addition edges. Preserve main-provider rate correspondence and buffer-stage rates with their basis; regenerate only after the stock/medium boundary is explicit.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Replace the unsupported mass-rate representation with the explicitly sourced liquid solvent volume and normality in its vitamin stock. Do not invent a final-medium NaOH dose.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Attach both precise primary locations and the provider version, then resolve or explicitly qualify the dose conflict before calculating any final vitamin rates.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action4

Move or qualify each existing instruction under its exact stock/buffer object. Keep main pH 7.0–7.2 and post-sterilization additions distinct; attribute trace 15-min autoclaving to the current provider only.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action5

Reconcile the exact supplied hexahydrate with an independently verified suitable ontology representation. Preserve the source hydrate and stock mass; do not convert using the anhydrous formula or guess an identifier.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action6

Record the legacy/current linkage distinction and reconcile it through the current catalog without inventing a historical conclusion or source salt.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/Basic_mineral_medium.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/basic_mineral_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| dsm1615 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1615.pdf; Entire pages 1–2; main assembly, trace stock and four vitamin stocks | supports | Complete two-page primary PDF, including literal copper chloride pentahydrate, trace-only pH and the conflicting vitamin doses. Both PDF pages were visually inspected. |
| api1615 | https://mediadive.dsmz.de/rest/medium/1615; $.data.medium and all $.data.solutions | supports | Current exact medium1615 API declares eight solution objects and source-specific g_l/mmol_l fields. Numerical correspondence is credited only at its own stock or main-solution stage. |
| provider-stage-census | REVIEW_WORK/batch055/record02/provider-stage-census.json | context_only | Lossless eight-solution recipe/step inventory including every source amount, unit, attribute, volume, g_l and mmol_l. |
| pdf-visual-1 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1615.pdf; PDF page 1; render REVIEW_WORK/batch055/record02/dsm1615-page-1.png | supports | Visual primary-page inspection confirms printed amounts, stock headings and source dose conflict. |
| pdf-visual-2 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1615.pdf; PDF page 2; render REVIEW_WORK/batch055/record02/dsm1615-page-2.png | supports | Visual primary-page inspection confirms printed amounts, stock headings and source dose conflict. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition/_parse_api_solutions/_is_api_stock_addition | context_only | Current _parse_api_composition uses the first solution and skips stock/solvent edges; _parse_api_solutions retains referenced stocks separately. These present safeguards are credited, not blamed for historical flattening. |
| writer-cleanup | scripts/cleanup_recipe_ingredients.py; merge_ingredient_group | context_only | Current merge_ingredient_group keeps the first concentration and flags differing values; it does not sum stock concentrations. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current sole-owner merge copies maintained content and adds generated metadata; it does not repair stock structure or authenticate source arithmetic. |
| historical-1 | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/basic_mineral_medium.yaml.md; Entire report; exact Record header and all claim rows | context_only | Full exact selected-path historical report read. Its past source-access statements and snippets are derivative evidence; the cited raw response is not automatically authenticated. |
| historical-2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Basic_mineral_medium.md; Entire report; exact Record header and all claim rows | context_only | Full exact selected-path historical report read. Its past source-access statements and snippets are derivative evidence; the cited raw response is not automatically authenticated. |
| historical-3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/basic_mineral_medium.md; Entire report; exact Record header and all claim rows | context_only | Full exact selected-path historical report read. Its past source-access statements and snippets are derivative evidence; the cited raw response is not automatically authenticated. |
| historical-4 | reports/yaml_record_review/20260921T185556Z-Basic_mineral_medium.md; Entire report; exact Record header and all claim rows | context_only | Full exact selected-path historical report read. Its past source-access statements and snippets are derivative evidence; the cited raw response is not automatically authenticated. |
| historical-reader | REVIEW_WORK/batch055/record02/historical-reader.json | context_only | Complete selected target/owner historical reports and exact report hashes, preserving derivative-only limits. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32954; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi16643 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16643; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi4735 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_4735; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi35176 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_35176; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi63041 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63041; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi91245 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91245; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63036; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi18385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_18385; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31345; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15956; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30753; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15940; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi16709 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16709; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32145; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_27470; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17015; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch055/record02/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch055/record02/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch055/record02/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch055/record02/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch055/record02/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch055/record02/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch055/record02/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch055/record02/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch055/record02/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- The primary PDF contains an unresolved 0.5 versus 1 mL/L vitamin-dose conflict; no final vitamin rates are calculated.
- Listed water input is not automatically a measured final-volume declaration. Current API g_l and solution volumes are direct provider evidence at their named stages, not independent proof of all primary arithmetic.
- Calcium 5% lacks an explicit basis in the primary. Na-aspartate, B12, EDTA ionic form and thiamine salt are not made more specific by guesswork.
- Historical reports and their decoded snippets remain derivative artifacts; current captured primary/API bytes are the scientific basis here. Existing current importer and cleanup guards are credited, without reconstructing historical execution.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T044230Z-batch055-record02-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Basic mineral medium: restore source stock boundaries and conflicting vitamin
  doses'
started_at: '2026-10-28T04:31:44.522101Z'
finished_at: '2026-10-28T04:42:30.212534Z'
reviewer:
  identity: Codex independent source reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh assessment of the inspected checkout and newly captured
    primary/provider/ontology evidence; no reconstruction of lost reviews and no record
    edits.
skill: .claude/skills/review-yaml-record/SKILL.md; .claude/skills/review-ingredient-concentrations/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Current DSM1615 and its provider separate buffer, trace elements and four
  vitamin stocks. Local direct ingredients mix receiving-medium rates with stock strengths
  and a sodium-hydroxide solvent volume. Existing preparation is substantial but over-scoped.
  The primary main-table vitamin dose conflicts with its footer and is retained as
  unresolved.
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
  - path: data/merge_yaml/merged/Basic_mineral_medium.yaml
    sha256: 71ee5bf4f1636438925b3cfbaa8fd39cf0e745e72485ce3de9421710e6bde0e2
    role: target
  - path: data/normalized_yaml/bacterial/basic_mineral_medium.yaml
    sha256: fffd65174f31b1ce85c5fa3f80591021dc0e36ebb24d466f568464936f06e9ad
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/basic_mineral_medium.yaml.md
    sha256: 5cd22108704b02f5432f2e8b2c04c01c0ab899b25b66a32b2a48134d474afef6
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Basic_mineral_medium.md
    sha256: 48b6640010e1b69342c4434229eadb31530ef0904b89ba4330decfc1543fb233
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/basic_mineral_medium.md
    sha256: f37c198f3dea6089c0bc54b7747c0b8d8e6d118a509f2a9e9603cc5c40a659c8
    role: context
  - path: reports/yaml_record_review/20260921T185556Z-Basic_mineral_medium.md
    sha256: 0cdd31a8210a2c9723a5c9e0668afa968d0737306b311cdb7ca2a158c66d2a32
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: 6116d95493b8f91faed19956301291a73d090a3b83671303650a561798933456
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
    role: context
  - path: src/culturemech/import/mediadb_importer.py
    sha256: 5c2d98caf450ee8bb2f73f112e4edab7c3e0f2fa5f2aa7bd2a34e6fd2fdfd4d0
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
  - path: src/culturemech/merge/fingerprint.py
    sha256: 9bc62b7f462b26775e7dff15bb91beb653ba8f1642b247466dba1c0366ed8a9e
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
  description: Full selected record and exact maintained contributors; external source
    limits explicitly retained.
  selection: Actual batch055 native selection index 02.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001096
targets:
- target_id: CultureMech:001096
  path: data/merge_yaml/merged/Basic_mineral_medium.yaml
  label: basic_mineral_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basic_mineral_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:001096
  command: just validate-schema data/merge_yaml/merged/Basic_mineral_medium.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
  scope_note: Exact selected target; scientific source and owner assessments are separate.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:001096
  command: just validate-strict data/merge_yaml/merged/Basic_mineral_medium.yaml --out
    REVIEW_WORK/batch055/record02/strict.tsv --workers 1
  exit_code: 0
  evidence_ids:
  - validate-strict
  scope_note: Exact selected target; scientific source and owner assessments are separate.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:001096
  command: just validate-terms data/merge_yaml/merged/Basic_mineral_medium.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
  scope_note: Exact selected target; scientific source and owner assessments are separate.
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Native reference checker performed zero reference checks; this is not claim
    authentication.
  target_ids:
  - CultureMech:001096
  command: just validate-references data/merge_yaml/merged/Basic_mineral_medium.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/Basic_mineral_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T04:41:57.389818Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 71ee5bf4f1636438925b3cfbaa8fd39cf0e745e72485ce3de9421710e6bde0e2
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/basic_mineral_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T04:41:57.389818Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: fffd65174f31b1ce85c5fa3f80591021dc0e36ebb24d466f568464936f06e9ad
- evidence_id: dsm1615
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1615.pdf
  locator: Entire pages 1–2; main assembly, trace stock and four vitamin stocks
  accessed_at: '2026-10-28T04:32:46.058756Z'
  support: supports
  summary: Complete two-page primary PDF, including literal copper chloride pentahydrate,
    trace-only pH and the conflicting vitamin doses. Both PDF pages were visually
    inspected.
  snapshot_sha256: 67c48c0397fbb5add36f04d2995f30ca93ba57daac554c5603cca65fddb1ce05
- evidence_id: api1615
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1615
  locator: $.data.medium and all $.data.solutions
  accessed_at: '2026-10-28T04:32:45.964892Z'
  support: supports
  summary: Current exact medium1615 API declares eight solution objects and source-specific
    g_l/mmol_l fields. Numerical correspondence is credited only at its own stock
    or main-solution stage.
  snapshot_sha256: 8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29
- evidence_id: provider-stage-census
  kind: record_content
  reference: REVIEW_WORK/batch055/record02/provider-stage-census.json
  accessed_at: '2026-10-28T04:41:57.440551Z'
  support: context_only
  summary: Lossless eight-solution recipe/step inventory including every source amount,
    unit, attribute, volume, g_l and mmol_l.
  snapshot_sha256: 660702040338fc97a6b45faf4c50776c762c44cf983f0226191d3cfe26bfb03d
- evidence_id: pdf-visual-1
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1615.pdf
  locator: PDF page 1; render REVIEW_WORK/batch055/record02/dsm1615-page-1.png
  accessed_at: '2026-10-28T04:41:57.441461Z'
  support: supports
  summary: Visual primary-page inspection confirms printed amounts, stock headings
    and source dose conflict.
  snapshot_sha256: 7d22040fba4efbb9502cb6a50218710915a9b859be0a243600ddef4d5cfd5041
- evidence_id: pdf-visual-2
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1615.pdf
  locator: PDF page 2; render REVIEW_WORK/batch055/record02/dsm1615-page-2.png
  accessed_at: '2026-10-28T04:41:57.442376Z'
  support: supports
  summary: Visual primary-page inspection confirms printed amounts, stock headings
    and source dose conflict.
  snapshot_sha256: 9c715b551a9d7117469c2cf943a100154f455645898bca7d372ea4c9db17e367
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition/_parse_api_solutions/_is_api_stock_addition
  accessed_at: '2026-10-28T04:41:57.389818Z'
  support: context_only
  summary: Current _parse_api_composition uses the first solution and skips stock/solvent
    edges; _parse_api_solutions retains referenced stocks separately. These present
    safeguards are credited, not blamed for historical flattening.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: merge_ingredient_group
  accessed_at: '2026-10-28T04:41:57.389818Z'
  support: context_only
  summary: Current merge_ingredient_group keeps the first concentration and flags
    differing values; it does not sum stock concentrations.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer-merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T04:41:57.389818Z'
  support: context_only
  summary: Current sole-owner merge copies maintained content and adds generated metadata;
    it does not repair stock structure or authenticate source arithmetic.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: historical-1
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/basic_mineral_medium.yaml.md
  locator: Entire report; exact Record header and all claim rows
  accessed_at: '2026-10-28T04:41:57.389818Z'
  support: context_only
  summary: Full exact selected-path historical report read. Its past source-access
    statements and snippets are derivative evidence; the cited raw response is not
    automatically authenticated.
  snapshot_sha256: 5cd22108704b02f5432f2e8b2c04c01c0ab899b25b66a32b2a48134d474afef6
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Basic_mineral_medium.md
  locator: Entire report; exact Record header and all claim rows
  accessed_at: '2026-10-28T04:41:57.389818Z'
  support: context_only
  summary: Full exact selected-path historical report read. Its past source-access
    statements and snippets are derivative evidence; the cited raw response is not
    automatically authenticated.
  snapshot_sha256: 48b6640010e1b69342c4434229eadb31530ef0904b89ba4330decfc1543fb233
- evidence_id: historical-3
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/basic_mineral_medium.md
  locator: Entire report; exact Record header and all claim rows
  accessed_at: '2026-10-28T04:41:57.389818Z'
  support: context_only
  summary: Full exact selected-path historical report read. Its past source-access
    statements and snippets are derivative evidence; the cited raw response is not
    automatically authenticated.
  snapshot_sha256: f37c198f3dea6089c0bc54b7747c0b8d8e6d118a509f2a9e9603cc5c40a659c8
- evidence_id: historical-4
  kind: record_content
  reference: reports/yaml_record_review/20260921T185556Z-Basic_mineral_medium.md
  locator: Entire report; exact Record header and all claim rows
  accessed_at: '2026-10-28T04:41:57.389818Z'
  support: context_only
  summary: Full exact selected-path historical report read. Its past source-access
    statements and snippets are derivative evidence; the cited raw response is not
    automatically authenticated.
  snapshot_sha256: 0cdd31a8210a2c9723a5c9e0668afa968d0737306b311cdb7ca2a158c66d2a32
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch055/record02/historical-reader.json
  accessed_at: '2026-10-28T04:41:57.445656Z'
  support: context_only
  summary: Complete selected target/owner historical reports and exact report hashes,
    preserving derivative-only limits.
  snapshot_sha256: 95a641e3459e373fb149f1ea0af817c08510b62ad781bda0de5660cb6da11321
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:49.479874Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 1635f67d01e00cabdef4ed0d9ef6d5383787c56bd0447051deb90ad353b499a2
- evidence_id: chebi32954
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32954
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:50.028297Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 34c7d0dea7bc001a0a3b3b388138837cb1aba3b252017bc1ff8625b7a3ff655d
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:52.817765Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: df8f702eb5b9d3e50209bfa2b0c4b6f1db30c116e56a58e348cbd4bf3bc0ebc1
- evidence_id: chebi16643
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16643
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:47.566680Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b61d0bd7a885fc9c19e0c04d68e7638a8a9a51d373e48ea96722d0c3d4f2c374
- evidence_id: chebi4735
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_4735
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:50.906347Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f07827212a55318fd8fcd95e1827e108ea86bb3e185e227c96706b7b0f8a60cd
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:52.444680Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: e12b865122aab78645385260e1e83ff28f3c45365cb67c9181166628f68974b3
- evidence_id: chebi35176
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_35176
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:50.728115Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: bc0c5111bcf25886ba3e493084197b581a719cb597c5e27663ceed08d52b6661
- evidence_id: chebi63041
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63041
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:51.627460Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a4b28bcd431eb1bf3473ada547e008fa0c1541daf0fcab8d992ac55f2e17dd73
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:50.245936Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f23e1405347fa9d8a0826d4dd1279b7cdec8361390d20e439154dcbbd386a2d4
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:51.321973Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 31dc996638b0cc1341ed24fcb38ec344af726c99d376ac94e952210fcb9ed583
- evidence_id: chebi91245
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91245
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:53.090568Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: d2337e07c103c3fb5c64d35dc7cb6b9e5193c0586ecd8d33e1043e4fbfe2543f
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:50.556539Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a43b8268f70ae50c4cfbc53e12bbd195618c521619cfab8f71d3704b338af95b
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:52.090143Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0271a149a298ff837ad8f690ce8cb0acf111f5d25c5efaf6fa828401ab951d56
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:47.022231Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 97e9c2b05f3937c5beeebb4e6338aa6730f9e422ee0e7570a6c622dda8d97a86
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63036
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:51.446529Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 913baf38abc38dd61f05c5d636fd6532b70a668673a1f5762f290d2b67270164
- evidence_id: chebi18385
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_18385
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:48.564035Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 6370e2e611ce20ae9b889e646ff290e866b4d0afa66fe1fd24e53864daec2908
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31345
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:49.315308Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: d2a04309eb6976fd395f9684ec4c3f5192362e2b6b75464b0af128a28e188d25
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15956
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:47.346781Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0d2e75e0bd98dbffff14d85a41dfd0af8aae2a8d65a945d34a4126a17091c2b8
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30753
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:49.206550Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 42ea4022bd68e8fa28962bc496ca757174da7bbd18ce06b7f3d521885609a50c
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15940
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:46.968032Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2890ef915cd546e70c1e638af285a3cc19b8299ae7722d00b43a40170a57ab8a
- evidence_id: chebi16709
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16709
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:47.778750Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 3b055ff5d94d307b9d6d97cebfa2030b03966247245866eb796c099dbe08327c
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32145
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:49.643629Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 1f39a220b091088af20782dd27577fb7ca89e037d2b0ea83e76075fb8d77b797
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_27470
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:48.959900Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: dcee85bb585d3a73341ab66eff772dc6361330b3c899c4daecbda49d5e84e590
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17015
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T04:32:48.119288Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f8bec809c7ba5a36faea58b8fe1b5110f0d75dbd4ac1929a121cd352bce63309
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch055/record02/quantity-inventory.json
  accessed_at: '2026-10-28T04:41:57.482258Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 8599b49cb5eeb1a3b04e808915d9a4969b035ac3790f03bdc5f5e530ed869e45
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch055/record02/grounding-inventory.json
  accessed_at: '2026-10-28T04:41:57.482355Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: 3f7f6b6df5e64c595d816655a993dabca0c8112511f8bd43191e21a6d765d32d
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch055/record02/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T04:41:57.482523Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 8b02e5823f731ebb1671669bf977321b03ab8e7f80d071eb39982be8d6943364
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch055/record02/scalar-census.json
  accessed_at: '2026-10-28T04:41:57.482570Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: 4629cbb05e5b71a5cfef12aecfd71d5a4ca3e1e913a399b8e0ce55b060a9ce4f
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch055/record02/validate-schema.json
  accessed_at: '2026-10-28T04:31:46.160408Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: 852d8d64e1844bef98f27a6c6572252dca9b9209de39396da7085a0ed1c22aa8
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch055/record02/validate-strict.json
  accessed_at: '2026-10-28T04:31:47.476950Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch055/record02/strict.tsv\n"
  snapshot_sha256: cd3be8e09de2a3aea25c8f51cf360580855241a985898a832e0b8b64479f02aa
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch055/record02/validate-terms.json
  accessed_at: '2026-10-28T04:31:48.920858Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: 817aef8e2ce05b463b55f418567e46c51cf3953ae811384aa9ee348094825bdd
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch055/record02/validate-references.json
  accessed_at: '2026-10-28T04:31:49.936404Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: de418fd52bd2263d68e29b5dc39106c5ead25af39fd8fa511362db379daaa5f4
assessments:
- assessment_id: a1
  area: identity
  topic: Exact DSM1615 identity and unchanged supported claims
  outcome: supported
  summary: The selected record and its sole maintained owner are DSM1615. Main pH,
    all nine existing preparation statements and direct provider rate correspondences
    are explicitly credited within their source scopes. No external strain or growth
    claim is added.
  target_ids:
  - CultureMech:001096
  evidence_ids:
  - dsm1615
  - api1615
  - owner-1
- assessment_id: a2
  area: grounding
  topic: Hydrates, generic names and current legacy status
  outcome: concern
  summary: CuCl2 x 5 H2O is literally printed and CHEBI:91245 matches that pentahydrate.
    Nickel chloride hexahydrate is broader/mismatched against CHEBI:34887, whose formula
    lacks waters. Source EDTA and thiamine do not warrant inventing salts; Na-aspartate
    and B12 remain chemically underspecified. MediaIngredientMech:000898 has no row
    in the current packaged catalog, without proving historical invalidity. All other
    asserted primary/secondary labels are current OLS labels.
  target_ids:
  - CultureMech:001096
  evidence_ids:
  - dsm1615
  - chebi91245
  - chebi34887
  - grounding
- assessment_id: a3
  area: quantity
  topic: Complete quantity and numeric preparation audit
  outcome: concern
  summary: Every local concentration field has an explicit disposition; source-only
    doses, batch volumes and conditional preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:001096
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "MgSO4 x 7 H2O", "source": {"evidence_id":
    "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path":
    "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"attribute\":
    \"1 M\",\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.246476,\n                        \"mmol_l\":
    1,\n                        \"optional\": 0\n                    }", "quote_basis":
    "Literal raw JSON substring, independently decoded to the located object"}, "decision":
    "evidence_only", "rationale": "The current provider explicitly declares this g_l
    value on Main sol.1615, and the primary specifies its stock dose and strength.
    Retain the provider-supported numerical correspondence while adding the missing
    stock/addition context; it is not an independently measured additive final volume.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.246476",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current provider
    explicitly declares this g_l value on Main sol.1615, and the primary specifies
    its stock dose and strength. Retain the provider-supported numerical correspondence
    while adding the missing stock/addition context; it is not an independently measured
    additive final volume."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.246476",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current provider
    explicitly declares this g_l value on Main sol.1615, and the primary specifies
    its stock dose and strength. Retain the provider-supported numerical correspondence
    while adding the missing stock/addition context; it is not an independently measured
    additive final volume."}]}, {"quantity_id": "q2", "topic": "Sodium acetate", "source":
    {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Sodium acetate\",\n                        \"compound_id\": 731,\n                        \"attribute\":
    \"1 M\",\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.8203,\n                        \"mmol_l\":
    10,\n                        \"optional\": 0\n                    }", "quote_basis":
    "Literal raw JSON substring, independently decoded to the located object"}, "decision":
    "evidence_only", "rationale": "The current provider explicitly declares this g_l
    value on Main sol.1615, and the primary specifies its stock dose and strength.
    Retain the provider-supported numerical correspondence while adding the missing
    stock/addition context; it is not an independently measured additive final volume.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.8203",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current provider
    explicitly declares this g_l value on Main sol.1615, and the primary specifies
    its stock dose and strength. Retain the provider-supported numerical correspondence
    while adding the missing stock/addition context; it is not an independently measured
    additive final volume."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.8203",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current provider
    explicitly declares this g_l value on Main sol.1615, and the primary specifies
    its stock dose and strength. Retain the provider-supported numerical correspondence
    while adding the missing stock/addition context; it is not an independently measured
    additive final volume."}]}, {"quantity_id": "q3", "topic": "CaCl2 x 2 H2O", "source":
    {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"condition\":
    \"\",\n                        \"attribute\": \"5%\",\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.340101,\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "evidence_only", "rationale": "The
    current provider explicitly declares this g_l value on Main sol.1615, and the
    primary specifies its stock dose and strength. Retain the provider-supported numerical
    correspondence while adding the missing stock/addition context; it is not an independently
    measured additive final volume. The primary 5% calcium stock does not state a
    mass/volume percentage basis; the provider 0.05 g/L is credited as its own assertion,
    not independently derived from that bare percentage.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[2].concentration",
    "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The current provider explicitly declares this g_l value on Main
    sol.1615, and the primary specifies its stock dose and strength. Retain the provider-supported
    numerical correspondence while adding the missing stock/addition context; it is
    not an independently measured additive final volume. The primary 5% calcium stock
    does not state a mass/volume percentage basis; the provider 0.05 g/L is credited
    as its own assertion, not independently derived from that bare percentage."},
    {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path":
    "ingredients[2].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "The current provider explicitly declares
    this g_l value on Main sol.1615, and the primary specifies its stock dose and
    strength. Retain the provider-supported numerical correspondence while adding
    the missing stock/addition context; it is not an independently measured additive
    final volume. The primary 5% calcium stock does not state a mass/volume percentage
    basis; the provider 0.05 g/L is credited as its own assertion, not independently
    derived from that bare percentage."}]}, {"quantity_id": "q4", "topic": "Na-aspartate",
    "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Na-aspartate\",\n                        \"compound_id\": 228,\n                        \"attribute\":
    \"2 M\",\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.35414,\n                        \"mmol_l\":
    2,\n                        \"optional\": 0\n                    }", "quote_basis":
    "Literal raw JSON substring, independently decoded to the located object"}, "decision":
    "evidence_only", "rationale": "The current provider explicitly declares this g_l
    value on Main sol.1615, and the primary specifies its stock dose and strength.
    Retain the provider-supported numerical correspondence while adding the missing
    stock/addition context; it is not an independently measured additive final volume.
    Sodium aspartate form/stereochemistry is not resolved from this name; no ontology
    or molecular-weight-based replacement is guessed.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[3].concentration",
    "stored_value": {"value": "0.35414", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The current provider explicitly declares this g_l value on Main
    sol.1615, and the primary specifies its stock dose and strength. Retain the provider-supported
    numerical correspondence while adding the missing stock/addition context; it is
    not an independently measured additive final volume. Sodium aspartate form/stereochemistry
    is not resolved from this name; no ontology or molecular-weight-based replacement
    is guessed."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.35414",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current provider
    explicitly declares this g_l value on Main sol.1615, and the primary specifies
    its stock dose and strength. Retain the provider-supported numerical correspondence
    while adding the missing stock/addition context; it is not an independently measured
    additive final volume. Sodium aspartate form/stereochemistry is not resolved from
    this name; no ontology or molecular-weight-based replacement is guessed."}]},
    {"quantity_id": "q5", "topic": "L-Methionine", "source": {"evidence_id": "api1615",
    "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin",
    "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"L-Methionine\",\n                        \"compound_id\": 1330,\n                        \"attribute\":
    \"50 mM, filter sterilized, neutralised\",\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.0074605,\n                        \"mmol_l\": 0.05,\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "evidence_only", "rationale": "The
    current provider explicitly declares this g_l value on Main sol.1615, and the
    primary specifies its stock dose and strength. Retain the provider-supported numerical
    correspondence while adding the missing stock/addition context; it is not an independently
    measured additive final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.0074605",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current provider
    explicitly declares this g_l value on Main sol.1615, and the primary specifies
    its stock dose and strength. Retain the provider-supported numerical correspondence
    while adding the missing stock/addition context; it is not an independently measured
    additive final volume."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.0074605",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current provider
    explicitly declares this g_l value on Main sol.1615, and the primary specifies
    its stock dose and strength. Retain the provider-supported numerical correspondence
    while adding the missing stock/addition context; it is not an independently measured
    additive final volume."}]}, {"quantity_id": "q6", "topic": "EDTA", "source": {"evidence_id":
    "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path":
    "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"EDTA\",\n                        \"compound_id\": 271,\n                        \"amount\":
    5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    5,\n                        \"mmol_l\": 17.1092,\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "correct", "rationale": "This value
    is the provider-declared trace-stock g/L value, matching the primary batch mass
    and its listed 1000 mL water. It is not the direct receiving-medium rate; the
    primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather
    than flattening or silently asserting a measured final volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[5].concentration",
    "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This value is the provider-declared trace-stock g/L value, matching the primary
    batch mass and its listed 1000 mL water. It is not the direct receiving-medium
    rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately
    rather than flattening or silently asserting a measured final volume."}, {"path":
    "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[5].concentration",
    "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This value is the provider-declared trace-stock g/L value, matching the primary
    batch mass and its listed 1000 mL water. It is not the direct receiving-medium
    rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately
    rather than flattening or silently asserting a measured final volume."}]}, {"quantity_id":
    "q7", "topic": "FeSO4 x 7 H2O", "source": {"evidence_id": "api1615", "reference":
    "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin",
    "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\":
    2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    2,\n                        \"mmol_l\": 7.19386,\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "correct", "rationale": "This value
    is the provider-declared trace-stock g/L value, matching the primary batch mass
    and its listed 1000 mL water. It is not the direct receiving-medium rate; the
    primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather
    than flattening or silently asserting a measured final volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[6].concentration",
    "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This value is the provider-declared trace-stock g/L value, matching the primary
    batch mass and its listed 1000 mL water. It is not the direct receiving-medium
    rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately
    rather than flattening or silently asserting a measured final volume."}, {"path":
    "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[6].concentration",
    "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This value is the provider-declared trace-stock g/L value, matching the primary
    batch mass and its listed 1000 mL water. It is not the direct receiving-medium
    rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately
    rather than flattening or silently asserting a measured final volume."}]}, {"quantity_id":
    "q8", "topic": "ZnSO4", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"ZnSO4\",\n                        \"compound_id\": 441,\n                        \"amount\":
    0.1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.619579,\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "correct", "rationale": "This value
    is the provider-declared trace-stock g/L value, matching the primary batch mass
    and its listed 1000 mL water. It is not the direct receiving-medium rate; the
    primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather
    than flattening or silently asserting a measured final volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[7].concentration",
    "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This value is the provider-declared trace-stock g/L value, matching the primary
    batch mass and its listed 1000 mL water. It is not the direct receiving-medium
    rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately
    rather than flattening or silently asserting a measured final volume."}, {"path":
    "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[7].concentration",
    "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This value is the provider-declared trace-stock g/L value, matching the primary
    batch mass and its listed 1000 mL water. It is not the direct receiving-medium
    rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately
    rather than flattening or silently asserting a measured final volume."}]}, {"quantity_id":
    "q9", "topic": "MnCl2", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[1].recipe[3]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"MnCl2\",\n                        \"compound_id\": 980,\n                        \"amount\":
    0.03,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.03,\n                        \"mmol_l\": 0.238398,\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "correct", "rationale": "This value
    is the provider-declared trace-stock g/L value, matching the primary batch mass
    and its listed 1000 mL water. It is not the direct receiving-medium rate; the
    primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather
    than flattening or silently asserting a measured final volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[8].concentration",
    "stored_value": {"value": "0.03", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This value is the provider-declared trace-stock g/L value, matching the primary
    batch mass and its listed 1000 mL water. It is not the direct receiving-medium
    rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately
    rather than flattening or silently asserting a measured final volume."}, {"path":
    "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[8].concentration",
    "stored_value": {"value": "0.03", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This value is the provider-declared trace-stock g/L value, matching the primary
    batch mass and its listed 1000 mL water. It is not the direct receiving-medium
    rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately
    rather than flattening or silently asserting a measured final volume."}]}, {"quantity_id":
    "q10", "topic": "H3BO3", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[1].recipe[4]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\":
    0.3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "correct", "rationale": "This value
    is the provider-declared trace-stock g/L value, matching the primary batch mass
    and its listed 1000 mL water. It is not the direct receiving-medium rate; the
    primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather
    than flattening or silently asserting a measured final volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[9].concentration",
    "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This value is the provider-declared trace-stock g/L value, matching the primary
    batch mass and its listed 1000 mL water. It is not the direct receiving-medium
    rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately
    rather than flattening or silently asserting a measured final volume."}, {"path":
    "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[9].concentration",
    "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This value is the provider-declared trace-stock g/L value, matching the primary
    batch mass and its listed 1000 mL water. It is not the direct receiving-medium
    rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately
    rather than flattening or silently asserting a measured final volume."}]}, {"quantity_id":
    "q11", "topic": "CoCl2 x 6 H2O", "source": {"evidence_id": "api1615", "reference":
    "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin",
    "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[1].recipe[5]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\":
    0.2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "correct", "rationale": "This value
    is the provider-declared trace-stock g/L value, matching the primary batch mass
    and its listed 1000 mL water. It is not the direct receiving-medium rate; the
    primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather
    than flattening or silently asserting a measured final volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[10].concentration",
    "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This value is the provider-declared trace-stock g/L value, matching the primary
    batch mass and its listed 1000 mL water. It is not the direct receiving-medium
    rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately
    rather than flattening or silently asserting a measured final volume."}, {"path":
    "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[10].concentration",
    "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This value is the provider-declared trace-stock g/L value, matching the primary
    batch mass and its listed 1000 mL water. It is not the direct receiving-medium
    rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately
    rather than flattening or silently asserting a measured final volume."}]}, {"quantity_id":
    "q12", "topic": "CuCl2 x 5 H2O", "source": {"evidence_id": "api1615", "reference":
    "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin",
    "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"CuCl2 x 5 H2O\",\n                        \"compound_id\": 838,\n                        \"amount\":
    0.01,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.01,\n                        \"mmol_l\": 0.0445379,\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "correct", "rationale": "This value
    is the provider-declared trace-stock g/L value, matching the primary batch mass
    and its listed 1000 mL water. It is not the direct receiving-medium rate; the
    primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather
    than flattening or silently asserting a measured final volume. CuCl2 x 5 H2O is
    literal in the primary; its pentahydrate identity must not be silently changed
    to a more familiar hydrate.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared
    trace-stock g/L value, matching the primary batch mass and its listed 1000 mL
    water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace
    stock. Preserve the stock and dose separately rather than flattening or silently
    asserting a measured final volume. CuCl2 x 5 H2O is literal in the primary; its
    pentahydrate identity must not be silently changed to a more familiar hydrate."},
    {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path":
    "ingredients[11].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This value is the provider-declared trace-stock
    g/L value, matching the primary batch mass and its listed 1000 mL water. It is
    not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve
    the stock and dose separately rather than flattening or silently asserting a measured
    final volume. CuCl2 x 5 H2O is literal in the primary; its pentahydrate identity
    must not be silently changed to a more familiar hydrate."}]}, {"quantity_id":
    "q13", "topic": "NiCl2 x 6 H2O", "source": {"evidence_id": "api1615", "reference":
    "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin",
    "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[1].recipe[7]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\":
    0.02,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "correct", "rationale": "This value
    is the provider-declared trace-stock g/L value, matching the primary batch mass
    and its listed 1000 mL water. It is not the direct receiving-medium rate; the
    primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather
    than flattening or silently asserting a measured final volume. The source names
    nickel chloride hexahydrate, whereas the local CHEBI object denotes nickel dichloride
    without those waters.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This value is the provider-declared
    trace-stock g/L value, matching the primary batch mass and its listed 1000 mL
    water. It is not the direct receiving-medium rate; the primary adds 1 mL/L trace
    stock. Preserve the stock and dose separately rather than flattening or silently
    asserting a measured final volume. The source names nickel chloride hexahydrate,
    whereas the local CHEBI object denotes nickel dichloride without those waters."},
    {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path":
    "ingredients[12].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This value is the provider-declared trace-stock
    g/L value, matching the primary batch mass and its listed 1000 mL water. It is
    not the direct receiving-medium rate; the primary adds 1 mL/L trace stock. Preserve
    the stock and dose separately rather than flattening or silently asserting a measured
    final volume. The source names nickel chloride hexahydrate, whereas the local
    CHEBI object denotes nickel dichloride without those waters."}]}, {"quantity_id":
    "q14", "topic": "Na2MoO4 x 2 H2O", "source": {"evidence_id": "api1615", "reference":
    "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin",
    "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[1].recipe[8]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\":
    0.02,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.0826617,\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "correct", "rationale": "This value
    is the provider-declared trace-stock g/L value, matching the primary batch mass
    and its listed 1000 mL water. It is not the direct receiving-medium rate; the
    primary adds 1 mL/L trace stock. Preserve the stock and dose separately rather
    than flattening or silently asserting a measured final volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[13].concentration",
    "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This value is the provider-declared trace-stock g/L value, matching the primary
    batch mass and its listed 1000 mL water. It is not the direct receiving-medium
    rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately
    rather than flattening or silently asserting a measured final volume."}, {"path":
    "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "ingredients[13].concentration",
    "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This value is the provider-declared trace-stock g/L value, matching the primary
    batch mass and its listed 1000 mL water. It is not the direct receiving-medium
    rate; the primary adds 1 mL/L trace stock. Preserve the stock and dose separately
    rather than flattening or silently asserting a measured final volume."}]}, {"quantity_id":
    "q15", "topic": "K2HPO4", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"attribute\":
    \"0.1 M\",\n                        \"amount\": 130,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 2.26429,\n                        \"mmol_l\":
    13,\n                        \"optional\": 0\n                    }", "quote_basis":
    "Literal raw JSON substring, independently decoded to the located object"}, "decision":
    "correct", "rationale": "The current rate is explicitly declared on the 1000 mL
    K-P buffer object. The primary gives the corresponding 0.1 M stock volume, plus
    800 mL water, before post-sterilization additions. Preserve this buffer-basis
    rate and make its stage explicit; do not silently treat pre-addition buffer volume
    as measured final-medium volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "2.26429",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current rate is explicitly
    declared on the 1000 mL K-P buffer object. The primary gives the corresponding
    0.1 M stock volume, plus 800 mL water, before post-sterilization additions. Preserve
    this buffer-basis rate and make its stage explicit; do not silently treat pre-addition
    buffer volume as measured final-medium volume."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "2.26429",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current rate is explicitly
    declared on the 1000 mL K-P buffer object. The primary gives the corresponding
    0.1 M stock volume, plus 800 mL water, before post-sterilization additions. Preserve
    this buffer-basis rate and make its stage explicit; do not silently treat pre-addition
    buffer volume as measured final-medium volume."}]}, {"quantity_id": "q16", "topic":
    "KH2PO4", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[2].recipe[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"attribute\":
    \"0.1 M\",\n                        \"amount\": 70,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.952595,\n                        \"mmol_l\":
    7,\n                        \"optional\": 0\n                    }", "quote_basis":
    "Literal raw JSON substring, independently decoded to the located object"}, "decision":
    "correct", "rationale": "The current rate is explicitly declared on the 1000 mL
    K-P buffer object. The primary gives the corresponding 0.1 M stock volume, plus
    800 mL water, before post-sterilization additions. Preserve this buffer-basis
    rate and make its stage explicit; do not silently treat pre-addition buffer volume
    as measured final-medium volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.952595",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current rate is explicitly
    declared on the 1000 mL K-P buffer object. The primary gives the corresponding
    0.1 M stock volume, plus 800 mL water, before post-sterilization additions. Preserve
    this buffer-basis rate and make its stage explicit; do not silently treat pre-addition
    buffer volume as measured final-medium volume."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.952595",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current rate is explicitly
    declared on the 1000 mL K-P buffer object. The primary gives the corresponding
    0.1 M stock volume, plus 800 mL water, before post-sterilization additions. Preserve
    this buffer-basis rate and make its stage explicit; do not silently treat pre-addition
    buffer volume as measured final-medium volume."}]}, {"quantity_id": "q17", "topic":
    "Thiamine", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[4].recipe[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Thiamine\",\n                        \"compound_id\": 666,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.188423,\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "correct", "rationale": "This rate
    belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that
    solvent input and the provider explicitly declares this stock g_l. The four stocks
    are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct
    final-medium concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to
    one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input
    and the provider explicitly declares this stock g_l. The four stocks are mixed
    1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium
    concentration."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to
    one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input
    and the provider explicitly declares this stock g_l. The four stocks are mixed
    1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium
    concentration."}]}, {"quantity_id": "q18", "topic": "Calcium pantothenate", "source":
    {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[4].recipe[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.104925,\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "correct", "rationale": "This rate
    belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that
    solvent input and the provider explicitly declares this stock g_l. The four stocks
    are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct
    final-medium concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to
    one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input
    and the provider explicitly declares this stock g_l. The four stocks are mixed
    1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium
    concentration."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to
    one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input
    and the provider explicitly declares this stock g_l. The four stocks are mixed
    1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium
    concentration."}]}, {"quantity_id": "q19", "topic": "Biotin", "source": {"evidence_id":
    "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path":
    "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[5].recipe[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\":
    2,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "correct", "rationale": "This rate
    belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that
    solvent input and the provider explicitly declares this stock g_l. The four stocks
    are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct
    final-medium concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to
    one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input
    and the provider explicitly declares this stock g_l. The four stocks are mixed
    1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium
    concentration."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to
    one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input
    and the provider explicitly declares this stock g_l. The four stocks are mixed
    1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium
    concentration."}]}, {"quantity_id": "q20", "topic": "PABA", "source": {"evidence_id":
    "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path":
    "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[5].recipe[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"PABA\",\n                        \"compound_id\": 1309,\n                        \"attribute\":
    \"p-aminobenzoic acid\",\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }", "quote_basis":
    "Literal raw JSON substring, independently decoded to the located object"}, "decision":
    "correct", "rationale": "This rate belongs to one 100 mL vitamin stock; the primary
    lists a mass in mg with that solvent input and the provider explicitly declares
    this stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus
    1 mL/L dose. It is not a direct final-medium concentration.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[19].concentration",
    "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This rate belongs to one 100 mL vitamin stock; the primary lists a mass in mg
    with that solvent input and the provider explicitly declares this stock g_l. The
    four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It
    is not a direct final-medium concentration."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to
    one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input
    and the provider explicitly declares this stock g_l. The four stocks are mixed
    1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium
    concentration."}]}, {"quantity_id": "q21", "topic": "Nicotinic acid", "source":
    {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[5].recipe[2]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "correct", "rationale": "This rate
    belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that
    solvent input and the provider explicitly declares this stock g_l. The four stocks
    are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct
    final-medium concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to
    one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input
    and the provider explicitly declares this stock g_l. The four stocks are mixed
    1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium
    concentration."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to
    one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input
    and the provider explicitly declares this stock g_l. The four stocks are mixed
    1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium
    concentration."}]}, {"quantity_id": "q22", "topic": "Pyridoxine", "source": {"evidence_id":
    "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path":
    "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[5].recipe[3]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Pyridoxine\",\n                        \"compound_id\": 637,\n                        \"amount\":
    10,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.591086,\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "correct", "rationale": "This rate
    belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that
    solvent input and the provider explicitly declares this stock g_l. The four stocks
    are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct
    final-medium concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to
    one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input
    and the provider explicitly declares this stock g_l. The four stocks are mixed
    1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium
    concentration."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to
    one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input
    and the provider explicitly declares this stock g_l. The four stocks are mixed
    1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium
    concentration."}]}, {"quantity_id": "q23", "topic": "NaOH", "source": {"evidence_id":
    "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path":
    "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[5].recipe[4]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"NaOH\",\n                        \"compound_id\": 256,\n                        \"attribute\":
    \"0.1N\",\n                        \"amount\": 100,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis":
    "Literal raw JSON substring, independently decoded to the located object"}, "decision":
    "correct", "rationale": "The source specifies 100 mL of 0.1 N NaOH as the solvent
    of the basic vitamin stock. Local 100 G_PER_L changes liquid volume into an unsupported
    mass rate. Preserve normality, volume and stock scope; do not retain or reinterpret
    100 g/L as a supported concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "ingredients[22].concentration", "stored_value": {"value": "100",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source specifies
    100 mL of 0.1 N NaOH as the solvent of the basic vitamin stock. Local 100 G_PER_L
    changes liquid volume into an unsupported mass rate. Preserve normality, volume
    and stock scope; do not retain or reinterpret 100 g/L as a supported concentration."},
    {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path":
    "ingredients[22].concentration", "stored_value": {"value": "100", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The source specifies 100 mL of 0.1 N NaOH
    as the solvent of the basic vitamin stock. Local 100 G_PER_L changes liquid volume
    into an unsupported mass rate. Preserve normality, volume and stock scope; do
    not retain or reinterpret 100 g/L as a supported concentration."}]}, {"quantity_id":
    "q24", "topic": "Folic acid", "source": {"evidence_id": "api1615", "reference":
    "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin",
    "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[6].recipe[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\":
    2,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "correct", "rationale": "This rate
    belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that
    solvent input and the provider explicitly declares this stock g_l. The four stocks
    are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct
    final-medium concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to
    one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input
    and the provider explicitly declares this stock g_l. The four stocks are mixed
    1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium
    concentration."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to
    one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input
    and the provider explicitly declares this stock g_l. The four stocks are mixed
    1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium
    concentration."}]}, {"quantity_id": "q25", "topic": "Riboflavin", "source": {"evidence_id":
    "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path":
    "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[6].recipe[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "correct", "rationale": "This rate
    belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that
    solvent input and the provider explicitly declares this stock g_l. The four stocks
    are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct
    final-medium concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to
    one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input
    and the provider explicitly declares this stock g_l. The four stocks are mixed
    1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium
    concentration."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to
    one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input
    and the provider explicitly declares this stock g_l. The four stocks are mixed
    1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium
    concentration."}]}, {"quantity_id": "q26", "topic": "B12", "source": {"evidence_id":
    "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path":
    "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[7].recipe[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"B12\",\n                        \"compound_id\": 1238,\n                        \"amount\":
    0.5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.00368895,\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "correct", "rationale": "This rate
    belongs to one 100 mL vitamin stock; the primary lists a mass in mg with that
    solvent input and the provider explicitly declares this stock g_l. The four stocks
    are mixed 1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct
    final-medium concentration. Generic B12 does not identify a particular cobalamin
    species; no chemical identity or molar conversion is inferred.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ingredients[25].concentration",
    "stored_value": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct",
    "rationale": "This rate belongs to one 100 mL vitamin stock; the primary lists
    a mass in mg with that solvent input and the provider explicitly declares this
    stock g_l. The four stocks are mixed 1:1:1:1 before an unresolved 0.5 versus 1
    mL/L dose. It is not a direct final-medium concentration. Generic B12 does not
    identify a particular cobalamin species; no chemical identity or molar conversion
    is inferred."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.005",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This rate belongs to
    one 100 mL vitamin stock; the primary lists a mass in mg with that solvent input
    and the provider explicitly declares this stock g_l. The four stocks are mixed
    1:1:1:1 before an unresolved 0.5 versus 1 mL/L dose. It is not a direct final-medium
    concentration. Generic B12 does not identify a particular cobalamin species; no
    chemical identity or molar conversion is inferred."}]}, {"quantity_id": "q27",
    "topic": "Existing preparation step 1", "source": {"evidence_id": "api1615", "reference":
    "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin",
    "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"step\": \"pH 7.0-7.2\"\n                    }",
    "quote_basis": "Literal raw JSON substring, independently decoded to the located
    object"}, "decision": "evidence_only", "rationale": "The existing pH 7.0–7.2 is
    the buffer/main medium scope, not the acidic trace-stock pH.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "preparation_steps[0].description",
    "stored_value": "pH 7.0-7.2", "decision": "evidence_only", "rationale": "The existing
    pH 7.0–7.2 is the buffer/main medium scope, not the acidic trace-stock pH."},
    {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path":
    "preparation_steps[0].description", "stored_value": "pH 7.0-7.2", "decision":
    "evidence_only", "rationale": "The existing pH 7.0–7.2 is the buffer/main medium
    scope, not the acidic trace-stock pH."}]}, {"quantity_id": "q28", "topic": "Existing
    preparation step 2", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[0].steps[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"step\":
    \"After sterilization add from sterile stock solutions:\"\n                    }",
    "quote_basis": "Literal raw JSON substring, independently decoded to the located
    object"}, "decision": "evidence_only", "rationale": "Preserve the existing instruction
    to add sterile stocks after sterilization; attach the corresponding stock objects
    and doses.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "preparation_steps[1].description", "stored_value": "After sterilization
    add from sterile stock solutions:", "decision": "evidence_only", "rationale":
    "Preserve the existing instruction to add sterile stocks after sterilization;
    attach the corresponding stock objects and doses."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "preparation_steps[1].description", "stored_value": "After sterilization
    add from sterile stock solutions:", "decision": "evidence_only", "rationale":
    "Preserve the existing instruction to add sterile stocks after sterilization;
    attach the corresponding stock objects and doses."}]}, {"quantity_id": "q29",
    "topic": "Existing preparation step 3", "source": {"evidence_id": "api1615", "reference":
    "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin",
    "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[0].steps[2]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"step\":
    \"might result in colloid formation, especially when added into\\r\\nhot medium,
    but dissolves after vigorous shaking\"\n                    }", "quote_basis":
    "Literal raw JSON substring, independently decoded to the located object"}, "decision":
    "evidence_only", "rationale": "Preserve the existing calcium-stock colloid warning
    and its hot-medium/shaking context; it is not a new quantity.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "preparation_steps[2].description",
    "stored_value": "might result in colloid formation, especially when added into\r\nhot
    medium, but dissolves after vigorous shaking", "decision": "evidence_only", "rationale":
    "Preserve the existing calcium-stock colloid warning and its hot-medium/shaking
    context; it is not a new quantity."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "preparation_steps[2].description", "stored_value": "might result
    in colloid formation, especially when added into\r\nhot medium, but dissolves
    after vigorous shaking", "decision": "evidence_only", "rationale": "Preserve the
    existing calcium-stock colloid warning and its hot-medium/shaking context; it
    is not a new quantity."}]}, {"quantity_id": "q30", "topic": "Existing preparation
    step 4", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"step\": \"Adjust pH to 3.0-4.0 with HCl.\"\n                    }",
    "quote_basis": "Literal raw JSON substring, independently decoded to the located
    object"}, "decision": "correct", "rationale": "The existing pH 3.0–4.0 instruction
    belongs only to the trace stock. It must not override main pH 7.0–7.2.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "preparation_steps[3].description",
    "stored_value": "Adjust pH to 3.0-4.0 with HCl.", "decision": "correct", "rationale":
    "The existing pH 3.0–4.0 instruction belongs only to the trace stock. It must
    not override main pH 7.0–7.2."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "preparation_steps[3].description", "stored_value": "Adjust pH to
    3.0-4.0 with HCl.", "decision": "correct", "rationale": "The existing pH 3.0–4.0
    instruction belongs only to the trace stock. It must not override main pH 7.0–7.2."}]},
    {"quantity_id": "q31", "topic": "Existing preparation step 5", "source": {"evidence_id":
    "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path":
    "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[1].steps[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"step\": \"Autoclave at 121 \\u00b0C for
    15 min.\"\n                    }", "quote_basis": "Literal raw JSON substring,
    independently decoded to the located object"}, "decision": "correct", "rationale":
    "The existing 121 °C/15 min cycle is explicitly present in the current provider
    trace-stock steps. The primary PDF does not specify this trace cycle; preserve
    provider attribution and do not transfer it to the main buffer.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "preparation_steps[4].description",
    "stored_value": "Autoclave at 121 °C for 15 min.", "decision": "correct", "rationale":
    "The existing 121 °C/15 min cycle is explicitly present in the current provider
    trace-stock steps. The primary PDF does not specify this trace cycle; preserve
    provider attribution and do not transfer it to the main buffer."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "preparation_steps[4].description", "stored_value": "Autoclave at
    121 °C for 15 min.", "decision": "correct", "rationale": "The existing 121 °C/15
    min cycle is explicitly present in the current provider trace-stock steps. The
    primary PDF does not specify this trace cycle; preserve provider attribution and
    do not transfer it to the main buffer."}]}, {"quantity_id": "q32", "topic": "Existing
    preparation step 6", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[1].steps[2]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"step\": \"Note: autoclave in closed bottles\"\n                    }",
    "quote_basis": "Literal raw JSON substring, independently decoded to the located
    object"}, "decision": "correct", "rationale": "Closed-bottle autoclaving is a
    current provider trace-stock instruction, not a universal medium condition.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "preparation_steps[5].description", "stored_value": "Note: autoclave
    in closed bottles", "decision": "correct", "rationale": "Closed-bottle autoclaving
    is a current provider trace-stock instruction, not a universal medium condition."},
    {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path":
    "preparation_steps[5].description", "stored_value": "Note: autoclave in closed
    bottles", "decision": "correct", "rationale": "Closed-bottle autoclaving is a
    current provider trace-stock instruction, not a universal medium condition."}]},
    {"quantity_id": "q33", "topic": "Existing preparation step 7", "source": {"evidence_id":
    "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path":
    "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[2].steps[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"step\": \"Sterilize at 121\\u00b0C for
    20 minutes in 1L Schott bottle\"\n                    }", "quote_basis": "Literal
    raw JSON substring, independently decoded to the located object"}, "decision":
    "correct", "rationale": "The existing 121 °C/20 min and 1 L Schott bottle instruction
    belongs to the K-P buffer. Both primary and provider support it.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "preparation_steps[6].description",
    "stored_value": "Sterilize at 121°C for 20 minutes in 1L Schott bottle", "decision":
    "correct", "rationale": "The existing 121 °C/20 min and 1 L Schott bottle instruction
    belongs to the K-P buffer. Both primary and provider support it."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "preparation_steps[6].description", "stored_value": "Sterilize at
    121°C for 20 minutes in 1L Schott bottle", "decision": "correct", "rationale":
    "The existing 121 °C/20 min and 1 L Schott bottle instruction belongs to the K-P
    buffer. Both primary and provider support it."}]}, {"quantity_id": "q34", "topic":
    "Existing preparation step 8", "source": {"evidence_id": "api1615", "reference":
    "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin",
    "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[3].steps[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"step\": \"Sterilize by filtration.\"\n                    }",
    "quote_basis": "Literal raw JSON substring, independently decoded to the located
    object"}, "decision": "correct", "rationale": "Existing filtration belongs to
    the vitamin solutions. Do not extend it to every ingredient or invent a pore size.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "preparation_steps[7].description", "stored_value": "Sterilize by
    filtration.", "decision": "correct", "rationale": "Existing filtration belongs
    to the vitamin solutions. Do not extend it to every ingredient or invent a pore
    size."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "preparation_steps[7].description", "stored_value": "Sterilize by
    filtration.", "decision": "correct", "rationale": "Existing filtration belongs
    to the vitamin solutions. Do not extend it to every ingredient or invent a pore
    size."}, {"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path":
    "preparation_steps[7].action", "stored_value": "MIX", "decision": "correct", "rationale":
    "The literal instruction is filtration, but the existing action is MIX. Use a
    filtration action within the vitamin-stock scope while retaining the source text."},
    {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path":
    "preparation_steps[7].action", "stored_value": "MIX", "decision": "correct", "rationale":
    "The literal instruction is filtration, but the existing action is MIX. Use a
    filtration action within the vitamin-stock scope while retaining the source text."}]},
    {"quantity_id": "q35", "topic": "Existing preparation step 9", "source": {"evidence_id":
    "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path":
    "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[3].steps[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"step\": \"Mix the four solutions in the
    ratio 1:1:1:1.\"\n                    }", "quote_basis": "Literal raw JSON substring,
    independently decoded to the located object"}, "decision": "correct", "rationale":
    "Existing 1:1:1:1 mixing is supported for the four vitamin stocks; the receiving
    dose still conflicts between the primary main list and footer.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "preparation_steps[8].description",
    "stored_value": "Mix the four solutions in the ratio 1:1:1:1.", "decision": "correct",
    "rationale": "Existing 1:1:1:1 mixing is supported for the four vitamin stocks;
    the receiving dose still conflicts between the primary main list and footer."},
    {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path":
    "preparation_steps[8].description", "stored_value": "Mix the four solutions in
    the ratio 1:1:1:1.", "decision": "correct", "rationale": "Existing 1:1:1:1 mixing
    is supported for the four vitamin stocks; the receiving dose still conflicts between
    the primary main list and footer."}]}, {"quantity_id": "q36", "topic": "Existing
    main pH range", "source": {"evidence_id": "dsm1615", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1615.pdf",
    "raw_path": "REVIEW_WORK/batch055/source01-03/dsm1615.bin", "raw_sha256": "67c48c0397fbb5add36f04d2995f30ca93ba57daac554c5603cca65fddb1ce05",
    "locator": "Page1 K-P buffer", "accessed_at": "2026-10-28T04:32:46.058756+00:00",
    "quote": "pH 7.0-7.2"}, "decision": "evidence_only", "rationale": "The acidic
    stock pH values must not replace this main pH range.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "ph_range",
    "stored_value": {"min": 7.0, "max": 7.2}, "decision": "evidence_only", "rationale":
    "Retain the explicitly supported main/buffer pH range, distinct from trace and
    acidic-vitamin pH."}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "ph_range", "stored_value": {"min": 7.0, "max": 7.2}, "decision":
    "evidence_only", "rationale": "Retain the explicitly supported main/buffer pH
    range, distinct from trace and acidic-vitamin pH."}]}, {"quantity_id": "q37",
    "topic": "Source-only Main sol. 1615: 20 mM K-P-Buffer", "source": {"evidence_id":
    "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path":
    "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\":
    \"20 mM K-P-Buffer\",\n                        \"solution_id\": 5756,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "add", "rationale": "Add this explicit
    stock-addition edge to the missing solution topology. Preserve its exact source
    solution identity, dose and provider main-volume basis. The vitamin 0.5 mL dose
    is one side of the primary conflict, not a resolved universal dose.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "Add this explicit stock-addition
    edge to the missing solution topology. Preserve its exact source solution identity,
    dose and provider main-volume basis. The vitamin 0.5 mL dose is one side of the
    primary conflict, not a resolved universal dose.", "missing": true}, {"path":
    "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "Add this explicit stock-addition
    edge to the missing solution topology. Preserve its exact source solution identity,
    dose and provider main-volume basis. The vitamin 0.5 mL dose is one side of the
    primary conflict, not a resolved universal dose.", "missing": true}]}, {"quantity_id":
    "q38", "topic": "Source-only Main sol. 1615: Trace element solution", "source":
    {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\":
    \"Trace element solution\",\n                        \"solution_id\": 3027,\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "add", "rationale": "Add this explicit
    stock-addition edge to the missing solution topology. Preserve its exact source
    solution identity, dose and provider main-volume basis. The vitamin 0.5 mL dose
    is one side of the primary conflict, not a resolved universal dose.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "Add this explicit stock-addition
    edge to the missing solution topology. Preserve its exact source solution identity,
    dose and provider main-volume basis. The vitamin 0.5 mL dose is one side of the
    primary conflict, not a resolved universal dose.", "missing": true}, {"path":
    "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "Add this explicit stock-addition
    edge to the missing solution topology. Preserve its exact source solution identity,
    dose and provider main-volume basis. The vitamin 0.5 mL dose is one side of the
    primary conflict, not a resolved universal dose.", "missing": true}]}, {"quantity_id":
    "q39", "topic": "Source-only Main sol. 1615: Vitamine mixture", "source": {"evidence_id":
    "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path":
    "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\":
    \"Vitamine mixture\",\n                        \"solution_id\": 5757,\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "add", "rationale": "Add this explicit
    stock-addition edge to the missing solution topology. Preserve its exact source
    solution identity, dose and provider main-volume basis. The vitamin 0.5 mL dose
    is one side of the primary conflict, not a resolved universal dose.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "Add this explicit stock-addition
    edge to the missing solution topology. Preserve its exact source solution identity,
    dose and provider main-volume basis. The vitamin 0.5 mL dose is one side of the
    primary conflict, not a resolved universal dose.", "missing": true}, {"path":
    "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "Add this explicit stock-addition
    edge to the missing solution topology. Preserve its exact source solution identity,
    dose and provider main-volume basis. The vitamin 0.5 mL dose is one side of the
    primary conflict, not a resolved universal dose.", "missing": true}]}, {"quantity_id":
    "q40", "topic": "Source-only Trace element solution: Distilled water", "source":
    {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[1].recipe[9]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "add", "rationale": "Retain 1000
    mL distilled water as the listed trace-stock solvent. The provider separately
    declares a 1000 mL stock volume; do not describe the primary solvent listing as
    an explicit final-makeup instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain 1000 mL distilled water as the listed trace-stock solvent. The provider
    separately declares a 1000 mL stock volume; do not describe the primary solvent
    listing as an explicit final-makeup instruction.", "missing": true}, {"path":
    "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "Retain 1000 mL distilled
    water as the listed trace-stock solvent. The provider separately declares a 1000
    mL stock volume; do not describe the primary solvent listing as an explicit final-makeup
    instruction.", "missing": true}]}, {"quantity_id": "q41", "topic": "Source-only
    20 mM K-P-Buffer: Distilled water", "source": {"evidence_id": "api1615", "reference":
    "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin",
    "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[2].recipe[2]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    800,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "add", "rationale": "Retain 800 mL
    distilled water in the buffer alongside the two 0.1 M phosphate stock volumes.
    This is separate from subsequent medium additions.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "Retain 800 mL distilled
    water in the buffer alongside the two 0.1 M phosphate stock volumes. This is separate
    from subsequent medium additions.", "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain 800 mL distilled water in the buffer alongside the two 0.1 M phosphate
    stock volumes. This is separate from subsequent medium additions.", "missing":
    true}]}, {"quantity_id": "q42", "topic": "Source-only Vitamine mixture: Acidic
    thiamine / Ca pantothenate solution", "source": {"evidence_id": "api1615", "reference":
    "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin",
    "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[3].recipe[0]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\":
    \"Acidic thiamine / Ca pantothenate solution\",\n                        \"solution_id\":
    5758,\n                        \"amount\": 100,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis":
    "Literal raw JSON substring, independently decoded to the located object"}, "decision":
    "add", "rationale": "Retain the provider 100 mL contribution of this named vitamin
    stock to its declared 400 mL mixture; the primary independently specifies the
    equal-volume 1:1:1:1 ratio.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain the provider 100 mL contribution of this named vitamin stock to its declared
    400 mL mixture; the primary independently specifies the equal-volume 1:1:1:1 ratio.",
    "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain the provider 100 mL contribution of this named vitamin stock to its declared
    400 mL mixture; the primary independently specifies the equal-volume 1:1:1:1 ratio.",
    "missing": true}]}, {"quantity_id": "q43", "topic": "Source-only Vitamine mixture:
    Basic vitamin solution", "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[3].recipe[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\":
    \"Basic vitamin solution\",\n                        \"solution_id\": 5759,\n                        \"amount\":
    100,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "add", "rationale": "Retain the provider
    100 mL contribution of this named vitamin stock to its declared 400 mL mixture;
    the primary independently specifies the equal-volume 1:1:1:1 ratio.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "Retain the provider 100
    mL contribution of this named vitamin stock to its declared 400 mL mixture; the
    primary independently specifies the equal-volume 1:1:1:1 ratio.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "Retain the
    provider 100 mL contribution of this named vitamin stock to its declared 400 mL
    mixture; the primary independently specifies the equal-volume 1:1:1:1 ratio.",
    "missing": true}]}, {"quantity_id": "q44", "topic": "Source-only Vitamine mixture:
    Neutral folic acid / riboflavin solution", "source": {"evidence_id": "api1615",
    "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin",
    "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[3].recipe[2]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\":
    \"Neutral folic acid / riboflavin solution\",\n                        \"solution_id\":
    5760,\n                        \"amount\": 100,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis":
    "Literal raw JSON substring, independently decoded to the located object"}, "decision":
    "add", "rationale": "Retain the provider 100 mL contribution of this named vitamin
    stock to its declared 400 mL mixture; the primary independently specifies the
    equal-volume 1:1:1:1 ratio.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain the provider 100 mL contribution of this named vitamin stock to its declared
    400 mL mixture; the primary independently specifies the equal-volume 1:1:1:1 ratio.",
    "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain the provider 100 mL contribution of this named vitamin stock to its declared
    400 mL mixture; the primary independently specifies the equal-volume 1:1:1:1 ratio.",
    "missing": true}]}, {"quantity_id": "q45", "topic": "Source-only Vitamine mixture:
    Neutral B12 solution 0.005 g/L", "source": {"evidence_id": "api1615", "reference":
    "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin",
    "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[3].recipe[3]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\":
    \"Neutral B12 solution 0.005 g/L\",\n                        \"solution_id\":
    5761,\n                        \"amount\": 100,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis":
    "Literal raw JSON substring, independently decoded to the located object"}, "decision":
    "add", "rationale": "Retain the provider 100 mL contribution of this named vitamin
    stock to its declared 400 mL mixture; the primary independently specifies the
    equal-volume 1:1:1:1 ratio.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain the provider 100 mL contribution of this named vitamin stock to its declared
    400 mL mixture; the primary independently specifies the equal-volume 1:1:1:1 ratio.",
    "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain the provider 100 mL contribution of this named vitamin stock to its declared
    400 mL mixture; the primary independently specifies the equal-volume 1:1:1:1 ratio.",
    "missing": true}]}, {"quantity_id": "q46", "topic": "Source-only Acidic thiamine
    / Ca pantothenate solution: Distilled water", "source": {"evidence_id": "api1615",
    "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin",
    "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[4].recipe[2]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"attribute\":
    \"acidified to pH 3.0 with HCl\",\n                        \"amount\": 100,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis":
    "Literal raw JSON substring, independently decoded to the located object"}, "decision":
    "add", "rationale": "Retain 100 mL water acidified to pH 3 with HCl for this vitamin
    stock. HCl concentration and amount are not given; do not invent them or treat
    this as main-medium pH.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain 100 mL water acidified to pH 3 with HCl for this vitamin stock. HCl concentration
    and amount are not given; do not invent them or treat this as main-medium pH.",
    "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain 100 mL water acidified to pH 3 with HCl for this vitamin stock. HCl concentration
    and amount are not given; do not invent them or treat this as main-medium pH.",
    "missing": true}]}, {"quantity_id": "q47", "topic": "Source-only Neutral folic
    acid / riboflavin solution: Distilled water", "source": {"evidence_id": "api1615",
    "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin",
    "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[6].recipe[2]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    100,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "add", "rationale": "Retain this
    100 mL water input in its specific vitamin stock. The provider stock volume is
    explicit, whereas the primary describes solvent input; no receiving-medium amount
    is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain this 100 mL water input in its specific vitamin stock. The provider stock
    volume is explicit, whereas the primary describes solvent input; no receiving-medium
    amount is inferred.", "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain this 100 mL water input in its specific vitamin stock. The provider stock
    volume is explicit, whereas the primary describes solvent input; no receiving-medium
    amount is inferred.", "missing": true}]}, {"quantity_id": "q48", "topic": "Source-only
    Neutral B12 solution 0.005 g/L: Distilled water", "source": {"evidence_id": "api1615",
    "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin",
    "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[7].recipe[1]", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    100,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_basis": "Literal raw JSON substring, independently
    decoded to the located object"}, "decision": "add", "rationale": "Retain this
    100 mL water input in its specific vitamin stock. The provider stock volume is
    explicit, whereas the primary describes solvent input; no receiving-medium amount
    is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain this 100 mL water input in its specific vitamin stock. The provider stock
    volume is explicit, whereas the primary describes solvent input; no receiving-medium
    amount is inferred.", "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain this 100 mL water input in its specific vitamin stock. The provider stock
    volume is explicit, whereas the primary describes solvent input; no receiving-medium
    amount is inferred.", "missing": true}]}, {"quantity_id": "q49", "topic": "Provider
    solution basis: Main sol. 1615", "source": {"evidence_id": "api1615", "reference":
    "https://mediadive.dsmz.de/rest/medium/1615", "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin",
    "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[0].volume", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "\"volume\": 1000"}, "decision": "evidence_only", "rationale": "Preserve
    the provider-declared volume at this exact solution object. It is not a license
    to sum or transfer rates between buffer, trace stock, individual vitamin stocks,
    mixture and finished medium.", "layer_assessments": []}, {"quantity_id": "q50",
    "topic": "Provider solution basis: Trace element solution", "source": {"evidence_id":
    "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path":
    "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[1].volume", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "\"volume\": 1000"}, "decision": "evidence_only", "rationale": "Preserve
    the provider-declared volume at this exact solution object. It is not a license
    to sum or transfer rates between buffer, trace stock, individual vitamin stocks,
    mixture and finished medium.", "layer_assessments": []}, {"quantity_id": "q51",
    "topic": "Provider solution basis: 20 mM K-P-Buffer", "source": {"evidence_id":
    "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path":
    "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[2].volume", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "\"volume\": 1000"}, "decision": "evidence_only", "rationale": "Preserve
    the provider-declared volume at this exact solution object. It is not a license
    to sum or transfer rates between buffer, trace stock, individual vitamin stocks,
    mixture and finished medium.", "layer_assessments": []}, {"quantity_id": "q52",
    "topic": "Provider solution basis: Vitamine mixture", "source": {"evidence_id":
    "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path":
    "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[3].volume", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "\"volume\": 400"}, "decision": "evidence_only", "rationale": "Preserve
    the provider-declared volume at this exact solution object. It is not a license
    to sum or transfer rates between buffer, trace stock, individual vitamin stocks,
    mixture and finished medium.", "layer_assessments": []}, {"quantity_id": "q53",
    "topic": "Provider solution basis: Acidic thiamine / Ca pantothenate solution",
    "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[4].volume", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "\"volume\": 100"}, "decision": "evidence_only", "rationale": "Preserve
    the provider-declared volume at this exact solution object. It is not a license
    to sum or transfer rates between buffer, trace stock, individual vitamin stocks,
    mixture and finished medium.", "layer_assessments": []}, {"quantity_id": "q54",
    "topic": "Provider solution basis: Basic vitamin solution", "source": {"evidence_id":
    "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615", "raw_path":
    "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[5].volume", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "\"volume\": 100"}, "decision": "evidence_only", "rationale": "Preserve
    the provider-declared volume at this exact solution object. It is not a license
    to sum or transfer rates between buffer, trace stock, individual vitamin stocks,
    mixture and finished medium.", "layer_assessments": []}, {"quantity_id": "q55",
    "topic": "Provider solution basis: Neutral folic acid / riboflavin solution",
    "source": {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[6].volume", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "\"volume\": 100"}, "decision": "evidence_only", "rationale": "Preserve
    the provider-declared volume at this exact solution object. It is not a license
    to sum or transfer rates between buffer, trace stock, individual vitamin stocks,
    mixture and finished medium.", "layer_assessments": []}, {"quantity_id": "q56",
    "topic": "Provider solution basis: Neutral B12 solution 0.005 g/L", "source":
    {"evidence_id": "api1615", "reference": "https://mediadive.dsmz.de/rest/medium/1615",
    "raw_path": "REVIEW_WORK/batch055/source01-03/api1615.bin", "raw_sha256": "8f75e9abb72f739e2fd308b46901015968b4399fd3c96e4c706b1c4ca842da29",
    "locator": "$.data.solutions[7].volume", "accessed_at": "2026-10-28T04:32:45.964892+00:00",
    "quote": "\"volume\": 100"}, "decision": "evidence_only", "rationale": "Preserve
    the provider-declared volume at this exact solution object. It is not a license
    to sum or transfer rates between buffer, trace stock, individual vitamin stocks,
    mixture and finished medium.", "layer_assessments": []}, {"quantity_id": "q57",
    "topic": "Conflicting vitamin mixture addition doses", "source": [{"evidence_id":
    "dsm1615", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1615.pdf",
    "raw_path": "REVIEW_WORK/batch055/source01-03/dsm1615.bin", "raw_sha256": "67c48c0397fbb5add36f04d2995f30ca93ba57daac554c5603cca65fddb1ce05",
    "locator": "Page1 post-sterilization additions", "accessed_at": "2026-10-28T04:32:46.058756+00:00",
    "quote": "0.5 ml/l Vitamins"}, {"evidence_id": "dsm1615", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1615.pdf",
    "raw_path": "REVIEW_WORK/batch055/source01-03/dsm1615.bin", "raw_sha256": "67c48c0397fbb5add36f04d2995f30ca93ba57daac554c5603cca65fddb1ce05",
    "locator": "Page2 final vitamin instruction", "accessed_at": "2026-10-28T04:32:46.058756+00:00",
    "quote": "Mix the four solutions in the ratio1:1:1:1 and 1.0 ml/L or separately
    add 250 µl/L. of\neach solution."}], "decision": "unsupported", "rationale": "The
    primary main recipe gives 0.5 mL/L, but the footer gives 1 mL/L mixed stock or
    250 µL/L of each. The current provider follows 0.5 mL in its main object. Do not
    select a convenient version or silently average the doses.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "Represent both source-located
    dose statements as an unresolved conflict, not interchangeable resolved values.",
    "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Represent both source-located dose statements as an unresolved conflict, not
    interchangeable resolved values.", "missing": true}]}, {"quantity_id": "q58",
    "topic": "Main stock strengths and methionine processing", "source": {"evidence_id":
    "dsm1615", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1615.pdf",
    "raw_path": "REVIEW_WORK/batch055/source01-03/dsm1615.bin", "raw_sha256": "67c48c0397fbb5add36f04d2995f30ca93ba57daac554c5603cca65fddb1ce05",
    "locator": "Page1 complete post-sterilization list", "accessed_at": "2026-10-28T04:32:46.058756+00:00",
    "quote": "1.0 ml/l 50 mM L-methionine, filter sterilized, neutralised (50 µM)."},
    "decision": "add", "rationale": "All primary stock strengths and parenthetical
    receiving-molarity statements are recorded distinctly from source solution volumes
    and provider g_l. Neutralisation details and bare percentage basis remain unknown.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Basic_mineral_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Preserve 1 M magnesium and acetate, 5% calcium of unspecified basis, 2 M sodium
    aspartate and 50 mM methionine stocks with their stated addition volumes. Methionine
    is filter sterilized and neutralised; no pore size or neutralizer amount is stated.",
    "missing": true}, {"path": "data/normalized_yaml/bacterial/basic_mineral_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Preserve 1 M magnesium and acetate, 5% calcium of unspecified basis, 2 M sodium
    aspartate and 50 mM methionine stocks with their stated addition volumes. Methionine
    is filter sterilized and neutralised; no pore size or neutralizer amount is stated.",
    "missing": true}]}]'
- assessment_id: a4
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: supported
  summary: The grounding inventory enumerates every asserted identifier and exact
    preferred label. Exact identifier rows and ontology-linked rows are recorded separately,
    including mapping_status. Present catalog membership does not validate supplied
    hydrate form or historical identity; specific limits are assessed separately.
  target_ids:
  - CultureMech:001096
  evidence_ids:
  - grounding
- assessment_id: a5
  area: provenance
  topic: History and evidence scope
  outcome: supported
  summary: Complete owner and target histories were read. Current source bytes and
    inspected code are independent evidence; historical timestamps remain historical
    claims unless an exact cited raw digest is recovered.
  target_ids:
  - CultureMech:001096
  evidence_ids:
  - history
  - scalars
- assessment_id: a6
  area: scope
  topic: Growth and taxonomic evidence
  outcome: unknown
  summary: Generic cultivation applications and bacterial filing are not strain-level
    growth evidence. No organism-specific growth, temperature or atmosphere is inferred
    from names or source catalog identifiers.
  target_ids:
  - CultureMech:001096
  evidence_ids:
  - local-target
- assessment_id: a7
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:001096
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-001096-trace-and-vitamin-stocks-are-flattened-into-direct-ingredients
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Trace and vitamin stocks are flattened into direct ingredients
  description: The local ingredients include nine trace-stock g/L values and individual
    vitamin-stock strengths as if they were direct medium concentrations. Source buffer,
    trace stock, four vitamin stocks and mixed vitamin assembly are absent as solution
    topology. Current importer stock-separation safeguards already exist.
  target_ids:
  - CultureMech:001096
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - dsm1615
  - api1615
  - provider-stage-census
  - writer-mediadive
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basic_mineral_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-001096-basic-vitamin-solvent-volume-is-stored-as-a-mass-rate
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Basic-vitamin solvent volume is stored as a mass rate
  description: ingredients[22] is 100 G_PER_L NaOH, while both exact sources specify
    100 mL of 0.1 N NaOH as the basic vitamin stock solvent. The local number preserves
    a volume magnitude with an unsupported mass dimension.
  target_ids:
  - CultureMech:001096
  field_paths:
  - ingredients[22].concentration
  evidence_ids:
  - dsm1615
  - api1615
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basic_mineral_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-001096-primary-vitamin-addition-doses-conflict
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Primary vitamin addition doses conflict
  description: The primary main list says 0.5 mL/L vitamins; its footer says 1 mL/L
    mixed solution or 250 µL/L of each stock. Current API follows the first value.
    Stock restoration must retain this source-internal conflict instead of choosing
    or averaging one dose.
  target_ids:
  - CultureMech:001096
  field_paths:
  - solutions
  - preparation_steps[8].description
  evidence_ids:
  - dsm1615
  - api1615
  - pdf-visual-1
  - pdf-visual-2
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basic_mineral_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f4
  issue_key: culturemech-001096-existing-preparation-loses-stock-specific-conditions
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Existing preparation loses stock-specific conditions
  description: Trace pH 3–4, provider trace autoclaving at 121 °C for 15 min, buffer
    autoclaving at 121 °C for 20 min in a 1 L bottle, and vitamin filtration/mixing
    appear in one unscoped top-level sequence. The existing prose is supported in
    those distinct objects and should be preserved with correct ownership. The vitamin
    filtration description is additionally classified as MIX and needs a filtration
    action.
  target_ids:
  - CultureMech:001096
  field_paths:
  - preparation_steps[3].description
  - preparation_steps[4].description
  - preparation_steps[5].description
  - preparation_steps[6].description
  - preparation_steps[7].description
  - preparation_steps[8].description
  - preparation_steps[7].action
  evidence_ids:
  - dsm1615
  - api1615
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basic_mineral_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f5
  issue_key: culturemech-001096-nickel-chloride-hexahydrate-is-grounded-without-its-waters
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel chloride hexahydrate is grounded without its waters
  description: The source and preferred name specify NiCl2 x 6 H2O, but primary and
    secondary CHEBI:34887 identify nickel dichloride with formula Cl2Ni. Current MIM
    ontology-linked hydrate rows do not validate an exact six-water form.
  target_ids:
  - CultureMech:001096
  field_paths:
  - ingredients[12].term
  - ingredients[12].mediaingredientmech_chebi_term
  evidence_ids:
  - dsm1615
  - chebi34887
  - grounding
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basic_mineral_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f6
  issue_key: culturemech-001096-legacy-thiamine-linkage-has-no-current-catalog-row
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Legacy thiamine linkage has no current catalog row
  description: MediaIngredientMech:000898 is absent from the complete current packaged
    label index. CHEBI:18385 remains a verified thiamine(1+) object, but current catalog
    absence does not establish historical invalidity or specify a thiamine salt.
  target_ids:
  - CultureMech:001096
  field_paths:
  - ingredients[16].mediaingredientmech_term
  evidence_ids:
  - grounding
  - chebi18385
  rule_id: source-stage-or-identity
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basic_mineral_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Curate the maintained owner with explicit stock composition, solvent,
    preparation and addition edges. Preserve main-provider rate correspondence and
    buffer-stage rates with their basis; regenerate only after the stock/medium boundary
    is explicit.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001096
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basic_mineral_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Replace the unsupported mass-rate representation with the explicitly
    sourced liquid solvent volume and normality in its vitamin stock. Do not invent
    a final-medium NaOH dose.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001096
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basic_mineral_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Attach both precise primary locations and the provider version, then
    resolve or explicitly qualify the dose conflict before calculating any final vitamin
    rates.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001096
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basic_mineral_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action4
  description: Move or qualify each existing instruction under its exact stock/buffer
    object. Keep main pH 7.0–7.2 and post-sterilization additions distinct; attribute
    trace 15-min autoclaving to the current provider only.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001096
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basic_mineral_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action5
  description: Reconcile the exact supplied hexahydrate with an independently verified
    suitable ontology representation. Preserve the source hydrate and stock mass;
    do not convert using the anhydrous formula or guess an identifier.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:001096
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basic_mineral_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action6
  description: Record the legacy/current linkage distinction and reconcile it through
    the current catalog without inventing a historical conclusion or source salt.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:001096
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/basic_mineral_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- The primary PDF contains an unresolved 0.5 versus 1 mL/L vitamin-dose conflict;
  no final vitamin rates are calculated.
- Listed water input is not automatically a measured final-volume declaration. Current
  API g_l and solution volumes are direct provider evidence at their named stages,
  not independent proof of all primary arithmetic.
- Calcium 5% lacks an explicit basis in the primary. Na-aspartate, B12, EDTA ionic
  form and thiamine salt are not made more specific by guesswork.
- Historical reports and their decoded snippets remain derivative artifacts; current
  captured primary/API bytes are the scientific basis here. Existing current importer
  and cleanup guards are credited, without reconstructing historical execution.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
