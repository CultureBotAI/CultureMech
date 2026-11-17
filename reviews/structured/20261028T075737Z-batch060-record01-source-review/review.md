# CARCBOXYDIBRACHIUM MEDIUM: preserve main rates and restore stock stages

- Review: 20261028T075737Z-batch060-record01-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T07:45:59.659790Z
- Finished UTC: 2026-10-28T07:57:37.957067Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The DSM902 identity and 13 provider-declared main concentrations are supported. Nineteen stock-composition rows are incorrectly placed as direct medium ingredients, both receiving stock additions and solvent context are missing, and two supplied chemical forms conflict with their identifiers. Existing anoxic preparation is substantially retained and must be scoped, not replaced.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch060 native selection index 01.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002069 | data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml | generated | carcboxydibrachium_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002069 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:002069 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:002069 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:002069 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Exact source and ownership

identity: supported. Targets: CultureMech:002069.

The generated target has one maintained DSM902 owner. Primary PDF and current provider use the same CARCBOXYDIBRACHIUM title; no speculative spelling correction or transfer from a similarly named medium is proposed. Bacterial/complex/undefined/liquid classification agrees with source metadata and yeast extract.

### Current preparation and missing topology

completeness: concern. Targets: CultureMech:002069.

Main pH and preparation are already present. Restore stock objects/doses and water context while relocating only the SL-10-specific makeup instruction. The main provider rates are supported independently of the obsolete blanket conflict labels in the October report.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:002069.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "NaCl", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 19.9601,\n                        \"mmol_l\": 341.548,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "NaCl", "compound_id": 43, "amount": 20, "unit": "g", "g_l": 19.9601, "mmol_l": 341.548, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 19.9601 g/L and supplies the source batch amount 20 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "19.9601", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 19.9601 g/L and supplies the source batch amount 20 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "19.9601", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 19.9601 g/L and supplies the source batch amount 20 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}]}, {"quantity_id": "q2", "topic": "KCl", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.7,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.698603,\n                        \"mmol_l\": 9.37093,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "KCl", "compound_id": 61, "amount": 0.7, "unit": "g", "g_l": 0.698603, "mmol_l": 9.37093, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.698603 g/L and supplies the source batch amount 0.7 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.698603", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.698603 g/L and supplies the source batch amount 0.7 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.698603", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.698603 g/L and supplies the source batch amount 0.7 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}]}, {"quantity_id": "q3", "topic": "MgSO4 x 7 H2O", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3.9,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.89222,\n                        \"mmol_l\": 15.7915,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "MgSO4 x 7 H2O", "compound_id": 8, "amount": 3.9, "unit": "g", "g_l": 3.89222, "mmol_l": 15.7915, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 3.89222 g/L and supplies the source batch amount 3.9 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "3.89222", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 3.89222 g/L and supplies the source batch amount 3.9 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "3.89222", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 3.89222 g/L and supplies the source batch amount 3.9 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}]}, {"quantity_id": "q4", "topic": "CaCl2 x 2 H2O", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.399202,\n                        \"mmol_l\": 2.71538,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "CaCl2 x 2 H2O", "compound_id": 7, "amount": 0.4, "unit": "g", "g_l": 0.399202, "mmol_l": 2.71538, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.399202 g/L and supplies the source batch amount 0.4 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.399202", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.399202 g/L and supplies the source batch amount 0.4 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.399202", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.399202 g/L and supplies the source batch amount 0.4 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}]}, {"quantity_id": "q5", "topic": "NH4Cl", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.299401,\n                        \"mmol_l\": 5.59733,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "NH4Cl", "compound_id": 42, "amount": 0.3, "unit": "g", "g_l": 0.299401, "mmol_l": 5.59733, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.299401 g/L and supplies the source batch amount 0.3 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.299401", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.299401 g/L and supplies the source batch amount 0.3 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.299401", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.299401 g/L and supplies the source batch amount 0.3 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}]}, {"quantity_id": "q6", "topic": "Na2HPO4", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2HPO4\",\n                        \"compound_id\": 233,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.149701,\n                        \"mmol_l\": 1.05453,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "Na2HPO4", "compound_id": 233, "amount": 0.15, "unit": "g", "g_l": 0.149701, "mmol_l": 1.05453, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.149701 g/L and supplies the source batch amount 0.15 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.149701", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.149701 g/L and supplies the source batch amount 0.15 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.149701", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.149701 g/L and supplies the source batch amount 0.15 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}]}, {"quantity_id": "q7", "topic": "Na2SiO3", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2SiO3\",\n                        \"compound_id\": 823,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0299401,\n                        \"mmol_l\": 0.245284,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "Na2SiO3", "compound_id": 823, "amount": 0.03, "unit": "g", "g_l": 0.0299401, "mmol_l": 0.245284, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.0299401 g/L and supplies the source batch amount 0.03 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.0299401", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.0299401 g/L and supplies the source batch amount 0.03 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.0299401", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.0299401 g/L and supplies the source batch amount 0.03 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}]}, {"quantity_id": "q8", "topic": "Yeast extract", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0499002,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "Yeast extract", "compound_id": 16, "amount": 0.05, "unit": "g", "g_l": 0.0499002, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.0499002 g/L and supplies the source batch amount 0.05 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.0499002", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.0499002 g/L and supplies the source batch amount 0.05 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.0499002", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.0499002 g/L and supplies the source batch amount 0.05 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}]}, {"quantity_id": "q9", "topic": "Sodium resazurin", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000499002,\n                        \"mmol_l\": 0.00198671,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "Sodium resazurin", "compound_id": 1852, "attribute": "0.1% w/v", "amount": 0.5, "unit": "ml", "g_l": 0.000499002, "mmol_l": 0.00198671, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.000499002 g/L and supplies the source batch amount 0.5 ml. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator. The primary 0.5 ml of 0.1% w/v sodium resazurin supplies 0.5 mg per batch; correcting its chemical identifier does not change that amount.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.000499002", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.000499002 g/L and supplies the source batch amount 0.5 ml. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator. The primary 0.5 ml of 0.1% w/v sodium resazurin supplies 0.5 mg per batch; correcting its chemical identifier does not change that amount."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.000499002", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.000499002 g/L and supplies the source batch amount 0.5 ml. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator. The primary 0.5 ml of 0.1% w/v sodium resazurin supplies 0.5 mg per batch; correcting its chemical identifier does not change that amount."}]}, {"quantity_id": "q10", "topic": "NaHCO3", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[0].recipe[10]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\": 5.94,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound": "NaHCO3", "compound_id": 55, "amount": 0.5, "unit": "g", "g_l": 0.499002, "mmol_l": 5.94, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.499002 g/L and supplies the source batch amount 0.5 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.499002", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.499002 g/L and supplies the source batch amount 0.5 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.499002", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.499002 g/L and supplies the source batch amount 0.5 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}]}, {"quantity_id": "q11", "topic": "Na-pyruvate", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[0].recipe[11]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na-pyruvate\",\n                        \"compound_id\": 113,\n                        \"amount\": 2.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.49501,\n                        \"mmol_l\": 22.6728,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 12, "compound": "Na-pyruvate", "compound_id": 113, "amount": 2.5, "unit": "g", "g_l": 2.49501, "mmol_l": 22.6728, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 2.49501 g/L and supplies the source batch amount 2.5 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "2.49501", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 2.49501 g/L and supplies the source batch amount 2.5 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "2.49501", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 2.49501 g/L and supplies the source batch amount 2.5 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}]}, {"quantity_id": "q12", "topic": "L-Cysteine HCl x H2O", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[0].recipe[13]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.45,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.449102,\n                        \"mmol_l\": 2.557,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 14, "compound": "L-Cysteine HCl x H2O", "compound_id": 770, "amount": 0.45, "unit": "g", "g_l": 0.449102, "mmol_l": 2.557, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.449102 g/L and supplies the source batch amount 0.45 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.449102", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.449102 g/L and supplies the source batch amount 0.45 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.449102", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.449102 g/L and supplies the source batch amount 0.45 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}]}, {"quantity_id": "q13", "topic": "Na2S x 9 H2O", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[0].recipe[14]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.45,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.449102,\n                        \"mmol_l\": 1.86984,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 15, "compound": "Na2S x 9 H2O", "compound_id": 54, "amount": 0.45, "unit": "g", "g_l": 0.449102, "mmol_l": 1.86984, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.449102 g/L and supplies the source batch amount 0.45 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.449102", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.449102 g/L and supplies the source batch amount 0.45 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.449102", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution row explicitly declares 0.449102 g/L and supplies the source batch amount 0.45 g. Retain this declared main-stage rate with exact evidence and provider volume1002 context; the PDF water1000 ml is not proof of a final-medium denominator."}]}, {"quantity_id": "q14", "topic": "HCl", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "HCl", "compound_id": 68, "attribute": "25%", "amount": 10, "unit": "ml", "g_l": 2.5, "mmol_l": 68.5683, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 10 ml in its source recipe and provider g_l=2.5. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred. The bare25% HCl source does not state a mass/volume basis, so the provider2.5 g/L must not be presented as an independently derived primary-source conversion.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "2.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 10 ml in its source recipe and provider g_l=2.5. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred. The bare25% HCl source does not state a mass/volume basis, so the provider2.5 g/L must not be presented as an independently derived primary-source conversion."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "2.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 10 ml in its source recipe and provider g_l=2.5. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred. The bare25% HCl source does not state a mass/volume basis, so the provider2.5 g/L must not be presented as an independently derived primary-source conversion."}]}, {"quantity_id": "q15", "topic": "FeCl2 x 4 H2O", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "FeCl2 x 4 H2O", "compound_id": 260, "amount": 1.5, "unit": "g", "g_l": 1.5, "mmol_l": 7.54482, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 1.5 g in its source recipe and provider g_l=1.5. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 1.5 g in its source recipe and provider g_l=1.5. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 1.5 g in its source recipe and provider g_l=1.5. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]}, {"quantity_id": "q16", "topic": "ZnCl2", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "ZnCl2", "compound_id": 64, "amount": 70, "unit": "mg", "g_l": 0.07, "mmol_l": 0.513573, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 70 mg in its source recipe and provider g_l=0.07. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.07", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 70 mg in its source recipe and provider g_l=0.07. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.07", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 70 mg in its source recipe and provider g_l=0.07. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]}, {"quantity_id": "q17", "topic": "MnCl2 x 4 H2O", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[1].recipe[3]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "MnCl2 x 4 H2O", "compound_id": 36, "amount": 100, "unit": "mg", "g_l": 0.1, "mmol_l": 0.505293, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 100 mg in its source recipe and provider g_l=0.1. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 100 mg in its source recipe and provider g_l=0.1. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 100 mg in its source recipe and provider g_l=0.1. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]}, {"quantity_id": "q18", "topic": "H3BO3", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[1].recipe[4]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "H3BO3", "compound_id": 37, "amount": 6, "unit": "mg", "g_l": 0.006, "mmol_l": 0.0970246, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 6 mg in its source recipe and provider g_l=0.006. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.006", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 6 mg in its source recipe and provider g_l=0.006. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.006", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 6 mg in its source recipe and provider g_l=0.006. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]}, {"quantity_id": "q19", "topic": "CoCl2 x 6 H2O", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[1].recipe[5]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "CoCl2 x 6 H2O", "compound_id": 38, "amount": 190, "unit": "mg", "g_l": 0.19, "mmol_l": 1.46335, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 190 mg in its source recipe and provider g_l=0.19. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.19", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 190 mg in its source recipe and provider g_l=0.19. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.19", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 190 mg in its source recipe and provider g_l=0.19. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]}, {"quantity_id": "q20", "topic": "CuCl2 x 2 H2O", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "CuCl2 x 2 H2O", "compound_id": 39, "amount": 2, "unit": "mg", "g_l": 0.002, "mmol_l": 0.0117314, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 2 mg in its source recipe and provider g_l=0.002. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.002", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 2 mg in its source recipe and provider g_l=0.002. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.002", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 2 mg in its source recipe and provider g_l=0.002. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]}, {"quantity_id": "q21", "topic": "NiCl2 x 6 H2O", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[1].recipe[7]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "NiCl2 x 6 H2O", "compound_id": 40, "amount": 24, "unit": "mg", "g_l": 0.024, "mmol_l": 0.185187, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 24 mg in its source recipe and provider g_l=0.024. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.024", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 24 mg in its source recipe and provider g_l=0.024. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.024", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 24 mg in its source recipe and provider g_l=0.024. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]}, {"quantity_id": "q22", "topic": "Na2MoO4 x 2 H2O", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[1].recipe[8]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 36, "unit": "mg", "g_l": 0.036, "mmol_l": 0.148791, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 36 mg in its source recipe and provider g_l=0.036. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.036", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 36 mg in its source recipe and provider g_l=0.036. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.036", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element solution SL-10 stock composition, explicitly 36 mg in its source recipe and provider g_l=0.036. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]}, {"quantity_id": "q23", "topic": "Biotin", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Biotin", "compound_id": 46, "amount": 20, "unit": "mg", "g_l": 0.02, "mmol_l": 0.0818632, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 20 mg in its source recipe and provider g_l=0.02. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 20 mg in its source recipe and provider g_l=0.02. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 20 mg in its source recipe and provider g_l=0.02. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]}, {"quantity_id": "q24", "topic": "Folic acid", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[2].recipe[1]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Folic acid", "compound_id": 138, "amount": 20, "unit": "mg", "g_l": 0.02, "mmol_l": 0.0453104, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 20 mg in its source recipe and provider g_l=0.02. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 20 mg in its source recipe and provider g_l=0.02. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 20 mg in its source recipe and provider g_l=0.02. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]}, {"quantity_id": "q25", "topic": "Pyridoxine hydrochloride", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[2].recipe[2]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "Pyridoxine hydrochloride", "compound_id": 519, "amount": 100, "unit": "mg", "g_l": 0.1, "mmol_l": 0.486287, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 100 mg in its source recipe and provider g_l=0.1. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 100 mg in its source recipe and provider g_l=0.1. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 100 mg in its source recipe and provider g_l=0.1. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]}, {"quantity_id": "q26", "topic": "Thiamine HCl", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[2].recipe[3]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "Thiamine HCl", "compound_id": 1207, "amount": 50, "unit": "mg", "g_l": 0.05, "mmol_l": 0.148236, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]}, {"quantity_id": "q27", "topic": "Riboflavin", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[2].recipe[4]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "Riboflavin", "compound_id": 136, "amount": 50, "unit": "mg", "g_l": 0.05, "mmol_l": 0.132837, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]}, {"quantity_id": "q28", "topic": "Nicotinic acid", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[2].recipe[5]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "Nicotinic acid", "compound_id": 139, "amount": 50, "unit": "mg", "g_l": 0.05, "mmol_l": 0.406141, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[27].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[27].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]}, {"quantity_id": "q29", "topic": "Calcium D-(+)-pantothenate", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[2].recipe[6]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "Calcium D-(+)-pantothenate", "compound_id": 1512, "amount": 50, "unit": "mg", "g_l": 0.05, "mmol_l": 0.209846, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[28].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[28].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]}, {"quantity_id": "q30", "topic": "Vitamin B12", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[2].recipe[7]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "Vitamin B12", "compound_id": 18, "amount": 1, "unit": "mg", "g_l": 0.001, "mmol_l": 0.00073779, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 1 mg in its source recipe and provider g_l=0.001. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[29].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 1 mg in its source recipe and provider g_l=0.001. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[29].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 1 mg in its source recipe and provider g_l=0.001. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]}, {"quantity_id": "q31", "topic": "p-Aminobenzoic acid", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[2].recipe[8]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "p-Aminobenzoic acid", "compound_id": 47, "amount": 50, "unit": "mg", "g_l": 0.05, "mmol_l": 0.364591, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[30].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[30].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]}, {"quantity_id": "q32", "topic": "(DL)-alpha-Lipoic acid", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[2].recipe[9]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "(DL)-alpha-Lipoic acid", "compound_id": 252, "amount": 50, "unit": "mg", "g_l": 0.05, "mmol_l": 0.24233, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[31].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ingredients[31].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin's vitamin solution (10x) stock composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within the scoped stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]}, {"quantity_id": "q33", "topic": "main recipe: Trace element solution SL-10", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "solution": "Trace element solution SL-10", "solution_id": 595, "amount": 1, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Retain 1 ml as the source main recipe amount. This is a receiving stock dose or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain 1 ml as the source main recipe amount. This is a receiving stock dose or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium volume.", "missing": true}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain 1 ml as the source main recipe amount. This is a receiving stock dose or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium volume.", "missing": true}]}, {"quantity_id": "q34", "topic": "main recipe: Wolin's vitamin solution (10x)", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[0].recipe[12]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 13, "solution": "Wolin's vitamin solution (10x)", "solution_id": 5980, "amount": 1, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Retain 1 ml as the source main recipe amount. This is a receiving stock dose or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain 1 ml as the source main recipe amount. This is a receiving stock dose or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium volume.", "missing": true}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain 1 ml as the source main recipe amount. This is a receiving stock dose or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium volume.", "missing": true}]}, {"quantity_id": "q35", "topic": "main recipe: Distilled water", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[0].recipe[15]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 16, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Retain 1000 ml as the source main recipe amount. This is a receiving stock dose or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "notes", "stored_value": "Source: DSMZ &#124; Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium902.pdf", "decision": "add", "rationale": "Retain 1000 ml as the source main recipe amount. This is a receiving stock dose or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium volume."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "notes", "stored_value": "Source: DSMZ &#124; Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium902.pdf", "decision": "add", "rationale": "Retain 1000 ml as the source main recipe amount. This is a receiving stock dose or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium volume."}]}, {"quantity_id": "q36", "topic": "Trace element solution SL-10: Distilled water", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[1].recipe[9]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "Distilled water", "compound_id": 4, "amount": 990, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Retain 990 ml as the source Trace element solution SL-10 amount. This is a receiving stock dose or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain 990 ml as the source Trace element solution SL-10 amount. This is a receiving stock dose or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium volume.", "missing": true}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain 990 ml as the source Trace element solution SL-10 amount. This is a receiving stock dose or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium volume.", "missing": true}]}, {"quantity_id": "q37", "topic": "Wolin's vitamin solution (10x): Distilled water", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[2].recipe[10]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Retain 1000 ml as the source Wolin's vitamin solution (10x) amount. This is a receiving stock dose or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain 1000 ml as the source Wolin's vitamin solution (10x) amount. This is a receiving stock dose or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium volume.", "missing": true}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain 1000 ml as the source Wolin's vitamin solution (10x) amount. This is a receiving stock dose or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium volume.", "missing": true}]}, {"quantity_id": "q38", "topic": "Existing main preparation including every numeric condition", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"step\": \"Dissolve ingredients except bicarbonate, pyruvate, vitamins and reducing agents, then adjust pH of solution to 7.0 with NaOH. Sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic, then dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add pyruvate, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 7.0, if necessary.\"\n                    }", "exact_decoded_object": {"step": "Dissolve ingredients except bicarbonate, pyruvate, vitamins and reducing agents, then adjust pH of solution to 7.0 with NaOH. Sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic, then dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add pyruvate, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 7.0, if necessary."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The complete main preparation is already retained, including pH7, N2 sparging30–45 min, stock atmospheres100%N2 or80%N2/20%CO2 and vitamin filtration. Credit the current text; source does not supply autoclave time/temperature or all late-stock strengths/doses.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "preparation_steps[0]", "stored_value": {"step_number": 1, "action": "AUTOCLAVE", "description": "Dissolve ingredients except bicarbonate, pyruvate, vitamins and reducing agents, then adjust pH of solution to 7.0 with NaOH. Sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic, then dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add pyruvate, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 7.0, if necessary."}, "decision": "evidence_only", "rationale": "The complete main preparation is already retained, including pH7, N2 sparging30–45 min, stock atmospheres100%N2 or80%N2/20%CO2 and vitamin filtration. Credit the current text; source does not supply autoclave time/temperature or all late-stock strengths/doses."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "preparation_steps[0]", "stored_value": {"step_number": 1, "action": "AUTOCLAVE", "description": "Dissolve ingredients except bicarbonate, pyruvate, vitamins and reducing agents, then adjust pH of solution to 7.0 with NaOH. Sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic, then dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add pyruvate, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 7.0, if necessary."}, "decision": "evidence_only", "rationale": "The complete main preparation is already retained, including pH7, N2 sparging30–45 min, stock atmospheres100%N2 or80%N2/20%CO2 and vitamin filtration. Credit the current text; source does not supply autoclave time/temperature or all late-stock strengths/doses."}]}, {"quantity_id": "q39", "topic": "Existing SL-10 preparation including every numeric condition", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8", "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T07:48:20.053969Z", "quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "exact_decoded_object": {"step": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The existing text correctly gives SL-10 final makeup1000 ml, but its root preparation placement lacks stock-stage scope. Keep the instruction on SL-10; it is not the receiving-medium final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "preparation_steps[1]", "stored_value": {"step_number": 2, "action": "DISSOLVE", "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}, "decision": "correct", "rationale": "The existing text correctly gives SL-10 final makeup1000 ml, but its root preparation placement lacks stock-stage scope. Keep the instruction on SL-10; it is not the receiving-medium final volume."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "preparation_steps[1]", "stored_value": {"step_number": 2, "action": "DISSOLVE", "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}, "decision": "correct", "rationale": "The existing text correctly gives SL-10 final makeup1000 ml, but its root preparation placement lacks stock-stage scope. Keep the instruction on SL-10; it is not the receiving-medium final volume."}]}, {"quantity_id": "q40", "topic": "Main pH7", "source": [{"evidence_id": "dsm902", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium902.pdf", "raw_path": "REVIEW_WORK/batch060/source01-03/dsm902.bin", "raw_sha256": "a4ea1524e87543e0671e6b7ec76f355f4355eea6e13fbb5b993e2bcc644cf735", "locator": "Page1 main preparation", "accessed_at": "2026-10-28T07:48:20.206078Z", "quote": "adjust pH of solution to 7.0 with NaOH."}], "decision": "evidence_only", "rationale": "Existing pH7 is explicitly supported; no strain-specific optimum inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale": "Existing pH7 is explicitly supported; no strain-specific optimum inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale": "Existing pH7 is explicitly supported; no strain-specific optimum inferred."}]}, {"quantity_id": "q41", "topic": "Late-stock strengths and addition volumes not specified", "source": [{"evidence_id": "dsm902", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium902.pdf", "raw_path": "REVIEW_WORK/batch060/source01-03/dsm902.bin", "raw_sha256": "a4ea1524e87543e0671e6b7ec76f355f4355eea6e13fbb5b993e2bcc644cf735", "locator": "Page1 main preparation", "accessed_at": "2026-10-28T07:48:20.206078Z", "quote": "Add pyruvate, vitamins, cysteine and\nsulfide from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate\nfrom a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture."}], "decision": "unsupported", "rationale": "The source gives batch masses and specified SL-10/vitamin/resazurin additions, but not the strengths or addition volumes for the later pyruvate, cysteine, sulfide and bicarbonate stock preparations. Do not invent these missing quantities.", "layer_assessments": []}]

