# CLOSTRIDIUM GRANTII medium: retain supported amounts and correct source context

- Review: 20261028T103622Z-batch063-record04-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T10:18:43.747623Z
- Finished UTC: 2026-10-28T10:36:22.683000Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

All six local amounts agree with the current DSM648 generic recipe and provider declarations; the primary now explicitly states a final volume of 1000 ml. Four DSM-owner quantity claims are already authenticated. The generated/KOMODO records omit the source preparation and say Aerobic: Yes despite its anoxic protocol, and sodium resazurin points to the neutral compound. Evidence retention and historical metadata need bounded follow-up.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch063 native selection index 04.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006195 | data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml | generated | clostridium_grantii_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006195 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:006195 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:006195 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:006195 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Generic DSM648 identity and source-specific override

identity: concern. Targets: CultureMech:006195.

The exact generated lineage resolves KOMODO648 and DSM648 contributors. Current primary and API agree on the generic medium. The primary separately labels a DSM115762 pH override; it is outside this generic record assessment and does not establish an organism identity or universal growth condition. KOMODO catalogue authentication remains incomplete.

### Supported generic formulation

quantity: supported. Targets: CultureMech:006195.

The explicit primary final volume of 1000 ml supports the listed generic main quantities. This is stronger evidence than an inference from the 1000 ml water line. Four DSM-owner attached claims already match current raw bytes and exact API objects; retain them. Salt identity and missing preparation are separate concerns.

### Owner preparation and generated evidence loss

completeness: concern. Targets: CultureMech:006195.

