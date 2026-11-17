# Chromatium salexigens: restore the required base and distinguish feeding-stock strength

- Review: 20261028T094947Z-batch062-record01-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T09:27:29.234425Z
- Finished UTC: 2026-10-28T09:49:47.300430Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM421 explicitly supplements medium28; the local five-ingredient record omits that base and misplaces the neutralized-sulfide stock strength as a direct rate. Four supplement rates are supported as provider declarations. The DSM owner’s substantial preparation must be retained and scoped, while the base dependency’s flattened stocks and conflicting primary/provider versions prevent an unqualified complete formulation.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch062 native selection index 01.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:005246 | data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml | generated | chromatium_salexigens_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:005246 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:005246 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:005246 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:005246 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Exact provenance and explicit base dependency

identity: supported. Targets: CultureMech:005246.

The two exact maintained contributors retain distinct stable IDs and reciprocal historical SOURCE_DUPLICATE links. The selected record uses the KOMODO identity, whose local notes explicitly cite DSM421. The historical selected-pair relationship supports provenance, not full preparation equality: the DSM owner has eleven steps and the KOMODO owner has none. DSM421 expressly names medium28.

### Complex liquid formulation

consistency: supported. Targets: CultureMech:005246.

The complete referenced base contains yeast extract, supporting COMPLEX/UNDEFINED and liquid state. The truncated five-ingredient view alone would conceal that basis; it must not motivate a false defined-medium recategorization.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:005246.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "NaCl supplement", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T09:27:43.186753Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 10,\n                        \"unit\": \"%\",\n                        \"g_l\": 100,\n                        \"mmol_l\": 1711.16,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "NaCl", "compound_id": 43, "amount": 10, "unit": "%", "g_l": 100, "mmol_l": 1711.16, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm421", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium421.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm421.bin", "raw_sha256": "147737ed0bfdd97948c86a691a34151f6e28a89687ab665b857bdd210f385ccc", "locator": "Complete supplement instruction", "accessed_at": "2026-10-28T09:27:43.389676Z", "quote": "421. CHROMATIUM SALEXIGENS MEDIUM\n\nSupplement medium 28 with NaCl (10%), MgCl 2 x 6 H2O (0.3%) Na-acetate (0.05%)\nand sodium thiosulfate (0.05%). Incubate at 500 to 1000 Lux light intensity."}], "decision": "evidence_only", "rationale": "The provider explicitly declares this supplement g_l rate in Main421. Retain it at the supplement stage with evidence; the primary bare percent alone does not establish w/v and the incomplete base prevents treating this list as the complete final formulation.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "100", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly declares this supplement g_l rate in Main421. Retain it at the supplement stage with evidence; the primary bare percent alone does not establish w/v and the incomplete base prevents treating this list as the complete final formulation."}, {"path": "data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "100", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly declares this supplement g_l rate in Main421. Retain it at the supplement stage with evidence; the primary bare percent alone does not establish w/v and the incomplete base prevents treating this list as the complete final formulation."}, {"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "100", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly declares this supplement g_l rate in Main421. Retain it at the supplement stage with evidence; the primary bare percent alone does not establish w/v and the incomplete base prevents treating this list as the complete final formulation."}]}, {"quantity_id": "q2", "topic": "MgCl2 x6 H2O supplement", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T09:27:43.186753Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.3,\n                        \"unit\": \"%\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 14.7563,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "MgCl2 x 6 H2O", "compound_id": 79, "amount": 0.3, "unit": "%", "g_l": 3, "mmol_l": 14.7563, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm421", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium421.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm421.bin", "raw_sha256": "147737ed0bfdd97948c86a691a34151f6e28a89687ab665b857bdd210f385ccc", "locator": "Complete supplement instruction", "accessed_at": "2026-10-28T09:27:43.389676Z", "quote": "421. CHROMATIUM SALEXIGENS MEDIUM\n\nSupplement medium 28 with NaCl (10%), MgCl 2 x 6 H2O (0.3%) Na-acetate (0.05%)\nand sodium thiosulfate (0.05%). Incubate at 500 to 1000 Lux light intensity."}], "decision": "evidence_only", "rationale": "The provider explicitly declares this supplement g_l rate in Main421. Retain it at the supplement stage with evidence; the primary bare percent alone does not establish w/v and the incomplete base prevents treating this list as the complete final formulation.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "3", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly declares this supplement g_l rate in Main421. Retain it at the supplement stage with evidence; the primary bare percent alone does not establish w/v and the incomplete base prevents treating this list as the complete final formulation."}, {"path": "data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "3", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly declares this supplement g_l rate in Main421. Retain it at the supplement stage with evidence; the primary bare percent alone does not establish w/v and the incomplete base prevents treating this list as the complete final formulation."}, {"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "3", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly declares this supplement g_l rate in Main421. Retain it at the supplement stage with evidence; the primary bare percent alone does not establish w/v and the incomplete base prevents treating this list as the complete final formulation."}]}, {"quantity_id": "q3", "topic": "Sodium acetate supplement", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T09:27:43.186753Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Na acetate\",\n                        \"compound_id\": 401,\n                        \"amount\": 0.05,\n                        \"unit\": \"%\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 6.09505,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "Na acetate", "compound_id": 401, "amount": 0.05, "unit": "%", "g_l": 0.5, "mmol_l": 6.09505, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm421", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium421.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm421.bin", "raw_sha256": "147737ed0bfdd97948c86a691a34151f6e28a89687ab665b857bdd210f385ccc", "locator": "Complete supplement instruction", "accessed_at": "2026-10-28T09:27:43.389676Z", "quote": "421. CHROMATIUM SALEXIGENS MEDIUM\n\nSupplement medium 28 with NaCl (10%), MgCl 2 x 6 H2O (0.3%) Na-acetate (0.05%)\nand sodium thiosulfate (0.05%). Incubate at 500 to 1000 Lux light intensity."}], "decision": "evidence_only", "rationale": "The provider explicitly declares this supplement g_l rate in Main421. Retain it at the supplement stage with evidence; the primary bare percent alone does not establish w/v and the incomplete base prevents treating this list as the complete final formulation.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly declares this supplement g_l rate in Main421. Retain it at the supplement stage with evidence; the primary bare percent alone does not establish w/v and the incomplete base prevents treating this list as the complete final formulation."}, {"path": "data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly declares this supplement g_l rate in Main421. Retain it at the supplement stage with evidence; the primary bare percent alone does not establish w/v and the incomplete base prevents treating this list as the complete final formulation."}, {"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly declares this supplement g_l rate in Main421. Retain it at the supplement stage with evidence; the primary bare percent alone does not establish w/v and the incomplete base prevents treating this list as the complete final formulation."}]}, {"quantity_id": "q4", "topic": "Sodium thiosulfate supplement", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T09:27:43.186753Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Sodium Thiosulfate\",\n                        \"compound_id\": 1126,\n                        \"amount\": 0.05,\n                        \"unit\": \"%\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 3.16236,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "Sodium Thiosulfate", "compound_id": 1126, "amount": 0.05, "unit": "%", "g_l": 0.5, "mmol_l": 3.16236, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm421", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium421.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm421.bin", "raw_sha256": "147737ed0bfdd97948c86a691a34151f6e28a89687ab665b857bdd210f385ccc", "locator": "Complete supplement instruction", "accessed_at": "2026-10-28T09:27:43.389676Z", "quote": "421. CHROMATIUM SALEXIGENS MEDIUM\n\nSupplement medium 28 with NaCl (10%), MgCl 2 x 6 H2O (0.3%) Na-acetate (0.05%)\nand sodium thiosulfate (0.05%). Incubate at 500 to 1000 Lux light intensity."}], "decision": "evidence_only", "rationale": "The provider explicitly declares this supplement g_l rate in Main421. Retain it at the supplement stage with evidence; the primary bare percent alone does not establish w/v and the incomplete base prevents treating this list as the complete final formulation.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly declares this supplement g_l rate in Main421. Retain it at the supplement stage with evidence; the primary bare percent alone does not establish w/v and the incomplete base prevents treating this list as the complete final formulation."}, {"path": "data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly declares this supplement g_l rate in Main421. Retain it at the supplement stage with evidence; the primary bare percent alone does not establish w/v and the incomplete base prevents treating this list as the complete final formulation."}, {"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly declares this supplement g_l rate in Main421. Retain it at the supplement stage with evidence; the primary bare percent alone does not establish w/v and the incomplete base prevents treating this list as the complete final formulation."}]}, {"quantity_id": "q5", "topic": "Neutralized feeding-stock strength mislocated as direct ingredient", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52", "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T09:27:43.186753Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 124.905,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Na2S x 9 H2O", "compound_id": 54, "amount": 3, "unit": "g", "g_l": 30, "mmol_l": 124.905, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52", "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T09:27:43.186753Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Neutralized sulfide solution 3% (w/v)\",\n                        \"solution_id\": 34,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "solution": "Neutralized sulfide solution 3% (w/v)", "solution_id": 34, "amount": 10, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm28", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm28.bin", "raw_sha256": "442636c7b32c8f6de4a54fd8acaaa22f8e1a130f3d4b45af59d5782fe77a6c3d", "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T09:27:43.589061Z", "quote": "Neutralized sulfide solution:\nDistilled water                                                100.00       ml\nNa2S x 9 H2O                                                     3.00        g\n\nThe sulfide solution is prepared"}], "decision": "correct", "rationale": "The current API states a10 ml recipe row and variable1–3 ml/100 ml feed prose, whereas the primary prescribes periodic feeding without a fixed dose. Keep the conflict visible instead of selecting one dose for a complete-medium calculation.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "30", "unit": "G_PER_L"}, "decision": "correct", "rationale": "30 g/L describes the separate neutralized feeding stock, not the complete medium. Retain3 g/100 ml stock provenance and the separate variable feeding stage; no fixed final-medium contribution is justified."}, {"path": "data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "30", "unit": "G_PER_L"}, "decision": "correct", "rationale": "30 g/L describes the separate neutralized feeding stock, not the complete medium. Retain3 g/100 ml stock provenance and the separate variable feeding stage; no fixed final-medium contribution is justified."}, {"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "30", "unit": "G_PER_L"}, "decision": "correct", "rationale": "30 g/L describes the separate neutralized feeding stock, not the complete medium. Retain3 g/100 ml stock provenance and the separate variable feeding stage; no fixed final-medium contribution is justified."}]}, {"quantity_id": "q6", "topic": "Required Main28 base", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T09:27:43.186753Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Main sol. 28\",\n                        \"solution_id\": 26,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "solution": "Main sol. 28", "solution_id": 26, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm421", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium421.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm421.bin", "raw_sha256": "147737ed0bfdd97948c86a691a34151f6e28a89687ab665b857bdd210f385ccc", "locator": "Supplement medium28 instruction", "accessed_at": "2026-10-28T09:27:43.389676Z", "quote": "421. CHROMATIUM SALEXIGENS MEDIUM\n\nSupplement medium 28 with NaCl (10%), MgCl 2 x 6 H2O (0.3%) Na-acetate (0.05%)\nand sodium thiosulfate (0.05%). Incubate at 500 to 1000 Lux light intensity."}], "decision": "add", "rationale": "The API references1000 ml Main28; the primary says supplement medium28. This is a recipe/base quantity, not proof that all additions yield an independently measured one-litre final preparation.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Create the explicitly required base reference/topology rather than pretending that four supplements and a feeding stock form the full medium.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Create the explicitly required base reference/topology rather than pretending that four supplements and a feeding stock form the full medium.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Create the explicitly required base reference/topology rather than pretending that four supplements and a feeding stock form the full medium.", "missing": true}]}, {"quantity_id": "q7", "topic": "Scoped DSM28 CaCl2 x 2 H2O", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.543478,\n                        \"mmol_l\": 3.69675,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "CaCl2 x 2 H2O", "compound_id": 7, "amount": 0.25, "unit": "g", "g_l": 0.543478, "mmol_l": 3.69675, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The current provider explicitly declares this rate for Solution A, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.543478", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider explicitly declares this rate for Solution A, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q8", "topic": "Scoped DSM28 Yeast extract", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.543478,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Yeast extract", "compound_id": 16, "amount": 0.25, "unit": "g", "g_l": 0.543478, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The current provider explicitly declares this rate for Solution A, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.543478", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider explicitly declares this rate for Solution A, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q9", "topic": "Scoped DSM28 Na2S x 9 H2O", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 14.8148,\n                        \"mmol_l\": 61.6816,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Na2S x 9 H2O", "compound_id": 54, "amount": 2, "unit": "g", "g_l": 14.8148, "mmol_l": 61.6816, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[8].recipe[0]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 124.905,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Na2S x 9 H2O", "compound_id": 54, "amount": 3, "unit": "g", "g_l": 30, "mmol_l": 124.905, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm28", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm28.bin", "raw_sha256": "442636c7b32c8f6de4a54fd8acaaa22f8e1a130f3d4b45af59d5782fe77a6c3d", "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T09:27:43.589061Z", "quote": "Solution B:\nNa2S x 9 H2O                                                      2.00        g\nDistilled water                                                 135.00       ml\nPrepare in a screw-cap bottle, bubble with N2 to replace air, close tightly and autoclave.\n\nSolution C:"}, {"evidence_id": "dsm28", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm28.bin", "raw_sha256": "442636c7b32c8f6de4a54fd8acaaa22f8e1a130f3d4b45af59d5782fe77a6c3d", "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T09:27:43.589061Z", "quote": "Neutralized sulfide solution:\nDistilled water                                                100.00       ml\nNa2S x 9 H2O                                                     3.00        g\n\nThe sulfide solution is prepared"}], "decision": "correct", "rationale": "44.8148 g/L sums14.8148 g/L initial sulfide-stock and30 g/L later feeding-stock rates. These are distinct stages and cannot be added as a final-medium concentration. Retain separate source stocks and addition instructions.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "44.8148", "unit": "G_PER_L"}, "decision": "correct", "rationale": "44.8148 g/L sums14.8148 g/L initial sulfide-stock and30 g/L later feeding-stock rates. These are distinct stages and cannot be added as a final-medium concentration. Retain separate source stocks and addition instructions."}]}, {"quantity_id": "q10", "topic": "Scoped DSM28 NaHCO3", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[3].recipe[0]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 357.113,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "NaHCO3", "compound_id": 55, "amount": 1.5, "unit": "g", "g_l": 30, "mmol_l": 357.113, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The current provider explicitly declares this rate for Bicarbonate solution, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "30", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider explicitly declares this rate for Bicarbonate solution, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q11", "topic": "Scoped DSM28 Resazurin", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[4].recipe[0]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"attribute\": \"0,1%\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0111111,\n                        \"mmol_l\": 0.0484799,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Resazurin", "compound_id": 25, "attribute": "0,1%", "amount": 0.5, "unit": "ml", "g_l": 0.0111111, "mmol_l": 0.0484799, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm28", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm28.bin", "raw_sha256": "442636c7b32c8f6de4a54fd8acaaa22f8e1a130f3d4b45af59d5782fe77a6c3d", "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T09:27:43.589061Z", "quote": "Solution D\nResazurin (0,1%)                                                        0.5     ml\nDistilled water                                                      450.00     ml\n\nAutoclave in a cotton"}], "decision": "conflict", "rationale": "The provider declares0.0111111 g/L within resazurin solution, whereas the primary supplies0.5 ml of0.1% reagent in450 ml water without a percentage basis. Preserve both statements; no independent mass conversion or final-medium resazurin rate is authenticated.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.0111111", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The provider declares0.0111111 g/L within resazurin solution, whereas the primary supplies0.5 ml of0.1% reagent in450 ml water without a percentage basis. Preserve both statements; no independent mass conversion or final-medium resazurin rate is authenticated."}]}, {"quantity_id": "q12", "topic": "Scoped DSM28 Ammonium chloride", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[5].recipe[0]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Ammonium chloride\",\n                        \"compound_id\": 57,\n                        \"amount\": 0.35,\n                        \"unit\": \"g\",\n                        \"g_l\": 13.4615,\n                        \"mmol_l\": 251.665,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Ammonium chloride", "compound_id": 57, "amount": 0.35, "unit": "g", "g_l": 13.4615, "mmol_l": 251.665, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The current provider explicitly declares this rate for Pfennig's heterotrophic salts solution, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "13.4615", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider explicitly declares this rate for Pfennig's heterotrophic salts solution, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q13", "topic": "Scoped DSM28 Ammonium acetate", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[5].recipe[1]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Ammonium acetate\",\n                        \"compound_id\": 58,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 9.61539,\n                        \"mmol_l\": 124.746,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Ammonium acetate", "compound_id": 58, "amount": 0.25, "unit": "g", "g_l": 9.61539, "mmol_l": 124.746, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The current provider explicitly declares this rate for Pfennig's heterotrophic salts solution, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "9.61539", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider explicitly declares this rate for Pfennig's heterotrophic salts solution, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q14", "topic": "Scoped DSM28 Pyruvic acid sodium salt", "source": [{"evidence_id": "dsm28", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm28.bin", "raw_sha256": "442636c7b32c8f6de4a54fd8acaaa22f8e1a130f3d4b45af59d5782fe77a6c3d", "locator": "PDF extracted line 36; visually checked page", "accessed_at": "2026-10-28T09:27:43.589061Z", "quote": "Pyruvic acid sodium salt                                               0.25      g"}, {"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[5].recipe; complete current solutionE payload", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n  \"status\": 200,\n  \"count\": 1,\n  \"data\": {\n    \"medium\": {\n      \"id\": 28,\n      \"name\": \"PFENNIG'S MEDIUM I \",\n      \"complex_medium\": \"yes\",\n      \"min_pH\": 7.1,\n      \"max_pH\": 7.3,\n      \"source\": \"DSMZ\",\n      \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf\"\n    },\n    \"solutions\": [\n      {\n        \"id\": 26,\n        \"name\": \"Main sol. 28\",\n        \"volume\": 1000,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"solution\": \"Solution A\",\n            \"solution_id\": 27,\n            \"amount\": 460,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 2,\n            \"solution\": \"Resazurin solution\",\n            \"solution_id\": 30,\n            \"amount\": 450,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 3,\n            \"solution\": \"Bicarbonate solution\",\n            \"solution_id\": 29,\n            \"amount\": 50,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 4,\n            \"solution\": \"Pfennig's heterotrophic salts solution\",\n            \"solution_id\": 31,\n            \"amount\": 26,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 5,\n            \"solution\": \"Sulfide solution, 1.5%\",\n            \"solution_id\": 28,\n            \"amount\": 40,\n            \"unit\": \"ml/l\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 6,\n            \"solution\": \"Vitamin B12 solution\",\n            \"solution_id\": 32,\n            \"amount\": 1,\n            \"unit\": \"ml/l\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 7,\n            \"solution\": \"Neutralized sulfide solution 3% (w/v)\",\n            \"solution_id\": 34,\n            \"amount\": 10,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\": [\n          {\n            \"recipe_order\": 7,\n            \"step\": \"Adjust the pH with filter-sterilised 1M Na2CO3 to 7.1-7.3.\"\n          },\n          {\n            \"recipe_order\": 7,\n            \"step\": \"If needed, aliquot into sterile, N&lt;sub&gt;2&lt;/sub&gt; gassed screw-cap tubes under N&lt;sub&gt;2&lt;/sub&gt; gas.\"\n          },\n          {\n            \"recipe_order\": 7,\n            \"step\": \"During the first 24 h, the iron of the medium precipitates in the form of black flocks. No other sediment should arise in the otherwise clear medium.\"\n          },\n          {\n            \"recipe_order\": 2,\n            \"step\": \"Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121°C for 15 min (as decribed below).\"\n          },\n          {\n            \"recipe_order\": 2,\n            \"step\": \"Prepare the following solutions (resazurin, bicarbonate and Pfennig's heterotrophic salts) and sterilize as given below.\"\n          },\n          {\n            \"recipe_order\": 5,\n            \"step\": \"Add bicarbonate solution and Pfennig's heterotrophic salts to the resazurin (complete volumina, i.e. 50 mL bicarbonate solution and 26 mL Pfennig's heterotrophic salts solution). Bubble with CO2 in an ice bath under sterile conditions.\"\n          },\n          {\n            \"recipe_order\": 5,\n            \"step\": \"Fill 50 ml of this mixture to each bottle of solution A (46 mL + 50 mL).\"\n          },\n          {\n            \"recipe_order\": 5,\n            \"step\": \"Before use, add 4 ml sulfide solution (1.5%) and 0.1 ml Vitamin B12 solution to each 100 mL bottle.\"\n          },\n          {\n            \"recipe_order\": 7,\n            \"step\": \"Feed the actively growing culture periodically with neutralized 3% solution of sodium sulfide (use 1 -3 mL/100 mL depending on strain and cultivation stage) to replenish sulfide and with other supplement solutions (see Ref. 3365).\"\n          },\n          {\n            \"step\": \"Note: for marine species use 1-3% NaCl and increase the amount of MgSO4 7*H2O to 2,8g/L\"\n          }\n        ]\n      },\n      {\n        \"id\": 27,\n        \"name\": \"Solution A\",\n        \"volume\": 460,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"CaCl2 x 2 H2O\",\n            \"compound_id\": 7,\n            \"amount\": 0.25,\n            \"unit\": \"g\",\n            \"g_l\": 0.543478,\n            \"mmol_l\": 3.69675,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\": \"Yeast extract\",\n            \"compound_id\": 16,\n            \"amount\": 0.25,\n            \"unit\": \"g\",\n            \"g_l\": 0.543478,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 3,\n            \"compound\": \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\": 460,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\": \"Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121°C for 15 min.\"\n          }\n        ],\n        \"equipment\": {\n          \"5486\": \"Autoclave\"\n        }\n      },\n      {\n        \"id\": 28,\n        \"name\": \"Sulfide solution, 1.5%\",\n        \"volume\": 135,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"Na2S x 9 H2O\",\n            \"compound_id\": 54,\n            \"amount\": 2,\n            \"unit\": \"g\",\n            \"g_l\": 14.8148,\n            \"mmol_l\": 61.6816,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\": \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\": 135,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\": \"Prepare in a screw-cap bottle, bubble with N2 to replace air, close tightly and autoclave.\"\n          }\n        ],\n        \"equipment\": {\n          \"5487\": \"Autoclave\"\n        }\n      },\n      {\n        \"id\": 29,\n        \"name\": \"Bicarbonate solution\",\n        \"volume\": 50,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"NaHCO3\",\n            \"compound_id\": 55,\n            \"amount\": 1.5,\n            \"unit\": \"g\",\n            \"g_l\": 30,\n            \"mmol_l\": 357.113,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\": \"H2O\",\n            \"compound_id\": 56,\n            \"amount\": 50,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\": \"Bubble with CO2 and filter sterilize into sterile, gas-tight, 100 ml screw-cap bottle.\"\n          }\n        ],\n        \"equipment\": {\n          \"5488\": \"Filter\"\n        }\n      },\n      {\n        \"id\": 30,\n        \"name\": \"Resazurin solution\",\n        \"volume\": 450,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"Resazurin\",\n            \"compound_id\": 25,\n            \"attribute\": \"0,1%\",\n            \"amount\": 0.5,\n            \"unit\": \"ml\",\n            \"g_l\": 0.0111111,\n            \"mmol_l\": 0.0484799,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\": \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\": 450,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\": \"Cool to room temperature under an atmosphere of N2/CO2 in an ice bath.\"\n          },\n          {\n            \"step\": \"Autoclave in a cotton-stoppered Erlenmeyer flask with an outlet tube for medium, connected to a glass outlet at the bottom of the vessel and has, at the other end, a silicon rubber tube with a pinch cock and a bell for aseptic dispensing of the medium into bottles.\"\n          }\n        ],\n        \"equipment\": {\n          \"5490\": \"Ice bath\",\n          \"5489\": \"Autoclave\"\n        }\n      },\n      {\n        \"id\": 31,\n        \"name\": \"Pfennig's heterotrophic salts solution\",\n        \"volume\": 26,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"Ammonium chloride\",\n            \"compound_id\": 57,\n            \"amount\": 0.35,\n            \"unit\": \"g\",\n            \"g_l\": 13.4615,\n            \"mmol_l\": 251.665,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\": \"Ammonium acetate\",\n            \"compound_id\": 58,\n            \"amount\": 0.25,\n            \"unit\": \"g\",\n            \"g_l\": 9.61539,\n            \"mmol_l\": 124.746,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 5,\n            \"compound\": \"MgSO4 x 7 H2O\",\n            \"compound_id\": 8,\n            \"amount\": 0.5,\n            \"unit\": \"g\",\n            \"g_l\": 19.2308,\n            \"mmol_l\": 78.0229,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 6,\n            \"compound\": \"KCl\",\n            \"compound_id\": 61,\n            \"amount\": 0.35,\n            \"unit\": \"g\",\n            \"g_l\": 13.4615,\n            \"mmol_l\": 180.571,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 7,\n            \"compound\": \"KH2PO4\",\n            \"compound_id\": 11,\n            \"amount\": 0.35,\n            \"unit\": \"g\",\n            \"g_l\": 13.4615,\n            \"mmol_l\": 98.9201,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 8,\n            \"solution\": \"Trace element solution SL-12 B\",\n            \"solution_id\": 33,\n            \"amount\": 1,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 9,\n            \"compound\": \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\": 25,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\": \"Filter sterilize into sterile, gas-tight, 100 ml screw-cap bottle.\"\n          }\n        ],\n        \"equipment\": {\n          \"3563\": \"Filter\"\n        }\n      },\n      {\n        \"id\": 32,\n        \"name\": \"Vitamin B12 solution\",\n        \"volume\": 100,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"Vitamin B12\",\n            \"compound_id\": 18,\n            \"amount\": 0.01,\n            \"unit\": \"g\",\n            \"g_l\": 0.1,\n            \"mmol_l\": 0.073779,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\": \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\": 100,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\": \"Filter sterilized\"\n          }\n        ],\n        \"equipment\": {\n          \"5492\": \"Filter\"\n        }\n      },\n      {\n        \"id\": 33,\n        \"name\": \"Trace element solution SL-12 B\",\n        \"volume\": 1000,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"Na2-EDTA\",\n            \"compound_id\": 34,\n            \"amount\": 3,\n            \"unit\": \"g\",\n            \"g_l\": 3,\n            \"mmol_l\": 8.9231,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\": \"FeSO4 x 7 H2O\",\n            \"compound_id\": 12,\n            \"amount\": 1.1,\n            \"unit\": \"g\",\n            \"g_l\": 1.1,\n            \"mmol_l\": 3.95662,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 3,\n            \"compound\": \"CoCl2 x 6 H2O\",\n            \"compound_id\": 38,\n            \"amount\": 190,\n            \"unit\": \"mg\",\n            \"g_l\": 0.19,\n            \"mmol_l\": 1.46335,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 4,\n            \"compound\": \"MnCl2 x 2 H2O\",\n            \"compound_id\": 63,\n            \"amount\": 50,\n            \"unit\": \"mg\",\n            \"g_l\": 0.05,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 5,\n            \"compound\": \"ZnCl2\",\n            \"compound_id\": 64,\n            \"amount\": 42,\n            \"unit\": \"mg\",\n            \"g_l\": 0.042,\n            \"mmol_l\": 0.308144,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 6,\n            \"compound\": \"NiCl2 x 6 H2O\",\n            \"compound_id\": 40,\n            \"amount\": 24,\n            \"unit\": \"mg\",\n            \"g_l\": 0.024,\n            \"mmol_l\": 0.185187,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 7,\n            \"compound\": \"Na2MoO4 x 2 H2O\",\n            \"compound_id\": 9,\n            \"amount\": 18,\n            \"unit\": \"mg\",\n            \"g_l\": 0.018,\n            \"mmol_l\": 0.0743955,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 8,\n            \"compound\": \"H3BO3\",\n            \"compound_id\": 37,\n            \"amount\": 300,\n            \"unit\": \"mg\",\n            \"g_l\": 0.3,\n            \"mmol_l\": 4.85123,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 9,\n            \"compound\": \"CuCl2 x 2 H2O\",\n            \"compound_id\": 39,\n            \"amount\": 2,\n            \"unit\": \"mg\",\n            \"g_l\": 0.002,\n            \"mmol_l\": 0.0117314,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 10,\n            \"compound\": \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\": 1000,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\": \"Adjust pH to 6.0.\"\n          }\n        ],\n        \"equipment\": {\n          \"572\": \"Ice bath\",\n          \"2369\": \"Filter\"\n        }\n      },\n      {\n        \"id\": 34,\n        \"name\": \"Neutralized sulfide solution 3% (w/v)\",\n        \"volume\": 100,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"Na2S x 9 H2O\",\n            \"compound_id\": 54,\n            \"amount\": 3,\n            \"unit\": \"g\",\n            \"g_l\": 30,\n            \"mmol_l\": 124.905,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\": \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\": 100,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\": \"The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at 121°C. After cooling to room temperature the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle.\"\n          }\n        ]\n      }\n    ]\n  }\n}\n"}], "decision": "unsupported", "rationale": "The primary expressly supplies0.25 g in solutionE. The current API omits this ingredient from E;25 ml water plus1 ml trace addition is not an explicit final-volume declaration. Preserve the primary batch mass and the provider omission, but the local9.61539 g/L denominator is not independently authenticated.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "9.61539", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary expressly supplies0.25 g in solutionE. The current API omits this ingredient from E;25 ml water plus1 ml trace addition is not an explicit final-volume declaration. Preserve the primary batch mass and the provider omission, but the local9.61539 g/L denominator is not independently authenticated."}]}, {"quantity_id": "q15", "topic": "Scoped DSM28 Dextrose", "source": [{"evidence_id": "dsm28", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm28.bin", "raw_sha256": "442636c7b32c8f6de4a54fd8acaaa22f8e1a130f3d4b45af59d5782fe77a6c3d", "locator": "PDF extracted line 37; visually checked page", "accessed_at": "2026-10-28T09:27:43.589061Z", "quote": "Dextrose                                                               0.25      g"}, {"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[5].recipe; complete current solutionE payload", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n  \"status\": 200,\n  \"count\": 1,\n  \"data\": {\n    \"medium\": {\n      \"id\": 28,\n      \"name\": \"PFENNIG'S MEDIUM I \",\n      \"complex_medium\": \"yes\",\n      \"min_pH\": 7.1,\n      \"max_pH\": 7.3,\n      \"source\": \"DSMZ\",\n      \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf\"\n    },\n    \"solutions\": [\n      {\n        \"id\": 26,\n        \"name\": \"Main sol. 28\",\n        \"volume\": 1000,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"solution\": \"Solution A\",\n            \"solution_id\": 27,\n            \"amount\": 460,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 2,\n            \"solution\": \"Resazurin solution\",\n            \"solution_id\": 30,\n            \"amount\": 450,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 3,\n            \"solution\": \"Bicarbonate solution\",\n            \"solution_id\": 29,\n            \"amount\": 50,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 4,\n            \"solution\": \"Pfennig's heterotrophic salts solution\",\n            \"solution_id\": 31,\n            \"amount\": 26,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 5,\n            \"solution\": \"Sulfide solution, 1.5%\",\n            \"solution_id\": 28,\n            \"amount\": 40,\n            \"unit\": \"ml/l\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 6,\n            \"solution\": \"Vitamin B12 solution\",\n            \"solution_id\": 32,\n            \"amount\": 1,\n            \"unit\": \"ml/l\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 7,\n            \"solution\": \"Neutralized sulfide solution 3% (w/v)\",\n            \"solution_id\": 34,\n            \"amount\": 10,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\": [\n          {\n            \"recipe_order\": 7,\n            \"step\": \"Adjust the pH with filter-sterilised 1M Na2CO3 to 7.1-7.3.\"\n          },\n          {\n            \"recipe_order\": 7,\n            \"step\": \"If needed, aliquot into sterile, N&lt;sub&gt;2&lt;/sub&gt; gassed screw-cap tubes under N&lt;sub&gt;2&lt;/sub&gt; gas.\"\n          },\n          {\n            \"recipe_order\": 7,\n            \"step\": \"During the first 24 h, the iron of the medium precipitates in the form of black flocks. No other sediment should arise in the otherwise clear medium.\"\n          },\n          {\n            \"recipe_order\": 2,\n            \"step\": \"Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121°C for 15 min (as decribed below).\"\n          },\n          {\n            \"recipe_order\": 2,\n            \"step\": \"Prepare the following solutions (resazurin, bicarbonate and Pfennig's heterotrophic salts) and sterilize as given below.\"\n          },\n          {\n            \"recipe_order\": 5,\n            \"step\": \"Add bicarbonate solution and Pfennig's heterotrophic salts to the resazurin (complete volumina, i.e. 50 mL bicarbonate solution and 26 mL Pfennig's heterotrophic salts solution). Bubble with CO2 in an ice bath under sterile conditions.\"\n          },\n          {\n            \"recipe_order\": 5,\n            \"step\": \"Fill 50 ml of this mixture to each bottle of solution A (46 mL + 50 mL).\"\n          },\n          {\n            \"recipe_order\": 5,\n            \"step\": \"Before use, add 4 ml sulfide solution (1.5%) and 0.1 ml Vitamin B12 solution to each 100 mL bottle.\"\n          },\n          {\n            \"recipe_order\": 7,\n            \"step\": \"Feed the actively growing culture periodically with neutralized 3% solution of sodium sulfide (use 1 -3 mL/100 mL depending on strain and cultivation stage) to replenish sulfide and with other supplement solutions (see Ref. 3365).\"\n          },\n          {\n            \"step\": \"Note: for marine species use 1-3% NaCl and increase the amount of MgSO4 7*H2O to 2,8g/L\"\n          }\n        ]\n      },\n      {\n        \"id\": 27,\n        \"name\": \"Solution A\",\n        \"volume\": 460,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"CaCl2 x 2 H2O\",\n            \"compound_id\": 7,\n            \"amount\": 0.25,\n            \"unit\": \"g\",\n            \"g_l\": 0.543478,\n            \"mmol_l\": 3.69675,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\": \"Yeast extract\",\n            \"compound_id\": 16,\n            \"amount\": 0.25,\n            \"unit\": \"g\",\n            \"g_l\": 0.543478,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 3,\n            \"compound\": \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\": 460,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\": \"Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121°C for 15 min.\"\n          }\n        ],\n        \"equipment\": {\n          \"5486\": \"Autoclave\"\n        }\n      },\n      {\n        \"id\": 28,\n        \"name\": \"Sulfide solution, 1.5%\",\n        \"volume\": 135,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"Na2S x 9 H2O\",\n            \"compound_id\": 54,\n            \"amount\": 2,\n            \"unit\": \"g\",\n            \"g_l\": 14.8148,\n            \"mmol_l\": 61.6816,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\": \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\": 135,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\": \"Prepare in a screw-cap bottle, bubble with N2 to replace air, close tightly and autoclave.\"\n          }\n        ],\n        \"equipment\": {\n          \"5487\": \"Autoclave\"\n        }\n      },\n      {\n        \"id\": 29,\n        \"name\": \"Bicarbonate solution\",\n        \"volume\": 50,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"NaHCO3\",\n            \"compound_id\": 55,\n            \"amount\": 1.5,\n            \"unit\": \"g\",\n            \"g_l\": 30,\n            \"mmol_l\": 357.113,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\": \"H2O\",\n            \"compound_id\": 56,\n            \"amount\": 50,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\": \"Bubble with CO2 and filter sterilize into sterile, gas-tight, 100 ml screw-cap bottle.\"\n          }\n        ],\n        \"equipment\": {\n          \"5488\": \"Filter\"\n        }\n      },\n      {\n        \"id\": 30,\n        \"name\": \"Resazurin solution\",\n        \"volume\": 450,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"Resazurin\",\n            \"compound_id\": 25,\n            \"attribute\": \"0,1%\",\n            \"amount\": 0.5,\n            \"unit\": \"ml\",\n            \"g_l\": 0.0111111,\n            \"mmol_l\": 0.0484799,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\": \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\": 450,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\": \"Cool to room temperature under an atmosphere of N2/CO2 in an ice bath.\"\n          },\n          {\n            \"step\": \"Autoclave in a cotton-stoppered Erlenmeyer flask with an outlet tube for medium, connected to a glass outlet at the bottom of the vessel and has, at the other end, a silicon rubber tube with a pinch cock and a bell for aseptic dispensing of the medium into bottles.\"\n          }\n        ],\n        \"equipment\": {\n          \"5490\": \"Ice bath\",\n          \"5489\": \"Autoclave\"\n        }\n      },\n      {\n        \"id\": 31,\n        \"name\": \"Pfennig's heterotrophic salts solution\",\n        \"volume\": 26,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"Ammonium chloride\",\n            \"compound_id\": 57,\n            \"amount\": 0.35,\n            \"unit\": \"g\",\n            \"g_l\": 13.4615,\n            \"mmol_l\": 251.665,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\": \"Ammonium acetate\",\n            \"compound_id\": 58,\n            \"amount\": 0.25,\n            \"unit\": \"g\",\n            \"g_l\": 9.61539,\n            \"mmol_l\": 124.746,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 5,\n            \"compound\": \"MgSO4 x 7 H2O\",\n            \"compound_id\": 8,\n            \"amount\": 0.5,\n            \"unit\": \"g\",\n            \"g_l\": 19.2308,\n            \"mmol_l\": 78.0229,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 6,\n            \"compound\": \"KCl\",\n            \"compound_id\": 61,\n            \"amount\": 0.35,\n            \"unit\": \"g\",\n            \"g_l\": 13.4615,\n            \"mmol_l\": 180.571,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 7,\n            \"compound\": \"KH2PO4\",\n            \"compound_id\": 11,\n            \"amount\": 0.35,\n            \"unit\": \"g\",\n            \"g_l\": 13.4615,\n            \"mmol_l\": 98.9201,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 8,\n            \"solution\": \"Trace element solution SL-12 B\",\n            \"solution_id\": 33,\n            \"amount\": 1,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 9,\n            \"compound\": \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\": 25,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\": \"Filter sterilize into sterile, gas-tight, 100 ml screw-cap bottle.\"\n          }\n        ],\n        \"equipment\": {\n          \"3563\": \"Filter\"\n        }\n      },\n      {\n        \"id\": 32,\n        \"name\": \"Vitamin B12 solution\",\n        \"volume\": 100,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"Vitamin B12\",\n            \"compound_id\": 18,\n            \"amount\": 0.01,\n            \"unit\": \"g\",\n            \"g_l\": 0.1,\n            \"mmol_l\": 0.073779,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\": \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\": 100,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\": \"Filter sterilized\"\n          }\n        ],\n        \"equipment\": {\n          \"5492\": \"Filter\"\n        }\n      },\n      {\n        \"id\": 33,\n        \"name\": \"Trace element solution SL-12 B\",\n        \"volume\": 1000,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"Na2-EDTA\",\n            \"compound_id\": 34,\n            \"amount\": 3,\n            \"unit\": \"g\",\n            \"g_l\": 3,\n            \"mmol_l\": 8.9231,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\": \"FeSO4 x 7 H2O\",\n            \"compound_id\": 12,\n            \"amount\": 1.1,\n            \"unit\": \"g\",\n            \"g_l\": 1.1,\n            \"mmol_l\": 3.95662,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 3,\n            \"compound\": \"CoCl2 x 6 H2O\",\n            \"compound_id\": 38,\n            \"amount\": 190,\n            \"unit\": \"mg\",\n            \"g_l\": 0.19,\n            \"mmol_l\": 1.46335,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 4,\n            \"compound\": \"MnCl2 x 2 H2O\",\n            \"compound_id\": 63,\n            \"amount\": 50,\n            \"unit\": \"mg\",\n            \"g_l\": 0.05,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 5,\n            \"compound\": \"ZnCl2\",\n            \"compound_id\": 64,\n            \"amount\": 42,\n            \"unit\": \"mg\",\n            \"g_l\": 0.042,\n            \"mmol_l\": 0.308144,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 6,\n            \"compound\": \"NiCl2 x 6 H2O\",\n            \"compound_id\": 40,\n            \"amount\": 24,\n            \"unit\": \"mg\",\n            \"g_l\": 0.024,\n            \"mmol_l\": 0.185187,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 7,\n            \"compound\": \"Na2MoO4 x 2 H2O\",\n            \"compound_id\": 9,\n            \"amount\": 18,\n            \"unit\": \"mg\",\n            \"g_l\": 0.018,\n            \"mmol_l\": 0.0743955,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 8,\n            \"compound\": \"H3BO3\",\n            \"compound_id\": 37,\n            \"amount\": 300,\n            \"unit\": \"mg\",\n            \"g_l\": 0.3,\n            \"mmol_l\": 4.85123,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 9,\n            \"compound\": \"CuCl2 x 2 H2O\",\n            \"compound_id\": 39,\n            \"amount\": 2,\n            \"unit\": \"mg\",\n            \"g_l\": 0.002,\n            \"mmol_l\": 0.0117314,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 10,\n            \"compound\": \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\": 1000,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\": \"Adjust pH to 6.0.\"\n          }\n        ],\n        \"equipment\": {\n          \"572\": \"Ice bath\",\n          \"2369\": \"Filter\"\n        }\n      },\n      {\n        \"id\": 34,\n        \"name\": \"Neutralized sulfide solution 3% (w/v)\",\n        \"volume\": 100,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"Na2S x 9 H2O\",\n            \"compound_id\": 54,\n            \"amount\": 3,\n            \"unit\": \"g\",\n            \"g_l\": 30,\n            \"mmol_l\": 124.905,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\": \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\": 100,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\": \"The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at 121°C. After cooling to room temperature the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle.\"\n          }\n        ]\n      }\n    ]\n  }\n}\n"}], "decision": "unsupported", "rationale": "The primary expressly supplies0.25 g in solutionE. The current API omits this ingredient from E;25 ml water plus1 ml trace addition is not an explicit final-volume declaration. Preserve the primary batch mass and the provider omission, but the local9.61539 g/L denominator is not independently authenticated.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "9.61539", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary expressly supplies0.25 g in solutionE. The current API omits this ingredient from E;25 ml water plus1 ml trace addition is not an explicit final-volume declaration. Preserve the primary batch mass and the provider omission, but the local9.61539 g/L denominator is not independently authenticated."}]}, {"quantity_id": "q16", "topic": "Scoped DSM28 MgSO4 x 7 H2O", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[5].recipe[2]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 19.2308,\n                        \"mmol_l\": 78.0229,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "MgSO4 x 7 H2O", "compound_id": 8, "amount": 0.5, "unit": "g", "g_l": 19.2308, "mmol_l": 78.0229, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The current provider explicitly declares this rate for Pfennig's heterotrophic salts solution, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "19.2308", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider explicitly declares this rate for Pfennig's heterotrophic salts solution, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q17", "topic": "Scoped DSM28 KCl", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[5].recipe[3]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.35,\n                        \"unit\": \"g\",\n                        \"g_l\": 13.4615,\n                        \"mmol_l\": 180.571,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "KCl", "compound_id": 61, "amount": 0.35, "unit": "g", "g_l": 13.4615, "mmol_l": 180.571, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The current provider explicitly declares this rate for Pfennig's heterotrophic salts solution, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "13.4615", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider explicitly declares this rate for Pfennig's heterotrophic salts solution, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q18", "topic": "Scoped DSM28 KH2PO4", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[5].recipe[4]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.35,\n                        \"unit\": \"g\",\n                        \"g_l\": 13.4615,\n                        \"mmol_l\": 98.9201,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "KH2PO4", "compound_id": 11, "amount": 0.35, "unit": "g", "g_l": 13.4615, "mmol_l": 98.9201, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The current provider explicitly declares this rate for Pfennig's heterotrophic salts solution, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "13.4615", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider explicitly declares this rate for Pfennig's heterotrophic salts solution, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q19", "topic": "Scoped DSM28 Vitamin B12", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[6].recipe[0]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.073779,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Vitamin B12", "compound_id": 18, "amount": 0.01, "unit": "g", "g_l": 0.1, "mmol_l": 0.073779, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The current provider explicitly declares this rate for Vitamin B12 solution, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider explicitly declares this rate for Vitamin B12 solution, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q20", "topic": "Scoped DSM28 Na2-EDTA", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[7].recipe[0]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2-EDTA\",\n                        \"compound_id\": 34,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 8.9231,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Na2-EDTA", "compound_id": 34, "amount": 3, "unit": "g", "g_l": 3, "mmol_l": 8.9231, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The current provider explicitly declares this rate for Trace element solution SL-12 B, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "3", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider explicitly declares this rate for Trace element solution SL-12 B, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q21", "topic": "Scoped DSM28 FeSO4 x 7 H2O", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[7].recipe[1]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 1.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.1,\n                        \"mmol_l\": 3.95662,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "FeSO4 x 7 H2O", "compound_id": 12, "amount": 1.1, "unit": "g", "g_l": 1.1, "mmol_l": 3.95662, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The current provider explicitly declares this rate for Trace element solution SL-12 B, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "1.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider explicitly declares this rate for Trace element solution SL-12 B, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q22", "topic": "Scoped DSM28 CoCl2 x 6 H2O", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[7].recipe[2]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "CoCl2 x 6 H2O", "compound_id": 38, "amount": 190, "unit": "mg", "g_l": 0.19, "mmol_l": 1.46335, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The current provider explicitly declares this rate for Trace element solution SL-12 B, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.19", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider explicitly declares this rate for Trace element solution SL-12 B, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q23", "topic": "Scoped DSM28 MnCl2 x 2 H2O", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[7].recipe[3]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 2 H2O\",\n                        \"compound_id\": 63,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "MnCl2 x 2 H2O", "compound_id": 63, "amount": 50, "unit": "mg", "g_l": 0.05, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The current provider explicitly declares this rate for Trace element solution SL-12 B, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider explicitly declares this rate for Trace element solution SL-12 B, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q24", "topic": "Scoped DSM28 ZnCl2", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[7].recipe[4]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 42,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.042,\n                        \"mmol_l\": 0.308144,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "ZnCl2", "compound_id": 64, "amount": 42, "unit": "mg", "g_l": 0.042, "mmol_l": 0.308144, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The current provider explicitly declares this rate for Trace element solution SL-12 B, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.042", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider explicitly declares this rate for Trace element solution SL-12 B, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q25", "topic": "Scoped DSM28 NiCl2 x 6 H2O", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[7].recipe[5]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "NiCl2 x 6 H2O", "compound_id": 40, "amount": 24, "unit": "mg", "g_l": 0.024, "mmol_l": 0.185187, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The current provider explicitly declares this rate for Trace element solution SL-12 B, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.024", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider explicitly declares this rate for Trace element solution SL-12 B, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q26", "topic": "Scoped DSM28 Na2MoO4 x 2 H2O", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[7].recipe[6]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 18,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.018,\n                        \"mmol_l\": 0.0743955,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 18, "unit": "mg", "g_l": 0.018, "mmol_l": 0.0743955, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The current provider explicitly declares this rate for Trace element solution SL-12 B, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.018", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider explicitly declares this rate for Trace element solution SL-12 B, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q27", "topic": "Scoped DSM28 H3BO3", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[7].recipe[7]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 300,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "H3BO3", "compound_id": 37, "amount": 300, "unit": "mg", "g_l": 0.3, "mmol_l": 4.85123, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The current provider explicitly declares this rate for Trace element solution SL-12 B, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider explicitly declares this rate for Trace element solution SL-12 B, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q28", "topic": "Scoped DSM28 CuCl2 x 2 H2O", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[7].recipe[8]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "CuCl2 x 2 H2O", "compound_id": 39, "amount": 2, "unit": "mg", "g_l": 0.002, "mmol_l": 0.0117314, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The current provider explicitly declares this rate for Trace element solution SL-12 B, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.002", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider explicitly declares this rate for Trace element solution SL-12 B, a component solution. Preserve its source batch amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q29", "topic": "DSM28 source-only Main sol. 28: Solution A", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 27,\n                        \"amount\": 460,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "solution": "Solution A", "solution_id": 27, "amount": 460, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact Main sol. 28 recipe-stage quantity. Bare ml amounts remain batch/addition quantities; only explicitly printed ml/l is a provider per-litre declaration. Water rows are not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Rebuild the absent named solution/water topology with this exact stage. Retain existing preparation text as separately credited.", "missing": true}]}, {"quantity_id": "q30", "topic": "DSM28 source-only Main sol. 28: Resazurin solution", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Resazurin solution\",\n                        \"solution_id\": 30,\n                        \"amount\": 450,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "solution": "Resazurin solution", "solution_id": 30, "amount": 450, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact Main sol. 28 recipe-stage quantity. Bare ml amounts remain batch/addition quantities; only explicitly printed ml/l is a provider per-litre declaration. Water rows are not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Rebuild the absent named solution/water topology with this exact stage. Retain existing preparation text as separately credited.", "missing": true}]}, {"quantity_id": "q31", "topic": "DSM28 source-only Main sol. 28: Bicarbonate solution", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Bicarbonate solution\",\n                        \"solution_id\": 29,\n                        \"amount\": 50,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "solution": "Bicarbonate solution", "solution_id": 29, "amount": 50, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact Main sol. 28 recipe-stage quantity. Bare ml amounts remain batch/addition quantities; only explicitly printed ml/l is a provider per-litre declaration. Water rows are not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Rebuild the absent named solution/water topology with this exact stage. Retain existing preparation text as separately credited.", "missing": true}]}, {"quantity_id": "q32", "topic": "DSM28 source-only Main sol. 28: Pfennig's heterotrophic salts solution", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\": \"Pfennig's heterotrophic salts solution\",\n                        \"solution_id\": 31,\n                        \"amount\": 26,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "solution": "Pfennig's heterotrophic salts solution", "solution_id": 31, "amount": 26, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact Main sol. 28 recipe-stage quantity. Bare ml amounts remain batch/addition quantities; only explicitly printed ml/l is a provider per-litre declaration. Water rows are not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Rebuild the absent named solution/water topology with this exact stage. Retain existing preparation text as separately credited.", "missing": true}]}, {"quantity_id": "q33", "topic": "DSM28 source-only Main sol. 28: Sulfide solution, 1.5%", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"solution\": \"Sulfide solution, 1.5%\",\n                        \"solution_id\": 28,\n                        \"amount\": 40,\n                        \"unit\": \"ml/l\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "solution": "Sulfide solution, 1.5%", "solution_id": 28, "amount": 40, "unit": "ml/l", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact Main sol. 28 recipe-stage quantity. Bare ml amounts remain batch/addition quantities; only explicitly printed ml/l is a provider per-litre declaration. Water rows are not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Rebuild the absent named solution/water topology with this exact stage. Retain existing preparation text as separately credited.", "missing": true}]}, {"quantity_id": "q34", "topic": "DSM28 source-only Main sol. 28: Vitamin B12 solution", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Vitamin B12 solution\",\n                        \"solution_id\": 32,\n                        \"amount\": 1,\n                        \"unit\": \"ml/l\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "solution": "Vitamin B12 solution", "solution_id": 32, "amount": 1, "unit": "ml/l", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact Main sol. 28 recipe-stage quantity. Bare ml amounts remain batch/addition quantities; only explicitly printed ml/l is a provider per-litre declaration. Water rows are not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Rebuild the absent named solution/water topology with this exact stage. Retain existing preparation text as separately credited.", "missing": true}]}, {"quantity_id": "q35", "topic": "DSM28 source-only Main sol. 28: Neutralized sulfide solution 3% (w/v)", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Neutralized sulfide solution 3% (w/v)\",\n                        \"solution_id\": 34,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "solution": "Neutralized sulfide solution 3% (w/v)", "solution_id": 34, "amount": 10, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "conflict", "rationale": "Preserve the exact Main sol. 28 recipe-stage quantity. Bare ml amounts remain batch/addition quantities; only explicitly printed ml/l is a provider per-litre declaration. Water rows are not measured final volumes. The10 ml feeding row conflicts with variable feeding prose and the primary’s unfixed periodic feed; do not promote it to a universal dose.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Rebuild the absent named solution/water topology with this exact stage. Retain existing preparation text as separately credited.", "missing": true}]}, {"quantity_id": "q36", "topic": "DSM28 source-only Solution A: Distilled water", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 460,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "Distilled water", "compound_id": 4, "amount": 460, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact Solution A recipe-stage quantity. Bare ml amounts remain batch/addition quantities; only explicitly printed ml/l is a provider per-litre declaration. Water rows are not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Rebuild the absent named solution/water topology with this exact stage. Retain existing preparation text as separately credited.", "missing": true}]}, {"quantity_id": "q37", "topic": "DSM28 source-only Sulfide solution, 1.5%: Distilled water", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[2].recipe[1]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 135,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Distilled water", "compound_id": 4, "amount": 135, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact Sulfide solution, 1.5% recipe-stage quantity. Bare ml amounts remain batch/addition quantities; only explicitly printed ml/l is a provider per-litre declaration. Water rows are not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Rebuild the absent named solution/water topology with this exact stage. Retain existing preparation text as separately credited.", "missing": true}]}, {"quantity_id": "q38", "topic": "DSM28 source-only Bicarbonate solution: H2O", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[3].recipe[1]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"H2O\",\n                        \"compound_id\": 56,\n                        \"amount\": 50,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "H2O", "compound_id": 56, "amount": 50, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact Bicarbonate solution recipe-stage quantity. Bare ml amounts remain batch/addition quantities; only explicitly printed ml/l is a provider per-litre declaration. Water rows are not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Rebuild the absent named solution/water topology with this exact stage. Retain existing preparation text as separately credited.", "missing": true}]}, {"quantity_id": "q39", "topic": "DSM28 source-only Resazurin solution: Distilled water", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[4].recipe[1]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 450,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Distilled water", "compound_id": 4, "amount": 450, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact Resazurin solution recipe-stage quantity. Bare ml amounts remain batch/addition quantities; only explicitly printed ml/l is a provider per-litre declaration. Water rows are not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Rebuild the absent named solution/water topology with this exact stage. Retain existing preparation text as separately credited.", "missing": true}]}, {"quantity_id": "q40", "topic": "DSM28 source-only Pfennig's heterotrophic salts solution: Trace element solution SL-12 B", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[5].recipe[5]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Trace element solution SL-12 B\",\n                        \"solution_id\": 33,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "solution": "Trace element solution SL-12 B", "solution_id": 33, "amount": 1, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact Pfennig's heterotrophic salts solution recipe-stage quantity. Bare ml amounts remain batch/addition quantities; only explicitly printed ml/l is a provider per-litre declaration. Water rows are not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Rebuild the absent named solution/water topology with this exact stage. Retain existing preparation text as separately credited.", "missing": true}]}, {"quantity_id": "q41", "topic": "DSM28 source-only Pfennig's heterotrophic salts solution: Distilled water", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[5].recipe[6]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 25,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "Distilled water", "compound_id": 4, "amount": 25, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact Pfennig's heterotrophic salts solution recipe-stage quantity. Bare ml amounts remain batch/addition quantities; only explicitly printed ml/l is a provider per-litre declaration. Water rows are not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Rebuild the absent named solution/water topology with this exact stage. Retain existing preparation text as separately credited.", "missing": true}]}, {"quantity_id": "q42", "topic": "DSM28 source-only Vitamin B12 solution: Distilled water", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[6].recipe[1]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Distilled water", "compound_id": 4, "amount": 100, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact Vitamin B12 solution recipe-stage quantity. Bare ml amounts remain batch/addition quantities; only explicitly printed ml/l is a provider per-litre declaration. Water rows are not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Rebuild the absent named solution/water topology with this exact stage. Retain existing preparation text as separately credited.", "missing": true}]}, {"quantity_id": "q43", "topic": "DSM28 source-only Trace element solution SL-12 B: Distilled water", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[7].recipe[9]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact Trace element solution SL-12 B recipe-stage quantity. Bare ml amounts remain batch/addition quantities; only explicitly printed ml/l is a provider per-litre declaration. Water rows are not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Rebuild the absent named solution/water topology with this exact stage. Retain existing preparation text as separately credited.", "missing": true}]}, {"quantity_id": "q44", "topic": "DSM28 source-only Neutralized sulfide solution 3% (w/v): Distilled water", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[8].recipe[1]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Distilled water", "compound_id": 4, "amount": 100, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact Neutralized sulfide solution 3% (w/v) recipe-stage quantity. Bare ml amounts remain batch/addition quantities; only explicitly printed ml/l is a provider per-litre declaration. Water rows are not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Rebuild the absent named solution/water topology with this exact stage. Retain existing preparation text as separately credited.", "missing": true}]}, {"quantity_id": "q45", "topic": "Retained DSM421 owner preparation step 1", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T09:27:43.186753Z", "quote": "{\n                        \"step\": \"Supplement medium 28 with NaCl (10%), MgCl2 x 6 H2O (0.3%) Na-acetate (0.05%) and sodium thiosulfate (0.05%). Incubate at 500 to 1000 Lux light intensity.\"\n                    }", "exact_decoded_object": {"step": "Supplement medium 28 with NaCl (10%), MgCl2 x 6 H2O (0.3%) Na-acetate (0.05%) and sodium thiosulfate (0.05%). Incubate at 500 to 1000 Lux light intensity."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path": "preparation_steps[0].description", "stored_value": "Supplement medium 28 with NaCl (10%), MgCl2 x 6 H2O (0.3%) Na-acetate (0.05%) and sodium thiosulfate (0.05%). Incubate at 500 to 1000 Lux light intensity.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q46", "topic": "Retained DSM421 owner preparation step 2", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52", "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T09:27:43.186753Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"step\": \"Adjust the pH with filter-sterilised 1M Na2CO3 to 7.1-7.3.\"\n                    }", "exact_decoded_object": {"recipe_order": 7, "step": "Adjust the pH with filter-sterilised 1M Na2CO3 to 7.1-7.3."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path": "preparation_steps[1].description", "stored_value": "Adjust the pH with filter-sterilised 1M Na2CO3 to 7.1-7.3.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q47", "topic": "Retained DSM421 owner preparation step 3", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52", "locator": "$.data.solutions[1].steps[1]", "accessed_at": "2026-10-28T09:27:43.186753Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"step\": \"If needed, aliquot into sterile, N&lt;sub&gt;2&lt;/sub&gt; gassed screw-cap tubes under N&lt;sub&gt;2&lt;/sub&gt; gas.\"\n                    }", "exact_decoded_object": {"recipe_order": 7, "step": "If needed, aliquot into sterile, N&lt;sub&gt;2&lt;/sub&gt; gassed screw-cap tubes under N&lt;sub&gt;2&lt;/sub&gt; gas."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path": "preparation_steps[2].description", "stored_value": "If needed, aliquot into sterile, N&lt;sub&gt;2&lt;/sub&gt; gassed screw-cap tubes under N&lt;sub&gt;2&lt;/sub&gt; gas.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q48", "topic": "Retained DSM421 owner preparation step 4", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52", "locator": "$.data.solutions[1].steps[2]", "accessed_at": "2026-10-28T09:27:43.186753Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"step\": \"During the first 24 h, the iron of the medium precipitates in the form of black flocks. No other sediment should arise in the otherwise clear medium.\"\n                    }", "exact_decoded_object": {"recipe_order": 7, "step": "During the first 24 h, the iron of the medium precipitates in the form of black flocks. No other sediment should arise in the otherwise clear medium."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path": "preparation_steps[3].description", "stored_value": "During the first 24 h, the iron of the medium precipitates in the form of black flocks. No other sediment should arise in the otherwise clear medium.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q49", "topic": "Retained DSM421 owner preparation step 5", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52", "locator": "$.data.solutions[1].steps[3]", "accessed_at": "2026-10-28T09:27:43.186753Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"step\": \"Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121\\u00b0C for 15 min (as decribed below).\"\n                    }", "exact_decoded_object": {"recipe_order": 2, "step": "Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121°C for 15 min (as decribed below)."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path": "preparation_steps[4].description", "stored_value": "Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121°C for 15 min (as decribed below).", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q50", "topic": "Retained DSM421 owner preparation step 6", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52", "locator": "$.data.solutions[1].steps[4]", "accessed_at": "2026-10-28T09:27:43.186753Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"step\": \"Prepare the following solutions (resazurin, bicarbonate and Pfennig's heterotrophic salts) and sterilize as given below.\"\n                    }", "exact_decoded_object": {"recipe_order": 2, "step": "Prepare the following solutions (resazurin, bicarbonate and Pfennig's heterotrophic salts) and sterilize as given below."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path": "preparation_steps[5].description", "stored_value": "Prepare the following solutions (resazurin, bicarbonate and Pfennig's heterotrophic salts) and sterilize as given below.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q51", "topic": "Retained DSM421 owner preparation step 7", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52", "locator": "$.data.solutions[1].steps[5]", "accessed_at": "2026-10-28T09:27:43.186753Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"step\": \"Add bicarbonate solution and Pfennig's heterotrophic salts to the resazurin (complete volumina, i.e. 50 mL bicarbonate solution and 26 mL Pfennig's heterotrophic salts solution). Bubble with CO2 in an ice bath under sterile conditions.\"\n                    }", "exact_decoded_object": {"recipe_order": 5, "step": "Add bicarbonate solution and Pfennig's heterotrophic salts to the resazurin (complete volumina, i.e. 50 mL bicarbonate solution and 26 mL Pfennig's heterotrophic salts solution). Bubble with CO2 in an ice bath under sterile conditions."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path": "preparation_steps[6].description", "stored_value": "Add bicarbonate solution and Pfennig's heterotrophic salts to the resazurin (complete volumina, i.e. 50 mL bicarbonate solution and 26 mL Pfennig's heterotrophic salts solution). Bubble with CO2 in an ice bath under sterile conditions.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q52", "topic": "Retained DSM421 owner preparation step 8", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52", "locator": "$.data.solutions[1].steps[6]", "accessed_at": "2026-10-28T09:27:43.186753Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"step\": \"Fill 50 ml of this mixture to each bottle of solution A (46 mL + 50 mL).\"\n                    }", "exact_decoded_object": {"recipe_order": 5, "step": "Fill 50 ml of this mixture to each bottle of solution A (46 mL + 50 mL)."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path": "preparation_steps[7].description", "stored_value": "Fill 50 ml of this mixture to each bottle of solution A (46 mL + 50 mL).", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q53", "topic": "Retained DSM421 owner preparation step 9", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52", "locator": "$.data.solutions[1].steps[7]", "accessed_at": "2026-10-28T09:27:43.186753Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"step\": \"Before use, add 4 ml sulfide solution (1.5%) and 0.1 ml Vitamin B12 solution to each 100 mL bottle.\"\n                    }", "exact_decoded_object": {"recipe_order": 5, "step": "Before use, add 4 ml sulfide solution (1.5%) and 0.1 ml Vitamin B12 solution to each 100 mL bottle."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path": "preparation_steps[8].description", "stored_value": "Before use, add 4 ml sulfide solution (1.5%) and 0.1 ml Vitamin B12 solution to each 100 mL bottle.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q54", "topic": "Retained DSM421 owner preparation step 10", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52", "locator": "$.data.solutions[1].steps[8]", "accessed_at": "2026-10-28T09:27:43.186753Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"step\": \"Feed the actively growing culture periodically with neutralized 3% solution of sodium sulfide (use 1 -3 mL/100 mL depending on strain and cultivation stage) to replenish sulfide and with other supplement solutions (see Ref. 3365).\"\n                    }", "exact_decoded_object": {"recipe_order": 7, "step": "Feed the actively growing culture periodically with neutralized 3% solution of sodium sulfide (use 1 -3 mL/100 mL depending on strain and cultivation stage) to replenish sulfide and with other supplement solutions (see Ref. 3365)."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "conflict", "rationale": "The current provider supplies variable1–3 ml/100 ml feeding, while the primary gives only periodic feeding and the provider also has a10 ml row. Retain the discrepancy; no universal fixed dose is selected.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path": "preparation_steps[9].description", "stored_value": "Feed the actively growing culture periodically with neutralized 3% solution of sodium sulfide (use 1 -3 mL/100 mL depending on strain and cultivation stage) to replenish sulfide and with other supplement solutions (see Ref. 3365).", "decision": "conflict", "rationale": "The current provider supplies variable1–3 ml/100 ml feeding, while the primary gives only periodic feeding and the provider also has a10 ml row. Retain the discrepancy; no universal fixed dose is selected."}]}, {"quantity_id": "q55", "topic": "Retained DSM421 owner preparation step 11", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52", "locator": "$.data.solutions[2].steps[0]", "accessed_at": "2026-10-28T09:27:43.186753Z", "quote": "{\n                        \"step\": \"The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at 121\\u00b0C. After cooling to room temperature the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle.\"\n                    }", "exact_decoded_object": {"step": "The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at 121°C. After cooling to room temperature the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path": "preparation_steps[10].description", "stored_value": "The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at 121°C. After cooling to room temperature the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q56", "topic": "Retained DSM28 base preparation step 1", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"step\": \"Adjust the pH with filter-sterilised 1M Na2CO3 to 7.1-7.3.\"\n                    }", "exact_decoded_object": {"recipe_order": 7, "step": "Adjust the pH with filter-sterilised 1M Na2CO3 to 7.1-7.3."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps[0].description", "stored_value": "Adjust the pH with filter-sterilised 1M Na2CO3 to 7.1-7.3.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q57", "topic": "Retained DSM28 base preparation step 2", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[0].steps[1]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"step\": \"If needed, aliquot into sterile, N&lt;sub&gt;2&lt;/sub&gt; gassed screw-cap tubes under N&lt;sub&gt;2&lt;/sub&gt; gas.\"\n                    }", "exact_decoded_object": {"recipe_order": 7, "step": "If needed, aliquot into sterile, N&lt;sub&gt;2&lt;/sub&gt; gassed screw-cap tubes under N&lt;sub&gt;2&lt;/sub&gt; gas."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps[1].description", "stored_value": "If needed, aliquot into sterile, N&lt;sub&gt;2&lt;/sub&gt; gassed screw-cap tubes under N&lt;sub&gt;2&lt;/sub&gt; gas.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q58", "topic": "Retained DSM28 base preparation step 3", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[0].steps[2]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"step\": \"During the first 24 h, the iron of the medium precipitates in the form of black flocks. No other sediment should arise in the otherwise clear medium.\"\n                    }", "exact_decoded_object": {"recipe_order": 7, "step": "During the first 24 h, the iron of the medium precipitates in the form of black flocks. No other sediment should arise in the otherwise clear medium."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps[2].description", "stored_value": "During the first 24 h, the iron of the medium precipitates in the form of black flocks. No other sediment should arise in the otherwise clear medium.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q59", "topic": "Retained DSM28 base preparation step 4", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[0].steps[3]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"step\": \"Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121\\u00b0C for 15 min (as decribed below).\"\n                    }", "exact_decoded_object": {"recipe_order": 2, "step": "Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121°C for 15 min (as decribed below)."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps[3].description", "stored_value": "Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121°C for 15 min (as decribed below).", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q60", "topic": "Retained DSM28 base preparation step 5", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[0].steps[4]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"step\": \"Prepare the following solutions (resazurin, bicarbonate and Pfennig's heterotrophic salts) and sterilize as given below.\"\n                    }", "exact_decoded_object": {"recipe_order": 2, "step": "Prepare the following solutions (resazurin, bicarbonate and Pfennig's heterotrophic salts) and sterilize as given below."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps[4].description", "stored_value": "Prepare the following solutions (resazurin, bicarbonate and Pfennig's heterotrophic salts) and sterilize as given below.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q61", "topic": "Retained DSM28 base preparation step 6", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[0].steps[5]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"step\": \"Add bicarbonate solution and Pfennig's heterotrophic salts to the resazurin (complete volumina, i.e. 50 mL bicarbonate solution and 26 mL Pfennig's heterotrophic salts solution). Bubble with CO2 in an ice bath under sterile conditions.\"\n                    }", "exact_decoded_object": {"recipe_order": 5, "step": "Add bicarbonate solution and Pfennig's heterotrophic salts to the resazurin (complete volumina, i.e. 50 mL bicarbonate solution and 26 mL Pfennig's heterotrophic salts solution). Bubble with CO2 in an ice bath under sterile conditions."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps[5].description", "stored_value": "Add bicarbonate solution and Pfennig's heterotrophic salts to the resazurin (complete volumina, i.e. 50 mL bicarbonate solution and 26 mL Pfennig's heterotrophic salts solution). Bubble with CO2 in an ice bath under sterile conditions.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q62", "topic": "Retained DSM28 base preparation step 7", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[0].steps[6]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"step\": \"Fill 50 ml of this mixture to each bottle of solution A (46 mL + 50 mL).\"\n                    }", "exact_decoded_object": {"recipe_order": 5, "step": "Fill 50 ml of this mixture to each bottle of solution A (46 mL + 50 mL)."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps[6].description", "stored_value": "Fill 50 ml of this mixture to each bottle of solution A (46 mL + 50 mL).", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q63", "topic": "Retained DSM28 base preparation step 8", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[0].steps[7]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"step\": \"Before use, add 4 ml sulfide solution (1.5%) and 0.1 ml Vitamin B12 solution to each 100 mL bottle.\"\n                    }", "exact_decoded_object": {"recipe_order": 5, "step": "Before use, add 4 ml sulfide solution (1.5%) and 0.1 ml Vitamin B12 solution to each 100 mL bottle."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps[7].description", "stored_value": "Before use, add 4 ml sulfide solution (1.5%) and 0.1 ml Vitamin B12 solution to each 100 mL bottle.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q64", "topic": "Retained DSM28 base preparation step 9", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[0].steps[8]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"step\": \"Feed the actively growing culture periodically with neutralized 3% solution of sodium sulfide (use 1 -3 mL/100 mL depending on strain and cultivation stage) to replenish sulfide and with other supplement solutions (see Ref. 3365).\"\n                    }", "exact_decoded_object": {"recipe_order": 7, "step": "Feed the actively growing culture periodically with neutralized 3% solution of sodium sulfide (use 1 -3 mL/100 mL depending on strain and cultivation stage) to replenish sulfide and with other supplement solutions (see Ref. 3365)."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "conflict", "rationale": "The current provider supplies variable1–3 ml/100 ml feeding, while the primary gives only periodic feeding and the provider also has a10 ml row. Retain the discrepancy; no universal fixed dose is selected.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps[8].description", "stored_value": "Feed the actively growing culture periodically with neutralized 3% solution of sodium sulfide (use 1 -3 mL/100 mL depending on strain and cultivation stage) to replenish sulfide and with other supplement solutions (see Ref. 3365).", "decision": "conflict", "rationale": "The current provider supplies variable1–3 ml/100 ml feeding, while the primary gives only periodic feeding and the provider also has a10 ml row. Retain the discrepancy; no universal fixed dose is selected."}]}, {"quantity_id": "q65", "topic": "Retained DSM28 base preparation step 10", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"step\": \"Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121\\u00b0C for 15 min.\"\n                    }", "exact_decoded_object": {"step": "Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121°C for 15 min."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps[9].description", "stored_value": "Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121°C for 15 min.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q66", "topic": "Retained DSM28 base preparation step 11", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[2].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"step\": \"Prepare in a screw-cap bottle, bubble with N2 to replace air, close tightly and autoclave.\"\n                    }", "exact_decoded_object": {"step": "Prepare in a screw-cap bottle, bubble with N2 to replace air, close tightly and autoclave."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps[10].description", "stored_value": "Prepare in a screw-cap bottle, bubble with N2 to replace air, close tightly and autoclave.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q67", "topic": "Retained DSM28 base preparation step 12", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[3].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"step\": \"Bubble with CO2 and filter sterilize into sterile, gas-tight, 100 ml screw-cap bottle.\"\n                    }", "exact_decoded_object": {"step": "Bubble with CO2 and filter sterilize into sterile, gas-tight, 100 ml screw-cap bottle."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps[11].description", "stored_value": "Bubble with CO2 and filter sterilize into sterile, gas-tight, 100 ml screw-cap bottle.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q68", "topic": "Retained DSM28 base preparation step 13", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[4].steps[1]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"step\": \"Autoclave in a cotton-stoppered Erlenmeyer flask with an outlet tube for medium, connected to a glass outlet at the bottom of the vessel and has, at the other end, a silicon rubber tube with a pinch cock and a bell for aseptic dispensing of the medium into bottles.\"\n                    }", "exact_decoded_object": {"step": "Autoclave in a cotton-stoppered Erlenmeyer flask with an outlet tube for medium, connected to a glass outlet at the bottom of the vessel and has, at the other end, a silicon rubber tube with a pinch cock and a bell for aseptic dispensing of the medium into bottles."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps[12].description", "stored_value": "Autoclave in a cotton-stoppered Erlenmeyer flask with an outlet tube for medium, connected to a glass outlet at the bottom of the vessel and has, at the other end, a silicon rubber tube with a pinch cock and a bell for aseptic dispensing of the medium into bottles.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q69", "topic": "Retained DSM28 base preparation step 14", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[4].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"step\": \"Cool to room temperature under an atmosphere of N2/CO2 in an ice bath.\"\n                    }", "exact_decoded_object": {"step": "Cool to room temperature under an atmosphere of N2/CO2 in an ice bath."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps[13].description", "stored_value": "Cool to room temperature under an atmosphere of N2/CO2 in an ice bath.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q70", "topic": "Retained DSM28 base preparation step 15", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[5].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"step\": \"Filter sterilize into sterile, gas-tight, 100 ml screw-cap bottle.\"\n                    }", "exact_decoded_object": {"step": "Filter sterilize into sterile, gas-tight, 100 ml screw-cap bottle."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps[14].description", "stored_value": "Filter sterilize into sterile, gas-tight, 100 ml screw-cap bottle.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q71", "topic": "Retained DSM28 base preparation step 16", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[6].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"step\": \"Filter sterilized\"\n                    }", "exact_decoded_object": {"step": "Filter sterilized"}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps[15].description", "stored_value": "Filter sterilized", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q72", "topic": "Retained DSM28 base preparation step 17", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[7].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"step\": \"Adjust pH to 6.0.\"\n                    }", "exact_decoded_object": {"step": "Adjust pH to 6.0."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps[16].description", "stored_value": "Adjust pH to 6.0.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q73", "topic": "Retained DSM28 base preparation step 18", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[8].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"step\": \"The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at 121\\u00b0C. After cooling to room temperature the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle.\"\n                    }", "exact_decoded_object": {"step": "The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at 121°C. After cooling to room temperature the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps[17].description", "stored_value": "The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at 121°C. After cooling to room temperature the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle.", "decision": "evidence_only", "rationale": "The current provider exactly supports this retained description at its stated solution/preparation stage. Keep the existing instruction and add scoped root evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id": "q74", "topic": "Restore the omitted421 instruction in generated/KOMODO layers", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T09:27:43.186753Z", "quote": "{\n                        \"step\": \"Supplement medium 28 with NaCl (10%), MgCl2 x 6 H2O (0.3%) Na-acetate (0.05%) and sodium thiosulfate (0.05%). Incubate at 500 to 1000 Lux light intensity.\"\n                    }", "exact_decoded_object": {"step": "Supplement medium 28 with NaCl (10%), MgCl2 x 6 H2O (0.3%) Na-acetate (0.05%) and sodium thiosulfate (0.05%). Incubate at 500 to 1000 Lux light intensity."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm421", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium421.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm421.bin", "raw_sha256": "147737ed0bfdd97948c86a691a34151f6e28a89687ab665b857bdd210f385ccc", "locator": "Complete421 primary instruction", "accessed_at": "2026-10-28T09:27:43.389676Z", "quote": "421. CHROMATIUM SALEXIGENS MEDIUM\n\nSupplement medium 28 with NaCl (10%), MgCl 2 x 6 H2O (0.3%) Na-acetate (0.05%)\nand sodium thiosulfate (0.05%). Incubate at 500 to 1000 Lux light intensity."}], "decision": "add", "rationale": "Preserve the DSM owner repair; do not claim that all three layers lack preparation.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "The generated/KOMODO layer lacks the explicit supplement and500–1000 Lux instruction. Add only source-scoped instructions; the DSM contributor already retains them.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "The generated/KOMODO layer lacks the explicit supplement and500–1000 Lux instruction. Add only source-scoped instructions; the DSM contributor already retains them.", "missing": true}]}, {"quantity_id": "q75", "topic": "Inherited base pH range and1M adjuster", "source": [{"evidence_id": "dsm28", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm28.bin", "raw_sha256": "442636c7b32c8f6de4a54fd8acaaa22f8e1a130f3d4b45af59d5782fe77a6c3d", "locator": "PDF extracted line 77; visually checked page", "accessed_at": "2026-10-28T09:27:43.589061Z", "quote": "Adjust the pH with filter-sterilised 1M Na2CO3 to 7.1-7.3."}, {"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"step\": \"Adjust the pH with filter-sterilised 1M Na2CO3 to 7.1-7.3.\"\n                    }", "exact_decoded_object": {"recipe_order": 7, "step": "Adjust the pH with filter-sterilised 1M Na2CO3 to 7.1-7.3."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "The source specifies1M sodium carbonate and pH7.1–7.3 for assembled base28; no titrant volume is supplied.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ph_range", "stored_value": {"min": 7.1, "max": 7.3}, "decision": "evidence_only", "rationale": "The existing range7.1–7.3 is supported for base28; retain its explicit source stage."}, {"path": "data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml", "field_path": "ph_range", "stored_value": null, "decision": "add", "rationale": "Record the inherited base range with the explicit421→28 cross-reference and preserve an absent421-specific override; do not invent a separate value.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml", "field_path": "ph_range", "stored_value": null, "decision": "add", "rationale": "Record the inherited base range with the explicit421→28 cross-reference and preserve an absent421-specific override; do not invent a separate value.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path": "ph_range", "stored_value": null, "decision": "add", "rationale": "Record the inherited base range with the explicit421→28 cross-reference and preserve an absent421-specific override; do not invent a separate value.", "missing": true}]}, {"quantity_id": "q76", "topic": "Conflicting conditional marine-base formulations", "source": [{"evidence_id": "dsm28", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm28.bin", "raw_sha256": "442636c7b32c8f6de4a54fd8acaaa22f8e1a130f3d4b45af59d5782fe77a6c3d", "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T09:27:43.589061Z", "quote": "(For marine or estuarine isolates add 100.0 g NaCl to this solution and increase the\nMgSO4 x 7 H2O to 15.0 g)."}, {"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3", "locator": "$.data.solutions[0].steps[9]", "accessed_at": "2026-10-28T09:27:43.365556Z", "quote": "{\n                        \"step\": \"Note: for marine species use 1-3% NaCl and increase the amount of MgSO4 7*H2O to 2,8g/L\"\n                    }", "exact_decoded_object": {"step": "Note: for marine species use 1-3% NaCl and increase the amount of MgSO4 7*H2O to 2,8g/L"}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "conflict", "rationale": "Preserve both exact conditional variants and report their conflict. The medium name is not evidence that a strain-specific marine override applies.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps", "stored_value": [{"step_number": 1, "action": "FILTER_STERILIZE", "description": "Adjust the pH with filter-sterilised 1M Na2CO3 to 7.1-7.3."}, {"step_number": 2, "action": "ALIQUOT", "description": "If needed, aliquot into sterile, N&lt;sub&gt;2&lt;/sub&gt; gassed screw-cap tubes under N&lt;sub&gt;2&lt;/sub&gt; gas."}, {"step_number": 3, "action": "MIX", "description": "During the first 24 h, the iron of the medium precipitates in the form of black flocks. No other sediment should arise in the otherwise clear medium."}, {"step_number": 4, "action": "AUTOCLAVE", "description": "Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121°C for 15 min (as decribed below)."}, {"step_number": 5, "action": "MIX", "description": "Prepare the following solutions (resazurin, bicarbonate and Pfennig's heterotrophic salts) and sterilize as given below."}, {"step_number": 6, "action": "COOL", "description": "Add bicarbonate solution and Pfennig's heterotrophic salts to the resazurin (complete volumina, i.e. 50 mL bicarbonate solution and 26 mL Pfennig's heterotrophic salts solution). Bubble with CO2 in an ice bath under sterile conditions."}, {"step_number": 7, "action": "MIX", "description": "Fill 50 ml of this mixture to each bottle of solution A (46 mL + 50 mL)."}, {"step_number": 8, "action": "MIX", "description": "Before use, add 4 ml sulfide solution (1.5%) and 0.1 ml Vitamin B12 solution to each 100 mL bottle."}, {"step_number": 9, "action": "MIX", "description": "Feed the actively growing culture periodically with neutralized 3% solution of sodium sulfide (use 1 -3 mL/100 mL depending on strain and cultivation stage) to replenish sulfide and with other supplement solutions (see Ref. 3365)."}, {"step_number": 10, "action": "AUTOCLAVE", "description": "Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121°C for 15 min."}, {"step_number": 11, "action": "AUTOCLAVE", "description": "Prepare in a screw-cap bottle, bubble with N2 to replace air, close tightly and autoclave."}, {"step_number": 12, "action": "FILTER_STERILIZE", "description": "Bubble with CO2 and filter sterilize into sterile, gas-tight, 100 ml screw-cap bottle."}, {"step_number": 13, "action": "AUTOCLAVE", "description": "Autoclave in a cotton-stoppered Erlenmeyer flask with an outlet tube for medium, connected to a glass outlet at the bottom of the vessel and has, at the other end, a silicon rubber tube with a pinch cock and a bell for aseptic dispensing of the medium into bottles."}, {"step_number": 14, "action": "COOL", "description": "Cool to room temperature under an atmosphere of N2/CO2 in an ice bath."}, {"step_number": 15, "action": "FILTER_STERILIZE", "description": "Filter sterilize into sterile, gas-tight, 100 ml screw-cap bottle."}, {"step_number": 16, "action": "FILTER_STERILIZE", "description": "Filter sterilized"}, {"step_number": 17, "action": "ADJUST_PH", "description": "Adjust pH to 6.0."}, {"step_number": 18, "action": "AUTOCLAVE", "description": "The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at 121°C. After cooling to room temperature the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle."}], "decision": "unsupported", "rationale": "The primary conditional100 gNaCl/15 gMgSO4hept instruction and current API1–3%NaCl/2.8g/L statement are distinct source versions. Do not combine either automatically with421’s10% supplement."}]}, {"quantity_id": "q77", "topic": "Additional primary feeding-stock pH indicator/context", "source": [{"evidence_id": "dsm28", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf", "raw_path": "REVIEW_WORK/batch062/source01-03/dsm28.bin", "raw_sha256": "442636c7b32c8f6de4a54fd8acaaa22f8e1a130f3d4b45af59d5782fe77a6c3d", "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T09:27:43.589061Z", "quote": "Appearance of a yellow colour indicates the drop of pH to about 8. The solution should\nbe stirred continuously to avoid precipitation of elemental sulfur. The final solution\nshould be clear and is yellow in colour."}], "decision": "add", "rationale": "The primary preparation includes pH~8 indicator context absent from the current provider step; it does not replace final feeding-stock pH~7 or base pH7.1–7.3.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "preparation_steps", "stored_value": [{"step_number": 1, "action": "FILTER_STERILIZE", "description": "Adjust the pH with filter-sterilised 1M Na2CO3 to 7.1-7.3."}, {"step_number": 2, "action": "ALIQUOT", "description": "If needed, aliquot into sterile, N&lt;sub&gt;2&lt;/sub&gt; gassed screw-cap tubes under N&lt;sub&gt;2&lt;/sub&gt; gas."}, {"step_number": 3, "action": "MIX", "description": "During the first 24 h, the iron of the medium precipitates in the form of black flocks. No other sediment should arise in the otherwise clear medium."}, {"step_number": 4, "action": "AUTOCLAVE", "description": "Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121°C for 15 min (as decribed below)."}, {"step_number": 5, "action": "MIX", "description": "Prepare the following solutions (resazurin, bicarbonate and Pfennig's heterotrophic salts) and sterilize as given below."}, {"step_number": 6, "action": "COOL", "description": "Add bicarbonate solution and Pfennig's heterotrophic salts to the resazurin (complete volumina, i.e. 50 mL bicarbonate solution and 26 mL Pfennig's heterotrophic salts solution). Bubble with CO2 in an ice bath under sterile conditions."}, {"step_number": 7, "action": "MIX", "description": "Fill 50 ml of this mixture to each bottle of solution A (46 mL + 50 mL)."}, {"step_number": 8, "action": "MIX", "description": "Before use, add 4 ml sulfide solution (1.5%) and 0.1 ml Vitamin B12 solution to each 100 mL bottle."}, {"step_number": 9, "action": "MIX", "description": "Feed the actively growing culture periodically with neutralized 3% solution of sodium sulfide (use 1 -3 mL/100 mL depending on strain and cultivation stage) to replenish sulfide and with other supplement solutions (see Ref. 3365)."}, {"step_number": 10, "action": "AUTOCLAVE", "description": "Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121°C for 15 min."}, {"step_number": 11, "action": "AUTOCLAVE", "description": "Prepare in a screw-cap bottle, bubble with N2 to replace air, close tightly and autoclave."}, {"step_number": 12, "action": "FILTER_STERILIZE", "description": "Bubble with CO2 and filter sterilize into sterile, gas-tight, 100 ml screw-cap bottle."}, {"step_number": 13, "action": "AUTOCLAVE", "description": "Autoclave in a cotton-stoppered Erlenmeyer flask with an outlet tube for medium, connected to a glass outlet at the bottom of the vessel and has, at the other end, a silicon rubber tube with a pinch cock and a bell for aseptic dispensing of the medium into bottles."}, {"step_number": 14, "action": "COOL", "description": "Cool to room temperature under an atmosphere of N2/CO2 in an ice bath."}, {"step_number": 15, "action": "FILTER_STERILIZE", "description": "Filter sterilize into sterile, gas-tight, 100 ml screw-cap bottle."}, {"step_number": 16, "action": "FILTER_STERILIZE", "description": "Filter sterilized"}, {"step_number": 17, "action": "ADJUST_PH", "description": "Adjust pH to 6.0."}, {"step_number": 18, "action": "AUTOCLAVE", "description": "The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at 121°C. After cooling to room temperature the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle."}], "decision": "add", "rationale": "Preserve the primary-only pH~8 yellow-colour indicator, stirring and appearance as feeding-stock context, not a target-medium pH or organism-growth assertion."}]}]

### Current ontology and MIM correspondence

grounding: concern. Targets: CultureMech:005246.

The selected five primary/secondary CHEBI pairs resolve with current canonical labels and source forms. The separately scoped base has a confirmed nickel-hydrate mismatch, current-negative legacy000399 and missing mixture/secondary links; EDTA hydration remains unspecified. All recursive identities and current preferred/synonym rows are retained without treating medium IDs as failed chemical IDs.

### History and evidence scope

provenance: concern. Targets: CultureMech:005246.

Five exact current-record historical reports and the selected pair/method of the large source-duplicate report were read. Most old API421 quoted objects match current bytes; the neutralized-sulfide object now adds g_l/mmol_l and the full old raw digest differs. Exact current KOMODO mapping/medium routes returned403. Preserve these distinctions and all original events; no historical timestamp or execution is reconstructed.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:005246.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:005246.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Restore the required base and isolate the feeding stock

major / open / confirmed; issue key: culturemech-005246-restore-the-required-base-and-isolate-the-feeding-stock.

DSM421 supplements medium28; no local layer has the necessary base/solution topology. The four supplement rates match explicit current provider g_l declarations, but30 g/L sodium sulfide is the neutralized feeding-stock strength. Restore the base and feeding stages without flattening or choosing a fixed feed from conflicting source variants.

### f2: Repair the referenced base before transferring it

major / open / confirmed; issue key: culturemech-005246-repair-the-referenced-base-before-transferring-it.

The separately inspected DSM28 dependency is itself flattened: all22 direct fields represent stock constituents, and44.8148 g/L sulfide is a sum of two different stock bases. Current providerE omits primary pyruvate/dextrose; their local per-litre rates remain unsupported. Resazurin has an unresolved percentage basis. These dependency findings do not assert that its22 ingredients already occur in the selected target.

### f3: Preserve the DSM owner preparation during regeneration

major / open / confirmed; issue key: culturemech-005246-preserve-the-dsm-owner-preparation-during-regeneration.

The DSM contributor already contains11 source-supported preparation descriptions, while generated/KOMODO layers omit them. Base-stock steps are concatenated and require stage labels; the inherited pH range and root evidence are absent. Current resolver omits preparation/range/evidence, and current merge compatibility rejects unequal scientific content; neither proves the old run. Preserve the source-duplicate relationship without forcing an incompatible merge.

### f4: Reconcile the scoped base hydrate and legacy linkage

minor / open / confirmed; issue key: culturemech-005246-reconcile-the-scoped-base-hydrate-and-legacy-linkage.

In DSM28 only, NiCl2 x6 H2O points to valid34887 nickel dichloride rather than verified53542 hexahydrate. Pyruvate’s primary50144 is valid while secondary MediaIngredientMech000399 is absent from the current packaged catalog; absence is not proof of historical invalidity. Yeast lacks linkage and manganese131395 lacks its secondary link. EDTA hydration is unspecified, so anhydrous64734 remains an unverified specificity.

### f5: Keep historical defects and unresolved evidence append-only

minor / open / confirmed; issue key: culturemech-005246-keep-historical-defects-and-unresolved-evidence-append-only.

The selected/KOMODO history contains a literal malformed.fZ timestamp and a separate timezone-unspecified resolver timestamp. Do not rewrite either event. The exact current KOMODO routes failed403; the old selected mapping row remains derivative. Most oldAPI421 objects still match, but its sulfide object changed and the complete old raw digest is not authenticated by today’s capture.

## Recommended Actions And Acceptance Checks

### action1

Retain the four source-supported supplement rates, create an explicitly scoped base28 dependency and separate the30 g/L feeding stock. Reconcile source-version conflicts before declaring a complete final formulation; do not infer a final volume or feed dose.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Curate the explicitly referenced DSM28 stock topology with separate A–F,SL12B and feeding stages. Preserve source batch amounts and primary/provider differences; remove the invalid sum only through an evidence-backed owner repair and do not export stock strengths as421 final rates.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Retain the DSM contributor’s supported instructions, add only missing scoped root evidence and source-stage structure, then reconcile compatible owner content before regeneration. Keep source-duplicate provenance distinct from complete formulation equivalence.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action4

Before base reuse, verify the nickel hydrate in both slots and refresh the exact pyruvate secondary linkage through current authority evidence. Preserve legacy history and unresolved EDTA specificity; do not treat current catalog status as historical proof.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action5

Preserve every original event and failed capture. Append verified source/context evidence and, only if authoritative event provenance is recovered, a new correction event; never silently rewrite the malformed or timezone-unspecified timestamps.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-2 | data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| identity-search | REVIEW_WORK/batch062/record01/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| historical-1 | reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md; Selected salexigens pair at line377 plus report purpose/method and validation claims only; other651 pair-specific conclusions are outside scope. | context_only | Selected exact reciprocal DSM421/KOMODO421 relationship row and method support a historical source-duplicate annotation, not current formulation completeness or preparation equality. Other pairs are outside scope. |
| historical-2 | reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-3 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/chromatium_salexigens_medium.yaml.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-4 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-5 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-6 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chromatium_salexigens_medium.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-reader | REVIEW_WORK/batch062/record01/historical-reader.json | context_only | Full exact-header historical texts and scoped large report, with literal/decoded current-source joins and explicit mismatches. Historical access events are not reauthenticated. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _parse_api_solutions, _parse_preparation_steps | context_only | Current composition parser restricts ingredients to the primary solution, excludes solvent and recognized stock additions, and retains explicit g_l. The solution parser preserves referenced or percent-defined stocks and source attributes. Preparation parsing still concatenates all solution steps into root preparation_steps; source-stage annotation remains important. These present functions do not prove the historical execution that produced this record. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group copies a sole contributor with merge metadata. For multiple contributors it passes records to merge_formulation_evidence, which checks compatibility; it does not authorize merging different preparation assertions. |
| writer-formulation | src/culturemech/merge/formulation.py; formulation_content, merge_formulation_evidence | context_only | Current compatibility preserves scientific fields and list order and rejects unequal formulations; only specified provenance/evidence lists are unioned. It performs no concentration conversion or stock expansion and does not authenticate historical merges. |
| writer-cleanup | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients, merge_ingredient_group | context_only | Current cleanup groups identical normalized names, keeps the first entry as a base, flags differing concentrations and combines a warning note; it does not sum concentrations. It can still discard distinctions when names repeat, so source stage must be retained. Current behavior does not establish the historical cause of an existing discrepancy. |
| attached-evidence-joins | REVIEW_WORK/batch062/record01/attached-evidence-joins.json | context_only | Every existing attached evidence claim is preserved and compared to the exact freshly captured response. Matching snippets do not authenticate historical access times. |
| base28 | data/normalized_yaml/bacterial/pfennigs_medium_i.yaml; Complete document | context_only | Entire expressly referenced DSM28 base, including all22 concentrations,18 preparation steps, histories and grounding; no unrelated parent transfer. |
| writer-resolver | src/culturemech/enrich/dsmz_resolver.py; merge_composition | context_only | Current merge_composition copies ingredients/solutions/pH value/state/type but not preparation_steps,ph_range or source evidence. This is a current integration boundary, not proof of the historical execution. |
| dsm421 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium421.pdf; Exact source identity and scoped formulation/preparation | supports | Complete primary DSM421 page: supplement medium28 with four bare-percent amounts; the percent basis is not stated.500–1000 Lux is explicitly supplied. |
| api421 | https://mediadive.dsmz.de/rest/medium/421; Exact source identity and scoped formulation/preparation | supports | Complete current provider421 declares the four supplement g_l rates and explicitly references Main28. Its separate neutralized-sulfide solution is30 g/L stock, not a direct final-medium concentration. |
| dsm28 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf; Exact source identity and scoped formulation/preparation | supports | Complete two-page primary DSM28 base, all A–F and SL12B/feeding-stock tables, conditional marine instruction and preparation visually read. Exact printed amounts and source-only rows remain scoped to their solutions. |
| api28 | https://mediadive.dsmz.de/rest/medium/28; Exact source identity and scoped formulation/preparation | supports | Complete current official API28, all nine solution objects and steps read. Provider nominal g_l rates do not resolve primary/provider ingredient or marine-variant conflicts. |
| komodo421 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=421; Exact source identity and scoped formulation/preparation | unknown | The exact historical MediaInfo=421 route returned403. Its challenge body supplies no formulation; old mapping snippets remain historical derivative evidence. |
| komodoList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact source identity and scoped formulation/preparation | unknown | The exact historical MediaList route returned403. The retained old selected mapping row is not a freshly authenticated catalogue response. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53542; Exact source identity and scoped formulation/preparation | supports | Exact current OLS nickel dichloride hexahydrate object verifies the supplied form alternative to valid anhydrous34887; this concerns only the expressly reviewed base dependency. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86345; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32954; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi132112 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_132112; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_76209; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32139; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_8806; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31206; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi62947 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_62947; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi50144 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_50144; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17634; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32588; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63036; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_176843; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi64734 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_64734; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi131395 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131395; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49976; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86318; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch062/record01/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch062/record01/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch062/record01/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch062/record01/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch062/record01/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch062/record01/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch062/record01/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch062/record01/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch062/record01/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- The current primary and provider differ on conditional marine-base salts and omit different solutionE ingredients. Neither version is silently selected or combined with the421 supplement.
- Bare percentages in the421 primary and resazurin reagent have no stated mass/volume basis. Provider g_l declarations are credited only at their named stages, not as independently validated percentage conversions.
- Primary base assembly amounts do not establish an exact final litre. Provider10 ml feeding, variable1–3 ml/100 ml prose and primary unfixed periodic feed remain separate/conflicting.
- Exact KOMODO routes returned403; old mapping/source objects are historical derivative evidence except specifically recorded literal matches. The complete old API421 response digest was not recovered.
- All dependency observations concern the expressly referenced DSM28 record, not an instruction to transfer its raw stocks or conditional species prescriptions into421. No strain growth or optimization claim is made.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T094947Z-batch062-record01-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Chromatium salexigens: restore the required base and distinguish feeding-stock
  strength'
started_at: '2026-10-28T09:27:29.234425Z'
finished_at: '2026-10-28T09:49:47.300430Z'
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
summary: DSM421 explicitly supplements medium28; the local five-ingredient record
  omits that base and misplaces the neutralized-sulfide stock strength as a direct
  rate. Four supplement rates are supported as provider declarations. The DSM owner’s
  substantial preparation must be retained and scoped, while the base dependency’s
  flattened stocks and conflicting primary/provider versions prevent an unqualified
  complete formulation.
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
  - path: data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml
    sha256: 82e28d4a5bfd14e8be56e1e741abce12812517740ca3779d2756f8f816d9d219
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml
    sha256: 31c90d7b01140ed112bcd56de48486dcb9a3bbc47e221a533d33acf2fb2eb578
    role: context
  - path: data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml
    sha256: d2e665f7e81eda0f2d10fc4b3eac2aec6c6f34c7512700eb7b4526f9a777e5f7
    role: context
  - path: data/normalized_yaml/bacterial/pfennigs_medium_i.yaml
    sha256: 331d789551237be004e244b955bdf6f7af18b4bba9b90e4fc85c6948121f5ab9
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
  - path: reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md
    sha256: a723d4b7950bf4ac296a8a7fe4890d4d0881199a5d17c12a5fe39c2afbc40a10
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml.md
    sha256: 4c782048073414873f946a8286eb6aeff925f2c98373adbcec86e812b3bb8d13
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/chromatium_salexigens_medium.yaml.md
    sha256: b1fb7d5c2c084f0e84024874cbb2236e503039e49d7ee3f8d9a706c3ebfb5fa0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.md
    sha256: ca0ce8ea6b88e983ccfc49700158cf234facd94ca82f9911994959187e81ca30
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.md
    sha256: 4c788620999f85c175c83466bf4b26ffbc431a54c0e7525d94e1369c3d19c0b7
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chromatium_salexigens_medium.md
    sha256: ad135e78bf02c5abdd0db6f5f352f0fe7f3be468a50385c2196dfc7da3e5f9c0
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_media_variant_links.py
    sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
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
  - path: scripts/validate_media_variant_links.py
    sha256: d18ef71320a0c50abe085e151d0d0d4d963007d1e1c9afbefab97581a983e31e
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
  selection: Actual batch062 native selection index 01.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:005246
targets:
- target_id: CultureMech:005246
  path: data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml
  label: chromatium_salexigens_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:005246
  command: just validate-schema data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml
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
  - CultureMech:005246
  command: just validate-strict data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml
    --out REVIEW_WORK/batch062/record01/strict.tsv --workers 1
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
  - CultureMech:005246
  command: just validate-terms data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml
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
  - CultureMech:005246
  command: just validate-references data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T09:46:13.103519Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 82e28d4a5bfd14e8be56e1e741abce12812517740ca3779d2756f8f816d9d219
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T09:46:13.103519Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 31c90d7b01140ed112bcd56de48486dcb9a3bbc47e221a533d33acf2fb2eb578
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T09:46:13.103519Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: d2e665f7e81eda0f2d10fc4b3eac2aec6c6f34c7512700eb7b4526f9a777e5f7
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch062/record01/identity-search.json
  accessed_at: '2026-10-28T09:46:13.182502Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems and stable identity resolve the owner;
    excluded namesakes are retained in the census. Similar names and source accessions
    are not promoted to owners.
  snapshot_sha256: a76c3e9c3aef4ceb04f5be5001ee4bcbe4dc4ca1c96cc51a04dc1cd5860321c6
- evidence_id: historical-1
  kind: record_content
  reference: reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md
  locator: Selected salexigens pair at line377 plus report purpose/method and validation
    claims only; other651 pair-specific conclusions are outside scope.
  accessed_at: '2026-10-28T09:46:13.103519Z'
  support: context_only
  summary: Selected exact reciprocal DSM421/KOMODO421 relationship row and method
    support a historical source-duplicate annotation, not current formulation completeness
    or preparation equality. Other pairs are outside scope.
  snapshot_sha256: a723d4b7950bf4ac296a8a7fe4890d4d0881199a5d17c12a5fe39c2afbc40a10
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T09:46:13.103519Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: 4c782048073414873f946a8286eb6aeff925f2c98373adbcec86e812b3bb8d13
- evidence_id: historical-3
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/chromatium_salexigens_medium.yaml.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T09:46:13.103519Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: b1fb7d5c2c084f0e84024874cbb2236e503039e49d7ee3f8d9a706c3ebfb5fa0
- evidence_id: historical-4
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T09:46:13.103519Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: ca0ce8ea6b88e983ccfc49700158cf234facd94ca82f9911994959187e81ca30
- evidence_id: historical-5
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T09:46:13.103519Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: 4c788620999f85c175c83466bf4b26ffbc431a54c0e7525d94e1369c3d19c0b7
- evidence_id: historical-6
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chromatium_salexigens_medium.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T09:46:13.103519Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: ad135e78bf02c5abdd0db6f5f352f0fe7f3be468a50385c2196dfc7da3e5f9c0
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch062/record01/historical-reader.json
  accessed_at: '2026-10-28T09:46:13.187449Z'
  support: context_only
  summary: Full exact-header historical texts and scoped large report, with literal/decoded
    current-source joins and explicit mismatches. Historical access events are not
    reauthenticated.
  snapshot_sha256: a933da835bbc939fb9ca31546b5eff62aa07cf0485ea6da45105f6798f5e0912
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _parse_api_solutions, _parse_preparation_steps
  accessed_at: '2026-10-28T09:46:13.103519Z'
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
  accessed_at: '2026-10-28T09:46:13.103519Z'
  support: context_only
  summary: Current merge_group copies a sole contributor with merge metadata. For
    multiple contributors it passes records to merge_formulation_evidence, which checks
    compatibility; it does not authorize merging different preparation assertions.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content, merge_formulation_evidence
  accessed_at: '2026-10-28T09:46:13.103519Z'
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
  accessed_at: '2026-10-28T09:46:13.103519Z'
  support: context_only
  summary: Current cleanup groups identical normalized names, keeps the first entry
    as a base, flags differing concentrations and combines a warning note; it does
    not sum concentrations. It can still discard distinctions when names repeat, so
    source stage must be retained. Current behavior does not establish the historical
    cause of an existing discrepancy.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: attached-evidence-joins
  kind: record_content
  reference: REVIEW_WORK/batch062/record01/attached-evidence-joins.json
  accessed_at: '2026-10-28T09:46:13.187799Z'
  support: context_only
  summary: Every existing attached evidence claim is preserved and compared to the
    exact freshly captured response. Matching snippets do not authenticate historical
    access times.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: base28
  kind: record_content
  reference: data/normalized_yaml/bacterial/pfennigs_medium_i.yaml
  locator: Complete document
  accessed_at: '2026-10-28T09:46:13.103519Z'
  support: context_only
  summary: Entire expressly referenced DSM28 base, including all22 concentrations,18
    preparation steps, histories and grounding; no unrelated parent transfer.
  snapshot_sha256: 331d789551237be004e244b955bdf6f7af18b4bba9b90e4fc85c6948121f5ab9
- evidence_id: writer-resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: merge_composition
  accessed_at: '2026-10-28T09:46:13.103519Z'
  support: context_only
  summary: Current merge_composition copies ingredients/solutions/pH value/state/type
    but not preparation_steps,ph_range or source evidence. This is a current integration
    boundary, not proof of the historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: dsm421
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium421.pdf
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T09:27:43.389676Z'
  support: supports
  summary: 'Complete primary DSM421 page: supplement medium28 with four bare-percent
    amounts; the percent basis is not stated.500–1000 Lux is explicitly supplied.'
  snapshot_sha256: 147737ed0bfdd97948c86a691a34151f6e28a89687ab665b857bdd210f385ccc
- evidence_id: api421
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/421
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T09:27:43.186753Z'
  support: supports
  summary: Complete current provider421 declares the four supplement g_l rates and
    explicitly references Main28. Its separate neutralized-sulfide solution is30 g/L
    stock, not a direct final-medium concentration.
  snapshot_sha256: d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52
- evidence_id: dsm28
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T09:27:43.589061Z'
  support: supports
  summary: Complete two-page primary DSM28 base, all A–F and SL12B/feeding-stock tables,
    conditional marine instruction and preparation visually read. Exact printed amounts
    and source-only rows remain scoped to their solutions.
  snapshot_sha256: 442636c7b32c8f6de4a54fd8acaaa22f8e1a130f3d4b45af59d5782fe77a6c3d
- evidence_id: api28
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/28
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T09:27:43.365556Z'
  support: supports
  summary: Complete current official API28, all nine solution objects and steps read.
    Provider nominal g_l rates do not resolve primary/provider ingredient or marine-variant
    conflicts.
  snapshot_sha256: bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3
- evidence_id: komodo421
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=421
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T09:27:42.513020Z'
  support: unknown
  summary: The exact historical MediaInfo=421 route returned403. Its challenge body
    supplies no formulation; old mapping snippets remain historical derivative evidence.
  snapshot_sha256: 438593dac74eec7309440468057fc559eb35a3eea96768ab754fe47129cedec3
- evidence_id: komodoList
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T09:27:42.516780Z'
  support: unknown
  summary: The exact historical MediaList route returned403. The retained old selected
    mapping row is not a freshly authenticated catalogue response.
  snapshot_sha256: e37fdad3fd9afe5ff2f11a56afcfe41441c59c33006a395fe4edbac90e142d11
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53542
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T09:27:47.196512Z'
  support: supports
  summary: Exact current OLS nickel dichloride hexahydrate object verifies the supplied
    form alternative to valid anhydrous34887; this concerns only the expressly reviewed
    base dependency.
  snapshot_sha256: 1e444345efd33c02d5050deadd66637cc6dae004c55e6962c62abd172291e526
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:45.403037Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b145f4ff9b90ebb993ff576d9ab35a6c10b7c42a3b99e18feffcc8d75c0e1e50
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86345
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:49.006017Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 015a33a158257cc5cba8a8e62de382053399be060366af5d95074883bb22b86e
- evidence_id: chebi32954
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32954
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:46.190097Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 34c7d0dea7bc001a0a3b3b388138837cb1aba3b252017bc1ff8625b7a3ff655d
- evidence_id: chebi132112
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_132112
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:44.646530Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 65e27e84f62d5cd9aebe13567134d76a6edfafddb0b06715f788d66a0c7f6bb9
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_76209
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:48.411329Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 3eece7d96d2433ff020ece90db55323d138c5c828b78198f91d26b3eafa91f9f
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:48.524475Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: df8f702eb5b9d3e50209bfa2b0c4b6f1db30c116e56a58e348cbd4bf3bc0ebc1
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32139
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:45.941682Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 314c75cd12ea5d1343b4c0bafd40e0ad72c15b19d64f8cb9152000c0d8839f56
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_8806
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:49.583332Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: ceb05e9dd7fba3802d28b34c50bbb604ded87951e4ea3a812739824a84648d72
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31206
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:45.593948Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: c70055293606f21dcdfb72325a4677661b51efb723ba9357efab43f8ec9b03f7
- evidence_id: chebi62947
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_62947
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:47.266126Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: de293a89a98140f99ac1ae2997d02384921f598c6073d24d799ad20c9d921650
- evidence_id: chebi50144
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_50144
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:46.789375Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 5cbd7ac1ce425bbe4d80bc9e815f0bf02693123023342deddf3bb962108bfd10
- evidence_id: chebi17634
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17634
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:44.990023Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 6e02f3cee82012b7f630c04f122676c0029753074a4421cb005301b8bf24cedb
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:45.844386Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 1635f67d01e00cabdef4ed0d9ef6d5383787c56bd0447051deb90ad353b499a2
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32588
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:45.994811Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 8fc333e98ee953346b5c291b9e5765e77d03cc46740a1282af3e5f4ad355de1a
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63036
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:47.733150Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 913baf38abc38dd61f05c5d636fd6532b70a668673a1f5762f290d2b67270164
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_176843
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:45.234092Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 5c42e2236866d0314bc8d45947ddf9eb2fdf6364d08e802b0fb271011cbfe563
- evidence_id: chebi64734
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_64734
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:47.871541Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 169db4b78f8f464430da6982919f8d425063268fbd374b9e7653a8d7aed041d9
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:48.356849Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: e12b865122aab78645385260e1e83ff28f3c45365cb67c9181166628f68974b3
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:47.104419Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 31dc996638b0cc1341ed24fcb38ec344af726c99d376ac94e952210fcb9ed583
- evidence_id: chebi131395
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131395
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:44.617795Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: ca2a44df04c2e63dc0d171208efe25d4ac44e9248a5ac288a7f21cacb8d50a99
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49976
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:46.638173Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2d2305ca671adbbd3b0cc07b2331373a768bb44d41f32f61ba894594ae470eff
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:46.585151Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a43b8268f70ae50c4cfbc53e12bbd195618c521619cfab8f71d3704b338af95b
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:48.135283Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0271a149a298ff837ad8f690ce8cb0acf111f5d25c5efaf6fa828401ab951d56
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:46.458484Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f23e1405347fa9d8a0826d4dd1279b7cdec8361390d20e439154dcbbd386a2d4
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86318
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T09:27:49.002535Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 8ba4e0a242571ae9a62ca7ba5c0f4af765962a02f5119a96d47dda9df7c9d593
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch062/record01/quantity-inventory.json
  accessed_at: '2026-10-28T09:46:13.233676Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 0150b74191a3c92d7d45870e09fc8fc55a722d68359017245a147f15dc95f9cf
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch062/record01/grounding-inventory.json
  accessed_at: '2026-10-28T09:46:13.233775Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: bf0a3254b55dd7d5989059bd5713a554906f8e8be22635e1a6d1fdf5ae2ec7f7
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch062/record01/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T09:46:13.233853Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: b6b406136aeefd176d1937789a0d788dee8fb0d0a81f42e3ee36f0824e0819c0
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch062/record01/scalar-census.json
  accessed_at: '2026-10-28T09:46:13.233874Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: 1d0c192e8f5c0f4bd1ddc318d1a1e08c692bfdafa722c4abeba3d2fb14413d27
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch062/record01/validate-schema.json
  accessed_at: '2026-10-28T09:27:30.326167Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: ee6ee60e1e6a0c4e153516e0e5f9691dfbab32afae840307520ac22352f23dc2
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch062/record01/validate-strict.json
  accessed_at: '2026-10-28T09:27:31.270736Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch062/record01/strict.tsv\n"
  snapshot_sha256: 66935fcaa8f93b14b05d71ead5c3220749f40add8bd22d28581cca8b89eeb5b3
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch062/record01/validate-terms.json
  accessed_at: '2026-10-28T09:27:32.736126Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: ab5ff87134706b0b25d82012f6cf1b71e3047c7dfca3993541d10ce9a1be0c54
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch062/record01/validate-references.json
  accessed_at: '2026-10-28T09:27:33.499416Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: 216ef5bb700a7202b288c7fc530d348404b9922ba73dc3fe6fa52b215fc2f783
assessments:
- assessment_id: a1
  area: identity
  topic: Exact provenance and explicit base dependency
  outcome: supported
  summary: 'The two exact maintained contributors retain distinct stable IDs and reciprocal
    historical SOURCE_DUPLICATE links. The selected record uses the KOMODO identity,
    whose local notes explicitly cite DSM421. The historical selected-pair relationship
    supports provenance, not full preparation equality: the DSM owner has eleven steps
    and the KOMODO owner has none. DSM421 expressly names medium28.'
  target_ids:
  - CultureMech:005246
  evidence_ids:
  - identity-search
  - historical-reader
  - dsm421
  - base28
- assessment_id: a2
  area: consistency
  topic: Complex liquid formulation
  outcome: supported
  summary: The complete referenced base contains yeast extract, supporting COMPLEX/UNDEFINED
    and liquid state. The truncated five-ingredient view alone would conceal that
    basis; it must not motivate a false defined-medium recategorization.
  target_ids:
  - CultureMech:005246
  evidence_ids:
  - dsm28
  - api28
  - dsm421
- assessment_id: a3
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:005246
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "NaCl supplement", "source": [{"evidence_id":
    "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T09:27:43.186753Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\":
    10,\n                        \"unit\": \"%\",\n                        \"g_l\":
    100,\n                        \"mmol_l\": 1711.16,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "NaCl", "compound_id": 43, "amount": 10, "unit": "%", "g_l": 100, "mmol_l": 1711.16,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "dsm421", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium421.pdf", "raw_path":
    "REVIEW_WORK/batch062/source01-03/dsm421.bin", "raw_sha256": "147737ed0bfdd97948c86a691a34151f6e28a89687ab665b857bdd210f385ccc",
    "locator": "Complete supplement instruction", "accessed_at": "2026-10-28T09:27:43.389676Z",
    "quote": "421. CHROMATIUM SALEXIGENS MEDIUM\n\nSupplement medium 28 with NaCl
    (10%), MgCl 2 x 6 H2O (0.3%) Na-acetate (0.05%)\nand sodium thiosulfate (0.05%).
    Incubate at 500 to 1000 Lux light intensity."}], "decision": "evidence_only",
    "rationale": "The provider explicitly declares this supplement g_l rate in Main421.
    Retain it at the supplement stage with evidence; the primary bare percent alone
    does not establish w/v and the incomplete base prevents treating this list as
    the complete final formulation.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "100",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly
    declares this supplement g_l rate in Main421. Retain it at the supplement stage
    with evidence; the primary bare percent alone does not establish w/v and the incomplete
    base prevents treating this list as the complete final formulation."}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "100",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly
    declares this supplement g_l rate in Main421. Retain it at the supplement stage
    with evidence; the primary bare percent alone does not establish w/v and the incomplete
    base prevents treating this list as the complete final formulation."}, {"path":
    "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path":
    "ingredients[0].concentration", "stored_value": {"value": "100", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "The provider explicitly declares this
    supplement g_l rate in Main421. Retain it at the supplement stage with evidence;
    the primary bare percent alone does not establish w/v and the incomplete base
    prevents treating this list as the complete final formulation."}]}, {"quantity_id":
    "q2", "topic": "MgCl2 x6 H2O supplement", "source": [{"evidence_id": "api421",
    "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin",
    "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T09:27:43.186753Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\":
    0.3,\n                        \"unit\": \"%\",\n                        \"g_l\":
    3,\n                        \"mmol_l\": 14.7563,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "MgCl2 x 6 H2O", "compound_id": 79, "amount": 0.3, "unit": "%", "g_l": 3, "mmol_l":
    14.7563, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm421",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium421.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm421.bin", "raw_sha256": "147737ed0bfdd97948c86a691a34151f6e28a89687ab665b857bdd210f385ccc",
    "locator": "Complete supplement instruction", "accessed_at": "2026-10-28T09:27:43.389676Z",
    "quote": "421. CHROMATIUM SALEXIGENS MEDIUM\n\nSupplement medium 28 with NaCl
    (10%), MgCl 2 x 6 H2O (0.3%) Na-acetate (0.05%)\nand sodium thiosulfate (0.05%).
    Incubate at 500 to 1000 Lux light intensity."}], "decision": "evidence_only",
    "rationale": "The provider explicitly declares this supplement g_l rate in Main421.
    Retain it at the supplement stage with evidence; the primary bare percent alone
    does not establish w/v and the incomplete base prevents treating this list as
    the complete final formulation.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "3", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly
    declares this supplement g_l rate in Main421. Retain it at the supplement stage
    with evidence; the primary bare percent alone does not establish w/v and the incomplete
    base prevents treating this list as the complete final formulation."}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "3", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly
    declares this supplement g_l rate in Main421. Retain it at the supplement stage
    with evidence; the primary bare percent alone does not establish w/v and the incomplete
    base prevents treating this list as the complete final formulation."}, {"path":
    "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path":
    "ingredients[1].concentration", "stored_value": {"value": "3", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "The provider explicitly declares this
    supplement g_l rate in Main421. Retain it at the supplement stage with evidence;
    the primary bare percent alone does not establish w/v and the incomplete base
    prevents treating this list as the complete final formulation."}]}, {"quantity_id":
    "q3", "topic": "Sodium acetate supplement", "source": [{"evidence_id": "api421",
    "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin",
    "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T09:27:43.186753Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Na acetate\",\n                        \"compound_id\": 401,\n                        \"amount\":
    0.05,\n                        \"unit\": \"%\",\n                        \"g_l\":
    0.5,\n                        \"mmol_l\": 6.09505,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "Na acetate", "compound_id": 401, "amount": 0.05, "unit": "%", "g_l": 0.5, "mmol_l":
    6.09505, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm421",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium421.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm421.bin", "raw_sha256": "147737ed0bfdd97948c86a691a34151f6e28a89687ab665b857bdd210f385ccc",
    "locator": "Complete supplement instruction", "accessed_at": "2026-10-28T09:27:43.389676Z",
    "quote": "421. CHROMATIUM SALEXIGENS MEDIUM\n\nSupplement medium 28 with NaCl
    (10%), MgCl 2 x 6 H2O (0.3%) Na-acetate (0.05%)\nand sodium thiosulfate (0.05%).
    Incubate at 500 to 1000 Lux light intensity."}], "decision": "evidence_only",
    "rationale": "The provider explicitly declares this supplement g_l rate in Main421.
    Retain it at the supplement stage with evidence; the primary bare percent alone
    does not establish w/v and the incomplete base prevents treating this list as
    the complete final formulation.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly
    declares this supplement g_l rate in Main421. Retain it at the supplement stage
    with evidence; the primary bare percent alone does not establish w/v and the incomplete
    base prevents treating this list as the complete final formulation."}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly
    declares this supplement g_l rate in Main421. Retain it at the supplement stage
    with evidence; the primary bare percent alone does not establish w/v and the incomplete
    base prevents treating this list as the complete final formulation."}, {"path":
    "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path":
    "ingredients[2].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "The provider explicitly declares this
    supplement g_l rate in Main421. Retain it at the supplement stage with evidence;
    the primary bare percent alone does not establish w/v and the incomplete base
    prevents treating this list as the complete final formulation."}]}, {"quantity_id":
    "q4", "topic": "Sodium thiosulfate supplement", "source": [{"evidence_id": "api421",
    "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin",
    "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52",
    "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T09:27:43.186753Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Sodium Thiosulfate\",\n                        \"compound_id\": 1126,\n                        \"amount\":
    0.05,\n                        \"unit\": \"%\",\n                        \"g_l\":
    0.5,\n                        \"mmol_l\": 3.16236,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "Sodium Thiosulfate", "compound_id": 1126, "amount": 0.05, "unit": "%", "g_l":
    0.5, "mmol_l": 3.16236, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm421", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium421.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm421.bin", "raw_sha256": "147737ed0bfdd97948c86a691a34151f6e28a89687ab665b857bdd210f385ccc",
    "locator": "Complete supplement instruction", "accessed_at": "2026-10-28T09:27:43.389676Z",
    "quote": "421. CHROMATIUM SALEXIGENS MEDIUM\n\nSupplement medium 28 with NaCl
    (10%), MgCl 2 x 6 H2O (0.3%) Na-acetate (0.05%)\nand sodium thiosulfate (0.05%).
    Incubate at 500 to 1000 Lux light intensity."}], "decision": "evidence_only",
    "rationale": "The provider explicitly declares this supplement g_l rate in Main421.
    Retain it at the supplement stage with evidence; the primary bare percent alone
    does not establish w/v and the incomplete base prevents treating this list as
    the complete final formulation.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly
    declares this supplement g_l rate in Main421. Retain it at the supplement stage
    with evidence; the primary bare percent alone does not establish w/v and the incomplete
    base prevents treating this list as the complete final formulation."}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The provider explicitly
    declares this supplement g_l rate in Main421. Retain it at the supplement stage
    with evidence; the primary bare percent alone does not establish w/v and the incomplete
    base prevents treating this list as the complete final formulation."}, {"path":
    "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path":
    "ingredients[3].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "The provider explicitly declares this
    supplement g_l rate in Main421. Retain it at the supplement stage with evidence;
    the primary bare percent alone does not establish w/v and the incomplete base
    prevents treating this list as the complete final formulation."}]}, {"quantity_id":
    "q5", "topic": "Neutralized feeding-stock strength mislocated as direct ingredient",
    "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52",
    "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T09:27:43.186753Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\":
    3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    30,\n                        \"mmol_l\": 124.905,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Na2S x 9 H2O", "compound_id": 54, "amount": 3, "unit": "g", "g_l": 30, "mmol_l":
    124.905, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "api421",
    "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin",
    "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52",
    "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T09:27:43.186753Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\":
    \"Neutralized sulfide solution 3% (w/v)\",\n                        \"solution_id\":
    34,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 7, "solution": "Neutralized sulfide solution 3% (w/v)", "solution_id":
    34, "amount": 10, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."},
    {"evidence_id": "dsm28", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm28.bin", "raw_sha256": "442636c7b32c8f6de4a54fd8acaaa22f8e1a130f3d4b45af59d5782fe77a6c3d",
    "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T09:27:43.589061Z",
    "quote": "Neutralized sulfide solution:\nDistilled water                                                100.00       ml\nNa2S
    x 9 H2O                                                     3.00        g\n\nThe
    sulfide solution is prepared"}], "decision": "correct", "rationale": "The current
    API states a10 ml recipe row and variable1–3 ml/100 ml feed prose, whereas the
    primary prescribes periodic feeding without a fixed dose. Keep the conflict visible
    instead of selecting one dose for a complete-medium calculation.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml", "field_path":
    "ingredients[4].concentration", "stored_value": {"value": "30", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "30 g/L describes the separate neutralized
    feeding stock, not the complete medium. Retain3 g/100 ml stock provenance and
    the separate variable feeding stage; no fixed final-medium contribution is justified."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "30",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "30 g/L describes the
    separate neutralized feeding stock, not the complete medium. Retain3 g/100 ml
    stock provenance and the separate variable feeding stage; no fixed final-medium
    contribution is justified."}, {"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "30",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "30 g/L describes the
    separate neutralized feeding stock, not the complete medium. Retain3 g/100 ml
    stock provenance and the separate variable feeding stage; no fixed final-medium
    contribution is justified."}]}, {"quantity_id": "q6", "topic": "Required Main28
    base", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T09:27:43.186753Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\":
    \"Main sol. 28\",\n                        \"solution_id\": 26,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "solution":
    "Main sol. 28", "solution_id": 26, "amount": 1000, "unit": "ml", "optional": 0},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "dsm421", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium421.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm421.bin", "raw_sha256": "147737ed0bfdd97948c86a691a34151f6e28a89687ab665b857bdd210f385ccc",
    "locator": "Supplement medium28 instruction", "accessed_at": "2026-10-28T09:27:43.389676Z",
    "quote": "421. CHROMATIUM SALEXIGENS MEDIUM\n\nSupplement medium 28 with NaCl
    (10%), MgCl 2 x 6 H2O (0.3%) Na-acetate (0.05%)\nand sodium thiosulfate (0.05%).
    Incubate at 500 to 1000 Lux light intensity."}], "decision": "add", "rationale":
    "The API references1000 ml Main28; the primary says supplement medium28. This
    is a recipe/base quantity, not proof that all additions yield an independently
    measured one-litre final preparation.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Create the explicitly required base reference/topology rather than pretending
    that four supplements and a feeding stock form the full medium.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Create the explicitly required base reference/topology rather than pretending
    that four supplements and a feeding stock form the full medium.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "Create the
    explicitly required base reference/topology rather than pretending that four supplements
    and a feeding stock form the full medium.", "missing": true}]}, {"quantity_id":
    "q7", "topic": "Scoped DSM28 CaCl2 x 2 H2O", "source": [{"evidence_id": "api28",
    "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin",
    "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\":
    0.25,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.543478,\n                        \"mmol_l\": 3.69675,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "CaCl2 x 2 H2O", "compound_id": 7, "amount": 0.25, "unit": "g", "g_l": 0.543478,
    "mmol_l": 3.69675, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "The current provider explicitly declares this rate for
    Solution A, a component solution. Preserve its source batch amount and stock rate
    at that stage; it is incorrectly exposed as a direct base-medium ingredient and
    must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.543478",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider
    explicitly declares this rate for Solution A, a component solution. Preserve its
    source batch amount and stock rate at that stage; it is incorrectly exposed as
    a direct base-medium ingredient and must not transfer unchanged to421."}]}, {"quantity_id":
    "q8", "topic": "Scoped DSM28 Yeast extract", "source": [{"evidence_id": "api28",
    "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin",
    "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\":
    0.25,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.543478,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 2, "compound": "Yeast extract", "compound_id": 16, "amount":
    0.25, "unit": "g", "g_l": 0.543478, "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "correct", "rationale": "The current provider explicitly declares
    this rate for Solution A, a component solution. Preserve its source batch amount
    and stock rate at that stage; it is incorrectly exposed as a direct base-medium
    ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[1].concentration",
    "stored_value": {"value": "0.543478", "unit": "G_PER_L"}, "decision": "correct",
    "rationale": "The current provider explicitly declares this rate for Solution
    A, a component solution. Preserve its source batch amount and stock rate at that
    stage; it is incorrectly exposed as a direct base-medium ingredient and must not
    transfer unchanged to421."}]}, {"quantity_id": "q9", "topic": "Scoped DSM28 Na2S
    x 9 H2O", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\":
    2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    14.8148,\n                        \"mmol_l\": 61.6816,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Na2S x 9 H2O", "compound_id": 54, "amount": 2, "unit": "g", "g_l": 14.8148, "mmol_l":
    61.6816, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "api28",
    "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin",
    "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[8].recipe[0]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\":
    3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    30,\n                        \"mmol_l\": 124.905,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Na2S x 9 H2O", "compound_id": 54, "amount": 3, "unit": "g", "g_l": 30, "mmol_l":
    124.905, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm28",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm28.bin", "raw_sha256": "442636c7b32c8f6de4a54fd8acaaa22f8e1a130f3d4b45af59d5782fe77a6c3d",
    "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T09:27:43.589061Z",
    "quote": "Solution B:\nNa2S x 9 H2O                                                      2.00        g\nDistilled
    water                                                 135.00       ml\nPrepare
    in a screw-cap bottle, bubble with N2 to replace air, close tightly and autoclave.\n\nSolution
    C:"}, {"evidence_id": "dsm28", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm28.bin", "raw_sha256": "442636c7b32c8f6de4a54fd8acaaa22f8e1a130f3d4b45af59d5782fe77a6c3d",
    "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T09:27:43.589061Z",
    "quote": "Neutralized sulfide solution:\nDistilled water                                                100.00       ml\nNa2S
    x 9 H2O                                                     3.00        g\n\nThe
    sulfide solution is prepared"}], "decision": "correct", "rationale": "44.8148
    g/L sums14.8148 g/L initial sulfide-stock and30 g/L later feeding-stock rates.
    These are distinct stages and cannot be added as a final-medium concentration.
    Retain separate source stocks and addition instructions.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path":
    "ingredients[2].concentration", "stored_value": {"value": "44.8148", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "44.8148 g/L sums14.8148 g/L initial sulfide-stock
    and30 g/L later feeding-stock rates. These are distinct stages and cannot be added
    as a final-medium concentration. Retain separate source stocks and addition instructions."}]},
    {"quantity_id": "q10", "topic": "Scoped DSM28 NaHCO3", "source": [{"evidence_id":
    "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[3].recipe[0]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\":
    1.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    30,\n                        \"mmol_l\": 357.113,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "NaHCO3", "compound_id": 55, "amount": 1.5, "unit": "g", "g_l": 30, "mmol_l":
    357.113, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "The current provider explicitly declares this rate for Bicarbonate
    solution, a component solution. Preserve its source batch amount and stock rate
    at that stage; it is incorrectly exposed as a direct base-medium ingredient and
    must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "30",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider
    explicitly declares this rate for Bicarbonate solution, a component solution.
    Preserve its source batch amount and stock rate at that stage; it is incorrectly
    exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]},
    {"quantity_id": "q11", "topic": "Scoped DSM28 Resazurin", "source": [{"evidence_id":
    "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[4].recipe[0]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"attribute\":
    \"0,1%\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.0111111,\n                        \"mmol_l\":
    0.0484799,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 1, "compound": "Resazurin", "compound_id": 25, "attribute": "0,1%",
    "amount": 0.5, "unit": "ml", "g_l": 0.0111111, "mmol_l": 0.0484799, "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "dsm28", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm28.bin", "raw_sha256": "442636c7b32c8f6de4a54fd8acaaa22f8e1a130f3d4b45af59d5782fe77a6c3d",
    "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T09:27:43.589061Z",
    "quote": "Solution D\nResazurin (0,1%)                                                        0.5     ml\nDistilled
    water                                                      450.00     ml\n\nAutoclave
    in a cotton"}], "decision": "conflict", "rationale": "The provider declares0.0111111
    g/L within resazurin solution, whereas the primary supplies0.5 ml of0.1% reagent
    in450 ml water without a percentage basis. Preserve both statements; no independent
    mass conversion or final-medium resazurin rate is authenticated.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path":
    "ingredients[4].concentration", "stored_value": {"value": "0.0111111", "unit":
    "G_PER_L"}, "decision": "conflict", "rationale": "The provider declares0.0111111
    g/L within resazurin solution, whereas the primary supplies0.5 ml of0.1% reagent
    in450 ml water without a percentage basis. Preserve both statements; no independent
    mass conversion or final-medium resazurin rate is authenticated."}]}, {"quantity_id":
    "q12", "topic": "Scoped DSM28 Ammonium chloride", "source": [{"evidence_id": "api28",
    "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin",
    "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[5].recipe[0]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Ammonium chloride\",\n                        \"compound_id\": 57,\n                        \"amount\":
    0.35,\n                        \"unit\": \"g\",\n                        \"g_l\":
    13.4615,\n                        \"mmol_l\": 251.665,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Ammonium chloride", "compound_id": 57, "amount": 0.35, "unit": "g", "g_l": 13.4615,
    "mmol_l": 251.665, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "The current provider explicitly declares this rate for
    Pfennig''s heterotrophic salts solution, a component solution. Preserve its source
    batch amount and stock rate at that stage; it is incorrectly exposed as a direct
    base-medium ingredient and must not transfer unchanged to421.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path":
    "ingredients[5].concentration", "stored_value": {"value": "13.4615", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The current provider explicitly declares
    this rate for Pfennig''s heterotrophic salts solution, a component solution. Preserve
    its source batch amount and stock rate at that stage; it is incorrectly exposed
    as a direct base-medium ingredient and must not transfer unchanged to421."}]},
    {"quantity_id": "q13", "topic": "Scoped DSM28 Ammonium acetate", "source": [{"evidence_id":
    "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[5].recipe[1]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Ammonium acetate\",\n                        \"compound_id\": 58,\n                        \"amount\":
    0.25,\n                        \"unit\": \"g\",\n                        \"g_l\":
    9.61539,\n                        \"mmol_l\": 124.746,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "Ammonium acetate", "compound_id": 58, "amount": 0.25, "unit": "g", "g_l": 9.61539,
    "mmol_l": 124.746, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "The current provider explicitly declares this rate for
    Pfennig''s heterotrophic salts solution, a component solution. Preserve its source
    batch amount and stock rate at that stage; it is incorrectly exposed as a direct
    base-medium ingredient and must not transfer unchanged to421.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path":
    "ingredients[6].concentration", "stored_value": {"value": "9.61539", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The current provider explicitly declares
    this rate for Pfennig''s heterotrophic salts solution, a component solution. Preserve
    its source batch amount and stock rate at that stage; it is incorrectly exposed
    as a direct base-medium ingredient and must not transfer unchanged to421."}]},
    {"quantity_id": "q14", "topic": "Scoped DSM28 Pyruvic acid sodium salt", "source":
    [{"evidence_id": "dsm28", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm28.bin", "raw_sha256": "442636c7b32c8f6de4a54fd8acaaa22f8e1a130f3d4b45af59d5782fe77a6c3d",
    "locator": "PDF extracted line 36; visually checked page", "accessed_at": "2026-10-28T09:27:43.589061Z",
    "quote": "Pyruvic acid sodium salt                                               0.25      g"},
    {"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[5].recipe; complete current solutionE payload", "accessed_at":
    "2026-10-28T09:27:43.365556Z", "quote": "{\n  \"status\": 200,\n  \"count\": 1,\n  \"data\":
    {\n    \"medium\": {\n      \"id\": 28,\n      \"name\": \"PFENNIG''S MEDIUM I
    \",\n      \"complex_medium\": \"yes\",\n      \"min_pH\": 7.1,\n      \"max_pH\":
    7.3,\n      \"source\": \"DSMZ\",\n      \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf\"\n    },\n    \"solutions\":
    [\n      {\n        \"id\": 26,\n        \"name\": \"Main sol. 28\",\n        \"volume\":
    1000,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"solution\":
    \"Solution A\",\n            \"solution_id\": 27,\n            \"amount\": 460,\n            \"unit\":
    \"ml\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    2,\n            \"solution\": \"Resazurin solution\",\n            \"solution_id\":
    30,\n            \"amount\": 450,\n            \"unit\": \"ml\",\n            \"optional\":
    0\n          },\n          {\n            \"recipe_order\": 3,\n            \"solution\":
    \"Bicarbonate solution\",\n            \"solution_id\": 29,\n            \"amount\":
    50,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    4,\n            \"solution\": \"Pfennig''s heterotrophic salts solution\",\n            \"solution_id\":
    31,\n            \"amount\": 26,\n            \"unit\": \"ml\",\n            \"optional\":
    0\n          },\n          {\n            \"recipe_order\": 5,\n            \"solution\":
    \"Sulfide solution, 1.5%\",\n            \"solution_id\": 28,\n            \"amount\":
    40,\n            \"unit\": \"ml/l\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    6,\n            \"solution\": \"Vitamin B12 solution\",\n            \"solution_id\":
    32,\n            \"amount\": 1,\n            \"unit\": \"ml/l\",\n            \"optional\":
    0\n          },\n          {\n            \"recipe_order\": 7,\n            \"solution\":
    \"Neutralized sulfide solution 3% (w/v)\",\n            \"solution_id\": 34,\n            \"amount\":
    10,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\":
    [\n          {\n            \"recipe_order\": 7,\n            \"step\": \"Adjust
    the pH with filter-sterilised 1M Na2CO3 to 7.1-7.3.\"\n          },\n          {\n            \"recipe_order\":
    7,\n            \"step\": \"If needed, aliquot into sterile, N<sub>2</sub> gassed
    screw-cap tubes under N<sub>2</sub> gas.\"\n          },\n          {\n            \"recipe_order\":
    7,\n            \"step\": \"During the first 24 h, the iron of the medium precipitates
    in the form of black flocks. No other sediment should arise in the otherwise clear
    medium.\"\n          },\n          {\n            \"recipe_order\": 2,\n            \"step\":
    \"Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble
    with N2/CO2 and autoclave at 121°C for 15 min (as decribed below).\"\n          },\n          {\n            \"recipe_order\":
    2,\n            \"step\": \"Prepare the following solutions (resazurin, bicarbonate
    and Pfennig''s heterotrophic salts) and sterilize as given below.\"\n          },\n          {\n            \"recipe_order\":
    5,\n            \"step\": \"Add bicarbonate solution and Pfennig''s heterotrophic
    salts to the resazurin (complete volumina, i.e. 50 mL bicarbonate solution and
    26 mL Pfennig''s heterotrophic salts solution). Bubble with CO2 in an ice bath
    under sterile conditions.\"\n          },\n          {\n            \"recipe_order\":
    5,\n            \"step\": \"Fill 50 ml of this mixture to each bottle of solution
    A (46 mL + 50 mL).\"\n          },\n          {\n            \"recipe_order\":
    5,\n            \"step\": \"Before use, add 4 ml sulfide solution (1.5%) and 0.1
    ml Vitamin B12 solution to each 100 mL bottle.\"\n          },\n          {\n            \"recipe_order\":
    7,\n            \"step\": \"Feed the actively growing culture periodically with
    neutralized 3% solution of sodium sulfide (use 1 -3 mL/100 mL depending on strain
    and cultivation stage) to replenish sulfide and with other supplement solutions
    (see Ref. 3365).\"\n          },\n          {\n            \"step\": \"Note: for
    marine species use 1-3% NaCl and increase the amount of MgSO4 7*H2O to 2,8g/L\"\n          }\n        ]\n      },\n      {\n        \"id\":
    27,\n        \"name\": \"Solution A\",\n        \"volume\": 460,\n        \"recipe\":
    [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"CaCl2
    x 2 H2O\",\n            \"compound_id\": 7,\n            \"amount\": 0.25,\n            \"unit\":
    \"g\",\n            \"g_l\": 0.543478,\n            \"mmol_l\": 3.69675,\n            \"optional\":
    0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\":
    \"Yeast extract\",\n            \"compound_id\": 16,\n            \"amount\":
    0.25,\n            \"unit\": \"g\",\n            \"g_l\": 0.543478,\n            \"optional\":
    0\n          },\n          {\n            \"recipe_order\": 3,\n            \"compound\":
    \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\":
    460,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\":
    [\n          {\n            \"step\": \"Aliquot Solution A into 100 mL screw-cap
    bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121°C for
    15 min.\"\n          }\n        ],\n        \"equipment\": {\n          \"5486\":
    \"Autoclave\"\n        }\n      },\n      {\n        \"id\": 28,\n        \"name\":
    \"Sulfide solution, 1.5%\",\n        \"volume\": 135,\n        \"recipe\": [\n          {\n            \"recipe_order\":
    1,\n            \"compound\": \"Na2S x 9 H2O\",\n            \"compound_id\":
    54,\n            \"amount\": 2,\n            \"unit\": \"g\",\n            \"g_l\":
    14.8148,\n            \"mmol_l\": 61.6816,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    2,\n            \"compound\": \"Distilled water\",\n            \"compound_id\":
    4,\n            \"amount\": 135,\n            \"unit\": \"ml\",\n            \"optional\":
    0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\":
    \"Prepare in a screw-cap bottle, bubble with N2 to replace air, close tightly
    and autoclave.\"\n          }\n        ],\n        \"equipment\": {\n          \"5487\":
    \"Autoclave\"\n        }\n      },\n      {\n        \"id\": 29,\n        \"name\":
    \"Bicarbonate solution\",\n        \"volume\": 50,\n        \"recipe\": [\n          {\n            \"recipe_order\":
    1,\n            \"compound\": \"NaHCO3\",\n            \"compound_id\": 55,\n            \"amount\":
    1.5,\n            \"unit\": \"g\",\n            \"g_l\": 30,\n            \"mmol_l\":
    357.113,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    2,\n            \"compound\": \"H2O\",\n            \"compound_id\": 56,\n            \"amount\":
    50,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\":
    [\n          {\n            \"step\": \"Bubble with CO2 and filter sterilize into
    sterile, gas-tight, 100 ml screw-cap bottle.\"\n          }\n        ],\n        \"equipment\":
    {\n          \"5488\": \"Filter\"\n        }\n      },\n      {\n        \"id\":
    30,\n        \"name\": \"Resazurin solution\",\n        \"volume\": 450,\n        \"recipe\":
    [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"Resazurin\",\n            \"compound_id\":
    25,\n            \"attribute\": \"0,1%\",\n            \"amount\": 0.5,\n            \"unit\":
    \"ml\",\n            \"g_l\": 0.0111111,\n            \"mmol_l\": 0.0484799,\n            \"optional\":
    0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\":
    \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\":
    450,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\":
    [\n          {\n            \"step\": \"Cool to room temperature under an atmosphere
    of N2/CO2 in an ice bath.\"\n          },\n          {\n            \"step\":
    \"Autoclave in a cotton-stoppered Erlenmeyer flask with an outlet tube for medium,
    connected to a glass outlet at the bottom of the vessel and has, at the other
    end, a silicon rubber tube with a pinch cock and a bell for aseptic dispensing
    of the medium into bottles.\"\n          }\n        ],\n        \"equipment\":
    {\n          \"5490\": \"Ice bath\",\n          \"5489\": \"Autoclave\"\n        }\n      },\n      {\n        \"id\":
    31,\n        \"name\": \"Pfennig''s heterotrophic salts solution\",\n        \"volume\":
    26,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\":
    \"Ammonium chloride\",\n            \"compound_id\": 57,\n            \"amount\":
    0.35,\n            \"unit\": \"g\",\n            \"g_l\": 13.4615,\n            \"mmol_l\":
    251.665,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    2,\n            \"compound\": \"Ammonium acetate\",\n            \"compound_id\":
    58,\n            \"amount\": 0.25,\n            \"unit\": \"g\",\n            \"g_l\":
    9.61539,\n            \"mmol_l\": 124.746,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    5,\n            \"compound\": \"MgSO4 x 7 H2O\",\n            \"compound_id\":
    8,\n            \"amount\": 0.5,\n            \"unit\": \"g\",\n            \"g_l\":
    19.2308,\n            \"mmol_l\": 78.0229,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    6,\n            \"compound\": \"KCl\",\n            \"compound_id\": 61,\n            \"amount\":
    0.35,\n            \"unit\": \"g\",\n            \"g_l\": 13.4615,\n            \"mmol_l\":
    180.571,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    7,\n            \"compound\": \"KH2PO4\",\n            \"compound_id\": 11,\n            \"amount\":
    0.35,\n            \"unit\": \"g\",\n            \"g_l\": 13.4615,\n            \"mmol_l\":
    98.9201,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    8,\n            \"solution\": \"Trace element solution SL-12 B\",\n            \"solution_id\":
    33,\n            \"amount\": 1,\n            \"unit\": \"ml\",\n            \"optional\":
    0\n          },\n          {\n            \"recipe_order\": 9,\n            \"compound\":
    \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\":
    25,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\":
    [\n          {\n            \"step\": \"Filter sterilize into sterile, gas-tight,
    100 ml screw-cap bottle.\"\n          }\n        ],\n        \"equipment\": {\n          \"3563\":
    \"Filter\"\n        }\n      },\n      {\n        \"id\": 32,\n        \"name\":
    \"Vitamin B12 solution\",\n        \"volume\": 100,\n        \"recipe\": [\n          {\n            \"recipe_order\":
    1,\n            \"compound\": \"Vitamin B12\",\n            \"compound_id\": 18,\n            \"amount\":
    0.01,\n            \"unit\": \"g\",\n            \"g_l\": 0.1,\n            \"mmol_l\":
    0.073779,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    2,\n            \"compound\": \"Distilled water\",\n            \"compound_id\":
    4,\n            \"amount\": 100,\n            \"unit\": \"ml\",\n            \"optional\":
    0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\":
    \"Filter sterilized\"\n          }\n        ],\n        \"equipment\": {\n          \"5492\":
    \"Filter\"\n        }\n      },\n      {\n        \"id\": 33,\n        \"name\":
    \"Trace element solution SL-12 B\",\n        \"volume\": 1000,\n        \"recipe\":
    [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"Na2-EDTA\",\n            \"compound_id\":
    34,\n            \"amount\": 3,\n            \"unit\": \"g\",\n            \"g_l\":
    3,\n            \"mmol_l\": 8.9231,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    2,\n            \"compound\": \"FeSO4 x 7 H2O\",\n            \"compound_id\":
    12,\n            \"amount\": 1.1,\n            \"unit\": \"g\",\n            \"g_l\":
    1.1,\n            \"mmol_l\": 3.95662,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    3,\n            \"compound\": \"CoCl2 x 6 H2O\",\n            \"compound_id\":
    38,\n            \"amount\": 190,\n            \"unit\": \"mg\",\n            \"g_l\":
    0.19,\n            \"mmol_l\": 1.46335,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    4,\n            \"compound\": \"MnCl2 x 2 H2O\",\n            \"compound_id\":
    63,\n            \"amount\": 50,\n            \"unit\": \"mg\",\n            \"g_l\":
    0.05,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    5,\n            \"compound\": \"ZnCl2\",\n            \"compound_id\": 64,\n            \"amount\":
    42,\n            \"unit\": \"mg\",\n            \"g_l\": 0.042,\n            \"mmol_l\":
    0.308144,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    6,\n            \"compound\": \"NiCl2 x 6 H2O\",\n            \"compound_id\":
    40,\n            \"amount\": 24,\n            \"unit\": \"mg\",\n            \"g_l\":
    0.024,\n            \"mmol_l\": 0.185187,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    7,\n            \"compound\": \"Na2MoO4 x 2 H2O\",\n            \"compound_id\":
    9,\n            \"amount\": 18,\n            \"unit\": \"mg\",\n            \"g_l\":
    0.018,\n            \"mmol_l\": 0.0743955,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    8,\n            \"compound\": \"H3BO3\",\n            \"compound_id\": 37,\n            \"amount\":
    300,\n            \"unit\": \"mg\",\n            \"g_l\": 0.3,\n            \"mmol_l\":
    4.85123,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    9,\n            \"compound\": \"CuCl2 x 2 H2O\",\n            \"compound_id\":
    39,\n            \"amount\": 2,\n            \"unit\": \"mg\",\n            \"g_l\":
    0.002,\n            \"mmol_l\": 0.0117314,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    10,\n            \"compound\": \"Distilled water\",\n            \"compound_id\":
    4,\n            \"amount\": 1000,\n            \"unit\": \"ml\",\n            \"optional\":
    0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\":
    \"Adjust pH to 6.0.\"\n          }\n        ],\n        \"equipment\": {\n          \"572\":
    \"Ice bath\",\n          \"2369\": \"Filter\"\n        }\n      },\n      {\n        \"id\":
    34,\n        \"name\": \"Neutralized sulfide solution 3% (w/v)\",\n        \"volume\":
    100,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\":
    \"Na2S x 9 H2O\",\n            \"compound_id\": 54,\n            \"amount\": 3,\n            \"unit\":
    \"g\",\n            \"g_l\": 30,\n            \"mmol_l\": 124.905,\n            \"optional\":
    0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\":
    \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\":
    100,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\":
    [\n          {\n            \"step\": \"The sulfide solution is prepared in a
    250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer.
    The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at
    121°C. After cooling to room temperature the pH is adjusted to about 7.0 by adding
    of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle.\"\n          }\n        ]\n      }\n    ]\n  }\n}\n"}],
    "decision": "unsupported", "rationale": "The primary expressly supplies0.25 g
    in solutionE. The current API omits this ingredient from E;25 ml water plus1 ml
    trace addition is not an explicit final-volume declaration. Preserve the primary
    batch mass and the provider omission, but the local9.61539 g/L denominator is
    not independently authenticated.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "9.61539",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary expressly
    supplies0.25 g in solutionE. The current API omits this ingredient from E;25 ml
    water plus1 ml trace addition is not an explicit final-volume declaration. Preserve
    the primary batch mass and the provider omission, but the local9.61539 g/L denominator
    is not independently authenticated."}]}, {"quantity_id": "q15", "topic": "Scoped
    DSM28 Dextrose", "source": [{"evidence_id": "dsm28", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm28.bin", "raw_sha256": "442636c7b32c8f6de4a54fd8acaaa22f8e1a130f3d4b45af59d5782fe77a6c3d",
    "locator": "PDF extracted line 37; visually checked page", "accessed_at": "2026-10-28T09:27:43.589061Z",
    "quote": "Dextrose                                                               0.25      g"},
    {"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[5].recipe; complete current solutionE payload", "accessed_at":
    "2026-10-28T09:27:43.365556Z", "quote": "{\n  \"status\": 200,\n  \"count\": 1,\n  \"data\":
    {\n    \"medium\": {\n      \"id\": 28,\n      \"name\": \"PFENNIG''S MEDIUM I
    \",\n      \"complex_medium\": \"yes\",\n      \"min_pH\": 7.1,\n      \"max_pH\":
    7.3,\n      \"source\": \"DSMZ\",\n      \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf\"\n    },\n    \"solutions\":
    [\n      {\n        \"id\": 26,\n        \"name\": \"Main sol. 28\",\n        \"volume\":
    1000,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"solution\":
    \"Solution A\",\n            \"solution_id\": 27,\n            \"amount\": 460,\n            \"unit\":
    \"ml\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    2,\n            \"solution\": \"Resazurin solution\",\n            \"solution_id\":
    30,\n            \"amount\": 450,\n            \"unit\": \"ml\",\n            \"optional\":
    0\n          },\n          {\n            \"recipe_order\": 3,\n            \"solution\":
    \"Bicarbonate solution\",\n            \"solution_id\": 29,\n            \"amount\":
    50,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    4,\n            \"solution\": \"Pfennig''s heterotrophic salts solution\",\n            \"solution_id\":
    31,\n            \"amount\": 26,\n            \"unit\": \"ml\",\n            \"optional\":
    0\n          },\n          {\n            \"recipe_order\": 5,\n            \"solution\":
    \"Sulfide solution, 1.5%\",\n            \"solution_id\": 28,\n            \"amount\":
    40,\n            \"unit\": \"ml/l\",\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    6,\n            \"solution\": \"Vitamin B12 solution\",\n            \"solution_id\":
    32,\n            \"amount\": 1,\n            \"unit\": \"ml/l\",\n            \"optional\":
    0\n          },\n          {\n            \"recipe_order\": 7,\n            \"solution\":
    \"Neutralized sulfide solution 3% (w/v)\",\n            \"solution_id\": 34,\n            \"amount\":
    10,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\":
    [\n          {\n            \"recipe_order\": 7,\n            \"step\": \"Adjust
    the pH with filter-sterilised 1M Na2CO3 to 7.1-7.3.\"\n          },\n          {\n            \"recipe_order\":
    7,\n            \"step\": \"If needed, aliquot into sterile, N<sub>2</sub> gassed
    screw-cap tubes under N<sub>2</sub> gas.\"\n          },\n          {\n            \"recipe_order\":
    7,\n            \"step\": \"During the first 24 h, the iron of the medium precipitates
    in the form of black flocks. No other sediment should arise in the otherwise clear
    medium.\"\n          },\n          {\n            \"recipe_order\": 2,\n            \"step\":
    \"Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble
    with N2/CO2 and autoclave at 121°C for 15 min (as decribed below).\"\n          },\n          {\n            \"recipe_order\":
    2,\n            \"step\": \"Prepare the following solutions (resazurin, bicarbonate
    and Pfennig''s heterotrophic salts) and sterilize as given below.\"\n          },\n          {\n            \"recipe_order\":
    5,\n            \"step\": \"Add bicarbonate solution and Pfennig''s heterotrophic
    salts to the resazurin (complete volumina, i.e. 50 mL bicarbonate solution and
    26 mL Pfennig''s heterotrophic salts solution). Bubble with CO2 in an ice bath
    under sterile conditions.\"\n          },\n          {\n            \"recipe_order\":
    5,\n            \"step\": \"Fill 50 ml of this mixture to each bottle of solution
    A (46 mL + 50 mL).\"\n          },\n          {\n            \"recipe_order\":
    5,\n            \"step\": \"Before use, add 4 ml sulfide solution (1.5%) and 0.1
    ml Vitamin B12 solution to each 100 mL bottle.\"\n          },\n          {\n            \"recipe_order\":
    7,\n            \"step\": \"Feed the actively growing culture periodically with
    neutralized 3% solution of sodium sulfide (use 1 -3 mL/100 mL depending on strain
    and cultivation stage) to replenish sulfide and with other supplement solutions
    (see Ref. 3365).\"\n          },\n          {\n            \"step\": \"Note: for
    marine species use 1-3% NaCl and increase the amount of MgSO4 7*H2O to 2,8g/L\"\n          }\n        ]\n      },\n      {\n        \"id\":
    27,\n        \"name\": \"Solution A\",\n        \"volume\": 460,\n        \"recipe\":
    [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"CaCl2
    x 2 H2O\",\n            \"compound_id\": 7,\n            \"amount\": 0.25,\n            \"unit\":
    \"g\",\n            \"g_l\": 0.543478,\n            \"mmol_l\": 3.69675,\n            \"optional\":
    0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\":
    \"Yeast extract\",\n            \"compound_id\": 16,\n            \"amount\":
    0.25,\n            \"unit\": \"g\",\n            \"g_l\": 0.543478,\n            \"optional\":
    0\n          },\n          {\n            \"recipe_order\": 3,\n            \"compound\":
    \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\":
    460,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\":
    [\n          {\n            \"step\": \"Aliquot Solution A into 100 mL screw-cap
    bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121°C for
    15 min.\"\n          }\n        ],\n        \"equipment\": {\n          \"5486\":
    \"Autoclave\"\n        }\n      },\n      {\n        \"id\": 28,\n        \"name\":
    \"Sulfide solution, 1.5%\",\n        \"volume\": 135,\n        \"recipe\": [\n          {\n            \"recipe_order\":
    1,\n            \"compound\": \"Na2S x 9 H2O\",\n            \"compound_id\":
    54,\n            \"amount\": 2,\n            \"unit\": \"g\",\n            \"g_l\":
    14.8148,\n            \"mmol_l\": 61.6816,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    2,\n            \"compound\": \"Distilled water\",\n            \"compound_id\":
    4,\n            \"amount\": 135,\n            \"unit\": \"ml\",\n            \"optional\":
    0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\":
    \"Prepare in a screw-cap bottle, bubble with N2 to replace air, close tightly
    and autoclave.\"\n          }\n        ],\n        \"equipment\": {\n          \"5487\":
    \"Autoclave\"\n        }\n      },\n      {\n        \"id\": 29,\n        \"name\":
    \"Bicarbonate solution\",\n        \"volume\": 50,\n        \"recipe\": [\n          {\n            \"recipe_order\":
    1,\n            \"compound\": \"NaHCO3\",\n            \"compound_id\": 55,\n            \"amount\":
    1.5,\n            \"unit\": \"g\",\n            \"g_l\": 30,\n            \"mmol_l\":
    357.113,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    2,\n            \"compound\": \"H2O\",\n            \"compound_id\": 56,\n            \"amount\":
    50,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\":
    [\n          {\n            \"step\": \"Bubble with CO2 and filter sterilize into
    sterile, gas-tight, 100 ml screw-cap bottle.\"\n          }\n        ],\n        \"equipment\":
    {\n          \"5488\": \"Filter\"\n        }\n      },\n      {\n        \"id\":
    30,\n        \"name\": \"Resazurin solution\",\n        \"volume\": 450,\n        \"recipe\":
    [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"Resazurin\",\n            \"compound_id\":
    25,\n            \"attribute\": \"0,1%\",\n            \"amount\": 0.5,\n            \"unit\":
    \"ml\",\n            \"g_l\": 0.0111111,\n            \"mmol_l\": 0.0484799,\n            \"optional\":
    0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\":
    \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\":
    450,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\":
    [\n          {\n            \"step\": \"Cool to room temperature under an atmosphere
    of N2/CO2 in an ice bath.\"\n          },\n          {\n            \"step\":
    \"Autoclave in a cotton-stoppered Erlenmeyer flask with an outlet tube for medium,
    connected to a glass outlet at the bottom of the vessel and has, at the other
    end, a silicon rubber tube with a pinch cock and a bell for aseptic dispensing
    of the medium into bottles.\"\n          }\n        ],\n        \"equipment\":
    {\n          \"5490\": \"Ice bath\",\n          \"5489\": \"Autoclave\"\n        }\n      },\n      {\n        \"id\":
    31,\n        \"name\": \"Pfennig''s heterotrophic salts solution\",\n        \"volume\":
    26,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\":
    \"Ammonium chloride\",\n            \"compound_id\": 57,\n            \"amount\":
    0.35,\n            \"unit\": \"g\",\n            \"g_l\": 13.4615,\n            \"mmol_l\":
    251.665,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    2,\n            \"compound\": \"Ammonium acetate\",\n            \"compound_id\":
    58,\n            \"amount\": 0.25,\n            \"unit\": \"g\",\n            \"g_l\":
    9.61539,\n            \"mmol_l\": 124.746,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    5,\n            \"compound\": \"MgSO4 x 7 H2O\",\n            \"compound_id\":
    8,\n            \"amount\": 0.5,\n            \"unit\": \"g\",\n            \"g_l\":
    19.2308,\n            \"mmol_l\": 78.0229,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    6,\n            \"compound\": \"KCl\",\n            \"compound_id\": 61,\n            \"amount\":
    0.35,\n            \"unit\": \"g\",\n            \"g_l\": 13.4615,\n            \"mmol_l\":
    180.571,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    7,\n            \"compound\": \"KH2PO4\",\n            \"compound_id\": 11,\n            \"amount\":
    0.35,\n            \"unit\": \"g\",\n            \"g_l\": 13.4615,\n            \"mmol_l\":
    98.9201,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    8,\n            \"solution\": \"Trace element solution SL-12 B\",\n            \"solution_id\":
    33,\n            \"amount\": 1,\n            \"unit\": \"ml\",\n            \"optional\":
    0\n          },\n          {\n            \"recipe_order\": 9,\n            \"compound\":
    \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\":
    25,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\":
    [\n          {\n            \"step\": \"Filter sterilize into sterile, gas-tight,
    100 ml screw-cap bottle.\"\n          }\n        ],\n        \"equipment\": {\n          \"3563\":
    \"Filter\"\n        }\n      },\n      {\n        \"id\": 32,\n        \"name\":
    \"Vitamin B12 solution\",\n        \"volume\": 100,\n        \"recipe\": [\n          {\n            \"recipe_order\":
    1,\n            \"compound\": \"Vitamin B12\",\n            \"compound_id\": 18,\n            \"amount\":
    0.01,\n            \"unit\": \"g\",\n            \"g_l\": 0.1,\n            \"mmol_l\":
    0.073779,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    2,\n            \"compound\": \"Distilled water\",\n            \"compound_id\":
    4,\n            \"amount\": 100,\n            \"unit\": \"ml\",\n            \"optional\":
    0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\":
    \"Filter sterilized\"\n          }\n        ],\n        \"equipment\": {\n          \"5492\":
    \"Filter\"\n        }\n      },\n      {\n        \"id\": 33,\n        \"name\":
    \"Trace element solution SL-12 B\",\n        \"volume\": 1000,\n        \"recipe\":
    [\n          {\n            \"recipe_order\": 1,\n            \"compound\": \"Na2-EDTA\",\n            \"compound_id\":
    34,\n            \"amount\": 3,\n            \"unit\": \"g\",\n            \"g_l\":
    3,\n            \"mmol_l\": 8.9231,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    2,\n            \"compound\": \"FeSO4 x 7 H2O\",\n            \"compound_id\":
    12,\n            \"amount\": 1.1,\n            \"unit\": \"g\",\n            \"g_l\":
    1.1,\n            \"mmol_l\": 3.95662,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    3,\n            \"compound\": \"CoCl2 x 6 H2O\",\n            \"compound_id\":
    38,\n            \"amount\": 190,\n            \"unit\": \"mg\",\n            \"g_l\":
    0.19,\n            \"mmol_l\": 1.46335,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    4,\n            \"compound\": \"MnCl2 x 2 H2O\",\n            \"compound_id\":
    63,\n            \"amount\": 50,\n            \"unit\": \"mg\",\n            \"g_l\":
    0.05,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    5,\n            \"compound\": \"ZnCl2\",\n            \"compound_id\": 64,\n            \"amount\":
    42,\n            \"unit\": \"mg\",\n            \"g_l\": 0.042,\n            \"mmol_l\":
    0.308144,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    6,\n            \"compound\": \"NiCl2 x 6 H2O\",\n            \"compound_id\":
    40,\n            \"amount\": 24,\n            \"unit\": \"mg\",\n            \"g_l\":
    0.024,\n            \"mmol_l\": 0.185187,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    7,\n            \"compound\": \"Na2MoO4 x 2 H2O\",\n            \"compound_id\":
    9,\n            \"amount\": 18,\n            \"unit\": \"mg\",\n            \"g_l\":
    0.018,\n            \"mmol_l\": 0.0743955,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    8,\n            \"compound\": \"H3BO3\",\n            \"compound_id\": 37,\n            \"amount\":
    300,\n            \"unit\": \"mg\",\n            \"g_l\": 0.3,\n            \"mmol_l\":
    4.85123,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    9,\n            \"compound\": \"CuCl2 x 2 H2O\",\n            \"compound_id\":
    39,\n            \"amount\": 2,\n            \"unit\": \"mg\",\n            \"g_l\":
    0.002,\n            \"mmol_l\": 0.0117314,\n            \"optional\": 0\n          },\n          {\n            \"recipe_order\":
    10,\n            \"compound\": \"Distilled water\",\n            \"compound_id\":
    4,\n            \"amount\": 1000,\n            \"unit\": \"ml\",\n            \"optional\":
    0\n          }\n        ],\n        \"steps\": [\n          {\n            \"step\":
    \"Adjust pH to 6.0.\"\n          }\n        ],\n        \"equipment\": {\n          \"572\":
    \"Ice bath\",\n          \"2369\": \"Filter\"\n        }\n      },\n      {\n        \"id\":
    34,\n        \"name\": \"Neutralized sulfide solution 3% (w/v)\",\n        \"volume\":
    100,\n        \"recipe\": [\n          {\n            \"recipe_order\": 1,\n            \"compound\":
    \"Na2S x 9 H2O\",\n            \"compound_id\": 54,\n            \"amount\": 3,\n            \"unit\":
    \"g\",\n            \"g_l\": 30,\n            \"mmol_l\": 124.905,\n            \"optional\":
    0\n          },\n          {\n            \"recipe_order\": 2,\n            \"compound\":
    \"Distilled water\",\n            \"compound_id\": 4,\n            \"amount\":
    100,\n            \"unit\": \"ml\",\n            \"optional\": 0\n          }\n        ],\n        \"steps\":
    [\n          {\n            \"step\": \"The sulfide solution is prepared in a
    250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer.
    The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at
    121°C. After cooling to room temperature the pH is adjusted to about 7.0 by adding
    of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle.\"\n          }\n        ]\n      }\n    ]\n  }\n}\n"}],
    "decision": "unsupported", "rationale": "The primary expressly supplies0.25 g
    in solutionE. The current API omits this ingredient from E;25 ml water plus1 ml
    trace addition is not an explicit final-volume declaration. Preserve the primary
    batch mass and the provider omission, but the local9.61539 g/L denominator is
    not independently authenticated.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "9.61539",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary expressly
    supplies0.25 g in solutionE. The current API omits this ingredient from E;25 ml
    water plus1 ml trace addition is not an explicit final-volume declaration. Preserve
    the primary batch mass and the provider omission, but the local9.61539 g/L denominator
    is not independently authenticated."}]}, {"quantity_id": "q16", "topic": "Scoped
    DSM28 MgSO4 x 7 H2O", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[5].recipe[2]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    19.2308,\n                        \"mmol_l\": 78.0229,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "MgSO4 x 7 H2O", "compound_id": 8, "amount": 0.5, "unit": "g", "g_l": 19.2308,
    "mmol_l": 78.0229, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "The current provider explicitly declares this rate for
    Pfennig''s heterotrophic salts solution, a component solution. Preserve its source
    batch amount and stock rate at that stage; it is incorrectly exposed as a direct
    base-medium ingredient and must not transfer unchanged to421.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path":
    "ingredients[9].concentration", "stored_value": {"value": "19.2308", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The current provider explicitly declares
    this rate for Pfennig''s heterotrophic salts solution, a component solution. Preserve
    its source batch amount and stock rate at that stage; it is incorrectly exposed
    as a direct base-medium ingredient and must not transfer unchanged to421."}]},
    {"quantity_id": "q17", "topic": "Scoped DSM28 KCl", "source": [{"evidence_id":
    "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[5].recipe[3]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\":
    0.35,\n                        \"unit\": \"g\",\n                        \"g_l\":
    13.4615,\n                        \"mmol_l\": 180.571,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "KCl", "compound_id": 61, "amount": 0.35, "unit": "g", "g_l": 13.4615, "mmol_l":
    180.571, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "The current provider explicitly declares this rate for Pfennig''s
    heterotrophic salts solution, a component solution. Preserve its source batch
    amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium
    ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[10].concentration",
    "stored_value": {"value": "13.4615", "unit": "G_PER_L"}, "decision": "correct",
    "rationale": "The current provider explicitly declares this rate for Pfennig''s
    heterotrophic salts solution, a component solution. Preserve its source batch
    amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium
    ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q18",
    "topic": "Scoped DSM28 KH2PO4", "source": [{"evidence_id": "api28", "reference":
    "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin",
    "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[5].recipe[4]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\":
    0.35,\n                        \"unit\": \"g\",\n                        \"g_l\":
    13.4615,\n                        \"mmol_l\": 98.9201,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "KH2PO4", "compound_id": 11, "amount": 0.35, "unit": "g", "g_l": 13.4615, "mmol_l":
    98.9201, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "The current provider explicitly declares this rate for Pfennig''s
    heterotrophic salts solution, a component solution. Preserve its source batch
    amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium
    ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[11].concentration",
    "stored_value": {"value": "13.4615", "unit": "G_PER_L"}, "decision": "correct",
    "rationale": "The current provider explicitly declares this rate for Pfennig''s
    heterotrophic salts solution, a component solution. Preserve its source batch
    amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium
    ingredient and must not transfer unchanged to421."}]}, {"quantity_id": "q19",
    "topic": "Scoped DSM28 Vitamin B12", "source": [{"evidence_id": "api28", "reference":
    "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin",
    "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[6].recipe[0]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\":
    0.01,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.073779,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Vitamin B12", "compound_id": 18, "amount": 0.01, "unit": "g", "g_l": 0.1, "mmol_l":
    0.073779, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "The current provider explicitly declares this rate for Vitamin B12
    solution, a component solution. Preserve its source batch amount and stock rate
    at that stage; it is incorrectly exposed as a direct base-medium ingredient and
    must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider
    explicitly declares this rate for Vitamin B12 solution, a component solution.
    Preserve its source batch amount and stock rate at that stage; it is incorrectly
    exposed as a direct base-medium ingredient and must not transfer unchanged to421."}]},
    {"quantity_id": "q20", "topic": "Scoped DSM28 Na2-EDTA", "source": [{"evidence_id":
    "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[7].recipe[0]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Na2-EDTA\",\n                        \"compound_id\": 34,\n                        \"amount\":
    3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    3,\n                        \"mmol_l\": 8.9231,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Na2-EDTA", "compound_id": 34, "amount": 3, "unit": "g", "g_l": 3, "mmol_l": 8.9231,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "correct", "rationale":
    "The current provider explicitly declares this rate for Trace element solution
    SL-12 B, a component solution. Preserve its source batch amount and stock rate
    at that stage; it is incorrectly exposed as a direct base-medium ingredient and
    must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "3",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider
    explicitly declares this rate for Trace element solution SL-12 B, a component
    solution. Preserve its source batch amount and stock rate at that stage; it is
    incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged
    to421."}]}, {"quantity_id": "q21", "topic": "Scoped DSM28 FeSO4 x 7 H2O", "source":
    [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[7].recipe[1]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\":
    1.1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1.1,\n                        \"mmol_l\": 3.95662,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "FeSO4 x 7 H2O", "compound_id": 12, "amount": 1.1, "unit": "g", "g_l": 1.1, "mmol_l":
    3.95662, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "The current provider explicitly declares this rate for Trace element
    solution SL-12 B, a component solution. Preserve its source batch amount and stock
    rate at that stage; it is incorrectly exposed as a direct base-medium ingredient
    and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "1.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider
    explicitly declares this rate for Trace element solution SL-12 B, a component
    solution. Preserve its source batch amount and stock rate at that stage; it is
    incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged
    to421."}]}, {"quantity_id": "q22", "topic": "Scoped DSM28 CoCl2 x 6 H2O", "source":
    [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[7].recipe[2]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\":
    190,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "CoCl2 x 6 H2O", "compound_id": 38, "amount": 190, "unit": "mg", "g_l": 0.19,
    "mmol_l": 1.46335, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "The current provider explicitly declares this rate for
    Trace element solution SL-12 B, a component solution. Preserve its source batch
    amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium
    ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[15].concentration",
    "stored_value": {"value": "0.19", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "The current provider explicitly declares this rate for Trace element solution
    SL-12 B, a component solution. Preserve its source batch amount and stock rate
    at that stage; it is incorrectly exposed as a direct base-medium ingredient and
    must not transfer unchanged to421."}]}, {"quantity_id": "q23", "topic": "Scoped
    DSM28 MnCl2 x 2 H2O", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[7].recipe[3]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"MnCl2 x 2 H2O\",\n                        \"compound_id\": 63,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 4, "compound": "MnCl2 x 2 H2O", "compound_id": 63, "amount":
    50, "unit": "mg", "g_l": 0.05, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "The current provider explicitly declares this rate for
    Trace element solution SL-12 B, a component solution. Preserve its source batch
    amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium
    ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[16].concentration",
    "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "The current provider explicitly declares this rate for Trace element solution
    SL-12 B, a component solution. Preserve its source batch amount and stock rate
    at that stage; it is incorrectly exposed as a direct base-medium ingredient and
    must not transfer unchanged to421."}]}, {"quantity_id": "q24", "topic": "Scoped
    DSM28 ZnCl2", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[7].recipe[4]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\":
    42,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.042,\n                        \"mmol_l\": 0.308144,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "ZnCl2", "compound_id": 64, "amount": 42, "unit": "mg", "g_l": 0.042, "mmol_l":
    0.308144, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "The current provider explicitly declares this rate for Trace element
    solution SL-12 B, a component solution. Preserve its source batch amount and stock
    rate at that stage; it is incorrectly exposed as a direct base-medium ingredient
    and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.042",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider
    explicitly declares this rate for Trace element solution SL-12 B, a component
    solution. Preserve its source batch amount and stock rate at that stage; it is
    incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged
    to421."}]}, {"quantity_id": "q25", "topic": "Scoped DSM28 NiCl2 x 6 H2O", "source":
    [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[7].recipe[5]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\":
    24,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "NiCl2 x 6 H2O", "compound_id": 40, "amount": 24, "unit": "mg", "g_l": 0.024,
    "mmol_l": 0.185187, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "The current provider explicitly declares this rate for
    Trace element solution SL-12 B, a component solution. Preserve its source batch
    amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium
    ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[18].concentration",
    "stored_value": {"value": "0.024", "unit": "G_PER_L"}, "decision": "correct",
    "rationale": "The current provider explicitly declares this rate for Trace element
    solution SL-12 B, a component solution. Preserve its source batch amount and stock
    rate at that stage; it is incorrectly exposed as a direct base-medium ingredient
    and must not transfer unchanged to421."}]}, {"quantity_id": "q26", "topic": "Scoped
    DSM28 Na2MoO4 x 2 H2O", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[7].recipe[6]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\":
    18,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.018,\n                        \"mmol_l\": 0.0743955,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 18, "unit": "mg", "g_l": 0.018,
    "mmol_l": 0.0743955, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "The current provider explicitly declares this rate for
    Trace element solution SL-12 B, a component solution. Preserve its source batch
    amount and stock rate at that stage; it is incorrectly exposed as a direct base-medium
    ingredient and must not transfer unchanged to421.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "ingredients[19].concentration",
    "stored_value": {"value": "0.018", "unit": "G_PER_L"}, "decision": "correct",
    "rationale": "The current provider explicitly declares this rate for Trace element
    solution SL-12 B, a component solution. Preserve its source batch amount and stock
    rate at that stage; it is incorrectly exposed as a direct base-medium ingredient
    and must not transfer unchanged to421."}]}, {"quantity_id": "q27", "topic": "Scoped
    DSM28 H3BO3", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[7].recipe[7]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\":
    300,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound":
    "H3BO3", "compound_id": 37, "amount": 300, "unit": "mg", "g_l": 0.3, "mmol_l":
    4.85123, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "The current provider explicitly declares this rate for Trace element
    solution SL-12 B, a component solution. Preserve its source batch amount and stock
    rate at that stage; it is incorrectly exposed as a direct base-medium ingredient
    and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider
    explicitly declares this rate for Trace element solution SL-12 B, a component
    solution. Preserve its source batch amount and stock rate at that stage; it is
    incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged
    to421."}]}, {"quantity_id": "q28", "topic": "Scoped DSM28 CuCl2 x 2 H2O", "source":
    [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[7].recipe[8]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\":
    2,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound":
    "CuCl2 x 2 H2O", "compound_id": 39, "amount": 2, "unit": "mg", "g_l": 0.002, "mmol_l":
    0.0117314, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "The current provider explicitly declares this rate for Trace element
    solution SL-12 B, a component solution. Preserve its source batch amount and stock
    rate at that stage; it is incorrectly exposed as a direct base-medium ingredient
    and must not transfer unchanged to421.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.002",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The current provider
    explicitly declares this rate for Trace element solution SL-12 B, a component
    solution. Preserve its source batch amount and stock rate at that stage; it is
    incorrectly exposed as a direct base-medium ingredient and must not transfer unchanged
    to421."}]}, {"quantity_id": "q29", "topic": "DSM28 source-only Main sol. 28: Solution
    A", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\":
    \"Solution A\",\n                        \"solution_id\": 27,\n                        \"amount\":
    460,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "solution":
    "Solution A", "solution_id": 27, "amount": 460, "unit": "ml", "optional": 0},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact
    Main sol. 28 recipe-stage quantity. Bare ml amounts remain batch/addition quantities;
    only explicitly printed ml/l is a provider per-litre declaration. Water rows are
    not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Rebuild the absent named solution/water topology with this exact stage. Retain
    existing preparation text as separately credited.", "missing": true}]}, {"quantity_id":
    "q30", "topic": "DSM28 source-only Main sol. 28: Resazurin solution", "source":
    [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\":
    \"Resazurin solution\",\n                        \"solution_id\": 30,\n                        \"amount\":
    450,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "solution":
    "Resazurin solution", "solution_id": 30, "amount": 450, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact
    Main sol. 28 recipe-stage quantity. Bare ml amounts remain batch/addition quantities;
    only explicitly printed ml/l is a provider per-litre declaration. Water rows are
    not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Rebuild the absent named solution/water topology with this exact stage. Retain
    existing preparation text as separately credited.", "missing": true}]}, {"quantity_id":
    "q31", "topic": "DSM28 source-only Main sol. 28: Bicarbonate solution", "source":
    [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\":
    \"Bicarbonate solution\",\n                        \"solution_id\": 29,\n                        \"amount\":
    50,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "solution":
    "Bicarbonate solution", "solution_id": 29, "amount": 50, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact
    Main sol. 28 recipe-stage quantity. Bare ml amounts remain batch/addition quantities;
    only explicitly printed ml/l is a provider per-litre declaration. Water rows are
    not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Rebuild the absent named solution/water topology with this exact stage. Retain
    existing preparation text as separately credited.", "missing": true}]}, {"quantity_id":
    "q32", "topic": "DSM28 source-only Main sol. 28: Pfennig''s heterotrophic salts
    solution", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\":
    \"Pfennig''s heterotrophic salts solution\",\n                        \"solution_id\":
    31,\n                        \"amount\": 26,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 4, "solution": "Pfennig''s heterotrophic salts solution", "solution_id":
    31, "amount": 26, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "add", "rationale": "Preserve the exact Main sol. 28 recipe-stage
    quantity. Bare ml amounts remain batch/addition quantities; only explicitly printed
    ml/l is a provider per-litre declaration. Water rows are not measured final volumes.",
    "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Rebuild the absent named solution/water topology with this exact stage. Retain
    existing preparation text as separately credited.", "missing": true}]}, {"quantity_id":
    "q33", "topic": "DSM28 source-only Main sol. 28: Sulfide solution, 1.5%", "source":
    [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"solution\":
    \"Sulfide solution, 1.5%\",\n                        \"solution_id\": 28,\n                        \"amount\":
    40,\n                        \"unit\": \"ml/l\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "solution":
    "Sulfide solution, 1.5%", "solution_id": 28, "amount": 40, "unit": "ml/l", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact
    Main sol. 28 recipe-stage quantity. Bare ml amounts remain batch/addition quantities;
    only explicitly printed ml/l is a provider per-litre declaration. Water rows are
    not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Rebuild the absent named solution/water topology with this exact stage. Retain
    existing preparation text as separately credited.", "missing": true}]}, {"quantity_id":
    "q34", "topic": "DSM28 source-only Main sol. 28: Vitamin B12 solution", "source":
    [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\":
    \"Vitamin B12 solution\",\n                        \"solution_id\": 32,\n                        \"amount\":
    1,\n                        \"unit\": \"ml/l\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "solution":
    "Vitamin B12 solution", "solution_id": 32, "amount": 1, "unit": "ml/l", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact
    Main sol. 28 recipe-stage quantity. Bare ml amounts remain batch/addition quantities;
    only explicitly printed ml/l is a provider per-litre declaration. Water rows are
    not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Rebuild the absent named solution/water topology with this exact stage. Retain
    existing preparation text as separately credited.", "missing": true}]}, {"quantity_id":
    "q35", "topic": "DSM28 source-only Main sol. 28: Neutralized sulfide solution
    3% (w/v)", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\":
    \"Neutralized sulfide solution 3% (w/v)\",\n                        \"solution_id\":
    34,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 7, "solution": "Neutralized sulfide solution 3% (w/v)", "solution_id":
    34, "amount": 10, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "conflict", "rationale": "Preserve the exact Main sol. 28 recipe-stage
    quantity. Bare ml amounts remain batch/addition quantities; only explicitly printed
    ml/l is a provider per-litre declaration. Water rows are not measured final volumes.
    The10 ml feeding row conflicts with variable feeding prose and the primary’s unfixed
    periodic feed; do not promote it to a universal dose.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "Rebuild the absent named
    solution/water topology with this exact stage. Retain existing preparation text
    as separately credited.", "missing": true}]}, {"quantity_id": "q36", "topic":
    "DSM28 source-only Solution A: Distilled water", "source": [{"evidence_id": "api28",
    "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin",
    "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    460,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "Distilled water", "compound_id": 4, "amount": 460, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact
    Solution A recipe-stage quantity. Bare ml amounts remain batch/addition quantities;
    only explicitly printed ml/l is a provider per-litre declaration. Water rows are
    not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Rebuild the absent named solution/water topology with this exact stage. Retain
    existing preparation text as separately credited.", "missing": true}]}, {"quantity_id":
    "q37", "topic": "DSM28 source-only Sulfide solution, 1.5%: Distilled water", "source":
    [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[2].recipe[1]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    135,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "Distilled water", "compound_id": 4, "amount": 135, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact
    Sulfide solution, 1.5% recipe-stage quantity. Bare ml amounts remain batch/addition
    quantities; only explicitly printed ml/l is a provider per-litre declaration.
    Water rows are not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Rebuild the absent named solution/water topology with this exact stage. Retain
    existing preparation text as separately credited.", "missing": true}]}, {"quantity_id":
    "q38", "topic": "DSM28 source-only Bicarbonate solution: H2O", "source": [{"evidence_id":
    "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[3].recipe[1]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"H2O\",\n                        \"compound_id\": 56,\n                        \"amount\":
    50,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "H2O", "compound_id": 56, "amount": 50, "unit": "ml", "optional": 0}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}], "decision": "add", "rationale": "Preserve the exact Bicarbonate
    solution recipe-stage quantity. Bare ml amounts remain batch/addition quantities;
    only explicitly printed ml/l is a provider per-litre declaration. Water rows are
    not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Rebuild the absent named solution/water topology with this exact stage. Retain
    existing preparation text as separately credited.", "missing": true}]}, {"quantity_id":
    "q39", "topic": "DSM28 source-only Resazurin solution: Distilled water", "source":
    [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[4].recipe[1]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    450,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "Distilled water", "compound_id": 4, "amount": 450, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact
    Resazurin solution recipe-stage quantity. Bare ml amounts remain batch/addition
    quantities; only explicitly printed ml/l is a provider per-litre declaration.
    Water rows are not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Rebuild the absent named solution/water topology with this exact stage. Retain
    existing preparation text as separately credited.", "missing": true}]}, {"quantity_id":
    "q40", "topic": "DSM28 source-only Pfennig''s heterotrophic salts solution: Trace
    element solution SL-12 B", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[5].recipe[5]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\":
    \"Trace element solution SL-12 B\",\n                        \"solution_id\":
    33,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 8, "solution": "Trace element solution SL-12 B", "solution_id":
    33, "amount": 1, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "add", "rationale": "Preserve the exact Pfennig''s heterotrophic salts solution
    recipe-stage quantity. Bare ml amounts remain batch/addition quantities; only
    explicitly printed ml/l is a provider per-litre declaration. Water rows are not
    measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Rebuild the absent named solution/water topology with this exact stage. Retain
    existing preparation text as separately credited.", "missing": true}]}, {"quantity_id":
    "q41", "topic": "DSM28 source-only Pfennig''s heterotrophic salts solution: Distilled
    water", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[5].recipe[6]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    25,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound":
    "Distilled water", "compound_id": 4, "amount": 25, "unit": "ml", "optional": 0},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact
    Pfennig''s heterotrophic salts solution recipe-stage quantity. Bare ml amounts
    remain batch/addition quantities; only explicitly printed ml/l is a provider per-litre
    declaration. Water rows are not measured final volumes.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "Rebuild the
    absent named solution/water topology with this exact stage. Retain existing preparation
    text as separately credited.", "missing": true}]}, {"quantity_id": "q42", "topic":
    "DSM28 source-only Vitamin B12 solution: Distilled water", "source": [{"evidence_id":
    "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[6].recipe[1]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    100,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "Distilled water", "compound_id": 4, "amount": 100, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact
    Vitamin B12 solution recipe-stage quantity. Bare ml amounts remain batch/addition
    quantities; only explicitly printed ml/l is a provider per-litre declaration.
    Water rows are not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Rebuild the absent named solution/water topology with this exact stage. Retain
    existing preparation text as separately credited.", "missing": true}]}, {"quantity_id":
    "q43", "topic": "DSM28 source-only Trace element solution SL-12 B: Distilled water",
    "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[7].recipe[9]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact
    Trace element solution SL-12 B recipe-stage quantity. Bare ml amounts remain batch/addition
    quantities; only explicitly printed ml/l is a provider per-litre declaration.
    Water rows are not measured final volumes.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Rebuild the absent named solution/water topology with this exact stage. Retain
    existing preparation text as separately credited.", "missing": true}]}, {"quantity_id":
    "q44", "topic": "DSM28 source-only Neutralized sulfide solution 3% (w/v): Distilled
    water", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[8].recipe[1]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    100,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "Distilled water", "compound_id": 4, "amount": 100, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the exact
    Neutralized sulfide solution 3% (w/v) recipe-stage quantity. Bare ml amounts remain
    batch/addition quantities; only explicitly printed ml/l is a provider per-litre
    declaration. Water rows are not measured final volumes.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "Rebuild the
    absent named solution/water topology with this exact stage. Retain existing preparation
    text as separately credited.", "missing": true}]}, {"quantity_id": "q45", "topic":
    "Retained DSM421 owner preparation step 1", "source": [{"evidence_id": "api421",
    "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin",
    "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T09:27:43.186753Z",
    "quote": "{\n                        \"step\": \"Supplement medium 28 with NaCl
    (10%), MgCl2 x 6 H2O (0.3%) Na-acetate (0.05%) and sodium thiosulfate (0.05%).
    Incubate at 500 to 1000 Lux light intensity.\"\n                    }", "exact_decoded_object":
    {"step": "Supplement medium 28 with NaCl (10%), MgCl2 x 6 H2O (0.3%) Na-acetate
    (0.05%) and sodium thiosulfate (0.05%). Incubate at 500 to 1000 Lux light intensity."},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The
    current provider exactly supports this retained description at its stated solution/preparation
    stage. Keep the existing instruction and add scoped root evidence; do not mistake
    code-wide step concatenation for whole-medium applicability.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml",
    "field_path": "preparation_steps[0].description", "stored_value": "Supplement
    medium 28 with NaCl (10%), MgCl2 x 6 H2O (0.3%) Na-acetate (0.05%) and sodium
    thiosulfate (0.05%). Incubate at 500 to 1000 Lux light intensity.", "decision":
    "evidence_only", "rationale": "The current provider exactly supports this retained
    description at its stated solution/preparation stage. Keep the existing instruction
    and add scoped root evidence; do not mistake code-wide step concatenation for
    whole-medium applicability."}]}, {"quantity_id": "q46", "topic": "Retained DSM421
    owner preparation step 2", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52",
    "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T09:27:43.186753Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"step\":
    \"Adjust the pH with filter-sterilised 1M Na2CO3 to 7.1-7.3.\"\n                    }",
    "exact_decoded_object": {"recipe_order": 7, "step": "Adjust the pH with filter-sterilised
    1M Na2CO3 to 7.1-7.3."}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "evidence_only",
    "rationale": "The current provider exactly supports this retained description
    at its stated solution/preparation stage. Keep the existing instruction and add
    scoped root evidence; do not mistake code-wide step concatenation for whole-medium
    applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml",
    "field_path": "preparation_steps[1].description", "stored_value": "Adjust the
    pH with filter-sterilised 1M Na2CO3 to 7.1-7.3.", "decision": "evidence_only",
    "rationale": "The current provider exactly supports this retained description
    at its stated solution/preparation stage. Keep the existing instruction and add
    scoped root evidence; do not mistake code-wide step concatenation for whole-medium
    applicability."}]}, {"quantity_id": "q47", "topic": "Retained DSM421 owner preparation
    step 3", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52",
    "locator": "$.data.solutions[1].steps[1]", "accessed_at": "2026-10-28T09:27:43.186753Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"step\":
    \"If needed, aliquot into sterile, N<sub>2</sub> gassed screw-cap tubes under
    N<sub>2</sub> gas.\"\n                    }", "exact_decoded_object": {"recipe_order":
    7, "step": "If needed, aliquot into sterile, N<sub>2</sub> gassed screw-cap tubes
    under N<sub>2</sub> gas."}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "evidence_only",
    "rationale": "The current provider exactly supports this retained description
    at its stated solution/preparation stage. Keep the existing instruction and add
    scoped root evidence; do not mistake code-wide step concatenation for whole-medium
    applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml",
    "field_path": "preparation_steps[2].description", "stored_value": "If needed,
    aliquot into sterile, N<sub>2</sub> gassed screw-cap tubes under N<sub>2</sub>
    gas.", "decision": "evidence_only", "rationale": "The current provider exactly
    supports this retained description at its stated solution/preparation stage. Keep
    the existing instruction and add scoped root evidence; do not mistake code-wide
    step concatenation for whole-medium applicability."}]}, {"quantity_id": "q48",
    "topic": "Retained DSM421 owner preparation step 4", "source": [{"evidence_id":
    "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52",
    "locator": "$.data.solutions[1].steps[2]", "accessed_at": "2026-10-28T09:27:43.186753Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"step\":
    \"During the first 24 h, the iron of the medium precipitates in the form of black
    flocks. No other sediment should arise in the otherwise clear medium.\"\n                    }",
    "exact_decoded_object": {"recipe_order": 7, "step": "During the first 24 h, the
    iron of the medium precipitates in the form of black flocks. No other sediment
    should arise in the otherwise clear medium."}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "evidence_only", "rationale": "The current provider exactly supports this retained
    description at its stated solution/preparation stage. Keep the existing instruction
    and add scoped root evidence; do not mistake code-wide step concatenation for
    whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml",
    "field_path": "preparation_steps[3].description", "stored_value": "During the
    first 24 h, the iron of the medium precipitates in the form of black flocks. No
    other sediment should arise in the otherwise clear medium.", "decision": "evidence_only",
    "rationale": "The current provider exactly supports this retained description
    at its stated solution/preparation stage. Keep the existing instruction and add
    scoped root evidence; do not mistake code-wide step concatenation for whole-medium
    applicability."}]}, {"quantity_id": "q49", "topic": "Retained DSM421 owner preparation
    step 5", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52",
    "locator": "$.data.solutions[1].steps[3]", "accessed_at": "2026-10-28T09:27:43.186753Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"step\":
    \"Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble
    with N2/CO2 and autoclave at 121\\u00b0C for 15 min (as decribed below).\"\n                    }",
    "exact_decoded_object": {"recipe_order": 2, "step": "Aliquot Solution A into 100
    mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave
    at 121°C for 15 min (as decribed below)."}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "evidence_only", "rationale": "The current provider exactly supports this retained
    description at its stated solution/preparation stage. Keep the existing instruction
    and add scoped root evidence; do not mistake code-wide step concatenation for
    whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml",
    "field_path": "preparation_steps[4].description", "stored_value": "Aliquot Solution
    A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and
    autoclave at 121°C for 15 min (as decribed below).", "decision": "evidence_only",
    "rationale": "The current provider exactly supports this retained description
    at its stated solution/preparation stage. Keep the existing instruction and add
    scoped root evidence; do not mistake code-wide step concatenation for whole-medium
    applicability."}]}, {"quantity_id": "q50", "topic": "Retained DSM421 owner preparation
    step 6", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52",
    "locator": "$.data.solutions[1].steps[4]", "accessed_at": "2026-10-28T09:27:43.186753Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"step\":
    \"Prepare the following solutions (resazurin, bicarbonate and Pfennig''s heterotrophic
    salts) and sterilize as given below.\"\n                    }", "exact_decoded_object":
    {"recipe_order": 2, "step": "Prepare the following solutions (resazurin, bicarbonate
    and Pfennig''s heterotrophic salts) and sterilize as given below."}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}], "decision": "evidence_only", "rationale": "The current provider
    exactly supports this retained description at its stated solution/preparation
    stage. Keep the existing instruction and add scoped root evidence; do not mistake
    code-wide step concatenation for whole-medium applicability.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml",
    "field_path": "preparation_steps[5].description", "stored_value": "Prepare the
    following solutions (resazurin, bicarbonate and Pfennig''s heterotrophic salts)
    and sterilize as given below.", "decision": "evidence_only", "rationale": "The
    current provider exactly supports this retained description at its stated solution/preparation
    stage. Keep the existing instruction and add scoped root evidence; do not mistake
    code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id":
    "q51", "topic": "Retained DSM421 owner preparation step 7", "source": [{"evidence_id":
    "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52",
    "locator": "$.data.solutions[1].steps[5]", "accessed_at": "2026-10-28T09:27:43.186753Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"step\":
    \"Add bicarbonate solution and Pfennig''s heterotrophic salts to the resazurin
    (complete volumina, i.e. 50 mL bicarbonate solution and 26 mL Pfennig''s heterotrophic
    salts solution). Bubble with CO2 in an ice bath under sterile conditions.\"\n                    }",
    "exact_decoded_object": {"recipe_order": 5, "step": "Add bicarbonate solution
    and Pfennig''s heterotrophic salts to the resazurin (complete volumina, i.e. 50
    mL bicarbonate solution and 26 mL Pfennig''s heterotrophic salts solution). Bubble
    with CO2 in an ice bath under sterile conditions."}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "evidence_only", "rationale": "The current provider exactly supports
    this retained description at its stated solution/preparation stage. Keep the existing
    instruction and add scoped root evidence; do not mistake code-wide step concatenation
    for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml",
    "field_path": "preparation_steps[6].description", "stored_value": "Add bicarbonate
    solution and Pfennig''s heterotrophic salts to the resazurin (complete volumina,
    i.e. 50 mL bicarbonate solution and 26 mL Pfennig''s heterotrophic salts solution).
    Bubble with CO2 in an ice bath under sterile conditions.", "decision": "evidence_only",
    "rationale": "The current provider exactly supports this retained description
    at its stated solution/preparation stage. Keep the existing instruction and add
    scoped root evidence; do not mistake code-wide step concatenation for whole-medium
    applicability."}]}, {"quantity_id": "q52", "topic": "Retained DSM421 owner preparation
    step 8", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52",
    "locator": "$.data.solutions[1].steps[6]", "accessed_at": "2026-10-28T09:27:43.186753Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"step\":
    \"Fill 50 ml of this mixture to each bottle of solution A (46 mL + 50 mL).\"\n                    }",
    "exact_decoded_object": {"recipe_order": 5, "step": "Fill 50 ml of this mixture
    to each bottle of solution A (46 mL + 50 mL)."}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "evidence_only", "rationale": "The current provider exactly supports
    this retained description at its stated solution/preparation stage. Keep the existing
    instruction and add scoped root evidence; do not mistake code-wide step concatenation
    for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml",
    "field_path": "preparation_steps[7].description", "stored_value": "Fill 50 ml
    of this mixture to each bottle of solution A (46 mL + 50 mL).", "decision": "evidence_only",
    "rationale": "The current provider exactly supports this retained description
    at its stated solution/preparation stage. Keep the existing instruction and add
    scoped root evidence; do not mistake code-wide step concatenation for whole-medium
    applicability."}]}, {"quantity_id": "q53", "topic": "Retained DSM421 owner preparation
    step 9", "source": [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52",
    "locator": "$.data.solutions[1].steps[7]", "accessed_at": "2026-10-28T09:27:43.186753Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"step\":
    \"Before use, add 4 ml sulfide solution (1.5%) and 0.1 ml Vitamin B12 solution
    to each 100 mL bottle.\"\n                    }", "exact_decoded_object": {"recipe_order":
    5, "step": "Before use, add 4 ml sulfide solution (1.5%) and 0.1 ml Vitamin B12
    solution to each 100 mL bottle."}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "evidence_only", "rationale": "The current provider exactly supports this retained
    description at its stated solution/preparation stage. Keep the existing instruction
    and add scoped root evidence; do not mistake code-wide step concatenation for
    whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml",
    "field_path": "preparation_steps[8].description", "stored_value": "Before use,
    add 4 ml sulfide solution (1.5%) and 0.1 ml Vitamin B12 solution to each 100 mL
    bottle.", "decision": "evidence_only", "rationale": "The current provider exactly
    supports this retained description at its stated solution/preparation stage. Keep
    the existing instruction and add scoped root evidence; do not mistake code-wide
    step concatenation for whole-medium applicability."}]}, {"quantity_id": "q54",
    "topic": "Retained DSM421 owner preparation step 10", "source": [{"evidence_id":
    "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52",
    "locator": "$.data.solutions[1].steps[8]", "accessed_at": "2026-10-28T09:27:43.186753Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"step\":
    \"Feed the actively growing culture periodically with neutralized 3% solution
    of sodium sulfide (use 1 -3 mL/100 mL depending on strain and cultivation stage)
    to replenish sulfide and with other supplement solutions (see Ref. 3365).\"\n                    }",
    "exact_decoded_object": {"recipe_order": 7, "step": "Feed the actively growing
    culture periodically with neutralized 3% solution of sodium sulfide (use 1 -3
    mL/100 mL depending on strain and cultivation stage) to replenish sulfide and
    with other supplement solutions (see Ref. 3365)."}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "conflict", "rationale": "The current provider supplies variable1–3
    ml/100 ml feeding, while the primary gives only periodic feeding and the provider
    also has a10 ml row. Retain the discrepancy; no universal fixed dose is selected.",
    "layer_assessments": [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml",
    "field_path": "preparation_steps[9].description", "stored_value": "Feed the actively
    growing culture periodically with neutralized 3% solution of sodium sulfide (use
    1 -3 mL/100 mL depending on strain and cultivation stage) to replenish sulfide
    and with other supplement solutions (see Ref. 3365).", "decision": "conflict",
    "rationale": "The current provider supplies variable1–3 ml/100 ml feeding, while
    the primary gives only periodic feeding and the provider also has a10 ml row.
    Retain the discrepancy; no universal fixed dose is selected."}]}, {"quantity_id":
    "q55", "topic": "Retained DSM421 owner preparation step 11", "source": [{"evidence_id":
    "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52",
    "locator": "$.data.solutions[2].steps[0]", "accessed_at": "2026-10-28T09:27:43.186753Z",
    "quote": "{\n                        \"step\": \"The sulfide solution is prepared
    in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer.
    The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at
    121\\u00b0C. After cooling to room temperature the pH is adjusted to about 7.0
    by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle.\"\n                    }",
    "exact_decoded_object": {"step": "The sulfide solution is prepared in a 250 ml
    screw-capped bottle with a butyl rubber septum and a magnetic stirrer. The solution
    is bubbled with nitrogen gas, closed and autoclaved for 15 min. at 121°C. After
    cooling to room temperature the pH is adjusted to about 7.0 by adding of sterile
    2 M H2SO4 drop-wise with a syringe without opening the bottle."}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}], "decision": "evidence_only", "rationale": "The current provider
    exactly supports this retained description at its stated solution/preparation
    stage. Keep the existing instruction and add scoped root evidence; do not mistake
    code-wide step concatenation for whole-medium applicability.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml",
    "field_path": "preparation_steps[10].description", "stored_value": "The sulfide
    solution is prepared in a 250 ml screw-capped bottle with a butyl rubber septum
    and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and
    autoclaved for 15 min. at 121°C. After cooling to room temperature the pH is adjusted
    to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening
    the bottle.", "decision": "evidence_only", "rationale": "The current provider
    exactly supports this retained description at its stated solution/preparation
    stage. Keep the existing instruction and add scoped root evidence; do not mistake
    code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id":
    "q56", "topic": "Retained DSM28 base preparation step 1", "source": [{"evidence_id":
    "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"step\":
    \"Adjust the pH with filter-sterilised 1M Na2CO3 to 7.1-7.3.\"\n                    }",
    "exact_decoded_object": {"recipe_order": 7, "step": "Adjust the pH with filter-sterilised
    1M Na2CO3 to 7.1-7.3."}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "evidence_only",
    "rationale": "The current provider exactly supports this retained description
    at its stated solution/preparation stage. Keep the existing instruction and add
    scoped root evidence; do not mistake code-wide step concatenation for whole-medium
    applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "preparation_steps[0].description", "stored_value": "Adjust the
    pH with filter-sterilised 1M Na2CO3 to 7.1-7.3.", "decision": "evidence_only",
    "rationale": "The current provider exactly supports this retained description
    at its stated solution/preparation stage. Keep the existing instruction and add
    scoped root evidence; do not mistake code-wide step concatenation for whole-medium
    applicability."}]}, {"quantity_id": "q57", "topic": "Retained DSM28 base preparation
    step 2", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[0].steps[1]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"step\":
    \"If needed, aliquot into sterile, N<sub>2</sub> gassed screw-cap tubes under
    N<sub>2</sub> gas.\"\n                    }", "exact_decoded_object": {"recipe_order":
    7, "step": "If needed, aliquot into sterile, N<sub>2</sub> gassed screw-cap tubes
    under N<sub>2</sub> gas."}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "evidence_only",
    "rationale": "The current provider exactly supports this retained description
    at its stated solution/preparation stage. Keep the existing instruction and add
    scoped root evidence; do not mistake code-wide step concatenation for whole-medium
    applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "preparation_steps[1].description", "stored_value": "If needed,
    aliquot into sterile, N<sub>2</sub> gassed screw-cap tubes under N<sub>2</sub>
    gas.", "decision": "evidence_only", "rationale": "The current provider exactly
    supports this retained description at its stated solution/preparation stage. Keep
    the existing instruction and add scoped root evidence; do not mistake code-wide
    step concatenation for whole-medium applicability."}]}, {"quantity_id": "q58",
    "topic": "Retained DSM28 base preparation step 3", "source": [{"evidence_id":
    "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[0].steps[2]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"step\":
    \"During the first 24 h, the iron of the medium precipitates in the form of black
    flocks. No other sediment should arise in the otherwise clear medium.\"\n                    }",
    "exact_decoded_object": {"recipe_order": 7, "step": "During the first 24 h, the
    iron of the medium precipitates in the form of black flocks. No other sediment
    should arise in the otherwise clear medium."}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "evidence_only", "rationale": "The current provider exactly supports this retained
    description at its stated solution/preparation stage. Keep the existing instruction
    and add scoped root evidence; do not mistake code-wide step concatenation for
    whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "preparation_steps[2].description", "stored_value": "During the
    first 24 h, the iron of the medium precipitates in the form of black flocks. No
    other sediment should arise in the otherwise clear medium.", "decision": "evidence_only",
    "rationale": "The current provider exactly supports this retained description
    at its stated solution/preparation stage. Keep the existing instruction and add
    scoped root evidence; do not mistake code-wide step concatenation for whole-medium
    applicability."}]}, {"quantity_id": "q59", "topic": "Retained DSM28 base preparation
    step 4", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[0].steps[3]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"step\":
    \"Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble
    with N2/CO2 and autoclave at 121\\u00b0C for 15 min (as decribed below).\"\n                    }",
    "exact_decoded_object": {"recipe_order": 2, "step": "Aliquot Solution A into 100
    mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave
    at 121°C for 15 min (as decribed below)."}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "evidence_only", "rationale": "The current provider exactly supports this retained
    description at its stated solution/preparation stage. Keep the existing instruction
    and add scoped root evidence; do not mistake code-wide step concatenation for
    whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "preparation_steps[3].description", "stored_value": "Aliquot Solution
    A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and
    autoclave at 121°C for 15 min (as decribed below).", "decision": "evidence_only",
    "rationale": "The current provider exactly supports this retained description
    at its stated solution/preparation stage. Keep the existing instruction and add
    scoped root evidence; do not mistake code-wide step concatenation for whole-medium
    applicability."}]}, {"quantity_id": "q60", "topic": "Retained DSM28 base preparation
    step 5", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[0].steps[4]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"step\":
    \"Prepare the following solutions (resazurin, bicarbonate and Pfennig''s heterotrophic
    salts) and sterilize as given below.\"\n                    }", "exact_decoded_object":
    {"recipe_order": 2, "step": "Prepare the following solutions (resazurin, bicarbonate
    and Pfennig''s heterotrophic salts) and sterilize as given below."}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}], "decision": "evidence_only", "rationale": "The current provider
    exactly supports this retained description at its stated solution/preparation
    stage. Keep the existing instruction and add scoped root evidence; do not mistake
    code-wide step concatenation for whole-medium applicability.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path":
    "preparation_steps[4].description", "stored_value": "Prepare the following solutions
    (resazurin, bicarbonate and Pfennig''s heterotrophic salts) and sterilize as given
    below.", "decision": "evidence_only", "rationale": "The current provider exactly
    supports this retained description at its stated solution/preparation stage. Keep
    the existing instruction and add scoped root evidence; do not mistake code-wide
    step concatenation for whole-medium applicability."}]}, {"quantity_id": "q61",
    "topic": "Retained DSM28 base preparation step 6", "source": [{"evidence_id":
    "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[0].steps[5]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"step\":
    \"Add bicarbonate solution and Pfennig''s heterotrophic salts to the resazurin
    (complete volumina, i.e. 50 mL bicarbonate solution and 26 mL Pfennig''s heterotrophic
    salts solution). Bubble with CO2 in an ice bath under sterile conditions.\"\n                    }",
    "exact_decoded_object": {"recipe_order": 5, "step": "Add bicarbonate solution
    and Pfennig''s heterotrophic salts to the resazurin (complete volumina, i.e. 50
    mL bicarbonate solution and 26 mL Pfennig''s heterotrophic salts solution). Bubble
    with CO2 in an ice bath under sterile conditions."}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "evidence_only", "rationale": "The current provider exactly supports
    this retained description at its stated solution/preparation stage. Keep the existing
    instruction and add scoped root evidence; do not mistake code-wide step concatenation
    for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "preparation_steps[5].description", "stored_value": "Add bicarbonate
    solution and Pfennig''s heterotrophic salts to the resazurin (complete volumina,
    i.e. 50 mL bicarbonate solution and 26 mL Pfennig''s heterotrophic salts solution).
    Bubble with CO2 in an ice bath under sterile conditions.", "decision": "evidence_only",
    "rationale": "The current provider exactly supports this retained description
    at its stated solution/preparation stage. Keep the existing instruction and add
    scoped root evidence; do not mistake code-wide step concatenation for whole-medium
    applicability."}]}, {"quantity_id": "q62", "topic": "Retained DSM28 base preparation
    step 7", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[0].steps[6]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"step\":
    \"Fill 50 ml of this mixture to each bottle of solution A (46 mL + 50 mL).\"\n                    }",
    "exact_decoded_object": {"recipe_order": 5, "step": "Fill 50 ml of this mixture
    to each bottle of solution A (46 mL + 50 mL)."}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "evidence_only", "rationale": "The current provider exactly supports
    this retained description at its stated solution/preparation stage. Keep the existing
    instruction and add scoped root evidence; do not mistake code-wide step concatenation
    for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "preparation_steps[6].description", "stored_value": "Fill 50 ml
    of this mixture to each bottle of solution A (46 mL + 50 mL).", "decision": "evidence_only",
    "rationale": "The current provider exactly supports this retained description
    at its stated solution/preparation stage. Keep the existing instruction and add
    scoped root evidence; do not mistake code-wide step concatenation for whole-medium
    applicability."}]}, {"quantity_id": "q63", "topic": "Retained DSM28 base preparation
    step 8", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[0].steps[7]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"step\":
    \"Before use, add 4 ml sulfide solution (1.5%) and 0.1 ml Vitamin B12 solution
    to each 100 mL bottle.\"\n                    }", "exact_decoded_object": {"recipe_order":
    5, "step": "Before use, add 4 ml sulfide solution (1.5%) and 0.1 ml Vitamin B12
    solution to each 100 mL bottle."}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "evidence_only", "rationale": "The current provider exactly supports this retained
    description at its stated solution/preparation stage. Keep the existing instruction
    and add scoped root evidence; do not mistake code-wide step concatenation for
    whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "preparation_steps[7].description", "stored_value": "Before use,
    add 4 ml sulfide solution (1.5%) and 0.1 ml Vitamin B12 solution to each 100 mL
    bottle.", "decision": "evidence_only", "rationale": "The current provider exactly
    supports this retained description at its stated solution/preparation stage. Keep
    the existing instruction and add scoped root evidence; do not mistake code-wide
    step concatenation for whole-medium applicability."}]}, {"quantity_id": "q64",
    "topic": "Retained DSM28 base preparation step 9", "source": [{"evidence_id":
    "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[0].steps[8]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"step\":
    \"Feed the actively growing culture periodically with neutralized 3% solution
    of sodium sulfide (use 1 -3 mL/100 mL depending on strain and cultivation stage)
    to replenish sulfide and with other supplement solutions (see Ref. 3365).\"\n                    }",
    "exact_decoded_object": {"recipe_order": 7, "step": "Feed the actively growing
    culture periodically with neutralized 3% solution of sodium sulfide (use 1 -3
    mL/100 mL depending on strain and cultivation stage) to replenish sulfide and
    with other supplement solutions (see Ref. 3365)."}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "conflict", "rationale": "The current provider supplies variable1–3
    ml/100 ml feeding, while the primary gives only periodic feeding and the provider
    also has a10 ml row. Retain the discrepancy; no universal fixed dose is selected.",
    "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "preparation_steps[8].description", "stored_value": "Feed the actively
    growing culture periodically with neutralized 3% solution of sodium sulfide (use
    1 -3 mL/100 mL depending on strain and cultivation stage) to replenish sulfide
    and with other supplement solutions (see Ref. 3365).", "decision": "conflict",
    "rationale": "The current provider supplies variable1–3 ml/100 ml feeding, while
    the primary gives only periodic feeding and the provider also has a10 ml row.
    Retain the discrepancy; no universal fixed dose is selected."}]}, {"quantity_id":
    "q65", "topic": "Retained DSM28 base preparation step 10", "source": [{"evidence_id":
    "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"step\": \"Aliquot Solution A into 100 mL
    screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at
    121\\u00b0C for 15 min.\"\n                    }", "exact_decoded_object": {"step":
    "Aliquot Solution A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble
    with N2/CO2 and autoclave at 121°C for 15 min."}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "evidence_only", "rationale": "The current provider exactly supports
    this retained description at its stated solution/preparation stage. Keep the existing
    instruction and add scoped root evidence; do not mistake code-wide step concatenation
    for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "preparation_steps[9].description", "stored_value": "Aliquot Solution
    A into 100 mL screw-cap bottles, filled with 46 mL each. Bubble with N2/CO2 and
    autoclave at 121°C for 15 min.", "decision": "evidence_only", "rationale": "The
    current provider exactly supports this retained description at its stated solution/preparation
    stage. Keep the existing instruction and add scoped root evidence; do not mistake
    code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id":
    "q66", "topic": "Retained DSM28 base preparation step 11", "source": [{"evidence_id":
    "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[2].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"step\": \"Prepare in a screw-cap bottle,
    bubble with N2 to replace air, close tightly and autoclave.\"\n                    }",
    "exact_decoded_object": {"step": "Prepare in a screw-cap bottle, bubble with N2
    to replace air, close tightly and autoclave."}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "evidence_only", "rationale": "The current provider exactly supports
    this retained description at its stated solution/preparation stage. Keep the existing
    instruction and add scoped root evidence; do not mistake code-wide step concatenation
    for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "preparation_steps[10].description", "stored_value": "Prepare in
    a screw-cap bottle, bubble with N2 to replace air, close tightly and autoclave.",
    "decision": "evidence_only", "rationale": "The current provider exactly supports
    this retained description at its stated solution/preparation stage. Keep the existing
    instruction and add scoped root evidence; do not mistake code-wide step concatenation
    for whole-medium applicability."}]}, {"quantity_id": "q67", "topic": "Retained
    DSM28 base preparation step 12", "source": [{"evidence_id": "api28", "reference":
    "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin",
    "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[3].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"step\": \"Bubble with CO2 and filter sterilize
    into sterile, gas-tight, 100 ml screw-cap bottle.\"\n                    }", "exact_decoded_object":
    {"step": "Bubble with CO2 and filter sterilize into sterile, gas-tight, 100 ml
    screw-cap bottle."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "evidence_only",
    "rationale": "The current provider exactly supports this retained description
    at its stated solution/preparation stage. Keep the existing instruction and add
    scoped root evidence; do not mistake code-wide step concatenation for whole-medium
    applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "preparation_steps[11].description", "stored_value": "Bubble with
    CO2 and filter sterilize into sterile, gas-tight, 100 ml screw-cap bottle.", "decision":
    "evidence_only", "rationale": "The current provider exactly supports this retained
    description at its stated solution/preparation stage. Keep the existing instruction
    and add scoped root evidence; do not mistake code-wide step concatenation for
    whole-medium applicability."}]}, {"quantity_id": "q68", "topic": "Retained DSM28
    base preparation step 13", "source": [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[4].steps[1]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"step\": \"Autoclave in a cotton-stoppered
    Erlenmeyer flask with an outlet tube for medium, connected to a glass outlet at
    the bottom of the vessel and has, at the other end, a silicon rubber tube with
    a pinch cock and a bell for aseptic dispensing of the medium into bottles.\"\n                    }",
    "exact_decoded_object": {"step": "Autoclave in a cotton-stoppered Erlenmeyer flask
    with an outlet tube for medium, connected to a glass outlet at the bottom of the
    vessel and has, at the other end, a silicon rubber tube with a pinch cock and
    a bell for aseptic dispensing of the medium into bottles."}, "quote_basis": "Literal
    UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "evidence_only", "rationale": "The current provider exactly supports
    this retained description at its stated solution/preparation stage. Keep the existing
    instruction and add scoped root evidence; do not mistake code-wide step concatenation
    for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "preparation_steps[12].description", "stored_value": "Autoclave
    in a cotton-stoppered Erlenmeyer flask with an outlet tube for medium, connected
    to a glass outlet at the bottom of the vessel and has, at the other end, a silicon
    rubber tube with a pinch cock and a bell for aseptic dispensing of the medium
    into bottles.", "decision": "evidence_only", "rationale": "The current provider
    exactly supports this retained description at its stated solution/preparation
    stage. Keep the existing instruction and add scoped root evidence; do not mistake
    code-wide step concatenation for whole-medium applicability."}]}, {"quantity_id":
    "q69", "topic": "Retained DSM28 base preparation step 14", "source": [{"evidence_id":
    "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[4].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"step\": \"Cool to room temperature under
    an atmosphere of N2/CO2 in an ice bath.\"\n                    }", "exact_decoded_object":
    {"step": "Cool to room temperature under an atmosphere of N2/CO2 in an ice bath."},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The
    current provider exactly supports this retained description at its stated solution/preparation
    stage. Keep the existing instruction and add scoped root evidence; do not mistake
    code-wide step concatenation for whole-medium applicability.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path":
    "preparation_steps[13].description", "stored_value": "Cool to room temperature
    under an atmosphere of N2/CO2 in an ice bath.", "decision": "evidence_only", "rationale":
    "The current provider exactly supports this retained description at its stated
    solution/preparation stage. Keep the existing instruction and add scoped root
    evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]},
    {"quantity_id": "q70", "topic": "Retained DSM28 base preparation step 15", "source":
    [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[5].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"step\": \"Filter sterilize into sterile,
    gas-tight, 100 ml screw-cap bottle.\"\n                    }", "exact_decoded_object":
    {"step": "Filter sterilize into sterile, gas-tight, 100 ml screw-cap bottle."},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The
    current provider exactly supports this retained description at its stated solution/preparation
    stage. Keep the existing instruction and add scoped root evidence; do not mistake
    code-wide step concatenation for whole-medium applicability.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path":
    "preparation_steps[14].description", "stored_value": "Filter sterilize into sterile,
    gas-tight, 100 ml screw-cap bottle.", "decision": "evidence_only", "rationale":
    "The current provider exactly supports this retained description at its stated
    solution/preparation stage. Keep the existing instruction and add scoped root
    evidence; do not mistake code-wide step concatenation for whole-medium applicability."}]},
    {"quantity_id": "q71", "topic": "Retained DSM28 base preparation step 16", "source":
    [{"evidence_id": "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[6].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"step\": \"Filter sterilized\"\n                    }",
    "exact_decoded_object": {"step": "Filter sterilized"}, "quote_basis": "Literal
    UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "evidence_only", "rationale": "The current provider exactly supports
    this retained description at its stated solution/preparation stage. Keep the existing
    instruction and add scoped root evidence; do not mistake code-wide step concatenation
    for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "preparation_steps[15].description", "stored_value": "Filter sterilized",
    "decision": "evidence_only", "rationale": "The current provider exactly supports
    this retained description at its stated solution/preparation stage. Keep the existing
    instruction and add scoped root evidence; do not mistake code-wide step concatenation
    for whole-medium applicability."}]}, {"quantity_id": "q72", "topic": "Retained
    DSM28 base preparation step 17", "source": [{"evidence_id": "api28", "reference":
    "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin",
    "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[7].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"step\": \"Adjust pH to 6.0.\"\n                    }",
    "exact_decoded_object": {"step": "Adjust pH to 6.0."}, "quote_basis": "Literal
    UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "evidence_only", "rationale": "The current provider exactly supports
    this retained description at its stated solution/preparation stage. Keep the existing
    instruction and add scoped root evidence; do not mistake code-wide step concatenation
    for whole-medium applicability.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "preparation_steps[16].description", "stored_value": "Adjust pH
    to 6.0.", "decision": "evidence_only", "rationale": "The current provider exactly
    supports this retained description at its stated solution/preparation stage. Keep
    the existing instruction and add scoped root evidence; do not mistake code-wide
    step concatenation for whole-medium applicability."}]}, {"quantity_id": "q73",
    "topic": "Retained DSM28 base preparation step 18", "source": [{"evidence_id":
    "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[8].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"step\": \"The sulfide solution is prepared
    in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer.
    The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at
    121\\u00b0C. After cooling to room temperature the pH is adjusted to about 7.0
    by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle.\"\n                    }",
    "exact_decoded_object": {"step": "The sulfide solution is prepared in a 250 ml
    screw-capped bottle with a butyl rubber septum and a magnetic stirrer. The solution
    is bubbled with nitrogen gas, closed and autoclaved for 15 min. at 121°C. After
    cooling to room temperature the pH is adjusted to about 7.0 by adding of sterile
    2 M H2SO4 drop-wise with a syringe without opening the bottle."}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}], "decision": "evidence_only", "rationale": "The current provider
    exactly supports this retained description at its stated solution/preparation
    stage. Keep the existing instruction and add scoped root evidence; do not mistake
    code-wide step concatenation for whole-medium applicability.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml", "field_path":
    "preparation_steps[17].description", "stored_value": "The sulfide solution is
    prepared in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic
    stirrer. The solution is bubbled with nitrogen gas, closed and autoclaved for
    15 min. at 121°C. After cooling to room temperature the pH is adjusted to about
    7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the
    bottle.", "decision": "evidence_only", "rationale": "The current provider exactly
    supports this retained description at its stated solution/preparation stage. Keep
    the existing instruction and add scoped root evidence; do not mistake code-wide
    step concatenation for whole-medium applicability."}]}, {"quantity_id": "q74",
    "topic": "Restore the omitted421 instruction in generated/KOMODO layers", "source":
    [{"evidence_id": "api421", "reference": "https://mediadive.dsmz.de/rest/medium/421",
    "raw_path": "REVIEW_WORK/batch062/source01-03/api421.bin", "raw_sha256": "d26536bd466f341c03b9bb42572283cba695d50a73eacc053f74581cf0360c52",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T09:27:43.186753Z",
    "quote": "{\n                        \"step\": \"Supplement medium 28 with NaCl
    (10%), MgCl2 x 6 H2O (0.3%) Na-acetate (0.05%) and sodium thiosulfate (0.05%).
    Incubate at 500 to 1000 Lux light intensity.\"\n                    }", "exact_decoded_object":
    {"step": "Supplement medium 28 with NaCl (10%), MgCl2 x 6 H2O (0.3%) Na-acetate
    (0.05%) and sodium thiosulfate (0.05%). Incubate at 500 to 1000 Lux light intensity."},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "dsm421", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium421.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm421.bin", "raw_sha256": "147737ed0bfdd97948c86a691a34151f6e28a89687ab665b857bdd210f385ccc",
    "locator": "Complete421 primary instruction", "accessed_at": "2026-10-28T09:27:43.389676Z",
    "quote": "421. CHROMATIUM SALEXIGENS MEDIUM\n\nSupplement medium 28 with NaCl
    (10%), MgCl 2 x 6 H2O (0.3%) Na-acetate (0.05%)\nand sodium thiosulfate (0.05%).
    Incubate at 500 to 1000 Lux light intensity."}], "decision": "add", "rationale":
    "Preserve the DSM owner repair; do not claim that all three layers lack preparation.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "The generated/KOMODO layer lacks the explicit supplement and500–1000 Lux instruction.
    Add only source-scoped instructions; the DSM contributor already retains them.",
    "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "The generated/KOMODO layer lacks the explicit supplement and500–1000 Lux instruction.
    Add only source-scoped instructions; the DSM contributor already retains them.",
    "missing": true}]}, {"quantity_id": "q75", "topic": "Inherited base pH range and1M
    adjuster", "source": [{"evidence_id": "dsm28", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm28.bin", "raw_sha256": "442636c7b32c8f6de4a54fd8acaaa22f8e1a130f3d4b45af59d5782fe77a6c3d",
    "locator": "PDF extracted line 77; visually checked page", "accessed_at": "2026-10-28T09:27:43.589061Z",
    "quote": "Adjust the pH with filter-sterilised 1M Na2CO3 to 7.1-7.3."}, {"evidence_id":
    "api28", "reference": "https://mediadive.dsmz.de/rest/medium/28", "raw_path":
    "REVIEW_WORK/batch062/source01-03/api28.bin", "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"step\":
    \"Adjust the pH with filter-sterilised 1M Na2CO3 to 7.1-7.3.\"\n                    }",
    "exact_decoded_object": {"recipe_order": 7, "step": "Adjust the pH with filter-sterilised
    1M Na2CO3 to 7.1-7.3."}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "mixed",
    "rationale": "The source specifies1M sodium carbonate and pH7.1–7.3 for assembled
    base28; no titrant volume is supplied.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "ph_range", "stored_value": {"min": 7.1, "max": 7.3}, "decision":
    "evidence_only", "rationale": "The existing range7.1–7.3 is supported for base28;
    retain its explicit source stage."}, {"path": "data/merge_yaml/merged/CHROMATIUM_SALEXIGENS_MEDIUM.yaml",
    "field_path": "ph_range", "stored_value": null, "decision": "add", "rationale":
    "Record the inherited base range with the explicit421→28 cross-reference and preserve
    an absent421-specific override; do not invent a separate value.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml",
    "field_path": "ph_range", "stored_value": null, "decision": "add", "rationale":
    "Record the inherited base range with the explicit421→28 cross-reference and preserve
    an absent421-specific override; do not invent a separate value.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml", "field_path":
    "ph_range", "stored_value": null, "decision": "add", "rationale": "Record the
    inherited base range with the explicit421→28 cross-reference and preserve an absent421-specific
    override; do not invent a separate value.", "missing": true}]}, {"quantity_id":
    "q76", "topic": "Conflicting conditional marine-base formulations", "source":
    [{"evidence_id": "dsm28", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm28.bin", "raw_sha256": "442636c7b32c8f6de4a54fd8acaaa22f8e1a130f3d4b45af59d5782fe77a6c3d",
    "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T09:27:43.589061Z",
    "quote": "(For marine or estuarine isolates add 100.0 g NaCl to this solution
    and increase the\nMgSO4 x 7 H2O to 15.0 g)."}, {"evidence_id": "api28", "reference":
    "https://mediadive.dsmz.de/rest/medium/28", "raw_path": "REVIEW_WORK/batch062/source01-03/api28.bin",
    "raw_sha256": "bf66cb46a4809306d36ae5bb5710648fbddb70b888441b427c3e3906599141f3",
    "locator": "$.data.solutions[0].steps[9]", "accessed_at": "2026-10-28T09:27:43.365556Z",
    "quote": "{\n                        \"step\": \"Note: for marine species use
    1-3% NaCl and increase the amount of MgSO4 7*H2O to 2,8g/L\"\n                    }",
    "exact_decoded_object": {"step": "Note: for marine species use 1-3% NaCl and increase
    the amount of MgSO4 7*H2O to 2,8g/L"}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "conflict", "rationale": "Preserve both exact conditional variants and report
    their conflict. The medium name is not evidence that a strain-specific marine
    override applies.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "preparation_steps", "stored_value": [{"step_number": 1, "action":
    "FILTER_STERILIZE", "description": "Adjust the pH with filter-sterilised 1M Na2CO3
    to 7.1-7.3."}, {"step_number": 2, "action": "ALIQUOT", "description": "If needed,
    aliquot into sterile, N<sub>2</sub> gassed screw-cap tubes under N<sub>2</sub>
    gas."}, {"step_number": 3, "action": "MIX", "description": "During the first 24
    h, the iron of the medium precipitates in the form of black flocks. No other sediment
    should arise in the otherwise clear medium."}, {"step_number": 4, "action": "AUTOCLAVE",
    "description": "Aliquot Solution A into 100 mL screw-cap bottles, filled with
    46 mL each. Bubble with N2/CO2 and autoclave at 121°C for 15 min (as decribed
    below)."}, {"step_number": 5, "action": "MIX", "description": "Prepare the following
    solutions (resazurin, bicarbonate and Pfennig''s heterotrophic salts) and sterilize
    as given below."}, {"step_number": 6, "action": "COOL", "description": "Add bicarbonate
    solution and Pfennig''s heterotrophic salts to the resazurin (complete volumina,
    i.e. 50 mL bicarbonate solution and 26 mL Pfennig''s heterotrophic salts solution).
    Bubble with CO2 in an ice bath under sterile conditions."}, {"step_number": 7,
    "action": "MIX", "description": "Fill 50 ml of this mixture to each bottle of
    solution A (46 mL + 50 mL)."}, {"step_number": 8, "action": "MIX", "description":
    "Before use, add 4 ml sulfide solution (1.5%) and 0.1 ml Vitamin B12 solution
    to each 100 mL bottle."}, {"step_number": 9, "action": "MIX", "description": "Feed
    the actively growing culture periodically with neutralized 3% solution of sodium
    sulfide (use 1 -3 mL/100 mL depending on strain and cultivation stage) to replenish
    sulfide and with other supplement solutions (see Ref. 3365)."}, {"step_number":
    10, "action": "AUTOCLAVE", "description": "Aliquot Solution A into 100 mL screw-cap
    bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121°C for
    15 min."}, {"step_number": 11, "action": "AUTOCLAVE", "description": "Prepare
    in a screw-cap bottle, bubble with N2 to replace air, close tightly and autoclave."},
    {"step_number": 12, "action": "FILTER_STERILIZE", "description": "Bubble with
    CO2 and filter sterilize into sterile, gas-tight, 100 ml screw-cap bottle."},
    {"step_number": 13, "action": "AUTOCLAVE", "description": "Autoclave in a cotton-stoppered
    Erlenmeyer flask with an outlet tube for medium, connected to a glass outlet at
    the bottom of the vessel and has, at the other end, a silicon rubber tube with
    a pinch cock and a bell for aseptic dispensing of the medium into bottles."},
    {"step_number": 14, "action": "COOL", "description": "Cool to room temperature
    under an atmosphere of N2/CO2 in an ice bath."}, {"step_number": 15, "action":
    "FILTER_STERILIZE", "description": "Filter sterilize into sterile, gas-tight,
    100 ml screw-cap bottle."}, {"step_number": 16, "action": "FILTER_STERILIZE",
    "description": "Filter sterilized"}, {"step_number": 17, "action": "ADJUST_PH",
    "description": "Adjust pH to 6.0."}, {"step_number": 18, "action": "AUTOCLAVE",
    "description": "The sulfide solution is prepared in a 250 ml screw-capped bottle
    with a butyl rubber septum and a magnetic stirrer. The solution is bubbled with
    nitrogen gas, closed and autoclaved for 15 min. at 121°C. After cooling to room
    temperature the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise
    with a syringe without opening the bottle."}], "decision": "unsupported", "rationale":
    "The primary conditional100 gNaCl/15 gMgSO4hept instruction and current API1–3%NaCl/2.8g/L
    statement are distinct source versions. Do not combine either automatically with421’s10%
    supplement."}]}, {"quantity_id": "q77", "topic": "Additional primary feeding-stock
    pH indicator/context", "source": [{"evidence_id": "dsm28", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium28.pdf",
    "raw_path": "REVIEW_WORK/batch062/source01-03/dsm28.bin", "raw_sha256": "442636c7b32c8f6de4a54fd8acaaa22f8e1a130f3d4b45af59d5782fe77a6c3d",
    "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T09:27:43.589061Z",
    "quote": "Appearance of a yellow colour indicates the drop of pH to about 8. The
    solution should\nbe stirred continuously to avoid precipitation of elemental sulfur.
    The final solution\nshould be clear and is yellow in colour."}], "decision": "add",
    "rationale": "The primary preparation includes pH~8 indicator context absent from
    the current provider step; it does not replace final feeding-stock pH~7 or base
    pH7.1–7.3.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/pfennigs_medium_i.yaml",
    "field_path": "preparation_steps", "stored_value": [{"step_number": 1, "action":
    "FILTER_STERILIZE", "description": "Adjust the pH with filter-sterilised 1M Na2CO3
    to 7.1-7.3."}, {"step_number": 2, "action": "ALIQUOT", "description": "If needed,
    aliquot into sterile, N<sub>2</sub> gassed screw-cap tubes under N<sub>2</sub>
    gas."}, {"step_number": 3, "action": "MIX", "description": "During the first 24
    h, the iron of the medium precipitates in the form of black flocks. No other sediment
    should arise in the otherwise clear medium."}, {"step_number": 4, "action": "AUTOCLAVE",
    "description": "Aliquot Solution A into 100 mL screw-cap bottles, filled with
    46 mL each. Bubble with N2/CO2 and autoclave at 121°C for 15 min (as decribed
    below)."}, {"step_number": 5, "action": "MIX", "description": "Prepare the following
    solutions (resazurin, bicarbonate and Pfennig''s heterotrophic salts) and sterilize
    as given below."}, {"step_number": 6, "action": "COOL", "description": "Add bicarbonate
    solution and Pfennig''s heterotrophic salts to the resazurin (complete volumina,
    i.e. 50 mL bicarbonate solution and 26 mL Pfennig''s heterotrophic salts solution).
    Bubble with CO2 in an ice bath under sterile conditions."}, {"step_number": 7,
    "action": "MIX", "description": "Fill 50 ml of this mixture to each bottle of
    solution A (46 mL + 50 mL)."}, {"step_number": 8, "action": "MIX", "description":
    "Before use, add 4 ml sulfide solution (1.5%) and 0.1 ml Vitamin B12 solution
    to each 100 mL bottle."}, {"step_number": 9, "action": "MIX", "description": "Feed
    the actively growing culture periodically with neutralized 3% solution of sodium
    sulfide (use 1 -3 mL/100 mL depending on strain and cultivation stage) to replenish
    sulfide and with other supplement solutions (see Ref. 3365)."}, {"step_number":
    10, "action": "AUTOCLAVE", "description": "Aliquot Solution A into 100 mL screw-cap
    bottles, filled with 46 mL each. Bubble with N2/CO2 and autoclave at 121°C for
    15 min."}, {"step_number": 11, "action": "AUTOCLAVE", "description": "Prepare
    in a screw-cap bottle, bubble with N2 to replace air, close tightly and autoclave."},
    {"step_number": 12, "action": "FILTER_STERILIZE", "description": "Bubble with
    CO2 and filter sterilize into sterile, gas-tight, 100 ml screw-cap bottle."},
    {"step_number": 13, "action": "AUTOCLAVE", "description": "Autoclave in a cotton-stoppered
    Erlenmeyer flask with an outlet tube for medium, connected to a glass outlet at
    the bottom of the vessel and has, at the other end, a silicon rubber tube with
    a pinch cock and a bell for aseptic dispensing of the medium into bottles."},
    {"step_number": 14, "action": "COOL", "description": "Cool to room temperature
    under an atmosphere of N2/CO2 in an ice bath."}, {"step_number": 15, "action":
    "FILTER_STERILIZE", "description": "Filter sterilize into sterile, gas-tight,
    100 ml screw-cap bottle."}, {"step_number": 16, "action": "FILTER_STERILIZE",
    "description": "Filter sterilized"}, {"step_number": 17, "action": "ADJUST_PH",
    "description": "Adjust pH to 6.0."}, {"step_number": 18, "action": "AUTOCLAVE",
    "description": "The sulfide solution is prepared in a 250 ml screw-capped bottle
    with a butyl rubber septum and a magnetic stirrer. The solution is bubbled with
    nitrogen gas, closed and autoclaved for 15 min. at 121°C. After cooling to room
    temperature the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise
    with a syringe without opening the bottle."}], "decision": "add", "rationale":
    "Preserve the primary-only pH~8 yellow-colour indicator, stirring and appearance
    as feeding-stock context, not a target-medium pH or organism-growth assertion."}]}]'
- assessment_id: a4
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: concern
  summary: The selected five primary/secondary CHEBI pairs resolve with current canonical
    labels and source forms. The separately scoped base has a confirmed nickel-hydrate
    mismatch, current-negative legacy000399 and missing mixture/secondary links; EDTA
    hydration remains unspecified. All recursive identities and current preferred/synonym
    rows are retained without treating medium IDs as failed chemical IDs.
  target_ids:
  - CultureMech:005246
  evidence_ids:
  - grounding
- assessment_id: a5
  area: provenance
  topic: History and evidence scope
  outcome: concern
  summary: Five exact current-record historical reports and the selected pair/method
    of the large source-duplicate report were read. Most old API421 quoted objects
    match current bytes; the neutralized-sulfide object now adds g_l/mmol_l and the
    full old raw digest differs. Exact current KOMODO mapping/medium routes returned403.
    Preserve these distinctions and all original events; no historical timestamp or
    execution is reconstructed.
  target_ids:
  - CultureMech:005246
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
  - CultureMech:005246
  evidence_ids:
  - local-target
- assessment_id: a7
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:005246
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-005246-restore-the-required-base-and-isolate-the-feeding-stock
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore the required base and isolate the feeding stock
  description: DSM421 supplements medium28; no local layer has the necessary base/solution
    topology. The four supplement rates match explicit current provider g_l declarations,
    but30 g/L sodium sulfide is the neutralized feeding-stock strength. Restore the
    base and feeding stages without flattening or choosing a fixed feed from conflicting
    source variants.
  target_ids:
  - CultureMech:005246
  field_paths:
  - ingredients[4].concentration
  - solutions
  evidence_ids:
  - dsm421
  - api421
  - dsm28
  - api28
  - quantities
  rule_id: P2.3
  native_severity: P2
  normalization_reason: 'Major native concentration/topology mismatch: the source
    distinguishes base, supplement and feeding stages, while local direct ingredients
    misrepresent the stock as complete-medium concentration.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-005246-repair-the-referenced-base-before-transferring-it
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Repair the referenced base before transferring it
  description: 'The separately inspected DSM28 dependency is itself flattened: all22
    direct fields represent stock constituents, and44.8148 g/L sulfide is a sum of
    two different stock bases. Current providerE omits primary pyruvate/dextrose;
    their local per-litre rates remain unsupported. Resazurin has an unresolved percentage
    basis. These dependency findings do not assert that its22 ingredients already
    occur in the selected target.'
  target_ids:
  - CultureMech:005246
  field_paths:
  - data/normalized_yaml/bacterial/pfennigs_medium_i.yaml::ingredients
  - data/normalized_yaml/bacterial/pfennigs_medium_i.yaml::solutions
  - data/normalized_yaml/bacterial/pfennigs_medium_i.yaml::ingredients[2].concentration
  - data/normalized_yaml/bacterial/pfennigs_medium_i.yaml::ingredients[4].concentration
  - data/normalized_yaml/bacterial/pfennigs_medium_i.yaml::ingredients[7].concentration
  - data/normalized_yaml/bacterial/pfennigs_medium_i.yaml::ingredients[8].concentration
  evidence_ids:
  - base28
  - dsm28
  - api28
  - quantities
  - writer-cleanup
  rule_id: P2.3
  native_severity: P2
  normalization_reason: 'Major scoped dependency concentration mismatch: identical
    units refer to distinct solution-stage bases; the local sum cannot describe a
    final-medium total. Exact dependency-qualified locators prevent target misattribution.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/pfennigs_medium_i.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-005246-preserve-the-dsm-owner-preparation-during-regeneration
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preserve the DSM owner preparation during regeneration
  description: The DSM contributor already contains11 source-supported preparation
    descriptions, while generated/KOMODO layers omit them. Base-stock steps are concatenated
    and require stage labels; the inherited pH range and root evidence are absent.
    Current resolver omits preparation/range/evidence, and current merge compatibility
    rejects unequal scientific content; neither proves the old run. Preserve the source-duplicate
    relationship without forcing an incompatible merge.
  target_ids:
  - CultureMech:005246
  field_paths:
  - preparation_steps
  - ph_range
  - evidence
  - merged_from
  evidence_ids:
  - owner-2
  - local-target
  - dsm421
  - dsm28
  - writer-resolver
  - writer-merge
  - writer-formulation
  rule_id: P3.4
  native_severity: P3
  normalization_reason: Normalized major because the generated representation entirely
    loses the required base/supplement preparation, rather than merely lacking a cosmetic
    instruction. Existing DSM owner work is explicitly credited.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f4
  issue_key: culturemech-005246-reconcile-the-scoped-base-hydrate-and-legacy-linkage
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Reconcile the scoped base hydrate and legacy linkage
  description: In DSM28 only, NiCl2 x6 H2O points to valid34887 nickel dichloride
    rather than verified53542 hexahydrate. Pyruvate’s primary50144 is valid while
    secondary MediaIngredientMech000399 is absent from the current packaged catalog;
    absence is not proof of historical invalidity. Yeast lacks linkage and manganese131395
    lacks its secondary link. EDTA hydration is unspecified, so anhydrous64734 remains
    an unverified specificity.
  target_ids:
  - CultureMech:005246
  field_paths:
  - data/normalized_yaml/bacterial/pfennigs_medium_i.yaml::ingredients[18].term
  - data/normalized_yaml/bacterial/pfennigs_medium_i.yaml::ingredients[18].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/pfennigs_medium_i.yaml::ingredients[7].mediaingredientmech_term
  - data/normalized_yaml/bacterial/pfennigs_medium_i.yaml::ingredients[1].term
  - data/normalized_yaml/bacterial/pfennigs_medium_i.yaml::ingredients[16].mediaingredientmech_chebi_term
  evidence_ids:
  - base28
  - dsm28
  - chebi53542
  - grounding
  rule_id: scoped-dependency-grounding
  native_severity: P2
  normalization_reason: 'Minor mitigation: the confirmed form/link problems are confined
    to an explicitly inspected dependency, not the selected record’s five identities,
    and no molar conversion is proposed. Current canonical identities remain distinguished
    from historical membership.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/pfennigs_medium_i.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f5
  issue_key: culturemech-005246-keep-historical-defects-and-unresolved-evidence-append-only
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Keep historical defects and unresolved evidence append-only
  description: The selected/KOMODO history contains a literal malformed.fZ timestamp
    and a separate timezone-unspecified resolver timestamp. Do not rewrite either
    event. The exact current KOMODO routes failed403; the old selected mapping row
    remains derivative. Most oldAPI421 objects still match, but its sulfide object
    changed and the complete old raw digest is not authenticated by today’s capture.
  target_ids:
  - CultureMech:005246
  field_paths:
  - curation_history[0].timestamp
  - curation_history[1].timestamp
  - data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml::curation_history[1].timestamp
  - references
  - evidence
  evidence_ids:
  - historical-reader
  - komodo421
  - komodoList
  - local-target
  rule_id: historical-event-metadata
  native_severity: P4
  normalization_reason: 'Custom event-metadata rule normalized minor at nativeP4 provenance
    priority: this concerns malformed and timezone-unspecified timestamps in a populated
    history, not the nativeP4.4 single-event-history condition. Original events must
    remain byte-preserved; current source checks do not reconstruct an old access
    event.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Retain the four source-supported supplement rates, create an explicitly
    scoped base28 dependency and separate the30 g/L feeding stock. Reconcile source-version
    conflicts before declaring a complete final formulation; do not infer a final
    volume or feed dose.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:005246
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Curate the explicitly referenced DSM28 stock topology with separate
    A–F,SL12B and feeding stages. Preserve source batch amounts and primary/provider
    differences; remove the invalid sum only through an evidence-backed owner repair
    and do not export stock strengths as421 final rates.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:005246
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/pfennigs_medium_i.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Retain the DSM contributor’s supported instructions, add only missing
    scoped root evidence and source-stage structure, then reconcile compatible owner
    content before regeneration. Keep source-duplicate provenance distinct from complete
    formulation equivalence.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:005246
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action4
  description: Before base reuse, verify the nickel hydrate in both slots and refresh
    the exact pyruvate secondary linkage through current authority evidence. Preserve
    legacy history and unresolved EDTA specificity; do not treat current catalog status
    as historical proof.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:005246
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/pfennigs_medium_i.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action5
  description: Preserve every original event and failed capture. Append verified source/context
    evidence and, only if authoritative event provenance is recovered, a new correction
    event; never silently rewrite the malformed or timezone-unspecified timestamps.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:005246
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- The current primary and provider differ on conditional marine-base salts and omit
  different solutionE ingredients. Neither version is silently selected or combined
  with the421 supplement.
- Bare percentages in the421 primary and resazurin reagent have no stated mass/volume
  basis. Provider g_l declarations are credited only at their named stages, not as
  independently validated percentage conversions.
- Primary base assembly amounts do not establish an exact final litre. Provider10
  ml feeding, variable1–3 ml/100 ml prose and primary unfixed periodic feed remain
  separate/conflicting.
- Exact KOMODO routes returned403; old mapping/source objects are historical derivative
  evidence except specifically recorded literal matches. The complete old API421 response
  digest was not recovered.
- All dependency observations concern the expressly referenced DSM28 record, not an
  instruction to transfer its raw stocks or conditional species prescriptions into421.
  No strain growth or optimization claim is made.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