### Current ontology and MIM correspondence

grounding: concern. Targets: CultureMech:002069.

Every current ontology slot and current MIM row was checked. Sodium-resazurin and nickel supplied-form mismatches require correction. Calcium D-(+)-pantothenate is explicitly specified in the primary vitamin table and the current31345 object is stereospecified; broader biotin/B12/lipoic-acid identifiers do not justify choosing unreported stereoisomers or vitamers. Missing secondary slots alone are not wrong chemistry.

### History and evidence scope

provenance: concern. Targets: CultureMech:002069.

Current source bytes, complete histories and scoped historical reports were read. Missing claim-level linkage and any malformed historical metadata are distinguished from authenticated source bytes; originals remain append-only.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:002069.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:002069.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Separate two stock compositions from the receiving medium

major / open / confirmed; issue key: culturemech-002069-separate-two-stock-compositions-from-the-receiving-medium.

Nineteen rows at ingredients[13]–[31] reproduce SL-10 and Wolin vitamin stock concentrations as direct ingredients. The primary source instead adds1 ml of each stock. Model both stock recipes and receiving doses, retain the main water1000 ml context and all source stock solvents, and scope preparation_steps[1] to SL-10. Credit the 13 explicit API main rates; do not recompute final-medium totals using an unproven physical denominator.

