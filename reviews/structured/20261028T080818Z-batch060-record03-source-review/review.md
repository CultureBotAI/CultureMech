# Castenholz Medium: preserve base evidence and keep unresolved variants separate

- Review: 20261028T080818Z-batch060-record03-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T07:46:08.330450Z
- Finished UTC: 2026-10-28T08:08:18.758048Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

All16 base concentrations match explicit current provider rates and the primary batch table. Thirty attached base-owner quantity claims are authenticated by exact current response bytes. The generated merge loses these claims and the DSM preparation, while two named strain-modified wrappers remain unverified and must not inherit base formulation authority. Legacy nitrate links and malformed historical timestamps also need bounded, append-only follow-up.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch060 native selection index 03.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006701 | data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml | generated | castenholz_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006701 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:006701 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:006701 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:006701 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Base lineage and unresolved wrappers

identity: concern. Targets: CultureMech:006701.

Exact generated merged_from resolves four maintained contributors. DSM86 and base KOMODO86 linkage are historical identity claims with current base formulation support; the named11376/11377 wrappers have copied formulas and distinct source IDs. SOURCE_DUPLICATE annotations and equal ingredient signatures do not establish their exact recipes.

### Credit maintained base evidence and process

completeness: concern. Targets: CultureMech:006701.