The DSM owner already preserves the complete staged preparation and four quantity evidence entries. Target/KOMODO lack that preparation and retain an aerobic flag contrary to the source. Marine Broth is specifically BD Difco; the brand and separately prepared anoxic stock context should remain visible without inventing stock strengths.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:006195.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "Marine Broth generic main amount", "source": [{"evidence_id": "api648", "reference": "https://mediadive.dsmz.de/rest/medium/648", "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin", "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T10:19:17.509866Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Marine Broth\",\n                        \"compound_id\": 545,\n                        \"attribute\": \"BD Difco\",\n                        \"amount\": 18.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 18.5,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Marine Broth", "compound_id": 545, "attribute": "BD Difco", "amount": 18.5, "unit": "g", "g_l": 18.5, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26", "locator": "PDF extracted line 7; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z", "quote": "   Marine Broth (BD Difco)                               18.50       g"}, {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26", "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z", "quote": "Final volume: 1000 ml"}], "decision": "evidence_only", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=18.5 for the generic main solution. Preserve this supported amount and exact supplied form. The source specifies BD Difco Marine Broth, an undefined mixture; do not replace it with a guessed chemical composition.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "18.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=18.5 for the generic main solution. Preserve this supported amount and exact supplied form. The source specifies BD Difco Marine Broth, an undefined mixture; do not replace it with a guessed chemical composition. Link fresh exact evidence at this layer; do not change the supported number."}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "18.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=18.5 for the generic main solution. Preserve this supported amount and exact supplied form. The source specifies BD Difco Marine Broth, an undefined mixture; do not replace it with a guessed chemical composition. Link fresh exact evidence at this layer; do not change the supported number."}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "18.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=18.5 for the generic main solution. Preserve this supported amount and exact supplied form. The source specifies BD Difco Marine Broth, an undefined mixture; do not replace it with a guessed chemical composition. Link fresh exact evidence at this layer; do not change the supported number."}]}, {"quantity_id": "q2", "topic": "Sodium resazurin generic main amount", "source": [{"evidence_id": "api648", "reference": "https://mediadive.dsmz.de/rest/medium/648", "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin", "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T10:19:17.509866Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Sodium resazurin", "compound_id": 1852, "attribute": "0.1% w/v", "amount": 0.5, "unit": "ml", "g_l": 0.0005, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26", "locator": "PDF extracted line 8; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z", "quote": "   Sodium resazurin (0.1% w/v)                            0.50      ml"}, {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26", "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z", "quote": "Final volume: 1000 ml"}], "decision": "evidence_only", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=0.0005 for the generic main solution. Preserve this supported amount and exact supplied form. The0.5 ml input at 0.1% w/v contributes 0.5 mg per explicit final liter; this verifies the amount, not the neutral 8806 salt mapping.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=0.0005 for the generic main solution. Preserve this supported amount and exact supplied form. The0.5 ml input at 0.1% w/v contributes 0.5 mg per explicit final liter; this verifies the amount, not the neutral 8806 salt mapping. Link fresh exact evidence at this layer; do not change the supported number."}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=0.0005 for the generic main solution. Preserve this supported amount and exact supplied form. The0.5 ml input at 0.1% w/v contributes 0.5 mg per explicit final liter; this verifies the amount, not the neutral 8806 salt mapping. Link fresh exact evidence at this layer; do not change the supported number."}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=0.0005 for the generic main solution. Preserve this supported amount and exact supplied form. The0.5 ml input at 0.1% w/v contributes 0.5 mg per explicit final liter; this verifies the amount, not the neutral 8806 salt mapping. Link fresh exact evidence at this layer; do not change the supported number."}]}, {"quantity_id": "q3", "topic": "Na2CO3 generic main amount", "source": [{"evidence_id": "api648", "reference": "https://mediadive.dsmz.de/rest/medium/648", "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin", "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T10:19:17.509866Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 9.43503,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "Na2CO3", "compound_id": 32, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 9.43503, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26", "locator": "PDF extracted line 9; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z", "quote": "   Na2CO3                                                 1.00       g"}, {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26", "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z", "quote": "Final volume: 1000 ml"}], "decision": "mixed", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=1 for the generic main solution. Preserve this supported amount and exact supplied form. The amount is for the completed main formulation; late stock concentration and addition volume remain unspecified.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=1 for the generic main solution. Preserve this supported amount and exact supplied form. The amount is for the completed main formulation; late stock concentration and addition volume remain unspecified. Link fresh exact evidence at this layer; do not change the supported number."}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=1 for the generic main solution. Preserve this supported amount and exact supplied form. The amount is for the completed main formulation; late stock concentration and addition volume remain unspecified. Link fresh exact evidence at this layer; do not change the supported number."}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=1 for the generic main solution. Preserve this supported amount and exact supplied form. The amount is for the completed main formulation; late stock concentration and addition volume remain unspecified. Existing attached evidence has an exact literal current-raw match and matching cited response digest."}]}, {"quantity_id": "q4", "topic": "D-Glucose generic main amount", "source": [{"evidence_id": "api648", "reference": "https://mediadive.dsmz.de/rest/medium/648", "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin", "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T10:19:17.509866Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\": 211,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 27.7531,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "D-Glucose", "compound_id": 211, "amount": 5, "unit": "g", "g_l": 5, "mmol_l": 27.7531, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26", "locator": "PDF extracted line 10; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z", "quote": "   D-Glucose                                              5.00       g"}, {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26", "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z", "quote": "Final volume: 1000 ml"}], "decision": "mixed", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=5 for the generic main solution. Preserve this supported amount and exact supplied form. The amount is for the completed main formulation; late stock concentration and addition volume remain unspecified.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=5 for the generic main solution. Preserve this supported amount and exact supplied form. The amount is for the completed main formulation; late stock concentration and addition volume remain unspecified. Link fresh exact evidence at this layer; do not change the supported number."}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=5 for the generic main solution. Preserve this supported amount and exact supplied form. The amount is for the completed main formulation; late stock concentration and addition volume remain unspecified. Link fresh exact evidence at this layer; do not change the supported number."}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=5 for the generic main solution. Preserve this supported amount and exact supplied form. The amount is for the completed main formulation; late stock concentration and addition volume remain unspecified. Existing attached evidence has an exact literal current-raw match and matching cited response digest."}]}, {"quantity_id": "q5", "topic": "L-Cysteine HCl x H2O generic main amount", "source": [{"evidence_id": "api648", "reference": "https://mediadive.dsmz.de/rest/medium/648", "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin", "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T10:19:17.509866Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.70808,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "L-Cysteine HCl x H2O", "compound_id": 770, "amount": 0.3, "unit": "g", "g_l": 0.3, "mmol_l": 1.70808, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26", "locator": "PDF extracted line 11; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z", "quote": "   L-Cysteine HCl x H2O                                   0.30       g"}, {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26", "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z", "quote": "Final volume: 1000 ml"}], "decision": "mixed", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=0.3 for the generic main solution. Preserve this supported amount and exact supplied form. The amount is for the completed main formulation; late stock concentration and addition volume remain unspecified.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=0.3 for the generic main solution. Preserve this supported amount and exact supplied form. The amount is for the completed main formulation; late stock concentration and addition volume remain unspecified. Link fresh exact evidence at this layer; do not change the supported number."}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=0.3 for the generic main solution. Preserve this supported amount and exact supplied form. The amount is for the completed main formulation; late stock concentration and addition volume remain unspecified. Link fresh exact evidence at this layer; do not change the supported number."}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=0.3 for the generic main solution. Preserve this supported amount and exact supplied form. The amount is for the completed main formulation; late stock concentration and addition volume remain unspecified. Existing attached evidence has an exact literal current-raw match and matching cited response digest."}]}, {"quantity_id": "q6", "topic": "Na2S x 9 H2O generic main amount", "source": [{"evidence_id": "api648", "reference": "https://mediadive.dsmz.de/rest/medium/648", "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin", "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d", "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T10:19:17.509866Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.24905,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "Na2S x 9 H2O", "compound_id": 54, "amount": 0.3, "unit": "g", "g_l": 0.3, "mmol_l": 1.24905, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26", "locator": "PDF extracted line 12; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z", "quote": "   Na2S x 9 H2O                                           0.30       g"}, {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26", "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z", "quote": "Final volume: 1000 ml"}], "decision": "mixed", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=0.3 for the generic main solution. Preserve this supported amount and exact supplied form. The amount is for the completed main formulation; late stock concentration and addition volume remain unspecified.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=0.3 for the generic main solution. Preserve this supported amount and exact supplied form. The amount is for the completed main formulation; late stock concentration and addition volume remain unspecified. Link fresh exact evidence at this layer; do not change the supported number."}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=0.3 for the generic main solution. Preserve this supported amount and exact supplied form. The amount is for the completed main formulation; late stock concentration and addition volume remain unspecified. Link fresh exact evidence at this layer; do not change the supported number."}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "verified", "rationale": "The primary explicitly gives final volume 1000 ml and the API reports g_l=0.3 for the generic main solution. Preserve this supported amount and exact supplied form. The amount is for the completed main formulation; late stock concentration and addition volume remain unspecified. Existing attached evidence has an exact literal current-raw match and matching cited response digest."}]}, {"quantity_id": "q7", "topic": "Generic pH", "source": [{"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26", "locator": "PDF extracted line 3; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z", "quote": "Final pH: 6.6"}, {"evidence_id": "api648", "reference": "https://mediadive.dsmz.de/rest/medium/648", "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin", "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T10:19:17.509866Z", "quote": "{\n                        \"step\": \"Dissolve DIFCO Marine Broth powder and resazurin, bring the medium to a boil, then cool to room temperature under 80% N2 and 20% CO2 gas atmosphere. Dispense the medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Complete the medium by adding glucose, cysteine, and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. The pH of the complete medium should be around 6.6.\"\n                    }", "exact_decoded_object": {"step": "Dissolve DIFCO Marine Broth powder and resazurin, bring the medium to a boil, then cool to room temperature under 80% N2 and 20% CO2 gas atmosphere. Dispense the medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Complete the medium by adding glucose, cysteine, and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. The pH of the complete medium should be around 6.6."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Generic complete-medium pH 6.6 is explicit in the primary and API. The separately named strain override is not applied to this field.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml", "field_path": "ph_value", "stored_value": 6.6, "decision": "evidence_only", "rationale": "Generic complete-medium pH 6.6 is explicit in the primary and API. The separately named strain override is not applied to this field."}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml", "field_path": "ph_value", "stored_value": 6.6, "decision": "evidence_only", "rationale": "Generic complete-medium pH 6.6 is explicit in the primary and API. The separately named strain override is not applied to this field."}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml", "field_path": "ph_value", "stored_value": 6.6, "decision": "evidence_only", "rationale": "Generic complete-medium pH 6.6 is explicit in the primary and API. The separately named strain override is not applied to this field."}]}, {"quantity_id": "q8", "topic": "Water input and explicit final volume", "source": [{"evidence_id": "api648", "reference": "https://mediadive.dsmz.de/rest/medium/648", "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin", "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d", "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T10:19:17.509866Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26", "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z", "quote": "Final volume: 1000 ml"}], "decision": "add", "rationale": "Preserve the 1000 ml water input alongside the distinct explicit final-volume declaration. Do not claim that water alone proved final volume or that extra stock volumes are all known.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml", "field_path": "evidence", "stored_value": null, "decision": "add", "rationale": "Preserve the 1000 ml water input alongside the distinct explicit final-volume declaration. Do not claim that water alone proved final volume or that extra stock volumes are all known.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml", "field_path": "evidence", "stored_value": null, "decision": "add", "rationale": "Preserve the 1000 ml water input alongside the distinct explicit final-volume declaration. Do not claim that water alone proved final volume or that extra stock volumes are all known.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml", "field_path": "evidence", "stored_value": null, "decision": "add", "rationale": "Preserve the 1000 ml water input alongside the distinct explicit final-volume declaration. Do not claim that water alone proved final volume or that extra stock volumes are all known.", "missing": true}]}, {"quantity_id": "q9", "topic": "Sodium-resazurin solution dose", "source": [{"evidence_id": "api648", "reference": "https://mediadive.dsmz.de/rest/medium/648", "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin", "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T10:19:17.509866Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Sodium resazurin", "compound_id": 1852, "attribute": "0.1% w/v", "amount": 0.5, "unit": "ml", "g_l": 0.0005, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26", "locator": "PDF extracted line 8; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z", "quote": "   Sodium resazurin (0.1% w/v)                            0.50      ml"}], "decision": "add", "rationale": "The primary and API specify a 0.5 ml dose of 0.1% w/v sodium-resazurin solution. Preserve its strength and volume in the correct solution stage while retaining the already supported final solute amount.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The primary and API specify a 0.5 ml dose of 0.1% w/v sodium-resazurin solution. Preserve its strength and volume in the correct solution stage while retaining the already supported final solute amount.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The primary and API specify a 0.5 ml dose of 0.1% w/v sodium-resazurin solution. Preserve its strength and volume in the correct solution stage while retaining the already supported final solute amount.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The primary and API specify a 0.5 ml dose of 0.1% w/v sodium-resazurin solution. Preserve its strength and volume in the correct solution stage while retaining the already supported final solute amount.", "missing": true}]}, {"quantity_id": "q10", "topic": "Staged preparation", "source": [{"evidence_id": "api648", "reference": "https://mediadive.dsmz.de/rest/medium/648", "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin", "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T10:19:17.509866Z", "quote": "{\n                        \"step\": \"Dissolve DIFCO Marine Broth powder and resazurin, bring the medium to a boil, then cool to room temperature under 80% N2 and 20% CO2 gas atmosphere. Dispense the medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Complete the medium by adding glucose, cysteine, and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. The pH of the complete medium should be around 6.6.\"\n                    }", "exact_decoded_object": {"step": "Dissolve DIFCO Marine Broth powder and resazurin, bring the medium to a boil, then cool to room temperature under 80% N2 and 20% CO2 gas atmosphere. Dispense the medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Complete the medium by adding glucose, cysteine, and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. The pH of the complete medium should be around 6.6."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "The current DSM owner retains this full source paragraph, including the 80/20 and 100% gas stages; generated and KOMODO contributors omit it. Retain each number in its own stage and add claim-level root evidence, without inventing stock strengths, holding times or temperatures.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "The current DSM owner retains this full source paragraph, including the 80/20 and 100% gas stages; generated and KOMODO contributors omit it. Retain each number in its own stage and add claim-level root evidence, without inventing stock strengths, holding times or temperatures.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "The current DSM owner retains this full source paragraph, including the 80/20 and 100% gas stages; generated and KOMODO contributors omit it. Retain each number in its own stage and add claim-level root evidence, without inventing stock strengths, holding times or temperatures.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml", "field_path": "preparation_steps[0].description", "stored_value": "Dissolve DIFCO Marine Broth powder and resazurin, bring the medium to a boil, then cool to room temperature under 80% N2 and 20% CO2 gas atmosphere. Dispense the medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Complete the medium by adding glucose, cysteine, and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. The pH of the complete medium should be around 6.6.", "decision": "evidence_only", "rationale": "The current DSM owner retains this full source paragraph, including the 80/20 and 100% gas stages; generated and KOMODO contributors omit it. Retain each number in its own stage and add claim-level root evidence, without inventing stock strengths, holding times or temperatures."}]}, {"quantity_id": "q11", "topic": "Late stock strengths and volumes", "source": [{"evidence_id": "api648", "reference": "https://mediadive.dsmz.de/rest/medium/648", "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin", "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T10:19:17.509866Z", "quote": "{\n                        \"step\": \"Dissolve DIFCO Marine Broth powder and resazurin, bring the medium to a boil, then cool to room temperature under 80% N2 and 20% CO2 gas atmosphere. Dispense the medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Complete the medium by adding glucose, cysteine, and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. The pH of the complete medium should be around 6.6.\"\n                    }", "exact_decoded_object": {"step": "Dissolve DIFCO Marine Broth powder and resazurin, bring the medium to a boil, then cool to room temperature under 80% N2 and 20% CO2 gas atmosphere. Dispense the medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Complete the medium by adding glucose, cysteine, and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. The pH of the complete medium should be around 6.6."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "not_quantified", "rationale": "The source supplies final main solute amounts and explicit final volume, but not the concentrations or added volumes of the late glucose, cysteine, sulfide and carbonate stocks. Keep these unknown rather than infer a standard stock.", "layer_assessments": []}, {"quantity_id": "q12", "topic": "Excluded strain-specific pH branch", "source": [{"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf", "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26", "locator": "PDF extracted line 24; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z", "quote": "For DSM 115762: Adjust pH of final medium to 7.3."}], "decision": "evidence_only", "rationale": "The source-only pH 7.3 override is explicitly conditional on DSM115762. It is recorded for completeness but excluded from the generic target correction; no strain identity, growth claim or transfer of that value is proposed.", "layer_assessments": []}]

