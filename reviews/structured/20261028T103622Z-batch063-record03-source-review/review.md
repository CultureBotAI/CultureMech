# CLOSTRIDIUM FORMICACETICUM medium: SL-4 and nominal-volume boundaries

- Review: 20261028T103622Z-batch063-record03-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T10:18:39.723721Z
- Finished UTC: 2026-10-28T10:36:22.604349Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated DSM14/KOMODO14 pair combines eight provider-declared main quantities with nine SL-4 stock constituents at stock strength. The stock receiving amount and percent-defined inputs are not represented. Main provider normalization is preserved as a declaration with unresolved final-volume basis. The DSM preparation is credited, the KOMODO aerobic flag conflicts with the source, and sodium-resazurin and nickel-hydrate mappings require correction.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch063 native selection index 03.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000969 | data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml | generated | clostridium_formicaceticum_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000969 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:000969 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:000969 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:000969 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Exact source aliases and contributors

identity: concern. Targets: CultureMech:000969.

The target derives from the exact DSM formicaceticum and KOMODO formicoaceticum contributors. Current DSM14/API14 agree on medium identity; the spelling difference is recorded as source identity, not silently corrected by biological inference. Historical KOMODO14 mapping exists but its current route remains inaccessible.

### Conditional solid form and preserved preparation

completeness: concern. Targets: CultureMech:000969.