### f2: Resolve supplied sodium and nickel forms

major / open / confirmed; issue key: culturemech-002069-resolve-supplied-sodium-and-nickel-forms.

Sodium resazurin at ingredients[8] uses CHEBI:8806, whose current formula C12H7NO4 contains no sodium; copying that accession to another slot would not fix the supplied-form mismatch. Nickel chloride hexahydrate at ingredients[20] uses anhydrous CHEBI:34887 in both slots; current CHEBI:53542 explicitly represents the hexahydrate. The preferred NiCl2 x6H2O catalog row is REJECTED while an exact chemical-name synonym row is MAPPED; preserve both observations. Na2SiO3 remains ungrounded; the September standalone-solution suggestion is a lead, not authority to copy a term.

### f3: Attach scoped source support without rewriting history

minor / open / confirmed; issue key: culturemech-002069-attach-scoped-source-support-without-rewriting-history.

The current owner and generated target lack attached claim-level source evidence for their ingredient quantities and stock/preparation stages. The fresh API response can authenticate matching historical response bytes, but historical access events and September final-volume or mirror recommendations are not established by that match.

## Recommended Actions And Acceptance Checks

### action1

Curate the maintained owner with separately scoped SL-10 and Wolin vitamin composition and1 ml receiving additions; preserve every source amount, supplied form, solvent and stage-specific preparation. Retain the provider-declared main g_l with its1002 ml metadata context and explicit primary final-volume limitation, then regenerate.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Verify an exact sodium-resazurin salt identifier and label before changing its primary grounding; do not add a neutral-resazurin mirror. Reconcile nickel hexahydrate with the verified53542 supplied form while preserving current catalog statuses. Resolve sodium silicate only from specific authoritative identity evidence. Retain all supported batch amounts.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Add claim-level quantity evidence and root evidence explicitly identifying each solution/preparation stage. Preserve existing history events byte-for-byte; append a new verified review/curation event rather than rewriting earlier timestamps or recommendations.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| identity-search | REVIEW_WORK/batch060/record01/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _parse_api_solutions, _parse_preparation_steps | context_only | Current composition parser restricts ingredients to the primary solution, excludes solvent and recognized stock additions, and retains explicit g_l. The solution parser preserves referenced or percent-defined stocks and source attributes. Preparation parsing still concatenates all solution steps into root preparation_steps; source-stage annotation remains important. These present functions do not prove the historical execution that produced this record. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group copies a sole contributor with merge metadata. For multiple contributors it passes records to merge_formulation_evidence, which checks compatibility; it does not authorize merging different preparation assertions. |
| writer-formulation | src/culturemech/merge/formulation.py; formulation_content, merge_formulation_evidence | context_only | Current compatibility preserves scientific fields and list order and rejects unequal formulations; only specified provenance/evidence lists are unioned. It performs no concentration conversion or stock expansion and does not authenticate historical merges. |
| writer-cleanup | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients, merge_ingredient_group | context_only | Current cleanup groups identical normalized names, keeps the first entry as a base, flags differing concentrations and combines a warning note; it does not sum concentrations. It can still discard distinctions when names repeat, so source stage must be retained. Current behavior does not establish the historical cause of an existing discrepancy. |
| historical-1 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/carcboxydibrachium_medium.yaml.md; Entire exact Record-header report, every claim row and narrative | context_only | Current independently captured API response has exactly the cited historical raw SHA256; all 39 literal JSON snippets and locators match. This authenticates those response bytes, not the historical access time or recommendations. |
| historical-2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/carcboxydibrachium_medium.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-4 | reports/yaml_record_review/20260922T041930Z-CARCBOXYDIBRACHIUM_MEDIUM.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-reader | REVIEW_WORK/batch060/record01/historical-reader.json | context_only | All exact target/owner historical report texts and current raw/literal/locator joins; historical recommendations remain subject to current stage and volume evidence. |
| dsm902 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium902.pdf; Pages 1–2, all tables and preparation paragraphs | supports | Both primary PDF pages read textually and visually: main batch, preparation, SL-10 stock and Wolin vitamin stock. The main water amount is not an explicit final-medium volume; the explicit 1000 ml makeup applies only to SL-10. |
| api902 | https://mediadive.dsmz.de/rest/medium/902; $.data.medium and all $.data.solutions recipes/steps | supports | Complete current response: main solution1855 declares volume1002 and explicit g_l; stocks595 and5980 remain separate. These provider rates do not prove a measured final-volume instruction in the primary PDF. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32588; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31206; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34683; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_8806; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32139; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi50144 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_50144; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91248; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_76209; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17883; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86249; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49976; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86368; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86318; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15956; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_27470; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30961; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49105; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17015; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15940; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31345; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_176843; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30753; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16494; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch060/record01/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch060/record01/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch060/record01/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch060/record01/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch060/record01/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch060/record01/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch060/record01/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch060/record01/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch060/record01/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- The primary902 PDF lists1000 ml main water and late stocks but does not explicitly state a final-medium volume. API1002 is provider-declared metadata, not a measured-final-volume instruction.
- Bare25% HCl lacks a stated percentage basis; provider stock g_l is retained as provider data, not independently converted from that label. Wolin vitamin water1000 ml likewise does not by itself prove a final makeup.
- Late pyruvate, cysteine, sulfide and bicarbonate stock strengths/addition volumes are not fully specified. No typical values or strain-level growth claims were inferred.
- An exact sodium-resazurin replacement accession and the ungrounded sodium-silicate identity remain unresolved. CHEBI:91245, captured as an exploratory lead, is copper(II) chloride pentahydrate and is not used as resazurin evidence.
- Historical raw-response equality authenticates bytes and literal claim objects, not historical execution, retrieval time or all recommendations. Standalone solution records mentioned in September were not newly inspected or adopted.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T075737Z-batch060-record01-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'CARCBOXYDIBRACHIUM MEDIUM: preserve main rates and restore stock stages'
started_at: '2026-10-28T07:45:59.659790Z'
finished_at: '2026-10-28T07:57:37.957067Z'
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
summary: The DSM902 identity and 13 provider-declared main concentrations are supported.
  Nineteen stock-composition rows are incorrectly placed as direct medium ingredients,
  both receiving stock additions and solvent context are missing, and two supplied
  chemical forms conflict with their identifiers. Existing anoxic preparation is substantially
  retained and must be scoped, not replaced.
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
  - path: data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml
    sha256: d18ab925bcc3a4821913bfbad1f1ef012015ee8dfb002fcf003d009bf1401c4e
    role: target
  - path: data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml
    sha256: e8cb7bcab5870c3b11662215bf846c2efb14f7bc29f78b9147384ee99ffa2868
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/carcboxydibrachium_medium.yaml.md
    sha256: ec1c66eace191a72c6b7649c68af8dfa4f556ab3f88589ea975ca22f7631682f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.md
    sha256: 10ef5eb6fd5f1c4c589c4b656c5c9776c0a6e3529f55185513799b8d97d2e435
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/carcboxydibrachium_medium.md
    sha256: d892268d008f171a69d85b9e780c31e0a7bb775fda87becc37b930991d3c4321
    role: context
  - path: reports/yaml_record_review/20260922T041930Z-CARCBOXYDIBRACHIUM_MEDIUM.md
    sha256: 79f7a8a7c192b2a1f7808e0bcf8b4e6f673577ccded53b0156720997d3df9112
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
  selection: Actual batch060 native selection index 01.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:002069