### Current ontology and MIM correspondence

grounding: concern. Targets: CultureMech:006195.

Every existing CHEBI term resolves with its current label. Sodium-resazurin 8806 is nevertheless a neutral-form mismatch, distinct from validity. The undefined Marine Broth mixture remains ungrounded without a guessed single compound. MIM preferred and synonym rows are preserved as current observations only.

### History and evidence scope

provenance: concern. Targets: CultureMech:006195.

Current source bytes, complete histories and scoped historical reports were read. Missing claim-level linkage and any malformed historical metadata are distinguished from authenticated source bytes; originals remain append-only.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:006195.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:006195.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Retain preparation and reconcile the aerobic flag

major / open / confirmed; issue key: culturemech-006195-retain-preparation-and-reconcile-the-aerobic-flag.

Selected and KOMODO notes say Aerobic: Yes while the primary uses an anoxic preparation. Both omit the full preparation paragraph already retained by the DSM owner. Preserve BD Difco specificity, the sodium-resazurin stock input and the distinct late-stock stages; the four latter stock strengths and addition volumes are not supplied.

### f2: Resolve the sodium-resazurin supplied form

major / open / confirmed; issue key: culturemech-006195-resolve-the-sodium-resazurin-supplied-form.

The source specifies sodium resazurin, but valid CHEBI8806 denotes neutral Resazurin with no sodium in its formula. Current MIM maps the sodium synonym to that neutral term; that catalog entry cannot settle the supplied-form mismatch. Other current named chemical forms and labels match the inspected authority objects.

### f3: Preserve authenticated owner evidence during regeneration

minor / open / confirmed; issue key: culturemech-006195-preserve-authenticated-owner-evidence-during-regeneration.

The DSM owner already has four exact attached quantity claims and a source reference. The generated target and KOMODO owner lack those links. Current formulation-aware merging rejects incompatible preparation metadata; do not bypass that guard merely to union evidence. The two remaining ingredient quantities are supported by fresh primary/provider evidence and need linkage rather than numeric changes.

### f4: Preserve and qualify historical event metadata

minor / open / confirmed; issue key: culturemech-006195-preserve-and-qualify-historical-event-metadata.

KOMODO import events contain a literal .fZ timestamp and resolver events omit a UTC offset. Historical concentration reports preserve unresolved claims and exact source mappings, but are not independent proof of those historical retrieval events. The four DSM-owner attached claims are already authenticated and must not be erased when adding fresh context.

## Recommended Actions And Acceptance Checks

### action1

Reconcile the inaccurate aerobic flag with exact primary evidence, retain the existing DSM-owner preparation and named commercial mixture, and restore source solution context. Keep unspecified stock strengths unknown. Regenerate only after current contributor formulations are compatible.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Resolve the exact sodium-salt identifier and canonical label using authority evidence before replacing the term. Retain the verified final amount and source stock strength/dose; do not import a neutral-form molecular weight.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Retain all four authenticated DSM-owner claims unchanged, add scoped evidence for the remaining supported quantities and preparation, and preserve their links after compatible regeneration. Keep actual old retrieval events distinct from this new capture.

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
| local-target | data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-2 | data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| identity-search | REVIEW_WORK/batch063/record04/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _parse_api_solutions, _parse_preparation_steps | context_only | Current composition parser restricts ingredients to the primary solution, excludes solvent and recognized stock additions, and retains explicit g_l. The solution parser preserves referenced or percent-defined stocks and source attributes. Preparation parsing still concatenates all solution steps into root preparation_steps; source-stage annotation remains important. These present functions do not prove the historical execution that produced this record. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group copies a sole contributor with merge metadata. For multiple contributors it passes records to merge_formulation_evidence, which checks compatibility; it does not authorize merging different preparation assertions. |
| writer-formulation | src/culturemech/merge/formulation.py; formulation_content, merge_formulation_evidence | context_only | Current compatibility preserves scientific fields and list order and rejects unequal formulations; only specified provenance/evidence lists are unioned. It performs no concentration conversion or stock expansion and does not authenticate historical merges. |
| writer-cleanup | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients, merge_ingredient_group | context_only | Current cleanup groups identical normalized names, keeps the first entry as a base, flags differing concentrations and combines a warning note; it does not sum concentrations. It can still discard distinctions when names repeat, so source stage must be retained. Current behavior does not establish the historical cause of an existing discrepancy. |
| writer-resolver | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.merge_composition | context_only | Current merge_composition copies nonplaceholder ingredients and available solutions, ph_value when absent, physical_state and medium_type. It does not copy preparation_steps or ph_range; present behavior is not proof of historical execution. |
| writer-komodo | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current _convert_to_culturemech builds KOMODO identity, source mapping and aerobic notes from table flags and emits placeholder ingredients. It uses time.strftime with %f, which does not itself establish a valid fractional timestamp. Existing malformed events remain original evidence, not a license to rewrite history. |
| historical-1 | reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md; Exact selected-owner matching rows, if present, plus report purpose/method and validation claims only; all other pair-specific conclusions outside scope. | context_only | Historical source-duplicate report: only exact selected-owner rows, where present, and its stated signature method are in scope. Similarity does not prove complete preparation identity; no assertion about absent exact pairs is inferred. |
| historical-2 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Current independent capture exactly matches the cited old response digest; 8 historical literal/decoded objects join. Access-event provenance remains historical. |
| historical-3 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/clostridium_grantii_medium.yaml.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Current independent capture exactly matches the cited old response digest; 8 historical literal/decoded objects join. Access-event provenance remains historical. |
| historical-4 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-5 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-6 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_grantii_medium.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-reader | REVIEW_WORK/batch063/record04/historical-reader.json | context_only | Full exact-header historical texts and scoped large report, with literal/decoded current-source joins and explicit mismatches. Historical access events are not reauthenticated. |
| attached-evidence-joins | REVIEW_WORK/batch063/record04/attached-evidence-joins.json | context_only | Every existing attached evidence claim is preserved and compared to the exact freshly captured response. Matching snippets do not authenticate historical access times. |
| complete-source-rows | REVIEW_WORK/batch063/record04/complete-source-rows.json | context_only | Every source recipe row and preparation object, with exact raw substring and decoded JSON locator, kept in its own solution stage. No biological recommendation follows from provider equipment metadata. |
| dsm648 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf; Exact source identity and scoped formulation/preparation | supports | Complete fresh one-page primary DSM648 visually read, including explicit final volume 1000 ml and generic pH 6.6. The separate DSM115762 pH 7.3 override is recorded only as an excluded strain-specific source branch, never transferred to the generic record. |
| api648 | https://mediadive.dsmz.de/rest/medium/648; Exact source identity and scoped formulation/preparation | supports | Complete current API648 medium, one main solution, seven recipe rows and full preparation read. Its raw digest matches the existing DSM-owner evidence capture; four attached literal objects are independently authenticated. |
| komodo648 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=648; Exact source identity and scoped formulation/preparation | unknown | Exact historical MediaInfo=648 route returned403; challenge content supplies no fresh accession or formulation authentication. |
| komodoList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact source identity and scoped formulation/preparation | unknown | Exact historical MediaList route returned403. The historical mapping row remains derivative, with no fresh catalogue body recovered. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_8806; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_29377; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17634; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91248; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_76209; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch063/record04/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch063/record04/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch063/record04/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch063/record04/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch063/record04/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch063/record04/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch063/record04/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch063/record04/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch063/record04/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- The exact KOMODO648 accession and catalogue routes returned403. Historical mapping rows support derivative context but do not complete current accession verification.
- The separate DSM115762 pH override is excluded from the generic formulation review; no organism or strain-level growth claim is inferred or proposed.
- Late glucose/cysteine/sulfide/carbonate stock strengths and added volumes are not stated. The primary explicit final volume supports generic main amounts, not invented stock recipes.
- The neutral-resazurin mismatch is established, but no sodium-salt replacement identifier is guessed.
- Current code behavior and freshly matching raw bytes do not prove historical writer execution or retrieval timestamps. Original curation events must remain append-only.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T103622Z-batch063-record04-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'CLOSTRIDIUM GRANTII medium: retain supported amounts and correct source context'
started_at: '2026-10-28T10:18:43.747623Z'
finished_at: '2026-10-28T10:36:22.683000Z'
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
summary: 'All six local amounts agree with the current DSM648 generic recipe and provider
  declarations; the primary now explicitly states a final volume of 1000 ml. Four
  DSM-owner quantity claims are already authenticated. The generated/KOMODO records
  omit the source preparation and say Aerobic: Yes despite its anoxic protocol, and
  sodium resazurin points to the neutral compound. Evidence retention and historical
  metadata need bounded follow-up.'
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
  - path: data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml
    sha256: 27b9d550546f82e08fafeaa433685173bd94965286b94ff07482767b8ef558bd
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml
    sha256: 432c686f7c546aa3e9a93fa9fc7e58837a26d812b2c3d38fec60879741a9f2c2
    role: context
  - path: data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml
    sha256: 8607402467706b95aef97ab436aee270018c30ad9d5a5f9d2eaf1359c9f67f7d
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml.md
    sha256: a3feece98b436e97d762ddffcc05470ac1420e788b58f7c58fdf83ba26715d5e
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/clostridium_grantii_medium.yaml.md
    sha256: 949bb8218e89413a3fa5dbfce398a9d981186dc24763c04bebc930ae628dfba4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.md
    sha256: d3a468d0277eeadbd2c3fdd1f3484158475ff741464633a6e148498cbf0bd327
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.md
    sha256: 9377bf43e589400c845bc249dc0582625ad7b4f60a0c68a6a899f56a3b4bfff4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_grantii_medium.md
    sha256: 04ab1936618c04b2cc43dc6beb260314e26f4075278c92b248ba7f61c10fadd1
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
  selection: Actual batch063 native selection index 04.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006195