Optional agar explicitly supports a solid branch, while the source also allows a broth branch; no unconditional species growth is inferred. Target and DSM owner retain main and SL-4 preparation plus pH 8.0. KOMODO lacks preparation and says Aerobic: Yes despite the source anoxic protocol. Stock context must not be flattened into an ordinary main ingredient list.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:000969.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "Yeast extract — declared main quantity", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.9456,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Yeast extract", "compound_id": 16, "amount": 5, "unit": "g", "g_l": 4.9456, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 3; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   Yeast extract                                           5.00         g"}], "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=4.9456 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "4.9456", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=4.9456 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "4.9456", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=4.9456 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "4.9456", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=4.9456 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion."}]}, {"quantity_id": "q2", "topic": "K2HPO4 — declared main quantity", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 9.8912,\n                        \"mmol_l\": 56.7885,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "K2HPO4", "compound_id": 10, "amount": 10, "unit": "g", "g_l": 9.8912, "mmol_l": 56.7885, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   K2HPO4                                                 10.00         g"}], "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=9.8912 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "9.8912", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=9.8912 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "9.8912", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=9.8912 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "9.8912", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=9.8912 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion."}]}, {"quantity_id": "q3", "topic": "Pyridoxine hydrochloride — declared main quantity", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00098912,\n                        \"mmol_l\": 0.00480996,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "Pyridoxine hydrochloride", "compound_id": 519, "attribute": "0.1% w/v", "amount": 1, "unit": "ml", "g_l": 0.00098912, "mmol_l": 0.00480996, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 6; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   Pyridoxine hydrochloride (0.1% w/v)                     1.00        ml"}], "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=0.00098912 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion. The source supplies a 0.1% w/v solution by volume; retain that stock strength and receiving amount rather than only its normalized solute value.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.00098912", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=0.00098912 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion. The source supplies a 0.1% w/v solution by volume; retain that stock strength and receiving amount rather than only its normalized solute value."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.00098912", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=0.00098912 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion. The source supplies a 0.1% w/v solution by volume; retain that stock strength and receiving amount rather than only its normalized solute value."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.00098912", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=0.00098912 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion. The source supplies a 0.1% w/v solution by volume; retain that stock strength and receiving amount rather than only its normalized solute value."}]}, {"quantity_id": "q4", "topic": "Na-thioglycolate — declared main quantity", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na-thioglycolate\",\n                        \"compound_id\": 30,\n                        \"amount\": 0.75,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.74184,\n                        \"mmol_l\": 6.50172,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "Na-thioglycolate", "compound_id": 30, "amount": 0.75, "unit": "g", "g_l": 0.74184, "mmol_l": 6.50172, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 7; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   Na-thioglycolate                                        0.75         g"}], "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=0.74184 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.74184", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=0.74184 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.74184", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=0.74184 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.74184", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=0.74184 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion."}]}, {"quantity_id": "q5", "topic": "Sodium resazurin — declared main quantity", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00049456,\n                        \"mmol_l\": 0.00196902,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "Sodium resazurin", "compound_id": 1852, "attribute": "0.1% w/v", "amount": 0.5, "unit": "ml", "g_l": 0.00049456, "mmol_l": 0.00196902, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 8; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   Sodium resazurin (0.1% w/v)                             0.50        ml"}], "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=0.00049456 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion. The source supplies a 0.1% w/v solution by volume; retain that stock strength and receiving amount rather than only its normalized solute value.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.00049456", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=0.00049456 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion. The source supplies a 0.1% w/v solution by volume; retain that stock strength and receiving amount rather than only its normalized solute value."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.00049456", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=0.00049456 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion. The source supplies a 0.1% w/v solution by volume; retain that stock strength and receiving amount rather than only its normalized solute value."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.00049456", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=0.00049456 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion. The source supplies a 0.1% w/v solution by volume; retain that stock strength and receiving amount rather than only its normalized solute value."}]}, {"quantity_id": "q6", "topic": "Na2CO3 — declared main quantity", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.98912,\n                        \"mmol_l\": 9.33237,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "Na2CO3", "compound_id": 32, "amount": 1, "unit": "g", "g_l": 0.98912, "mmol_l": 9.33237, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 9; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   Na2CO3                                                  1.00         g"}], "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=0.98912 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.98912", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=0.98912 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.98912", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=0.98912 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.98912", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=0.98912 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion."}]}, {"quantity_id": "q7", "topic": "D-Fructose — declared main quantity", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"D-Fructose\",\n                        \"compound_id\": 33,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.9456,\n                        \"mmol_l\": 27.4511,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "D-Fructose", "compound_id": 33, "amount": 5, "unit": "g", "g_l": 4.9456, "mmol_l": 27.4511, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 10; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   D-Fructose                                              5.00         g"}], "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=4.9456 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "4.9456", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=4.9456 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "4.9456", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=4.9456 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "4.9456", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=4.9456 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion."}]}, {"quantity_id": "q8", "topic": "Agar — declared main quantity", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"for solid medium\",\n                        \"attribute\": \"\",\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 14.8368,\n                        \"optional\": 1\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "Agar", "compound_id": 3, "condition": "for solid medium", "attribute": "", "amount": 15, "unit": "g", "g_l": 14.8368, "optional": 1}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 11; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   Agar, for solid medium (optional)                      15.00         g"}], "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=14.8368 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion. Agar is optional for the solid-medium branch; the quantity is not universal to broth.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "14.8368", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=14.8368 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion. Agar is optional for the solid-medium branch; the quantity is not universal to broth."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "14.8368", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=14.8368 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion. Agar is optional for the solid-medium branch; the quantity is not universal to broth."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "14.8368", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution g_l=14.8368 with nominal volume 1011 ml; the current local value matches that provider declaration. Primary batch amounts are independently preserved. Evidence-only credit is limited to the declared API basis, not a measured final concentration or water-derived conversion. Agar is optional for the solid-medium branch; the quantity is not universal to broth."}]}, {"quantity_id": "q9", "topic": "Na2-EDTA — SL-4 stock", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2-EDTA\",\n                        \"compound_id\": 34,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 1.48718,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Na2-EDTA", "compound_id": 34, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l": 1.48718, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 25; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   Na2-EDTA                                                0.50         g"}], "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.5. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.5. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.5. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.5. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}]}, {"quantity_id": "q10", "topic": "FeSO4 x 7 H2O — SL-4 stock", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.719386,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "FeSO4 x 7 H2O", "compound_id": 12, "amount": 0.2, "unit": "g", "g_l": 0.2, "mmol_l": 0.719386, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 26; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   FeSO4 x 7 H2O                                           0.20         g"}], "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.2. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.2. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.2. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.2. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}]}, {"quantity_id": "q11", "topic": "ZnSO4 x 7 H2O — SL-4 stock", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "ZnSO4 x 7 H2O", "compound_id": 35, "amount": 0.1, "unit": "g", "g_l": 0.1, "mmol_l": 0.347752, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 27; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   ZnSO4 x 7 H2O                                           0.10         g"}], "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.1. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.1. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.1. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.1. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}]}, {"quantity_id": "q12", "topic": "MnCl2 x 4 H2O — SL-4 stock", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[1].recipe[3]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.151588,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "MnCl2 x 4 H2O", "compound_id": 36, "amount": 0.03, "unit": "g", "g_l": 0.03, "mmol_l": 0.151588, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 28; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   MnCl2 x 4 H2O                                           0.03         g"}], "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.03. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.03. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.03. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.03. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}]}, {"quantity_id": "q13", "topic": "H3BO3 — SL-4 stock", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[1].recipe[4]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "H3BO3", "compound_id": 37, "amount": 0.3, "unit": "g", "g_l": 0.3, "mmol_l": 4.85123, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 29; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   H3BO3                                                   0.30         g"}], "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.3. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.3. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.3. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.3. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}]}, {"quantity_id": "q14", "topic": "CoCl2 x 6 H2O — SL-4 stock", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[1].recipe[5]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "CoCl2 x 6 H2O", "compound_id": 38, "amount": 0.2, "unit": "g", "g_l": 0.2, "mmol_l": 1.54037, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 30; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   CoCl2 x 6 H2O                                           0.20         g"}], "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.2. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.2. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.2. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.2. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}]}, {"quantity_id": "q15", "topic": "CuCl2 x 2 H2O — SL-4 stock", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0586569,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "CuCl2 x 2 H2O", "compound_id": 39, "amount": 0.01, "unit": "g", "g_l": 0.01, "mmol_l": 0.0586569, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 31; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   CuCl2 x 2 H2O                                           0.01         g"}], "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.01. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.01. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.01. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.01. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}]}, {"quantity_id": "q16", "topic": "NiCl2 x 6 H2O — SL-4 stock", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[1].recipe[7]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "NiCl2 x 6 H2O", "compound_id": 40, "amount": 0.02, "unit": "g", "g_l": 0.02, "mmol_l": 0.154322, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 32; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   NiCl2 x 6 H2O                                           0.02         g"}], "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.02. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.02. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.02. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.02. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}]}, {"quantity_id": "q17", "topic": "Na2MoO4 x 2 H2O — SL-4 stock", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[1].recipe[8]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.123993,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 0.03, "unit": "g", "g_l": 0.03, "mmol_l": 0.123993, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 33; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   Na2MoO4 x 2 H2O                                         0.03         g"}], "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.03. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.03. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.03. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection, whose API explicitly reports g_l=0.03. It is not a direct main-medium concentration. Preserve the source stock amount and separately restore the 10 ml batch addition; do not compute a final rate using an unresolved final volume."}]}, {"quantity_id": "q18", "topic": "Trace element solution SL-4 receiving input", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Trace element solution SL-4\",\n                        \"solution_id\": 20,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "solution": "Trace element solution SL-4", "solution_id": 20, "amount": 10, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 5; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   Trace element solution SL-4                            10.00        ml"}], "decision": "add", "rationale": "Represent this exact source solution amount and, where present, explicit 0.1% w/v strength. These source batch volumes do not become final-medium dosing rates merely because water is listed.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Represent this exact source solution amount and, where present, explicit 0.1% w/v strength. These source batch volumes do not become final-medium dosing rates merely because water is listed.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Represent this exact source solution amount and, where present, explicit 0.1% w/v strength. These source batch volumes do not become final-medium dosing rates merely because water is listed.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Represent this exact source solution amount and, where present, explicit 0.1% w/v strength. These source batch volumes do not become final-medium dosing rates merely because water is listed.", "missing": true}]}, {"quantity_id": "q19", "topic": "Pyridoxine hydrochloride receiving input", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00098912,\n                        \"mmol_l\": 0.00480996,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "Pyridoxine hydrochloride", "compound_id": 519, "attribute": "0.1% w/v", "amount": 1, "unit": "ml", "g_l": 0.00098912, "mmol_l": 0.00480996, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 6; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   Pyridoxine hydrochloride (0.1% w/v)                     1.00        ml"}], "decision": "add", "rationale": "Represent this exact source solution amount and, where present, explicit 0.1% w/v strength. These source batch volumes do not become final-medium dosing rates merely because water is listed.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Represent this exact source solution amount and, where present, explicit 0.1% w/v strength. These source batch volumes do not become final-medium dosing rates merely because water is listed.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Represent this exact source solution amount and, where present, explicit 0.1% w/v strength. These source batch volumes do not become final-medium dosing rates merely because water is listed.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Represent this exact source solution amount and, where present, explicit 0.1% w/v strength. These source batch volumes do not become final-medium dosing rates merely because water is listed.", "missing": true}]}, {"quantity_id": "q20", "topic": "Sodium resazurin receiving input", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00049456,\n                        \"mmol_l\": 0.00196902,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "Sodium resazurin", "compound_id": 1852, "attribute": "0.1% w/v", "amount": 0.5, "unit": "ml", "g_l": 0.00049456, "mmol_l": 0.00196902, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76", "locator": "PDF extracted line 8; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z", "quote": "   Sodium resazurin (0.1% w/v)                             0.50        ml"}], "decision": "add", "rationale": "Represent this exact source solution amount and, where present, explicit 0.1% w/v strength. These source batch volumes do not become final-medium dosing rates merely because water is listed.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Represent this exact source solution amount and, where present, explicit 0.1% w/v strength. These source batch volumes do not become final-medium dosing rates merely because water is listed.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Represent this exact source solution amount and, where present, explicit 0.1% w/v strength. These source batch volumes do not become final-medium dosing rates merely because water is listed.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Represent this exact source solution amount and, where present, explicit 0.1% w/v strength. These source batch volumes do not become final-medium dosing rates merely because water is listed.", "missing": true}]}, {"quantity_id": "q21", "topic": "Water scope 0", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the 1000 ml water input within Main sol. 14; neither the primary water line nor the API volume declaration establishes a measured final volume. Do not transfer stock water to the receiving medium.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "evidence", "stored_value": null, "decision": "add", "rationale": "Preserve the 1000 ml water input within Main sol. 14; neither the primary water line nor the API volume declaration establishes a measured final volume. Do not transfer stock water to the receiving medium.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "evidence", "stored_value": null, "decision": "add", "rationale": "Preserve the 1000 ml water input within Main sol. 14; neither the primary water line nor the API volume declaration establishes a measured final volume. Do not transfer stock water to the receiving medium.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "evidence", "stored_value": null, "decision": "add", "rationale": "Preserve the 1000 ml water input within Main sol. 14; neither the primary water line nor the API volume declaration establishes a measured final volume. Do not transfer stock water to the receiving medium.", "missing": true}]}, {"quantity_id": "q22", "topic": "Water scope 1", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[1].recipe[9]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the 1000 ml water input within Trace element solution SL-4; neither the primary water line nor the API volume declaration establishes a measured final volume. Do not transfer stock water to the receiving medium.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "evidence", "stored_value": null, "decision": "add", "rationale": "Preserve the 1000 ml water input within Trace element solution SL-4; neither the primary water line nor the API volume declaration establishes a measured final volume. Do not transfer stock water to the receiving medium.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "evidence", "stored_value": null, "decision": "add", "rationale": "Preserve the 1000 ml water input within Trace element solution SL-4; neither the primary water line nor the API volume declaration establishes a measured final volume. Do not transfer stock water to the receiving medium.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "evidence", "stored_value": null, "decision": "add", "rationale": "Preserve the 1000 ml water input within Trace element solution SL-4; neither the primary water line nor the API volume declaration establishes a measured final volume. Do not transfer stock water to the receiving medium.", "missing": true}]}, {"quantity_id": "q23", "topic": "Main preparation with late additions", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"step\": \"Dissolve ingredients (except carbonate and fructose) and sparge medium with 100% N2 gas for at least 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add fructose from a sterile anoxic stock solution prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Adjust pH of complete medium to 8.0.\"\n                    }", "exact_decoded_object": {"step": "Dissolve ingredients (except carbonate and fructose) and sparge medium with 100% N2 gas for at least 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add fructose from a sterile anoxic stock solution prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Adjust pH of complete medium to 8.0."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "The selected target and DSM owner retain the complete source paragraph. Add exact root evidence and keep it at this named stage; the KOMODO contributor lacks it. SL-4 pH 7.0 and 2 N NaOH belong to the stock, whereas pH 8.0 belongs to the complete medium. No NaOH addition volume is supplied.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "preparation_steps[0].description", "stored_value": "Dissolve ingredients (except carbonate and fructose) and sparge medium with 100% N2 gas for at least 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add fructose from a sterile anoxic stock solution prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Adjust pH of complete medium to 8.0.", "decision": "evidence_only", "rationale": "The selected target and DSM owner retain the complete source paragraph. Add exact root evidence and keep it at this named stage; the KOMODO contributor lacks it. SL-4 pH 7.0 and 2 N NaOH belong to the stock, whereas pH 8.0 belongs to the complete medium. No NaOH addition volume is supplied."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "preparation_steps[0].description", "stored_value": "Dissolve ingredients (except carbonate and fructose) and sparge medium with 100% N2 gas for at least 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add fructose from a sterile anoxic stock solution prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Adjust pH of complete medium to 8.0.", "decision": "evidence_only", "rationale": "The selected target and DSM owner retain the complete source paragraph. Add exact root evidence and keep it at this named stage; the KOMODO contributor lacks it. SL-4 pH 7.0 and 2 N NaOH belong to the stock, whereas pH 8.0 belongs to the complete medium. No NaOH addition volume is supplied."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "The selected target and DSM owner retain the complete source paragraph. Add exact root evidence and keep it at this named stage; the KOMODO contributor lacks it. SL-4 pH 7.0 and 2 N NaOH belong to the stock, whereas pH 8.0 belongs to the complete medium. No NaOH addition volume is supplied.", "missing": true}]}, {"quantity_id": "q24", "topic": "SL-4 preparation and pH adjustment", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"step\": \"First dissolve EDTA in distilled water and adjust pH to 7.0 using 2 N NaOH; then add other compounds.\"\n                    }", "exact_decoded_object": {"step": "First dissolve EDTA in distilled water and adjust pH to 7.0 using 2 N NaOH; then add other compounds."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "The selected target and DSM owner retain the complete source paragraph. Add exact root evidence and keep it at this named stage; the KOMODO contributor lacks it. SL-4 pH 7.0 and 2 N NaOH belong to the stock, whereas pH 8.0 belongs to the complete medium. No NaOH addition volume is supplied.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "preparation_steps[1].description", "stored_value": "First dissolve EDTA in distilled water and adjust pH to 7.0 using 2 N NaOH; then add other compounds.", "decision": "evidence_only", "rationale": "The selected target and DSM owner retain the complete source paragraph. Add exact root evidence and keep it at this named stage; the KOMODO contributor lacks it. SL-4 pH 7.0 and 2 N NaOH belong to the stock, whereas pH 8.0 belongs to the complete medium. No NaOH addition volume is supplied."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "preparation_steps[1].description", "stored_value": "First dissolve EDTA in distilled water and adjust pH to 7.0 using 2 N NaOH; then add other compounds.", "decision": "evidence_only", "rationale": "The selected target and DSM owner retain the complete source paragraph. Add exact root evidence and keep it at this named stage; the KOMODO contributor lacks it. SL-4 pH 7.0 and 2 N NaOH belong to the stock, whereas pH 8.0 belongs to the complete medium. No NaOH addition volume is supplied."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "The selected target and DSM owner retain the complete source paragraph. Add exact root evidence and keep it at this named stage; the KOMODO contributor lacks it. SL-4 pH 7.0 and 2 N NaOH belong to the stock, whereas pH 8.0 belongs to the complete medium. No NaOH addition volume is supplied.", "missing": true}]}, {"quantity_id": "q25", "topic": "Main pH", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"step\": \"Dissolve ingredients (except carbonate and fructose) and sparge medium with 100% N2 gas for at least 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add fructose from a sterile anoxic stock solution prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Adjust pH of complete medium to 8.0.\"\n                    }", "exact_decoded_object": {"step": "Dissolve ingredients (except carbonate and fructose) and sparge medium with 100% N2 gas for at least 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add fructose from a sterile anoxic stock solution prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Adjust pH of complete medium to 8.0."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The generic complete-medium pH 8.0 is explicitly supported; SL-4 pH 7.0 must not replace it.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path": "ph_value", "stored_value": 8.0, "decision": "evidence_only", "rationale": "The generic complete-medium pH 8.0 is explicitly supported; SL-4 pH 7.0 must not replace it."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml", "field_path": "ph_value", "stored_value": 8.0, "decision": "evidence_only", "rationale": "The generic complete-medium pH 8.0 is explicitly supported; SL-4 pH 7.0 must not replace it."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml", "field_path": "ph_value", "stored_value": 8.0, "decision": "evidence_only", "rationale": "The generic complete-medium pH 8.0 is explicitly supported; SL-4 pH 7.0 must not replace it."}]}, {"quantity_id": "q26", "topic": "Unresolved final volume and unquantified stock strengths", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Trace element solution SL-4\",\n                        \"solution_id\": 20,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "solution": "Trace element solution SL-4", "solution_id": 20, "amount": 10, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00098912,\n                        \"mmol_l\": 0.00480996,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "Pyridoxine hydrochloride", "compound_id": 519, "attribute": "0.1% w/v", "amount": 1, "unit": "ml", "g_l": 0.00098912, "mmol_l": 0.00480996, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00049456,\n                        \"mmol_l\": 0.00196902,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "Sodium resazurin", "compound_id": 1852, "attribute": "0.1% w/v", "amount": 0.5, "unit": "ml", "g_l": 0.00049456, "mmol_l": 0.00196902, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T10:19:16.990824Z", "quote": "{\n                        \"step\": \"Dissolve ingredients (except carbonate and fructose) and sparge medium with 100% N2 gas for at least 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add fructose from a sterile anoxic stock solution prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Adjust pH of complete medium to 8.0.\"\n                    }", "exact_decoded_object": {"step": "Dissolve ingredients (except carbonate and fructose) and sparge medium with 100% N2 gas for at least 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add fructose from a sterile anoxic stock solution prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Adjust pH of complete medium to 8.0."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "not_quantified", "rationale": "The listed liquid inputs total 1011.5 ml (1000 water+10 SL-4+1 pyridoxine+0.5 dye), whereas the API declares 1011 ml and normalizes g_l against it. Neither is an independently measured final volume, and the later carbonate/fructose stock strengths and addition volumes are unspecified. Retain the provider declaration and primary batch recipe as distinct evidence; do not automatically renormalize to either sum.", "layer_assessments": []}]

### Current ontology and MIM correspondence

grounding: concern. Targets: CultureMech:000969.

All existing CHEBI IDs resolve and current labels match. Source sodium-resazurin and nickel-hydrate identities still conflict with those valid terms. Current MIM preferred/synonym statuses are retained, including the REJECTED preferred nickel-hydrate row and MAPPED exact synonym; catalog membership is not historical validity. EDTA hydration and an absent yeast term remain unresolved.

### History and evidence scope

provenance: concern. Targets: CultureMech:000969.

Current source bytes, complete histories and scoped historical reports were read. Missing claim-level linkage and any malformed historical metadata are distinguished from authenticated source bytes; originals remain append-only.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:000969.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:000969.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Restore SL-4 and the percent-defined input stages

major / open / confirmed; issue key: culturemech-000969-restore-sl-4-and-the-percent-defined-input-stages.

Nine direct entries are SL-4 stock concentrations rather than main-medium quantities. The10 ml SL-4 addition and pyridoxine/resazurin solution strengths and doses are omitted. Keep eight exact main API g_l declarations qualified by their 1011 ml provider basis; the primary only lists water and liquid additions, which do not establish a final volume.

### f2: Reconcile the KOMODO atmosphere and retained DSM preparation

major / open / confirmed; issue key: culturemech-000969-reconcile-the-komodo-atmosphere-and-retained-dsm-preparation.

The current KOMODO contributor says Aerobic: Yes and lacks preparation, while DSM14 explicitly uses an anoxic protocol. Target and DSM owner already retain the main and stock paragraphs and pH 8.0. Credit that content; reconcile the contradictory contributor before regeneration under the current compatibility guard.

### f3: Resolve sodium resazurin and nickel supplied forms

major / open / confirmed; issue key: culturemech-000969-resolve-sodium-resazurin-and-nickel-supplied-forms.

CHEBI8806 denotes neutral Resazurin rather than the expressly supplied sodium salt. Both nickel slots use valid CHEBI34887 nickel dichloride although SL-4 specifies the hexahydrate; fresh OLS 53542 is nickel chloride hexahydrate. EDTA64734 additionally asserts anhydrous specificity not stated by the primary; that specificity remains unverified rather than a proved error.

### f4: Preserve and qualify historical event metadata

minor / open / confirmed; issue key: culturemech-000969-preserve-and-qualify-historical-event-metadata.

KOMODO import events contain a literal .fZ timestamp and resolver events omit a UTC offset. Historical concentration reports preserve unresolved claims and exact source mappings, but are not independent proof of those historical retrieval events. The current API authenticates the historical raw digest and exact source objects, not historical review execution or all stock conclusions. Current root references and claim-level links remain incomplete.

## Recommended Actions And Acceptance Checks

### action1

Restore the SL-4 stock composition and source receiving dose, and represent the percent-defined pyridoxine and sodium-resazurin inputs. Preserve primary batch amounts and the API-declared nominal rates as separate scoped evidence; resolve final-volume provenance before computing new final rates.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Qualify or correct the contradictory KOMODO source flag with exact primary evidence and retain the DSM preparation verbatim in its main/stock scope. Never infer a strain growth claim from the title or a table flag.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Verify the sodium-resazurin salt identifier before selecting a replacement, and reconcile nickel primary and secondary slots to the exact hydrated form with authority evidence. Keep the source stock amounts unchanged. Retain the unresolved EDTA hydration limit and all current MIM mapping-status distinctions.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action4

Retain every original event byte-for-byte. If authoritative provenance is recovered, append a verified correction or context event; never invent or overwrite its timestamp. Link fresh source evidence separately and preserve unresolved accession limitations.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-2 | data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| identity-search | REVIEW_WORK/batch063/record03/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _parse_api_solutions, _parse_preparation_steps | context_only | Current composition parser restricts ingredients to the primary solution, excludes solvent and recognized stock additions, and retains explicit g_l. The solution parser preserves referenced or percent-defined stocks and source attributes. Preparation parsing still concatenates all solution steps into root preparation_steps; source-stage annotation remains important. These present functions do not prove the historical execution that produced this record. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group copies a sole contributor with merge metadata. For multiple contributors it passes records to merge_formulation_evidence, which checks compatibility; it does not authorize merging different preparation assertions. |
| writer-formulation | src/culturemech/merge/formulation.py; formulation_content, merge_formulation_evidence | context_only | Current compatibility preserves scientific fields and list order and rejects unequal formulations; only specified provenance/evidence lists are unioned. It performs no concentration conversion or stock expansion and does not authenticate historical merges. |
| writer-cleanup | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients, merge_ingredient_group | context_only | Current cleanup groups identical normalized names, keeps the first entry as a base, flags differing concentrations and combines a warning note; it does not sum concentrations. It can still discard distinctions when names repeat, so source stage must be retained. Current behavior does not establish the historical cause of an existing discrepancy. |
| writer-resolver | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.merge_composition | context_only | Current merge_composition copies nonplaceholder ingredients and available solutions, ph_value when absent, physical_state and medium_type. It does not copy preparation_steps or ph_range; present behavior is not proof of historical execution. |
| writer-komodo | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current _convert_to_culturemech builds KOMODO identity, source mapping and aerobic notes from table flags and emits placeholder ingredients. It uses time.strftime with %f, which does not itself establish a valid fractional timestamp. Existing malformed events remain original evidence, not a license to rewrite history. |
| historical-1 | reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md; Exact selected-owner matching rows, if present, plus report purpose/method and validation claims only; all other pair-specific conclusions outside scope. | context_only | Historical source-duplicate report: only exact selected-owner rows, where present, and its stated signature method are in scope. Similarity does not prove complete preparation identity; no assertion about absent exact pairs is inferred. |
| historical-2 | reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/clostridium_formicoaceticum_medium.yaml.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Current independent capture exactly matches the cited old response digest; 22 historical literal/decoded objects join. Access-event provenance remains historical. |
| historical-3 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/clostridium_formicaceticum_medium.yaml.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Current independent capture exactly matches the cited old response digest; 22 historical literal/decoded objects join. Access-event provenance remains historical. |
| historical-4 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-5 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_formicaceticum_medium.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-6 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-reader | REVIEW_WORK/batch063/record03/historical-reader.json | context_only | Full exact-header historical texts and scoped large report, with literal/decoded current-source joins and explicit mismatches. Historical access events are not reauthenticated. |
| attached-evidence-joins | REVIEW_WORK/batch063/record03/attached-evidence-joins.json | context_only | Every existing attached evidence claim is preserved and compared to the exact freshly captured response. Matching snippets do not authenticate historical access times. |
| complete-source-rows | REVIEW_WORK/batch063/record03/complete-source-rows.json | context_only | Every source recipe row and preparation object, with exact raw substring and decoded JSON locator, kept in its own solution stage. No biological recommendation follows from provider equipment metadata. |
| dsm14 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf; Exact source identity and scoped formulation/preparation | supports | Complete primary DSM14 page and SL-4 subsection visually read. Water is an input, not an explicit final-volume instruction; optional agar, percent-defined pyridoxine/resazurin stocks and preparation stages remain separate. |
| api14 | https://mediadive.dsmz.de/rest/medium/14; Exact source identity and scoped formulation/preparation | supports | Complete current API14 medium and both solution objects read. Main volume is1011 ml, with exact reported g_l matching local values. This nominal declaration does not resolve all listed liquid inputs or late stock additions. |
| komodo14 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=14; Exact source identity and scoped formulation/preparation | unknown | Exact historical MediaInfo=14 route returned403; no current recipe/mapping body recovered. |
| komodoList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact source identity and scoped formulation/preparation | unknown | Exact historical MediaList route returned403. The old mapping row is historical derivative evidence. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53542; Exact source identity and scoped formulation/preparation | supports | Exact current OLS 53542 identifies nickel chloride hexahydrate, distinct from valid existing 34887 nickel dichloride. Current preferred/synonym MIM statuses remain separate. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30961; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86481 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86481; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_8806; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_29377; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi15824 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15824; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_2509; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi64734 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_64734; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86368; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86318; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch063/record03/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch063/record03/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch063/record03/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch063/record03/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch063/record03/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch063/record03/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch063/record03/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch063/record03/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch063/record03/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- The exact KOMODO14 accession and catalogue routes returned403; source identity authentication is partial. Historical mapping rows are not current catalogue responses.
- The API nominal1011 ml basis differs from the 1011.5 ml sum of listed liquid inputs. No measured final volume or automatic alternative normalization is asserted.
- Late carbonate/fructose stock strengths and addition volumes, and the SL-4 NaOH adjustment volume, are not quantified by the source.
- Optional agar defines a solid branch; this review does not turn it into an obligatory component for every use or infer species/strain growth.
- A sodium-resazurin replacement identifier and EDTA hydration are not guessed; current MIM rows do not establish historical mapping correctness.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T103622Z-batch063-record03-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'CLOSTRIDIUM FORMICACETICUM medium: SL-4 and nominal-volume boundaries'
started_at: '2026-10-28T10:18:39.723721Z'
finished_at: '2026-10-28T10:36:22.604349Z'
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
summary: The generated DSM14/KOMODO14 pair combines eight provider-declared main quantities
  with nine SL-4 stock constituents at stock strength. The stock receiving amount
  and percent-defined inputs are not represented. Main provider normalization is preserved
  as a declaration with unresolved final-volume basis. The DSM preparation is credited,
  the KOMODO aerobic flag conflicts with the source, and sodium-resazurin and nickel-hydrate
  mappings require correction.
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
  - path: data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml
    sha256: 679f270aa91b610f19f69f2352c3e5fe2c7a6f95001116e5543b64395d544a4c
    role: target
  - path: data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml
    sha256: b68237fa06f2e0680c8620f4deb01071cac7e5247bda9fc272da32fcc96e3691
    role: context
  - path: data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml
    sha256: 0ccaba36e25ddb1c62fcacdc4ea6e024b2c10f3dfac29a76fd6e0f5e5c4d1d9d
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/clostridium_formicoaceticum_medium.yaml.md
    sha256: 006d0910c98eceb5050e4e6810ee3fed5ad2d6141be891e954eafccb054b45df
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/clostridium_formicaceticum_medium.yaml.md
    sha256: 853f8c5a844e1e70e644a3c51f82bd178db3ce47177d3840163ec91bb4b79c6c
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.md
    sha256: 3e91c12944c7945498ed8e153cb261d9c51a8ac82a0c748d0830806987bd6190
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_formicaceticum_medium.md
    sha256: 336017af7109b9aa297a222ada98b2edc8bcbdbebc81a33e90968ac7a8504c00
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.md
    sha256: ca0028b8a087e68a89dd35e7cde5348a1736625c20f5b4c3097b9c844881c115
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
  selection: Actual batch063 native selection index 03.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000969
targets:
- target_id: CultureMech:000969
  path: data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml
  label: clostridium_formicaceticum_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:000969
  command: just validate-schema data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml
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
  - CultureMech:000969
  command: just validate-strict data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml
    --out REVIEW_WORK/batch063/record03/strict.tsv --workers 1 --quiet
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
  - CultureMech:000969
  command: just validate-terms data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml
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
  - CultureMech:000969
  command: just validate-references data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T10:27:48.303427Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 679f270aa91b610f19f69f2352c3e5fe2c7a6f95001116e5543b64395d544a4c
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T10:27:48.303427Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: b68237fa06f2e0680c8620f4deb01071cac7e5247bda9fc272da32fcc96e3691
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T10:27:48.303427Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 0ccaba36e25ddb1c62fcacdc4ea6e024b2c10f3dfac29a76fd6e0f5e5c4d1d9d
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch063/record03/identity-search.json
  accessed_at: '2026-10-28T10:27:48.354853Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems and stable identity resolve the owner;
    excluded namesakes are retained in the census. Similar names and source accessions
    are not promoted to owners.
  snapshot_sha256: 000ba22f295536aeb767a7763849ce395cfc91c93d5ecf0dd1f78678be131a3d
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _parse_api_solutions, _parse_preparation_steps
  accessed_at: '2026-10-28T10:27:48.303427Z'
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
  accessed_at: '2026-10-28T10:27:48.303427Z'
  support: context_only
  summary: Current merge_group copies a sole contributor with merge metadata. For
    multiple contributors it passes records to merge_formulation_evidence, which checks
    compatibility; it does not authorize merging different preparation assertions.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content, merge_formulation_evidence
  accessed_at: '2026-10-28T10:27:48.303427Z'
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
  accessed_at: '2026-10-28T10:27:48.303427Z'
  support: context_only
  summary: Current cleanup groups identical normalized names, keeps the first entry
    as a base, flags differing concentrations and combines a warning note; it does
    not sum concentrations. It can still discard distinctions when names repeat, so
    source stage must be retained. Current behavior does not establish the historical
    cause of an existing discrepancy.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer-resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.merge_composition
  accessed_at: '2026-10-28T10:27:48.303427Z'
  support: context_only
  summary: Current merge_composition copies nonplaceholder ingredients and available
    solutions, ph_value when absent, physical_state and medium_type. It does not copy
    preparation_steps or ph_range; present behavior is not proof of historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-komodo
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T10:27:48.303427Z'
  support: context_only
  summary: Current _convert_to_culturemech builds KOMODO identity, source mapping
    and aerobic notes from table flags and emits placeholder ingredients. It uses
    time.strftime with %f, which does not itself establish a valid fractional timestamp.
    Existing malformed events remain original evidence, not a license to rewrite history.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: historical-1
  kind: record_content
  reference: reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md
  locator: Exact selected-owner matching rows, if present, plus report purpose/method
    and validation claims only; all other pair-specific conclusions outside scope.
  accessed_at: '2026-10-28T10:27:48.303427Z'
  support: context_only
  summary: 'Historical source-duplicate report: only exact selected-owner rows, where
    present, and its stated signature method are in scope. Similarity does not prove
    complete preparation identity; no assertion about absent exact pairs is inferred.'
  snapshot_sha256: a723d4b7950bf4ac296a8a7fe4890d4d0881199a5d17c12a5fe39c2afbc40a10
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/clostridium_formicoaceticum_medium.yaml.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T10:27:48.303427Z'
  support: context_only
  summary: Current independent capture exactly matches the cited old response digest;
    22 historical literal/decoded objects join. Access-event provenance remains historical.
  snapshot_sha256: 006d0910c98eceb5050e4e6810ee3fed5ad2d6141be891e954eafccb054b45df
- evidence_id: historical-3
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/clostridium_formicaceticum_medium.yaml.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T10:27:48.303427Z'
  support: context_only
  summary: Current independent capture exactly matches the cited old response digest;
    22 historical literal/decoded objects join. Access-event provenance remains historical.
  snapshot_sha256: 853f8c5a844e1e70e644a3c51f82bd178db3ce47177d3840163ec91bb4b79c6c
- evidence_id: historical-4
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T10:27:48.303427Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: 3e91c12944c7945498ed8e153cb261d9c51a8ac82a0c748d0830806987bd6190
- evidence_id: historical-5
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_formicaceticum_medium.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T10:27:48.303427Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: 336017af7109b9aa297a222ada98b2edc8bcbdbebc81a33e90968ac7a8504c00
- evidence_id: historical-6
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T10:27:48.303427Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: ca0028b8a087e68a89dd35e7cde5348a1736625c20f5b4c3097b9c844881c115
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch063/record03/historical-reader.json
  accessed_at: '2026-10-28T10:27:48.358039Z'
  support: context_only
  summary: Full exact-header historical texts and scoped large report, with literal/decoded
    current-source joins and explicit mismatches. Historical access events are not
    reauthenticated.
  snapshot_sha256: 2cb2014eb30ef043bc8099bc9290b80c8edf53797689e9a18a9e69c8442cb639
- evidence_id: attached-evidence-joins
  kind: record_content
  reference: REVIEW_WORK/batch063/record03/attached-evidence-joins.json
  accessed_at: '2026-10-28T10:27:48.358339Z'
  support: context_only
  summary: Every existing attached evidence claim is preserved and compared to the
    exact freshly captured response. Matching snippets do not authenticate historical
    access times.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: complete-source-rows
  kind: record_content
  reference: REVIEW_WORK/batch063/record03/complete-source-rows.json
  accessed_at: '2026-10-28T10:27:48.360707Z'
  support: context_only
  summary: Every source recipe row and preparation object, with exact raw substring
    and decoded JSON locator, kept in its own solution stage. No biological recommendation
    follows from provider equipment metadata.
  snapshot_sha256: f8e3ae534369490a40f0be67018e4b58ef1db712ebf8bfe979879d74fbefa18a
- evidence_id: dsm14
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:19:17.249385Z'
  support: supports
  summary: Complete primary DSM14 page and SL-4 subsection visually read. Water is
    an input, not an explicit final-volume instruction; optional agar, percent-defined
    pyridoxine/resazurin stocks and preparation stages remain separate.
  snapshot_sha256: ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76
- evidence_id: api14
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/14
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:19:16.990824Z'
  support: supports
  summary: Complete current API14 medium and both solution objects read. Main volume
    is1011 ml, with exact reported g_l matching local values. This nominal declaration
    does not resolve all listed liquid inputs or late stock additions.
  snapshot_sha256: eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144
- evidence_id: komodo14
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=14
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:19:16.392851Z'
  support: unknown
  summary: Exact historical MediaInfo=14 route returned403; no current recipe/mapping
    body recovered.
  snapshot_sha256: 6cf4e0e4274e841cbdb70dcd7ce664573cb2351e6772bc40388c82b42925ed51
- evidence_id: komodoList
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:19:16.392827Z'
  support: unknown
  summary: Exact historical MediaList route returned403. The old mapping row is historical
    derivative evidence.
  snapshot_sha256: f131cc2773375f470395ba0d7679083e86252b979a38be9f63eaef76965df8e8
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53542
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:19:20.291953Z'
  support: supports
  summary: Exact current OLS 53542 identifies nickel chloride hexahydrate, distinct
    from valid existing 34887 nickel dichloride. Current preferred/synonym MIM statuses
    remain separate.
  snapshot_sha256: 1e444345efd33c02d5050deadd66637cc6dae004c55e6962c62abd172291e526
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:19:17.865139Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 97e9c2b05f3937c5beeebb4e6338aa6730f9e422ee0e7570a6c622dda8d97a86
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30961
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:19:18.990985Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 491af523ba70d13857fcb828561d0556e46382fa0591011a06693d7db24ad91f
- evidence_id: chebi86481
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86481
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:19:21.748162Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 88d3050aa8a8b2a37f9a6dfb1e0b52205ab107e3a273ba3c41eb61b80b699f9f
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_8806
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:19:22.081630Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: ceb05e9dd7fba3802d28b34c50bbb604ded87951e4ea3a812739824a84648d72
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_29377
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:19:18.708962Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: dee64859233d0b0898eba91901a001f1faaa5eaab37f7beb7e98318ab8c19569
- evidence_id: chebi15824
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15824
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:19:17.875264Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b2b7977e757934e4020df969971731a0cbbce496fe56860a87dd15f210ff34c9
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_2509
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:19:18.478804Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 348b20478bba221cc21e285237104281145111be6ea3aa30d381d6eae19c0a90
- evidence_id: chebi64734
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_64734
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:19:20.855282Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 169db4b78f8f464430da6982919f8d425063268fbd374b9e7653a8d7aed041d9
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:19:21.100671Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: e12b865122aab78645385260e1e83ff28f3c45365cb67c9181166628f68974b3
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:19:19.531971Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 6bf1390236046f1cb7b21e2fc324fccba6e6eac2bc4e519f12d998f0edce671b
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86368
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:19:21.748115Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2bb4588e6734285b5536bdac78701f9800fdb8d17236d12cf5a1c30490f1614d
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:19:19.597368Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f23e1405347fa9d8a0826d4dd1279b7cdec8361390d20e439154dcbbd386a2d4
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:19:20.122410Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 31dc996638b0cc1341ed24fcb38ec344af726c99d376ac94e952210fcb9ed583
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86318
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:19:21.530390Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 8ba4e0a242571ae9a62ca7ba5c0f4af765962a02f5119a96d47dda9df7c9d593
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:19:19.750236Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a43b8268f70ae50c4cfbc53e12bbd195618c521619cfab8f71d3704b338af95b
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:19:20.922572Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0271a149a298ff837ad8f690ce8cb0acf111f5d25c5efaf6fa828401ab951d56
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch063/record03/quantity-inventory.json
  accessed_at: '2026-10-28T10:27:48.393239Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 43a92fa4a0b7479b2efb66c16e95cedcca47aee8ea85411aef277cd52eebf769
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch063/record03/grounding-inventory.json
  accessed_at: '2026-10-28T10:27:48.393306Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: 03eb692d5898efd18eb7d867fdb184fec1d6285dbb67fc27060d740e9a67dde9
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch063/record03/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T10:27:48.393564Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 610d50992d9d3cbff7fcb6ebf943a041cc7a7e30a144d3e7dcdc179ab726d856
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch063/record03/scalar-census.json
  accessed_at: '2026-10-28T10:27:48.393586Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: e0c3122630e3f0f9b44dd3e57bbfadf26423c6dca8d79ea84300dc2d00632683
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch063/record03/validate-schema.json
  accessed_at: '2026-10-28T10:18:40.819493Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: 74dcb441efd15790d4c591f8c7021604117cf86927114a3e2019ea7520e5507f
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch063/record03/validate-strict.json
  accessed_at: '2026-10-28T10:18:41.804038Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch063/record03/strict.tsv\n"
  snapshot_sha256: b444046d054949de217ef9b905cc278bef5bf0623f7e18713d64f7e583c698c9
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch063/record03/validate-terms.json
  accessed_at: '2026-10-28T10:18:42.874956Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: b95c10d85ff0f408467dd7087ce8307b5532e29b60b1087fdb5a261412fc0469
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch063/record03/validate-references.json
  accessed_at: '2026-10-28T10:18:43.613115Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: c2bd986b9aceacdce027f9c7c58d17227aa8a6f95978cff3fad3af42d20dc4ab
assessments:
- assessment_id: a1
  area: identity
  topic: Exact source aliases and contributors
  outcome: concern
  summary: The target derives from the exact DSM formicaceticum and KOMODO formicoaceticum
    contributors. Current DSM14/API14 agree on medium identity; the spelling difference
    is recorded as source identity, not silently corrected by biological inference.
    Historical KOMODO14 mapping exists but its current route remains inaccessible.
  target_ids:
  - CultureMech:000969
  evidence_ids:
  - identity-search
  - dsm14
  - api14
  - historical-reader
  - komodo14
- assessment_id: a2
  area: completeness
  topic: Conditional solid form and preserved preparation
  outcome: concern
  summary: 'Optional agar explicitly supports a solid branch, while the source also
    allows a broth branch; no unconditional species growth is inferred. Target and
    DSM owner retain main and SL-4 preparation plus pH 8.0. KOMODO lacks preparation
    and says Aerobic: Yes despite the source anoxic protocol. Stock context must not
    be flattened into an ordinary main ingredient list.'
  target_ids:
  - CultureMech:000969
  evidence_ids:
  - local-target
  - owner-1
  - owner-2
  - dsm14
  - api14
- assessment_id: a3
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:000969
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "Yeast extract — declared main quantity",
    "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\":
    5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    4.9456,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 1, "compound": "Yeast extract", "compound_id": 16, "amount":
    5, "unit": "g", "g_l": 4.9456, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 3; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   Yeast extract                                           5.00         g"}],
    "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution
    g_l=4.9456 with nominal volume 1011 ml; the current local value matches that provider
    declaration. Primary batch amounts are independently preserved. Evidence-only
    credit is limited to the declared API basis, not a measured final concentration
    or water-derived conversion.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "4.9456",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=4.9456 with nominal volume 1011 ml; the current local
    value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "4.9456",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=4.9456 with nominal volume 1011 ml; the current local
    value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "4.9456",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=4.9456 with nominal volume 1011 ml; the current local
    value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion."}]}, {"quantity_id": "q2", "topic":
    "K2HPO4 — declared main quantity", "source": [{"evidence_id": "api14", "reference":
    "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin",
    "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\":
    10,\n                        \"unit\": \"g\",\n                        \"g_l\":
    9.8912,\n                        \"mmol_l\": 56.7885,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "K2HPO4", "compound_id": 10, "amount": 10, "unit": "g", "g_l": 9.8912, "mmol_l":
    56.7885, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   K2HPO4                                                 10.00         g"}],
    "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution
    g_l=9.8912 with nominal volume 1011 ml; the current local value matches that provider
    declaration. Primary batch amounts are independently preserved. Evidence-only
    credit is limited to the declared API basis, not a measured final concentration
    or water-derived conversion.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "9.8912",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=9.8912 with nominal volume 1011 ml; the current local
    value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "9.8912",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=9.8912 with nominal volume 1011 ml; the current local
    value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "9.8912",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=9.8912 with nominal volume 1011 ml; the current local
    value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion."}]}, {"quantity_id": "q3", "topic":
    "Pyridoxine hydrochloride — declared main quantity", "source": [{"evidence_id":
    "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path":
    "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"attribute\":
    \"0.1% w/v\",\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.00098912,\n                        \"mmol_l\":
    0.00480996,\n                        \"optional\": 0\n                    }",
    "exact_decoded_object": {"recipe_order": 4, "compound": "Pyridoxine hydrochloride",
    "compound_id": 519, "attribute": "0.1% w/v", "amount": 1, "unit": "ml", "g_l":
    0.00098912, "mmol_l": 0.00480996, "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."},
    {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 6; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   Pyridoxine hydrochloride (0.1% w/v)                     1.00        ml"}],
    "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution
    g_l=0.00098912 with nominal volume 1011 ml; the current local value matches that
    provider declaration. Primary batch amounts are independently preserved. Evidence-only
    credit is limited to the declared API basis, not a measured final concentration
    or water-derived conversion. The source supplies a 0.1% w/v solution by volume;
    retain that stock strength and receiving amount rather than only its normalized
    solute value.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.00098912",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=0.00098912 with nominal volume 1011 ml; the current
    local value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion. The source supplies a 0.1% w/v
    solution by volume; retain that stock strength and receiving amount rather than
    only its normalized solute value."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.00098912",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=0.00098912 with nominal volume 1011 ml; the current
    local value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion. The source supplies a 0.1% w/v
    solution by volume; retain that stock strength and receiving amount rather than
    only its normalized solute value."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.00098912",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=0.00098912 with nominal volume 1011 ml; the current
    local value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion. The source supplies a 0.1% w/v
    solution by volume; retain that stock strength and receiving amount rather than
    only its normalized solute value."}]}, {"quantity_id": "q4", "topic": "Na-thioglycolate
    — declared main quantity", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Na-thioglycolate\",\n                        \"compound_id\": 30,\n                        \"amount\":
    0.75,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.74184,\n                        \"mmol_l\": 6.50172,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "Na-thioglycolate", "compound_id": 30, "amount": 0.75, "unit": "g", "g_l": 0.74184,
    "mmol_l": 6.50172, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 7; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   Na-thioglycolate                                        0.75         g"}],
    "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution
    g_l=0.74184 with nominal volume 1011 ml; the current local value matches that
    provider declaration. Primary batch amounts are independently preserved. Evidence-only
    credit is limited to the declared API basis, not a measured final concentration
    or water-derived conversion.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.74184",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=0.74184 with nominal volume 1011 ml; the current local
    value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.74184",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=0.74184 with nominal volume 1011 ml; the current local
    value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.74184",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=0.74184 with nominal volume 1011 ml; the current local
    value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion."}]}, {"quantity_id": "q5", "topic":
    "Sodium resazurin — declared main quantity", "source": [{"evidence_id": "api14",
    "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin",
    "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\":
    \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.00049456,\n                        \"mmol_l\":
    0.00196902,\n                        \"optional\": 0\n                    }",
    "exact_decoded_object": {"recipe_order": 6, "compound": "Sodium resazurin", "compound_id":
    1852, "attribute": "0.1% w/v", "amount": 0.5, "unit": "ml", "g_l": 0.00049456,
    "mmol_l": 0.00196902, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 8; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   Sodium resazurin (0.1% w/v)                             0.50        ml"}],
    "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution
    g_l=0.00049456 with nominal volume 1011 ml; the current local value matches that
    provider declaration. Primary batch amounts are independently preserved. Evidence-only
    credit is limited to the declared API basis, not a measured final concentration
    or water-derived conversion. The source supplies a 0.1% w/v solution by volume;
    retain that stock strength and receiving amount rather than only its normalized
    solute value.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.00049456",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=0.00049456 with nominal volume 1011 ml; the current
    local value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion. The source supplies a 0.1% w/v
    solution by volume; retain that stock strength and receiving amount rather than
    only its normalized solute value."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.00049456",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=0.00049456 with nominal volume 1011 ml; the current
    local value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion. The source supplies a 0.1% w/v
    solution by volume; retain that stock strength and receiving amount rather than
    only its normalized solute value."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.00049456",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=0.00049456 with nominal volume 1011 ml; the current
    local value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion. The source supplies a 0.1% w/v
    solution by volume; retain that stock strength and receiving amount rather than
    only its normalized solute value."}]}, {"quantity_id": "q6", "topic": "Na2CO3
    — declared main quantity", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.98912,\n                        \"mmol_l\": 9.33237,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "Na2CO3", "compound_id": 32, "amount": 1, "unit": "g", "g_l": 0.98912, "mmol_l":
    9.33237, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 9; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   Na2CO3                                                  1.00         g"}],
    "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution
    g_l=0.98912 with nominal volume 1011 ml; the current local value matches that
    provider declaration. Primary batch amounts are independently preserved. Evidence-only
    credit is limited to the declared API basis, not a measured final concentration
    or water-derived conversion.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.98912",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=0.98912 with nominal volume 1011 ml; the current local
    value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.98912",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=0.98912 with nominal volume 1011 ml; the current local
    value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.98912",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=0.98912 with nominal volume 1011 ml; the current local
    value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion."}]}, {"quantity_id": "q7", "topic":
    "D-Fructose — declared main quantity", "source": [{"evidence_id": "api14", "reference":
    "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin",
    "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"D-Fructose\",\n                        \"compound_id\": 33,\n                        \"amount\":
    5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    4.9456,\n                        \"mmol_l\": 27.4511,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound":
    "D-Fructose", "compound_id": 33, "amount": 5, "unit": "g", "g_l": 4.9456, "mmol_l":
    27.4511, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 10; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   D-Fructose                                              5.00         g"}],
    "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution
    g_l=4.9456 with nominal volume 1011 ml; the current local value matches that provider
    declaration. Primary batch amounts are independently preserved. Evidence-only
    credit is limited to the declared API basis, not a measured final concentration
    or water-derived conversion.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "4.9456",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=4.9456 with nominal volume 1011 ml; the current local
    value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "4.9456",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=4.9456 with nominal volume 1011 ml; the current local
    value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "4.9456",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=4.9456 with nominal volume 1011 ml; the current local
    value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion."}]}, {"quantity_id": "q8", "topic":
    "Agar — declared main quantity", "source": [{"evidence_id": "api14", "reference":
    "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin",
    "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\":
    \"for solid medium\",\n                        \"attribute\": \"\",\n                        \"amount\":
    15,\n                        \"unit\": \"g\",\n                        \"g_l\":
    14.8368,\n                        \"optional\": 1\n                    }", "exact_decoded_object":
    {"recipe_order": 9, "compound": "Agar", "compound_id": 3, "condition": "for solid
    medium", "attribute": "", "amount": 15, "unit": "g", "g_l": 14.8368, "optional":
    1}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 11; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   Agar, for solid medium (optional)                      15.00         g"}],
    "decision": "evidence_only", "rationale": "API14 explicitly declares main-solution
    g_l=14.8368 with nominal volume 1011 ml; the current local value matches that
    provider declaration. Primary batch amounts are independently preserved. Evidence-only
    credit is limited to the declared API basis, not a measured final concentration
    or water-derived conversion. Agar is optional for the solid-medium branch; the
    quantity is not universal to broth.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "14.8368",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=14.8368 with nominal volume 1011 ml; the current local
    value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion. Agar is optional for the solid-medium
    branch; the quantity is not universal to broth."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "14.8368",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=14.8368 with nominal volume 1011 ml; the current local
    value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion. Agar is optional for the solid-medium
    branch; the quantity is not universal to broth."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "14.8368",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "API14 explicitly
    declares main-solution g_l=14.8368 with nominal volume 1011 ml; the current local
    value matches that provider declaration. Primary batch amounts are independently
    preserved. Evidence-only credit is limited to the declared API basis, not a measured
    final concentration or water-derived conversion. Agar is optional for the solid-medium
    branch; the quantity is not universal to broth."}]}, {"quantity_id": "q9", "topic":
    "Na2-EDTA — SL-4 stock", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Na2-EDTA\",\n                        \"compound_id\": 34,\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.5,\n                        \"mmol_l\": 1.48718,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Na2-EDTA", "compound_id": 34, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l":
    1.48718, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 25; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   Na2-EDTA                                                0.50         g"}],
    "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection,
    whose API explicitly reports g_l=0.5. It is not a direct main-medium concentration.
    Preserve the source stock amount and separately restore the 10 ml batch addition;
    do not compute a final rate using an unresolved final volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path":
    "ingredients[8].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection,
    whose API explicitly reports g_l=0.5. It is not a direct main-medium concentration.
    Preserve the source stock amount and separately restore the 10 ml batch addition;
    do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs
    to the SL-4 stock subsection, whose API explicitly reports g_l=0.5. It is not
    a direct main-medium concentration. Preserve the source stock amount and separately
    restore the 10 ml batch addition; do not compute a final rate using an unresolved
    final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs
    to the SL-4 stock subsection, whose API explicitly reports g_l=0.5. It is not
    a direct main-medium concentration. Preserve the source stock amount and separately
    restore the 10 ml batch addition; do not compute a final rate using an unresolved
    final volume."}]}, {"quantity_id": "q10", "topic": "FeSO4 x 7 H2O — SL-4 stock",
    "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\":
    0.2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.2,\n                        \"mmol_l\": 0.719386,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "FeSO4 x 7 H2O", "compound_id": 12, "amount": 0.2, "unit": "g", "g_l": 0.2, "mmol_l":
    0.719386, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 26; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   FeSO4 x 7 H2O                                           0.20         g"}],
    "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection,
    whose API explicitly reports g_l=0.2. It is not a direct main-medium concentration.
    Preserve the source stock amount and separately restore the 10 ml batch addition;
    do not compute a final rate using an unresolved final volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path":
    "ingredients[9].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection,
    whose API explicitly reports g_l=0.2. It is not a direct main-medium concentration.
    Preserve the source stock amount and separately restore the 10 ml batch addition;
    do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.2",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs
    to the SL-4 stock subsection, whose API explicitly reports g_l=0.2. It is not
    a direct main-medium concentration. Preserve the source stock amount and separately
    restore the 10 ml batch addition; do not compute a final rate using an unresolved
    final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.2",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs
    to the SL-4 stock subsection, whose API explicitly reports g_l=0.2. It is not
    a direct main-medium concentration. Preserve the source stock amount and separately
    restore the 10 ml batch addition; do not compute a final rate using an unresolved
    final volume."}]}, {"quantity_id": "q11", "topic": "ZnSO4 x 7 H2O — SL-4 stock",
    "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\":
    0.1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "ZnSO4 x 7 H2O", "compound_id": 35, "amount": 0.1, "unit": "g", "g_l": 0.1, "mmol_l":
    0.347752, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 27; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   ZnSO4 x 7 H2O                                           0.10         g"}],
    "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection,
    whose API explicitly reports g_l=0.1. It is not a direct main-medium concentration.
    Preserve the source stock amount and separately restore the 10 ml batch addition;
    do not compute a final rate using an unresolved final volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path":
    "ingredients[10].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection,
    whose API explicitly reports g_l=0.1. It is not a direct main-medium concentration.
    Preserve the source stock amount and separately restore the 10 ml batch addition;
    do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs
    to the SL-4 stock subsection, whose API explicitly reports g_l=0.1. It is not
    a direct main-medium concentration. Preserve the source stock amount and separately
    restore the 10 ml batch addition; do not compute a final rate using an unresolved
    final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs
    to the SL-4 stock subsection, whose API explicitly reports g_l=0.1. It is not
    a direct main-medium concentration. Preserve the source stock amount and separately
    restore the 10 ml batch addition; do not compute a final rate using an unresolved
    final volume."}]}, {"quantity_id": "q12", "topic": "MnCl2 x 4 H2O — SL-4 stock",
    "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[1].recipe[3]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\":
    0.03,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.03,\n                        \"mmol_l\": 0.151588,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "MnCl2 x 4 H2O", "compound_id": 36, "amount": 0.03, "unit": "g", "g_l": 0.03,
    "mmol_l": 0.151588, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 28; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   MnCl2 x 4 H2O                                           0.03         g"}],
    "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection,
    whose API explicitly reports g_l=0.03. It is not a direct main-medium concentration.
    Preserve the source stock amount and separately restore the 10 ml batch addition;
    do not compute a final rate using an unresolved final volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path":
    "ingredients[11].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection,
    whose API explicitly reports g_l=0.03. It is not a direct main-medium concentration.
    Preserve the source stock amount and separately restore the 10 ml batch addition;
    do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.03",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs
    to the SL-4 stock subsection, whose API explicitly reports g_l=0.03. It is not
    a direct main-medium concentration. Preserve the source stock amount and separately
    restore the 10 ml batch addition; do not compute a final rate using an unresolved
    final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.03",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs
    to the SL-4 stock subsection, whose API explicitly reports g_l=0.03. It is not
    a direct main-medium concentration. Preserve the source stock amount and separately
    restore the 10 ml batch addition; do not compute a final rate using an unresolved
    final volume."}]}, {"quantity_id": "q13", "topic": "H3BO3 — SL-4 stock", "source":
    [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[1].recipe[4]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\":
    0.3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "H3BO3", "compound_id": 37, "amount": 0.3, "unit": "g", "g_l": 0.3, "mmol_l":
    4.85123, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 29; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   H3BO3                                                   0.30         g"}],
    "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection,
    whose API explicitly reports g_l=0.3. It is not a direct main-medium concentration.
    Preserve the source stock amount and separately restore the 10 ml batch addition;
    do not compute a final rate using an unresolved final volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path":
    "ingredients[12].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection,
    whose API explicitly reports g_l=0.3. It is not a direct main-medium concentration.
    Preserve the source stock amount and separately restore the 10 ml batch addition;
    do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs
    to the SL-4 stock subsection, whose API explicitly reports g_l=0.3. It is not
    a direct main-medium concentration. Preserve the source stock amount and separately
    restore the 10 ml batch addition; do not compute a final rate using an unresolved
    final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs
    to the SL-4 stock subsection, whose API explicitly reports g_l=0.3. It is not
    a direct main-medium concentration. Preserve the source stock amount and separately
    restore the 10 ml batch addition; do not compute a final rate using an unresolved
    final volume."}]}, {"quantity_id": "q14", "topic": "CoCl2 x 6 H2O — SL-4 stock",
    "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[1].recipe[5]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\":
    0.2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "CoCl2 x 6 H2O", "compound_id": 38, "amount": 0.2, "unit": "g", "g_l": 0.2, "mmol_l":
    1.54037, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm14",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 30; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   CoCl2 x 6 H2O                                           0.20         g"}],
    "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection,
    whose API explicitly reports g_l=0.2. It is not a direct main-medium concentration.
    Preserve the source stock amount and separately restore the 10 ml batch addition;
    do not compute a final rate using an unresolved final volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path":
    "ingredients[13].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection,
    whose API explicitly reports g_l=0.2. It is not a direct main-medium concentration.
    Preserve the source stock amount and separately restore the 10 ml batch addition;
    do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.2",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs
    to the SL-4 stock subsection, whose API explicitly reports g_l=0.2. It is not
    a direct main-medium concentration. Preserve the source stock amount and separately
    restore the 10 ml batch addition; do not compute a final rate using an unresolved
    final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.2",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs
    to the SL-4 stock subsection, whose API explicitly reports g_l=0.2. It is not
    a direct main-medium concentration. Preserve the source stock amount and separately
    restore the 10 ml batch addition; do not compute a final rate using an unresolved
    final volume."}]}, {"quantity_id": "q15", "topic": "CuCl2 x 2 H2O — SL-4 stock",
    "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\":
    0.01,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.01,\n                        \"mmol_l\": 0.0586569,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "CuCl2 x 2 H2O", "compound_id": 39, "amount": 0.01, "unit": "g", "g_l": 0.01,
    "mmol_l": 0.0586569, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 31; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   CuCl2 x 2 H2O                                           0.01         g"}],
    "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection,
    whose API explicitly reports g_l=0.01. It is not a direct main-medium concentration.
    Preserve the source stock amount and separately restore the 10 ml batch addition;
    do not compute a final rate using an unresolved final volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path":
    "ingredients[14].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection,
    whose API explicitly reports g_l=0.01. It is not a direct main-medium concentration.
    Preserve the source stock amount and separately restore the 10 ml batch addition;
    do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs
    to the SL-4 stock subsection, whose API explicitly reports g_l=0.01. It is not
    a direct main-medium concentration. Preserve the source stock amount and separately
    restore the 10 ml batch addition; do not compute a final rate using an unresolved
    final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs
    to the SL-4 stock subsection, whose API explicitly reports g_l=0.01. It is not
    a direct main-medium concentration. Preserve the source stock amount and separately
    restore the 10 ml batch addition; do not compute a final rate using an unresolved
    final volume."}]}, {"quantity_id": "q16", "topic": "NiCl2 x 6 H2O — SL-4 stock",
    "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[1].recipe[7]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\":
    0.02,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound":
    "NiCl2 x 6 H2O", "compound_id": 40, "amount": 0.02, "unit": "g", "g_l": 0.02,
    "mmol_l": 0.154322, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 32; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   NiCl2 x 6 H2O                                           0.02         g"}],
    "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection,
    whose API explicitly reports g_l=0.02. It is not a direct main-medium concentration.
    Preserve the source stock amount and separately restore the 10 ml batch addition;
    do not compute a final rate using an unresolved final volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path":
    "ingredients[15].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection,
    whose API explicitly reports g_l=0.02. It is not a direct main-medium concentration.
    Preserve the source stock amount and separately restore the 10 ml batch addition;
    do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs
    to the SL-4 stock subsection, whose API explicitly reports g_l=0.02. It is not
    a direct main-medium concentration. Preserve the source stock amount and separately
    restore the 10 ml batch addition; do not compute a final rate using an unresolved
    final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs
    to the SL-4 stock subsection, whose API explicitly reports g_l=0.02. It is not
    a direct main-medium concentration. Preserve the source stock amount and separately
    restore the 10 ml batch addition; do not compute a final rate using an unresolved
    final volume."}]}, {"quantity_id": "q17", "topic": "Na2MoO4 x 2 H2O — SL-4 stock",
    "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[1].recipe[8]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\":
    0.03,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.03,\n                        \"mmol_l\": 0.123993,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound":
    "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 0.03, "unit": "g", "g_l": 0.03,
    "mmol_l": 0.123993, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 33; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   Na2MoO4 x 2 H2O                                         0.03         g"}],
    "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection,
    whose API explicitly reports g_l=0.03. It is not a direct main-medium concentration.
    Preserve the source stock amount and separately restore the 10 ml batch addition;
    do not compute a final rate using an unresolved final volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path":
    "ingredients[16].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "This amount belongs to the SL-4 stock subsection,
    whose API explicitly reports g_l=0.03. It is not a direct main-medium concentration.
    Preserve the source stock amount and separately restore the 10 ml batch addition;
    do not compute a final rate using an unresolved final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.03",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs
    to the SL-4 stock subsection, whose API explicitly reports g_l=0.03. It is not
    a direct main-medium concentration. Preserve the source stock amount and separately
    restore the 10 ml batch addition; do not compute a final rate using an unresolved
    final volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.03",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "This amount belongs
    to the SL-4 stock subsection, whose API explicitly reports g_l=0.03. It is not
    a direct main-medium concentration. Preserve the source stock amount and separately
    restore the 10 ml batch addition; do not compute a final rate using an unresolved
    final volume."}]}, {"quantity_id": "q18", "topic": "Trace element solution SL-4
    receiving input", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\":
    \"Trace element solution SL-4\",\n                        \"solution_id\": 20,\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "solution":
    "Trace element solution SL-4", "solution_id": 20, "amount": 10, "unit": "ml",
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "dsm14", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf", "raw_path":
    "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 5; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   Trace element solution SL-4                            10.00        ml"}],
    "decision": "add", "rationale": "Represent this exact source solution amount and,
    where present, explicit 0.1% w/v strength. These source batch volumes do not become
    final-medium dosing rates merely because water is listed.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "Represent
    this exact source solution amount and, where present, explicit 0.1% w/v strength.
    These source batch volumes do not become final-medium dosing rates merely because
    water is listed.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Represent this exact source solution amount and, where present, explicit 0.1%
    w/v strength. These source batch volumes do not become final-medium dosing rates
    merely because water is listed.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Represent this exact source solution amount and, where present, explicit 0.1%
    w/v strength. These source batch volumes do not become final-medium dosing rates
    merely because water is listed.", "missing": true}]}, {"quantity_id": "q19", "topic":
    "Pyridoxine hydrochloride receiving input", "source": [{"evidence_id": "api14",
    "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin",
    "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"attribute\":
    \"0.1% w/v\",\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.00098912,\n                        \"mmol_l\":
    0.00480996,\n                        \"optional\": 0\n                    }",
    "exact_decoded_object": {"recipe_order": 4, "compound": "Pyridoxine hydrochloride",
    "compound_id": 519, "attribute": "0.1% w/v", "amount": 1, "unit": "ml", "g_l":
    0.00098912, "mmol_l": 0.00480996, "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."},
    {"evidence_id": "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 6; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   Pyridoxine hydrochloride (0.1% w/v)                     1.00        ml"}],
    "decision": "add", "rationale": "Represent this exact source solution amount and,
    where present, explicit 0.1% w/v strength. These source batch volumes do not become
    final-medium dosing rates merely because water is listed.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "Represent
    this exact source solution amount and, where present, explicit 0.1% w/v strength.
    These source batch volumes do not become final-medium dosing rates merely because
    water is listed.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Represent this exact source solution amount and, where present, explicit 0.1%
    w/v strength. These source batch volumes do not become final-medium dosing rates
    merely because water is listed.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Represent this exact source solution amount and, where present, explicit 0.1%
    w/v strength. These source batch volumes do not become final-medium dosing rates
    merely because water is listed.", "missing": true}]}, {"quantity_id": "q20", "topic":
    "Sodium resazurin receiving input", "source": [{"evidence_id": "api14", "reference":
    "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin",
    "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\":
    \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.00049456,\n                        \"mmol_l\":
    0.00196902,\n                        \"optional\": 0\n                    }",
    "exact_decoded_object": {"recipe_order": 6, "compound": "Sodium resazurin", "compound_id":
    1852, "attribute": "0.1% w/v", "amount": 0.5, "unit": "ml", "g_l": 0.00049456,
    "mmol_l": 0.00196902, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm14", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm14.bin", "raw_sha256": "ecdd0f0b59ea333c5201108a97ca1627dc3b213a59692a5d5ea4c2dc30562e76",
    "locator": "PDF extracted line 8; visually checked page", "accessed_at": "2026-10-28T10:19:17.249385Z",
    "quote": "   Sodium resazurin (0.1% w/v)                             0.50        ml"}],
    "decision": "add", "rationale": "Represent this exact source solution amount and,
    where present, explicit 0.1% w/v strength. These source batch volumes do not become
    final-medium dosing rates merely because water is listed.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "Represent
    this exact source solution amount and, where present, explicit 0.1% w/v strength.
    These source batch volumes do not become final-medium dosing rates merely because
    water is listed.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Represent this exact source solution amount and, where present, explicit 0.1%
    w/v strength. These source batch volumes do not become final-medium dosing rates
    merely because water is listed.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Represent this exact source solution amount and, where present, explicit 0.1%
    w/v strength. These source batch volumes do not become final-medium dosing rates
    merely because water is listed.", "missing": true}]}, {"quantity_id": "q21", "topic":
    "Water scope 0", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the 1000
    ml water input within Main sol. 14; neither the primary water line nor the API
    volume declaration establishes a measured final volume. Do not transfer stock
    water to the receiving medium.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml",
    "field_path": "evidence", "stored_value": null, "decision": "add", "rationale":
    "Preserve the 1000 ml water input within Main sol. 14; neither the primary water
    line nor the API volume declaration establishes a measured final volume. Do not
    transfer stock water to the receiving medium.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "evidence", "stored_value": null, "decision": "add", "rationale":
    "Preserve the 1000 ml water input within Main sol. 14; neither the primary water
    line nor the API volume declaration establishes a measured final volume. Do not
    transfer stock water to the receiving medium.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "evidence", "stored_value": null, "decision": "add", "rationale":
    "Preserve the 1000 ml water input within Main sol. 14; neither the primary water
    line nor the API volume declaration establishes a measured final volume. Do not
    transfer stock water to the receiving medium.", "missing": true}]}, {"quantity_id":
    "q22", "topic": "Water scope 1", "source": [{"evidence_id": "api14", "reference":
    "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin",
    "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[1].recipe[9]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "Preserve the 1000
    ml water input within Trace element solution SL-4; neither the primary water line
    nor the API volume declaration establishes a measured final volume. Do not transfer
    stock water to the receiving medium.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml",
    "field_path": "evidence", "stored_value": null, "decision": "add", "rationale":
    "Preserve the 1000 ml water input within Trace element solution SL-4; neither
    the primary water line nor the API volume declaration establishes a measured final
    volume. Do not transfer stock water to the receiving medium.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "evidence", "stored_value": null, "decision": "add", "rationale":
    "Preserve the 1000 ml water input within Trace element solution SL-4; neither
    the primary water line nor the API volume declaration establishes a measured final
    volume. Do not transfer stock water to the receiving medium.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "evidence", "stored_value": null, "decision": "add", "rationale":
    "Preserve the 1000 ml water input within Trace element solution SL-4; neither
    the primary water line nor the API volume declaration establishes a measured final
    volume. Do not transfer stock water to the receiving medium.", "missing": true}]},
    {"quantity_id": "q23", "topic": "Main preparation with late additions", "source":
    [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"step\": \"Dissolve ingredients (except
    carbonate and fructose) and sparge medium with 100% N2 gas for at least 30 - 45
    min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave. Add fructose from a sterile anoxic stock solution
    prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution
    prepared under 80% N2 and 20% CO2 gas atmosphere. Adjust pH of complete medium
    to 8.0.\"\n                    }", "exact_decoded_object": {"step": "Dissolve
    ingredients (except carbonate and fructose) and sparge medium with 100% N2 gas
    for at least 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere
    into anoxic Hungate-type tubes or serum vials and autoclave. Add fructose from
    a sterile anoxic stock solution prepared under 100% N2 gas and carbonate from
    a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere.
    Adjust pH of complete medium to 8.0."}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "mixed", "rationale": "The selected target and DSM owner retain the complete source
    paragraph. Add exact root evidence and keep it at this named stage; the KOMODO
    contributor lacks it. SL-4 pH 7.0 and 2 N NaOH belong to the stock, whereas pH
    8.0 belongs to the complete medium. No NaOH addition volume is supplied.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml", "field_path":
    "preparation_steps[0].description", "stored_value": "Dissolve ingredients (except
    carbonate and fructose) and sparge medium with 100% N2 gas for at least 30 - 45
    min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave. Add fructose from a sterile anoxic stock solution
    prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution
    prepared under 80% N2 and 20% CO2 gas atmosphere. Adjust pH of complete medium
    to 8.0.", "decision": "evidence_only", "rationale": "The selected target and DSM
    owner retain the complete source paragraph. Add exact root evidence and keep it
    at this named stage; the KOMODO contributor lacks it. SL-4 pH 7.0 and 2 N NaOH
    belong to the stock, whereas pH 8.0 belongs to the complete medium. No NaOH addition
    volume is supplied."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "preparation_steps[0].description", "stored_value": "Dissolve ingredients
    (except carbonate and fructose) and sparge medium with 100% N2 gas for at least
    30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into
    anoxic Hungate-type tubes or serum vials and autoclave. Add fructose from a sterile
    anoxic stock solution prepared under 100% N2 gas and carbonate from a sterile
    anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Adjust
    pH of complete medium to 8.0.", "decision": "evidence_only", "rationale": "The
    selected target and DSM owner retain the complete source paragraph. Add exact
    root evidence and keep it at this named stage; the KOMODO contributor lacks it.
    SL-4 pH 7.0 and 2 N NaOH belong to the stock, whereas pH 8.0 belongs to the complete
    medium. No NaOH addition volume is supplied."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "The selected target and DSM owner retain the complete source paragraph. Add exact
    root evidence and keep it at this named stage; the KOMODO contributor lacks it.
    SL-4 pH 7.0 and 2 N NaOH belong to the stock, whereas pH 8.0 belongs to the complete
    medium. No NaOH addition volume is supplied.", "missing": true}]}, {"quantity_id":
    "q24", "topic": "SL-4 preparation and pH adjustment", "source": [{"evidence_id":
    "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path":
    "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"step\": \"First dissolve EDTA in distilled
    water and adjust pH to 7.0 using 2 N NaOH; then add other compounds.\"\n                    }",
    "exact_decoded_object": {"step": "First dissolve EDTA in distilled water and adjust
    pH to 7.0 using 2 N NaOH; then add other compounds."}, "quote_basis": "Literal
    UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "mixed", "rationale": "The selected target and DSM owner retain the
    complete source paragraph. Add exact root evidence and keep it at this named stage;
    the KOMODO contributor lacks it. SL-4 pH 7.0 and 2 N NaOH belong to the stock,
    whereas pH 8.0 belongs to the complete medium. No NaOH addition volume is supplied.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml",
    "field_path": "preparation_steps[1].description", "stored_value": "First dissolve
    EDTA in distilled water and adjust pH to 7.0 using 2 N NaOH; then add other compounds.",
    "decision": "evidence_only", "rationale": "The selected target and DSM owner retain
    the complete source paragraph. Add exact root evidence and keep it at this named
    stage; the KOMODO contributor lacks it. SL-4 pH 7.0 and 2 N NaOH belong to the
    stock, whereas pH 8.0 belongs to the complete medium. No NaOH addition volume
    is supplied."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "preparation_steps[1].description", "stored_value": "First dissolve
    EDTA in distilled water and adjust pH to 7.0 using 2 N NaOH; then add other compounds.",
    "decision": "evidence_only", "rationale": "The selected target and DSM owner retain
    the complete source paragraph. Add exact root evidence and keep it at this named
    stage; the KOMODO contributor lacks it. SL-4 pH 7.0 and 2 N NaOH belong to the
    stock, whereas pH 8.0 belongs to the complete medium. No NaOH addition volume
    is supplied."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "The selected target and DSM owner retain the complete source paragraph. Add exact
    root evidence and keep it at this named stage; the KOMODO contributor lacks it.
    SL-4 pH 7.0 and 2 N NaOH belong to the stock, whereas pH 8.0 belongs to the complete
    medium. No NaOH addition volume is supplied.", "missing": true}]}, {"quantity_id":
    "q25", "topic": "Main pH", "source": [{"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"step\": \"Dissolve ingredients (except
    carbonate and fructose) and sparge medium with 100% N2 gas for at least 30 - 45
    min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave. Add fructose from a sterile anoxic stock solution
    prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution
    prepared under 80% N2 and 20% CO2 gas atmosphere. Adjust pH of complete medium
    to 8.0.\"\n                    }", "exact_decoded_object": {"step": "Dissolve
    ingredients (except carbonate and fructose) and sparge medium with 100% N2 gas
    for at least 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere
    into anoxic Hungate-type tubes or serum vials and autoclave. Add fructose from
    a sterile anoxic stock solution prepared under 100% N2 gas and carbonate from
    a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere.
    Adjust pH of complete medium to 8.0."}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "evidence_only", "rationale": "The generic complete-medium pH 8.0 is explicitly
    supported; SL-4 pH 7.0 must not replace it.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_FORMICACETICUM_MEDIUM.yaml",
    "field_path": "ph_value", "stored_value": 8.0, "decision": "evidence_only", "rationale":
    "The generic complete-medium pH 8.0 is explicitly supported; SL-4 pH 7.0 must
    not replace it."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml",
    "field_path": "ph_value", "stored_value": 8.0, "decision": "evidence_only", "rationale":
    "The generic complete-medium pH 8.0 is explicitly supported; SL-4 pH 7.0 must
    not replace it."}, {"path": "data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml",
    "field_path": "ph_value", "stored_value": 8.0, "decision": "evidence_only", "rationale":
    "The generic complete-medium pH 8.0 is explicitly supported; SL-4 pH 7.0 must
    not replace it."}]}, {"quantity_id": "q26", "topic": "Unresolved final volume
    and unquantified stock strengths", "source": [{"evidence_id": "api14", "reference":
    "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin",
    "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\":
    \"Trace element solution SL-4\",\n                        \"solution_id\": 20,\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "solution":
    "Trace element solution SL-4", "solution_id": 20, "amount": 10, "unit": "ml",
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "api14", "reference":
    "https://mediadive.dsmz.de/rest/medium/14", "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin",
    "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"attribute\":
    \"0.1% w/v\",\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.00098912,\n                        \"mmol_l\":
    0.00480996,\n                        \"optional\": 0\n                    }",
    "exact_decoded_object": {"recipe_order": 4, "compound": "Pyridoxine hydrochloride",
    "compound_id": 519, "attribute": "0.1% w/v", "amount": 1, "unit": "ml", "g_l":
    0.00098912, "mmol_l": 0.00480996, "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."},
    {"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\":
    \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.00049456,\n                        \"mmol_l\":
    0.00196902,\n                        \"optional\": 0\n                    }",
    "exact_decoded_object": {"recipe_order": 6, "compound": "Sodium resazurin", "compound_id":
    1852, "attribute": "0.1% w/v", "amount": 0.5, "unit": "ml", "g_l": 0.00049456,
    "mmol_l": 0.00196902, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14", "raw_path":
    "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "api14", "reference": "https://mediadive.dsmz.de/rest/medium/14",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api14.bin", "raw_sha256": "eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T10:19:16.990824Z",
    "quote": "{\n                        \"step\": \"Dissolve ingredients (except
    carbonate and fructose) and sparge medium with 100% N2 gas for at least 30 - 45
    min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave. Add fructose from a sterile anoxic stock solution
    prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution
    prepared under 80% N2 and 20% CO2 gas atmosphere. Adjust pH of complete medium
    to 8.0.\"\n                    }", "exact_decoded_object": {"step": "Dissolve
    ingredients (except carbonate and fructose) and sparge medium with 100% N2 gas
    for at least 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere
    into anoxic Hungate-type tubes or serum vials and autoclave. Add fructose from
    a sterile anoxic stock solution prepared under 100% N2 gas and carbonate from
    a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere.
    Adjust pH of complete medium to 8.0."}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "not_quantified", "rationale": "The listed liquid inputs total 1011.5 ml (1000
    water+10 SL-4+1 pyridoxine+0.5 dye), whereas the API declares 1011 ml and normalizes
    g_l against it. Neither is an independently measured final volume, and the later
    carbonate/fructose stock strengths and addition volumes are unspecified. Retain
    the provider declaration and primary batch recipe as distinct evidence; do not
    automatically renormalize to either sum.", "layer_assessments": []}]'
- assessment_id: a4
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: concern
  summary: All existing CHEBI IDs resolve and current labels match. Source sodium-resazurin
    and nickel-hydrate identities still conflict with those valid terms. Current MIM
    preferred/synonym statuses are retained, including the REJECTED preferred nickel-hydrate
    row and MAPPED exact synonym; catalog membership is not historical validity. EDTA
    hydration and an absent yeast term remain unresolved.
  target_ids:
  - CultureMech:000969
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
  - CultureMech:000969
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
  - CultureMech:000969
  evidence_ids:
  - local-target
- assessment_id: a7
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:000969
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-000969-restore-sl-4-and-the-percent-defined-input-stages
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore SL-4 and the percent-defined input stages
  description: Nine direct entries are SL-4 stock concentrations rather than main-medium
    quantities. The10 ml SL-4 addition and pyridoxine/resazurin solution strengths
    and doses are omitted. Keep eight exact main API g_l declarations qualified by
    their 1011 ml provider basis; the primary only lists water and liquid additions,
    which do not establish a final volume.
  target_ids:
  - CultureMech:000969
  field_paths:
  - ingredients[8]
  - ingredients[9]
  - ingredients[10]
  - ingredients[11]
  - ingredients[12]
  - ingredients[13]
  - ingredients[14]
  - ingredients[15]
  - ingredients[16]
  - solutions
  evidence_ids:
  - dsm14
  - api14
  - quantities
  - writer-mediadive
  rule_id: custom-source-stock-and-normalization
  native_severity: P2
  normalization_reason: 'Major: stock composition is asserted as direct medium content
    and required source stages are absent. Native P2.3 physical-state wording is not
    used to imply that g/L is inherently invalid for agar media.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-000969-reconcile-the-komodo-atmosphere-and-retained-dsm-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile the KOMODO atmosphere and retained DSM preparation
  description: 'The current KOMODO contributor says Aerobic: Yes and lacks preparation,
    while DSM14 explicitly uses an anoxic protocol. Target and DSM owner already retain
    the main and stock paragraphs and pH 8.0. Credit that content; reconcile the contradictory
    contributor before regeneration under the current compatibility guard.'
  target_ids:
  - CultureMech:000969
  field_paths:
  - data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml::notes
  - data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml::preparation_steps
  - preparation_steps
  evidence_ids:
  - owner-2
  - owner-1
  - dsm14
  - writer-resolver
  - writer-formulation
  rule_id: custom-source-atmosphere-and-retention
  native_severity: P2
  normalization_reason: 'Major: an explicit aerobic assertion conflicts with the source
    anoxic preparation. The same finding credits existing target/DSM instructions
    instead of alleging their absence.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-000969-resolve-sodium-resazurin-and-nickel-supplied-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Resolve sodium resazurin and nickel supplied forms
  description: CHEBI8806 denotes neutral Resazurin rather than the expressly supplied
    sodium salt. Both nickel slots use valid CHEBI34887 nickel dichloride although
    SL-4 specifies the hexahydrate; fresh OLS 53542 is nickel chloride hexahydrate.
    EDTA64734 additionally asserts anhydrous specificity not stated by the primary;
    that specificity remains unverified rather than a proved error.
  target_ids:
  - CultureMech:000969
  field_paths:
  - ingredients[4].term
  - ingredients[15].term
  - ingredients[15].mediaingredientmech_chebi_term
  evidence_ids:
  - dsm14
  - api14
  - chebi8806
  - chebi34887
  - chebi53542
  - grounding
  rule_id: custom-supplied-form-grounding
  native_severity: P2
  normalization_reason: 'Major: valid identifiers denote the wrong supplied salt/hydrate;
    this is distinct from native P2.2 nonexistent-ID validation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f4
  issue_key: culturemech-000969-preserve-and-qualify-historical-event-metadata
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Preserve and qualify historical event metadata
  description: KOMODO import events contain a literal .fZ timestamp and resolver events
    omit a UTC offset. Historical concentration reports preserve unresolved claims
    and exact source mappings, but are not independent proof of those historical retrieval
    events. The current API authenticates the historical raw digest and exact source
    objects, not historical review execution or all stock conclusions. Current root
    references and claim-level links remain incomplete.
  target_ids:
  - CultureMech:000969
  field_paths:
  - data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml::curation_history[1].timestamp
  evidence_ids:
  - history
  - historical-reader
  - writer-komodo
  rule_id: custom-event-metadata-provenance
  native_severity: P3
  normalization_reason: 'Minor: malformed or timezone-unspecified historical event
    metadata limits auditability without changing any recipe quantity; native P4.4
    only covers a one-event history and is not invoked.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Restore the SL-4 stock composition and source receiving dose, and represent
    the percent-defined pyridoxine and sodium-resazurin inputs. Preserve primary batch
    amounts and the API-declared nominal rates as separate scoped evidence; resolve
    final-volume provenance before computing new final rates.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000969
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Qualify or correct the contradictory KOMODO source flag with exact
    primary evidence and retain the DSM preparation verbatim in its main/stock scope.
    Never infer a strain growth claim from the title or a table flag.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000969
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Verify the sodium-resazurin salt identifier before selecting a replacement,
    and reconcile nickel primary and secondary slots to the exact hydrated form with
    authority evidence. Keep the source stock amounts unchanged. Retain the unresolved
    EDTA hydration limit and all current MIM mapping-status distinctions.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000969
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action4
  description: Retain every original event byte-for-byte. If authoritative provenance
    is recovered, append a verified correction or context event; never invent or overwrite
    its timestamp. Link fresh source evidence separately and preserve unresolved accession
    limitations.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:000969
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_formicaceticum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_formicoaceticum_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- The exact KOMODO14 accession and catalogue routes returned403; source identity authentication
  is partial. Historical mapping rows are not current catalogue responses.
- The API nominal1011 ml basis differs from the 1011.5 ml sum of listed liquid inputs.
  No measured final volume or automatic alternative normalization is asserted.
- Late carbonate/fructose stock strengths and addition volumes, and the SL-4 NaOH
  adjustment volume, are not quantified by the source.
- Optional agar defines a solid branch; this review does not turn it into an obligatory
  component for every use or infer species/strain growth.
- A sodium-resazurin replacement identifier and EDTA hydration are not guessed; current
  MIM rows do not establish historical mapping correctness.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