targets:
- target_id: CultureMech:002069
  path: data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml
  label: carcboxydibrachium_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:002069
  command: just validate-schema data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml
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
  - CultureMech:002069
  command: just validate-strict data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml
    --out REVIEW_WORK/batch060/record01/strict.tsv --workers 1
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
  - CultureMech:002069
  command: just validate-terms data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml
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
  - CultureMech:002069
  command: just validate-references data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T07:57:37.860020Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: d18ab925bcc3a4821913bfbad1f1ef012015ee8dfb002fcf003d009bf1401c4e
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T07:57:37.860020Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: e8cb7bcab5870c3b11662215bf846c2efb14f7bc29f78b9147384ee99ffa2868
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch060/record01/identity-search.json
  accessed_at: '2026-10-28T07:57:37.911766Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems resolved uniquely. Similar names and
    source accessions are not promoted to owners.
  snapshot_sha256: ecdedf37d6547bed7f890e4fbc3695be49792d09441298126b06f5d500fdb45e
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _parse_api_solutions, _parse_preparation_steps
  accessed_at: '2026-10-28T07:57:37.860020Z'
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
  accessed_at: '2026-10-28T07:57:37.860020Z'
  support: context_only
  summary: Current merge_group copies a sole contributor with merge metadata. For
    multiple contributors it passes records to merge_formulation_evidence, which checks
    compatibility; it does not authorize merging different preparation assertions.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content, merge_formulation_evidence
  accessed_at: '2026-10-28T07:57:37.860020Z'
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
  accessed_at: '2026-10-28T07:57:37.860020Z'
  support: context_only
  summary: Current cleanup groups identical normalized names, keeps the first entry
    as a base, flags differing concentrations and combines a warning note; it does
    not sum concentrations. It can still discard distinctions when names repeat, so
    source stage must be retained. Current behavior does not establish the historical
    cause of an existing discrepancy.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: historical-1
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/carcboxydibrachium_medium.yaml.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T07:57:37.860020Z'
  support: context_only
  summary: Current independently captured API response has exactly the cited historical
    raw SHA256; all 39 literal JSON snippets and locators match. This authenticates
    those response bytes, not the historical access time or recommendations.
  snapshot_sha256: ec1c66eace191a72c6b7649c68af8dfa4f556ab3f88589ea975ca22f7631682f
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T07:57:37.860020Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: 10ef5eb6fd5f1c4c589c4b656c5c9776c0a6e3529f55185513799b8d97d2e435
- evidence_id: historical-3
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/carcboxydibrachium_medium.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T07:57:37.860020Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: d892268d008f171a69d85b9e780c31e0a7bb775fda87becc37b930991d3c4321
- evidence_id: historical-4
  kind: record_content
  reference: reports/yaml_record_review/20260922T041930Z-CARCBOXYDIBRACHIUM_MEDIUM.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T07:57:37.860020Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: 79f7a8a7c192b2a1f7808e0bcf8b4e6f673577ccded53b0156720997d3df9112
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch060/record01/historical-reader.json
  accessed_at: '2026-10-28T07:57:37.914794Z'
  support: context_only
  summary: All exact target/owner historical report texts and current raw/literal/locator
    joins; historical recommendations remain subject to current stage and volume evidence.
  snapshot_sha256: 9f054fc6c050dfea88ec668ba0191acf3fb1b4ef27cd1510891d86d4b1790619
- evidence_id: dsm902
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium902.pdf
  locator: Pages 1–2, all tables and preparation paragraphs
  accessed_at: '2026-10-28T07:48:20.206078Z'
  support: supports
  summary: 'Both primary PDF pages read textually and visually: main batch, preparation,
    SL-10 stock and Wolin vitamin stock. The main water amount is not an explicit
    final-medium volume; the explicit 1000 ml makeup applies only to SL-10.'
  snapshot_sha256: a4ea1524e87543e0671e6b7ec76f355f4355eea6e13fbb5b993e2bcc644cf735
- evidence_id: api902
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/902
  locator: $.data.medium and all $.data.solutions recipes/steps
  accessed_at: '2026-10-28T07:48:20.053969Z'
  support: supports
  summary: 'Complete current response: main solution1855 declares volume1002 and explicit
    g_l; stocks595 and5980 remain separate. These provider rates do not prove a measured
    final-volume instruction in the primary PDF.'
  snapshot_sha256: 85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8
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
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32588
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:26.473452Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 8fc333e98ee953346b5c291b9e5765e77d03cc46740a1282af3e5f4ad355de1a
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
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:29.594002Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: df8f702eb5b9d3e50209bfa2b0c4b6f1db30c116e56a58e348cbd4bf3bc0ebc1
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31206
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:25.230031Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: c70055293606f21dcdfb72325a4677661b51efb723ba9357efab43f8ec9b03f7
- evidence_id: chebi34683
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34683
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:26.883514Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b8fc153769cf791f5e08680678fe7df66be98486bbfbb734518f3de625596efe
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_8806
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:30.886467Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: ceb05e9dd7fba3802d28b34c50bbb604ded87951e4ea3a812739824a84648d72
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32139
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:25.925820Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 314c75cd12ea5d1343b4c0bafd40e0ad72c15b19d64f8cb9152000c0d8839f56
- evidence_id: chebi50144
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_50144
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:27.897977Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 5cbd7ac1ce425bbe4d80bc9e815f0bf02693123023342deddf3bb962108bfd10
- evidence_id: chebi91248
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91248
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:30.993081Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 98a5682728cfda4162de150a88ae8c4b3a70c2d7c248634a5108be50a888a692
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_76209
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:29.309113Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 3eece7d96d2433ff020ece90db55323d138c5c828b78198f91d26b3eafa91f9f
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17883
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:23.970715Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 5f7b2f292559b9033f3c62c8403ed552842a28535010d6af5daa018a0977c28d
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86249
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:29.604638Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 69797bf2582679b3f621fa4f982077ed90f48f3a5e1293c7444a3aaacbb25ba2
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49976
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:27.769771Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2d2305ca671adbbd3b0cc07b2331373a768bb44d41f32f61ba894594ae470eff
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86368
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:30.505165Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2bb4588e6734285b5536bdac78701f9800fdb8d17236d12cf5a1c30490f1614d
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
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86318
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:29.913144Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 8ba4e0a242571ae9a62ca7ba5c0f4af765962a02f5119a96d47dda9df7c9d593
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:27.082549Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a43b8268f70ae50c4cfbc53e12bbd195618c521619cfab8f71d3704b338af95b
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
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15956
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:23.253093Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0d2e75e0bd98dbffff14d85a41dfd0af8aae2a8d65a945d34a4126a17091c2b8
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_27470
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:24.718246Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: dcee85bb585d3a73341ab66eff772dc6361330b3c899c4daecbda49d5e84e590
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30961
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:25.064130Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 491af523ba70d13857fcb828561d0556e46382fa0591011a06693d7db24ad91f
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49105
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:27.692039Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: fc6b8e9d8657914ed8fd568c69d8a5b2cf41b26767bd6361a5e2d258883be97d
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17015
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:23.977351Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f8bec809c7ba5a36faea58b8fe1b5110f0d75dbd4ac1929a121cd352bce63309
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15940
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:23.237820Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2890ef915cd546e70c1e638af285a3cc19b8299ae7722d00b43a40170a57ab8a
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31345
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:25.316800Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: d2a04309eb6976fd395f9684ec4c3f5192362e2b6b75464b0af128a28e188d25
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_176843
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:23.841698Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 5c42e2236866d0314bc8d45947ddf9eb2fdf6364d08e802b0fb271011cbfe563
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30753
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:24.830018Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 42ea4022bd68e8fa28962bc496ca757174da7bbd18ce06b7f3d521885609a50c
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16494
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:23.355188Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: db6824ffab0d71efc11d1e64b505ae583949e9d5837086a4b0e7b364b2933a22
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch060/record01/quantity-inventory.json
  accessed_at: '2026-10-28T07:57:37.956426Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 8a130438af4fe95129b4596b99daac248dc2988a882ebe29460770c99cdbc694
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch060/record01/grounding-inventory.json
  accessed_at: '2026-10-28T07:57:37.956492Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: 46b40bdadf15f2dae94b548dcd7e89d9dc50ddcb22cab161ef5af90fb4a211d7
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch060/record01/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T07:57:37.956631Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 1052016f7dc1184b24149ef5f6415d9c79dc400b0edb249175ad85269482bc18
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch060/record01/scalar-census.json
  accessed_at: '2026-10-28T07:57:37.956651Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: eeee8846cd5b134987effdbbac8ee91a1212825ff98ca191a80c43170a67e565
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch060/record01/validate-schema.json
  accessed_at: '2026-10-28T07:46:00.854341Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: 4e683a12a5ce1334a85ab87a083b4b4393eca336ba252c25d1602fe67be20eb4
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch060/record01/validate-strict.json
  accessed_at: '2026-10-28T07:46:01.882234Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch060/record01/strict.tsv\n"
  snapshot_sha256: 79a8c0292a661b462bc06b7d4dd997c29f946be7f085eabf70e8c095b05d8188
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch060/record01/validate-terms.json
  accessed_at: '2026-10-28T07:46:02.997496Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: 93c23fff6d373e1f9a6d28b7d30736ccf7137a04f128cf7094018e000795ea1d
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch060/record01/validate-references.json
  accessed_at: '2026-10-28T07:46:03.819448Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: 9f35ccd831b3738796c4bfc36e31df1e3220b3bf68eb0670a68523cdd21de2aa
assessments:
- assessment_id: a1
  area: identity
  topic: Exact source and ownership
  outcome: supported
  summary: The generated target has one maintained DSM902 owner. Primary PDF and current
    provider use the same CARCBOXYDIBRACHIUM title; no speculative spelling correction
    or transfer from a similarly named medium is proposed. Bacterial/complex/undefined/liquid
    classification agrees with source metadata and yeast extract.
  target_ids:
  - CultureMech:002069
  evidence_ids:
  - local-target
  - owner-1
  - identity-search
  - dsm902
  - api902
- assessment_id: a2
  area: completeness
  topic: Current preparation and missing topology
  outcome: concern
  summary: Main pH and preparation are already present. Restore stock objects/doses
    and water context while relocating only the SL-10-specific makeup instruction.
    The main provider rates are supported independently of the obsolete blanket conflict
    labels in the October report.
  target_ids:
  - CultureMech:002069
  evidence_ids:
  - dsm902
  - api902
  - writer-mediadive
  - writer-cleanup
  - historical-reader