targets:
- target_id: CultureMech:006195
  path: data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml
  label: clostridium_grantii_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:006195
  command: just validate-schema data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml
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
  - CultureMech:006195
  command: just validate-strict data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml
    --out REVIEW_WORK/batch063/record04/strict.tsv --workers 1 --quiet
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
  - CultureMech:006195
  command: just validate-terms data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml
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
  - CultureMech:006195
  command: just validate-references data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T10:30:12.729032Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 27b9d550546f82e08fafeaa433685173bd94965286b94ff07482767b8ef558bd
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T10:30:12.729032Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 432c686f7c546aa3e9a93fa9fc7e58837a26d812b2c3d38fec60879741a9f2c2
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T10:30:12.729032Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 8607402467706b95aef97ab436aee270018c30ad9d5a5f9d2eaf1359c9f67f7d
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch063/record04/identity-search.json
  accessed_at: '2026-10-28T10:30:12.808162Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems and stable identity resolve the owner;
    excluded namesakes are retained in the census. Similar names and source accessions
    are not promoted to owners.
  snapshot_sha256: 0524648a5348099494601124367c95d0b77ad91fe11b896a3cf34f0061ae65da
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _parse_api_solutions, _parse_preparation_steps
  accessed_at: '2026-10-28T10:30:12.729032Z'
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
  accessed_at: '2026-10-28T10:30:12.729032Z'
  support: context_only
  summary: Current merge_group copies a sole contributor with merge metadata. For
    multiple contributors it passes records to merge_formulation_evidence, which checks
    compatibility; it does not authorize merging different preparation assertions.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content, merge_formulation_evidence
  accessed_at: '2026-10-28T10:30:12.729032Z'
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
  accessed_at: '2026-10-28T10:30:12.729032Z'
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
  accessed_at: '2026-10-28T10:30:12.729032Z'
  support: context_only
  summary: Current merge_composition copies nonplaceholder ingredients and available
    solutions, ph_value when absent, physical_state and medium_type. It does not copy
    preparation_steps or ph_range; present behavior is not proof of historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-komodo
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T10:30:12.729032Z'
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
  accessed_at: '2026-10-28T10:30:12.729032Z'
  support: context_only
  summary: 'Historical source-duplicate report: only exact selected-owner rows, where
    present, and its stated signature method are in scope. Similarity does not prove
    complete preparation identity; no assertion about absent exact pairs is inferred.'
  snapshot_sha256: a723d4b7950bf4ac296a8a7fe4890d4d0881199a5d17c12a5fe39c2afbc40a10
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T10:30:12.729032Z'
  support: context_only
  summary: Current independent capture exactly matches the cited old response digest;
    8 historical literal/decoded objects join. Access-event provenance remains historical.
  snapshot_sha256: a3feece98b436e97d762ddffcc05470ac1420e788b58f7c58fdf83ba26715d5e
- evidence_id: historical-3
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/clostridium_grantii_medium.yaml.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T10:30:12.729032Z'
  support: context_only
  summary: Current independent capture exactly matches the cited old response digest;
    8 historical literal/decoded objects join. Access-event provenance remains historical.
  snapshot_sha256: 949bb8218e89413a3fa5dbfce398a9d981186dc24763c04bebc930ae628dfba4
- evidence_id: historical-4
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T10:30:12.729032Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: d3a468d0277eeadbd2c3fdd1f3484158475ff741464633a6e148498cbf0bd327
- evidence_id: historical-5
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T10:30:12.729032Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: 9377bf43e589400c845bc249dc0582625ad7b4f60a0c68a6a899f56a3b4bfff4
- evidence_id: historical-6
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_grantii_medium.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T10:30:12.729032Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: 04ab1936618c04b2cc43dc6beb260314e26f4075278c92b248ba7f61c10fadd1
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch063/record04/historical-reader.json
  accessed_at: '2026-10-28T10:30:12.814455Z'
  support: context_only
  summary: Full exact-header historical texts and scoped large report, with literal/decoded
    current-source joins and explicit mismatches. Historical access events are not
    reauthenticated.
  snapshot_sha256: 161f7b27001dae97497bc3fb47da0ffb8aa3a502ad3fa3f82279becdc03869a4
- evidence_id: attached-evidence-joins
  kind: record_content
  reference: REVIEW_WORK/batch063/record04/attached-evidence-joins.json
  accessed_at: '2026-10-28T10:30:12.814729Z'
  support: context_only
  summary: Every existing attached evidence claim is preserved and compared to the
    exact freshly captured response. Matching snippets do not authenticate historical
    access times.
  snapshot_sha256: 823b907e9c7223df083b0d6ab18663288bae18f5d99eb16a5044ab6119748f04