Two base owners retain30 exact attached quantity claims; the DSM owner retains the pH-adjustment instruction. The generated record omits these. Current formulation compatibility compares scientific metadata and preparation and would reject these differing assertions rather than establish equivalence from the ingredient signature.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:006701.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "Nitrilotriacetic acid", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86", "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T07:48:19.868996Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"attribute\": \"Titriplex I\",\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.523177,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Nitrilotriacetic acid", "compound_id": 189, "attribute": "Titriplex I", "amount": 100, "unit": "mg", "g_l": 0.1, "mmol_l": 0.523177, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Base-provider amount support, already attached evidence, missing generated linkage and unverified named variants are separate layer-specific decisions. All source supplied forms and units are retained.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API explicitly declares this base main g_l and the primary PDF supports the corresponding batch amount and supplied form. Add exact linkage without calling the water input a measured final volume. The primary identifies nitrilotriacetic acid (Titriplex I) and100 mg; this is a source product annotation, not an optional stock-strength instruction. The previous generic attribute flag does not by itself invalidate the explicit base amount."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API explicitly declares this base main g_l and the primary PDF supports the corresponding batch amount and supplied form. Add exact linkage without calling the water input a measured final volume. The primary identifies nitrilotriacetic acid (Titriplex I) and100 mg; this is a source product annotation, not an optional stock-strength instruction. The previous generic attribute flag does not by itself invalidate the explicit base amount."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API explicitly declares this base main g_l and the primary PDF supports the corresponding batch amount and supplied form. Add exact linkage without calling the water input a measured final volume. The primary identifies nitrilotriacetic acid (Titriplex I) and100 mg; this is a source product annotation, not an optional stock-strength instruction. The previous generic attribute flag does not by itself invalidate the explicit base amount."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe. The primary identifies nitrilotriacetic acid (Titriplex I) and100 mg; this is a source product annotation, not an optional stock-strength instruction. The previous generic attribute flag does not by itself invalidate the explicit base amount."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe. The primary identifies nitrilotriacetic acid (Titriplex I) and100 mg; this is a source product annotation, not an optional stock-strength instruction. The previous generic attribute flag does not by itself invalidate the explicit base amount."}]}, {"quantity_id": "q2", "topic": "CaSO4 x 2 H2O", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86", "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T07:48:19.868996Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"CaSO4 x 2 H2O\",\n                        \"compound_id\": 190,\n                        \"amount\": 60,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.06,\n                        \"mmol_l\": 0.348489,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "CaSO4 x 2 H2O", "compound_id": 190, "amount": 60, "unit": "mg", "g_l": 0.06, "mmol_l": 0.348489, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Base-provider amount support, already attached evidence, missing generated linkage and unverified named variants are separate layer-specific decisions. All source supplied forms and units are retained.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.06", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API explicitly declares this base main g_l and the primary PDF supports the corresponding batch amount and supplied form. Add exact linkage without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.06", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.06", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.06", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.06", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}]}, {"quantity_id": "q3", "topic": "MgSO4 x 7 H2O", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86", "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T07:48:19.868996Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.405719,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "MgSO4 x 7 H2O", "compound_id": 8, "amount": 100, "unit": "mg", "g_l": 0.1, "mmol_l": 0.405719, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Base-provider amount support, already attached evidence, missing generated linkage and unverified named variants are separate layer-specific decisions. All source supplied forms and units are retained.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API explicitly declares this base main g_l and the primary PDF supports the corresponding batch amount and supplied form. Add exact linkage without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}]}, {"quantity_id": "q4", "topic": "NaCl", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86", "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T07:48:19.868996Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 8,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.008,\n                        \"mmol_l\": 0.136893,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "NaCl", "compound_id": 43, "amount": 8, "unit": "mg", "g_l": 0.008, "mmol_l": 0.136893, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Base-provider amount support, already attached evidence, missing generated linkage and unverified named variants are separate layer-specific decisions. All source supplied forms and units are retained.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.008", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API explicitly declares this base main g_l and the primary PDF supports the corresponding batch amount and supplied form. Add exact linkage without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.008", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.008", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.008", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.008", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}]}, {"quantity_id": "q5", "topic": "KNO3", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86", "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T07:48:19.868996Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KNO3\",\n                        \"compound_id\": 191,\n                        \"amount\": 103,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.103,\n                        \"mmol_l\": 1.01876,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "KNO3", "compound_id": 191, "amount": 103, "unit": "mg", "g_l": 0.103, "mmol_l": 1.01876, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Base-provider amount support, already attached evidence, missing generated linkage and unverified named variants are separate layer-specific decisions. All source supplied forms and units are retained.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.103", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API explicitly declares this base main g_l and the primary PDF supports the corresponding batch amount and supplied form. Add exact linkage without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.103", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.103", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.103", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.103", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}]}, {"quantity_id": "q6", "topic": "NaNO3", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86", "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539", "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T07:48:19.868996Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaNO3\",\n                        \"compound_id\": 187,\n                        \"amount\": 689,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.689,\n                        \"mmol_l\": 8.10636,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "NaNO3", "compound_id": 187, "amount": 689, "unit": "mg", "g_l": 0.689, "mmol_l": 8.10636, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Base-provider amount support, already attached evidence, missing generated linkage and unverified named variants are separate layer-specific decisions. All source supplied forms and units are retained.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.689", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API explicitly declares this base main g_l and the primary PDF supports the corresponding batch amount and supplied form. Add exact linkage without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.689", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.689", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.689", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.689", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}]}, {"quantity_id": "q7", "topic": "Na2HPO4 x 2 H2O", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86", "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539", "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T07:48:19.868996Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2HPO4 x 2 H2O\",\n                        \"compound_id\": 181,\n                        \"amount\": 140,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.14,\n                        \"mmol_l\": 0.9862,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "Na2HPO4 x 2 H2O", "compound_id": 181, "amount": 140, "unit": "mg", "g_l": 0.14, "mmol_l": 0.9862, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Base-provider amount support, already attached evidence, missing generated linkage and unverified named variants are separate layer-specific decisions. All source supplied forms and units are retained.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.14", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API explicitly declares this base main g_l and the primary PDF supports the corresponding batch amount and supplied form. Add exact linkage without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.14", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.14", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.14", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.14", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}]}, {"quantity_id": "q8", "topic": "FeCl3 x 6 H2O", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86", "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539", "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T07:48:19.868996Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"FeCl3 x 6 H2O\",\n                        \"compound_id\": 82,\n                        \"amount\": 0.47,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00047,\n                        \"mmol_l\": 0.00173883,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "FeCl3 x 6 H2O", "compound_id": 82, "amount": 0.47, "unit": "mg", "g_l": 0.00047, "mmol_l": 0.00173883, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Base-provider amount support, already attached evidence, missing generated linkage and unverified named variants are separate layer-specific decisions. All source supplied forms and units are retained.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00047", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API explicitly declares this base main g_l and the primary PDF supports the corresponding batch amount and supplied form. Add exact linkage without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00047", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00047", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00047", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00047", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}]}, {"quantity_id": "q9", "topic": "MnSO4 x H2O", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86", "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539", "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T07:48:19.868996Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 2.2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0022,\n                        \"mmol_l\": 0.0130165,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "MnSO4 x H2O", "compound_id": 14, "amount": 2.2, "unit": "mg", "g_l": 0.0022, "mmol_l": 0.0130165, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Base-provider amount support, already attached evidence, missing generated linkage and unverified named variants are separate layer-specific decisions. All source supplied forms and units are retained.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.0022", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API explicitly declares this base main g_l and the primary PDF supports the corresponding batch amount and supplied form. Add exact linkage without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.0022", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.0022", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.0022", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.0022", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}]}, {"quantity_id": "q10", "topic": "ZnSO4 x 7 H2O", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86", "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539", "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T07:48:19.868996Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0005,\n                        \"mmol_l\": 0.00173876,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "ZnSO4 x 7 H2O", "compound_id": 35, "amount": 0.5, "unit": "mg", "g_l": 0.0005, "mmol_l": 0.00173876, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Base-provider amount support, already attached evidence, missing generated linkage and unverified named variants are separate layer-specific decisions. All source supplied forms and units are retained.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API explicitly declares this base main g_l and the primary PDF supports the corresponding batch amount and supplied form. Add exact linkage without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}]}, {"quantity_id": "q11", "topic": "H3BO3", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86", "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539", "locator": "$.data.solutions[0].recipe[10]", "accessed_at": "2026-10-28T07:48:19.868996Z", "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0005,\n                        \"mmol_l\": 0.00808538,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound": "H3BO3", "compound_id": 37, "amount": 0.5, "unit": "mg", "g_l": 0.0005, "mmol_l": 0.00808538, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Base-provider amount support, already attached evidence, missing generated linkage and unverified named variants are separate layer-specific decisions. All source supplied forms and units are retained.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API explicitly declares this base main g_l and the primary PDF supports the corresponding batch amount and supplied form. Add exact linkage without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}]}, {"quantity_id": "q12", "topic": "CuSO4 x 5 H2O", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86", "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539", "locator": "$.data.solutions[0].recipe[11]", "accessed_at": "2026-10-28T07:48:19.868996Z", "quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 25,\n                        \"unit\": \"\\u00b5g\",\n                        \"g_l\": 2.5e-5,\n                        \"mmol_l\": 0.000100126,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 12, "compound": "CuSO4 x 5 H2O", "compound_id": 121, "amount": 25, "unit": "µg", "g_l": 2.5e-05, "mmol_l": 0.000100126, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Base-provider amount support, already attached evidence, missing generated linkage and unverified named variants are separate layer-specific decisions. All source supplied forms and units are retained.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "2.5e-05", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API explicitly declares this base main g_l and the primary PDF supports the corresponding batch amount and supplied form. Add exact linkage without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "2.5e-05", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "2.5e-05", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "2.5e-05", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "2.5e-05", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}]}, {"quantity_id": "q13", "topic": "Na2MoO4 x 2 H2O", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86", "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539", "locator": "$.data.solutions[0].recipe[12]", "accessed_at": "2026-10-28T07:48:19.868996Z", "quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 25,\n                        \"unit\": \"\\u00b5g\",\n                        \"g_l\": 2.5e-5,\n                        \"mmol_l\": 0.000103327,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 13, "compound": "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 25, "unit": "µg", "g_l": 2.5e-05, "mmol_l": 0.000103327, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Base-provider amount support, already attached evidence, missing generated linkage and unverified named variants are separate layer-specific decisions. All source supplied forms and units are retained.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "2.5e-05", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API explicitly declares this base main g_l and the primary PDF supports the corresponding batch amount and supplied form. Add exact linkage without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "2.5e-05", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "2.5e-05", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "2.5e-05", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "2.5e-05", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}]}, {"quantity_id": "q14", "topic": "CoCl2 x 6 H2O", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86", "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539", "locator": "$.data.solutions[0].recipe[13]", "accessed_at": "2026-10-28T07:48:19.868996Z", "quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 46,\n                        \"unit\": \"\\u00b5g\",\n                        \"g_l\": 4.6e-5,\n                        \"mmol_l\": 0.000354285,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 14, "compound": "CoCl2 x 6 H2O", "compound_id": 38, "amount": 46, "unit": "µg", "g_l": 4.6e-05, "mmol_l": 0.000354285, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Base-provider amount support, already attached evidence, missing generated linkage and unverified named variants are separate layer-specific decisions. All source supplied forms and units are retained.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "4.6e-05", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API explicitly declares this base main g_l and the primary PDF supports the corresponding batch amount and supplied form. Add exact linkage without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "4.6e-05", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "4.6e-05", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "4.6e-05", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "4.6e-05", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}]}, {"quantity_id": "q15", "topic": "Tryptone", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86", "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539", "locator": "$.data.solutions[0].recipe[14]", "accessed_at": "2026-10-28T07:48:19.868996Z", "quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Tryptone\",\n                        \"compound_id\": 71,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 14.0687,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 15, "compound": "Tryptone", "compound_id": 71, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 14.0687, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Base-provider amount support, already attached evidence, missing generated linkage and unverified named variants are separate layer-specific decisions. All source supplied forms and units are retained.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API explicitly declares this base main g_l and the primary PDF supports the corresponding batch amount and supplied form. Add exact linkage without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}]}, {"quantity_id": "q16", "topic": "Yeast extract", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86", "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539", "locator": "$.data.solutions[0].recipe[15]", "accessed_at": "2026-10-28T07:48:19.868996Z", "quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 16, "compound": "Yeast extract", "compound_id": 16, "amount": 1, "unit": "g", "g_l": 1, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Base-provider amount support, already attached evidence, missing generated linkage and unverified named variants are separate layer-specific decisions. All source supplied forms and units are retained.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API explicitly declares this base main g_l and the primary PDF supports the corresponding batch amount and supplied form. Add exact linkage without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached claim has the exact current API response digest, literal source object and matching locator. It explicitly supports this base provider-declared main g_l, with the final-volume limitation already retained; source mapping is identity-only and not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the base DSM86 provider rate, but this named strain-modified source lacks independent formulation evidence. Exact current variant endpoint403 and inherited copied ingredients do not authorize transferring the base recipe."}]}, {"quantity_id": "q17", "topic": "Base recipe water", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86", "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539", "locator": "$.data.solutions[0].recipe[16]", "accessed_at": "2026-10-28T07:48:19.868996Z", "quote": "{\n                        \"recipe_order\": 17,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 17, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "The source water row is omitted from the local formulation. Add the batch solvent context only for the authenticated base; no dose transfers to unknown variants.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "notes", "stored_value": "Source: KOMODO ModelSEED &#124; ID: 86 &#124; DSMZ Medium: 86 (mediadive.medium:86) &#124; Aerobic: No", "decision": "add", "rationale": "Retain the1000 ml batch-water amount in scoped base formulation context; it is not a G_PER_L ingredient, percent or measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path": "notes", "stored_value": "Source: KOMODO ModelSEED &#124; ID: 86 &#124; DSMZ Medium: 86 (mediadive.medium:86) &#124; Aerobic: No", "decision": "add", "rationale": "Retain the1000 ml batch-water amount in scoped base formulation context; it is not a G_PER_L ingredient, percent or measured final volume."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "notes", "stored_value": "Source: DSMZ &#124; Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium86.pdf", "decision": "add", "rationale": "Retain the1000 ml batch-water amount in scoped base formulation context; it is not a G_PER_L ingredient, percent or measured final volume."}]}, {"quantity_id": "q18", "topic": "Base pH adjustment preparation", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86", "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T07:48:19.868996Z", "quote": "{\n                        \"step\": \"Adjust pH to 8.2 with NaOH.\"\n                    }", "exact_decoded_object": {"step": "Adjust pH to 8.2 with NaOH."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Primary and provider specify adjustment to pH8.2 with NaOH, with no NaOH dose or stock strength. Restore lost base process without inventing a quantity or extending it to unverified variants.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "The base source pH-adjustment instruction is absent here; preserve the already existing DSM owner instruction when resolving the base record.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "The base source pH-adjustment instruction is absent here; preserve the already existing DSM owner instruction when resolving the base record.", "missing": true}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "preparation_steps[0]", "stored_value": {"step_number": 1, "action": "ADJUST_PH", "description": "Adjust pH to 8.2 with NaOH."}, "decision": "evidence_only", "rationale": "The maintained DSM owner already retains the exact pH-adjustment sentence; credit it and attach root source evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "unsupported", "rationale": "No variant-specific preparation was recovered; the absent field must not be filled from a presumed duplicate base.", "missing": true}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "unsupported", "rationale": "No variant-specific preparation was recovered; the absent field must not be filled from a presumed duplicate base.", "missing": true}]}, {"quantity_id": "q19", "topic": "Current pH fields", "source": [{"evidence_id": "dsm86", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium86.pdf", "raw_path": "REVIEW_WORK/batch060/source01-03/dsm86.bin", "raw_sha256": "19ce73dc1e0358ecde0115a6b796481e33a1b1b4186fddf13d232c5d463609bf", "locator": "Page1 preparation", "accessed_at": "2026-10-28T07:48:20.215885Z", "quote": "Adjust pH to 8.2 with NaOH."}], "decision": "mixed", "rationale": "All existing pH assertions are individually scoped; no strain optimum is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ph_value", "stored_value": 8.2, "decision": "evidence_only", "rationale": "Existing base pH8.2 is directly supported and retained."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path": "ph_value", "stored_value": 8.2, "decision": "evidence_only", "rationale": "Existing base pH8.2 is directly supported and retained."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "ph_value", "stored_value": 8.2, "decision": "evidence_only", "rationale": "Existing base pH8.2 is directly supported and retained."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml", "field_path": "ph_value", "stored_value": 8.2, "decision": "unsupported", "rationale": "Base pH8.2 is explicit; its equality in a named modified wrapper does not independently verify that variant."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path": "ph_value", "stored_value": 8.2, "decision": "unsupported", "rationale": "Base pH8.2 is explicit; its equality in a named modified wrapper does not independently verify that variant."}]}, {"quantity_id": "q20", "topic": "Unspecified base NaOH quantity", "source": [{"evidence_id": "dsm86", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium86.pdf", "raw_path": "REVIEW_WORK/batch060/source01-03/dsm86.bin", "raw_sha256": "19ce73dc1e0358ecde0115a6b796481e33a1b1b4186fddf13d232c5d463609bf", "locator": "Page1 preparation", "accessed_at": "2026-10-28T07:48:20.215885Z", "quote": "Adjust pH to 8.2 with NaOH."}], "decision": "unsupported", "rationale": "The source names an adjustment reagent but no stock strength or dose. Retain it as preparation text with root evidence; do not invent a numeric concentration.", "layer_assessments": []}]

### Current ontology and MIM correspondence

grounding: concern. Targets: CultureMech:006701.

All recursive current chemical IDs, canonical OLS labels, formulas/hydrates and exact current MIM preferred rows were checked. Primary nitrate and hydrate identities are supported; secondary legacy000170/000171 are currently absent and need a scoped migration. Tryptone and yeast extract remain mixtures rather than receiving guessed chemical identities. Present catalog membership is not proof of historical validity.

### History and evidence scope

provenance: concern. Targets: CultureMech:006701.

Current source bytes, complete histories and scoped historical reports were read. Missing claim-level linkage and any malformed historical metadata are distinguished from authenticated source bytes; originals remain append-only.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:006701.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:006701.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Keep unverified strain-modified wrappers distinct

major / open / confirmed; issue key: culturemech-006701-keep-unverified-strain-modified-wrappers-distinct.

The generated record merges base86 with records explicitly named modified for DSM11376 and DSM11377. Their identical ingredient lists and SOURCE_DUPLICATE assertions derive from copied base composition, not independently recovered variant formulations. Exact variant endpoints are currently403. The September report endorses duplicate collapse, while the October variant reports expressly withhold formulation support; the latter limitation remains unresolved.

### f2: Preserve base-owner evidence and preparation

minor / open / confirmed; issue key: culturemech-006701-preserve-base-owner-evidence-and-preparation.

The generated target drops30 exact authenticated quantity claims retained by the two base owners and the DSM preparation instruction. Nitrilotriacetic acid lacks attached evidence in both base owners but has explicit current source support; the Titriplex I product annotation is not an unsupported stock strength. The base batch-water row is also absent. Credit existing owner work and repair only missing linkage/context after resolving the scope boundary.

### f3: Migrate current legacy nitrate references without changing identity

minor / open / confirmed; issue key: culturemech-006701-migrate-current-legacy-nitrate-references-without-changing-identity.

KNO3 and NaNO3 have correct primary63043 and63005 terms, but all five layers retain secondary MediaIngredientMech:000170/000171. Neither legacy identifier is present in the current packaged catalog; exact current KNO3/NaNO3 preferred rows are MAPPED to their correct primary CHEBI IDs. This is current migration evidence, not proof the legacy IDs were historically invalid. Other supplied hydrates and current primary fixes are retained.

### f4: Preserve malformed historical timestamps and unresolved source flags

minor / open / confirmed; issue key: culturemech-006701-preserve-malformed-historical-timestamps-and-unresolved-source-flags.

KOMODO-derived histories retain the malformed fractional timestamp ending .fZ and enrichment timestamps without a timezone. Their exact original instants cannot be inferred from current code. Aerobic: No is inherited metadata whose source semantics are not freshly authenticated by the403 responses; the primary base sheet supplies no organism-specific growth assertion.

## Recommended Actions And Acceptance Checks

### action1

Resolve each named variant from its exact source before endorsing equivalent formulation or duplicate consolidation. Preserve variant IDs and historical lineage, keep current unresolved quantities visibly unsupported, and regenerate only source-compatible assertions. Do not use a strain number as growth evidence.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Preserve all30 existing base-owner quantity claims; add the exact NTA claim, batch-water context and root preparation evidence. Retain the current DSM pH instruction. Regenerate compatible base records without transferring these claims to unresolved variants.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Reconcile the two legacy secondary slots using the exact current KNO3/NaNO3 catalog rows and already correct primary IDs. Preserve source amounts and hydrate forms; append migration provenance and do not treat a current catalog absence as historical invalidity.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action4

Keep every original historical event byte-preserved. If authoritative event metadata is recovered, append verified correction/context in a new event rather than rewriting the original timestamp. Label unresolved source flags and mapping retrieval limits explicitly; do not infer growth, atmosphere or strain equivalence.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-2 | data/normalized_yaml/bacterial/castenholz_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-3 | data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-4 | data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| identity-search | REVIEW_WORK/batch060/record03/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _parse_api_solutions, _parse_preparation_steps | context_only | Current composition parser restricts ingredients to the primary solution, excludes solvent and recognized stock additions, and retains explicit g_l. The solution parser preserves referenced or percent-defined stocks and source attributes. Preparation parsing still concatenates all solution steps into root preparation_steps; source-stage annotation remains important. These present functions do not prove the historical execution that produced this record. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group copies a sole contributor with merge metadata. For multiple contributors it passes records to merge_formulation_evidence, which checks compatibility; it does not authorize merging different preparation assertions. |
| writer-formulation | src/culturemech/merge/formulation.py; formulation_content, merge_formulation_evidence | context_only | Current compatibility preserves scientific fields and list order and rejects unequal formulations; only specified provenance/evidence lists are unioned. It performs no concentration conversion or stock expansion and does not authenticate historical merges. |
| writer-cleanup | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients, merge_ingredient_group | context_only | Current cleanup groups identical normalized names, keeps the first entry as a base, flags differing concentrations and combines a warning note; it does not sum concentrations. It can still discard distinctions when names repeat, so source stage must be retained. Current behavior does not establish the historical cause of an existing discrepancy. |
| historical-1 | reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml.md; Entire exact Record-header report, every claim row and narrative | context_only | Current independently captured API response has exactly the cited historical raw SHA256; all 18 literal JSON snippets and locators match. This authenticates those response bytes, not the historical access time or recommendations. |
| historical-2 | reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_86_modified_for_dsm_11376.yaml.md; Entire exact Record-header report, every claim row and narrative | context_only | Current independently captured API response has exactly the cited historical raw SHA256; all 18 literal JSON snippets and locators match. This authenticates those response bytes, not the historical access time or recommendations. |
| historical-3 | reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_86_modified_for_dsm_11377.yaml.md; Entire exact Record-header report, every claim row and narrative | context_only | Current independently captured API response has exactly the cited historical raw SHA256; all 18 literal JSON snippets and locators match. This authenticates those response bytes, not the historical access time or recommendations. |
| historical-4 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/castenholz_medium.yaml.md; Entire exact Record-header report, every claim row and narrative | context_only | Current independently captured API response has exactly the cited historical raw SHA256; all 18 literal JSON snippets and locators match. This authenticates those response bytes, not the historical access time or recommendations. |
| historical-5 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CASTENHOLZ_MEDIUM.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-6 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-7 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/castenholz_medium.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-8 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-9 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-10 | reports/yaml_record_review/20260922T043306Z-CASTENHOLZ_MEDIUM.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-reader | REVIEW_WORK/batch060/record03/historical-reader.json | context_only | All exact target/owner historical report texts and current raw/literal/locator joins; historical recommendations remain subject to current stage and volume evidence. |
| dsm86 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium86.pdf; Page1, full table and sole preparation sentence | supports | Complete primary PDF read textually and visually:16 batch ingredients,1000 ml water and pH8.2 adjustment with NaOH. Water is not an explicit measured final-volume instruction; no strain-specific variant recipe or growth observation is supplied. |
| api86 | https://mediadive.dsmz.de/rest/medium/86; $.data.medium and $.data.solutions[0], complete recipe and steps | supports | Complete current API declares16 main g_l rates, volume1000, water and pH preparation. Current raw digest matches the historical86 response; exact object matches authenticate source bytes rather than old access events or variant equivalence. |
| komodo86 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=86; Complete response and capture metadata; exact historical href | context_only | Fresh request to the exact historical route returned HTTP403. No current mapping table or variant formulation was recovered; retained challenge body is an access failure, not scientific evidence. |
| komodo86_11376 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=86_11376; Complete response and capture metadata; exact historical href | context_only | Fresh request to the exact historical route returned HTTP403. No current mapping table or variant formulation was recovered; retained challenge body is an access failure, not scientific evidence. |
| komodo86_11377 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=86_11377; Complete response and capture metadata; exact historical href | context_only | Fresh request to the exact historical route returned HTTP403. No current mapping table or variant formulation was recovered; retained challenge body is an access failure, not scientific evidence. |
| komodoList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Complete response and capture metadata; exact historical href | context_only | Fresh request to the exact historical route returned HTTP403. No current mapping table or variant formulation was recovered; retained challenge body is an access failure, not scientific evidence. |
| writer-dsm-resolver | src/culturemech/enrich/dsmz_resolver.py; merge_composition, _add_enrichment_metadata, resolve_recipe | context_only | Current merge_composition copies non-placeholder ingredients and available solutions, pH, physical_state and medium_type from the DSM source, but does not copy preparation_steps. It adds local naive-time enrichment metadata. Current resolve_recipe is restricted to empty KOMODO_ records; this source body is not proof that the differently named variant files were processed by the current version. |
| attached-authentication | REVIEW_WORK/batch060/record03/attached-claim-authentication.json | supports | Thirty direct existing base-owner claims independently match the current API raw digest, literal quotes and decoded exact locators. Historical mapping-table bytes and original access events are not authenticated by this result. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_44557; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32583 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32583; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi63043 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63043; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi63005 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63005; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi91258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91258; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86254 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86254; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86364; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31440; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch060/record03/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch060/record03/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch060/record03/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch060/record03/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch060/record03/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch060/record03/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch060/record03/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch060/record03/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch060/record03/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- Exact current KOMODO base, two variant pages and historical MediaList route all returned403; source identity mapping remains a historical attached excerpt, not a freshly retrieved table. The base DSM recipe cannot authenticate strain-specific variants.
- Current API86 raw bytes equal the cited historical9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539 response and authenticate matching objects, not old retrieval events, variant equivalence or every historical recommendation.
- Primary water1000 ml is a batch input, not an explicit measured final-volume instruction. API g_l and volume1000 are retained as declared provider quantities. No molar concentration for undefined tryptone/yeast mixtures is endorsed.
- NaOH dose/stock strength, autoclave settings, culture temperature and strain growth are not supplied by the base sheet and were not inferred. No unverified variant process is filled from base evidence.
- The current resolver and merger bodies explain present behavior only; they do not establish which historical version created the copied ingredient lists or merge. The September proposed unconditional four-record remerge is not adopted.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T080818Z-batch060-record03-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Castenholz Medium: preserve base evidence and keep unresolved variants separate'
started_at: '2026-10-28T07:46:08.330450Z'
finished_at: '2026-10-28T08:08:18.758048Z'
reviewer:
  identity: Codex independent source reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh assessment of the inspected checkout and newly captured
    primary/provider/ontology evidence; no reconstruction of lost reviews and no record
    edits.
skill: .claude/skills/review-yaml-record/SKILL.md; .claude/skills/review-ingredient-concentrations/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: All16 base concentrations match explicit current provider rates and the primary
  batch table. Thirty attached base-owner quantity claims are authenticated by exact
  current response bytes. The generated merge loses these claims and the DSM preparation,
  while two named strain-modified wrappers remain unverified and must not inherit
  base formulation authority. Legacy nitrate links and malformed historical timestamps
  also need bounded, append-only follow-up.
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
  - path: data/culturemech_id_registry.tsv
    sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
    role: context
  - path: data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml
    sha256: 717fff1e3fcf7ee29e3207ec40de4a6a9d1f934f1f50770b23e13a26de05a220
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml
    sha256: 3a4499cc2433aaf42f5ade5e8013489c562d0d3261c135d92fa822d91e60d383
    role: context
  - path: data/normalized_yaml/bacterial/castenholz_medium.yaml
    sha256: 7fbcf1fb0529cdf2e0c465b1cc213ec82c1b4f9c2fccb9062dc4a46b20a9b7f9
    role: context
  - path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml
    sha256: 73d8afcc420902766f554628cc2d7c3691dd0b0d7eeb9a1b95dcd7032048b391
    role: context
  - path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml
    sha256: 3bf67f640c3294fdc0a7e60aec05e0f9d1225cdcb4257365b7cf0c18d3db1829
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml.md
    sha256: ce582ea6cbdba5998d6b1e4d514dcf348a092197133c0481132a8787114295d0
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_86_modified_for_dsm_11376.yaml.md
    sha256: 6ccbb0a8b7a578dac76fe424eb031d2c3a34a1bc804a0da90a492c9010ef60e1
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_86_modified_for_dsm_11377.yaml.md
    sha256: 869c5b0cbc6c5e7823c517e0ace0084e7f16e3906f520be572bafc0b3a92f781
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/castenholz_medium.yaml.md
    sha256: 92d74f9ca3f7990003e918eb0a1a16cf4470c988a92e3f50a38c0840ffab8c7d
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CASTENHOLZ_MEDIUM.md
    sha256: 1a4ec4eef00bfd7fb2fbdeb0002fc01172c4fefce5139a154d79c7c625364139
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.md
    sha256: 0cb96e9f22658ff882bacb593011cb971b57e9193fb2032aa56654de1f3bab86
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/castenholz_medium.md
    sha256: c4d3e2c2a25222e3295766a39fa63766a6ce157a50358880a2ea01e7808b20fd
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.md
    sha256: bb3f9550338bba0e3cd958b8b00084367cd198895a5f281e8458da67e706fbb5
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.md
    sha256: 350aeb4ae2932c8b8b6d9e6904f99e012f69a20e0ebf45582eec16afa87c80c8
    role: context
  - path: reports/yaml_record_review/20260922T043306Z-CASTENHOLZ_MEDIUM.md
    sha256: d7e922c23e207659edcb3788331f82ac36d94b822851c8d6cb5da9590cde0a3a
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
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
  description: Full selected record and exact maintained contributors; explicitly
    scoped dependency and external-source limits retained.
  selection: Actual batch060 native selection index 03.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006701
targets:
- target_id: CultureMech:006701
  path: data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml
  label: castenholz_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/castenholz_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:006701
  command: just validate-schema data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml
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
  - CultureMech:006701
  command: just validate-strict data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml --out
    REVIEW_WORK/batch060/record03/strict.tsv --workers 1
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
  - CultureMech:006701
  command: just validate-terms data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml
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
  - CultureMech:006701
  command: just validate-references data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 717fff1e3fcf7ee29e3207ec40de4a6a9d1f934f1f50770b23e13a26de05a220
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 3a4499cc2433aaf42f5ade5e8013489c562d0d3261c135d92fa822d91e60d383
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/castenholz_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 7fbcf1fb0529cdf2e0c465b1cc213ec82c1b4f9c2fccb9062dc4a46b20a9b7f9
- evidence_id: owner-3
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml
  locator: Complete document
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 73d8afcc420902766f554628cc2d7c3691dd0b0d7eeb9a1b95dcd7032048b391
- evidence_id: owner-4
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml
  locator: Complete document
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 3bf67f640c3294fdc0a7e60aec05e0f9d1225cdcb4257365b7cf0c18d3db1829
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch060/record03/identity-search.json
  accessed_at: '2026-10-28T08:08:18.706978Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems resolved uniquely. Similar names and
    source accessions are not promoted to owners.
  snapshot_sha256: 1d64430df249fee22e1f9bad6816e7a0cf79179005d4c514cf26b06abb2996c2
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _parse_api_solutions, _parse_preparation_steps
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Current composition parser restricts ingredients to the primary solution,
    excludes solvent and recognized stock additions, and retains explicit g_l. The
    solution parser preserves referenced or percent-defined stocks and source attributes.
    Preparation parsing still concatenates all solution steps into root preparation_steps;
    source-stage annotation remains important. These present functions do not prove
    the historical execution that produced this record.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Current merge_group copies a sole contributor with merge metadata. For
    multiple contributors it passes records to merge_formulation_evidence, which checks
    compatibility; it does not authorize merging different preparation assertions.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content, merge_formulation_evidence
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Current compatibility preserves scientific fields and list order and rejects
    unequal formulations; only specified provenance/evidence lists are unioned. It
    performs no concentration conversion or stock expansion and does not authenticate
    historical merges.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: merge_duplicate_ingredients, merge_ingredient_group
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Current cleanup groups identical normalized names, keeps the first entry
    as a base, flags differing concentrations and combines a warning note; it does
    not sum concentrations. It can still discard distinctions when names repeat, so
    source stage must be retained. Current behavior does not establish the historical
    cause of an existing discrepancy.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: historical-1
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Current independently captured API response has exactly the cited historical
    raw SHA256; all 18 literal JSON snippets and locators match. This authenticates
    those response bytes, not the historical access time or recommendations.
  snapshot_sha256: ce582ea6cbdba5998d6b1e4d514dcf348a092197133c0481132a8787114295d0
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_86_modified_for_dsm_11376.yaml.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Current independently captured API response has exactly the cited historical
    raw SHA256; all 18 literal JSON snippets and locators match. This authenticates
    those response bytes, not the historical access time or recommendations.
  snapshot_sha256: 6ccbb0a8b7a578dac76fe424eb031d2c3a34a1bc804a0da90a492c9010ef60e1
- evidence_id: historical-3
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_86_modified_for_dsm_11377.yaml.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Current independently captured API response has exactly the cited historical
    raw SHA256; all 18 literal JSON snippets and locators match. This authenticates
    those response bytes, not the historical access time or recommendations.
  snapshot_sha256: 869c5b0cbc6c5e7823c517e0ace0084e7f16e3906f520be572bafc0b3a92f781
- evidence_id: historical-4
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/castenholz_medium.yaml.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Current independently captured API response has exactly the cited historical
    raw SHA256; all 18 literal JSON snippets and locators match. This authenticates
    those response bytes, not the historical access time or recommendations.
  snapshot_sha256: 92d74f9ca3f7990003e918eb0a1a16cf4470c988a92e3f50a38c0840ffab8c7d
- evidence_id: historical-5
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CASTENHOLZ_MEDIUM.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: 1a4ec4eef00bfd7fb2fbdeb0002fc01172c4fefce5139a154d79c7c625364139
- evidence_id: historical-6
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: 0cb96e9f22658ff882bacb593011cb971b57e9193fb2032aa56654de1f3bab86
- evidence_id: historical-7
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/castenholz_medium.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: c4d3e2c2a25222e3295766a39fa63766a6ce157a50358880a2ea01e7808b20fd
- evidence_id: historical-8
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: bb3f9550338bba0e3cd958b8b00084367cd198895a5f281e8458da67e706fbb5
- evidence_id: historical-9
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: 350aeb4ae2932c8b8b6d9e6904f99e012f69a20e0ebf45582eec16afa87c80c8
- evidence_id: historical-10
  kind: record_content
  reference: reports/yaml_record_review/20260922T043306Z-CASTENHOLZ_MEDIUM.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: d7e922c23e207659edcb3788331f82ac36d94b822851c8d6cb5da9590cde0a3a
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch060/record03/historical-reader.json
  accessed_at: '2026-10-28T08:08:18.713117Z'
  support: context_only
  summary: All exact target/owner historical report texts and current raw/literal/locator
    joins; historical recommendations remain subject to current stage and volume evidence.
  snapshot_sha256: 19abd2cabebd5918a5fd2a3693ea4ae4f837106a47e6ded20ad78de6bd7011b2
- evidence_id: dsm86
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium86.pdf
  locator: Page1, full table and sole preparation sentence
  accessed_at: '2026-10-28T07:48:20.215885Z'
  support: supports
  summary: Complete primary PDF read textually and visually:16 batch ingredients,1000
    ml water and pH8.2 adjustment with NaOH. Water is not an explicit measured final-volume
    instruction; no strain-specific variant recipe or growth observation is supplied.
  snapshot_sha256: 19ce73dc1e0358ecde0115a6b796481e33a1b1b4186fddf13d232c5d463609bf
- evidence_id: api86
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/86
  locator: $.data.medium and $.data.solutions[0], complete recipe and steps
  accessed_at: '2026-10-28T07:48:19.868996Z'
  support: supports
  summary: Complete current API declares16 main g_l rates, volume1000, water and pH
    preparation. Current raw digest matches the historical86 response; exact object
    matches authenticate source bytes rather than old access events or variant equivalence.
  snapshot_sha256: 9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539
- evidence_id: komodo86
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=86
  locator: Complete response and capture metadata; exact historical href
  accessed_at: '2026-10-28T07:48:21.343950Z'
  support: context_only
  summary: Fresh request to the exact historical route returned HTTP403. No current
    mapping table or variant formulation was recovered; retained challenge body is
    an access failure, not scientific evidence.
  snapshot_sha256: 2418a36607f7a23f2256fe7db0c52c2dcbb82f2374665443aef20a6bb7cca63d
- evidence_id: komodo86_11376
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=86_11376
  locator: Complete response and capture metadata; exact historical href
  accessed_at: '2026-10-28T07:48:21.530663Z'
  support: context_only
  summary: Fresh request to the exact historical route returned HTTP403. No current
    mapping table or variant formulation was recovered; retained challenge body is
    an access failure, not scientific evidence.
  snapshot_sha256: 095dc2b601cb1ca2750289db327c5e510742ca8e0d0c7f0dfb2d4279f4d66e2c
- evidence_id: komodo86_11377
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=86_11377
  locator: Complete response and capture metadata; exact historical href
  accessed_at: '2026-10-28T07:48:21.575359Z'
  support: context_only
  summary: Fresh request to the exact historical route returned HTTP403. No current
    mapping table or variant formulation was recovered; retained challenge body is
    an access failure, not scientific evidence.
  snapshot_sha256: 9f69bd766ff459241ce9f6a07ab25db693042db29b1a30a372b1c515edc764c5
- evidence_id: komodoList
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Complete response and capture metadata; exact historical href
  accessed_at: '2026-10-28T07:48:21.628916Z'
  support: context_only
  summary: Fresh request to the exact historical route returned HTTP403. No current
    mapping table or variant formulation was recovered; retained challenge body is
    an access failure, not scientific evidence.
  snapshot_sha256: 110019f72f780bacc555175f4830d929f0beac01b8a4fedc2e320d9909122459
- evidence_id: writer-dsm-resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: merge_composition, _add_enrichment_metadata, resolve_recipe
  accessed_at: '2026-10-28T08:08:18.634011Z'
  support: context_only
  summary: Current merge_composition copies non-placeholder ingredients and available
    solutions, pH, physical_state and medium_type from the DSM source, but does not
    copy preparation_steps. It adds local naive-time enrichment metadata. Current
    resolve_recipe is restricted to empty KOMODO_ records; this source body is not
    proof that the differently named variant files were processed by the current version.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: attached-authentication
  kind: record_content
  reference: REVIEW_WORK/batch060/record03/attached-claim-authentication.json
  accessed_at: '2026-10-28T08:08:18.713709Z'
  support: supports
  summary: Thirty direct existing base-owner claims independently match the current
    API raw digest, literal quotes and decoded exact locators. Historical mapping-table
    bytes and original access events are not authenticated by this result.
  snapshot_sha256: f9d73027236cf1ad5b784c0d88f08cecd8042cde478926483db1f0d388eb2fe9
- evidence_id: chebi44557
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_44557
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:27.306683Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 371aa3b809db6c5d1ec8f8b8be40011e6b1132b1c0be40e70fb927788728d65a
- evidence_id: chebi32583
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32583
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:26.276350Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: bb76fa6464f579ff9218bf3c39d0374635193572c64fffc9e98c9d20aca283b1
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:25.672076Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 1635f67d01e00cabdef4ed0d9ef6d5383787c56bd0447051deb90ad353b499a2
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:24.600268Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b145f4ff9b90ebb993ff576d9ab35a6c10b7c42a3b99e18feffcc8d75c0e1e50
- evidence_id: chebi63043
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63043
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:28.707603Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 27d2a6a8a75a261941f0290b29dab700e2a3dc13dbf882f1624793e18ea2fa62
- evidence_id: chebi63005
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63005
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:28.375864Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 989f7dba2ab0bc556056f2d79a2f53fae9ce391393fc7ba373cbfe5afc25ae03
- evidence_id: chebi91258
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91258
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:31.107533Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a3f1cf351d76c04558ededfbd4973d468bf9e20f61e408de14e6a571ba4955b8
- evidence_id: chebi86254
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86254
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:29.742099Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 9ab13b3239309508e3fdfe4eed248db3fccb868d23243c20a61cf870527b1273
- evidence_id: chebi86364
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86364
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:30.328166Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0e8fbfc2ee82502bd7a5b4b3ba6cfaaae0ad1779400d07af8e2e0f726af793e9
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:26.037813Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 6bf1390236046f1cb7b21e2fc324fccba6e6eac2bc4e519f12d998f0edce671b
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:26.677867Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f23e1405347fa9d8a0826d4dd1279b7cdec8361390d20e439154dcbbd386a2d4
- evidence_id: chebi31440
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31440
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:25.442414Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 453e496e1e59b82bb42cd3252d410b9dc77d0c11e49f3da70496a82978e80505
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:28.978650Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0271a149a298ff837ad8f690ce8cb0acf111f5d25c5efaf6fa828401ab951d56
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:28.092789Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 31dc996638b0cc1341ed24fcb38ec344af726c99d376ac94e952210fcb9ed583
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch060/record03/quantity-inventory.json
  accessed_at: '2026-10-28T08:08:18.756915Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: b872545c9be3b030ea5e2fcee5ad36e9d45391ba7b6eeda28d4de06c296dd056
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch060/record03/grounding-inventory.json
  accessed_at: '2026-10-28T08:08:18.756971Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: f41c755da5627f46433a231550b91cdf0b5ab7906dbc40fc576065deb2e89e1c
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch060/record03/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T08:08:18.757107Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 56cdcb84e993b312a8986354d3f9dd82fa9edb027a9890ee470a8a49a03ed6ce
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch060/record03/scalar-census.json
  accessed_at: '2026-10-28T08:08:18.757147Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: a948596dac393d7524c59efc85c88bc0c91cc471867fb719c43754e4ad95c608
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch060/record03/validate-schema.json
  accessed_at: '2026-10-28T07:46:09.407018Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: 630eeb9fa68ed0c68af668874e82769aa2429aff24c890bb51fc739d1b7929ce
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch060/record03/validate-strict.json
  accessed_at: '2026-10-28T07:46:10.383048Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch060/record03/strict.tsv\n"
  snapshot_sha256: c713c0b126ad52f34cfa415656294ffd23b136b1548d431d598686ef32564135
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch060/record03/validate-terms.json
  accessed_at: '2026-10-28T07:46:11.442182Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: 294bb35e1f2f4aafd4be251fba78bf06c9632ec0fbd80c87c4da673142d01485
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch060/record03/validate-references.json
  accessed_at: '2026-10-28T07:46:12.166165Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: 01e4eb584fa5d6eee14a53f5493b795b321adcac6c5fd73c4f22c7ff2e364a5b
assessments:
- assessment_id: a1
  area: identity
  topic: Base lineage and unresolved wrappers
  outcome: concern
  summary: Exact generated merged_from resolves four maintained contributors. DSM86
    and base KOMODO86 linkage are historical identity claims with current base formulation
    support; the named11376/11377 wrappers have copied formulas and distinct source
    IDs. SOURCE_DUPLICATE annotations and equal ingredient signatures do not establish
    their exact recipes.
  target_ids:
  - CultureMech:006701
  evidence_ids:
  - identity-search
  - dsm86
  - api86
  - historical-reader
  - komodo86_11376
  - komodo86_11377
- assessment_id: a2
  area: completeness
  topic: Credit maintained base evidence and process
  outcome: concern
  summary: Two base owners retain30 exact attached quantity claims; the DSM owner
    retains the pH-adjustment instruction. The generated record omits these. Current
    formulation compatibility compares scientific metadata and preparation and would
    reject these differing assertions rather than establish equivalence from the ingredient
    signature.
  target_ids:
  - CultureMech:006701
  evidence_ids:
  - attached-authentication
  - writer-merge
  - writer-formulation
  - writer-dsm-resolver
- assessment_id: a3
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:006701
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "Nitrilotriacetic acid", "source": [{"evidence_id":
    "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86", "raw_path":
    "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T07:48:19.868996Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"attribute\":
    \"Titriplex I\",\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.523177,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 1, "compound": "Nitrilotriacetic acid", "compound_id": 189, "attribute":
    "Titriplex I", "amount": 100, "unit": "mg", "g_l": 0.1, "mmol_l": 0.523177, "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "mixed", "rationale": "Base-provider
    amount support, already attached evidence, missing generated linkage and unverified
    named variants are separate layer-specific decisions. All source supplied forms
    and units are retained.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API
    explicitly declares this base main g_l and the primary PDF supports the corresponding
    batch amount and supplied form. Add exact linkage without calling the water input
    a measured final volume. The primary identifies nitrilotriacetic acid (Titriplex
    I) and100 mg; this is a source product annotation, not an optional stock-strength
    instruction. The previous generic attribute flag does not by itself invalidate
    the explicit base amount."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API
    explicitly declares this base main g_l and the primary PDF supports the corresponding
    batch amount and supplied form. Add exact linkage without calling the water input
    a measured final volume. The primary identifies nitrilotriacetic acid (Titriplex
    I) and100 mg; this is a source product annotation, not an optional stock-strength
    instruction. The previous generic attribute flag does not by itself invalidate
    the explicit base amount."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API
    explicitly declares this base main g_l and the primary PDF supports the corresponding
    batch amount and supplied form. Add exact linkage without calling the water input
    a measured final volume. The primary identifies nitrilotriacetic acid (Titriplex
    I) and100 mg; this is a source product annotation, not an optional stock-strength
    instruction. The previous generic attribute flag does not by itself invalidate
    the explicit base amount."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number
    equals the base DSM86 provider rate, but this named strain-modified source lacks
    independent formulation evidence. Exact current variant endpoint403 and inherited
    copied ingredients do not authorize transferring the base recipe. The primary
    identifies nitrilotriacetic acid (Titriplex I) and100 mg; this is a source product
    annotation, not an optional stock-strength instruction. The previous generic attribute
    flag does not by itself invalidate the explicit base amount."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number
    equals the base DSM86 provider rate, but this named strain-modified source lacks
    independent formulation evidence. Exact current variant endpoint403 and inherited
    copied ingredients do not authorize transferring the base recipe. The primary
    identifies nitrilotriacetic acid (Titriplex I) and100 mg; this is a source product
    annotation, not an optional stock-strength instruction. The previous generic attribute
    flag does not by itself invalidate the explicit base amount."}]}, {"quantity_id":
    "q2", "topic": "CaSO4 x 2 H2O", "source": [{"evidence_id": "api86", "reference":
    "https://mediadive.dsmz.de/rest/medium/86", "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin",
    "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T07:48:19.868996Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"CaSO4 x 2 H2O\",\n                        \"compound_id\": 190,\n                        \"amount\":
    60,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.06,\n                        \"mmol_l\": 0.348489,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "CaSO4 x 2 H2O", "compound_id": 190, "amount": 60, "unit": "mg", "g_l": 0.06,
    "mmol_l": 0.348489, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "mixed", "rationale": "Base-provider amount support, already attached evidence,
    missing generated linkage and unverified named variants are separate layer-specific
    decisions. All source supplied forms and units are retained.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[1].concentration",
    "stored_value": {"value": "0.06", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The current API explicitly declares this base main g_l and the primary
    PDF supports the corresponding batch amount and supplied form. Add exact linkage
    without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.06",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.06",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.06",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number
    equals the base DSM86 provider rate, but this named strain-modified source lacks
    independent formulation evidence. Exact current variant endpoint403 and inherited
    copied ingredients do not authorize transferring the base recipe."}, {"path":
    "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path":
    "ingredients[1].concentration", "stored_value": {"value": "0.06", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The local number equals the base DSM86
    provider rate, but this named strain-modified source lacks independent formulation
    evidence. Exact current variant endpoint403 and inherited copied ingredients do
    not authorize transferring the base recipe."}]}, {"quantity_id": "q3", "topic":
    "MgSO4 x 7 H2O", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T07:48:19.868996Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\":
    100,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.405719,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "MgSO4 x 7 H2O", "compound_id": 8, "amount": 100, "unit": "mg", "g_l": 0.1, "mmol_l":
    0.405719, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "mixed",
    "rationale": "Base-provider amount support, already attached evidence, missing
    generated linkage and unverified named variants are separate layer-specific decisions.
    All source supplied forms and units are retained.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[2].concentration",
    "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The current API explicitly declares this base main g_l and the primary
    PDF supports the corresponding batch amount and supplied form. Add exact linkage
    without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number
    equals the base DSM86 provider rate, but this named strain-modified source lacks
    independent formulation evidence. Exact current variant endpoint403 and inherited
    copied ingredients do not authorize transferring the base recipe."}, {"path":
    "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path":
    "ingredients[2].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The local number equals the base DSM86
    provider rate, but this named strain-modified source lacks independent formulation
    evidence. Exact current variant endpoint403 and inherited copied ingredients do
    not authorize transferring the base recipe."}]}, {"quantity_id": "q4", "topic":
    "NaCl", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T07:48:19.868996Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\":
    8,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.008,\n                        \"mmol_l\": 0.136893,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "NaCl", "compound_id": 43, "amount": 8, "unit": "mg", "g_l": 0.008, "mmol_l":
    0.136893, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "mixed",
    "rationale": "Base-provider amount support, already attached evidence, missing
    generated linkage and unverified named variants are separate layer-specific decisions.
    All source supplied forms and units are retained.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[3].concentration",
    "stored_value": {"value": "0.008", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The current API explicitly declares this base main g_l and the primary
    PDF supports the corresponding batch amount and supplied form. Add exact linkage
    without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.008",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.008",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.008",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number
    equals the base DSM86 provider rate, but this named strain-modified source lacks
    independent formulation evidence. Exact current variant endpoint403 and inherited
    copied ingredients do not authorize transferring the base recipe."}, {"path":
    "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path":
    "ingredients[3].concentration", "stored_value": {"value": "0.008", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The local number equals the base DSM86
    provider rate, but this named strain-modified source lacks independent formulation
    evidence. Exact current variant endpoint403 and inherited copied ingredients do
    not authorize transferring the base recipe."}]}, {"quantity_id": "q5", "topic":
    "KNO3", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539",
    "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T07:48:19.868996Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"KNO3\",\n                        \"compound_id\": 191,\n                        \"amount\":
    103,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.103,\n                        \"mmol_l\": 1.01876,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "KNO3", "compound_id": 191, "amount": 103, "unit": "mg", "g_l": 0.103, "mmol_l":
    1.01876, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "mixed",
    "rationale": "Base-provider amount support, already attached evidence, missing
    generated linkage and unverified named variants are separate layer-specific decisions.
    All source supplied forms and units are retained.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[4].concentration",
    "stored_value": {"value": "0.103", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The current API explicitly declares this base main g_l and the primary
    PDF supports the corresponding batch amount and supplied form. Add exact linkage
    without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.103",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.103",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.103",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number
    equals the base DSM86 provider rate, but this named strain-modified source lacks
    independent formulation evidence. Exact current variant endpoint403 and inherited
    copied ingredients do not authorize transferring the base recipe."}, {"path":
    "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path":
    "ingredients[4].concentration", "stored_value": {"value": "0.103", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The local number equals the base DSM86
    provider rate, but this named strain-modified source lacks independent formulation
    evidence. Exact current variant endpoint403 and inherited copied ingredients do
    not authorize transferring the base recipe."}]}, {"quantity_id": "q6", "topic":
    "NaNO3", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539",
    "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T07:48:19.868996Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"NaNO3\",\n                        \"compound_id\": 187,\n                        \"amount\":
    689,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.689,\n                        \"mmol_l\": 8.10636,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "NaNO3", "compound_id": 187, "amount": 689, "unit": "mg", "g_l": 0.689, "mmol_l":
    8.10636, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "mixed",
    "rationale": "Base-provider amount support, already attached evidence, missing
    generated linkage and unverified named variants are separate layer-specific decisions.
    All source supplied forms and units are retained.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[5].concentration",
    "stored_value": {"value": "0.689", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The current API explicitly declares this base main g_l and the primary
    PDF supports the corresponding batch amount and supplied form. Add exact linkage
    without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.689",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.689",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.689",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number
    equals the base DSM86 provider rate, but this named strain-modified source lacks
    independent formulation evidence. Exact current variant endpoint403 and inherited
    copied ingredients do not authorize transferring the base recipe."}, {"path":
    "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path":
    "ingredients[5].concentration", "stored_value": {"value": "0.689", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The local number equals the base DSM86
    provider rate, but this named strain-modified source lacks independent formulation
    evidence. Exact current variant endpoint403 and inherited copied ingredients do
    not authorize transferring the base recipe."}]}, {"quantity_id": "q7", "topic":
    "Na2HPO4 x 2 H2O", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539",
    "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T07:48:19.868996Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"Na2HPO4 x 2 H2O\",\n                        \"compound_id\": 181,\n                        \"amount\":
    140,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.14,\n                        \"mmol_l\": 0.9862,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "Na2HPO4 x 2 H2O", "compound_id": 181, "amount": 140, "unit": "mg", "g_l": 0.14,
    "mmol_l": 0.9862, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "mixed",
    "rationale": "Base-provider amount support, already attached evidence, missing
    generated linkage and unverified named variants are separate layer-specific decisions.
    All source supplied forms and units are retained.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[6].concentration",
    "stored_value": {"value": "0.14", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The current API explicitly declares this base main g_l and the primary
    PDF supports the corresponding batch amount and supplied form. Add exact linkage
    without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.14",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.14",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.14",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number
    equals the base DSM86 provider rate, but this named strain-modified source lacks
    independent formulation evidence. Exact current variant endpoint403 and inherited
    copied ingredients do not authorize transferring the base recipe."}, {"path":
    "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path":
    "ingredients[6].concentration", "stored_value": {"value": "0.14", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The local number equals the base DSM86
    provider rate, but this named strain-modified source lacks independent formulation
    evidence. Exact current variant endpoint403 and inherited copied ingredients do
    not authorize transferring the base recipe."}]}, {"quantity_id": "q8", "topic":
    "FeCl3 x 6 H2O", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539",
    "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T07:48:19.868996Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"FeCl3 x 6 H2O\",\n                        \"compound_id\": 82,\n                        \"amount\":
    0.47,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.00047,\n                        \"mmol_l\": 0.00173883,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound":
    "FeCl3 x 6 H2O", "compound_id": 82, "amount": 0.47, "unit": "mg", "g_l": 0.00047,
    "mmol_l": 0.00173883, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "mixed", "rationale": "Base-provider amount support, already attached evidence,
    missing generated linkage and unverified named variants are separate layer-specific
    decisions. All source supplied forms and units are retained.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[7].concentration",
    "stored_value": {"value": "0.00047", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The current API explicitly declares this base main g_l and the primary
    PDF supports the corresponding batch amount and supplied form. Add exact linkage
    without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00047",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00047",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00047",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number
    equals the base DSM86 provider rate, but this named strain-modified source lacks
    independent formulation evidence. Exact current variant endpoint403 and inherited
    copied ingredients do not authorize transferring the base recipe."}, {"path":
    "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path":
    "ingredients[7].concentration", "stored_value": {"value": "0.00047", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The local number equals the base DSM86
    provider rate, but this named strain-modified source lacks independent formulation
    evidence. Exact current variant endpoint403 and inherited copied ingredients do
    not authorize transferring the base recipe."}]}, {"quantity_id": "q9", "topic":
    "MnSO4 x H2O", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539",
    "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T07:48:19.868996Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\":
    2.2,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.0022,\n                        \"mmol_l\": 0.0130165,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound":
    "MnSO4 x H2O", "compound_id": 14, "amount": 2.2, "unit": "mg", "g_l": 0.0022,
    "mmol_l": 0.0130165, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "mixed", "rationale": "Base-provider amount support, already attached evidence,
    missing generated linkage and unverified named variants are separate layer-specific
    decisions. All source supplied forms and units are retained.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[8].concentration",
    "stored_value": {"value": "0.0022", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The current API explicitly declares this base main g_l and the primary
    PDF supports the corresponding batch amount and supplied form. Add exact linkage
    without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.0022",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.0022",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.0022",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number
    equals the base DSM86 provider rate, but this named strain-modified source lacks
    independent formulation evidence. Exact current variant endpoint403 and inherited
    copied ingredients do not authorize transferring the base recipe."}, {"path":
    "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path":
    "ingredients[8].concentration", "stored_value": {"value": "0.0022", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The local number equals the base DSM86
    provider rate, but this named strain-modified source lacks independent formulation
    evidence. Exact current variant endpoint403 and inherited copied ingredients do
    not authorize transferring the base recipe."}]}, {"quantity_id": "q10", "topic":
    "ZnSO4 x 7 H2O", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539",
    "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T07:48:19.868996Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\":
    0.5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.0005,\n                        \"mmol_l\": 0.00173876,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "ZnSO4 x 7 H2O", "compound_id": 35, "amount": 0.5, "unit": "mg", "g_l": 0.0005,
    "mmol_l": 0.00173876, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "mixed", "rationale": "Base-provider amount support, already attached evidence,
    missing generated linkage and unverified named variants are separate layer-specific
    decisions. All source supplied forms and units are retained.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[9].concentration",
    "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The current API explicitly declares this base main g_l and the primary
    PDF supports the corresponding batch amount and supplied form. Add exact linkage
    without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.0005",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.0005",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.0005",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number
    equals the base DSM86 provider rate, but this named strain-modified source lacks
    independent formulation evidence. Exact current variant endpoint403 and inherited
    copied ingredients do not authorize transferring the base recipe."}, {"path":
    "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path":
    "ingredients[9].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The local number equals the base DSM86
    provider rate, but this named strain-modified source lacks independent formulation
    evidence. Exact current variant endpoint403 and inherited copied ingredients do
    not authorize transferring the base recipe."}]}, {"quantity_id": "q11", "topic":
    "H3BO3", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539",
    "locator": "$.data.solutions[0].recipe[10]", "accessed_at": "2026-10-28T07:48:19.868996Z",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\":
    0.5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.0005,\n                        \"mmol_l\": 0.00808538,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound":
    "H3BO3", "compound_id": 37, "amount": 0.5, "unit": "mg", "g_l": 0.0005, "mmol_l":
    0.00808538, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "mixed",
    "rationale": "Base-provider amount support, already attached evidence, missing
    generated linkage and unverified named variants are separate layer-specific decisions.
    All source supplied forms and units are retained.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[10].concentration",
    "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The current API explicitly declares this base main g_l and the primary
    PDF supports the corresponding batch amount and supplied form. Add exact linkage
    without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.0005",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.0005",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.0005",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number
    equals the base DSM86 provider rate, but this named strain-modified source lacks
    independent formulation evidence. Exact current variant endpoint403 and inherited
    copied ingredients do not authorize transferring the base recipe."}, {"path":
    "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path":
    "ingredients[10].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The local number equals the base DSM86
    provider rate, but this named strain-modified source lacks independent formulation
    evidence. Exact current variant endpoint403 and inherited copied ingredients do
    not authorize transferring the base recipe."}]}, {"quantity_id": "q12", "topic":
    "CuSO4 x 5 H2O", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539",
    "locator": "$.data.solutions[0].recipe[11]", "accessed_at": "2026-10-28T07:48:19.868996Z",
    "quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\":
    \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\":
    25,\n                        \"unit\": \"\\u00b5g\",\n                        \"g_l\":
    2.5e-5,\n                        \"mmol_l\": 0.000100126,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 12, "compound":
    "CuSO4 x 5 H2O", "compound_id": 121, "amount": 25, "unit": "µg", "g_l": 2.5e-05,
    "mmol_l": 0.000100126, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "mixed", "rationale": "Base-provider amount support, already attached evidence,
    missing generated linkage and unverified named variants are separate layer-specific
    decisions. All source supplied forms and units are retained.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[11].concentration",
    "stored_value": {"value": "2.5e-05", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The current API explicitly declares this base main g_l and the primary
    PDF supports the corresponding batch amount and supplied form. Add exact linkage
    without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "2.5e-05",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "2.5e-05",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "2.5e-05",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number
    equals the base DSM86 provider rate, but this named strain-modified source lacks
    independent formulation evidence. Exact current variant endpoint403 and inherited
    copied ingredients do not authorize transferring the base recipe."}, {"path":
    "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path":
    "ingredients[11].concentration", "stored_value": {"value": "2.5e-05", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the
    base DSM86 provider rate, but this named strain-modified source lacks independent
    formulation evidence. Exact current variant endpoint403 and inherited copied ingredients
    do not authorize transferring the base recipe."}]}, {"quantity_id": "q13", "topic":
    "Na2MoO4 x 2 H2O", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539",
    "locator": "$.data.solutions[0].recipe[12]", "accessed_at": "2026-10-28T07:48:19.868996Z",
    "quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\":
    \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\":
    25,\n                        \"unit\": \"\\u00b5g\",\n                        \"g_l\":
    2.5e-5,\n                        \"mmol_l\": 0.000103327,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 13, "compound":
    "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 25, "unit": "µg", "g_l": 2.5e-05,
    "mmol_l": 0.000103327, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "mixed", "rationale": "Base-provider amount support, already attached evidence,
    missing generated linkage and unverified named variants are separate layer-specific
    decisions. All source supplied forms and units are retained.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[12].concentration",
    "stored_value": {"value": "2.5e-05", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The current API explicitly declares this base main g_l and the primary
    PDF supports the corresponding batch amount and supplied form. Add exact linkage
    without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "2.5e-05",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "2.5e-05",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "2.5e-05",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number
    equals the base DSM86 provider rate, but this named strain-modified source lacks
    independent formulation evidence. Exact current variant endpoint403 and inherited
    copied ingredients do not authorize transferring the base recipe."}, {"path":
    "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path":
    "ingredients[12].concentration", "stored_value": {"value": "2.5e-05", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the
    base DSM86 provider rate, but this named strain-modified source lacks independent
    formulation evidence. Exact current variant endpoint403 and inherited copied ingredients
    do not authorize transferring the base recipe."}]}, {"quantity_id": "q14", "topic":
    "CoCl2 x 6 H2O", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539",
    "locator": "$.data.solutions[0].recipe[13]", "accessed_at": "2026-10-28T07:48:19.868996Z",
    "quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\":
    \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\":
    46,\n                        \"unit\": \"\\u00b5g\",\n                        \"g_l\":
    4.6e-5,\n                        \"mmol_l\": 0.000354285,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 14, "compound":
    "CoCl2 x 6 H2O", "compound_id": 38, "amount": 46, "unit": "µg", "g_l": 4.6e-05,
    "mmol_l": 0.000354285, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "mixed", "rationale": "Base-provider amount support, already attached evidence,
    missing generated linkage and unverified named variants are separate layer-specific
    decisions. All source supplied forms and units are retained.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[13].concentration",
    "stored_value": {"value": "4.6e-05", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The current API explicitly declares this base main g_l and the primary
    PDF supports the corresponding batch amount and supplied form. Add exact linkage
    without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "4.6e-05",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "4.6e-05",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "4.6e-05",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number
    equals the base DSM86 provider rate, but this named strain-modified source lacks
    independent formulation evidence. Exact current variant endpoint403 and inherited
    copied ingredients do not authorize transferring the base recipe."}, {"path":
    "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path":
    "ingredients[13].concentration", "stored_value": {"value": "4.6e-05", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The local number equals the
    base DSM86 provider rate, but this named strain-modified source lacks independent
    formulation evidence. Exact current variant endpoint403 and inherited copied ingredients
    do not authorize transferring the base recipe."}]}, {"quantity_id": "q15", "topic":
    "Tryptone", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539",
    "locator": "$.data.solutions[0].recipe[14]", "accessed_at": "2026-10-28T07:48:19.868996Z",
    "quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\":
    \"Tryptone\",\n                        \"compound_id\": 71,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"mmol_l\": 14.0687,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 15, "compound":
    "Tryptone", "compound_id": 71, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 14.0687,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "mixed", "rationale":
    "Base-provider amount support, already attached evidence, missing generated linkage
    and unverified named variants are separate layer-specific decisions. All source
    supplied forms and units are retained.", "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The current API
    explicitly declares this base main g_l and the primary PDF supports the corresponding
    batch amount and supplied form. Add exact linkage without calling the water input
    a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number
    equals the base DSM86 provider rate, but this named strain-modified source lacks
    independent formulation evidence. Exact current variant endpoint403 and inherited
    copied ingredients do not authorize transferring the base recipe."}, {"path":
    "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path":
    "ingredients[14].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The local number equals the base DSM86
    provider rate, but this named strain-modified source lacks independent formulation
    evidence. Exact current variant endpoint403 and inherited copied ingredients do
    not authorize transferring the base recipe."}]}, {"quantity_id": "q16", "topic":
    "Yeast extract", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539",
    "locator": "$.data.solutions[0].recipe[15]", "accessed_at": "2026-10-28T07:48:19.868996Z",
    "quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\":
    \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 16, "compound": "Yeast extract", "compound_id": 16, "amount":
    1, "unit": "g", "g_l": 1, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "mixed", "rationale": "Base-provider amount support, already attached evidence,
    missing generated linkage and unverified named variants are separate layer-specific
    decisions. All source supplied forms and units are retained.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "ingredients[15].concentration",
    "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The current API explicitly declares this base main g_l and the primary
    PDF supports the corresponding batch amount and supplied form. Add exact linkage
    without calling the water input a measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The existing attached
    claim has the exact current API response digest, literal source object and matching
    locator. It explicitly supports this base provider-declared main g_l, with the
    final-volume limitation already retained; source mapping is identity-only and
    not variant evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The local number
    equals the base DSM86 provider rate, but this named strain-modified source lacks
    independent formulation evidence. Exact current variant endpoint403 and inherited
    copied ingredients do not authorize transferring the base recipe."}, {"path":
    "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path":
    "ingredients[15].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The local number equals the base DSM86
    provider rate, but this named strain-modified source lacks independent formulation
    evidence. Exact current variant endpoint403 and inherited copied ingredients do
    not authorize transferring the base recipe."}]}, {"quantity_id": "q17", "topic":
    "Base recipe water", "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539",
    "locator": "$.data.solutions[0].recipe[16]", "accessed_at": "2026-10-28T07:48:19.868996Z",
    "quote": "{\n                        \"recipe_order\": 17,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 17, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "The source water
    row is omitted from the local formulation. Add the batch solvent context only
    for the authenticated base; no dose transfers to unknown variants.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml", "field_path": "notes",
    "stored_value": "Source: KOMODO ModelSEED | ID: 86 | DSMZ Medium: 86 (mediadive.medium:86)
    | Aerobic: No", "decision": "add", "rationale": "Retain the1000 ml batch-water
    amount in scoped base formulation context; it is not a G_PER_L ingredient, percent
    or measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml",
    "field_path": "notes", "stored_value": "Source: KOMODO ModelSEED | ID: 86 | DSMZ
    Medium: 86 (mediadive.medium:86) | Aerobic: No", "decision": "add", "rationale":
    "Retain the1000 ml batch-water amount in scoped base formulation context; it is
    not a G_PER_L ingredient, percent or measured final volume."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml",
    "field_path": "notes", "stored_value": "Source: DSMZ | Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium86.pdf",
    "decision": "add", "rationale": "Retain the1000 ml batch-water amount in scoped
    base formulation context; it is not a G_PER_L ingredient, percent or measured
    final volume."}]}, {"quantity_id": "q18", "topic": "Base pH adjustment preparation",
    "source": [{"evidence_id": "api86", "reference": "https://mediadive.dsmz.de/rest/medium/86",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api86.bin", "raw_sha256": "9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T07:48:19.868996Z",
    "quote": "{\n                        \"step\": \"Adjust pH to 8.2 with NaOH.\"\n                    }",
    "exact_decoded_object": {"step": "Adjust pH to 8.2 with NaOH."}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}], "decision": "mixed", "rationale": "Primary and provider specify
    adjustment to pH8.2 with NaOH, with no NaOH dose or stock strength. Restore lost
    base process without inventing a quantity or extending it to unverified variants.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "The base source pH-adjustment instruction is absent here; preserve the already
    existing DSM owner instruction when resolving the base record.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml", "field_path":
    "preparation_steps", "stored_value": null, "decision": "add", "rationale": "The
    base source pH-adjustment instruction is absent here; preserve the already existing
    DSM owner instruction when resolving the base record.", "missing": true}, {"path":
    "data/normalized_yaml/bacterial/castenholz_medium.yaml", "field_path": "preparation_steps[0]",
    "stored_value": {"step_number": 1, "action": "ADJUST_PH", "description": "Adjust
    pH to 8.2 with NaOH."}, "decision": "evidence_only", "rationale": "The maintained
    DSM owner already retains the exact pH-adjustment sentence; credit it and attach
    root source evidence."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "unsupported",
    "rationale": "No variant-specific preparation was recovered; the absent field
    must not be filled from a presumed duplicate base.", "missing": true}, {"path":
    "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml", "field_path":
    "preparation_steps", "stored_value": null, "decision": "unsupported", "rationale":
    "No variant-specific preparation was recovered; the absent field must not be filled
    from a presumed duplicate base.", "missing": true}]}, {"quantity_id": "q19", "topic":
    "Current pH fields", "source": [{"evidence_id": "dsm86", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium86.pdf",
    "raw_path": "REVIEW_WORK/batch060/source01-03/dsm86.bin", "raw_sha256": "19ce73dc1e0358ecde0115a6b796481e33a1b1b4186fddf13d232c5d463609bf",
    "locator": "Page1 preparation", "accessed_at": "2026-10-28T07:48:20.215885Z",
    "quote": "Adjust pH to 8.2 with NaOH."}], "decision": "mixed", "rationale": "All
    existing pH assertions are individually scoped; no strain optimum is inferred.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ph_value", "stored_value": 8.2, "decision": "evidence_only", "rationale":
    "Existing base pH8.2 is directly supported and retained."}, {"path": "data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml",
    "field_path": "ph_value", "stored_value": 8.2, "decision": "evidence_only", "rationale":
    "Existing base pH8.2 is directly supported and retained."}, {"path": "data/normalized_yaml/bacterial/castenholz_medium.yaml",
    "field_path": "ph_value", "stored_value": 8.2, "decision": "evidence_only", "rationale":
    "Existing base pH8.2 is directly supported and retained."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml",
    "field_path": "ph_value", "stored_value": 8.2, "decision": "unsupported", "rationale":
    "Base pH8.2 is explicit; its equality in a named modified wrapper does not independently
    verify that variant."}, {"path": "data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml",
    "field_path": "ph_value", "stored_value": 8.2, "decision": "unsupported", "rationale":
    "Base pH8.2 is explicit; its equality in a named modified wrapper does not independently
    verify that variant."}]}, {"quantity_id": "q20", "topic": "Unspecified base NaOH
    quantity", "source": [{"evidence_id": "dsm86", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium86.pdf",
    "raw_path": "REVIEW_WORK/batch060/source01-03/dsm86.bin", "raw_sha256": "19ce73dc1e0358ecde0115a6b796481e33a1b1b4186fddf13d232c5d463609bf",
    "locator": "Page1 preparation", "accessed_at": "2026-10-28T07:48:20.215885Z",
    "quote": "Adjust pH to 8.2 with NaOH."}], "decision": "unsupported", "rationale":
    "The source names an adjustment reagent but no stock strength or dose. Retain
    it as preparation text with root evidence; do not invent a numeric concentration.",
    "layer_assessments": []}]'
- assessment_id: a4
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: concern
  summary: All recursive current chemical IDs, canonical OLS labels, formulas/hydrates
    and exact current MIM preferred rows were checked. Primary nitrate and hydrate
    identities are supported; secondary legacy000170/000171 are currently absent and
    need a scoped migration. Tryptone and yeast extract remain mixtures rather than
    receiving guessed chemical identities. Present catalog membership is not proof
    of historical validity.
  target_ids:
  - CultureMech:006701
  evidence_ids:
  - grounding
- assessment_id: a5
  area: provenance
  topic: History and evidence scope
  outcome: concern
  summary: Current source bytes, complete histories and scoped historical reports
    were read. Missing claim-level linkage and any malformed historical metadata are
    distinguished from authenticated source bytes; originals remain append-only.
  target_ids:
  - CultureMech:006701
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
  - CultureMech:006701
  evidence_ids:
  - local-target
- assessment_id: a7
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:006701
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-006701-keep-unverified-strain-modified-wrappers-distinct
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Keep unverified strain-modified wrappers distinct
  description: The generated record merges base86 with records explicitly named modified
    for DSM11376 and DSM11377. Their identical ingredient lists and SOURCE_DUPLICATE
    assertions derive from copied base composition, not independently recovered variant
    formulations. Exact variant endpoints are currently403. The September report endorses
    duplicate collapse, while the October variant reports expressly withhold formulation
    support; the latter limitation remains unresolved.
  target_ids:
  - CultureMech:006701
  field_paths:
  - merged_from
  - synonyms
  - variant_children
  - parent_media
  - variant_relationship
  - variant_modifications
  evidence_ids:
  - identity-search
  - historical-reader
  - history
  - api86
  - komodo86_11376
  - komodo86_11377
  - writer-formulation
  rule_id: P2-source-variant-scope
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/castenholz_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-006701-preserve-base-owner-evidence-and-preparation
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Preserve base-owner evidence and preparation
  description: The generated target drops30 exact authenticated quantity claims retained
    by the two base owners and the DSM preparation instruction. Nitrilotriacetic acid
    lacks attached evidence in both base owners but has explicit current source support;
    the Titriplex I product annotation is not an unsupported stock strength. The base
    batch-water row is also absent. Credit existing owner work and repair only missing
    linkage/context after resolving the scope boundary.
  target_ids:
  - CultureMech:006701
  field_paths:
  - ingredients
  - evidence
  - preparation_steps
  - notes
  evidence_ids:
  - attached-authentication
  - dsm86
  - api86
  - quantities
  - writer-dsm-resolver
  - writer-formulation
  rule_id: P3-evidence-and-preparation
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/castenholz_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-006701-migrate-current-legacy-nitrate-references-without-changing-identity
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Migrate current legacy nitrate references without changing identity
  description: KNO3 and NaNO3 have correct primary63043 and63005 terms, but all five
    layers retain secondary MediaIngredientMech:000170/000171. Neither legacy identifier
    is present in the current packaged catalog; exact current KNO3/NaNO3 preferred
    rows are MAPPED to their correct primary CHEBI IDs. This is current migration
    evidence, not proof the legacy IDs were historically invalid. Other supplied hydrates
    and current primary fixes are retained.
  target_ids:
  - CultureMech:006701
  field_paths:
  - ingredients[4].mediaingredientmech_term
  - ingredients[5].mediaingredientmech_term
  evidence_ids:
  - grounding
  - history
  rule_id: P2.1-current-identifier-migration
  native_severity: P2
  normalization_reason: Native P2 identifier-link defect is normalized to minor because
    primary chemical identities and supported base quantities are already correct;
    only obsolete secondary-reference representation remains.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/castenholz_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f4
  issue_key: culturemech-006701-preserve-malformed-historical-timestamps-and-unresolved-source-flags
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Preserve malformed historical timestamps and unresolved source flags
  description: 'KOMODO-derived histories retain the malformed fractional timestamp
    ending .fZ and enrichment timestamps without a timezone. Their exact original
    instants cannot be inferred from current code. Aerobic: No is inherited metadata
    whose source semantics are not freshly authenticated by the403 responses; the
    primary base sheet supplies no organism-specific growth assertion.'
  target_ids:
  - CultureMech:006701
  field_paths:
  - notes
  - curation_history[0].timestamp
  - curation_history[1].timestamp
  - data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml::curation_history[1].timestamp
  evidence_ids:
  - history
  - historical-reader
  - komodoList
  - writer-dsm-resolver
  rule_id: P3-provenance-precision
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/castenholz_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Resolve each named variant from its exact source before endorsing equivalent
    formulation or duplicate consolidation. Preserve variant IDs and historical lineage,
    keep current unresolved quantities visibly unsupported, and regenerate only source-compatible
    assertions. Do not use a strain number as growth evidence.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006701
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/castenholz_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Preserve all30 existing base-owner quantity claims; add the exact NTA
    claim, batch-water context and root preparation evidence. Retain the current DSM
    pH instruction. Regenerate compatible base records without transferring these
    claims to unresolved variants.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006701
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/castenholz_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Reconcile the two legacy secondary slots using the exact current KNO3/NaNO3
    catalog rows and already correct primary IDs. Preserve source amounts and hydrate
    forms; append migration provenance and do not treat a current catalog absence
    as historical invalidity.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006701
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/castenholz_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action4
  description: Keep every original historical event byte-preserved. If authoritative
    event metadata is recovered, append verified correction/context in a new event
    rather than rewriting the original timestamp. Label unresolved source flags and
    mapping retrieval limits explicitly; do not infer growth, atmosphere or strain
    equivalence.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006701
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/castenholz_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11376.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_86_modified_for_dsm_11377.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- Exact current KOMODO base, two variant pages and historical MediaList route all
  returned403; source identity mapping remains a historical attached excerpt, not
  a freshly retrieved table. The base DSM recipe cannot authenticate strain-specific
  variants.
- Current API86 raw bytes equal the cited historical9524a3acc6aa20186693bb8125303862ddfc9ac7655ea2333c77d5b222d48539
  response and authenticate matching objects, not old retrieval events, variant equivalence
  or every historical recommendation.
- Primary water1000 ml is a batch input, not an explicit measured final-volume instruction.
  API g_l and volume1000 are retained as declared provider quantities. No molar concentration
  for undefined tryptone/yeast mixtures is endorsed.
- NaOH dose/stock strength, autoclave settings, culture temperature and strain growth
  are not supplied by the base sheet and were not inferred. No unverified variant
  process is filled from base evidence.
- The current resolver and merger bodies explain present behavior only; they do not
  establish which historical version created the copied ingredient lists or merge.
  The September proposed unconditional four-record remerge is not adopted.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