- assessment_id: a3
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:002069
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "NaCl", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\":
    20,\n                        \"unit\": \"g\",\n                        \"g_l\":
    19.9601,\n                        \"mmol_l\": 341.548,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "NaCl", "compound_id": 43, "amount": 20, "unit": "g", "g_l": 19.9601, "mmol_l":
    341.548, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "evidence_only",
    "rationale": "Current API main-solution row explicitly declares 19.9601 g/L and
    supplies the source batch amount 20 g. Retain this declared main-stage rate with
    exact evidence and provider volume1002 context; the PDF water1000 ml is not proof
    of a final-medium denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "19.9601",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 19.9601 g/L and supplies the source batch amount 20 g.
    Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path":
    "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[0].concentration", "stored_value": {"value": "19.9601", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "Current API main-solution row explicitly
    declares 19.9601 g/L and supplies the source batch amount 20 g. Retain this declared
    main-stage rate with exact evidence and provider volume1002 context; the PDF water1000
    ml is not proof of a final-medium denominator."}]}, {"quantity_id": "q2", "topic":
    "KCl", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\":
    0.7,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.698603,\n                        \"mmol_l\": 9.37093,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "KCl", "compound_id": 61, "amount": 0.7, "unit": "g", "g_l": 0.698603, "mmol_l":
    9.37093, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "evidence_only",
    "rationale": "Current API main-solution row explicitly declares 0.698603 g/L and
    supplies the source batch amount 0.7 g. Retain this declared main-stage rate with
    exact evidence and provider volume1002 context; the PDF water1000 ml is not proof
    of a final-medium denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.698603",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 0.698603 g/L and supplies the source batch amount 0.7
    g. Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path":
    "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[1].concentration", "stored_value": {"value": "0.698603", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 0.698603 g/L and supplies the source batch amount 0.7
    g. Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator."}]},
    {"quantity_id": "q3", "topic": "MgSO4 x 7 H2O", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\":
    3.9,\n                        \"unit\": \"g\",\n                        \"g_l\":
    3.89222,\n                        \"mmol_l\": 15.7915,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "MgSO4 x 7 H2O", "compound_id": 8, "amount": 3.9, "unit": "g", "g_l": 3.89222,
    "mmol_l": 15.7915, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "evidence_only", "rationale": "Current API main-solution row explicitly declares
    3.89222 g/L and supplies the source batch amount 3.9 g. Retain this declared main-stage
    rate with exact evidence and provider volume1002 context; the PDF water1000 ml
    is not proof of a final-medium denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "3.89222",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 3.89222 g/L and supplies the source batch amount 3.9 g.
    Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path":
    "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[2].concentration", "stored_value": {"value": "3.89222", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "Current API main-solution row explicitly
    declares 3.89222 g/L and supplies the source batch amount 3.9 g. Retain this declared
    main-stage rate with exact evidence and provider volume1002 context; the PDF water1000
    ml is not proof of a final-medium denominator."}]}, {"quantity_id": "q4", "topic":
    "CaCl2 x 2 H2O", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\":
    0.4,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.399202,\n                        \"mmol_l\": 2.71538,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "CaCl2 x 2 H2O", "compound_id": 7, "amount": 0.4, "unit": "g", "g_l": 0.399202,
    "mmol_l": 2.71538, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "evidence_only", "rationale": "Current API main-solution row explicitly declares
    0.399202 g/L and supplies the source batch amount 0.4 g. Retain this declared
    main-stage rate with exact evidence and provider volume1002 context; the PDF water1000
    ml is not proof of a final-medium denominator.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[3].concentration",
    "stored_value": {"value": "0.399202", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "Current API main-solution row explicitly declares 0.399202 g/L and
    supplies the source batch amount 0.4 g. Retain this declared main-stage rate with
    exact evidence and provider volume1002 context; the PDF water1000 ml is not proof
    of a final-medium denominator."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.399202",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 0.399202 g/L and supplies the source batch amount 0.4
    g. Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator."}]},
    {"quantity_id": "q5", "topic": "NH4Cl", "source": [{"evidence_id": "api902", "reference":
    "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\":
    0.3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.299401,\n                        \"mmol_l\": 5.59733,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "NH4Cl", "compound_id": 42, "amount": 0.3, "unit": "g", "g_l": 0.299401, "mmol_l":
    5.59733, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "evidence_only",
    "rationale": "Current API main-solution row explicitly declares 0.299401 g/L and
    supplies the source batch amount 0.3 g. Retain this declared main-stage rate with
    exact evidence and provider volume1002 context; the PDF water1000 ml is not proof
    of a final-medium denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.299401",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 0.299401 g/L and supplies the source batch amount 0.3
    g. Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path":
    "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[4].concentration", "stored_value": {"value": "0.299401", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 0.299401 g/L and supplies the source batch amount 0.3
    g. Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator."}]},
    {"quantity_id": "q6", "topic": "Na2HPO4", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Na2HPO4\",\n                        \"compound_id\": 233,\n                        \"amount\":
    0.15,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.149701,\n                        \"mmol_l\": 1.05453,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "Na2HPO4", "compound_id": 233, "amount": 0.15, "unit": "g", "g_l": 0.149701, "mmol_l":
    1.05453, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "evidence_only",
    "rationale": "Current API main-solution row explicitly declares 0.149701 g/L and
    supplies the source batch amount 0.15 g. Retain this declared main-stage rate
    with exact evidence and provider volume1002 context; the PDF water1000 ml is not
    proof of a final-medium denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.149701",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 0.149701 g/L and supplies the source batch amount 0.15
    g. Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path":
    "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[5].concentration", "stored_value": {"value": "0.149701", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 0.149701 g/L and supplies the source batch amount 0.15
    g. Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator."}]},
    {"quantity_id": "q7", "topic": "Na2SiO3", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"Na2SiO3\",\n                        \"compound_id\": 823,\n                        \"amount\":
    0.03,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.0299401,\n                        \"mmol_l\": 0.245284,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "Na2SiO3", "compound_id": 823, "amount": 0.03, "unit": "g", "g_l": 0.0299401,
    "mmol_l": 0.245284, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "evidence_only", "rationale": "Current API main-solution row explicitly declares
    0.0299401 g/L and supplies the source batch amount 0.03 g. Retain this declared
    main-stage rate with exact evidence and provider volume1002 context; the PDF water1000
    ml is not proof of a final-medium denominator.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[6].concentration",
    "stored_value": {"value": "0.0299401", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "Current API main-solution row explicitly declares 0.0299401 g/L
    and supplies the source batch amount 0.03 g. Retain this declared main-stage rate
    with exact evidence and provider volume1002 context; the PDF water1000 ml is not
    proof of a final-medium denominator."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.0299401",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 0.0299401 g/L and supplies the source batch amount 0.03
    g. Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator."}]},
    {"quantity_id": "q8", "topic": "Yeast extract", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\":
    0.05,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.0499002,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 8, "compound": "Yeast extract", "compound_id": 16, "amount":
    0.05, "unit": "g", "g_l": 0.0499002, "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "evidence_only", "rationale": "Current API main-solution row explicitly
    declares 0.0499002 g/L and supplies the source batch amount 0.05 g. Retain this
    declared main-stage rate with exact evidence and provider volume1002 context;
    the PDF water1000 ml is not proof of a final-medium denominator.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "ingredients[7].concentration", "stored_value": {"value": "0.0499002", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 0.0499002 g/L and supplies the source batch amount 0.05
    g. Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path":
    "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[7].concentration", "stored_value": {"value": "0.0499002", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 0.0499002 g/L and supplies the source batch amount 0.05
    g. Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator."}]},
    {"quantity_id": "q9", "topic": "Sodium resazurin", "source": [{"evidence_id":
    "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path":
    "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\":
    \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.000499002,\n                        \"mmol_l\":
    0.00198671,\n                        \"optional\": 0\n                    }",
    "exact_decoded_object": {"recipe_order": 10, "compound": "Sodium resazurin", "compound_id":
    1852, "attribute": "0.1% w/v", "amount": 0.5, "unit": "ml", "g_l": 0.000499002,
    "mmol_l": 0.00198671, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "evidence_only", "rationale": "Current API main-solution row explicitly declares
    0.000499002 g/L and supplies the source batch amount 0.5 ml. Retain this declared
    main-stage rate with exact evidence and provider volume1002 context; the PDF water1000
    ml is not proof of a final-medium denominator. The primary 0.5 ml of 0.1% w/v
    sodium resazurin supplies 0.5 mg per batch; correcting its chemical identifier
    does not change that amount.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.000499002",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 0.000499002 g/L and supplies the source batch amount 0.5
    ml. Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator. The
    primary 0.5 ml of 0.1% w/v sodium resazurin supplies 0.5 mg per batch; correcting
    its chemical identifier does not change that amount."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.000499002",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 0.000499002 g/L and supplies the source batch amount 0.5
    ml. Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator. The
    primary 0.5 ml of 0.1% w/v sodium resazurin supplies 0.5 mg per batch; correcting
    its chemical identifier does not change that amount."}]}, {"quantity_id": "q10",
    "topic": "NaHCO3", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[0].recipe[10]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.499002,\n                        \"mmol_l\": 5.94,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound":
    "NaHCO3", "compound_id": 55, "amount": 0.5, "unit": "g", "g_l": 0.499002, "mmol_l":
    5.94, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "evidence_only",
    "rationale": "Current API main-solution row explicitly declares 0.499002 g/L and
    supplies the source batch amount 0.5 g. Retain this declared main-stage rate with
    exact evidence and provider volume1002 context; the PDF water1000 ml is not proof
    of a final-medium denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.499002",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 0.499002 g/L and supplies the source batch amount 0.5
    g. Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path":
    "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[9].concentration", "stored_value": {"value": "0.499002", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 0.499002 g/L and supplies the source batch amount 0.5
    g. Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator."}]},
    {"quantity_id": "q11", "topic": "Na-pyruvate", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[0].recipe[11]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\":
    \"Na-pyruvate\",\n                        \"compound_id\": 113,\n                        \"amount\":
    2.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    2.49501,\n                        \"mmol_l\": 22.6728,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 12, "compound":
    "Na-pyruvate", "compound_id": 113, "amount": 2.5, "unit": "g", "g_l": 2.49501,
    "mmol_l": 22.6728, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "evidence_only", "rationale": "Current API main-solution row explicitly declares
    2.49501 g/L and supplies the source batch amount 2.5 g. Retain this declared main-stage
    rate with exact evidence and provider volume1002 context; the PDF water1000 ml
    is not proof of a final-medium denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "2.49501",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 2.49501 g/L and supplies the source batch amount 2.5 g.
    Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator."}, {"path":
    "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[10].concentration", "stored_value": {"value": "2.49501", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 2.49501 g/L and supplies the source batch amount 2.5 g.
    Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator."}]},
    {"quantity_id": "q12", "topic": "L-Cysteine HCl x H2O", "source": [{"evidence_id":
    "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path":
    "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[0].recipe[13]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\":
    \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\":
    0.45,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.449102,\n                        \"mmol_l\": 2.557,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 14, "compound":
    "L-Cysteine HCl x H2O", "compound_id": 770, "amount": 0.45, "unit": "g", "g_l":
    0.449102, "mmol_l": 2.557, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "evidence_only", "rationale": "Current API main-solution row explicitly declares
    0.449102 g/L and supplies the source batch amount 0.45 g. Retain this declared
    main-stage rate with exact evidence and provider volume1002 context; the PDF water1000
    ml is not proof of a final-medium denominator.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[11].concentration",
    "stored_value": {"value": "0.449102", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "Current API main-solution row explicitly declares 0.449102 g/L and
    supplies the source batch amount 0.45 g. Retain this declared main-stage rate
    with exact evidence and provider volume1002 context; the PDF water1000 ml is not
    proof of a final-medium denominator."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.449102",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 0.449102 g/L and supplies the source batch amount 0.45
    g. Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator."}]},
    {"quantity_id": "q13", "topic": "Na2S x 9 H2O", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[0].recipe[14]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\":
    \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\":
    0.45,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.449102,\n                        \"mmol_l\": 1.86984,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 15, "compound":
    "Na2S x 9 H2O", "compound_id": 54, "amount": 0.45, "unit": "g", "g_l": 0.449102,
    "mmol_l": 1.86984, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "evidence_only", "rationale": "Current API main-solution row explicitly declares
    0.449102 g/L and supplies the source batch amount 0.45 g. Retain this declared
    main-stage rate with exact evidence and provider volume1002 context; the PDF water1000
    ml is not proof of a final-medium denominator.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "ingredients[12].concentration",
    "stored_value": {"value": "0.449102", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "Current API main-solution row explicitly declares 0.449102 g/L and
    supplies the source batch amount 0.45 g. Retain this declared main-stage rate
    with exact evidence and provider volume1002 context; the PDF water1000 ml is not
    proof of a final-medium denominator."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.449102",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Current API main-solution
    row explicitly declares 0.449102 g/L and supplies the source batch amount 0.45
    g. Retain this declared main-stage rate with exact evidence and provider volume1002
    context; the PDF water1000 ml is not proof of a final-medium denominator."}]},
    {"quantity_id": "q14", "topic": "HCl", "source": [{"evidence_id": "api902", "reference":
    "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\":
    \"25%\",\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\":
    68.5683,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 1, "compound": "HCl", "compound_id": 68, "attribute": "25%",
    "amount": 10, "unit": "ml", "g_l": 2.5, "mmol_l": 68.5683, "optional": 0}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}], "decision": "correct", "rationale": "This is Trace element solution
    SL-10 stock composition, explicitly 10 ml in its source recipe and provider g_l=2.5.
    It is not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred.
    The bare25% HCl source does not state a mass/volume basis, so the provider2.5
    g/L must not be presented as an independently derived primary-source conversion.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "2.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element
    solution SL-10 stock composition, explicitly 10 ml in its source recipe and provider
    g_l=2.5. It is not a direct receiving-medium concentration. Retain it only within
    the scoped stock and retain the separate1 ml addition; no physical final-medium
    rate is inferred. The bare25% HCl source does not state a mass/volume basis, so
    the provider2.5 g/L must not be presented as an independently derived primary-source
    conversion."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "2.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Trace element
    solution SL-10 stock composition, explicitly 10 ml in its source recipe and provider
    g_l=2.5. It is not a direct receiving-medium concentration. Retain it only within
    the scoped stock and retain the separate1 ml addition; no physical final-medium
    rate is inferred. The bare25% HCl source does not state a mass/volume basis, so
    the provider2.5 g/L must not be presented as an independently derived primary-source
    conversion."}]}, {"quantity_id": "q15", "topic": "FeCl2 x 4 H2O", "source": [{"evidence_id":
    "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path":
    "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\":
    1.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "FeCl2 x 4 H2O", "compound_id": 260, "amount": 1.5, "unit": "g", "g_l": 1.5, "mmol_l":
    7.54482, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Trace element solution SL-10 stock composition, explicitly
    1.5 g in its source recipe and provider g_l=1.5. It is not a direct receiving-medium
    concentration. Retain it only within the scoped stock and retain the separate1
    ml addition; no physical final-medium rate is inferred.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "ingredients[14].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Trace element solution SL-10 stock
    composition, explicitly 1.5 g in its source recipe and provider g_l=1.5. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."},
    {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[14].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Trace element solution SL-10 stock
    composition, explicitly 1.5 g in its source recipe and provider g_l=1.5. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]},
    {"quantity_id": "q16", "topic": "ZnCl2", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\":
    70,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "ZnCl2", "compound_id": 64, "amount": 70, "unit": "mg", "g_l": 0.07, "mmol_l":
    0.513573, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Trace element solution SL-10 stock composition, explicitly
    70 mg in its source recipe and provider g_l=0.07. It is not a direct receiving-medium
    concentration. Retain it only within the scoped stock and retain the separate1
    ml addition; no physical final-medium rate is inferred.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "ingredients[15].concentration", "stored_value": {"value": "0.07", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Trace element solution SL-10 stock
    composition, explicitly 70 mg in its source recipe and provider g_l=0.07. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."},
    {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[15].concentration", "stored_value": {"value": "0.07", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Trace element solution SL-10 stock
    composition, explicitly 70 mg in its source recipe and provider g_l=0.07. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]},
    {"quantity_id": "q17", "topic": "MnCl2 x 4 H2O", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[1].recipe[3]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\":
    100,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "MnCl2 x 4 H2O", "compound_id": 36, "amount": 100, "unit": "mg", "g_l": 0.1, "mmol_l":
    0.505293, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Trace element solution SL-10 stock composition, explicitly
    100 mg in its source recipe and provider g_l=0.1. It is not a direct receiving-medium
    concentration. Retain it only within the scoped stock and retain the separate1
    ml addition; no physical final-medium rate is inferred.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "ingredients[16].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Trace element solution SL-10 stock
    composition, explicitly 100 mg in its source recipe and provider g_l=0.1. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."},
    {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[16].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Trace element solution SL-10 stock
    composition, explicitly 100 mg in its source recipe and provider g_l=0.1. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]},
    {"quantity_id": "q18", "topic": "H3BO3", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[1].recipe[4]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\":
    6,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "H3BO3", "compound_id": 37, "amount": 6, "unit": "mg", "g_l": 0.006, "mmol_l":
    0.0970246, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Trace element solution SL-10 stock composition, explicitly
    6 mg in its source recipe and provider g_l=0.006. It is not a direct receiving-medium
    concentration. Retain it only within the scoped stock and retain the separate1
    ml addition; no physical final-medium rate is inferred.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "ingredients[17].concentration", "stored_value": {"value": "0.006", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Trace element solution SL-10 stock
    composition, explicitly 6 mg in its source recipe and provider g_l=0.006. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."},
    {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[17].concentration", "stored_value": {"value": "0.006", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Trace element solution SL-10 stock
    composition, explicitly 6 mg in its source recipe and provider g_l=0.006. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]},
    {"quantity_id": "q19", "topic": "CoCl2 x 6 H2O", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[1].recipe[5]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\":
    190,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "CoCl2 x 6 H2O", "compound_id": 38, "amount": 190, "unit": "mg", "g_l": 0.19,
    "mmol_l": 1.46335, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "This is Trace element solution SL-10 stock composition,
    explicitly 190 mg in its source recipe and provider g_l=0.19. It is not a direct
    receiving-medium concentration. Retain it only within the scoped stock and retain
    the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "ingredients[18].concentration", "stored_value": {"value": "0.19", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Trace element solution SL-10 stock
    composition, explicitly 190 mg in its source recipe and provider g_l=0.19. It
    is not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."},
    {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[18].concentration", "stored_value": {"value": "0.19", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Trace element solution SL-10 stock
    composition, explicitly 190 mg in its source recipe and provider g_l=0.19. It
    is not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]},
    {"quantity_id": "q20", "topic": "CuCl2 x 2 H2O", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\":
    2,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "CuCl2 x 2 H2O", "compound_id": 39, "amount": 2, "unit": "mg", "g_l": 0.002, "mmol_l":
    0.0117314, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Trace element solution SL-10 stock composition, explicitly
    2 mg in its source recipe and provider g_l=0.002. It is not a direct receiving-medium
    concentration. Retain it only within the scoped stock and retain the separate1
    ml addition; no physical final-medium rate is inferred.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "ingredients[19].concentration", "stored_value": {"value": "0.002", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Trace element solution SL-10 stock
    composition, explicitly 2 mg in its source recipe and provider g_l=0.002. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."},
    {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[19].concentration", "stored_value": {"value": "0.002", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Trace element solution SL-10 stock
    composition, explicitly 2 mg in its source recipe and provider g_l=0.002. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]},
    {"quantity_id": "q21", "topic": "NiCl2 x 6 H2O", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[1].recipe[7]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\":
    24,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound":
    "NiCl2 x 6 H2O", "compound_id": 40, "amount": 24, "unit": "mg", "g_l": 0.024,
    "mmol_l": 0.185187, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "This is Trace element solution SL-10 stock composition,
    explicitly 24 mg in its source recipe and provider g_l=0.024. It is not a direct
    receiving-medium concentration. Retain it only within the scoped stock and retain
    the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "ingredients[20].concentration", "stored_value": {"value": "0.024", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Trace element solution SL-10 stock
    composition, explicitly 24 mg in its source recipe and provider g_l=0.024. It
    is not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."},
    {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[20].concentration", "stored_value": {"value": "0.024", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Trace element solution SL-10 stock
    composition, explicitly 24 mg in its source recipe and provider g_l=0.024. It
    is not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]},
    {"quantity_id": "q22", "topic": "Na2MoO4 x 2 H2O", "source": [{"evidence_id":
    "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path":
    "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[1].recipe[8]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\":
    36,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound":
    "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 36, "unit": "mg", "g_l": 0.036,
    "mmol_l": 0.148791, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "This is Trace element solution SL-10 stock composition,
    explicitly 36 mg in its source recipe and provider g_l=0.036. It is not a direct
    receiving-medium concentration. Retain it only within the scoped stock and retain
    the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "ingredients[21].concentration", "stored_value": {"value": "0.036", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Trace element solution SL-10 stock
    composition, explicitly 36 mg in its source recipe and provider g_l=0.036. It
    is not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."},
    {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[21].concentration", "stored_value": {"value": "0.036", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Trace element solution SL-10 stock
    composition, explicitly 36 mg in its source recipe and provider g_l=0.036. It
    is not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]},
    {"quantity_id": "q23", "topic": "Biotin", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\":
    20,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Biotin", "compound_id": 46, "amount": 20, "unit": "mg", "g_l": 0.02, "mmol_l":
    0.0818632, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Wolin''s vitamin solution (10x) stock composition, explicitly
    20 mg in its source recipe and provider g_l=0.02. It is not a direct receiving-medium
    concentration. Retain it only within the scoped stock and retain the separate1
    ml addition; no physical final-medium rate is inferred.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "ingredients[22].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock
    composition, explicitly 20 mg in its source recipe and provider g_l=0.02. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."},
    {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[22].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock
    composition, explicitly 20 mg in its source recipe and provider g_l=0.02. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]},
    {"quantity_id": "q24", "topic": "Folic acid", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[2].recipe[1]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\":
    20,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "Folic acid", "compound_id": 138, "amount": 20, "unit": "mg", "g_l": 0.02, "mmol_l":
    0.0453104, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Wolin''s vitamin solution (10x) stock composition, explicitly
    20 mg in its source recipe and provider g_l=0.02. It is not a direct receiving-medium
    concentration. Retain it only within the scoped stock and retain the separate1
    ml addition; no physical final-medium rate is inferred.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "ingredients[23].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock
    composition, explicitly 20 mg in its source recipe and provider g_l=0.02. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."},
    {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[23].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock
    composition, explicitly 20 mg in its source recipe and provider g_l=0.02. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]},
    {"quantity_id": "q25", "topic": "Pyridoxine hydrochloride", "source": [{"evidence_id":
    "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path":
    "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[2].recipe[2]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\":
    100,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "Pyridoxine hydrochloride", "compound_id": 519, "amount": 100, "unit": "mg", "g_l":
    0.1, "mmol_l": 0.486287, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock composition,
    explicitly 100 mg in its source recipe and provider g_l=0.1. It is not a direct
    receiving-medium concentration. Retain it only within the scoped stock and retain
    the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "ingredients[24].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock
    composition, explicitly 100 mg in its source recipe and provider g_l=0.1. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."},
    {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[24].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock
    composition, explicitly 100 mg in its source recipe and provider g_l=0.1. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]},
    {"quantity_id": "q26", "topic": "Thiamine HCl", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[2].recipe[3]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "Thiamine HCl", "compound_id": 1207, "amount": 50, "unit": "mg", "g_l": 0.05,
    "mmol_l": 0.148236, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock composition,
    explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct
    receiving-medium concentration. Retain it only within the scoped stock and retain
    the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "ingredients[25].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock
    composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."},
    {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[25].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock
    composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]},
    {"quantity_id": "q27", "topic": "Riboflavin", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[2].recipe[4]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "Riboflavin", "compound_id": 136, "amount": 50, "unit": "mg", "g_l": 0.05, "mmol_l":
    0.132837, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Wolin''s vitamin solution (10x) stock composition, explicitly
    50 mg in its source recipe and provider g_l=0.05. It is not a direct receiving-medium
    concentration. Retain it only within the scoped stock and retain the separate1
    ml addition; no physical final-medium rate is inferred.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "ingredients[26].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock
    composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."},
    {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[26].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock
    composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]},
    {"quantity_id": "q28", "topic": "Nicotinic acid", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[2].recipe[5]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "Nicotinic acid", "compound_id": 139, "amount": 50, "unit": "mg", "g_l": 0.05,
    "mmol_l": 0.406141, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock composition,
    explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct
    receiving-medium concentration. Retain it only within the scoped stock and retain
    the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "ingredients[27].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock
    composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."},
    {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[27].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock
    composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]},
    {"quantity_id": "q29", "topic": "Calcium D-(+)-pantothenate", "source": [{"evidence_id":
    "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path":
    "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[2].recipe[6]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "Calcium D-(+)-pantothenate", "compound_id": 1512, "amount": 50, "unit": "mg",
    "g_l": 0.05, "mmol_l": 0.209846, "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock
    composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml",
    "field_path": "ingredients[28].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin''s vitamin
    solution (10x) stock composition, explicitly 50 mg in its source recipe and provider
    g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within
    the scoped stock and retain the separate1 ml addition; no physical final-medium
    rate is inferred."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml",
    "field_path": "ingredients[28].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Wolin''s vitamin
    solution (10x) stock composition, explicitly 50 mg in its source recipe and provider
    g_l=0.05. It is not a direct receiving-medium concentration. Retain it only within
    the scoped stock and retain the separate1 ml addition; no physical final-medium
    rate is inferred."}]}, {"quantity_id": "q30", "topic": "Vitamin B12", "source":
    [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[2].recipe[7]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\":
    1,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound":
    "Vitamin B12", "compound_id": 18, "amount": 1, "unit": "mg", "g_l": 0.001, "mmol_l":
    0.00073779, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Wolin''s vitamin solution (10x) stock composition, explicitly
    1 mg in its source recipe and provider g_l=0.001. It is not a direct receiving-medium
    concentration. Retain it only within the scoped stock and retain the separate1
    ml addition; no physical final-medium rate is inferred.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "ingredients[29].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock
    composition, explicitly 1 mg in its source recipe and provider g_l=0.001. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."},
    {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[29].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock
    composition, explicitly 1 mg in its source recipe and provider g_l=0.001. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]},
    {"quantity_id": "q31", "topic": "p-Aminobenzoic acid", "source": [{"evidence_id":
    "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path":
    "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[2].recipe[8]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound":
    "p-Aminobenzoic acid", "compound_id": 47, "amount": 50, "unit": "mg", "g_l": 0.05,
    "mmol_l": 0.364591, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock composition,
    explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct
    receiving-medium concentration. Retain it only within the scoped stock and retain
    the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "ingredients[30].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock
    composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."},
    {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[30].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock
    composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]},
    {"quantity_id": "q32", "topic": "(DL)-alpha-Lipoic acid", "source": [{"evidence_id":
    "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path":
    "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[2].recipe[9]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "(DL)-alpha-Lipoic acid", "compound_id": 252, "amount": 50, "unit": "mg", "g_l":
    0.05, "mmol_l": 0.24233, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock composition,
    explicitly 50 mg in its source recipe and provider g_l=0.05. It is not a direct
    receiving-medium concentration. Retain it only within the scoped stock and retain
    the separate1 ml addition; no physical final-medium rate is inferred.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "ingredients[31].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock
    composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."},
    {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ingredients[31].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Wolin''s vitamin solution (10x) stock
    composition, explicitly 50 mg in its source recipe and provider g_l=0.05. It is
    not a direct receiving-medium concentration. Retain it only within the scoped
    stock and retain the separate1 ml addition; no physical final-medium rate is inferred."}]},
    {"quantity_id": "q33", "topic": "main recipe: Trace element solution SL-10", "source":
    [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\":
    \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "solution":
    "Trace element solution SL-10", "solution_id": 595, "amount": 1, "unit": "ml",
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "add", "rationale":
    "Retain 1 ml as the source main recipe amount. This is a receiving stock dose
    or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium
    volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain 1 ml as the source main recipe amount. This is a receiving stock dose
    or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium
    volume.", "missing": true}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain 1 ml as the source main recipe amount. This is a receiving stock dose
    or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium
    volume.", "missing": true}]}, {"quantity_id": "q34", "topic": "main recipe: Wolin''s
    vitamin solution (10x)", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[0].recipe[12]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 13,\n                        \"solution\":
    \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 13, "solution": "Wolin''s vitamin solution (10x)", "solution_id":
    5980, "amount": 1, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "add", "rationale": "Retain 1 ml as the source main recipe amount.
    This is a receiving stock dose or solvent amount, not a G_PER_L ingredient or
    an asserted measured final-medium volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain 1 ml as the source main recipe amount. This is a receiving stock dose
    or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium
    volume.", "missing": true}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain 1 ml as the source main recipe amount. This is a receiving stock dose
    or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium
    volume.", "missing": true}]}, {"quantity_id": "q35", "topic": "main recipe: Distilled
    water", "source": [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[0].recipe[15]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 16, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "Retain 1000 ml
    as the source main recipe amount. This is a receiving stock dose or solvent amount,
    not a G_PER_L ingredient or an asserted measured final-medium volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "notes", "stored_value": "Source: DSMZ | Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium902.pdf",
    "decision": "add", "rationale": "Retain 1000 ml as the source main recipe amount.
    This is a receiving stock dose or solvent amount, not a G_PER_L ingredient or
    an asserted measured final-medium volume."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml",
    "field_path": "notes", "stored_value": "Source: DSMZ | Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium902.pdf",
    "decision": "add", "rationale": "Retain 1000 ml as the source main recipe amount.
    This is a receiving stock dose or solvent amount, not a G_PER_L ingredient or
    an asserted measured final-medium volume."}]}, {"quantity_id": "q36", "topic":
    "Trace element solution SL-10: Distilled water", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[1].recipe[9]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    990,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "Distilled water", "compound_id": 4, "amount": 990, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "Retain 990 ml
    as the source Trace element solution SL-10 amount. This is a receiving stock dose
    or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium
    volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain 990 ml as the source Trace element solution SL-10 amount. This is a receiving
    stock dose or solvent amount, not a G_PER_L ingredient or an asserted measured
    final-medium volume.", "missing": true}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain 990 ml as the source Trace element solution SL-10 amount. This is a receiving
    stock dose or solvent amount, not a G_PER_L ingredient or an asserted measured
    final-medium volume.", "missing": true}]}, {"quantity_id": "q37", "topic": "Wolin''s
    vitamin solution (10x): Distilled water", "source": [{"evidence_id": "api902",
    "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin",
    "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[2].recipe[10]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "Retain 1000 ml
    as the source Wolin''s vitamin solution (10x) amount. This is a receiving stock
    dose or solvent amount, not a G_PER_L ingredient or an asserted measured final-medium
    volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain 1000 ml as the source Wolin''s vitamin solution (10x) amount. This is
    a receiving stock dose or solvent amount, not a G_PER_L ingredient or an asserted
    measured final-medium volume.", "missing": true}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain 1000 ml as the source Wolin''s vitamin solution (10x) amount. This is
    a receiving stock dose or solvent amount, not a G_PER_L ingredient or an asserted
    measured final-medium volume.", "missing": true}]}, {"quantity_id": "q38", "topic":
    "Existing main preparation including every numeric condition", "source": [{"evidence_id":
    "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902", "raw_path":
    "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"step\": \"Dissolve ingredients except bicarbonate,
    pyruvate, vitamins and reducing agents, then adjust pH of solution to 7.0 with
    NaOH. Sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic, then dispense
    medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials
    and autoclave. Add pyruvate, vitamins, cysteine and sulfide from sterile anoxic
    stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic
    stock solution prepared under 80% N2 and 20% CO2 gas mixture. Vitamins should
    be sterilized by filtration. Adjust pH of complete medium to 7.0, if necessary.\"\n                    }",
    "exact_decoded_object": {"step": "Dissolve ingredients except bicarbonate, pyruvate,
    vitamins and reducing agents, then adjust pH of solution to 7.0 with NaOH. Sparge
    medium with 100% N2 gas for 30 - 45 min to make it anoxic, then dispense medium
    under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.
    Add pyruvate, vitamins, cysteine and sulfide from sterile anoxic stock solutions
    prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution
    prepared under 80% N2 and 20% CO2 gas mixture. Vitamins should be sterilized by
    filtration. Adjust pH of complete medium to 7.0, if necessary."}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}], "decision": "evidence_only", "rationale": "The complete main
    preparation is already retained, including pH7, N2 sparging30–45 min, stock atmospheres100%N2
    or80%N2/20%CO2 and vitamin filtration. Credit the current text; source does not
    supply autoclave time/temperature or all late-stock strengths/doses.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path":
    "preparation_steps[0]", "stored_value": {"step_number": 1, "action": "AUTOCLAVE",
    "description": "Dissolve ingredients except bicarbonate, pyruvate, vitamins and
    reducing agents, then adjust pH of solution to 7.0 with NaOH. Sparge medium with
    100% N2 gas for 30 - 45 min to make it anoxic, then dispense medium under same
    gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add
    pyruvate, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared
    under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared
    under 80% N2 and 20% CO2 gas mixture. Vitamins should be sterilized by filtration.
    Adjust pH of complete medium to 7.0, if necessary."}, "decision": "evidence_only",
    "rationale": "The complete main preparation is already retained, including pH7,
    N2 sparging30–45 min, stock atmospheres100%N2 or80%N2/20%CO2 and vitamin filtration.
    Credit the current text; source does not supply autoclave time/temperature or
    all late-stock strengths/doses."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml",
    "field_path": "preparation_steps[0]", "stored_value": {"step_number": 1, "action":
    "AUTOCLAVE", "description": "Dissolve ingredients except bicarbonate, pyruvate,
    vitamins and reducing agents, then adjust pH of solution to 7.0 with NaOH. Sparge
    medium with 100% N2 gas for 30 - 45 min to make it anoxic, then dispense medium
    under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.
    Add pyruvate, vitamins, cysteine and sulfide from sterile anoxic stock solutions
    prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution
    prepared under 80% N2 and 20% CO2 gas mixture. Vitamins should be sterilized by
    filtration. Adjust pH of complete medium to 7.0, if necessary."}, "decision":
    "evidence_only", "rationale": "The complete main preparation is already retained,
    including pH7, N2 sparging30–45 min, stock atmospheres100%N2 or80%N2/20%CO2 and
    vitamin filtration. Credit the current text; source does not supply autoclave
    time/temperature or all late-stock strengths/doses."}]}, {"quantity_id": "q39",
    "topic": "Existing SL-10 preparation including every numeric condition", "source":
    [{"evidence_id": "api902", "reference": "https://mediadive.dsmz.de/rest/medium/902",
    "raw_path": "REVIEW_WORK/batch060/source01-03/api902.bin", "raw_sha256": "85c547a542129a64c8c2cc17052faefe2a030190036e61693b706b1096fc97d8",
    "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T07:48:20.053969Z",
    "quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl,
    then dilute in water, add and dissolve the other salts. Finally make up to 1000.00
    ml.\"\n                    }", "exact_decoded_object": {"step": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally
    make up to 1000.00 ml."}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "The existing text correctly gives SL-10 final makeup1000 ml, but
    its root preparation placement lacks stock-stage scope. Keep the instruction on
    SL-10; it is not the receiving-medium final volume.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml", "field_path": "preparation_steps[1]",
    "stored_value": {"step_number": 2, "action": "DISSOLVE", "description": "First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally make up to 1000.00 ml."}, "decision": "correct", "rationale": "The existing
    text correctly gives SL-10 final makeup1000 ml, but its root preparation placement
    lacks stock-stage scope. Keep the instruction on SL-10; it is not the receiving-medium
    final volume."}, {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml",
    "field_path": "preparation_steps[1]", "stored_value": {"step_number": 2, "action":
    "DISSOLVE", "description": "First dissolve FeCl2 in the HCl, then dilute in water,
    add and dissolve the other salts. Finally make up to 1000.00 ml."}, "decision":
    "correct", "rationale": "The existing text correctly gives SL-10 final makeup1000
    ml, but its root preparation placement lacks stock-stage scope. Keep the instruction
    on SL-10; it is not the receiving-medium final volume."}]}, {"quantity_id": "q40",
    "topic": "Main pH7", "source": [{"evidence_id": "dsm902", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium902.pdf",
    "raw_path": "REVIEW_WORK/batch060/source01-03/dsm902.bin", "raw_sha256": "a4ea1524e87543e0671e6b7ec76f355f4355eea6e13fbb5b993e2bcc644cf735",
    "locator": "Page1 main preparation", "accessed_at": "2026-10-28T07:48:20.206078Z",
    "quote": "adjust pH of solution to 7.0 with NaOH."}], "decision": "evidence_only",
    "rationale": "Existing pH7 is explicitly supported; no strain-specific optimum
    inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARCBOXYDIBRACHIUM_MEDIUM.yaml",
    "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale":
    "Existing pH7 is explicitly supported; no strain-specific optimum inferred."},
    {"path": "data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml", "field_path":
    "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale": "Existing
    pH7 is explicitly supported; no strain-specific optimum inferred."}]}, {"quantity_id":
    "q41", "topic": "Late-stock strengths and addition volumes not specified", "source":
    [{"evidence_id": "dsm902", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium902.pdf",
    "raw_path": "REVIEW_WORK/batch060/source01-03/dsm902.bin", "raw_sha256": "a4ea1524e87543e0671e6b7ec76f355f4355eea6e13fbb5b993e2bcc644cf735",
    "locator": "Page1 main preparation", "accessed_at": "2026-10-28T07:48:20.206078Z",
    "quote": "Add pyruvate, vitamins, cysteine and\nsulfide from sterile anoxic stock
    solutions prepared under 100% N2 gas and bicarbonate\nfrom a sterile anoxic stock
    solution prepared under 80% N2 and 20% CO2 gas mixture."}], "decision": "unsupported",
    "rationale": "The source gives batch masses and specified SL-10/vitamin/resazurin
    additions, but not the strengths or addition volumes for the later pyruvate, cysteine,
    sulfide and bicarbonate stock preparations. Do not invent these missing quantities.",
    "layer_assessments": []}]'
- assessment_id: a4
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: concern
  summary: Every current ontology slot and current MIM row was checked. Sodium-resazurin
    and nickel supplied-form mismatches require correction. Calcium D-(+)-pantothenate
    is explicitly specified in the primary vitamin table and the current31345 object
    is stereospecified; broader biotin/B12/lipoic-acid identifiers do not justify
    choosing unreported stereoisomers or vitamers. Missing secondary slots alone are
    not wrong chemistry.
  target_ids:
  - CultureMech:002069
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
  - CultureMech:002069
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
  - CultureMech:002069
  evidence_ids:
  - local-target
- assessment_id: a7
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:002069
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-002069-separate-two-stock-compositions-from-the-receiving-medium
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Separate two stock compositions from the receiving medium
  description: Nineteen rows at ingredients[13]–[31] reproduce SL-10 and Wolin vitamin
    stock concentrations as direct ingredients. The primary source instead adds1 ml
    of each stock. Model both stock recipes and receiving doses, retain the main water1000
    ml context and all source stock solvents, and scope preparation_steps[1] to SL-10.
    Credit the 13 explicit API main rates; do not recompute final-medium totals using
    an unproven physical denominator.
  target_ids:
  - CultureMech:002069
  field_paths:
  - ingredients
  - solutions
  - preparation_steps[1]
  - notes
  evidence_ids:
  - dsm902
  - api902
  - quantities
  - writer-mediadive
  - writer-cleanup
  rule_id: P2.2-stock-scope
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-002069-resolve-supplied-sodium-and-nickel-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Resolve supplied sodium and nickel forms
  description: Sodium resazurin at ingredients[8] uses CHEBI:8806, whose current formula
    C12H7NO4 contains no sodium; copying that accession to another slot would not
    fix the supplied-form mismatch. Nickel chloride hexahydrate at ingredients[20]
    uses anhydrous CHEBI:34887 in both slots; current CHEBI:53542 explicitly represents
    the hexahydrate. The preferred NiCl2 x6H2O catalog row is REJECTED while an exact
    chemical-name synonym row is MAPPED; preserve both observations. Na2SiO3 remains
    ungrounded; the September standalone-solution suggestion is a lead, not authority
    to copy a term.
  target_ids:
  - CultureMech:002069
  field_paths:
  - ingredients[8].term
  - ingredients[20].term
  - ingredients[20].mediaingredientmech_chebi_term
  - ingredients[6].term
  evidence_ids:
  - dsm902
  - api902
  - grounding
  - historical-reader
  rule_id: P2.1-supplied-form
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-002069-attach-scoped-source-support-without-rewriting-history
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Attach scoped source support without rewriting history
  description: The current owner and generated target lack attached claim-level source
    evidence for their ingredient quantities and stock/preparation stages. The fresh
    API response can authenticate matching historical response bytes, but historical
    access events and September final-volume or mirror recommendations are not established
    by that match.
  target_ids:
  - CultureMech:002069
  field_paths:
  - ingredients
  - evidence
  - curation_history
  evidence_ids:
  - api902
  - dsm902
  - history
  - historical-reader
  rule_id: P3-evidence-placement
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Curate the maintained owner with separately scoped SL-10 and Wolin
    vitamin composition and1 ml receiving additions; preserve every source amount,
    supplied form, solvent and stage-specific preparation. Retain the provider-declared
    main g_l with its1002 ml metadata context and explicit primary final-volume limitation,
    then regenerate.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002069
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Verify an exact sodium-resazurin salt identifier and label before changing
    its primary grounding; do not add a neutral-resazurin mirror. Reconcile nickel
    hexahydrate with the verified53542 supplied form while preserving current catalog
    statuses. Resolve sodium silicate only from specific authoritative identity evidence.
    Retain all supported batch amounts.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002069
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Add claim-level quantity evidence and root evidence explicitly identifying
    each solution/preparation stage. Preserve existing history events byte-for-byte;
    append a new verified review/curation event rather than rewriting earlier timestamps
    or recommendations.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002069
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carcboxydibrachium_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- The primary902 PDF lists1000 ml main water and late stocks but does not explicitly
  state a final-medium volume. API1002 is provider-declared metadata, not a measured-final-volume
  instruction.
- Bare25% HCl lacks a stated percentage basis; provider stock g_l is retained as provider
  data, not independently converted from that label. Wolin vitamin water1000 ml likewise
  does not by itself prove a final makeup.
- Late pyruvate, cysteine, sulfide and bicarbonate stock strengths/addition volumes
  are not fully specified. No typical values or strain-level growth claims were inferred.
- An exact sodium-resazurin replacement accession and the ungrounded sodium-silicate
  identity remain unresolved. CHEBI:91245, captured as an exploratory lead, is copper(II)
  chloride pentahydrate and is not used as resazurin evidence.
- Historical raw-response equality authenticates bytes and literal claim objects,
  not historical execution, retrieval time or all recommendations. Standalone solution
  records mentioned in September were not newly inspected or adopted.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