- evidence_id: complete-source-rows
  kind: record_content
  reference: REVIEW_WORK/batch063/record04/complete-source-rows.json
  accessed_at: '2026-10-28T10:30:12.815394Z'
  support: context_only
  summary: Every source recipe row and preparation object, with exact raw substring
    and decoded JSON locator, kept in its own solution stage. No biological recommendation
    follows from provider equipment metadata.
  snapshot_sha256: 8747932388c3029cf2037c0f0161b4763cdffff1de4c458239bc6fbbfe6d18fa
- evidence_id: dsm648
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:19:17.775559Z'
  support: supports
  summary: Complete fresh one-page primary DSM648 visually read, including explicit
    final volume 1000 ml and generic pH 6.6. The separate DSM115762 pH 7.3 override
    is recorded only as an excluded strain-specific source branch, never transferred
    to the generic record.
  snapshot_sha256: 70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26
- evidence_id: api648
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/648
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:19:17.509866Z'
  support: supports
  summary: Complete current API648 medium, one main solution, seven recipe rows and
    full preparation read. Its raw digest matches the existing DSM-owner evidence
    capture; four attached literal objects are independently authenticated.
  snapshot_sha256: e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d
- evidence_id: komodo648
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=648
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:19:16.390616Z'
  support: unknown
  summary: Exact historical MediaInfo=648 route returned403; challenge content supplies
    no fresh accession or formulation authentication.
  snapshot_sha256: 76823df594acf8c0f372d6f0e31f73c061084d53780e28f449898c57f76c0bb9
- evidence_id: komodoList
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:19:16.392827Z'
  support: unknown
  summary: Exact historical MediaList route returned403. The historical mapping row
    remains derivative, with no fresh catalogue body recovered.
  snapshot_sha256: f131cc2773375f470395ba0d7679083e86252b979a38be9f63eaef76965df8e8
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
- evidence_id: chebi17634
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17634
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:19:18.381952Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 6e02f3cee82012b7f630c04f122676c0029753074a4421cb005301b8bf24cedb
- evidence_id: chebi91248
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91248
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:19:22.132547Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 98a5682728cfda4162de150a88ae8c4b3a70c2d7c248634a5108be50a888a692
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_76209
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:19:21.042314Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 3eece7d96d2433ff020ece90db55323d138c5c828b78198f91d26b3eafa91f9f
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch063/record04/quantity-inventory.json
  accessed_at: '2026-10-28T10:30:12.826397Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 81869342f91971ea38fe3d26f0002d6606d8e7e440cea810c436d756b324fce2
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch063/record04/grounding-inventory.json
  accessed_at: '2026-10-28T10:30:12.826452Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: f2cb7d79449995aa55b5aca6d790185878d5b9997fc4954f197a9eafbebbe246
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch063/record04/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T10:30:12.826551Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 0f6cb32d4c3ead6edd1e2f4f9fd4d37b8a670532efa03348c2c1f3fa76ec5af8
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch063/record04/scalar-census.json
  accessed_at: '2026-10-28T10:30:12.826576Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: 818c549c3b02aed17c864e2626ea3e860144d12c8d79f920a30cbb010dede644
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch063/record04/validate-schema.json
  accessed_at: '2026-10-28T10:18:44.850590Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: c156a71e1d0785840fb01ea9e2f8e365f87ddaa8a27cca9f6bc6fa0f300e2901
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch063/record04/validate-strict.json
  accessed_at: '2026-10-28T10:18:45.858620Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch063/record04/strict.tsv\n"
  snapshot_sha256: 33ed2f4a952882c0a238bc5a36bf2509e277ad8443316313aaa8b826778dc561
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch063/record04/validate-terms.json
  accessed_at: '2026-10-28T10:18:46.971318Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: 198bf84a6117c831cf38400c01bfe40b4b4f4f0bf8885cf9a532faec16f6de85
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch063/record04/validate-references.json
  accessed_at: '2026-10-28T10:18:47.667389Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: decd9eb2ac96ef891e669374c4b647c193b016fb68e5d3494fbfd164ac10fd7f
assessments:
- assessment_id: a1
  area: identity
  topic: Generic DSM648 identity and source-specific override
  outcome: concern
  summary: The exact generated lineage resolves KOMODO648 and DSM648 contributors.
    Current primary and API agree on the generic medium. The primary separately labels
    a DSM115762 pH override; it is outside this generic record assessment and does
    not establish an organism identity or universal growth condition. KOMODO catalogue
    authentication remains incomplete.
  target_ids:
  - CultureMech:006195
  evidence_ids:
  - identity-search
  - dsm648
  - api648
  - historical-reader
  - komodo648
- assessment_id: a2
  area: quantity
  topic: Supported generic formulation
  outcome: supported
  summary: The explicit primary final volume of 1000 ml supports the listed generic
    main quantities. This is stronger evidence than an inference from the 1000 ml
    water line. Four DSM-owner attached claims already match current raw bytes and
    exact API objects; retain them. Salt identity and missing preparation are separate
    concerns.
  target_ids:
  - CultureMech:006195
  evidence_ids:
  - dsm648
  - api648
  - attached-evidence-joins
- assessment_id: a3
  area: completeness
  topic: Owner preparation and generated evidence loss
  outcome: concern
  summary: The DSM owner already preserves the complete staged preparation and four
    quantity evidence entries. Target/KOMODO lack that preparation and retain an aerobic
    flag contrary to the source. Marine Broth is specifically BD Difco; the brand
    and separately prepared anoxic stock context should remain visible without inventing
    stock strengths.
  target_ids:
  - CultureMech:006195
  evidence_ids:
  - owner-2
  - local-target
  - dsm648
  - api648
  - writer-formulation
- assessment_id: a4
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:006195
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "Marine Broth generic main amount", "source":
    [{"evidence_id": "api648", "reference": "https://mediadive.dsmz.de/rest/medium/648",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin", "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T10:19:17.509866Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Marine Broth\",\n                        \"compound_id\": 545,\n                        \"attribute\":
    \"BD Difco\",\n                        \"amount\": 18.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 18.5,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Marine Broth", "compound_id": 545, "attribute": "BD Difco", "amount": 18.5, "unit":
    "g", "g_l": 18.5, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm648",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26",
    "locator": "PDF extracted line 7; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z",
    "quote": "   Marine Broth (BD Difco)                               18.50       g"},
    {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26",
    "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z",
    "quote": "Final volume: 1000 ml"}], "decision": "evidence_only", "rationale":
    "The primary explicitly gives final volume 1000 ml and the API reports g_l=18.5
    for the generic main solution. Preserve this supported amount and exact supplied
    form. The source specifies BD Difco Marine Broth, an undefined mixture; do not
    replace it with a guessed chemical composition.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml", "field_path": "ingredients[0].concentration",
    "stored_value": {"value": "18.5", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The primary explicitly gives final volume 1000 ml and the API reports
    g_l=18.5 for the generic main solution. Preserve this supported amount and exact
    supplied form. The source specifies BD Difco Marine Broth, an undefined mixture;
    do not replace it with a guessed chemical composition. Link fresh exact evidence
    at this layer; do not change the supported number."}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "18.5",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly
    gives final volume 1000 ml and the API reports g_l=18.5 for the generic main solution.
    Preserve this supported amount and exact supplied form. The source specifies BD
    Difco Marine Broth, an undefined mixture; do not replace it with a guessed chemical
    composition. Link fresh exact evidence at this layer; do not change the supported
    number."}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "18.5",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly
    gives final volume 1000 ml and the API reports g_l=18.5 for the generic main solution.
    Preserve this supported amount and exact supplied form. The source specifies BD
    Difco Marine Broth, an undefined mixture; do not replace it with a guessed chemical
    composition. Link fresh exact evidence at this layer; do not change the supported
    number."}]}, {"quantity_id": "q2", "topic": "Sodium resazurin generic main amount",
    "source": [{"evidence_id": "api648", "reference": "https://mediadive.dsmz.de/rest/medium/648",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin", "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T10:19:17.509866Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\":
    \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "Sodium resazurin", "compound_id": 1852, "attribute": "0.1% w/v", "amount": 0.5,
    "unit": "ml", "g_l": 0.0005, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26",
    "locator": "PDF extracted line 8; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z",
    "quote": "   Sodium resazurin (0.1% w/v)                            0.50      ml"},
    {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26",
    "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z",
    "quote": "Final volume: 1000 ml"}], "decision": "evidence_only", "rationale":
    "The primary explicitly gives final volume 1000 ml and the API reports g_l=0.0005
    for the generic main solution. Preserve this supported amount and exact supplied
    form. The0.5 ml input at 0.1% w/v contributes 0.5 mg per explicit final liter;
    this verifies the amount, not the neutral 8806 salt mapping.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml", "field_path":
    "ingredients[1].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "The primary explicitly gives final
    volume 1000 ml and the API reports g_l=0.0005 for the generic main solution. Preserve
    this supported amount and exact supplied form. The0.5 ml input at 0.1% w/v contributes
    0.5 mg per explicit final liter; this verifies the amount, not the neutral 8806
    salt mapping. Link fresh exact evidence at this layer; do not change the supported
    number."}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.0005",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly
    gives final volume 1000 ml and the API reports g_l=0.0005 for the generic main
    solution. Preserve this supported amount and exact supplied form. The0.5 ml input
    at 0.1% w/v contributes 0.5 mg per explicit final liter; this verifies the amount,
    not the neutral 8806 salt mapping. Link fresh exact evidence at this layer; do
    not change the supported number."}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.0005",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly
    gives final volume 1000 ml and the API reports g_l=0.0005 for the generic main
    solution. Preserve this supported amount and exact supplied form. The0.5 ml input
    at 0.1% w/v contributes 0.5 mg per explicit final liter; this verifies the amount,
    not the neutral 8806 salt mapping. Link fresh exact evidence at this layer; do
    not change the supported number."}]}, {"quantity_id": "q3", "topic": "Na2CO3 generic
    main amount", "source": [{"evidence_id": "api648", "reference": "https://mediadive.dsmz.de/rest/medium/648",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin", "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T10:19:17.509866Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"mmol_l\": 9.43503,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "Na2CO3", "compound_id": 32, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 9.43503,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "dsm648", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf", "raw_path":
    "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26",
    "locator": "PDF extracted line 9; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z",
    "quote": "   Na2CO3                                                 1.00       g"},
    {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26",
    "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z",
    "quote": "Final volume: 1000 ml"}], "decision": "mixed", "rationale": "The primary
    explicitly gives final volume 1000 ml and the API reports g_l=1 for the generic
    main solution. Preserve this supported amount and exact supplied form. The amount
    is for the completed main formulation; late stock concentration and addition volume
    remain unspecified.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly
    gives final volume 1000 ml and the API reports g_l=1 for the generic main solution.
    Preserve this supported amount and exact supplied form. The amount is for the
    completed main formulation; late stock concentration and addition volume remain
    unspecified. Link fresh exact evidence at this layer; do not change the supported
    number."}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly
    gives final volume 1000 ml and the API reports g_l=1 for the generic main solution.
    Preserve this supported amount and exact supplied form. The amount is for the
    completed main formulation; late stock concentration and addition volume remain
    unspecified. Link fresh exact evidence at this layer; do not change the supported
    number."}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "verified", "rationale": "The primary explicitly gives
    final volume 1000 ml and the API reports g_l=1 for the generic main solution.
    Preserve this supported amount and exact supplied form. The amount is for the
    completed main formulation; late stock concentration and addition volume remain
    unspecified. Existing attached evidence has an exact literal current-raw match
    and matching cited response digest."}]}, {"quantity_id": "q4", "topic": "D-Glucose
    generic main amount", "source": [{"evidence_id": "api648", "reference": "https://mediadive.dsmz.de/rest/medium/648",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin", "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T10:19:17.509866Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"D-Glucose\",\n                        \"compound_id\": 211,\n                        \"amount\":
    5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    5,\n                        \"mmol_l\": 27.7531,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "D-Glucose", "compound_id": 211, "amount": 5, "unit": "g", "g_l": 5, "mmol_l":
    27.7531, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm648",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26",
    "locator": "PDF extracted line 10; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z",
    "quote": "   D-Glucose                                              5.00       g"},
    {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26",
    "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z",
    "quote": "Final volume: 1000 ml"}], "decision": "mixed", "rationale": "The primary
    explicitly gives final volume 1000 ml and the API reports g_l=5 for the generic
    main solution. Preserve this supported amount and exact supplied form. The amount
    is for the completed main formulation; late stock concentration and addition volume
    remain unspecified.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly
    gives final volume 1000 ml and the API reports g_l=5 for the generic main solution.
    Preserve this supported amount and exact supplied form. The amount is for the
    completed main formulation; late stock concentration and addition volume remain
    unspecified. Link fresh exact evidence at this layer; do not change the supported
    number."}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly
    gives final volume 1000 ml and the API reports g_l=5 for the generic main solution.
    Preserve this supported amount and exact supplied form. The amount is for the
    completed main formulation; late stock concentration and addition volume remain
    unspecified. Link fresh exact evidence at this layer; do not change the supported
    number."}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "verified", "rationale": "The primary explicitly gives
    final volume 1000 ml and the API reports g_l=5 for the generic main solution.
    Preserve this supported amount and exact supplied form. The amount is for the
    completed main formulation; late stock concentration and addition volume remain
    unspecified. Existing attached evidence has an exact literal current-raw match
    and matching cited response digest."}]}, {"quantity_id": "q5", "topic": "L-Cysteine
    HCl x H2O generic main amount", "source": [{"evidence_id": "api648", "reference":
    "https://mediadive.dsmz.de/rest/medium/648", "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin",
    "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d",
    "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T10:19:17.509866Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\":
    0.3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.3,\n                        \"mmol_l\": 1.70808,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "L-Cysteine HCl x H2O", "compound_id": 770, "amount": 0.3, "unit": "g", "g_l":
    0.3, "mmol_l": 1.70808, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26",
    "locator": "PDF extracted line 11; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z",
    "quote": "   L-Cysteine HCl x H2O                                   0.30       g"},
    {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26",
    "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z",
    "quote": "Final volume: 1000 ml"}], "decision": "mixed", "rationale": "The primary
    explicitly gives final volume 1000 ml and the API reports g_l=0.3 for the generic
    main solution. Preserve this supported amount and exact supplied form. The amount
    is for the completed main formulation; late stock concentration and addition volume
    remain unspecified.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly
    gives final volume 1000 ml and the API reports g_l=0.3 for the generic main solution.
    Preserve this supported amount and exact supplied form. The amount is for the
    completed main formulation; late stock concentration and addition volume remain
    unspecified. Link fresh exact evidence at this layer; do not change the supported
    number."}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly
    gives final volume 1000 ml and the API reports g_l=0.3 for the generic main solution.
    Preserve this supported amount and exact supplied form. The amount is for the
    completed main formulation; late stock concentration and addition volume remain
    unspecified. Link fresh exact evidence at this layer; do not change the supported
    number."}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The primary explicitly
    gives final volume 1000 ml and the API reports g_l=0.3 for the generic main solution.
    Preserve this supported amount and exact supplied form. The amount is for the
    completed main formulation; late stock concentration and addition volume remain
    unspecified. Existing attached evidence has an exact literal current-raw match
    and matching cited response digest."}]}, {"quantity_id": "q6", "topic": "Na2S
    x 9 H2O generic main amount", "source": [{"evidence_id": "api648", "reference":
    "https://mediadive.dsmz.de/rest/medium/648", "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin",
    "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d",
    "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T10:19:17.509866Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\":
    0.3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.3,\n                        \"mmol_l\": 1.24905,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "Na2S x 9 H2O", "compound_id": 54, "amount": 0.3, "unit": "g", "g_l": 0.3, "mmol_l":
    1.24905, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm648",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26",
    "locator": "PDF extracted line 12; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z",
    "quote": "   Na2S x 9 H2O                                           0.30       g"},
    {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26",
    "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z",
    "quote": "Final volume: 1000 ml"}], "decision": "mixed", "rationale": "The primary
    explicitly gives final volume 1000 ml and the API reports g_l=0.3 for the generic
    main solution. Preserve this supported amount and exact supplied form. The amount
    is for the completed main formulation; late stock concentration and addition volume
    remain unspecified.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly
    gives final volume 1000 ml and the API reports g_l=0.3 for the generic main solution.
    Preserve this supported amount and exact supplied form. The amount is for the
    completed main formulation; late stock concentration and addition volume remain
    unspecified. Link fresh exact evidence at this layer; do not change the supported
    number."}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly
    gives final volume 1000 ml and the API reports g_l=0.3 for the generic main solution.
    Preserve this supported amount and exact supplied form. The amount is for the
    completed main formulation; late stock concentration and addition volume remain
    unspecified. Link fresh exact evidence at this layer; do not change the supported
    number."}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "The primary explicitly
    gives final volume 1000 ml and the API reports g_l=0.3 for the generic main solution.
    Preserve this supported amount and exact supplied form. The amount is for the
    completed main formulation; late stock concentration and addition volume remain
    unspecified. Existing attached evidence has an exact literal current-raw match
    and matching cited response digest."}]}, {"quantity_id": "q7", "topic": "Generic
    pH", "source": [{"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26",
    "locator": "PDF extracted line 3; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z",
    "quote": "Final pH: 6.6"}, {"evidence_id": "api648", "reference": "https://mediadive.dsmz.de/rest/medium/648",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin", "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T10:19:17.509866Z",
    "quote": "{\n                        \"step\": \"Dissolve DIFCO Marine Broth powder
    and resazurin, bring the medium to a boil, then cool to room temperature under
    80% N2 and 20% CO2 gas atmosphere. Dispense the medium under the same gas atmosphere
    into anoxic Hungate-type tubes or serum vials and autoclave. Complete the medium
    by adding glucose, cysteine, and sulfide from sterile anoxic stock solutions prepared
    under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared
    under 80% N2 and 20% CO2 gas mixture. The pH of the complete medium should be
    around 6.6.\"\n                    }", "exact_decoded_object": {"step": "Dissolve
    DIFCO Marine Broth powder and resazurin, bring the medium to a boil, then cool
    to room temperature under 80% N2 and 20% CO2 gas atmosphere. Dispense the medium
    under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and
    autoclave. Complete the medium by adding glucose, cysteine, and sulfide from sterile
    anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile
    anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. The pH of
    the complete medium should be around 6.6."}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "evidence_only", "rationale": "Generic complete-medium pH 6.6 is explicit in the
    primary and API. The separately named strain override is not applied to this field.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml",
    "field_path": "ph_value", "stored_value": 6.6, "decision": "evidence_only", "rationale":
    "Generic complete-medium pH 6.6 is explicit in the primary and API. The separately
    named strain override is not applied to this field."}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml",
    "field_path": "ph_value", "stored_value": 6.6, "decision": "evidence_only", "rationale":
    "Generic complete-medium pH 6.6 is explicit in the primary and API. The separately
    named strain override is not applied to this field."}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml",
    "field_path": "ph_value", "stored_value": 6.6, "decision": "evidence_only", "rationale":
    "Generic complete-medium pH 6.6 is explicit in the primary and API. The separately
    named strain override is not applied to this field."}]}, {"quantity_id": "q8",
    "topic": "Water input and explicit final volume", "source": [{"evidence_id": "api648",
    "reference": "https://mediadive.dsmz.de/rest/medium/648", "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin",
    "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d",
    "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T10:19:17.509866Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26",
    "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z",
    "quote": "Final volume: 1000 ml"}], "decision": "add", "rationale": "Preserve
    the 1000 ml water input alongside the distinct explicit final-volume declaration.
    Do not claim that water alone proved final volume or that extra stock volumes
    are all known.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml",
    "field_path": "evidence", "stored_value": null, "decision": "add", "rationale":
    "Preserve the 1000 ml water input alongside the distinct explicit final-volume
    declaration. Do not claim that water alone proved final volume or that extra stock
    volumes are all known.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml",
    "field_path": "evidence", "stored_value": null, "decision": "add", "rationale":
    "Preserve the 1000 ml water input alongside the distinct explicit final-volume
    declaration. Do not claim that water alone proved final volume or that extra stock
    volumes are all known.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml",
    "field_path": "evidence", "stored_value": null, "decision": "add", "rationale":
    "Preserve the 1000 ml water input alongside the distinct explicit final-volume
    declaration. Do not claim that water alone proved final volume or that extra stock
    volumes are all known.", "missing": true}]}, {"quantity_id": "q9", "topic": "Sodium-resazurin
    solution dose", "source": [{"evidence_id": "api648", "reference": "https://mediadive.dsmz.de/rest/medium/648",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin", "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T10:19:17.509866Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\":
    \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "Sodium resazurin", "compound_id": 1852, "attribute": "0.1% w/v", "amount": 0.5,
    "unit": "ml", "g_l": 0.0005, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm648", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26",
    "locator": "PDF extracted line 8; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z",
    "quote": "   Sodium resazurin (0.1% w/v)                            0.50      ml"}],
    "decision": "add", "rationale": "The primary and API specify a 0.5 ml dose of
    0.1% w/v sodium-resazurin solution. Preserve its strength and volume in the correct
    solution stage while retaining the already supported final solute amount.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "The primary
    and API specify a 0.5 ml dose of 0.1% w/v sodium-resazurin solution. Preserve
    its strength and volume in the correct solution stage while retaining the already
    supported final solute amount.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The primary and API specify a 0.5 ml dose of 0.1% w/v sodium-resazurin solution.
    Preserve its strength and volume in the correct solution stage while retaining
    the already supported final solute amount.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The primary and API specify a 0.5 ml dose of 0.1% w/v sodium-resazurin solution.
    Preserve its strength and volume in the correct solution stage while retaining
    the already supported final solute amount.", "missing": true}]}, {"quantity_id":
    "q10", "topic": "Staged preparation", "source": [{"evidence_id": "api648", "reference":
    "https://mediadive.dsmz.de/rest/medium/648", "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin",
    "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T10:19:17.509866Z",
    "quote": "{\n                        \"step\": \"Dissolve DIFCO Marine Broth powder
    and resazurin, bring the medium to a boil, then cool to room temperature under
    80% N2 and 20% CO2 gas atmosphere. Dispense the medium under the same gas atmosphere
    into anoxic Hungate-type tubes or serum vials and autoclave. Complete the medium
    by adding glucose, cysteine, and sulfide from sterile anoxic stock solutions prepared
    under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared
    under 80% N2 and 20% CO2 gas mixture. The pH of the complete medium should be
    around 6.6.\"\n                    }", "exact_decoded_object": {"step": "Dissolve
    DIFCO Marine Broth powder and resazurin, bring the medium to a boil, then cool
    to room temperature under 80% N2 and 20% CO2 gas atmosphere. Dispense the medium
    under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and
    autoclave. Complete the medium by adding glucose, cysteine, and sulfide from sterile
    anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile
    anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. The pH of
    the complete medium should be around 6.6."}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "mixed", "rationale": "The current DSM owner retains this full source paragraph,
    including the 80/20 and 100% gas stages; generated and KOMODO contributors omit
    it. Retain each number in its own stage and add claim-level root evidence, without
    inventing stock strengths, holding times or temperatures.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml", "field_path":
    "preparation_steps", "stored_value": null, "decision": "add", "rationale": "The
    current DSM owner retains this full source paragraph, including the 80/20 and
    100% gas stages; generated and KOMODO contributors omit it. Retain each number
    in its own stage and add claim-level root evidence, without inventing stock strengths,
    holding times or temperatures.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "The current DSM owner retains this full source paragraph, including the 80/20
    and 100% gas stages; generated and KOMODO contributors omit it. Retain each number
    in its own stage and add claim-level root evidence, without inventing stock strengths,
    holding times or temperatures.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml",
    "field_path": "preparation_steps[0].description", "stored_value": "Dissolve DIFCO
    Marine Broth powder and resazurin, bring the medium to a boil, then cool to room
    temperature under 80% N2 and 20% CO2 gas atmosphere. Dispense the medium under
    the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.
    Complete the medium by adding glucose, cysteine, and sulfide from sterile anoxic
    stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic
    stock solution prepared under 80% N2 and 20% CO2 gas mixture. The pH of the complete
    medium should be around 6.6.", "decision": "evidence_only", "rationale": "The
    current DSM owner retains this full source paragraph, including the 80/20 and
    100% gas stages; generated and KOMODO contributors omit it. Retain each number
    in its own stage and add claim-level root evidence, without inventing stock strengths,
    holding times or temperatures."}]}, {"quantity_id": "q11", "topic": "Late stock
    strengths and volumes", "source": [{"evidence_id": "api648", "reference": "https://mediadive.dsmz.de/rest/medium/648",
    "raw_path": "REVIEW_WORK/batch063/source02-04/api648.bin", "raw_sha256": "e6cac93f5c07185a4c6bdd3c6062944fd03736ca28220417f71d9c590fe5239d",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T10:19:17.509866Z",
    "quote": "{\n                        \"step\": \"Dissolve DIFCO Marine Broth powder
    and resazurin, bring the medium to a boil, then cool to room temperature under
    80% N2 and 20% CO2 gas atmosphere. Dispense the medium under the same gas atmosphere
    into anoxic Hungate-type tubes or serum vials and autoclave. Complete the medium
    by adding glucose, cysteine, and sulfide from sterile anoxic stock solutions prepared
    under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared
    under 80% N2 and 20% CO2 gas mixture. The pH of the complete medium should be
    around 6.6.\"\n                    }", "exact_decoded_object": {"step": "Dissolve
    DIFCO Marine Broth powder and resazurin, bring the medium to a boil, then cool
    to room temperature under 80% N2 and 20% CO2 gas atmosphere. Dispense the medium
    under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and
    autoclave. Complete the medium by adding glucose, cysteine, and sulfide from sterile
    anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile
    anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. The pH of
    the complete medium should be around 6.6."}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "not_quantified", "rationale": "The source supplies final main solute amounts
    and explicit final volume, but not the concentrations or added volumes of the
    late glucose, cysteine, sulfide and carbonate stocks. Keep these unknown rather
    than infer a standard stock.", "layer_assessments": []}, {"quantity_id": "q12",
    "topic": "Excluded strain-specific pH branch", "source": [{"evidence_id": "dsm648",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium648.pdf",
    "raw_path": "REVIEW_WORK/batch063/source02-04/dsm648.bin", "raw_sha256": "70c9fe5707cb75eedb11d8d825a1df2f58ded23859e11c956e836c6fc110aa26",
    "locator": "PDF extracted line 24; visually checked page", "accessed_at": "2026-10-28T10:19:17.775559Z",
    "quote": "For DSM 115762: Adjust pH of final medium to 7.3."}], "decision": "evidence_only",
    "rationale": "The source-only pH 7.3 override is explicitly conditional on DSM115762.
    It is recorded for completeness but excluded from the generic target correction;
    no strain identity, growth claim or transfer of that value is proposed.", "layer_assessments":
    []}]'
- assessment_id: a5
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: concern
  summary: Every existing CHEBI term resolves with its current label. Sodium-resazurin
    8806 is nevertheless a neutral-form mismatch, distinct from validity. The undefined
    Marine Broth mixture remains ungrounded without a guessed single compound. MIM
    preferred and synonym rows are preserved as current observations only.
  target_ids:
  - CultureMech:006195
  evidence_ids:
  - grounding
- assessment_id: a6
  area: provenance
  topic: History and evidence scope
  outcome: concern
  summary: Current source bytes, complete histories and scoped historical reports
    were read. Missing claim-level linkage and any malformed historical metadata are
    distinguished from authenticated source bytes; originals remain append-only.
  target_ids:
  - CultureMech:006195
  evidence_ids:
  - history
  - scalars
- assessment_id: a7
  area: scope
  topic: Growth and taxonomic evidence
  outcome: unknown
  summary: Generic cultivation applications and bacterial filing are not strain-level
    growth evidence. No organism-specific growth, temperature or atmosphere is inferred
    from names or source catalog identifiers.
  target_ids:
  - CultureMech:006195
  evidence_ids:
  - local-target
- assessment_id: a8
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:006195
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-006195-retain-preparation-and-reconcile-the-aerobic-flag
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Retain preparation and reconcile the aerobic flag
  description: 'Selected and KOMODO notes say Aerobic: Yes while the primary uses
    an anoxic preparation. Both omit the full preparation paragraph already retained
    by the DSM owner. Preserve BD Difco specificity, the sodium-resazurin stock input
    and the distinct late-stock stages; the four latter stock strengths and addition
    volumes are not supplied.'
  target_ids:
  - CultureMech:006195
  field_paths:
  - notes
  - preparation_steps
  - solutions
  - data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml::notes
  - data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml::preparation_steps
  evidence_ids:
  - dsm648
  - api648
  - owner-2
  - writer-resolver
  - writer-formulation
  - quantities
  rule_id: custom-source-atmosphere-and-retention
  native_severity: P2
  normalization_reason: 'Major: explicit atmosphere metadata conflicts with the primary
    source and complete staged preparation is absent from the generated/KOMODO views;
    the repaired DSM owner is credited.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-006195-resolve-the-sodium-resazurin-supplied-form
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Resolve the sodium-resazurin supplied form
  description: The source specifies sodium resazurin, but valid CHEBI8806 denotes
    neutral Resazurin with no sodium in its formula. Current MIM maps the sodium synonym
    to that neutral term; that catalog entry cannot settle the supplied-form mismatch.
    Other current named chemical forms and labels match the inspected authority objects.
  target_ids:
  - CultureMech:006195
  field_paths:
  - ingredients[1].term
  evidence_ids:
  - dsm648
  - api648
  - chebi8806
  - grounding
  rule_id: custom-supplied-form-grounding
  native_severity: P2
  normalization_reason: 'Major: the existing identifier is valid but denotes a different
    supplied salt form; native P2.2 invalid-ID wording does not apply.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-006195-preserve-authenticated-owner-evidence-during-regeneration
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Preserve authenticated owner evidence during regeneration
  description: The DSM owner already has four exact attached quantity claims and a
    source reference. The generated target and KOMODO owner lack those links. Current
    formulation-aware merging rejects incompatible preparation metadata; do not bypass
    that guard merely to union evidence. The two remaining ingredient quantities are
    supported by fresh primary/provider evidence and need linkage rather than numeric
    changes.
  target_ids:
  - CultureMech:006195
  field_paths:
  - ingredients[0].evidence
  - ingredients[1].evidence
  - ingredients[2].evidence
  - ingredients[3].evidence
  - ingredients[4].evidence
  - ingredients[5].evidence
  - references
  evidence_ids:
  - owner-2
  - attached-evidence-joins
  - dsm648
  - api648
  - writer-formulation
  rule_id: P4.3
  native_severity: P4
  normalization_reason: 'Normalized minor: missing citations/evidence retention are
    bounded provenance defects while all six generic numeric amounts are positively
    supported; this does not allege a new formulation error.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f4
  issue_key: culturemech-006195-preserve-and-qualify-historical-event-metadata
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Preserve and qualify historical event metadata
  description: KOMODO import events contain a literal .fZ timestamp and resolver events
    omit a UTC offset. Historical concentration reports preserve unresolved claims
    and exact source mappings, but are not independent proof of those historical retrieval
    events. The four DSM-owner attached claims are already authenticated and must
    not be erased when adding fresh context.
  target_ids:
  - CultureMech:006195
  field_paths:
  - data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml::curation_history[0].timestamp
  - data/merge_yaml/merged/CLOSTRIDIUM_GRANTII_MEDIUM.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml::curation_history[1].timestamp
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
    path: data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Reconcile the inaccurate aerobic flag with exact primary evidence,
    retain the existing DSM-owner preparation and named commercial mixture, and restore
    source solution context. Keep unspecified stock strengths unknown. Regenerate
    only after current contributor formulations are compatible.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006195
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Resolve the exact sodium-salt identifier and canonical label using
    authority evidence before replacing the term. Retain the verified final amount
    and source stock strength/dose; do not import a neutral-form molecular weight.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006195
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Retain all four authenticated DSM-owner claims unchanged, add scoped
    evidence for the remaining supported quantities and preparation, and preserve
    their links after compatible regeneration. Keep actual old retrieval events distinct
    from this new capture.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006195
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml
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
  - CultureMech:006195
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- The exact KOMODO648 accession and catalogue routes returned403. Historical mapping
  rows support derivative context but do not complete current accession verification.
- The separate DSM115762 pH override is excluded from the generic formulation review;
  no organism or strain-level growth claim is inferred or proposed.
- Late glucose/cysteine/sulfide/carbonate stock strengths and added volumes are not
  stated. The primary explicit final volume supports generic main amounts, not invented
  stock recipes.
- The neutral-resazurin mismatch is established, but no sodium-salt replacement identifier
  is guessed.
- Current code behavior and freshly matching raw bytes do not prove historical writer
  execution or retrieval timestamps. Original curation events must remain append-only.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
