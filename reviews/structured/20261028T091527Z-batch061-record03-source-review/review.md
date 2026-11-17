# CHITINIVIBRIO: separate source variants and restore nested stock stages

- Review: 20261028T091527Z-batch061-record03-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T08:33:32.887567Z
- Finished UTC: 2026-10-28T09:15:27.470495Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The target identifies DSM 1464 but contains the carbonate/bicarbonate pair from DSM 1465. Both maintained variants already preserve their distinct main amounts and chitin grounding. Eighteen stock components remain flattened in all three records, preparation lacks stage scope, and the provider sodium-sulfide mass conversion conflicts with the primary molarity and current chemical mass. Preserve supported main claims and exact source alternatives while resolving supplied nickel form and missing evidence.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch061 native selection index 03.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000930 | data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml | generated | chitinivibrio_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000930 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:000930 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:000930 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:000930 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Distinct1464 and1465 concentration variants

identity: concern. Targets: CultureMech:000930.

The selected stable ID/source is DSM 1464. Two maintained contributors explicitly carry reciprocal CONCENTRATION_VARIANT links and distinct15/95 versus8/22 bicarbonate/carbonate values. These relationships are supported; they do not authorize one canonical mixture of the two source identities. Complex/undefined liquid state is supported.

### Preserve nested stages and already retained values

completeness: concern. Targets: CultureMech:000930.

All 81 local concentration fields and every source-only solvent/dose/stock condition are assessed. Main rates, conditional chitin midpoint and retained main preparation receive source-specific credit. Both stocks and three vitamin subsolutions need representation; existing stock preparation must be relocated, not discarded.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:000930.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "NaHCO3 variant-specific main amount", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 15,\n                        \"unit\": \"g/l\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 178.557,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "NaHCO3", "compound_id": 55, "amount": 15, "unit": "g/l", "g_l": 15, "mmol_l": 178.557, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 8,\n                        \"unit\": \"g\",\n                        \"g_l\": 8,\n                        \"mmol_l\": 95.2302,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "NaHCO3", "compound_id": 55, "amount": 8, "unit": "g", "g_l": 8, "mmol_l": 95.2302, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "DSM1464 explicitly supplies15 and95 g/L for bicarbonate/carbonate; DSM1465 PDF instead gives8 and22 g batch amounts, with corresponding explicit provider g_l. The target identity is1464 but its first two values are from1465. Both owners already preserve their own values and relationship; do not overwrite the child to match the parent.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "8", "unit": "G_PER_L"}, "decision": "correct", "rationale": "DSM1464 explicitly supplies15 and95 g/L for bicarbonate/carbonate; DSM1465 PDF instead gives8 and22 g batch amounts, with corresponding explicit provider g_l. The target identity is1464 but its first two values are from1465. Both owners already preserve their own values and relationship; do not overwrite the child to match the parent."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "15", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "DSM1464 explicitly supplies15 and95 g/L for bicarbonate/carbonate; DSM1465 PDF instead gives8 and22 g batch amounts, with corresponding explicit provider g_l. The target identity is1464 but its first two values are from1465. Both owners already preserve their own values and relationship; do not overwrite the child to match the parent."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "8", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "DSM1464 explicitly supplies15 and95 g/L for bicarbonate/carbonate; DSM1465 PDF instead gives8 and22 g batch amounts, with corresponding explicit provider g_l. The target identity is1464 but its first two values are from1465. Both owners already preserve their own values and relationship; do not overwrite the child to match the parent."}]}, {"quantity_id": "q2", "topic": "Na2CO3 variant-specific main amount", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 95,\n                        \"unit\": \"g/l\",\n                        \"g_l\": 95,\n                        \"mmol_l\": 896.328,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Na2CO3", "compound_id": 32, "amount": 95, "unit": "g/l", "g_l": 95, "mmol_l": 896.328, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 22,\n                        \"unit\": \"g\",\n                        \"g_l\": 22,\n                        \"mmol_l\": 207.571,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Na2CO3", "compound_id": 32, "amount": 22, "unit": "g", "g_l": 22, "mmol_l": 207.571, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "DSM1464 explicitly supplies15 and95 g/L for bicarbonate/carbonate; DSM1465 PDF instead gives8 and22 g batch amounts, with corresponding explicit provider g_l. The target identity is1464 but its first two values are from1465. Both owners already preserve their own values and relationship; do not overwrite the child to match the parent.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "22", "unit": "G_PER_L"}, "decision": "correct", "rationale": "DSM1464 explicitly supplies15 and95 g/L for bicarbonate/carbonate; DSM1465 PDF instead gives8 and22 g batch amounts, with corresponding explicit provider g_l. The target identity is1464 but its first two values are from1465. Both owners already preserve their own values and relationship; do not overwrite the child to match the parent."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "95", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "DSM1464 explicitly supplies15 and95 g/L for bicarbonate/carbonate; DSM1465 PDF instead gives8 and22 g batch amounts, with corresponding explicit provider g_l. The target identity is1464 but its first two values are from1465. Both owners already preserve their own values and relationship; do not overwrite the child to match the parent."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "22", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "DSM1464 explicitly supplies15 and95 g/L for bicarbonate/carbonate; DSM1465 PDF instead gives8 and22 g batch amounts, with corresponding explicit provider g_l. The target identity is1464 but its first two values are from1465. Both owners already preserve their own values and relationship; do not overwrite the child to match the parent."}]}, {"quantity_id": "q3", "topic": "NaCl variant-specific main amount", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 6,\n                        \"unit\": \"g/l\",\n                        \"g_l\": 6,\n                        \"mmol_l\": 102.669,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "NaCl", "compound_id": 43, "amount": 6, "unit": "g/l", "g_l": 6, "mmol_l": 102.669, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 6,\n                        \"unit\": \"g\",\n                        \"g_l\": 6,\n                        \"mmol_l\": 102.669,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "NaCl", "compound_id": 43, "amount": 6, "unit": "g", "g_l": 6, "mmol_l": 102.669, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "This main-stage amount agrees in both variants. DSM1464 PDF explicitly uses g/L; DSM1465 PDF uses batch g and its API separately declares the local g_l. Preserve that source-basis distinction without deriving a physical final volume from water.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "6", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "This main-stage amount agrees in both variants. DSM1464 PDF explicitly uses g/L; DSM1465 PDF uses batch g and its API separately declares the local g_l. Preserve that source-basis distinction without deriving a physical final volume from water."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "6", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "This main-stage amount agrees in both variants. DSM1464 PDF explicitly uses g/L; DSM1465 PDF uses batch g and its API separately declares the local g_l. Preserve that source-basis distinction without deriving a physical final volume from water."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "6", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "This main-stage amount agrees in both variants. DSM1464 PDF explicitly uses g/L; DSM1465 PDF uses batch g and its API separately declares the local g_l. Preserve that source-basis distinction without deriving a physical final volume from water."}]}, {"quantity_id": "q4", "topic": "K2HPO4 variant-specific main amount", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 1,\n                        \"unit\": \"g/l\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.74132,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "K2HPO4", "compound_id": 10, "amount": 1, "unit": "g/l", "g_l": 1, "mmol_l": 5.74132, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.74132,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "K2HPO4", "compound_id": 10, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 5.74132, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "This main-stage amount agrees in both variants. DSM1464 PDF explicitly uses g/L; DSM1465 PDF uses batch g and its API separately declares the local g_l. Preserve that source-basis distinction without deriving a physical final volume from water.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "This main-stage amount agrees in both variants. DSM1464 PDF explicitly uses g/L; DSM1465 PDF uses batch g and its API separately declares the local g_l. Preserve that source-basis distinction without deriving a physical final volume from water."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "This main-stage amount agrees in both variants. DSM1464 PDF explicitly uses g/L; DSM1465 PDF uses batch g and its API separately declares the local g_l. Preserve that source-basis distinction without deriving a physical final volume from water."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "This main-stage amount agrees in both variants. DSM1464 PDF explicitly uses g/L; DSM1465 PDF uses batch g and its API separately declares the local g_l. Preserve that source-basis distinction without deriving a physical final volume from water."}]}, {"quantity_id": "q5", "topic": "Chitin range and conditional provider midpoint", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Chitin\",\n                        \"compound_id\": 2138,\n                        \"condition\": \"adjust volume in range 1-2 if required\",\n                        \"attribute\": \"amorphous or Sigma C7170, 5% solution\",\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "Chitin", "compound_id": 2138, "condition": "adjust volume in range 1-2 if required", "attribute": "amorphous or Sigma C7170, 5% solution", "amount": 1.5, "unit": "g", "g_l": 1.5, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Chitin\",\n                        \"compound_id\": 2138,\n                        \"condition\": \"adjust in range 1 - 2 g/l if required\",\n                        \"attribute\": \"amorphous, from 5% solution\",\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "Chitin", "compound_id": 2138, "condition": "adjust in range 1 - 2 g/l if required", "attribute": "amorphous, from 5% solution", "amount": 1.5, "unit": "g", "g_l": 1.5, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1464", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1464.bin", "raw_sha256": "1a27d397090c1d2eb31c7c6835bc79f094c2fa88010ceb3a900b8b08e8a8f46a", "locator": "Page1 post-autoclave additions", "accessed_at": "2026-10-28T08:34:40.751275Z", "quote": "1 – 2g/l (from 5% solution)"}], "decision": "mixed", "rationale": "Both PDFs specify a chitin range1–2 g/L from a bare5% solution; the APIs supply conditional midpoint1.5 g/L. The local1.5 plus range note can be retained only as that provider-selected point, not as a fixed primary prescription. The DSM1464 owner note says adjust volume without units and must instead preserve the explicit concentration range; no5% mass/volume basis or stock volume is assumed.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Both PDFs specify a chitin range1–2 g/L from a bare5% solution; the APIs supply conditional midpoint1.5 g/L. The local1.5 plus range note can be retained only as that provider-selected point, not as a fixed primary prescription. The DSM1464 owner note says adjust volume without units and must instead preserve the explicit concentration range; no5% mass/volume basis or stock volume is assumed."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Both PDFs specify a chitin range1–2 g/L from a bare5% solution; the APIs supply conditional midpoint1.5 g/L. The local1.5 plus range note can be retained only as that provider-selected point, not as a fixed primary prescription. The DSM1464 owner note says adjust volume without units and must instead preserve the explicit concentration range; no5% mass/volume basis or stock volume is assumed."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Both PDFs specify a chitin range1–2 g/L from a bare5% solution; the APIs supply conditional midpoint1.5 g/L. The local1.5 plus range note can be retained only as that provider-selected point, not as a fixed primary prescription. The DSM1464 owner note says adjust volume without units and must instead preserve the explicit concentration range; no5% mass/volume basis or stock volume is assumed."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[4].notes", "stored_value": " (adjust volume in range 1-2 if required)", "decision": "correct", "rationale": "Both PDFs specify a chitin range1–2 g/L from a bare5% solution; the APIs supply conditional midpoint1.5 g/L. The local1.5 plus range note can be retained only as that provider-selected point, not as a fixed primary prescription. The DSM1464 owner note says adjust volume without units and must instead preserve the explicit concentration range; no5% mass/volume basis or stock volume is assumed."}]}, {"quantity_id": "q6", "topic": "MgSO4 main final concentration", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"MgSO4\",\n                        \"compound_id\": 325,\n                        \"amount\": 1,\n                        \"unit\": \"mM\",\n                        \"g_l\": 0.12037,\n                        \"mmol_l\": 1,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "MgSO4", "compound_id": 325, "amount": 1, "unit": "mM", "g_l": 0.12037, "mmol_l": 1, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"MgSO4\",\n                        \"compound_id\": 325,\n                        \"amount\": 1,\n                        \"unit\": \"mM\",\n                        \"g_l\": 0.12037,\n                        \"mmol_l\": 1,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "MgSO4", "compound_id": 325, "amount": 1, "unit": "mM", "g_l": 0.12037, "mmol_l": 1, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The primary explicitly prescribes final1 mM MgSO4. Current anhydrous CHEBI32599 mass120.368 gives0.120368 g/L, consistent with the provider0.12037 rounding. Preserve native molarity and supplied anhydrous identity; do not transfer a hydrate mass.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.12037", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly prescribes final1 mM MgSO4. Current anhydrous CHEBI32599 mass120.368 gives0.120368 g/L, consistent with the provider0.12037 rounding. Preserve native molarity and supplied anhydrous identity; do not transfer a hydrate mass."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.12037", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly prescribes final1 mM MgSO4. Current anhydrous CHEBI32599 mass120.368 gives0.120368 g/L, consistent with the provider0.12037 rounding. Preserve native molarity and supplied anhydrous identity; do not transfer a hydrate mass."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.12037", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly prescribes final1 mM MgSO4. Current anhydrous CHEBI32599 mass120.368 gives0.120368 g/L, consistent with the provider0.12037 rounding. Preserve native molarity and supplied anhydrous identity; do not transfer a hydrate mass."}]}, {"quantity_id": "q7", "topic": "Yeast extract main final concentration", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "Yeast extract", "compound_id": 16, "amount": 20, "unit": "mg", "g_l": 0.02, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "Yeast extract", "compound_id": 16, "amount": 20, "unit": "mg", "g_l": 0.02, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Primary20 mg/L equals0.02 g/L directly; both provider declarations and all current local values agree. No new chemical identifier or strain growth inference is required.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Primary20 mg/L equals0.02 g/L directly; both provider declarations and all current local values agree. No new chemical identifier or strain growth inference is required."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Primary20 mg/L equals0.02 g/L directly; both provider declarations and all current local values agree. No new chemical identifier or strain growth inference is required."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Primary20 mg/L equals0.02 g/L directly; both provider declarations and all current local values agree. No new chemical identifier or strain growth inference is required."}]}, {"quantity_id": "q8", "topic": "NH4Cl main final concentration", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 4,\n                        \"unit\": \"mM\",\n                        \"g_l\": 0.21396,\n                        \"mmol_l\": 4,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "NH4Cl", "compound_id": 42, "amount": 4, "unit": "mM", "g_l": 0.21396, "mmol_l": 4, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 4,\n                        \"unit\": \"mM\",\n                        \"g_l\": 0.21396,\n                        \"mmol_l\": 4,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "NH4Cl", "compound_id": 42, "amount": 4, "unit": "mM", "g_l": 0.21396, "mmol_l": 4, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The primary explicitly prescribes final4 mM NH4Cl; current CHEBI31206 mass53.492 gives0.213968 g/L. The provider0.21396 is a nearby source-rounded mass conversion, retained as declared provider precision rather than claiming identical atomic-weight precision.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.21396", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly prescribes final4 mM NH4Cl; current CHEBI31206 mass53.492 gives0.213968 g/L. The provider0.21396 is a nearby source-rounded mass conversion, retained as declared provider precision rather than claiming identical atomic-weight precision."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.21396", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly prescribes final4 mM NH4Cl; current CHEBI31206 mass53.492 gives0.213968 g/L. The provider0.21396 is a nearby source-rounded mass conversion, retained as declared provider precision rather than claiming identical atomic-weight precision."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.21396", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly prescribes final4 mM NH4Cl; current CHEBI31206 mass53.492 gives0.213968 g/L. The provider0.21396 is a nearby source-rounded mass conversion, retained as declared provider precision rather than claiming identical atomic-weight precision."}]}, {"quantity_id": "q9", "topic": "Na2S main final concentration", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Na2S\",\n                        \"compound_id\": 490,\n                        \"amount\": 1,\n                        \"unit\": \"mM\",\n                        \"g_l\": 0.07906,\n                        \"mmol_l\": 1,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "Na2S", "compound_id": 490, "amount": 1, "unit": "mM", "g_l": 0.07906, "mmol_l": 1, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Na2S\",\n                        \"compound_id\": 490,\n                        \"amount\": 1,\n                        \"unit\": \"mM\",\n                        \"g_l\": 0.07906,\n                        \"mmol_l\": 1,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "Na2S", "compound_id": 490, "amount": 1, "unit": "mM", "g_l": 0.07906, "mmol_l": 1, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "conflict", "rationale": "The primary explicitly prescribes final1 mM Na2S. Both APIs declare0.07906 g/L, but the current exact anhydrous CHEBI76208 formula2Na.S and mass78.047 imply0.078047 g/L at1 mM. Preserve the contradictory provider number as evidence; prefer the explicitly supplied native molarity pending conversion reconciliation, without inventing a hydrate or silently endorsing the mass value.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.07906", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary explicitly prescribes final1 mM Na2S. Both APIs declare0.07906 g/L, but the current exact anhydrous CHEBI76208 formula2Na.S and mass78.047 imply0.078047 g/L at1 mM. Preserve the contradictory provider number as evidence; prefer the explicitly supplied native molarity pending conversion reconciliation, without inventing a hydrate or silently endorsing the mass value."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.07906", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary explicitly prescribes final1 mM Na2S. Both APIs declare0.07906 g/L, but the current exact anhydrous CHEBI76208 formula2Na.S and mass78.047 imply0.078047 g/L at1 mM. Preserve the contradictory provider number as evidence; prefer the explicitly supplied native molarity pending conversion reconciliation, without inventing a hydrate or silently endorsing the mass value."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.07906", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary explicitly prescribes final1 mM Na2S. Both APIs declare0.07906 g/L, but the current exact anhydrous CHEBI76208 formula2Na.S and mass78.047 imply0.078047 g/L at1 mM. Preserve the contradictory provider number as evidence; prefer the explicitly supplied native molarity pending conversion reconciliation, without inventing a hydrate or silently endorsing the mass value."}]}, {"quantity_id": "q10", "topic": "Biotin in Basic solution (100 ml 0.1 N NaOH)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Biotin", "compound_id": 46, "amount": 2, "unit": "mg", "g_l": 0.02, "mmol_l": 0.0818632, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[3].recipe[0]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Biotin", "compound_id": 46, "amount": 2, "unit": "mg", "g_l": 0.02, "mmol_l": 0.0818632, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 2 mg and provider stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 2 mg and provider stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 2 mg and provider stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 2 mg and provider stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}]}, {"quantity_id": "q11", "topic": "PABA in Basic solution (100 ml 0.1 N NaOH)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[2].recipe[1]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"PABA\",\n                        \"compound_id\": 1309,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "PABA", "compound_id": 1309, "amount": 5, "unit": "mg", "g_l": 0.05, "mmol_l": 0.364591, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[3].recipe[1]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"PABA\",\n                        \"compound_id\": 1309,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "PABA", "compound_id": 1309, "amount": 5, "unit": "mg", "g_l": 0.05, "mmol_l": 0.364591, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}]}, {"quantity_id": "q12", "topic": "Nicotinic acid in Basic solution (100 ml 0.1 N NaOH)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[2].recipe[2]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "Nicotinic acid", "compound_id": 139, "amount": 5, "unit": "mg", "g_l": 0.05, "mmol_l": 0.406141, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[3].recipe[2]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "Nicotinic acid", "compound_id": 139, "amount": 5, "unit": "mg", "g_l": 0.05, "mmol_l": 0.406141, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}]}, {"quantity_id": "q13", "topic": "Pyridoxine in Basic solution (100 ml 0.1 N NaOH)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[2].recipe[3]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Pyridoxine\",\n                        \"compound_id\": 637,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.591086,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "Pyridoxine", "compound_id": 637, "amount": 10, "unit": "mg", "g_l": 0.1, "mmol_l": 0.591086, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[3].recipe[3]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Pyridoxine\",\n                        \"compound_id\": 637,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.591086,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "Pyridoxine", "compound_id": 637, "amount": 10, "unit": "mg", "g_l": 0.1, "mmol_l": 0.591086, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 10 mg and provider stock g_l=0.1; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 10 mg and provider stock g_l=0.1; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 10 mg and provider stock g_l=0.1; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 10 mg and provider stock g_l=0.1; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}]}, {"quantity_id": "q14", "topic": "Folic acid in Neutral solution (100 ml Aqua dem.)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[3].recipe[0]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Folic acid", "compound_id": 138, "amount": 2, "unit": "mg", "g_l": 0.02, "mmol_l": 0.0453104, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[4].recipe[0]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Folic acid", "compound_id": 138, "amount": 2, "unit": "mg", "g_l": 0.02, "mmol_l": 0.0453104, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Neutral solution (100 ml Aqua dem.) composition, with source amount 2 mg and provider stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Neutral solution (100 ml Aqua dem.) composition, with source amount 2 mg and provider stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Neutral solution (100 ml Aqua dem.) composition, with source amount 2 mg and provider stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Neutral solution (100 ml Aqua dem.) composition, with source amount 2 mg and provider stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}]}, {"quantity_id": "q15", "topic": "Riboflavin in Neutral solution (100 ml Aqua dem.)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[3].recipe[1]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Riboflavin", "compound_id": 136, "amount": 5, "unit": "mg", "g_l": 0.05, "mmol_l": 0.132837, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[4].recipe[1]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Riboflavin", "compound_id": 136, "amount": 5, "unit": "mg", "g_l": 0.05, "mmol_l": 0.132837, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Neutral solution (100 ml Aqua dem.) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Neutral solution (100 ml Aqua dem.) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Neutral solution (100 ml Aqua dem.) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Neutral solution (100 ml Aqua dem.) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}]}, {"quantity_id": "q16", "topic": "EDTA in Acidic trace metals (Pfennig &amp; Lippert, 1965)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[4].recipe[0]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"EDTA\",\n                        \"compound_id\": 271,\n                        \"amount\": 5,\n                        \"unit\": \"g/l\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 17.1092,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "EDTA", "compound_id": 271, "amount": 5, "unit": "g/l", "g_l": 5, "mmol_l": 17.1092, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[5].recipe[0]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"EDTA\",\n                        \"compound_id\": 271,\n                        \"amount\": 5,\n                        \"unit\": \"g/l\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 17.1092,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "EDTA", "compound_id": 271, "amount": 5, "unit": "g/l", "g_l": 5, "mmol_l": 17.1092, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 5 g/l and provider stock g_l=5; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 5 g/l and provider stock g_l=5; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 5 g/l and provider stock g_l=5; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 5 g/l and provider stock g_l=5; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}]}, {"quantity_id": "q17", "topic": "FeSO4 x 7 H2O in Acidic trace metals (Pfennig &amp; Lippert, 1965)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[4].recipe[1]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 2,\n                        \"unit\": \"g/l\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 7.19386,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "FeSO4 x 7 H2O", "compound_id": 12, "amount": 2, "unit": "g/l", "g_l": 2, "mmol_l": 7.19386, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[5].recipe[1]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 2,\n                        \"unit\": \"g/l\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 7.19386,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "FeSO4 x 7 H2O", "compound_id": 12, "amount": 2, "unit": "g/l", "g_l": 2, "mmol_l": 7.19386, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 2 g/l and provider stock g_l=2; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 2 g/l and provider stock g_l=2; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 2 g/l and provider stock g_l=2; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 2 g/l and provider stock g_l=2; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}]}, {"quantity_id": "q18", "topic": "ZnSO4 x 7 H2O in Acidic trace metals (Pfennig &amp; Lippert, 1965)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[4].recipe[2]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 100,\n                        \"unit\": \"mg/l\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "ZnSO4 x 7 H2O", "compound_id": 35, "amount": 100, "unit": "mg/l", "g_l": 0.1, "mmol_l": 0.347752, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[5].recipe[2]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 100,\n                        \"unit\": \"mg/l\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "ZnSO4 x 7 H2O", "compound_id": 35, "amount": 100, "unit": "mg/l", "g_l": 0.1, "mmol_l": 0.347752, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 100 mg/l and provider stock g_l=0.1; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 100 mg/l and provider stock g_l=0.1; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 100 mg/l and provider stock g_l=0.1; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 100 mg/l and provider stock g_l=0.1; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}]}, {"quantity_id": "q19", "topic": "MnCl2 in Acidic trace metals (Pfennig &amp; Lippert, 1965)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[4].recipe[3]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2\",\n                        \"compound_id\": 980,\n                        \"amount\": 30,\n                        \"unit\": \"mg/l\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.238398,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "MnCl2", "compound_id": 980, "amount": 30, "unit": "mg/l", "g_l": 0.03, "mmol_l": 0.238398, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[5].recipe[3]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2\",\n                        \"compound_id\": 980,\n                        \"amount\": 30,\n                        \"unit\": \"mg/l\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.238398,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "MnCl2", "compound_id": 980, "amount": 30, "unit": "mg/l", "g_l": 0.03, "mmol_l": 0.238398, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 30 mg/l and provider stock g_l=0.03; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 30 mg/l and provider stock g_l=0.03; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 30 mg/l and provider stock g_l=0.03; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 30 mg/l and provider stock g_l=0.03; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}]}, {"quantity_id": "q20", "topic": "H3BO3 in Acidic trace metals (Pfennig &amp; Lippert, 1965)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[4].recipe[4]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 300,\n                        \"unit\": \"mg/l\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "H3BO3", "compound_id": 37, "amount": 300, "unit": "mg/l", "g_l": 0.3, "mmol_l": 4.85123, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[5].recipe[4]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 300,\n                        \"unit\": \"mg/l\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "H3BO3", "compound_id": 37, "amount": 300, "unit": "mg/l", "g_l": 0.3, "mmol_l": 4.85123, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 300 mg/l and provider stock g_l=0.3; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 300 mg/l and provider stock g_l=0.3; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 300 mg/l and provider stock g_l=0.3; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 300 mg/l and provider stock g_l=0.3; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}]}, {"quantity_id": "q21", "topic": "CoCl2 x 6 H2O in Acidic trace metals (Pfennig &amp; Lippert, 1965)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[4].recipe[5]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 200,\n                        \"unit\": \"mg/l\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "CoCl2 x 6 H2O", "compound_id": 38, "amount": 200, "unit": "mg/l", "g_l": 0.2, "mmol_l": 1.54037, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[5].recipe[5]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 200,\n                        \"unit\": \"mg/l\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "CoCl2 x 6 H2O", "compound_id": 38, "amount": 200, "unit": "mg/l", "g_l": 0.2, "mmol_l": 1.54037, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 200 mg/l and provider stock g_l=0.2; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 200 mg/l and provider stock g_l=0.2; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 200 mg/l and provider stock g_l=0.2; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 200 mg/l and provider stock g_l=0.2; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}]}, {"quantity_id": "q22", "topic": "CuCl2 in Acidic trace metals (Pfennig &amp; Lippert, 1965)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[4].recipe[6]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2\",\n                        \"compound_id\": 261,\n                        \"amount\": 10,\n                        \"unit\": \"mg/l\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0743771,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "CuCl2", "compound_id": 261, "amount": 10, "unit": "mg/l", "g_l": 0.01, "mmol_l": 0.0743771, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[5].recipe[6]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2\",\n                        \"compound_id\": 261,\n                        \"amount\": 10,\n                        \"unit\": \"mg/l\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0743771,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "CuCl2", "compound_id": 261, "amount": 10, "unit": "mg/l", "g_l": 0.01, "mmol_l": 0.0743771, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 10 mg/l and provider stock g_l=0.01; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 10 mg/l and provider stock g_l=0.01; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 10 mg/l and provider stock g_l=0.01; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 10 mg/l and provider stock g_l=0.01; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock."}]}, {"quantity_id": "q23", "topic": "NiCl2 x 2 H2O in Acidic trace metals (Pfennig &amp; Lippert, 1965)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[4].recipe[7]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 2 H2O\",\n                        \"compound_id\": 981,\n                        \"amount\": 20,\n                        \"unit\": \"mg/l\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "NiCl2 x 2 H2O", "compound_id": 981, "amount": 20, "unit": "mg/l", "g_l": 0.02, "mmol_l": 0.154322, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[5].recipe[7]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 2 H2O\",\n                        \"compound_id\": 981,\n                        \"amount\": 20,\n                        \"unit\": \"mg/l\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "NiCl2 x 2 H2O", "compound_id": 981, "amount": 20, "unit": "mg/l", "g_l": 0.02, "mmol_l": 0.154322, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 20 mg/l and provider stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock. The supplied dihydrate conflicts with the anhydrous34887 identifier; do not substitute hexahydrate.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 20 mg/l and provider stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock. The supplied dihydrate conflicts with the anhydrous34887 identifier; do not substitute hexahydrate."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 20 mg/l and provider stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock. The supplied dihydrate conflicts with the anhydrous34887 identifier; do not substitute hexahydrate."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 20 mg/l and provider stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock. The supplied dihydrate conflicts with the anhydrous34887 identifier; do not substitute hexahydrate."}]}, {"quantity_id": "q24", "topic": "Na2MoO4 x 2 H2O in Acidic trace metals (Pfennig &amp; Lippert, 1965)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[4].recipe[8]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 20,\n                        \"unit\": \"mg/l\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0826617,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 20, "unit": "mg/l", "g_l": 0.02, "mmol_l": 0.0826617, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[5].recipe[8]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 20,\n                        \"unit\": \"mg/l\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0826617,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 20, "unit": "mg/l", "g_l": 0.02, "mmol_l": 0.0826617, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 20 mg/l and provider stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock. The primary alternative printed as NH4MoO4 remains a separate unresolved source alternative; no chemical formula correction is invented.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 20 mg/l and provider stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock. The primary alternative printed as NH4MoO4 remains a separate unresolved source alternative; no chemical formula correction is invented."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 20 mg/l and provider stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock. The primary alternative printed as NH4MoO4 remains a separate unresolved source alternative; no chemical formula correction is invented."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig &amp; Lippert, 1965) composition, with source amount 20 mg/l and provider stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions belong only to this stock. The primary alternative printed as NH4MoO4 remains a separate unresolved source alternative; no chemical formula correction is invented."}]}, {"quantity_id": "q25", "topic": "Thiamin in Acidic solution (HCl, pH 3; 100 ml)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[5].recipe[0]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Thiamin\",\n                        \"compound_id\": 1307,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.188423,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Thiamin", "compound_id": 1307, "amount": 5, "unit": "mg", "g_l": 0.05, "mmol_l": 0.188423, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Thiamin\",\n                        \"compound_id\": 1307,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.188423,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Thiamin", "compound_id": 1307, "amount": 5, "unit": "mg", "g_l": 0.05, "mmol_l": 0.188423, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Acidic solution (HCl, pH 3; 100 ml) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic solution (HCl, pH 3; 100 ml) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic solution (HCl, pH 3; 100 ml) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic solution (HCl, pH 3; 100 ml) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}]}, {"quantity_id": "q26", "topic": "Calcium pantothenate in Acidic solution (HCl, pH 3; 100 ml)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[5].recipe[1]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.104925,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Calcium pantothenate", "compound_id": 518, "amount": 5, "unit": "mg", "g_l": 0.05, "mmol_l": 0.104925, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[2].recipe[1]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.104925,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Calcium pantothenate", "compound_id": 518, "amount": 5, "unit": "mg", "g_l": 0.05, "mmol_l": 0.104925, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Acidic solution (HCl, pH 3; 100 ml) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries. Source calcium pantothenate does not independently establish the stereochemistry encoded by31345.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic solution (HCl, pH 3; 100 ml) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries. Source calcium pantothenate does not independently establish the stereochemistry encoded by31345."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic solution (HCl, pH 3; 100 ml) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries. Source calcium pantothenate does not independently establish the stereochemistry encoded by31345."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic solution (HCl, pH 3; 100 ml) composition, with source amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries. Source calcium pantothenate does not independently establish the stereochemistry encoded by31345."}]}, {"quantity_id": "q27", "topic": "B12 in Acidic solution (HCl, pH 3; 100 ml)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[5].recipe[2]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"B12\",\n                        \"compound_id\": 1238,\n                        \"amount\": 0.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.00368895,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "B12", "compound_id": 1238, "amount": 0.5, "unit": "mg", "g_l": 0.005, "mmol_l": 0.00368895, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[2].recipe[2]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"B12\",\n                        \"compound_id\": 1238,\n                        \"amount\": 0.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.00368895,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "B12", "compound_id": 1238, "amount": 0.5, "unit": "mg", "g_l": 0.005, "mmol_l": 0.00368895, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This is Acidic solution (HCl, pH 3; 100 ml) composition, with source amount 0.5 mg and provider stock g_l=0.005; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic solution (HCl, pH 3; 100 ml) composition, with source amount 0.5 mg and provider stock g_l=0.005; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic solution (HCl, pH 3; 100 ml) composition, with source amount 0.5 mg and provider stock g_l=0.005; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic solution (HCl, pH 3; 100 ml) composition, with source amount 0.5 mg and provider stock g_l=0.005; all local values reproduce that stock rate as a direct ingredient. Relocate it to this exact stock stage, retaining source amount and form. The primary specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both successive mixing/addition boundaries."}]}, {"quantity_id": "q28", "topic": "Receiving dose 5701", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[0].recipe[10]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 11,\n                        \"solution\": \"Vitamine mixture (Pfennig &amp; Lippert, 1965)\",\n                        \"solution_id\": 5701,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 11, "solution": "Vitamine mixture (Pfennig &amp; Lippert, 1965)", "solution_id": 5701, "amount": 1, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[0].recipe[11]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Vitamine mixture (Pfennig &amp; Lippert, 1965)\",\n                        \"solution_id\": 5701,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 12, "solution": "Vitamine mixture (Pfennig &amp; Lippert, 1965)", "solution_id": 5701, "amount": 1, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1464", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1464.bin", "raw_sha256": "1a27d397090c1d2eb31c7c6835bc79f094c2fa88010ceb3a900b8b08e8a8f46a", "locator": "Primary main-medium table; extracted PDF text line 20 (1-based)", "accessed_at": "2026-10-28T08:34:40.751275Z", "quote": " Vitamine mixture (Pfennig &amp; Lippert, 1965)             1         ml/l"}, {"evidence_id": "dsm1465", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1465.bin", "raw_sha256": "61633d2fad4085c3cd67f6f55f7be13067816f10c93104859782df1da7cb84f6", "locator": "Primary main-medium table; extracted PDF text line 20 (1-based)", "accessed_at": "2026-10-28T08:34:41.044645Z", "quote": " Vitamine mixture (Pfennig &amp; Lippert, 1965)             1         ml/l"}], "decision": "add", "rationale": "Both primary sources explicitly prescribe1 ml/L of this named stock. All local solutions blocks are absent. Create a scoped stock object and receiving dose; retain the ingredient compositions only inside their proper stock or substock, not as direct receiving-medium values.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Both primary sources explicitly prescribe1 ml/L of this named stock. All local solutions blocks are absent. Create a scoped stock object and receiving dose; retain the ingredient compositions only inside their proper stock or substock, not as direct receiving-medium values.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Both primary sources explicitly prescribe1 ml/L of this named stock. All local solutions blocks are absent. Create a scoped stock object and receiving dose; retain the ingredient compositions only inside their proper stock or substock, not as direct receiving-medium values.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Both primary sources explicitly prescribe1 ml/L of this named stock. All local solutions blocks are absent. Create a scoped stock object and receiving dose; retain the ingredient compositions only inside their proper stock or substock, not as direct receiving-medium values.", "missing": true}]}, {"quantity_id": "q29", "topic": "Receiving dose 5704", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[0].recipe[11]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Acidic trace metals (Pfennig &amp; Lippert, 1965)\",\n                        \"solution_id\": 5704,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 12, "solution": "Acidic trace metals (Pfennig &amp; Lippert, 1965)", "solution_id": 5704, "amount": 1, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[0].recipe[10]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 11,\n                        \"solution\": \"Acidic trace metals (Pfennig &amp; Lippert, 1965)\",\n                        \"solution_id\": 5704,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 11, "solution": "Acidic trace metals (Pfennig &amp; Lippert, 1965)", "solution_id": 5704, "amount": 1, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm1464", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1464.bin", "raw_sha256": "1a27d397090c1d2eb31c7c6835bc79f094c2fa88010ceb3a900b8b08e8a8f46a", "locator": "Primary main-medium table; extracted PDF text line 19 (1-based)", "accessed_at": "2026-10-28T08:34:40.751275Z", "quote": " Acidic trace metals (Pfennig &amp; Lippert, 1965)          1         ml/l"}, {"evidence_id": "dsm1465", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1465.bin", "raw_sha256": "61633d2fad4085c3cd67f6f55f7be13067816f10c93104859782df1da7cb84f6", "locator": "Primary main-medium table; extracted PDF text line 19 (1-based)", "accessed_at": "2026-10-28T08:34:41.044645Z", "quote": " Acidic trace metals (Pfennig &amp; Lippert, 1965)          1         ml/l"}], "decision": "add", "rationale": "Both primary sources explicitly prescribe1 ml/L of this named stock. All local solutions blocks are absent. Create a scoped stock object and receiving dose; retain the ingredient compositions only inside their proper stock or substock, not as direct receiving-medium values.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Both primary sources explicitly prescribe1 ml/L of this named stock. All local solutions blocks are absent. Create a scoped stock object and receiving dose; retain the ingredient compositions only inside their proper stock or substock, not as direct receiving-medium values.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Both primary sources explicitly prescribe1 ml/L of this named stock. All local solutions blocks are absent. Create a scoped stock object and receiving dose; retain the ingredient compositions only inside their proper stock or substock, not as direct receiving-medium values.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Both primary sources explicitly prescribe1 ml/L of this named stock. All local solutions blocks are absent. Create a scoped stock object and receiving dose; retain the ingredient compositions only inside their proper stock or substock, not as direct receiving-medium values.", "missing": true}]}, {"quantity_id": "q30", "topic": "Vitamin mixture aliquot Basic solution (100 ml 0.1 N NaOH)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Basic solution (100 ml 0.1 N NaOH)\",\n                        \"solution_id\": 5702,\n                        \"amount\": 50,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "solution": "Basic solution (100 ml 0.1 N NaOH)", "solution_id": 5702, "amount": 50, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Basic solution (100 ml 0.1 N NaOH)\",\n                        \"solution_id\": 5702,\n                        \"amount\": 50,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "solution": "Basic solution (100 ml 0.1 N NaOH)", "solution_id": 5702, "amount": 50, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "The API vitamin-mixture recipe supplies50 ml of this subsolution, with total provider volume150 ml. The primary instead gives the scale-free1:1:1 volume ratio. Preserve50 ml as the provider realization of that ratio, not a required primary batch size or a100 ml receiving dose.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The API vitamin-mixture recipe supplies50 ml of this subsolution, with total provider volume150 ml. The primary instead gives the scale-free1:1:1 volume ratio. Preserve50 ml as the provider realization of that ratio, not a required primary batch size or a100 ml receiving dose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The API vitamin-mixture recipe supplies50 ml of this subsolution, with total provider volume150 ml. The primary instead gives the scale-free1:1:1 volume ratio. Preserve50 ml as the provider realization of that ratio, not a required primary batch size or a100 ml receiving dose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The API vitamin-mixture recipe supplies50 ml of this subsolution, with total provider volume150 ml. The primary instead gives the scale-free1:1:1 volume ratio. Preserve50 ml as the provider realization of that ratio, not a required primary batch size or a100 ml receiving dose.", "missing": true}]}, {"quantity_id": "q31", "topic": "Vitamin mixture aliquot Neutral solution (100 ml Aqua dem.)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Neutral solution (100 ml Aqua dem.)\",\n                        \"solution_id\": 5703,\n                        \"amount\": 50,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "solution": "Neutral solution (100 ml Aqua dem.)", "solution_id": 5703, "amount": 50, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Neutral solution (100 ml Aqua dem.)\",\n                        \"solution_id\": 5703,\n                        \"amount\": 50,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "solution": "Neutral solution (100 ml Aqua dem.)", "solution_id": 5703, "amount": 50, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "The API vitamin-mixture recipe supplies50 ml of this subsolution, with total provider volume150 ml. The primary instead gives the scale-free1:1:1 volume ratio. Preserve50 ml as the provider realization of that ratio, not a required primary batch size or a100 ml receiving dose.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The API vitamin-mixture recipe supplies50 ml of this subsolution, with total provider volume150 ml. The primary instead gives the scale-free1:1:1 volume ratio. Preserve50 ml as the provider realization of that ratio, not a required primary batch size or a100 ml receiving dose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The API vitamin-mixture recipe supplies50 ml of this subsolution, with total provider volume150 ml. The primary instead gives the scale-free1:1:1 volume ratio. Preserve50 ml as the provider realization of that ratio, not a required primary batch size or a100 ml receiving dose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The API vitamin-mixture recipe supplies50 ml of this subsolution, with total provider volume150 ml. The primary instead gives the scale-free1:1:1 volume ratio. Preserve50 ml as the provider realization of that ratio, not a required primary batch size or a100 ml receiving dose.", "missing": true}]}, {"quantity_id": "q32", "topic": "Vitamin mixture aliquot Acidic solution (HCl, pH 3; 100 ml)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Acidic solution (HCl, pH 3; 100 ml)\",\n                        \"solution_id\": 5705,\n                        \"amount\": 50,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "solution": "Acidic solution (HCl, pH 3; 100 ml)", "solution_id": 5705, "amount": 50, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Acidic solution (HCl, pH 3; 100 ml)\",\n                        \"solution_id\": 5705,\n                        \"amount\": 50,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "solution": "Acidic solution (HCl, pH 3; 100 ml)", "solution_id": 5705, "amount": 50, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "The API vitamin-mixture recipe supplies50 ml of this subsolution, with total provider volume150 ml. The primary instead gives the scale-free1:1:1 volume ratio. Preserve50 ml as the provider realization of that ratio, not a required primary batch size or a100 ml receiving dose.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The API vitamin-mixture recipe supplies50 ml of this subsolution, with total provider volume150 ml. The primary instead gives the scale-free1:1:1 volume ratio. Preserve50 ml as the provider realization of that ratio, not a required primary batch size or a100 ml receiving dose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The API vitamin-mixture recipe supplies50 ml of this subsolution, with total provider volume150 ml. The primary instead gives the scale-free1:1:1 volume ratio. Preserve50 ml as the provider realization of that ratio, not a required primary batch size or a100 ml receiving dose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The API vitamin-mixture recipe supplies50 ml of this subsolution, with total provider volume150 ml. The primary instead gives the scale-free1:1:1 volume ratio. Preserve50 ml as the provider realization of that ratio, not a required primary batch size or a100 ml receiving dose.", "missing": true}]}, {"quantity_id": "q33", "topic": "Main recipe solvent context", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Main1000 ml water is explicitly provider data; neither primary PDF states this as a main water/makeup instruction. Preserve that source attribution without changing a mineral g/L basis or inventing a measured final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "notes", "stored_value": "Source: DSMZ &#124; Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf", "decision": "add", "rationale": "Main1000 ml water is explicitly provider data; neither primary PDF states this as a main water/makeup instruction. Preserve that source attribution without changing a mineral g/L basis or inventing a measured final volume."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "notes", "stored_value": "Source: DSMZ &#124; Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf", "decision": "add", "rationale": "Main1000 ml water is explicitly provider data; neither primary PDF states this as a main water/makeup instruction. Preserve that source attribution without changing a mineral g/L basis or inventing a measured final volume."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "notes", "stored_value": "Source: DSMZ &#124; Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf", "decision": "add", "rationale": "Main1000 ml water is explicitly provider data; neither primary PDF states this as a main water/makeup instruction. Preserve that source attribution without changing a mineral g/L basis or inventing a measured final volume."}]}, {"quantity_id": "q34", "topic": "Basic solution (100 ml 0.1 N NaOH) solvent context", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[2].recipe[4]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "Distilled water", "compound_id": 4, "amount": 100, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[3].recipe[4]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "Distilled water", "compound_id": 4, "amount": 100, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "The source stock stage is Basic solution (100 ml 0.1 N NaOH). Preserve the API solvent amount at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the API plain-water row cannot replace that solvent chemistry; for the acidic solution retain HCl/pH3. No adjustment volume is given.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source stock stage is Basic solution (100 ml 0.1 N NaOH). Preserve the API solvent amount at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the API plain-water row cannot replace that solvent chemistry; for the acidic solution retain HCl/pH3. No adjustment volume is given.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source stock stage is Basic solution (100 ml 0.1 N NaOH). Preserve the API solvent amount at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the API plain-water row cannot replace that solvent chemistry; for the acidic solution retain HCl/pH3. No adjustment volume is given.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source stock stage is Basic solution (100 ml 0.1 N NaOH). Preserve the API solvent amount at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the API plain-water row cannot replace that solvent chemistry; for the acidic solution retain HCl/pH3. No adjustment volume is given.", "missing": true}]}, {"quantity_id": "q35", "topic": "Neutral solution (100 ml Aqua dem.) solvent context", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[3].recipe[2]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "Distilled water", "compound_id": 4, "amount": 100, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[4].recipe[2]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "Distilled water", "compound_id": 4, "amount": 100, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "The source stock stage is Neutral solution (100 ml Aqua dem.). Preserve the API solvent amount at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the API plain-water row cannot replace that solvent chemistry; for the acidic solution retain HCl/pH3. No adjustment volume is given.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source stock stage is Neutral solution (100 ml Aqua dem.). Preserve the API solvent amount at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the API plain-water row cannot replace that solvent chemistry; for the acidic solution retain HCl/pH3. No adjustment volume is given.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source stock stage is Neutral solution (100 ml Aqua dem.). Preserve the API solvent amount at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the API plain-water row cannot replace that solvent chemistry; for the acidic solution retain HCl/pH3. No adjustment volume is given.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source stock stage is Neutral solution (100 ml Aqua dem.). Preserve the API solvent amount at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the API plain-water row cannot replace that solvent chemistry; for the acidic solution retain HCl/pH3. No adjustment volume is given.", "missing": true}]}, {"quantity_id": "q36", "topic": "Acidic trace metals (Pfennig &amp; Lippert, 1965) solvent context", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[4].recipe[9]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[5].recipe[9]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "The source stock stage is Acidic trace metals (Pfennig &amp; Lippert, 1965). Preserve the API solvent amount at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the API plain-water row cannot replace that solvent chemistry; for the acidic solution retain HCl/pH3. No adjustment volume is given.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source stock stage is Acidic trace metals (Pfennig &amp; Lippert, 1965). Preserve the API solvent amount at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the API plain-water row cannot replace that solvent chemistry; for the acidic solution retain HCl/pH3. No adjustment volume is given.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source stock stage is Acidic trace metals (Pfennig &amp; Lippert, 1965). Preserve the API solvent amount at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the API plain-water row cannot replace that solvent chemistry; for the acidic solution retain HCl/pH3. No adjustment volume is given.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source stock stage is Acidic trace metals (Pfennig &amp; Lippert, 1965). Preserve the API solvent amount at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the API plain-water row cannot replace that solvent chemistry; for the acidic solution retain HCl/pH3. No adjustment volume is given.", "missing": true}]}, {"quantity_id": "q37", "topic": "Acidic solution (HCl, pH 3; 100 ml) solvent context", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[5].recipe[3]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "Distilled water", "compound_id": 4, "amount": 100, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[2].recipe[3]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "Distilled water", "compound_id": 4, "amount": 100, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "The source stock stage is Acidic solution (HCl, pH 3; 100 ml). Preserve the API solvent amount at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the API plain-water row cannot replace that solvent chemistry; for the acidic solution retain HCl/pH3. No adjustment volume is given.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source stock stage is Acidic solution (HCl, pH 3; 100 ml). Preserve the API solvent amount at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the API plain-water row cannot replace that solvent chemistry; for the acidic solution retain HCl/pH3. No adjustment volume is given.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source stock stage is Acidic solution (HCl, pH 3; 100 ml). Preserve the API solvent amount at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the API plain-water row cannot replace that solvent chemistry; for the acidic solution retain HCl/pH3. No adjustment volume is given.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source stock stage is Acidic solution (HCl, pH 3; 100 ml). Preserve the API solvent amount at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the API plain-water row cannot replace that solvent chemistry; for the acidic solution retain HCl/pH3. No adjustment volume is given.", "missing": true}]}, {"quantity_id": "q38", "topic": "Preparation stage 1", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"step\": \"Adjust pH to 10.0 with NaOH or HCl. Make anoxic under nitrogen stream and autoclave at 121\\u00b0C.\"\n                    }", "exact_decoded_object": {"recipe_order": 6, "step": "Adjust pH to 10.0 with NaOH or HCl. Make anoxic under nitrogen stream and autoclave at 121°C."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"step\": \"Adjust pH to 10.0 with NaOH or HCl. Make anoxic under nitrogen stream and autoclave at 121\\u00b0C.\"\n                    }", "exact_decoded_object": {"recipe_order": 6, "step": "Adjust pH to 10.0 with NaOH or HCl. Make anoxic under nitrogen stream and autoclave at 121°C."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The retained mineral-base text is supported: pH10 with NaOH or HCl, nitrogen and121°C. Autoclave duration and titrant amounts are not supplied; do not infer them.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "preparation_steps[0]", "stored_value": {"step_number": 1, "action": "AUTOCLAVE", "description": "Adjust pH to 10.0 with NaOH or HCl. Make anoxic under nitrogen stream and autoclave at 121°C."}, "decision": "evidence_only", "rationale": "The retained mineral-base text is supported: pH10 with NaOH or HCl, nitrogen and121°C. Autoclave duration and titrant amounts are not supplied; do not infer them."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "preparation_steps[0]", "stored_value": {"step_number": 1, "action": "AUTOCLAVE", "description": "Adjust pH to 10.0 with NaOH or HCl. Make anoxic under nitrogen stream and autoclave at 121°C."}, "decision": "evidence_only", "rationale": "The retained mineral-base text is supported: pH10 with NaOH or HCl, nitrogen and121°C. Autoclave duration and titrant amounts are not supplied; do not infer them."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "preparation_steps[0]", "stored_value": {"step_number": 1, "action": "AUTOCLAVE", "description": "Adjust pH to 10.0 with NaOH or HCl. Make anoxic under nitrogen stream and autoclave at 121°C."}, "decision": "evidence_only", "rationale": "The retained mineral-base text is supported: pH10 with NaOH or HCl, nitrogen and121°C. Autoclave duration and titrant amounts are not supplied; do not infer them."}]}, {"quantity_id": "q39", "topic": "Preparation stage 2", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[0].steps[1]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"step\": \"After autoclaving add sterile, anoxic solutions of:\"\n                    }", "exact_decoded_object": {"recipe_order": 6, "step": "After autoclaving add sterile, anoxic solutions of:"}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[0].steps[1]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"step\": \"After autoclaving add sterile, anoxic solutions of:\"\n                    }", "exact_decoded_object": {"recipe_order": 6, "step": "After autoclaving add sterile, anoxic solutions of:"}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The post-autoclave introduction is retained but dangling. Connect it to the explicitly enumerated sterile anoxic supplements, amounts and source forms, rather than treating it as a complete standalone mixing instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "preparation_steps[1]", "stored_value": {"step_number": 2, "action": "MIX", "description": "After autoclaving add sterile, anoxic solutions of:"}, "decision": "correct", "rationale": "The post-autoclave introduction is retained but dangling. Connect it to the explicitly enumerated sterile anoxic supplements, amounts and source forms, rather than treating it as a complete standalone mixing instruction."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "preparation_steps[1]", "stored_value": {"step_number": 2, "action": "MIX", "description": "After autoclaving add sterile, anoxic solutions of:"}, "decision": "correct", "rationale": "The post-autoclave introduction is retained but dangling. Connect it to the explicitly enumerated sterile anoxic supplements, amounts and source forms, rather than treating it as a complete standalone mixing instruction."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "preparation_steps[1]", "stored_value": {"step_number": 2, "action": "MIX", "description": "After autoclaving add sterile, anoxic solutions of:"}, "decision": "correct", "rationale": "The post-autoclave introduction is retained but dangling. Connect it to the explicitly enumerated sterile anoxic supplements, amounts and source forms, rather than treating it as a complete standalone mixing instruction."}]}, {"quantity_id": "q40", "topic": "Preparation stage 3", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"step\": \"Sterilize by filtration and keep at 4\\u00b0C. Before addition to the medium mix 1:1:1 (vol:vol:vol).\"\n                    }", "exact_decoded_object": {"step": "Sterilize by filtration and keep at 4°C. Before addition to the medium mix 1:1:1 (vol:vol:vol)."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"step\": \"Sterilize by filtration and keep at 4\\u00b0C. Before addition to the medium mix 1:1:1 (vol:vol:vol).\"\n                    }", "exact_decoded_object": {"step": "Sterilize by filtration and keep at 4°C. Before addition to the medium mix 1:1:1 (vol:vol:vol)."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This instruction belongs to the vitamin mixture/subsolutions: filtration,4°C storage and1:1:1 equal-volume mixing before receiving-medium addition. Its current HEAT action is wrong and top-level placement lacks stock scope; retain the source text and replace with accurately scoped schema-valid actions.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "preparation_steps[2]", "stored_value": {"step_number": 3, "action": "HEAT", "description": "Sterilize by filtration and keep at 4°C. Before addition to the medium mix 1:1:1 (vol:vol:vol)."}, "decision": "correct", "rationale": "This instruction belongs to the vitamin mixture/subsolutions: filtration,4°C storage and1:1:1 equal-volume mixing before receiving-medium addition. Its current HEAT action is wrong and top-level placement lacks stock scope; retain the source text and replace with accurately scoped schema-valid actions."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "preparation_steps[2]", "stored_value": {"step_number": 3, "action": "HEAT", "description": "Sterilize by filtration and keep at 4°C. Before addition to the medium mix 1:1:1 (vol:vol:vol)."}, "decision": "correct", "rationale": "This instruction belongs to the vitamin mixture/subsolutions: filtration,4°C storage and1:1:1 equal-volume mixing before receiving-medium addition. Its current HEAT action is wrong and top-level placement lacks stock scope; retain the source text and replace with accurately scoped schema-valid actions."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "preparation_steps[2]", "stored_value": {"step_number": 3, "action": "HEAT", "description": "Sterilize by filtration and keep at 4°C. Before addition to the medium mix 1:1:1 (vol:vol:vol)."}, "decision": "correct", "rationale": "This instruction belongs to the vitamin mixture/subsolutions: filtration,4°C storage and1:1:1 equal-volume mixing before receiving-medium addition. Its current HEAT action is wrong and top-level placement lacks stock scope; retain the source text and replace with accurately scoped schema-valid actions."}]}, {"quantity_id": "q41", "topic": "Preparation stage 4", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578", "locator": "$.data.solutions[4].steps[0]", "accessed_at": "2026-10-28T08:34:40.418030Z", "quote": "{\n                        \"step\": \"adjust pH to 3-4 with HCl; autoclave in closed bottles, 120\\u00b0C, 20 min.\"\n                    }", "exact_decoded_object": {"step": "adjust pH to 3-4 with HCl; autoclave in closed bottles, 120°C, 20 min."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886", "locator": "$.data.solutions[5].steps[0]", "accessed_at": "2026-10-28T08:34:40.867549Z", "quote": "{\n                        \"step\": \"adjust pH to 3-4 with HCl; autoclave in closed bottles, 120\\u00b0C, 20 min.\"\n                    }", "exact_decoded_object": {"step": "adjust pH to 3-4 with HCl; autoclave in closed bottles, 120°C, 20 min."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This instruction belongs only to the acidic trace stock: pH3–4 with HCl and closed-bottle autoclave120°C20 min. It must not replace the main pH10/121°C preparation. Preserve the numeric stock conditions while relocating their scope.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "preparation_steps[3]", "stored_value": {"step_number": 4, "action": "AUTOCLAVE", "description": "adjust pH to 3-4 with HCl; autoclave in closed bottles, 120°C, 20 min."}, "decision": "correct", "rationale": "This instruction belongs only to the acidic trace stock: pH3–4 with HCl and closed-bottle autoclave120°C20 min. It must not replace the main pH10/121°C preparation. Preserve the numeric stock conditions while relocating their scope."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "preparation_steps[3]", "stored_value": {"step_number": 4, "action": "AUTOCLAVE", "description": "adjust pH to 3-4 with HCl; autoclave in closed bottles, 120°C, 20 min."}, "decision": "correct", "rationale": "This instruction belongs only to the acidic trace stock: pH3–4 with HCl and closed-bottle autoclave120°C20 min. It must not replace the main pH10/121°C preparation. Preserve the numeric stock conditions while relocating their scope."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "preparation_steps[3]", "stored_value": {"step_number": 4, "action": "AUTOCLAVE", "description": "adjust pH to 3-4 with HCl; autoclave in closed bottles, 120°C, 20 min."}, "decision": "correct", "rationale": "This instruction belongs only to the acidic trace stock: pH3–4 with HCl and closed-bottle autoclave120°C20 min. It must not replace the main pH10/121°C preparation. Preserve the numeric stock conditions while relocating their scope."}]}, {"quantity_id": "q42", "topic": "Main pH10", "source": [{"evidence_id": "dsm1464", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1464.bin", "raw_sha256": "1a27d397090c1d2eb31c7c6835bc79f094c2fa88010ceb3a900b8b08e8a8f46a", "locator": "Page1 mineral preparation", "accessed_at": "2026-10-28T08:34:40.751275Z", "quote": "Adjust pH to 10.0 with NaOH or HCl."}, {"evidence_id": "dsm1465", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1465.bin", "raw_sha256": "61633d2fad4085c3cd67f6f55f7be13067816f10c93104859782df1da7cb84f6", "locator": "Page1 mineral preparation", "accessed_at": "2026-10-28T08:34:41.044645Z", "quote": "Adjust pH to 10.0 with NaOH or HCl."}], "decision": "evidence_only", "rationale": "Retained main pH is supported and is not a stock pH.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ph_value", "stored_value": 10.0, "decision": "evidence_only", "rationale": "The explicit main pH10 is retained; stock pH3/3–4 is separate."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ph_value", "stored_value": 10.0, "decision": "evidence_only", "rationale": "The explicit main pH10 is retained; stock pH3/3–4 is separate."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ph_value", "stored_value": 10.0, "decision": "evidence_only", "rationale": "The explicit main pH10 is retained; stock pH3/3–4 is separate."}]}, {"quantity_id": "q43", "topic": "Acidic vitamin preparation", "source": [{"evidence_id": "dsm1464", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1464.bin", "raw_sha256": "1a27d397090c1d2eb31c7c6835bc79f094c2fa88010ceb3a900b8b08e8a8f46a", "locator": "Exact scoped primary paragraph", "accessed_at": "2026-10-28T08:34:40.751275Z", "quote": "1: acidic solution (HCl, pH 3; 100 ml)"}, {"evidence_id": "dsm1465", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1465.bin", "raw_sha256": "61633d2fad4085c3cd67f6f55f7be13067816f10c93104859782df1da7cb84f6", "locator": "Exact scoped primary paragraph", "accessed_at": "2026-10-28T08:34:41.044645Z", "quote": "1: acidic solution (HCl, pH 3; 100 ml)"}], "decision": "add", "rationale": "Preserve HCl/pH3 and100 ml acidic subsolution identity. No HCl strength or titrant volume is supplied.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Preserve HCl/pH3 and100 ml acidic subsolution identity. No HCl strength or titrant volume is supplied.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Preserve HCl/pH3 and100 ml acidic subsolution identity. No HCl strength or titrant volume is supplied.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Preserve HCl/pH3 and100 ml acidic subsolution identity. No HCl strength or titrant volume is supplied.", "missing": true}]}, {"quantity_id": "q44", "topic": "Basic vitamin preparation", "source": [{"evidence_id": "dsm1464", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1464.bin", "raw_sha256": "1a27d397090c1d2eb31c7c6835bc79f094c2fa88010ceb3a900b8b08e8a8f46a", "locator": "Exact scoped primary paragraph", "accessed_at": "2026-10-28T08:34:40.751275Z", "quote": "2: basic solution (100 ml 0.1 N NaOH)"}, {"evidence_id": "dsm1465", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1465.bin", "raw_sha256": "61633d2fad4085c3cd67f6f55f7be13067816f10c93104859782df1da7cb84f6", "locator": "Exact scoped primary paragraph", "accessed_at": "2026-10-28T08:34:41.044645Z", "quote": "2: basic solution (100 ml 0.1 N NaOH)"}], "decision": "add", "rationale": "Preserve100 ml0.1 N NaOH at the basic vitamin stage. Do not replace the specified solvent by plain API distilled-water context.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Preserve100 ml0.1 N NaOH at the basic vitamin stage. Do not replace the specified solvent by plain API distilled-water context.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Preserve100 ml0.1 N NaOH at the basic vitamin stage. Do not replace the specified solvent by plain API distilled-water context.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Preserve100 ml0.1 N NaOH at the basic vitamin stage. Do not replace the specified solvent by plain API distilled-water context.", "missing": true}]}, {"quantity_id": "q45", "topic": "Neutral vitamin preparation", "source": [{"evidence_id": "dsm1464", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1464.bin", "raw_sha256": "1a27d397090c1d2eb31c7c6835bc79f094c2fa88010ceb3a900b8b08e8a8f46a", "locator": "Exact scoped primary paragraph", "accessed_at": "2026-10-28T08:34:40.751275Z", "quote": "3: Neutral solution (100 ml Aqua dem.)"}, {"evidence_id": "dsm1465", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1465.bin", "raw_sha256": "61633d2fad4085c3cd67f6f55f7be13067816f10c93104859782df1da7cb84f6", "locator": "Exact scoped primary paragraph", "accessed_at": "2026-10-28T08:34:41.044645Z", "quote": "3: Neutral solution (100 ml Aqua dem.)"}], "decision": "add", "rationale": "Preserve100 ml demineralized water at the neutral vitamin stage.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Preserve100 ml demineralized water at the neutral vitamin stage.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Preserve100 ml demineralized water at the neutral vitamin stage.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Preserve100 ml demineralized water at the neutral vitamin stage.", "missing": true}]}, {"quantity_id": "q46", "topic": "Molybdate source alternative", "source": [{"evidence_id": "dsm1464", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1464.bin", "raw_sha256": "1a27d397090c1d2eb31c7c6835bc79f094c2fa88010ceb3a900b8b08e8a8f46a", "locator": "Primary acidic trace-metal stock table; extracted PDF text line 33 (1-based)", "accessed_at": "2026-10-28T08:34:40.751275Z", "quote": "9. Na2MoO4 x 2H2O or NH4MoO4                                      20 mg/l"}, {"evidence_id": "dsm1465", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1465.bin", "raw_sha256": "61633d2fad4085c3cd67f6f55f7be13067816f10c93104859782df1da7cb84f6", "locator": "Primary acidic trace-metal stock table; extracted PDF text line 34 (1-based)", "accessed_at": "2026-10-28T08:34:41.044645Z", "quote": "9. Na2MoO4 x 2H2O or NH4MoO4                                      20 mg/l"}], "decision": "add", "rationale": "Retain the printed alternative and its20 mg/L trace-stock context. The API selects sodium molybdate dihydrate; it does not authenticate or correct the alternative formula or authorize adding both.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain the printed alternative and its20 mg/L trace-stock context. The API selects sodium molybdate dihydrate; it does not authenticate or correct the alternative formula or authorize adding both.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain the printed alternative and its20 mg/L trace-stock context. The API selects sodium molybdate dihydrate; it does not authenticate or correct the alternative formula or authorize adding both.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Retain the printed alternative and its20 mg/L trace-stock context. The API selects sodium molybdate dihydrate; it does not authenticate or correct the alternative formula or authorize adding both.", "missing": true}]}, {"quantity_id": "q47", "topic": "Unspecified late-stock doses", "source": [{"evidence_id": "dsm1464", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1464.bin", "raw_sha256": "1a27d397090c1d2eb31c7c6835bc79f094c2fa88010ceb3a900b8b08e8a8f46a", "locator": "Exact scoped primary paragraph", "accessed_at": "2026-10-28T08:34:40.751275Z", "quote": "After autoclaving add sterile, anoxic solutions of:"}, {"evidence_id": "dsm1465", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1465.bin", "raw_sha256": "61633d2fad4085c3cd67f6f55f7be13067816f10c93104859782df1da7cb84f6", "locator": "Exact scoped primary paragraph", "accessed_at": "2026-10-28T08:34:41.044645Z", "quote": "After autoclaving add sterile, anoxic solutions of:"}], "decision": "unsupported", "rationale": "The primary gives final concentrations, specific trace/vitamin additions and a bare5% chitin solution, but not every late-stock strength or addition volume, autoclave duration, titrant volume or percentage basis. Leave these unresolved instead of choosing typical values.", "layer_assessments": []}]

### Current ontology and MIM correspondence

grounding: concern. Targets: CultureMech:000930.

All current recursive chemical slots, labels and exact MIM rows were checked against fresh OLS objects. Preserve the owner chitin repair and supported sulfate/metal forms; nickel dihydrate versus anhydrous34887 is a confirmed mismatch. Generic calcium pantothenate does not authenticate CHEBI:31345 stereochemistry, and thiamine cation does not establish a counterion. Current catalog REJECTED/MAPPED alternatives remain explicit rather than treated as universal authority.

### History and evidence scope

provenance: concern. Targets: CultureMech:000930.

Seven complete historical reports and current histories were read, including every claim row and per-accession raw-object join. Current API bytes authenticate the matching historical response, not retrieval time, historical commands or old recommendations. No attached claim evidence is falsely credited as present.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:000930.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:000930.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Separate concentration variants before regeneration

major / open / confirmed; issue key: culturemech-000930-separate-concentration-variants-before-regeneration.

The generated target identifies DSM 1464/000930 yet uses8 and22 from DSM 1465/000931. The two maintained variants already preserve15/95 and8/22 respectively and explicit reciprocal links. Current merge_formulation_evidence rejects differing assertions; the historical ingredient-only merge is not current policy.

### f2: Restore two receiving stocks and three vitamin subsolutions

major / open / confirmed; issue key: culturemech-000930-restore-two-receiving-stocks-and-three-vitamin-subsolutions.

Eighteen direct rows represent trace-stock or unmixed vitamin-subsolution concentrations. Both primary sources instead add 1 ml/L trace stock and1 ml/L of the 1:1:1 vitamin mixture. Solvents, acid/base identities and mixing boundaries are missing. Vitamin filtration/storage and trace pH/autoclave steps are unscoped, and the vitamin step is mislabeled HEAT.

### f3: Reconcile the sodium sulfide conversion with explicit source molarity

major / open / confirmed; issue key: culturemech-000930-reconcile-the-sodium-sulfide-conversion-with-explicit-source-molarity.

All records retain provider 0.07906 g/L Na2S. The primary prescribes final 1 mM; current exact anhydrous CHEBI:76208 mass 78.047 gives 0.078047 g/L at1 mM. This is a source conversion conflict, not evidence for a hydrate or for altering other supported main rates.

### f4: Preserve supplied nickel dihydrate specificity

major / open / confirmed; issue key: culturemech-000930-preserve-supplied-nickel-dihydrate-specificity.

The primary and API explicitly supply NiCl2 x2H2O, while both local term slots point to anhydrous nickel dichloride CHEBI:34887. Current catalog linkage of that name to34887 does not add water to the OLS chemical object. Calcium pantothenate CHEBI:31345 has stereospecified structure not independently established by the generic source name; thiamine is a cation-level identity, not a verified supplied counterion.

### f5: Carry forward the existing owner chitin grounding

minor / open / confirmed; issue key: culturemech-000930-carry-forward-the-existing-owner-chitin-grounding.

Both maintained owners already carry current CHEBI:17029 chitin and the later grounding event; the target lacks this term. The fresh OLS object and exact current Chitin row support preserving that owner repair. Missing secondary slots are not automatically wrong chemistry.

### f6: Attach stage-specific evidence without rewriting prior reviews

minor / open / confirmed; issue key: culturemech-000930-attach-stage-specific-evidence-without-rewriting-prior-reviews.

Current records lack attached quantity and stock-stage evidence. Both current API digests authenticate matching October source bytes and all exact table objects; their blanket conflict decisions do not override supported main values. September endorsed the sodium-sulfide conversion and described an older merger; those conclusions are reassessed rather than silently adopted.

## Recommended Actions And Acceptance Checks

### action1

Preserve both maintained variant identities and their current source amounts. Regenerate them through the current compatibility guard without collapsing unequal formulations or publishing sibling quantities under DSM 1464. Verify the1464 target against 15/95 and retain the1465 record separately.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Model the trace stock, mixed vitamin stock and three subsolutions with exact source amounts, forms, solvents and receiving additions. Relocate their preparation and replace HEAT with appropriate scoped actions; retain main pH/preparation. Preserve the primary 1:1:1 ratio and distinguish optional provider 50 ml aliquot scale. Do not retain direct stock-rate ingredients or infer missing stock strengths.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Retain the explicit primary 1 mM final concentration and document the inconsistent provider mass value. Reconcile formula/molar-mass assumptions before any mass representation; do not silently endorse 0.07906 g/L, substitute an unreported hydrate or change source-prescribed molarity.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action4

Resolve the exact nickel-dihydrate grounding while retaining its supplied name and stock amount. Do not substitute hexahydrate or certify the anhydrous object as a hydrate. Keep calcium stereochemistry and thiamine supplied-salt specificity explicitly unresolved unless exact authoritative evidence is obtained.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action5

Preserve the verified owner chitin term and original later history during correct separate regeneration. Do not recreate the grounding as a new unsupported chemical claim or erase original events.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action6

Attach exact source-specific ingredient evidence and root evidence for named solution/preparation stages. Keep both variants and every original historical event unchanged; append a verified current curation event with explicit source conflicts and unresolved alternatives.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/chitinispirillum_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-2 | data/normalized_yaml/bacterial/chitinivibrio_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| identity-search | REVIEW_WORK/batch061/record03/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _parse_api_solutions, _parse_preparation_steps | context_only | Current composition parser restricts ingredients to the primary solution, excludes solvent and recognized stock additions, and retains explicit g_l. The solution parser preserves referenced or percent-defined stocks and source attributes. Preparation parsing still concatenates all solution steps into root preparation_steps; source-stage annotation remains important. These present functions do not prove the historical execution that produced this record. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group copies a sole contributor with merge metadata. For multiple contributors it passes records to merge_formulation_evidence, which checks compatibility; it does not authorize merging different preparation assertions. |
| writer-formulation | src/culturemech/merge/formulation.py; formulation_content, merge_formulation_evidence | context_only | Current compatibility preserves scientific fields and list order and rejects unequal formulations; only specified provenance/evidence lists are unioned. It performs no concentration conversion or stock expansion and does not authenticate historical merges. |
| writer-cleanup | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients, merge_ingredient_group | context_only | Current cleanup groups identical normalized names, keeps the first entry as a base, flags differing concentrations and combines a warning note; it does not sum concentrations. It can still discard distinctions when names repeat, so source stage must be retained. Current behavior does not establish the historical cause of an existing discrepancy. |
| historical-1 | reports/archive/media_variant_haloalkaliphile_alkaliphilus_chitin_review.md; Entire selected report; exact chitin pair only for cross-pair conclusions | context_only | Complete derivative report read. Variant lineage is retained; old formula-wide conflict labels, historical merge causality and unexplained conversion endorsements are reassessed against current sources. |
| historical-2 | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/chitinispirillum_medium.yaml.md; Entire selected report; exact chitin pair only for cross-pair conclusions | context_only | Current raw response exactly matches the cited digest; all 41 literal/decoded objects authenticate these source bytes, not historical access or blanket conflict conclusions. |
| historical-3 | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/chitinivibrio_medium.yaml.md; Entire selected report; exact chitin pair only for cross-pair conclusions | context_only | Current raw response exactly matches the cited digest; all 41 literal/decoded objects authenticate these source bytes, not historical access or blanket conflict conclusions. |
| historical-4 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.md; Entire selected report; exact chitin pair only for cross-pair conclusions | context_only | Complete derivative report read. Variant lineage is retained; old formula-wide conflict labels, historical merge causality and unexplained conversion endorsements are reassessed against current sources. |
| historical-5 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chitinispirillum_medium.md; Entire selected report; exact chitin pair only for cross-pair conclusions | context_only | Complete derivative report read. Variant lineage is retained; old formula-wide conflict labels, historical merge causality and unexplained conversion endorsements are reassessed against current sources. |
| historical-6 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chitinivibrio_medium.md; Entire selected report; exact chitin pair only for cross-pair conclusions | context_only | Complete derivative report read. Variant lineage is retained; old formula-wide conflict labels, historical merge causality and unexplained conversion endorsements are reassessed against current sources. |
| historical-7 | reports/yaml_record_review/20260922T070021Z-CHITINIVIBRIO_MEDIUM.md; Entire selected report; exact chitin pair only for cross-pair conclusions | context_only | Complete derivative report read. Variant lineage is retained; old formula-wide conflict labels, historical merge causality and unexplained conversion endorsements are reassessed against current sources. |
| historical-reader | REVIEW_WORK/batch061/record03/historical-reader.json | context_only | Seven complete historical reports, all tables and exact per-accession raw joins. No historical execution inferred. |
| dsm1464 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf; Pages1–2, complete tables and preparation | supports | Both primary pages read textually and visually, including mineral units, all post-autoclave additions, trace-metal recipe and three vitamin subsolutions with1:1:1 mixing. Each accession remains a separate variant. |
| dsm1465 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf; Pages1–2, complete tables and preparation | supports | Both primary pages read textually and visually, including mineral units, all post-autoclave additions, trace-metal recipe and three vitamin subsolutions with1:1:1 mixing. Each accession remains a separate variant. |
| api1464 | https://mediadive.dsmz.de/rest/medium/1464; $.data.medium and all $.data.solutions | supports | Complete source-specific response read, including all six solution objects, declared g_l, stock waters and50ml vitamin aliquots. Explicit provider values are retained separately from primary instructions and unresolved conversion discrepancies. |
| api1465 | https://mediadive.dsmz.de/rest/medium/1465; $.data.medium and all $.data.solutions | supports | Complete source-specific response read, including all six solution objects, declared g_l, stock waters and50ml vitamin aliquots. Explicit provider values are retained separately from primary instructions and unresolved conversion discrepancies. |
| writer-grounding | scripts/apply_mim_groundings.py; target_slot, groundable, apply_to_record | context_only | Current target_slot preserves existing CHEBI and other source anchors; groundable rejects conflicting corpus opinions. Missing own-term additions and hydrate disagreements are separate operations. The existing owner chitin repair is credited without claiming execution from current code. |
| variant-apply | scripts/apply_media_variant_links.py; recipe_ref and plan_links | context_only | Current proposal machinery manages explicit parent/child references; a relationship label does not authenticate a recipe or authorize merging different concentrations. The existing two owner links already identify a concentration variant. |
| variant-check | scripts/validate_media_variant_links.py; resolve_ref, child_links_parent, parent_links_child, validate_links | context_only | Current link validator resolves references and reciprocal parent/child links; this structural check does not authenticate scientific equality or justify collapse of a concentration variant. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32139; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_29377; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32599; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31206; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi76208 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_76208; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi18385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_18385; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31345; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15956; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30753; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15940; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi16709 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16709; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_27470; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17015; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi4735 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_4735; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi63041 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63041; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi49553 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49553; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17029 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17029; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch061/record03/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch061/record03/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch061/record03/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch061/record03/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch061/record03/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch061/record03/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch061/record03/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch061/record03/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch061/record03/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- DSM 1464 explicitly labels mineral concentrations g/L; DSM 1465 labels those mineral amounts g, while its API separately supplies g_l. Main water and provider volumes are not silently promoted to a physical final-volume instruction.
- Primary chitin is1–2 g/L from a bare5% solution. Provider 1.5 g/L is a conditional midpoint, not the only source prescription; the percentage basis and stock addition volume are unreported.
- Primary1 mM sodium sulfide conflicts with provider 0.07906 g/L under the current exact Na2S mass. The conflict remains documented rather than hidden by choosing convenient provider data.
- The source alternative printed NH4MoO4 is retained without guessing a corrected formula, hydrate or replacement amount. Calcium pantothenate stereochemistry and thiamine counterion are not independently established by the generic names.
- Original Pfennig and Lippert1965 publication was not retrieved. The DSM reproduced stock recipes are the verified primary catalogue source; no original-paper DOI or organism-growth claim is fabricated.
- No autoclave duration for the main mineral base, full late-stock strengths/doses, titrant volumes or incubation conditions are inferred. Stock 4°C storage and trace 120°C / 20 min remain separate from main preparation.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T091527Z-batch061-record03-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'CHITINIVIBRIO: separate source variants and restore nested stock stages'
started_at: '2026-10-28T08:33:32.887567Z'
finished_at: '2026-10-28T09:15:27.470495Z'
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
summary: The target identifies DSM 1464 but contains the carbonate/bicarbonate pair
  from DSM 1465. Both maintained variants already preserve their distinct main amounts
  and chitin grounding. Eighteen stock components remain flattened in all three records,
  preparation lacks stage scope, and the provider sodium-sulfide mass conversion conflicts
  with the primary molarity and current chemical mass. Preserve supported main claims
  and exact source alternatives while resolving supplied nickel form and missing evidence.
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
  - path: data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml
    sha256: 6c31efeaa16f716f4c59e1b6f665362ec0fcec6de96da4fc46ff26e79074e7cf
    role: target
  - path: data/normalized_yaml/bacterial/chitinispirillum_medium.yaml
    sha256: 40a2c1611b6a53b8d33be67b6bf72c062b932cbd4b20fa95d6c69f555e0dbabb
    role: context
  - path: data/normalized_yaml/bacterial/chitinivibrio_medium.yaml
    sha256: 2f0137e0da78e0fa4512effe5314e70ff732be7164e977f9c3cf69beed383845
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
  - path: reports/archive/media_variant_haloalkaliphile_alkaliphilus_chitin_review.md
    sha256: 00e5372726e5584b61bd1a6ee82c6d6c5cf86f1f26e2ba756f30b5e9cdf979dd
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/chitinispirillum_medium.yaml.md
    sha256: dc112a1bdd723047edc4b64f7a9fddf4704afed5407f2ad6531ed054fa4ebd9e
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/chitinivibrio_medium.yaml.md
    sha256: beeb4a1e8dd3ccc0f74d4ccced9badba542abd40a649962b0d6d7918018cf928
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.md
    sha256: c90711ab0447c371b70e8aed237c186da88b7210af3fdab46bce712e278b6d3a
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chitinispirillum_medium.md
    sha256: e8620c4ab583fa14cc982ca773f8852a20b0cae000f60e75ae625af83e03e2de
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chitinivibrio_medium.md
    sha256: 5cf6fc01ff1f4e4762677ed4cfe3090eedcc8743e0da610ef927214c0648d773
    role: context
  - path: reports/yaml_record_review/20260922T070021Z-CHITINIVIBRIO_MEDIUM.md
    sha256: a424b7af00ba0fd01dcbdfe44c139d38968f68083c21a9e74a54468300b3ceef
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_media_variant_links.py
    sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
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
  selection: Actual batch061 native selection index 03.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000930
targets:
- target_id: CultureMech:000930
  path: data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml
  label: chitinivibrio_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinispirillum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinivibrio_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:000930
  command: just validate-schema data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml
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
  - CultureMech:000930
  command: just validate-strict data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml --out
    REVIEW_WORK/batch061/record03/strict.tsv --workers 1
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
  - CultureMech:000930
  command: just validate-terms data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml
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
  - CultureMech:000930
  command: just validate-references data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T08:52:32.484002Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 6c31efeaa16f716f4c59e1b6f665362ec0fcec6de96da4fc46ff26e79074e7cf
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/chitinispirillum_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T08:52:32.484002Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 40a2c1611b6a53b8d33be67b6bf72c062b932cbd4b20fa95d6c69f555e0dbabb
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/chitinivibrio_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T08:52:32.484002Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 2f0137e0da78e0fa4512effe5314e70ff732be7164e977f9c3cf69beed383845
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch061/record03/identity-search.json
  accessed_at: '2026-10-28T08:52:32.540975Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems and stable identity resolve the owner;
    excluded namesakes are retained in the census. Similar names and source accessions
    are not promoted to owners.
  snapshot_sha256: 04a19672f80ecbb4c86869e5b713f31eeee6211a46228b14e32597a2bc267cc9
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _parse_api_solutions, _parse_preparation_steps
  accessed_at: '2026-10-28T08:52:32.484002Z'
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
  accessed_at: '2026-10-28T08:52:32.484002Z'
  support: context_only
  summary: Current merge_group copies a sole contributor with merge metadata. For
    multiple contributors it passes records to merge_formulation_evidence, which checks
    compatibility; it does not authorize merging different preparation assertions.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content, merge_formulation_evidence
  accessed_at: '2026-10-28T08:52:32.484002Z'
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
  accessed_at: '2026-10-28T08:52:32.484002Z'
  support: context_only
  summary: Current cleanup groups identical normalized names, keeps the first entry
    as a base, flags differing concentrations and combines a warning note; it does
    not sum concentrations. It can still discard distinctions when names repeat, so
    source stage must be retained. Current behavior does not establish the historical
    cause of an existing discrepancy.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: historical-1
  kind: record_content
  reference: reports/archive/media_variant_haloalkaliphile_alkaliphilus_chitin_review.md
  locator: Entire selected report; exact chitin pair only for cross-pair conclusions
  accessed_at: '2026-10-28T08:52:32.484002Z'
  support: context_only
  summary: Complete derivative report read. Variant lineage is retained; old formula-wide
    conflict labels, historical merge causality and unexplained conversion endorsements
    are reassessed against current sources.
  snapshot_sha256: 00e5372726e5584b61bd1a6ee82c6d6c5cf86f1f26e2ba756f30b5e9cdf979dd
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/chitinispirillum_medium.yaml.md
  locator: Entire selected report; exact chitin pair only for cross-pair conclusions
  accessed_at: '2026-10-28T08:52:32.484002Z'
  support: context_only
  summary: Current raw response exactly matches the cited digest; all 41 literal/decoded
    objects authenticate these source bytes, not historical access or blanket conflict
    conclusions.
  snapshot_sha256: dc112a1bdd723047edc4b64f7a9fddf4704afed5407f2ad6531ed054fa4ebd9e
- evidence_id: historical-3
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/chitinivibrio_medium.yaml.md
  locator: Entire selected report; exact chitin pair only for cross-pair conclusions
  accessed_at: '2026-10-28T08:52:32.484002Z'
  support: context_only
  summary: Current raw response exactly matches the cited digest; all 41 literal/decoded
    objects authenticate these source bytes, not historical access or blanket conflict
    conclusions.
  snapshot_sha256: beeb4a1e8dd3ccc0f74d4ccced9badba542abd40a649962b0d6d7918018cf928
- evidence_id: historical-4
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.md
  locator: Entire selected report; exact chitin pair only for cross-pair conclusions
  accessed_at: '2026-10-28T08:52:32.484002Z'
  support: context_only
  summary: Complete derivative report read. Variant lineage is retained; old formula-wide
    conflict labels, historical merge causality and unexplained conversion endorsements
    are reassessed against current sources.
  snapshot_sha256: c90711ab0447c371b70e8aed237c186da88b7210af3fdab46bce712e278b6d3a
- evidence_id: historical-5
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chitinispirillum_medium.md
  locator: Entire selected report; exact chitin pair only for cross-pair conclusions
  accessed_at: '2026-10-28T08:52:32.484002Z'
  support: context_only
  summary: Complete derivative report read. Variant lineage is retained; old formula-wide
    conflict labels, historical merge causality and unexplained conversion endorsements
    are reassessed against current sources.
  snapshot_sha256: e8620c4ab583fa14cc982ca773f8852a20b0cae000f60e75ae625af83e03e2de
- evidence_id: historical-6
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chitinivibrio_medium.md
  locator: Entire selected report; exact chitin pair only for cross-pair conclusions
  accessed_at: '2026-10-28T08:52:32.484002Z'
  support: context_only
  summary: Complete derivative report read. Variant lineage is retained; old formula-wide
    conflict labels, historical merge causality and unexplained conversion endorsements
    are reassessed against current sources.
  snapshot_sha256: 5cf6fc01ff1f4e4762677ed4cfe3090eedcc8743e0da610ef927214c0648d773
- evidence_id: historical-7
  kind: record_content
  reference: reports/yaml_record_review/20260922T070021Z-CHITINIVIBRIO_MEDIUM.md
  locator: Entire selected report; exact chitin pair only for cross-pair conclusions
  accessed_at: '2026-10-28T08:52:32.484002Z'
  support: context_only
  summary: Complete derivative report read. Variant lineage is retained; old formula-wide
    conflict labels, historical merge causality and unexplained conversion endorsements
    are reassessed against current sources.
  snapshot_sha256: a424b7af00ba0fd01dcbdfe44c139d38968f68083c21a9e74a54468300b3ceef
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch061/record03/historical-reader.json
  accessed_at: '2026-10-28T08:52:32.545039Z'
  support: context_only
  summary: Seven complete historical reports, all tables and exact per-accession raw
    joins. No historical execution inferred.
  snapshot_sha256: 7855d6255b807870ca4054cea29bc24216fb3275127fb46e17a996f104926a61
- evidence_id: dsm1464
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf
  locator: Pages1–2, complete tables and preparation
  accessed_at: '2026-10-28T08:34:40.751275Z'
  support: supports
  summary: Both primary pages read textually and visually, including mineral units,
    all post-autoclave additions, trace-metal recipe and three vitamin subsolutions
    with1:1:1 mixing. Each accession remains a separate variant.
  snapshot_sha256: 1a27d397090c1d2eb31c7c6835bc79f094c2fa88010ceb3a900b8b08e8a8f46a
- evidence_id: dsm1465
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf
  locator: Pages1–2, complete tables and preparation
  accessed_at: '2026-10-28T08:34:41.044645Z'
  support: supports
  summary: Both primary pages read textually and visually, including mineral units,
    all post-autoclave additions, trace-metal recipe and three vitamin subsolutions
    with1:1:1 mixing. Each accession remains a separate variant.
  snapshot_sha256: 61633d2fad4085c3cd67f6f55f7be13067816f10c93104859782df1da7cb84f6
- evidence_id: api1464
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1464
  locator: $.data.medium and all $.data.solutions
  accessed_at: '2026-10-28T08:34:40.418030Z'
  support: supports
  summary: Complete source-specific response read, including all six solution objects,
    declared g_l, stock waters and50ml vitamin aliquots. Explicit provider values
    are retained separately from primary instructions and unresolved conversion discrepancies.
  snapshot_sha256: a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578
- evidence_id: api1465
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1465
  locator: $.data.medium and all $.data.solutions
  accessed_at: '2026-10-28T08:34:40.867549Z'
  support: supports
  summary: Complete source-specific response read, including all six solution objects,
    declared g_l, stock waters and50ml vitamin aliquots. Explicit provider values
    are retained separately from primary instructions and unresolved conversion discrepancies.
  snapshot_sha256: 0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886
- evidence_id: writer-grounding
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: target_slot, groundable, apply_to_record
  accessed_at: '2026-10-28T08:52:32.484002Z'
  support: context_only
  summary: Current target_slot preserves existing CHEBI and other source anchors;
    groundable rejects conflicting corpus opinions. Missing own-term additions and
    hydrate disagreements are separate operations. The existing owner chitin repair
    is credited without claiming execution from current code.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: variant-apply
  kind: record_content
  reference: scripts/apply_media_variant_links.py
  locator: recipe_ref and plan_links
  accessed_at: '2026-10-28T08:52:32.484002Z'
  support: context_only
  summary: Current proposal machinery manages explicit parent/child references; a
    relationship label does not authenticate a recipe or authorize merging different
    concentrations. The existing two owner links already identify a concentration
    variant.
  snapshot_sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
- evidence_id: variant-check
  kind: record_content
  reference: scripts/validate_media_variant_links.py
  locator: resolve_ref, child_links_parent, parent_links_child, validate_links
  accessed_at: '2026-10-28T08:52:32.484002Z'
  support: context_only
  summary: Current link validator resolves references and reciprocal parent/child
    links; this structural check does not authenticate scientific equality or justify
    collapse of a concentration variant.
  snapshot_sha256: d18ef71320a0c50abe085e151d0d0d4d963007d1e1c9afbefab97581a983e31e
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32139
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:43.837408Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 314c75cd12ea5d1343b4c0bafd40e0ad72c15b19d64f8cb9152000c0d8839f56
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_29377
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:43.008537Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: dee64859233d0b0898eba91901a001f1faaa5eaab37f7beb7e98318ab8c19569
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:42.769919Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b145f4ff9b90ebb993ff576d9ab35a6c10b7c42a3b99e18feffcc8d75c0e1e50
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:41.378250Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 97e9c2b05f3937c5beeebb4e6338aa6730f9e422ee0e7570a6c622dda8d97a86
- evidence_id: chebi32599
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32599
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:44.223366Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 1a3fd204bffef0735a8d1a12385aec1c330013f84a182acc909368cd164cf821
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31206
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:43.372711Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: c70055293606f21dcdfb72325a4677661b51efb723ba9357efab43f8ec9b03f7
- evidence_id: chebi76208
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_76208
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:46.126248Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 67d01e49fb5e1b47f16d7cabf50083dc22ef08d48e811f675ea3f0dda9e5f698
- evidence_id: chebi18385
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_18385
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:42.385829Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 6370e2e611ce20ae9b889e646ff290e866b4d0afa66fe1fd24e53864daec2908
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31345
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:43.567369Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: d2a04309eb6976fd395f9684ec4c3f5192362e2b6b75464b0af128a28e188d25
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15956
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:41.745687Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0d2e75e0bd98dbffff14d85a41dfd0af8aae2a8d65a945d34a4126a17091c2b8
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30753
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:43.229211Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 42ea4022bd68e8fa28962bc496ca757174da7bbd18ce06b7f3d521885609a50c
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15940
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:41.628056Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2890ef915cd546e70c1e638af285a3cc19b8299ae7722d00b43a40170a57ab8a
- evidence_id: chebi16709
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16709
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:42.022607Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 3b055ff5d94d307b9d6d97cebfa2030b03966247245866eb796c099dbe08327c
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_27470
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:42.950745Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: dcee85bb585d3a73341ab66eff772dc6361330b3c899c4daecbda49d5e84e590
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17015
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:42.161622Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f8bec809c7ba5a36faea58b8fe1b5110f0d75dbd4ac1929a121cd352bce63309
- evidence_id: chebi4735
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_4735
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:44.892679Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f07827212a55318fd8fcd95e1827e108ea86bb3e185e227c96706b7b0f8a60cd
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:46.098303Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: e12b865122aab78645385260e1e83ff28f3c45365cb67c9181166628f68974b3
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:43.968904Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 6bf1390236046f1cb7b21e2fc324fccba6e6eac2bc4e519f12d998f0edce671b
- evidence_id: chebi63041
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63041
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:45.786002Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a4b28bcd431eb1bf3473ada547e008fa0c1541daf0fcab8d992ac55f2e17dd73
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:44.543671Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f23e1405347fa9d8a0826d4dd1279b7cdec8361390d20e439154dcbbd386a2d4
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:45.171977Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 31dc996638b0cc1341ed24fcb38ec344af726c99d376ac94e952210fcb9ed583
- evidence_id: chebi49553
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49553
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:45.206502Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: fb38cbec0d8e8f422fbf3992bc1076af9213b2fec1cd371223b249795e9d7d07
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:44.826993Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a43b8268f70ae50c4cfbc53e12bbd195618c521619cfab8f71d3704b338af95b
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:45.831867Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0271a149a298ff837ad8f690ce8cb0acf111f5d25c5efaf6fa828401ab951d56
- evidence_id: chebi17029
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17029
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:42.226882Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 8b016cf40ec86d7f3ce297e71566827474714bad00a3dcf63f93aa062b6ed64e
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch061/record03/quantity-inventory.json
  accessed_at: '2026-10-28T09:15:27.470495Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 26ee1e67da6afa1113cf1e90f0e9f1dc7cb57e7da40a84166c58f1fd49b31e07
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch061/record03/grounding-inventory.json
  accessed_at: '2026-10-28T08:52:32.603243Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: 8fac4e04d8486d8d06caac82e740ee43219211f91809c10134c480865861ef74
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch061/record03/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T08:52:32.603422Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 2a4e2cc5376ad701d5e413da566d659ffd2896abb2dcbd6db892aa341c2249ed
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch061/record03/scalar-census.json
  accessed_at: '2026-10-28T08:52:32.603444Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: 90d6c92a867a6d8d8237c8ac8eb0acf0b278dcc0b269bba8bc8d0599cab32d26
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch061/record03/validate-schema.json
  accessed_at: '2026-10-28T08:33:33.896024Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: aedab4a8c082a9763dc997f3f8a6a0873332129a34301cca3b374d9a5584f662
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch061/record03/validate-strict.json
  accessed_at: '2026-10-28T08:33:34.823778Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch061/record03/strict.tsv\n"
  snapshot_sha256: 5c2c14935710cfd1acb916898e340b6fda1c09a23c57ccc0abfba2563cffe3aa
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch061/record03/validate-terms.json
  accessed_at: '2026-10-28T08:33:35.840460Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: a26a85a3b447a9b8b9bcbcf675fade6629ab9aea54e446293ab5b5c2015de544
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch061/record03/validate-references.json
  accessed_at: '2026-10-28T08:33:36.553925Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: 19834a24d320597b6c1fc53ab76f999fb1a0e4e7de8c2c63638d55c0ded11cef
assessments:
- assessment_id: a1
  area: identity
  topic: Distinct1464 and1465 concentration variants
  outcome: concern
  summary: The selected stable ID/source is DSM 1464. Two maintained contributors
    explicitly carry reciprocal CONCENTRATION_VARIANT links and distinct15/95 versus8/22
    bicarbonate/carbonate values. These relationships are supported; they do not authorize
    one canonical mixture of the two source identities. Complex/undefined liquid state
    is supported.
  target_ids:
  - CultureMech:000930
  evidence_ids:
  - local-target
  - owner-1
  - owner-2
  - dsm1464
  - dsm1465
  - api1464
  - api1465
  - identity-search
- assessment_id: a2
  area: completeness
  topic: Preserve nested stages and already retained values
  outcome: concern
  summary: All 81 local concentration fields and every source-only solvent/dose/stock
    condition are assessed. Main rates, conditional chitin midpoint and retained main
    preparation receive source-specific credit. Both stocks and three vitamin subsolutions
    need representation; existing stock preparation must be relocated, not discarded.
  target_ids:
  - CultureMech:000930
  evidence_ids:
  - quantities
  - dsm1464
  - dsm1465
  - writer-mediadive
  - writer-formulation
- assessment_id: a3
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:000930
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "NaHCO3 variant-specific main amount",
    "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\":
    15,\n                        \"unit\": \"g/l\",\n                        \"g_l\":
    15,\n                        \"mmol_l\": 178.557,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "NaHCO3", "compound_id": 55, "amount": 15, "unit": "g/l", "g_l": 15, "mmol_l":
    178.557, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\":
    8,\n                        \"unit\": \"g\",\n                        \"g_l\":
    8,\n                        \"mmol_l\": 95.2302,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "NaHCO3", "compound_id": 55, "amount": 8, "unit": "g", "g_l": 8, "mmol_l": 95.2302,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "mixed", "rationale":
    "DSM1464 explicitly supplies15 and95 g/L for bicarbonate/carbonate; DSM1465 PDF
    instead gives8 and22 g batch amounts, with corresponding explicit provider g_l.
    The target identity is1464 but its first two values are from1465. Both owners
    already preserve their own values and relationship; do not overwrite the child
    to match the parent.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "8", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "DSM1464 explicitly supplies15
    and95 g/L for bicarbonate/carbonate; DSM1465 PDF instead gives8 and22 g batch
    amounts, with corresponding explicit provider g_l. The target identity is1464
    but its first two values are from1465. Both owners already preserve their own
    values and relationship; do not overwrite the child to match the parent."}, {"path":
    "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[0].concentration",
    "stored_value": {"value": "15", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "DSM1464 explicitly supplies15 and95 g/L for bicarbonate/carbonate;
    DSM1465 PDF instead gives8 and22 g batch amounts, with corresponding explicit
    provider g_l. The target identity is1464 but its first two values are from1465.
    Both owners already preserve their own values and relationship; do not overwrite
    the child to match the parent."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "8", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "DSM1464 explicitly supplies15
    and95 g/L for bicarbonate/carbonate; DSM1465 PDF instead gives8 and22 g batch
    amounts, with corresponding explicit provider g_l. The target identity is1464
    but its first two values are from1465. Both owners already preserve their own
    values and relationship; do not overwrite the child to match the parent."}]},
    {"quantity_id": "q2", "topic": "Na2CO3 variant-specific main amount", "source":
    [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\":
    95,\n                        \"unit\": \"g/l\",\n                        \"g_l\":
    95,\n                        \"mmol_l\": 896.328,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "Na2CO3", "compound_id": 32, "amount": 95, "unit": "g/l", "g_l": 95, "mmol_l":
    896.328, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\":
    22,\n                        \"unit\": \"g\",\n                        \"g_l\":
    22,\n                        \"mmol_l\": 207.571,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "Na2CO3", "compound_id": 32, "amount": 22, "unit": "g", "g_l": 22, "mmol_l": 207.571,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "mixed", "rationale":
    "DSM1464 explicitly supplies15 and95 g/L for bicarbonate/carbonate; DSM1465 PDF
    instead gives8 and22 g batch amounts, with corresponding explicit provider g_l.
    The target identity is1464 but its first two values are from1465. Both owners
    already preserve their own values and relationship; do not overwrite the child
    to match the parent.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "22",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "DSM1464 explicitly supplies15
    and95 g/L for bicarbonate/carbonate; DSM1465 PDF instead gives8 and22 g batch
    amounts, with corresponding explicit provider g_l. The target identity is1464
    but its first two values are from1465. Both owners already preserve their own
    values and relationship; do not overwrite the child to match the parent."}, {"path":
    "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "ingredients[1].concentration",
    "stored_value": {"value": "95", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "DSM1464 explicitly supplies15 and95 g/L for bicarbonate/carbonate;
    DSM1465 PDF instead gives8 and22 g batch amounts, with corresponding explicit
    provider g_l. The target identity is1464 but its first two values are from1465.
    Both owners already preserve their own values and relationship; do not overwrite
    the child to match the parent."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "22",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "DSM1464 explicitly
    supplies15 and95 g/L for bicarbonate/carbonate; DSM1465 PDF instead gives8 and22
    g batch amounts, with corresponding explicit provider g_l. The target identity
    is1464 but its first two values are from1465. Both owners already preserve their
    own values and relationship; do not overwrite the child to match the parent."}]},
    {"quantity_id": "q3", "topic": "NaCl variant-specific main amount", "source":
    [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\":
    6,\n                        \"unit\": \"g/l\",\n                        \"g_l\":
    6,\n                        \"mmol_l\": 102.669,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "NaCl", "compound_id": 43, "amount": 6, "unit": "g/l", "g_l": 6, "mmol_l": 102.669,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\":
    6,\n                        \"unit\": \"g\",\n                        \"g_l\":
    6,\n                        \"mmol_l\": 102.669,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "NaCl", "compound_id": 43, "amount": 6, "unit": "g", "g_l": 6, "mmol_l": 102.669,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "evidence_only",
    "rationale": "This main-stage amount agrees in both variants. DSM1464 PDF explicitly
    uses g/L; DSM1465 PDF uses batch g and its API separately declares the local g_l.
    Preserve that source-basis distinction without deriving a physical final volume
    from water.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "6", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "This main-stage amount
    agrees in both variants. DSM1464 PDF explicitly uses g/L; DSM1465 PDF uses batch
    g and its API separately declares the local g_l. Preserve that source-basis distinction
    without deriving a physical final volume from water."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "6", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "This main-stage amount
    agrees in both variants. DSM1464 PDF explicitly uses g/L; DSM1465 PDF uses batch
    g and its API separately declares the local g_l. Preserve that source-basis distinction
    without deriving a physical final volume from water."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "6", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "This main-stage amount
    agrees in both variants. DSM1464 PDF explicitly uses g/L; DSM1465 PDF uses batch
    g and its API separately declares the local g_l. Preserve that source-basis distinction
    without deriving a physical final volume from water."}]}, {"quantity_id": "q4",
    "topic": "K2HPO4 variant-specific main amount", "source": [{"evidence_id": "api1464",
    "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin",
    "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\":
    1,\n                        \"unit\": \"g/l\",\n                        \"g_l\":
    1,\n                        \"mmol_l\": 5.74132,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "K2HPO4", "compound_id": 10, "amount": 1, "unit": "g/l", "g_l": 1, "mmol_l": 5.74132,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"mmol_l\": 5.74132,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "K2HPO4", "compound_id": 10, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 5.74132,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "evidence_only",
    "rationale": "This main-stage amount agrees in both variants. DSM1464 PDF explicitly
    uses g/L; DSM1465 PDF uses batch g and its API separately declares the local g_l.
    Preserve that source-basis distinction without deriving a physical final volume
    from water.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "This main-stage amount
    agrees in both variants. DSM1464 PDF explicitly uses g/L; DSM1465 PDF uses batch
    g and its API separately declares the local g_l. Preserve that source-basis distinction
    without deriving a physical final volume from water."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "This main-stage amount
    agrees in both variants. DSM1464 PDF explicitly uses g/L; DSM1465 PDF uses batch
    g and its API separately declares the local g_l. Preserve that source-basis distinction
    without deriving a physical final volume from water."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "This main-stage amount
    agrees in both variants. DSM1464 PDF explicitly uses g/L; DSM1465 PDF uses batch
    g and its API separately declares the local g_l. Preserve that source-basis distinction
    without deriving a physical final volume from water."}]}, {"quantity_id": "q5",
    "topic": "Chitin range and conditional provider midpoint", "source": [{"evidence_id":
    "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path":
    "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Chitin\",\n                        \"compound_id\": 2138,\n                        \"condition\":
    \"adjust volume in range 1-2 if required\",\n                        \"attribute\":
    \"amorphous or Sigma C7170, 5% solution\",\n                        \"amount\":
    1.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1.5,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 6, "compound": "Chitin", "compound_id": 2138, "condition": "adjust
    volume in range 1-2 if required", "attribute": "amorphous or Sigma C7170, 5% solution",
    "amount": 1.5, "unit": "g", "g_l": 1.5, "optional": 0}, "quote_basis": "Literal
    UTF-8 raw-response substring; decoded object independently equals exact JSON locator."},
    {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Chitin\",\n                        \"compound_id\": 2138,\n                        \"condition\":
    \"adjust in range 1 - 2 g/l if required\",\n                        \"attribute\":
    \"amorphous, from 5% solution\",\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "Chitin", "compound_id": 2138, "condition": "adjust in range 1 - 2 g/l if required",
    "attribute": "amorphous, from 5% solution", "amount": 1.5, "unit": "g", "g_l":
    1.5, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "dsm1464",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf",
    "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1464.bin", "raw_sha256": "1a27d397090c1d2eb31c7c6835bc79f094c2fa88010ceb3a900b8b08e8a8f46a",
    "locator": "Page1 post-autoclave additions", "accessed_at": "2026-10-28T08:34:40.751275Z",
    "quote": "1 – 2g/l (from 5% solution)"}], "decision": "mixed", "rationale": "Both
    PDFs specify a chitin range1–2 g/L from a bare5% solution; the APIs supply conditional
    midpoint1.5 g/L. The local1.5 plus range note can be retained only as that provider-selected
    point, not as a fixed primary prescription. The DSM1464 owner note says adjust
    volume without units and must instead preserve the explicit concentration range;
    no5% mass/volume basis or stock volume is assumed.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[4].concentration",
    "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "Both PDFs specify a chitin range1–2 g/L from a bare5% solution;
    the APIs supply conditional midpoint1.5 g/L. The local1.5 plus range note can
    be retained only as that provider-selected point, not as a fixed primary prescription.
    The DSM1464 owner note says adjust volume without units and must instead preserve
    the explicit concentration range; no5% mass/volume basis or stock volume is assumed."},
    {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path":
    "ingredients[4].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "Both PDFs specify a chitin range1–2
    g/L from a bare5% solution; the APIs supply conditional midpoint1.5 g/L. The local1.5
    plus range note can be retained only as that provider-selected point, not as a
    fixed primary prescription. The DSM1464 owner note says adjust volume without
    units and must instead preserve the explicit concentration range; no5% mass/volume
    basis or stock volume is assumed."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "1.5",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Both PDFs specify
    a chitin range1–2 g/L from a bare5% solution; the APIs supply conditional midpoint1.5
    g/L. The local1.5 plus range note can be retained only as that provider-selected
    point, not as a fixed primary prescription. The DSM1464 owner note says adjust
    volume without units and must instead preserve the explicit concentration range;
    no5% mass/volume basis or stock volume is assumed."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[4].notes", "stored_value": " (adjust volume in range
    1-2 if required)", "decision": "correct", "rationale": "Both PDFs specify a chitin
    range1–2 g/L from a bare5% solution; the APIs supply conditional midpoint1.5 g/L.
    The local1.5 plus range note can be retained only as that provider-selected point,
    not as a fixed primary prescription. The DSM1464 owner note says adjust volume
    without units and must instead preserve the explicit concentration range; no5%
    mass/volume basis or stock volume is assumed."}]}, {"quantity_id": "q6", "topic":
    "MgSO4 main final concentration", "source": [{"evidence_id": "api1464", "reference":
    "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin",
    "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"MgSO4\",\n                        \"compound_id\": 325,\n                        \"amount\":
    1,\n                        \"unit\": \"mM\",\n                        \"g_l\":
    0.12037,\n                        \"mmol_l\": 1,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "MgSO4", "compound_id": 325, "amount": 1, "unit": "mM", "g_l": 0.12037, "mmol_l":
    1, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"MgSO4\",\n                        \"compound_id\": 325,\n                        \"amount\":
    1,\n                        \"unit\": \"mM\",\n                        \"g_l\":
    0.12037,\n                        \"mmol_l\": 1,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "MgSO4", "compound_id": 325, "amount": 1, "unit": "mM", "g_l": 0.12037, "mmol_l":
    1, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "evidence_only",
    "rationale": "The primary explicitly prescribes final1 mM MgSO4. Current anhydrous
    CHEBI32599 mass120.368 gives0.120368 g/L, consistent with the provider0.12037
    rounding. Preserve native molarity and supplied anhydrous identity; do not transfer
    a hydrate mass.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.12037",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly
    prescribes final1 mM MgSO4. Current anhydrous CHEBI32599 mass120.368 gives0.120368
    g/L, consistent with the provider0.12037 rounding. Preserve native molarity and
    supplied anhydrous identity; do not transfer a hydrate mass."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.12037",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly
    prescribes final1 mM MgSO4. Current anhydrous CHEBI32599 mass120.368 gives0.120368
    g/L, consistent with the provider0.12037 rounding. Preserve native molarity and
    supplied anhydrous identity; do not transfer a hydrate mass."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.12037",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly
    prescribes final1 mM MgSO4. Current anhydrous CHEBI32599 mass120.368 gives0.120368
    g/L, consistent with the provider0.12037 rounding. Preserve native molarity and
    supplied anhydrous identity; do not transfer a hydrate mass."}]}, {"quantity_id":
    "q7", "topic": "Yeast extract main final concentration", "source": [{"evidence_id":
    "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path":
    "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\":
    20,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.02,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 8, "compound": "Yeast extract", "compound_id": 16, "amount":
    20, "unit": "mg", "g_l": 0.02, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path":
    "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\":
    20,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.02,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 8, "compound": "Yeast extract", "compound_id": 16, "amount":
    20, "unit": "mg", "g_l": 0.02, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "evidence_only", "rationale": "Primary20 mg/L equals0.02 g/L directly; both provider
    declarations and all current local values agree. No new chemical identifier or
    strain growth inference is required.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Primary20 mg/L
    equals0.02 g/L directly; both provider declarations and all current local values
    agree. No new chemical identifier or strain growth inference is required."}, {"path":
    "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "ingredients[6].concentration",
    "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "Primary20 mg/L equals0.02 g/L directly; both provider declarations
    and all current local values agree. No new chemical identifier or strain growth
    inference is required."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Primary20 mg/L
    equals0.02 g/L directly; both provider declarations and all current local values
    agree. No new chemical identifier or strain growth inference is required."}]},
    {"quantity_id": "q8", "topic": "NH4Cl main final concentration", "source": [{"evidence_id":
    "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path":
    "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\":
    4,\n                        \"unit\": \"mM\",\n                        \"g_l\":
    0.21396,\n                        \"mmol_l\": 4,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound":
    "NH4Cl", "compound_id": 42, "amount": 4, "unit": "mM", "g_l": 0.21396, "mmol_l":
    4, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\":
    4,\n                        \"unit\": \"mM\",\n                        \"g_l\":
    0.21396,\n                        \"mmol_l\": 4,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound":
    "NH4Cl", "compound_id": 42, "amount": 4, "unit": "mM", "g_l": 0.21396, "mmol_l":
    4, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "evidence_only",
    "rationale": "The primary explicitly prescribes final4 mM NH4Cl; current CHEBI31206
    mass53.492 gives0.213968 g/L. The provider0.21396 is a nearby source-rounded mass
    conversion, retained as declared provider precision rather than claiming identical
    atomic-weight precision.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.21396",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly
    prescribes final4 mM NH4Cl; current CHEBI31206 mass53.492 gives0.213968 g/L. The
    provider0.21396 is a nearby source-rounded mass conversion, retained as declared
    provider precision rather than claiming identical atomic-weight precision."},
    {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path":
    "ingredients[7].concentration", "stored_value": {"value": "0.21396", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "The primary explicitly prescribes final4
    mM NH4Cl; current CHEBI31206 mass53.492 gives0.213968 g/L. The provider0.21396
    is a nearby source-rounded mass conversion, retained as declared provider precision
    rather than claiming identical atomic-weight precision."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.21396",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The primary explicitly
    prescribes final4 mM NH4Cl; current CHEBI31206 mass53.492 gives0.213968 g/L. The
    provider0.21396 is a nearby source-rounded mass conversion, retained as declared
    provider precision rather than claiming identical atomic-weight precision."}]},
    {"quantity_id": "q9", "topic": "Na2S main final concentration", "source": [{"evidence_id":
    "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path":
    "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Na2S\",\n                        \"compound_id\": 490,\n                        \"amount\":
    1,\n                        \"unit\": \"mM\",\n                        \"g_l\":
    0.07906,\n                        \"mmol_l\": 1,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "Na2S", "compound_id": 490, "amount": 1, "unit": "mM", "g_l": 0.07906, "mmol_l":
    1, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Na2S\",\n                        \"compound_id\": 490,\n                        \"amount\":
    1,\n                        \"unit\": \"mM\",\n                        \"g_l\":
    0.07906,\n                        \"mmol_l\": 1,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "Na2S", "compound_id": 490, "amount": 1, "unit": "mM", "g_l": 0.07906, "mmol_l":
    1, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "conflict", "rationale":
    "The primary explicitly prescribes final1 mM Na2S. Both APIs declare0.07906 g/L,
    but the current exact anhydrous CHEBI76208 formula2Na.S and mass78.047 imply0.078047
    g/L at1 mM. Preserve the contradictory provider number as evidence; prefer the
    explicitly supplied native molarity pending conversion reconciliation, without
    inventing a hydrate or silently endorsing the mass value.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[8].concentration",
    "stored_value": {"value": "0.07906", "unit": "G_PER_L"}, "decision": "conflict",
    "rationale": "The primary explicitly prescribes final1 mM Na2S. Both APIs declare0.07906
    g/L, but the current exact anhydrous CHEBI76208 formula2Na.S and mass78.047 imply0.078047
    g/L at1 mM. Preserve the contradictory provider number as evidence; prefer the
    explicitly supplied native molarity pending conversion reconciliation, without
    inventing a hydrate or silently endorsing the mass value."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.07906",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary explicitly
    prescribes final1 mM Na2S. Both APIs declare0.07906 g/L, but the current exact
    anhydrous CHEBI76208 formula2Na.S and mass78.047 imply0.078047 g/L at1 mM. Preserve
    the contradictory provider number as evidence; prefer the explicitly supplied
    native molarity pending conversion reconciliation, without inventing a hydrate
    or silently endorsing the mass value."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.07906",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary explicitly
    prescribes final1 mM Na2S. Both APIs declare0.07906 g/L, but the current exact
    anhydrous CHEBI76208 formula2Na.S and mass78.047 imply0.078047 g/L at1 mM. Preserve
    the contradictory provider number as evidence; prefer the explicitly supplied
    native molarity pending conversion reconciliation, without inventing a hydrate
    or silently endorsing the mass value."}]}, {"quantity_id": "q10", "topic": "Biotin
    in Basic solution (100 ml 0.1 N NaOH)", "source": [{"evidence_id": "api1464",
    "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin",
    "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\":
    2,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Biotin", "compound_id": 46, "amount": 2, "unit": "mg", "g_l": 0.02, "mmol_l":
    0.0818632, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[3].recipe[0]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\":
    2,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Biotin", "compound_id": 46, "amount": 2, "unit": "mg", "g_l": 0.02, "mmol_l":
    0.0818632, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition, with source
    amount 2 mg and provider stock g_l=0.02; all local values reproduce that stock
    rate as a direct ingredient. Relocate it to this exact stock stage, retaining
    source amount and form. The primary specifies this100 ml subsolution. Its concentration
    is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium;
    retain both successive mixing/addition boundaries.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[12].concentration",
    "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 2
    mg and provider stock g_l=0.02; all local values reproduce that stock rate as
    a direct ingredient. Relocate it to this exact stock stage, retaining source amount
    and form. The primary specifies this100 ml subsolution. Its concentration is neither
    the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both
    successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution
    (100 ml 0.1 N NaOH) composition, with source amount 2 mg and provider stock g_l=0.02;
    all local values reproduce that stock rate as a direct ingredient. Relocate it
    to this exact stock stage, retaining source amount and form. The primary specifies
    this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed
    vitamin stock nor the receiving medium; retain both successive mixing/addition
    boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution
    (100 ml 0.1 N NaOH) composition, with source amount 2 mg and provider stock g_l=0.02;
    all local values reproduce that stock rate as a direct ingredient. Relocate it
    to this exact stock stage, retaining source amount and form. The primary specifies
    this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed
    vitamin stock nor the receiving medium; retain both successive mixing/addition
    boundaries."}]}, {"quantity_id": "q11", "topic": "PABA in Basic solution (100
    ml 0.1 N NaOH)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[2].recipe[1]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"PABA\",\n                        \"compound_id\": 1309,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "PABA", "compound_id": 1309, "amount": 5, "unit": "mg", "g_l": 0.05, "mmol_l":
    0.364591, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[3].recipe[1]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"PABA\",\n                        \"compound_id\": 1309,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "PABA", "compound_id": 1309, "amount": 5, "unit": "mg", "g_l": 0.05, "mmol_l":
    0.364591, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition, with source
    amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock
    rate as a direct ingredient. Relocate it to this exact stock stage, retaining
    source amount and form. The primary specifies this100 ml subsolution. Its concentration
    is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium;
    retain both successive mixing/addition boundaries.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[13].concentration",
    "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 5
    mg and provider stock g_l=0.05; all local values reproduce that stock rate as
    a direct ingredient. Relocate it to this exact stock stage, retaining source amount
    and form. The primary specifies this100 ml subsolution. Its concentration is neither
    the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both
    successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution
    (100 ml 0.1 N NaOH) composition, with source amount 5 mg and provider stock g_l=0.05;
    all local values reproduce that stock rate as a direct ingredient. Relocate it
    to this exact stock stage, retaining source amount and form. The primary specifies
    this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed
    vitamin stock nor the receiving medium; retain both successive mixing/addition
    boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution
    (100 ml 0.1 N NaOH) composition, with source amount 5 mg and provider stock g_l=0.05;
    all local values reproduce that stock rate as a direct ingredient. Relocate it
    to this exact stock stage, retaining source amount and form. The primary specifies
    this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed
    vitamin stock nor the receiving medium; retain both successive mixing/addition
    boundaries."}]}, {"quantity_id": "q12", "topic": "Nicotinic acid in Basic solution
    (100 ml 0.1 N NaOH)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[2].recipe[2]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "Nicotinic acid", "compound_id": 139, "amount": 5, "unit": "mg", "g_l": 0.05,
    "mmol_l": 0.406141, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path":
    "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[3].recipe[2]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "Nicotinic acid", "compound_id": 139, "amount": 5, "unit": "mg", "g_l": 0.05,
    "mmol_l": 0.406141, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition,
    with source amount 5 mg and provider stock g_l=0.05; all local values reproduce
    that stock rate as a direct ingredient. Relocate it to this exact stock stage,
    retaining source amount and form. The primary specifies this100 ml subsolution.
    Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the
    receiving medium; retain both successive mixing/addition boundaries.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[14].concentration",
    "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 5
    mg and provider stock g_l=0.05; all local values reproduce that stock rate as
    a direct ingredient. Relocate it to this exact stock stage, retaining source amount
    and form. The primary specifies this100 ml subsolution. Its concentration is neither
    the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both
    successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution
    (100 ml 0.1 N NaOH) composition, with source amount 5 mg and provider stock g_l=0.05;
    all local values reproduce that stock rate as a direct ingredient. Relocate it
    to this exact stock stage, retaining source amount and form. The primary specifies
    this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed
    vitamin stock nor the receiving medium; retain both successive mixing/addition
    boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution
    (100 ml 0.1 N NaOH) composition, with source amount 5 mg and provider stock g_l=0.05;
    all local values reproduce that stock rate as a direct ingredient. Relocate it
    to this exact stock stage, retaining source amount and form. The primary specifies
    this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed
    vitamin stock nor the receiving medium; retain both successive mixing/addition
    boundaries."}]}, {"quantity_id": "q13", "topic": "Pyridoxine in Basic solution
    (100 ml 0.1 N NaOH)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[2].recipe[3]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Pyridoxine\",\n                        \"compound_id\": 637,\n                        \"amount\":
    10,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.591086,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "Pyridoxine", "compound_id": 637, "amount": 10, "unit": "mg", "g_l": 0.1, "mmol_l":
    0.591086, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[3].recipe[3]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Pyridoxine\",\n                        \"compound_id\": 637,\n                        \"amount\":
    10,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.591086,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "Pyridoxine", "compound_id": 637, "amount": 10, "unit": "mg", "g_l": 0.1, "mmol_l":
    0.591086, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Basic solution (100 ml 0.1 N NaOH) composition, with source
    amount 10 mg and provider stock g_l=0.1; all local values reproduce that stock
    rate as a direct ingredient. Relocate it to this exact stock stage, retaining
    source amount and form. The primary specifies this100 ml subsolution. Its concentration
    is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium;
    retain both successive mixing/addition boundaries.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[15].concentration",
    "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This is Basic solution (100 ml 0.1 N NaOH) composition, with source amount 10
    mg and provider stock g_l=0.1; all local values reproduce that stock rate as a
    direct ingredient. Relocate it to this exact stock stage, retaining source amount
    and form. The primary specifies this100 ml subsolution. Its concentration is neither
    the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both
    successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution
    (100 ml 0.1 N NaOH) composition, with source amount 10 mg and provider stock g_l=0.1;
    all local values reproduce that stock rate as a direct ingredient. Relocate it
    to this exact stock stage, retaining source amount and form. The primary specifies
    this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed
    vitamin stock nor the receiving medium; retain both successive mixing/addition
    boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Basic solution
    (100 ml 0.1 N NaOH) composition, with source amount 10 mg and provider stock g_l=0.1;
    all local values reproduce that stock rate as a direct ingredient. Relocate it
    to this exact stock stage, retaining source amount and form. The primary specifies
    this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed
    vitamin stock nor the receiving medium; retain both successive mixing/addition
    boundaries."}]}, {"quantity_id": "q14", "topic": "Folic acid in Neutral solution
    (100 ml Aqua dem.)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[3].recipe[0]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\":
    2,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Folic acid", "compound_id": 138, "amount": 2, "unit": "mg", "g_l": 0.02, "mmol_l":
    0.0453104, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[4].recipe[0]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\":
    2,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Folic acid", "compound_id": 138, "amount": 2, "unit": "mg", "g_l": 0.02, "mmol_l":
    0.0453104, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Neutral solution (100 ml Aqua dem.) composition, with source
    amount 2 mg and provider stock g_l=0.02; all local values reproduce that stock
    rate as a direct ingredient. Relocate it to this exact stock stage, retaining
    source amount and form. The primary specifies this100 ml subsolution. Its concentration
    is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium;
    retain both successive mixing/addition boundaries.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[16].concentration",
    "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This is Neutral solution (100 ml Aqua dem.) composition, with source amount 2
    mg and provider stock g_l=0.02; all local values reproduce that stock rate as
    a direct ingredient. Relocate it to this exact stock stage, retaining source amount
    and form. The primary specifies this100 ml subsolution. Its concentration is neither
    the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both
    successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Neutral solution
    (100 ml Aqua dem.) composition, with source amount 2 mg and provider stock g_l=0.02;
    all local values reproduce that stock rate as a direct ingredient. Relocate it
    to this exact stock stage, retaining source amount and form. The primary specifies
    this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed
    vitamin stock nor the receiving medium; retain both successive mixing/addition
    boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Neutral solution
    (100 ml Aqua dem.) composition, with source amount 2 mg and provider stock g_l=0.02;
    all local values reproduce that stock rate as a direct ingredient. Relocate it
    to this exact stock stage, retaining source amount and form. The primary specifies
    this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed
    vitamin stock nor the receiving medium; retain both successive mixing/addition
    boundaries."}]}, {"quantity_id": "q15", "topic": "Riboflavin in Neutral solution
    (100 ml Aqua dem.)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[3].recipe[1]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "Riboflavin", "compound_id": 136, "amount": 5, "unit": "mg", "g_l": 0.05, "mmol_l":
    0.132837, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[4].recipe[1]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "Riboflavin", "compound_id": 136, "amount": 5, "unit": "mg", "g_l": 0.05, "mmol_l":
    0.132837, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Neutral solution (100 ml Aqua dem.) composition, with source
    amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock
    rate as a direct ingredient. Relocate it to this exact stock stage, retaining
    source amount and form. The primary specifies this100 ml subsolution. Its concentration
    is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium;
    retain both successive mixing/addition boundaries.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[17].concentration",
    "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This is Neutral solution (100 ml Aqua dem.) composition, with source amount 5
    mg and provider stock g_l=0.05; all local values reproduce that stock rate as
    a direct ingredient. Relocate it to this exact stock stage, retaining source amount
    and form. The primary specifies this100 ml subsolution. Its concentration is neither
    the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both
    successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Neutral solution
    (100 ml Aqua dem.) composition, with source amount 5 mg and provider stock g_l=0.05;
    all local values reproduce that stock rate as a direct ingredient. Relocate it
    to this exact stock stage, retaining source amount and form. The primary specifies
    this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed
    vitamin stock nor the receiving medium; retain both successive mixing/addition
    boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Neutral solution
    (100 ml Aqua dem.) composition, with source amount 5 mg and provider stock g_l=0.05;
    all local values reproduce that stock rate as a direct ingredient. Relocate it
    to this exact stock stage, retaining source amount and form. The primary specifies
    this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed
    vitamin stock nor the receiving medium; retain both successive mixing/addition
    boundaries."}]}, {"quantity_id": "q16", "topic": "EDTA in Acidic trace metals
    (Pfennig & Lippert, 1965)", "source": [{"evidence_id": "api1464", "reference":
    "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin",
    "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[4].recipe[0]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"EDTA\",\n                        \"compound_id\": 271,\n                        \"amount\":
    5,\n                        \"unit\": \"g/l\",\n                        \"g_l\":
    5,\n                        \"mmol_l\": 17.1092,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "EDTA", "compound_id": 271, "amount": 5, "unit": "g/l", "g_l": 5, "mmol_l": 17.1092,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[5].recipe[0]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"EDTA\",\n                        \"compound_id\": 271,\n                        \"amount\":
    5,\n                        \"unit\": \"g/l\",\n                        \"g_l\":
    5,\n                        \"mmol_l\": 17.1092,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "EDTA", "compound_id": 271, "amount": 5, "unit": "g/l", "g_l": 5, "mmol_l": 17.1092,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "correct", "rationale":
    "This is Acidic trace metals (Pfennig & Lippert, 1965) composition, with source
    amount 5 g/l and provider stock g_l=5; all local values reproduce that stock rate
    as a direct ingredient. Relocate it to this exact stock stage, retaining source
    amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L
    and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions
    belong only to this stock.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[18].concentration", "stored_value": {"value": "5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace
    metals (Pfennig & Lippert, 1965) composition, with source amount 5 g/l and provider
    stock g_l=5; all local values reproduce that stock rate as a direct ingredient.
    Relocate it to this exact stock stage, retaining source amount and form. The source
    trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L
    of the trace stock; its pH and autoclave instructions belong only to this stock."},
    {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path":
    "ingredients[18].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig & Lippert,
    1965) composition, with source amount 5 g/l and provider stock g_l=5; all local
    values reproduce that stock rate as a direct ingredient. Relocate it to this exact
    stock stage, retaining source amount and form. The source trace recipe explicitly
    uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock;
    its pH and autoclave instructions belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace
    metals (Pfennig & Lippert, 1965) composition, with source amount 5 g/l and provider
    stock g_l=5; all local values reproduce that stock rate as a direct ingredient.
    Relocate it to this exact stock stage, retaining source amount and form. The source
    trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L
    of the trace stock; its pH and autoclave instructions belong only to this stock."}]},
    {"quantity_id": "q17", "topic": "FeSO4 x 7 H2O in Acidic trace metals (Pfennig
    & Lippert, 1965)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[4].recipe[1]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\":
    2,\n                        \"unit\": \"g/l\",\n                        \"g_l\":
    2,\n                        \"mmol_l\": 7.19386,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "FeSO4 x 7 H2O", "compound_id": 12, "amount": 2, "unit": "g/l", "g_l": 2, "mmol_l":
    7.19386, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[5].recipe[1]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\":
    2,\n                        \"unit\": \"g/l\",\n                        \"g_l\":
    2,\n                        \"mmol_l\": 7.19386,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "FeSO4 x 7 H2O", "compound_id": 12, "amount": 2, "unit": "g/l", "g_l": 2, "mmol_l":
    7.19386, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Acidic trace metals (Pfennig & Lippert, 1965) composition,
    with source amount 2 g/l and provider stock g_l=2; all local values reproduce
    that stock rate as a direct ingredient. Relocate it to this exact stock stage,
    retaining source amount and form. The source trace recipe explicitly uses mg/L
    or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and
    autoclave instructions belong only to this stock.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[19].concentration",
    "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This is Acidic trace metals (Pfennig & Lippert, 1965) composition, with source
    amount 2 g/l and provider stock g_l=2; all local values reproduce that stock rate
    as a direct ingredient. Relocate it to this exact stock stage, retaining source
    amount and form. The source trace recipe explicitly uses mg/L or equivalent g/L
    and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions
    belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[19].concentration", "stored_value": {"value": "2",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace
    metals (Pfennig & Lippert, 1965) composition, with source amount 2 g/l and provider
    stock g_l=2; all local values reproduce that stock rate as a direct ingredient.
    Relocate it to this exact stock stage, retaining source amount and form. The source
    trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L
    of the trace stock; its pH and autoclave instructions belong only to this stock."},
    {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path":
    "ingredients[16].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig & Lippert,
    1965) composition, with source amount 2 g/l and provider stock g_l=2; all local
    values reproduce that stock rate as a direct ingredient. Relocate it to this exact
    stock stage, retaining source amount and form. The source trace recipe explicitly
    uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock;
    its pH and autoclave instructions belong only to this stock."}]}, {"quantity_id":
    "q18", "topic": "ZnSO4 x 7 H2O in Acidic trace metals (Pfennig & Lippert, 1965)",
    "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[4].recipe[2]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\":
    100,\n                        \"unit\": \"mg/l\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "ZnSO4 x 7 H2O", "compound_id": 35, "amount": 100, "unit": "mg/l", "g_l": 0.1,
    "mmol_l": 0.347752, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path":
    "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[5].recipe[2]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\":
    100,\n                        \"unit\": \"mg/l\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "ZnSO4 x 7 H2O", "compound_id": 35, "amount": 100, "unit": "mg/l", "g_l": 0.1,
    "mmol_l": 0.347752, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "This is Acidic trace metals (Pfennig & Lippert, 1965)
    composition, with source amount 100 mg/l and provider stock g_l=0.1; all local
    values reproduce that stock rate as a direct ingredient. Relocate it to this exact
    stock stage, retaining source amount and form. The source trace recipe explicitly
    uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock;
    its pH and autoclave instructions belong only to this stock.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[20].concentration",
    "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This is Acidic trace metals (Pfennig & Lippert, 1965) composition, with source
    amount 100 mg/l and provider stock g_l=0.1; all local values reproduce that stock
    rate as a direct ingredient. Relocate it to this exact stock stage, retaining
    source amount and form. The source trace recipe explicitly uses mg/L or equivalent
    g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions
    belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace
    metals (Pfennig & Lippert, 1965) composition, with source amount 100 mg/l and
    provider stock g_l=0.1; all local values reproduce that stock rate as a direct
    ingredient. Relocate it to this exact stock stage, retaining source amount and
    form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium
    receives1 ml/L of the trace stock; its pH and autoclave instructions belong only
    to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace
    metals (Pfennig & Lippert, 1965) composition, with source amount 100 mg/l and
    provider stock g_l=0.1; all local values reproduce that stock rate as a direct
    ingredient. Relocate it to this exact stock stage, retaining source amount and
    form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium
    receives1 ml/L of the trace stock; its pH and autoclave instructions belong only
    to this stock."}]}, {"quantity_id": "q19", "topic": "MnCl2 in Acidic trace metals
    (Pfennig & Lippert, 1965)", "source": [{"evidence_id": "api1464", "reference":
    "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin",
    "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[4].recipe[3]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"MnCl2\",\n                        \"compound_id\": 980,\n                        \"amount\":
    30,\n                        \"unit\": \"mg/l\",\n                        \"g_l\":
    0.03,\n                        \"mmol_l\": 0.238398,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "MnCl2", "compound_id": 980, "amount": 30, "unit": "mg/l", "g_l": 0.03, "mmol_l":
    0.238398, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[5].recipe[3]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"MnCl2\",\n                        \"compound_id\": 980,\n                        \"amount\":
    30,\n                        \"unit\": \"mg/l\",\n                        \"g_l\":
    0.03,\n                        \"mmol_l\": 0.238398,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "MnCl2", "compound_id": 980, "amount": 30, "unit": "mg/l", "g_l": 0.03, "mmol_l":
    0.238398, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Acidic trace metals (Pfennig & Lippert, 1965) composition,
    with source amount 30 mg/l and provider stock g_l=0.03; all local values reproduce
    that stock rate as a direct ingredient. Relocate it to this exact stock stage,
    retaining source amount and form. The source trace recipe explicitly uses mg/L
    or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and
    autoclave instructions belong only to this stock.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[21].concentration",
    "stored_value": {"value": "0.03", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This is Acidic trace metals (Pfennig & Lippert, 1965) composition, with source
    amount 30 mg/l and provider stock g_l=0.03; all local values reproduce that stock
    rate as a direct ingredient. Relocate it to this exact stock stage, retaining
    source amount and form. The source trace recipe explicitly uses mg/L or equivalent
    g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions
    belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.03",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace
    metals (Pfennig & Lippert, 1965) composition, with source amount 30 mg/l and provider
    stock g_l=0.03; all local values reproduce that stock rate as a direct ingredient.
    Relocate it to this exact stock stage, retaining source amount and form. The source
    trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L
    of the trace stock; its pH and autoclave instructions belong only to this stock."},
    {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path":
    "ingredients[18].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig & Lippert,
    1965) composition, with source amount 30 mg/l and provider stock g_l=0.03; all
    local values reproduce that stock rate as a direct ingredient. Relocate it to
    this exact stock stage, retaining source amount and form. The source trace recipe
    explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace
    stock; its pH and autoclave instructions belong only to this stock."}]}, {"quantity_id":
    "q20", "topic": "H3BO3 in Acidic trace metals (Pfennig & Lippert, 1965)", "source":
    [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[4].recipe[4]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\":
    300,\n                        \"unit\": \"mg/l\",\n                        \"g_l\":
    0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "H3BO3", "compound_id": 37, "amount": 300, "unit": "mg/l", "g_l": 0.3, "mmol_l":
    4.85123, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[5].recipe[4]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\":
    300,\n                        \"unit\": \"mg/l\",\n                        \"g_l\":
    0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "H3BO3", "compound_id": 37, "amount": 300, "unit": "mg/l", "g_l": 0.3, "mmol_l":
    4.85123, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Acidic trace metals (Pfennig & Lippert, 1965) composition,
    with source amount 300 mg/l and provider stock g_l=0.3; all local values reproduce
    that stock rate as a direct ingredient. Relocate it to this exact stock stage,
    retaining source amount and form. The source trace recipe explicitly uses mg/L
    or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and
    autoclave instructions belong only to this stock.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[22].concentration",
    "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This is Acidic trace metals (Pfennig & Lippert, 1965) composition, with source
    amount 300 mg/l and provider stock g_l=0.3; all local values reproduce that stock
    rate as a direct ingredient. Relocate it to this exact stock stage, retaining
    source amount and form. The source trace recipe explicitly uses mg/L or equivalent
    g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions
    belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace
    metals (Pfennig & Lippert, 1965) composition, with source amount 300 mg/l and
    provider stock g_l=0.3; all local values reproduce that stock rate as a direct
    ingredient. Relocate it to this exact stock stage, retaining source amount and
    form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium
    receives1 ml/L of the trace stock; its pH and autoclave instructions belong only
    to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace
    metals (Pfennig & Lippert, 1965) composition, with source amount 300 mg/l and
    provider stock g_l=0.3; all local values reproduce that stock rate as a direct
    ingredient. Relocate it to this exact stock stage, retaining source amount and
    form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium
    receives1 ml/L of the trace stock; its pH and autoclave instructions belong only
    to this stock."}]}, {"quantity_id": "q21", "topic": "CoCl2 x 6 H2O in Acidic trace
    metals (Pfennig & Lippert, 1965)", "source": [{"evidence_id": "api1464", "reference":
    "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin",
    "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[4].recipe[5]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\":
    200,\n                        \"unit\": \"mg/l\",\n                        \"g_l\":
    0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "CoCl2 x 6 H2O", "compound_id": 38, "amount": 200, "unit": "mg/l", "g_l": 0.2,
    "mmol_l": 1.54037, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path":
    "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[5].recipe[5]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\":
    200,\n                        \"unit\": \"mg/l\",\n                        \"g_l\":
    0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "CoCl2 x 6 H2O", "compound_id": 38, "amount": 200, "unit": "mg/l", "g_l": 0.2,
    "mmol_l": 1.54037, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "This is Acidic trace metals (Pfennig & Lippert, 1965)
    composition, with source amount 200 mg/l and provider stock g_l=0.2; all local
    values reproduce that stock rate as a direct ingredient. Relocate it to this exact
    stock stage, retaining source amount and form. The source trace recipe explicitly
    uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock;
    its pH and autoclave instructions belong only to this stock.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[23].concentration",
    "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This is Acidic trace metals (Pfennig & Lippert, 1965) composition, with source
    amount 200 mg/l and provider stock g_l=0.2; all local values reproduce that stock
    rate as a direct ingredient. Relocate it to this exact stock stage, retaining
    source amount and form. The source trace recipe explicitly uses mg/L or equivalent
    g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions
    belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.2",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace
    metals (Pfennig & Lippert, 1965) composition, with source amount 200 mg/l and
    provider stock g_l=0.2; all local values reproduce that stock rate as a direct
    ingredient. Relocate it to this exact stock stage, retaining source amount and
    form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium
    receives1 ml/L of the trace stock; its pH and autoclave instructions belong only
    to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.2",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace
    metals (Pfennig & Lippert, 1965) composition, with source amount 200 mg/l and
    provider stock g_l=0.2; all local values reproduce that stock rate as a direct
    ingredient. Relocate it to this exact stock stage, retaining source amount and
    form. The source trace recipe explicitly uses mg/L or equivalent g/L and the medium
    receives1 ml/L of the trace stock; its pH and autoclave instructions belong only
    to this stock."}]}, {"quantity_id": "q22", "topic": "CuCl2 in Acidic trace metals
    (Pfennig & Lippert, 1965)", "source": [{"evidence_id": "api1464", "reference":
    "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin",
    "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[4].recipe[6]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"CuCl2\",\n                        \"compound_id\": 261,\n                        \"amount\":
    10,\n                        \"unit\": \"mg/l\",\n                        \"g_l\":
    0.01,\n                        \"mmol_l\": 0.0743771,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "CuCl2", "compound_id": 261, "amount": 10, "unit": "mg/l", "g_l": 0.01, "mmol_l":
    0.0743771, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[5].recipe[6]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"CuCl2\",\n                        \"compound_id\": 261,\n                        \"amount\":
    10,\n                        \"unit\": \"mg/l\",\n                        \"g_l\":
    0.01,\n                        \"mmol_l\": 0.0743771,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "CuCl2", "compound_id": 261, "amount": 10, "unit": "mg/l", "g_l": 0.01, "mmol_l":
    0.0743771, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Acidic trace metals (Pfennig & Lippert, 1965) composition,
    with source amount 10 mg/l and provider stock g_l=0.01; all local values reproduce
    that stock rate as a direct ingredient. Relocate it to this exact stock stage,
    retaining source amount and form. The source trace recipe explicitly uses mg/L
    or equivalent g/L and the medium receives1 ml/L of the trace stock; its pH and
    autoclave instructions belong only to this stock.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[24].concentration",
    "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This is Acidic trace metals (Pfennig & Lippert, 1965) composition, with source
    amount 10 mg/l and provider stock g_l=0.01; all local values reproduce that stock
    rate as a direct ingredient. Relocate it to this exact stock stage, retaining
    source amount and form. The source trace recipe explicitly uses mg/L or equivalent
    g/L and the medium receives1 ml/L of the trace stock; its pH and autoclave instructions
    belong only to this stock."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace
    metals (Pfennig & Lippert, 1965) composition, with source amount 10 mg/l and provider
    stock g_l=0.01; all local values reproduce that stock rate as a direct ingredient.
    Relocate it to this exact stock stage, retaining source amount and form. The source
    trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L
    of the trace stock; its pH and autoclave instructions belong only to this stock."},
    {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path":
    "ingredients[21].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "This is Acidic trace metals (Pfennig & Lippert,
    1965) composition, with source amount 10 mg/l and provider stock g_l=0.01; all
    local values reproduce that stock rate as a direct ingredient. Relocate it to
    this exact stock stage, retaining source amount and form. The source trace recipe
    explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace
    stock; its pH and autoclave instructions belong only to this stock."}]}, {"quantity_id":
    "q23", "topic": "NiCl2 x 2 H2O in Acidic trace metals (Pfennig & Lippert, 1965)",
    "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[4].recipe[7]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"NiCl2 x 2 H2O\",\n                        \"compound_id\": 981,\n                        \"amount\":
    20,\n                        \"unit\": \"mg/l\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound":
    "NiCl2 x 2 H2O", "compound_id": 981, "amount": 20, "unit": "mg/l", "g_l": 0.02,
    "mmol_l": 0.154322, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path":
    "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[5].recipe[7]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"NiCl2 x 2 H2O\",\n                        \"compound_id\": 981,\n                        \"amount\":
    20,\n                        \"unit\": \"mg/l\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound":
    "NiCl2 x 2 H2O", "compound_id": 981, "amount": 20, "unit": "mg/l", "g_l": 0.02,
    "mmol_l": 0.154322, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "This is Acidic trace metals (Pfennig & Lippert, 1965)
    composition, with source amount 20 mg/l and provider stock g_l=0.02; all local
    values reproduce that stock rate as a direct ingredient. Relocate it to this exact
    stock stage, retaining source amount and form. The source trace recipe explicitly
    uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock;
    its pH and autoclave instructions belong only to this stock. The supplied dihydrate
    conflicts with the anhydrous34887 identifier; do not substitute hexahydrate.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace
    metals (Pfennig & Lippert, 1965) composition, with source amount 20 mg/l and provider
    stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient.
    Relocate it to this exact stock stage, retaining source amount and form. The source
    trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L
    of the trace stock; its pH and autoclave instructions belong only to this stock.
    The supplied dihydrate conflicts with the anhydrous34887 identifier; do not substitute
    hexahydrate."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace
    metals (Pfennig & Lippert, 1965) composition, with source amount 20 mg/l and provider
    stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient.
    Relocate it to this exact stock stage, retaining source amount and form. The source
    trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L
    of the trace stock; its pH and autoclave instructions belong only to this stock.
    The supplied dihydrate conflicts with the anhydrous34887 identifier; do not substitute
    hexahydrate."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace
    metals (Pfennig & Lippert, 1965) composition, with source amount 20 mg/l and provider
    stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient.
    Relocate it to this exact stock stage, retaining source amount and form. The source
    trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L
    of the trace stock; its pH and autoclave instructions belong only to this stock.
    The supplied dihydrate conflicts with the anhydrous34887 identifier; do not substitute
    hexahydrate."}]}, {"quantity_id": "q24", "topic": "Na2MoO4 x 2 H2O in Acidic trace
    metals (Pfennig & Lippert, 1965)", "source": [{"evidence_id": "api1464", "reference":
    "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin",
    "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[4].recipe[8]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\":
    20,\n                        \"unit\": \"mg/l\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.0826617,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound":
    "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 20, "unit": "mg/l", "g_l": 0.02,
    "mmol_l": 0.0826617, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path":
    "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[5].recipe[8]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\":
    20,\n                        \"unit\": \"mg/l\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.0826617,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound":
    "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 20, "unit": "mg/l", "g_l": 0.02,
    "mmol_l": 0.0826617, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "This is Acidic trace metals (Pfennig & Lippert, 1965)
    composition, with source amount 20 mg/l and provider stock g_l=0.02; all local
    values reproduce that stock rate as a direct ingredient. Relocate it to this exact
    stock stage, retaining source amount and form. The source trace recipe explicitly
    uses mg/L or equivalent g/L and the medium receives1 ml/L of the trace stock;
    its pH and autoclave instructions belong only to this stock. The primary alternative
    printed as NH4MoO4 remains a separate unresolved source alternative; no chemical
    formula correction is invented.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace
    metals (Pfennig & Lippert, 1965) composition, with source amount 20 mg/l and provider
    stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient.
    Relocate it to this exact stock stage, retaining source amount and form. The source
    trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L
    of the trace stock; its pH and autoclave instructions belong only to this stock.
    The primary alternative printed as NH4MoO4 remains a separate unresolved source
    alternative; no chemical formula correction is invented."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace
    metals (Pfennig & Lippert, 1965) composition, with source amount 20 mg/l and provider
    stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient.
    Relocate it to this exact stock stage, retaining source amount and form. The source
    trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L
    of the trace stock; its pH and autoclave instructions belong only to this stock.
    The primary alternative printed as NH4MoO4 remains a separate unresolved source
    alternative; no chemical formula correction is invented."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic trace
    metals (Pfennig & Lippert, 1965) composition, with source amount 20 mg/l and provider
    stock g_l=0.02; all local values reproduce that stock rate as a direct ingredient.
    Relocate it to this exact stock stage, retaining source amount and form. The source
    trace recipe explicitly uses mg/L or equivalent g/L and the medium receives1 ml/L
    of the trace stock; its pH and autoclave instructions belong only to this stock.
    The primary alternative printed as NH4MoO4 remains a separate unresolved source
    alternative; no chemical formula correction is invented."}]}, {"quantity_id":
    "q25", "topic": "Thiamin in Acidic solution (HCl, pH 3; 100 ml)", "source": [{"evidence_id":
    "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path":
    "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[5].recipe[0]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Thiamin\",\n                        \"compound_id\": 1307,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.188423,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Thiamin", "compound_id": 1307, "amount": 5, "unit": "mg", "g_l": 0.05, "mmol_l":
    0.188423, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Thiamin\",\n                        \"compound_id\": 1307,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.188423,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Thiamin", "compound_id": 1307, "amount": 5, "unit": "mg", "g_l": 0.05, "mmol_l":
    0.188423, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Acidic solution (HCl, pH 3; 100 ml) composition, with source
    amount 5 mg and provider stock g_l=0.05; all local values reproduce that stock
    rate as a direct ingredient. Relocate it to this exact stock stage, retaining
    source amount and form. The primary specifies this100 ml subsolution. Its concentration
    is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium;
    retain both successive mixing/addition boundaries.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[9].concentration",
    "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "This is Acidic solution (HCl, pH 3; 100 ml) composition, with source amount 5
    mg and provider stock g_l=0.05; all local values reproduce that stock rate as
    a direct ingredient. Relocate it to this exact stock stage, retaining source amount
    and form. The primary specifies this100 ml subsolution. Its concentration is neither
    the equal-volume1:1:1 mixed vitamin stock nor the receiving medium; retain both
    successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic solution
    (HCl, pH 3; 100 ml) composition, with source amount 5 mg and provider stock g_l=0.05;
    all local values reproduce that stock rate as a direct ingredient. Relocate it
    to this exact stock stage, retaining source amount and form. The primary specifies
    this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed
    vitamin stock nor the receiving medium; retain both successive mixing/addition
    boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic solution
    (HCl, pH 3; 100 ml) composition, with source amount 5 mg and provider stock g_l=0.05;
    all local values reproduce that stock rate as a direct ingredient. Relocate it
    to this exact stock stage, retaining source amount and form. The primary specifies
    this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed
    vitamin stock nor the receiving medium; retain both successive mixing/addition
    boundaries."}]}, {"quantity_id": "q26", "topic": "Calcium pantothenate in Acidic
    solution (HCl, pH 3; 100 ml)", "source": [{"evidence_id": "api1464", "reference":
    "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin",
    "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[5].recipe[1]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.104925,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "Calcium pantothenate", "compound_id": 518, "amount": 5, "unit": "mg", "g_l":
    0.05, "mmol_l": 0.104925, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path":
    "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[2].recipe[1]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.104925,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "Calcium pantothenate", "compound_id": 518, "amount": 5, "unit": "mg", "g_l":
    0.05, "mmol_l": 0.104925, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "This is Acidic solution (HCl, pH 3; 100 ml) composition,
    with source amount 5 mg and provider stock g_l=0.05; all local values reproduce
    that stock rate as a direct ingredient. Relocate it to this exact stock stage,
    retaining source amount and form. The primary specifies this100 ml subsolution.
    Its concentration is neither the equal-volume1:1:1 mixed vitamin stock nor the
    receiving medium; retain both successive mixing/addition boundaries. Source calcium
    pantothenate does not independently establish the stereochemistry encoded by31345.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic solution
    (HCl, pH 3; 100 ml) composition, with source amount 5 mg and provider stock g_l=0.05;
    all local values reproduce that stock rate as a direct ingredient. Relocate it
    to this exact stock stage, retaining source amount and form. The primary specifies
    this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed
    vitamin stock nor the receiving medium; retain both successive mixing/addition
    boundaries. Source calcium pantothenate does not independently establish the stereochemistry
    encoded by31345."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic solution
    (HCl, pH 3; 100 ml) composition, with source amount 5 mg and provider stock g_l=0.05;
    all local values reproduce that stock rate as a direct ingredient. Relocate it
    to this exact stock stage, retaining source amount and form. The primary specifies
    this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed
    vitamin stock nor the receiving medium; retain both successive mixing/addition
    boundaries. Source calcium pantothenate does not independently establish the stereochemistry
    encoded by31345."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic solution
    (HCl, pH 3; 100 ml) composition, with source amount 5 mg and provider stock g_l=0.05;
    all local values reproduce that stock rate as a direct ingredient. Relocate it
    to this exact stock stage, retaining source amount and form. The primary specifies
    this100 ml subsolution. Its concentration is neither the equal-volume1:1:1 mixed
    vitamin stock nor the receiving medium; retain both successive mixing/addition
    boundaries. Source calcium pantothenate does not independently establish the stereochemistry
    encoded by31345."}]}, {"quantity_id": "q27", "topic": "B12 in Acidic solution
    (HCl, pH 3; 100 ml)", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[5].recipe[2]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"B12\",\n                        \"compound_id\": 1238,\n                        \"amount\":
    0.5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.00368895,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "B12", "compound_id": 1238, "amount": 0.5, "unit": "mg", "g_l": 0.005, "mmol_l":
    0.00368895, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[2].recipe[2]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"B12\",\n                        \"compound_id\": 1238,\n                        \"amount\":
    0.5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.00368895,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "B12", "compound_id": 1238, "amount": 0.5, "unit": "mg", "g_l": 0.005, "mmol_l":
    0.00368895, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This is Acidic solution (HCl, pH 3; 100 ml) composition, with source
    amount 0.5 mg and provider stock g_l=0.005; all local values reproduce that stock
    rate as a direct ingredient. Relocate it to this exact stock stage, retaining
    source amount and form. The primary specifies this100 ml subsolution. Its concentration
    is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium;
    retain both successive mixing/addition boundaries.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ingredients[11].concentration",
    "stored_value": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct",
    "rationale": "This is Acidic solution (HCl, pH 3; 100 ml) composition, with source
    amount 0.5 mg and provider stock g_l=0.005; all local values reproduce that stock
    rate as a direct ingredient. Relocate it to this exact stock stage, retaining
    source amount and form. The primary specifies this100 ml subsolution. Its concentration
    is neither the equal-volume1:1:1 mixed vitamin stock nor the receiving medium;
    retain both successive mixing/addition boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.005",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic solution
    (HCl, pH 3; 100 ml) composition, with source amount 0.5 mg and provider stock
    g_l=0.005; all local values reproduce that stock rate as a direct ingredient.
    Relocate it to this exact stock stage, retaining source amount and form. The primary
    specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1
    mixed vitamin stock nor the receiving medium; retain both successive mixing/addition
    boundaries."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.005",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This is Acidic solution
    (HCl, pH 3; 100 ml) composition, with source amount 0.5 mg and provider stock
    g_l=0.005; all local values reproduce that stock rate as a direct ingredient.
    Relocate it to this exact stock stage, retaining source amount and form. The primary
    specifies this100 ml subsolution. Its concentration is neither the equal-volume1:1:1
    mixed vitamin stock nor the receiving medium; retain both successive mixing/addition
    boundaries."}]}, {"quantity_id": "q28", "topic": "Receiving dose 5701", "source":
    [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[0].recipe[10]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"solution\":
    \"Vitamine mixture (Pfennig & Lippert, 1965)\",\n                        \"solution_id\":
    5701,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 11, "solution": "Vitamine mixture (Pfennig & Lippert, 1965)",
    "solution_id": 5701, "amount": 1, "unit": "ml", "optional": 0}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[0].recipe[11]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\":
    \"Vitamine mixture (Pfennig & Lippert, 1965)\",\n                        \"solution_id\":
    5701,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 12, "solution": "Vitamine mixture (Pfennig & Lippert, 1965)",
    "solution_id": 5701, "amount": 1, "unit": "ml", "optional": 0}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}, {"evidence_id": "dsm1464", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf",
    "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1464.bin", "raw_sha256": "1a27d397090c1d2eb31c7c6835bc79f094c2fa88010ceb3a900b8b08e8a8f46a",
    "locator": "Primary main-medium table; extracted PDF text line 20 (1-based)",
    "accessed_at": "2026-10-28T08:34:40.751275Z", "quote": " Vitamine mixture (Pfennig
    & Lippert, 1965)             1         ml/l"}, {"evidence_id": "dsm1465", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf", "raw_path":
    "REVIEW_WORK/batch061/source01-03/dsm1465.bin", "raw_sha256": "61633d2fad4085c3cd67f6f55f7be13067816f10c93104859782df1da7cb84f6",
    "locator": "Primary main-medium table; extracted PDF text line 20 (1-based)",
    "accessed_at": "2026-10-28T08:34:41.044645Z", "quote": " Vitamine mixture (Pfennig
    & Lippert, 1965)             1         ml/l"}], "decision": "add", "rationale":
    "Both primary sources explicitly prescribe1 ml/L of this named stock. All local
    solutions blocks are absent. Create a scoped stock object and receiving dose;
    retain the ingredient compositions only inside their proper stock or substock,
    not as direct receiving-medium values.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Both primary sources explicitly prescribe1 ml/L of this named stock. All local
    solutions blocks are absent. Create a scoped stock object and receiving dose;
    retain the ingredient compositions only inside their proper stock or substock,
    not as direct receiving-medium values.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Both primary sources explicitly prescribe1 ml/L of this named stock. All local
    solutions blocks are absent. Create a scoped stock object and receiving dose;
    retain the ingredient compositions only inside their proper stock or substock,
    not as direct receiving-medium values.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Both primary sources explicitly prescribe1 ml/L of this named stock. All local
    solutions blocks are absent. Create a scoped stock object and receiving dose;
    retain the ingredient compositions only inside their proper stock or substock,
    not as direct receiving-medium values.", "missing": true}]}, {"quantity_id": "q29",
    "topic": "Receiving dose 5704", "source": [{"evidence_id": "api1464", "reference":
    "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin",
    "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[0].recipe[11]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\":
    \"Acidic trace metals (Pfennig & Lippert, 1965)\",\n                        \"solution_id\":
    5704,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 12, "solution": "Acidic trace metals (Pfennig & Lippert, 1965)",
    "solution_id": 5704, "amount": 1, "unit": "ml", "optional": 0}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[0].recipe[10]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"solution\":
    \"Acidic trace metals (Pfennig & Lippert, 1965)\",\n                        \"solution_id\":
    5704,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 11, "solution": "Acidic trace metals (Pfennig & Lippert, 1965)",
    "solution_id": 5704, "amount": 1, "unit": "ml", "optional": 0}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}, {"evidence_id": "dsm1464", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf",
    "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1464.bin", "raw_sha256": "1a27d397090c1d2eb31c7c6835bc79f094c2fa88010ceb3a900b8b08e8a8f46a",
    "locator": "Primary main-medium table; extracted PDF text line 19 (1-based)",
    "accessed_at": "2026-10-28T08:34:40.751275Z", "quote": " Acidic trace metals (Pfennig
    & Lippert, 1965)          1         ml/l"}, {"evidence_id": "dsm1465", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf", "raw_path":
    "REVIEW_WORK/batch061/source01-03/dsm1465.bin", "raw_sha256": "61633d2fad4085c3cd67f6f55f7be13067816f10c93104859782df1da7cb84f6",
    "locator": "Primary main-medium table; extracted PDF text line 19 (1-based)",
    "accessed_at": "2026-10-28T08:34:41.044645Z", "quote": " Acidic trace metals (Pfennig
    & Lippert, 1965)          1         ml/l"}], "decision": "add", "rationale": "Both
    primary sources explicitly prescribe1 ml/L of this named stock. All local solutions
    blocks are absent. Create a scoped stock object and receiving dose; retain the
    ingredient compositions only inside their proper stock or substock, not as direct
    receiving-medium values.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Both primary sources explicitly prescribe1 ml/L of this named stock. All local
    solutions blocks are absent. Create a scoped stock object and receiving dose;
    retain the ingredient compositions only inside their proper stock or substock,
    not as direct receiving-medium values.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Both primary sources explicitly prescribe1 ml/L of this named stock. All local
    solutions blocks are absent. Create a scoped stock object and receiving dose;
    retain the ingredient compositions only inside their proper stock or substock,
    not as direct receiving-medium values.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Both primary sources explicitly prescribe1 ml/L of this named stock. All local
    solutions blocks are absent. Create a scoped stock object and receiving dose;
    retain the ingredient compositions only inside their proper stock or substock,
    not as direct receiving-medium values.", "missing": true}]}, {"quantity_id": "q30",
    "topic": "Vitamin mixture aliquot Basic solution (100 ml 0.1 N NaOH)", "source":
    [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\":
    \"Basic solution (100 ml 0.1 N NaOH)\",\n                        \"solution_id\":
    5702,\n                        \"amount\": 50,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 1, "solution": "Basic solution (100 ml 0.1 N NaOH)", "solution_id":
    5702, "amount": 50, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."},
    {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\":
    \"Basic solution (100 ml 0.1 N NaOH)\",\n                        \"solution_id\":
    5702,\n                        \"amount\": 50,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 1, "solution": "Basic solution (100 ml 0.1 N NaOH)", "solution_id":
    5702, "amount": 50, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "add", "rationale": "The API vitamin-mixture recipe supplies50 ml
    of this subsolution, with total provider volume150 ml. The primary instead gives
    the scale-free1:1:1 volume ratio. Preserve50 ml as the provider realization of
    that ratio, not a required primary batch size or a100 ml receiving dose.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "The API vitamin-mixture
    recipe supplies50 ml of this subsolution, with total provider volume150 ml. The
    primary instead gives the scale-free1:1:1 volume ratio. Preserve50 ml as the provider
    realization of that ratio, not a required primary batch size or a100 ml receiving
    dose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The API vitamin-mixture recipe supplies50 ml of this subsolution, with total
    provider volume150 ml. The primary instead gives the scale-free1:1:1 volume ratio.
    Preserve50 ml as the provider realization of that ratio, not a required primary
    batch size or a100 ml receiving dose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The API vitamin-mixture recipe supplies50 ml of this subsolution, with total
    provider volume150 ml. The primary instead gives the scale-free1:1:1 volume ratio.
    Preserve50 ml as the provider realization of that ratio, not a required primary
    batch size or a100 ml receiving dose.", "missing": true}]}, {"quantity_id": "q31",
    "topic": "Vitamin mixture aliquot Neutral solution (100 ml Aqua dem.)", "source":
    [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\":
    \"Neutral solution (100 ml Aqua dem.)\",\n                        \"solution_id\":
    5703,\n                        \"amount\": 50,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 2, "solution": "Neutral solution (100 ml Aqua dem.)", "solution_id":
    5703, "amount": 50, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."},
    {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\":
    \"Neutral solution (100 ml Aqua dem.)\",\n                        \"solution_id\":
    5703,\n                        \"amount\": 50,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 2, "solution": "Neutral solution (100 ml Aqua dem.)", "solution_id":
    5703, "amount": 50, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "add", "rationale": "The API vitamin-mixture recipe supplies50 ml
    of this subsolution, with total provider volume150 ml. The primary instead gives
    the scale-free1:1:1 volume ratio. Preserve50 ml as the provider realization of
    that ratio, not a required primary batch size or a100 ml receiving dose.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "The API vitamin-mixture
    recipe supplies50 ml of this subsolution, with total provider volume150 ml. The
    primary instead gives the scale-free1:1:1 volume ratio. Preserve50 ml as the provider
    realization of that ratio, not a required primary batch size or a100 ml receiving
    dose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The API vitamin-mixture recipe supplies50 ml of this subsolution, with total
    provider volume150 ml. The primary instead gives the scale-free1:1:1 volume ratio.
    Preserve50 ml as the provider realization of that ratio, not a required primary
    batch size or a100 ml receiving dose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The API vitamin-mixture recipe supplies50 ml of this subsolution, with total
    provider volume150 ml. The primary instead gives the scale-free1:1:1 volume ratio.
    Preserve50 ml as the provider realization of that ratio, not a required primary
    batch size or a100 ml receiving dose.", "missing": true}]}, {"quantity_id": "q32",
    "topic": "Vitamin mixture aliquot Acidic solution (HCl, pH 3; 100 ml)", "source":
    [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\":
    \"Acidic solution (HCl, pH 3; 100 ml)\",\n                        \"solution_id\":
    5705,\n                        \"amount\": 50,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 3, "solution": "Acidic solution (HCl, pH 3; 100 ml)", "solution_id":
    5705, "amount": 50, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."},
    {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\":
    \"Acidic solution (HCl, pH 3; 100 ml)\",\n                        \"solution_id\":
    5705,\n                        \"amount\": 50,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 3, "solution": "Acidic solution (HCl, pH 3; 100 ml)", "solution_id":
    5705, "amount": 50, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "add", "rationale": "The API vitamin-mixture recipe supplies50 ml
    of this subsolution, with total provider volume150 ml. The primary instead gives
    the scale-free1:1:1 volume ratio. Preserve50 ml as the provider realization of
    that ratio, not a required primary batch size or a100 ml receiving dose.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "The API vitamin-mixture
    recipe supplies50 ml of this subsolution, with total provider volume150 ml. The
    primary instead gives the scale-free1:1:1 volume ratio. Preserve50 ml as the provider
    realization of that ratio, not a required primary batch size or a100 ml receiving
    dose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The API vitamin-mixture recipe supplies50 ml of this subsolution, with total
    provider volume150 ml. The primary instead gives the scale-free1:1:1 volume ratio.
    Preserve50 ml as the provider realization of that ratio, not a required primary
    batch size or a100 ml receiving dose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The API vitamin-mixture recipe supplies50 ml of this subsolution, with total
    provider volume150 ml. The primary instead gives the scale-free1:1:1 volume ratio.
    Preserve50 ml as the provider realization of that ratio, not a required primary
    batch size or a100 ml receiving dose.", "missing": true}]}, {"quantity_id": "q33",
    "topic": "Main recipe solvent context", "source": [{"evidence_id": "api1464",
    "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin",
    "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "Main1000 ml water
    is explicitly provider data; neither primary PDF states this as a main water/makeup
    instruction. Preserve that source attribution without changing a mineral g/L basis
    or inventing a measured final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml",
    "field_path": "notes", "stored_value": "Source: DSMZ | Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf",
    "decision": "add", "rationale": "Main1000 ml water is explicitly provider data;
    neither primary PDF states this as a main water/makeup instruction. Preserve that
    source attribution without changing a mineral g/L basis or inventing a measured
    final volume."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "notes", "stored_value": "Source: DSMZ | Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf",
    "decision": "add", "rationale": "Main1000 ml water is explicitly provider data;
    neither primary PDF states this as a main water/makeup instruction. Preserve that
    source attribution without changing a mineral g/L basis or inventing a measured
    final volume."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "notes", "stored_value": "Source: DSMZ | Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf",
    "decision": "add", "rationale": "Main1000 ml water is explicitly provider data;
    neither primary PDF states this as a main water/makeup instruction. Preserve that
    source attribution without changing a mineral g/L basis or inventing a measured
    final volume."}]}, {"quantity_id": "q34", "topic": "Basic solution (100 ml 0.1
    N NaOH) solvent context", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[2].recipe[4]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    100,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "Distilled water", "compound_id": 4, "amount": 100, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[3].recipe[4]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    100,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "Distilled water", "compound_id": 4, "amount": 100, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "The source stock
    stage is Basic solution (100 ml 0.1 N NaOH). Preserve the API solvent amount at
    that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the
    API plain-water row cannot replace that solvent chemistry; for the acidic solution
    retain HCl/pH3. No adjustment volume is given.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "The source stock stage
    is Basic solution (100 ml 0.1 N NaOH). Preserve the API solvent amount at that
    stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the API
    plain-water row cannot replace that solvent chemistry; for the acidic solution
    retain HCl/pH3. No adjustment volume is given.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The source stock stage is Basic solution (100 ml 0.1 N NaOH). Preserve the API
    solvent amount at that stage. For the basic solution the primary requires100 ml0.1
    N NaOH, so the API plain-water row cannot replace that solvent chemistry; for
    the acidic solution retain HCl/pH3. No adjustment volume is given.", "missing":
    true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "The source
    stock stage is Basic solution (100 ml 0.1 N NaOH). Preserve the API solvent amount
    at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so
    the API plain-water row cannot replace that solvent chemistry; for the acidic
    solution retain HCl/pH3. No adjustment volume is given.", "missing": true}]},
    {"quantity_id": "q35", "topic": "Neutral solution (100 ml Aqua dem.) solvent context",
    "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[3].recipe[2]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    100,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "Distilled water", "compound_id": 4, "amount": 100, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[4].recipe[2]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    100,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "Distilled water", "compound_id": 4, "amount": 100, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "The source stock
    stage is Neutral solution (100 ml Aqua dem.). Preserve the API solvent amount
    at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so
    the API plain-water row cannot replace that solvent chemistry; for the acidic
    solution retain HCl/pH3. No adjustment volume is given.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "The source stock stage
    is Neutral solution (100 ml Aqua dem.). Preserve the API solvent amount at that
    stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the API
    plain-water row cannot replace that solvent chemistry; for the acidic solution
    retain HCl/pH3. No adjustment volume is given.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The source stock stage is Neutral solution (100 ml Aqua dem.). Preserve the API
    solvent amount at that stage. For the basic solution the primary requires100 ml0.1
    N NaOH, so the API plain-water row cannot replace that solvent chemistry; for
    the acidic solution retain HCl/pH3. No adjustment volume is given.", "missing":
    true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "The source
    stock stage is Neutral solution (100 ml Aqua dem.). Preserve the API solvent amount
    at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so
    the API plain-water row cannot replace that solvent chemistry; for the acidic
    solution retain HCl/pH3. No adjustment volume is given.", "missing": true}]},
    {"quantity_id": "q36", "topic": "Acidic trace metals (Pfennig & Lippert, 1965)
    solvent context", "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[4].recipe[9]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[5].recipe[9]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "The source stock
    stage is Acidic trace metals (Pfennig & Lippert, 1965). Preserve the API solvent
    amount at that stage. For the basic solution the primary requires100 ml0.1 N NaOH,
    so the API plain-water row cannot replace that solvent chemistry; for the acidic
    solution retain HCl/pH3. No adjustment volume is given.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "The source stock stage
    is Acidic trace metals (Pfennig & Lippert, 1965). Preserve the API solvent amount
    at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so
    the API plain-water row cannot replace that solvent chemistry; for the acidic
    solution retain HCl/pH3. No adjustment volume is given.", "missing": true}, {"path":
    "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "The source stock stage
    is Acidic trace metals (Pfennig & Lippert, 1965). Preserve the API solvent amount
    at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so
    the API plain-water row cannot replace that solvent chemistry; for the acidic
    solution retain HCl/pH3. No adjustment volume is given.", "missing": true}, {"path":
    "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "The source stock stage
    is Acidic trace metals (Pfennig & Lippert, 1965). Preserve the API solvent amount
    at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so
    the API plain-water row cannot replace that solvent chemistry; for the acidic
    solution retain HCl/pH3. No adjustment volume is given.", "missing": true}]},
    {"quantity_id": "q37", "topic": "Acidic solution (HCl, pH 3; 100 ml) solvent context",
    "source": [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[5].recipe[3]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    100,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "Distilled water", "compound_id": 4, "amount": 100, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[2].recipe[3]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    100,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "Distilled water", "compound_id": 4, "amount": 100, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "The source stock
    stage is Acidic solution (HCl, pH 3; 100 ml). Preserve the API solvent amount
    at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so
    the API plain-water row cannot replace that solvent chemistry; for the acidic
    solution retain HCl/pH3. No adjustment volume is given.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "The source stock stage
    is Acidic solution (HCl, pH 3; 100 ml). Preserve the API solvent amount at that
    stage. For the basic solution the primary requires100 ml0.1 N NaOH, so the API
    plain-water row cannot replace that solvent chemistry; for the acidic solution
    retain HCl/pH3. No adjustment volume is given.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The source stock stage is Acidic solution (HCl, pH 3; 100 ml). Preserve the API
    solvent amount at that stage. For the basic solution the primary requires100 ml0.1
    N NaOH, so the API plain-water row cannot replace that solvent chemistry; for
    the acidic solution retain HCl/pH3. No adjustment volume is given.", "missing":
    true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "The source
    stock stage is Acidic solution (HCl, pH 3; 100 ml). Preserve the API solvent amount
    at that stage. For the basic solution the primary requires100 ml0.1 N NaOH, so
    the API plain-water row cannot replace that solvent chemistry; for the acidic
    solution retain HCl/pH3. No adjustment volume is given.", "missing": true}]},
    {"quantity_id": "q38", "topic": "Preparation stage 1", "source": [{"evidence_id":
    "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path":
    "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"step\":
    \"Adjust pH to 10.0 with NaOH or HCl. Make anoxic under nitrogen stream and autoclave
    at 121\\u00b0C.\"\n                    }", "exact_decoded_object": {"recipe_order":
    6, "step": "Adjust pH to 10.0 with NaOH or HCl. Make anoxic under nitrogen stream
    and autoclave at 121°C."}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"step\":
    \"Adjust pH to 10.0 with NaOH or HCl. Make anoxic under nitrogen stream and autoclave
    at 121\\u00b0C.\"\n                    }", "exact_decoded_object": {"recipe_order":
    6, "step": "Adjust pH to 10.0 with NaOH or HCl. Make anoxic under nitrogen stream
    and autoclave at 121°C."}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "evidence_only",
    "rationale": "The retained mineral-base text is supported: pH10 with NaOH or HCl,
    nitrogen and121°C. Autoclave duration and titrant amounts are not supplied; do
    not infer them.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml",
    "field_path": "preparation_steps[0]", "stored_value": {"step_number": 1, "action":
    "AUTOCLAVE", "description": "Adjust pH to 10.0 with NaOH or HCl. Make anoxic under
    nitrogen stream and autoclave at 121°C."}, "decision": "evidence_only", "rationale":
    "The retained mineral-base text is supported: pH10 with NaOH or HCl, nitrogen
    and121°C. Autoclave duration and titrant amounts are not supplied; do not infer
    them."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "preparation_steps[0]", "stored_value": {"step_number": 1, "action":
    "AUTOCLAVE", "description": "Adjust pH to 10.0 with NaOH or HCl. Make anoxic under
    nitrogen stream and autoclave at 121°C."}, "decision": "evidence_only", "rationale":
    "The retained mineral-base text is supported: pH10 with NaOH or HCl, nitrogen
    and121°C. Autoclave duration and titrant amounts are not supplied; do not infer
    them."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "preparation_steps[0]", "stored_value": {"step_number": 1, "action":
    "AUTOCLAVE", "description": "Adjust pH to 10.0 with NaOH or HCl. Make anoxic under
    nitrogen stream and autoclave at 121°C."}, "decision": "evidence_only", "rationale":
    "The retained mineral-base text is supported: pH10 with NaOH or HCl, nitrogen
    and121°C. Autoclave duration and titrant amounts are not supplied; do not infer
    them."}]}, {"quantity_id": "q39", "topic": "Preparation stage 2", "source": [{"evidence_id":
    "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path":
    "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[0].steps[1]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"step\":
    \"After autoclaving add sterile, anoxic solutions of:\"\n                    }",
    "exact_decoded_object": {"recipe_order": 6, "step": "After autoclaving add sterile,
    anoxic solutions of:"}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "api1465",
    "reference": "https://mediadive.dsmz.de/rest/medium/1465", "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin",
    "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[0].steps[1]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"step\":
    \"After autoclaving add sterile, anoxic solutions of:\"\n                    }",
    "exact_decoded_object": {"recipe_order": 6, "step": "After autoclaving add sterile,
    anoxic solutions of:"}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "The post-autoclave introduction is retained but dangling. Connect
    it to the explicitly enumerated sterile anoxic supplements, amounts and source
    forms, rather than treating it as a complete standalone mixing instruction.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml",
    "field_path": "preparation_steps[1]", "stored_value": {"step_number": 2, "action":
    "MIX", "description": "After autoclaving add sterile, anoxic solutions of:"},
    "decision": "correct", "rationale": "The post-autoclave introduction is retained
    but dangling. Connect it to the explicitly enumerated sterile anoxic supplements,
    amounts and source forms, rather than treating it as a complete standalone mixing
    instruction."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "preparation_steps[1]", "stored_value": {"step_number": 2, "action":
    "MIX", "description": "After autoclaving add sterile, anoxic solutions of:"},
    "decision": "correct", "rationale": "The post-autoclave introduction is retained
    but dangling. Connect it to the explicitly enumerated sterile anoxic supplements,
    amounts and source forms, rather than treating it as a complete standalone mixing
    instruction."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "preparation_steps[1]", "stored_value": {"step_number": 2, "action":
    "MIX", "description": "After autoclaving add sterile, anoxic solutions of:"},
    "decision": "correct", "rationale": "The post-autoclave introduction is retained
    but dangling. Connect it to the explicitly enumerated sterile anoxic supplements,
    amounts and source forms, rather than treating it as a complete standalone mixing
    instruction."}]}, {"quantity_id": "q40", "topic": "Preparation stage 3", "source":
    [{"evidence_id": "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"step\": \"Sterilize by filtration and keep
    at 4\\u00b0C. Before addition to the medium mix 1:1:1 (vol:vol:vol).\"\n                    }",
    "exact_decoded_object": {"step": "Sterilize by filtration and keep at 4°C. Before
    addition to the medium mix 1:1:1 (vol:vol:vol)."}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."},
    {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"step\": \"Sterilize by filtration and keep
    at 4\\u00b0C. Before addition to the medium mix 1:1:1 (vol:vol:vol).\"\n                    }",
    "exact_decoded_object": {"step": "Sterilize by filtration and keep at 4°C. Before
    addition to the medium mix 1:1:1 (vol:vol:vol)."}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "correct", "rationale": "This instruction belongs to the vitamin mixture/subsolutions:
    filtration,4°C storage and1:1:1 equal-volume mixing before receiving-medium addition.
    Its current HEAT action is wrong and top-level placement lacks stock scope; retain
    the source text and replace with accurately scoped schema-valid actions.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "preparation_steps[2]",
    "stored_value": {"step_number": 3, "action": "HEAT", "description": "Sterilize
    by filtration and keep at 4°C. Before addition to the medium mix 1:1:1 (vol:vol:vol)."},
    "decision": "correct", "rationale": "This instruction belongs to the vitamin mixture/subsolutions:
    filtration,4°C storage and1:1:1 equal-volume mixing before receiving-medium addition.
    Its current HEAT action is wrong and top-level placement lacks stock scope; retain
    the source text and replace with accurately scoped schema-valid actions."}, {"path":
    "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml", "field_path": "preparation_steps[2]",
    "stored_value": {"step_number": 3, "action": "HEAT", "description": "Sterilize
    by filtration and keep at 4°C. Before addition to the medium mix 1:1:1 (vol:vol:vol)."},
    "decision": "correct", "rationale": "This instruction belongs to the vitamin mixture/subsolutions:
    filtration,4°C storage and1:1:1 equal-volume mixing before receiving-medium addition.
    Its current HEAT action is wrong and top-level placement lacks stock scope; retain
    the source text and replace with accurately scoped schema-valid actions."}, {"path":
    "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path": "preparation_steps[2]",
    "stored_value": {"step_number": 3, "action": "HEAT", "description": "Sterilize
    by filtration and keep at 4°C. Before addition to the medium mix 1:1:1 (vol:vol:vol)."},
    "decision": "correct", "rationale": "This instruction belongs to the vitamin mixture/subsolutions:
    filtration,4°C storage and1:1:1 equal-volume mixing before receiving-medium addition.
    Its current HEAT action is wrong and top-level placement lacks stock scope; retain
    the source text and replace with accurately scoped schema-valid actions."}]},
    {"quantity_id": "q41", "topic": "Preparation stage 4", "source": [{"evidence_id":
    "api1464", "reference": "https://mediadive.dsmz.de/rest/medium/1464", "raw_path":
    "REVIEW_WORK/batch061/source01-03/api1464.bin", "raw_sha256": "a7fd66ea6a4d43e8c7656b4e598ff835b5b6d7e01d302d4fc5d2f185e6a42578",
    "locator": "$.data.solutions[4].steps[0]", "accessed_at": "2026-10-28T08:34:40.418030Z",
    "quote": "{\n                        \"step\": \"adjust pH to 3-4 with HCl; autoclave
    in closed bottles, 120\\u00b0C, 20 min.\"\n                    }", "exact_decoded_object":
    {"step": "adjust pH to 3-4 with HCl; autoclave in closed bottles, 120°C, 20 min."},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "api1465", "reference": "https://mediadive.dsmz.de/rest/medium/1465",
    "raw_path": "REVIEW_WORK/batch061/source01-03/api1465.bin", "raw_sha256": "0cd6a09835da55f21127e659ed203340e09879f609744c4c732dc151daa94886",
    "locator": "$.data.solutions[5].steps[0]", "accessed_at": "2026-10-28T08:34:40.867549Z",
    "quote": "{\n                        \"step\": \"adjust pH to 3-4 with HCl; autoclave
    in closed bottles, 120\\u00b0C, 20 min.\"\n                    }", "exact_decoded_object":
    {"step": "adjust pH to 3-4 with HCl; autoclave in closed bottles, 120°C, 20 min."},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "correct", "rationale": "This instruction
    belongs only to the acidic trace stock: pH3–4 with HCl and closed-bottle autoclave120°C20
    min. It must not replace the main pH10/121°C preparation. Preserve the numeric
    stock conditions while relocating their scope.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "preparation_steps[3]",
    "stored_value": {"step_number": 4, "action": "AUTOCLAVE", "description": "adjust
    pH to 3-4 with HCl; autoclave in closed bottles, 120°C, 20 min."}, "decision":
    "correct", "rationale": "This instruction belongs only to the acidic trace stock:
    pH3–4 with HCl and closed-bottle autoclave120°C20 min. It must not replace the
    main pH10/121°C preparation. Preserve the numeric stock conditions while relocating
    their scope."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "preparation_steps[3]", "stored_value": {"step_number": 4, "action":
    "AUTOCLAVE", "description": "adjust pH to 3-4 with HCl; autoclave in closed bottles,
    120°C, 20 min."}, "decision": "correct", "rationale": "This instruction belongs
    only to the acidic trace stock: pH3–4 with HCl and closed-bottle autoclave120°C20
    min. It must not replace the main pH10/121°C preparation. Preserve the numeric
    stock conditions while relocating their scope."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "preparation_steps[3]", "stored_value": {"step_number": 4, "action":
    "AUTOCLAVE", "description": "adjust pH to 3-4 with HCl; autoclave in closed bottles,
    120°C, 20 min."}, "decision": "correct", "rationale": "This instruction belongs
    only to the acidic trace stock: pH3–4 with HCl and closed-bottle autoclave120°C20
    min. It must not replace the main pH10/121°C preparation. Preserve the numeric
    stock conditions while relocating their scope."}]}, {"quantity_id": "q42", "topic":
    "Main pH10", "source": [{"evidence_id": "dsm1464", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf",
    "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1464.bin", "raw_sha256": "1a27d397090c1d2eb31c7c6835bc79f094c2fa88010ceb3a900b8b08e8a8f46a",
    "locator": "Page1 mineral preparation", "accessed_at": "2026-10-28T08:34:40.751275Z",
    "quote": "Adjust pH to 10.0 with NaOH or HCl."}, {"evidence_id": "dsm1465", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf", "raw_path":
    "REVIEW_WORK/batch061/source01-03/dsm1465.bin", "raw_sha256": "61633d2fad4085c3cd67f6f55f7be13067816f10c93104859782df1da7cb84f6",
    "locator": "Page1 mineral preparation", "accessed_at": "2026-10-28T08:34:41.044645Z",
    "quote": "Adjust pH to 10.0 with NaOH or HCl."}], "decision": "evidence_only",
    "rationale": "Retained main pH is supported and is not a stock pH.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "ph_value",
    "stored_value": 10.0, "decision": "evidence_only", "rationale": "The explicit
    main pH10 is retained; stock pH3/3–4 is separate."}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "ph_value", "stored_value": 10.0, "decision": "evidence_only", "rationale":
    "The explicit main pH10 is retained; stock pH3/3–4 is separate."}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "ph_value", "stored_value": 10.0, "decision": "evidence_only", "rationale":
    "The explicit main pH10 is retained; stock pH3/3–4 is separate."}]}, {"quantity_id":
    "q43", "topic": "Acidic vitamin preparation", "source": [{"evidence_id": "dsm1464",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf",
    "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1464.bin", "raw_sha256": "1a27d397090c1d2eb31c7c6835bc79f094c2fa88010ceb3a900b8b08e8a8f46a",
    "locator": "Exact scoped primary paragraph", "accessed_at": "2026-10-28T08:34:40.751275Z",
    "quote": "1: acidic solution (HCl, pH 3; 100 ml)"}, {"evidence_id": "dsm1465",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf",
    "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1465.bin", "raw_sha256": "61633d2fad4085c3cd67f6f55f7be13067816f10c93104859782df1da7cb84f6",
    "locator": "Exact scoped primary paragraph", "accessed_at": "2026-10-28T08:34:41.044645Z",
    "quote": "1: acidic solution (HCl, pH 3; 100 ml)"}], "decision": "add", "rationale":
    "Preserve HCl/pH3 and100 ml acidic subsolution identity. No HCl strength or titrant
    volume is supplied.", "layer_assessments": [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Preserve HCl/pH3 and100 ml acidic subsolution identity. No HCl strength or titrant
    volume is supplied.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Preserve HCl/pH3 and100 ml acidic subsolution identity. No HCl strength or titrant
    volume is supplied.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Preserve HCl/pH3 and100 ml acidic subsolution identity. No HCl strength or titrant
    volume is supplied.", "missing": true}]}, {"quantity_id": "q44", "topic": "Basic
    vitamin preparation", "source": [{"evidence_id": "dsm1464", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf",
    "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1464.bin", "raw_sha256": "1a27d397090c1d2eb31c7c6835bc79f094c2fa88010ceb3a900b8b08e8a8f46a",
    "locator": "Exact scoped primary paragraph", "accessed_at": "2026-10-28T08:34:40.751275Z",
    "quote": "2: basic solution (100 ml 0.1 N NaOH)"}, {"evidence_id": "dsm1465",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf",
    "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1465.bin", "raw_sha256": "61633d2fad4085c3cd67f6f55f7be13067816f10c93104859782df1da7cb84f6",
    "locator": "Exact scoped primary paragraph", "accessed_at": "2026-10-28T08:34:41.044645Z",
    "quote": "2: basic solution (100 ml 0.1 N NaOH)"}], "decision": "add", "rationale":
    "Preserve100 ml0.1 N NaOH at the basic vitamin stage. Do not replace the specified
    solvent by plain API distilled-water context.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "Preserve100 ml0.1 N NaOH
    at the basic vitamin stage. Do not replace the specified solvent by plain API
    distilled-water context.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Preserve100 ml0.1 N NaOH at the basic vitamin stage. Do not replace the specified
    solvent by plain API distilled-water context.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Preserve100 ml0.1 N NaOH at the basic vitamin stage. Do not replace the specified
    solvent by plain API distilled-water context.", "missing": true}]}, {"quantity_id":
    "q45", "topic": "Neutral vitamin preparation", "source": [{"evidence_id": "dsm1464",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf",
    "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1464.bin", "raw_sha256": "1a27d397090c1d2eb31c7c6835bc79f094c2fa88010ceb3a900b8b08e8a8f46a",
    "locator": "Exact scoped primary paragraph", "accessed_at": "2026-10-28T08:34:40.751275Z",
    "quote": "3: Neutral solution (100 ml Aqua dem.)"}, {"evidence_id": "dsm1465",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf",
    "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1465.bin", "raw_sha256": "61633d2fad4085c3cd67f6f55f7be13067816f10c93104859782df1da7cb84f6",
    "locator": "Exact scoped primary paragraph", "accessed_at": "2026-10-28T08:34:41.044645Z",
    "quote": "3: Neutral solution (100 ml Aqua dem.)"}], "decision": "add", "rationale":
    "Preserve100 ml demineralized water at the neutral vitamin stage.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "Preserve100 ml demineralized
    water at the neutral vitamin stage.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Preserve100 ml demineralized water at the neutral vitamin stage.", "missing":
    true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "Preserve100
    ml demineralized water at the neutral vitamin stage.", "missing": true}]}, {"quantity_id":
    "q46", "topic": "Molybdate source alternative", "source": [{"evidence_id": "dsm1464",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf",
    "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1464.bin", "raw_sha256": "1a27d397090c1d2eb31c7c6835bc79f094c2fa88010ceb3a900b8b08e8a8f46a",
    "locator": "Primary acidic trace-metal stock table; extracted PDF text line 33
    (1-based)", "accessed_at": "2026-10-28T08:34:40.751275Z", "quote": "9. Na2MoO4
    x 2H2O or NH4MoO4                                      20 mg/l"}, {"evidence_id":
    "dsm1465", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf",
    "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1465.bin", "raw_sha256": "61633d2fad4085c3cd67f6f55f7be13067816f10c93104859782df1da7cb84f6",
    "locator": "Primary acidic trace-metal stock table; extracted PDF text line 34
    (1-based)", "accessed_at": "2026-10-28T08:34:41.044645Z", "quote": "9. Na2MoO4
    x 2H2O or NH4MoO4                                      20 mg/l"}], "decision":
    "add", "rationale": "Retain the printed alternative and its20 mg/L trace-stock
    context. The API selects sodium molybdate dihydrate; it does not authenticate
    or correct the alternative formula or authorize adding both.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "add", "rationale": "Retain the printed alternative
    and its20 mg/L trace-stock context. The API selects sodium molybdate dihydrate;
    it does not authenticate or correct the alternative formula or authorize adding
    both.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinispirillum_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain the printed alternative and its20 mg/L trace-stock context. The API selects
    sodium molybdate dihydrate; it does not authenticate or correct the alternative
    formula or authorize adding both.", "missing": true}, {"path": "data/normalized_yaml/bacterial/chitinivibrio_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Retain the printed alternative and its20 mg/L trace-stock context. The API selects
    sodium molybdate dihydrate; it does not authenticate or correct the alternative
    formula or authorize adding both.", "missing": true}]}, {"quantity_id": "q47",
    "topic": "Unspecified late-stock doses", "source": [{"evidence_id": "dsm1464",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1464.pdf",
    "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1464.bin", "raw_sha256": "1a27d397090c1d2eb31c7c6835bc79f094c2fa88010ceb3a900b8b08e8a8f46a",
    "locator": "Exact scoped primary paragraph", "accessed_at": "2026-10-28T08:34:40.751275Z",
    "quote": "After autoclaving add sterile, anoxic solutions of:"}, {"evidence_id":
    "dsm1465", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1465.pdf",
    "raw_path": "REVIEW_WORK/batch061/source01-03/dsm1465.bin", "raw_sha256": "61633d2fad4085c3cd67f6f55f7be13067816f10c93104859782df1da7cb84f6",
    "locator": "Exact scoped primary paragraph", "accessed_at": "2026-10-28T08:34:41.044645Z",
    "quote": "After autoclaving add sterile, anoxic solutions of:"}], "decision":
    "unsupported", "rationale": "The primary gives final concentrations, specific
    trace/vitamin additions and a bare5% chitin solution, but not every late-stock
    strength or addition volume, autoclave duration, titrant volume or percentage
    basis. Leave these unresolved instead of choosing typical values.", "layer_assessments":
    []}]'
- assessment_id: a4
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: concern
  summary: All current recursive chemical slots, labels and exact MIM rows were checked
    against fresh OLS objects. Preserve the owner chitin repair and supported sulfate/metal
    forms; nickel dihydrate versus anhydrous34887 is a confirmed mismatch. Generic
    calcium pantothenate does not authenticate CHEBI:31345 stereochemistry, and thiamine
    cation does not establish a counterion. Current catalog REJECTED/MAPPED alternatives
    remain explicit rather than treated as universal authority.
  target_ids:
  - CultureMech:000930
  evidence_ids:
  - grounding
- assessment_id: a5
  area: provenance
  topic: History and evidence scope
  outcome: concern
  summary: Seven complete historical reports and current histories were read, including
    every claim row and per-accession raw-object join. Current API bytes authenticate
    the matching historical response, not retrieval time, historical commands or old
    recommendations. No attached claim evidence is falsely credited as present.
  target_ids:
  - CultureMech:000930
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
  - CultureMech:000930
  evidence_ids:
  - local-target
- assessment_id: a7
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:000930
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-000930-separate-concentration-variants-before-regeneration
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Separate concentration variants before regeneration
  description: The generated target identifies DSM 1464/000930 yet uses8 and22 from
    DSM 1465/000931. The two maintained variants already preserve15/95 and8/22 respectively
    and explicit reciprocal links. Current merge_formulation_evidence rejects differing
    assertions; the historical ingredient-only merge is not current policy.
  target_ids:
  - CultureMech:000930
  field_paths:
  - media_term
  - ingredients[0].concentration
  - ingredients[1].concentration
  - merged_from
  evidence_ids:
  - dsm1464
  - dsm1465
  - api1464
  - api1465
  - writer-formulation
  - historical-reader
  rule_id: P2.5
  native_severity: P2
  normalization_reason: 'Major: P2.5 duplicate/variant review is applied to an erroneous
    collapse, not to mandate merging; stable source identity is coupled to the wrong
    variant amounts despite valid schema.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinispirillum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinivibrio_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-000930-restore-two-receiving-stocks-and-three-vitamin-subsolutions
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore two receiving stocks and three vitamin subsolutions
  description: Eighteen direct rows represent trace-stock or unmixed vitamin-subsolution
    concentrations. Both primary sources instead add 1 ml/L trace stock and1 ml/L
    of the 1:1:1 vitamin mixture. Solvents, acid/base identities and mixing boundaries
    are missing. Vitamin filtration/storage and trace pH/autoclave steps are unscoped,
    and the vitamin step is mislabeled HEAT.
  target_ids:
  - CultureMech:000930
  field_paths:
  - ingredients
  - solutions
  - preparation_steps[1]
  - preparation_steps[2]
  - preparation_steps[3]
  evidence_ids:
  - dsm1464
  - dsm1465
  - api1464
  - api1465
  - quantities
  - writer-mediadive
  rule_id: P2.3
  native_severity: P2
  normalization_reason: 'Major: P2.3 concentration interpretation is generalized to
    incompatible solution-stage bases. Units are individually valid; stock rates cannot
    be treated as final-medium rates.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinispirillum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinivibrio_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-000930-reconcile-the-sodium-sulfide-conversion-with-explicit-source-molarity
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile the sodium sulfide conversion with explicit source molarity
  description: All records retain provider 0.07906 g/L Na2S. The primary prescribes
    final 1 mM; current exact anhydrous CHEBI:76208 mass 78.047 gives 0.078047 g/L
    at1 mM. This is a source conversion conflict, not evidence for a hydrate or for
    altering other supported main rates.
  target_ids:
  - CultureMech:000930
  field_paths:
  - ingredients[8].concentration
  evidence_ids:
  - dsm1464
  - dsm1465
  - api1464
  - api1465
  - chebi76208
  - quantities
  rule_id: P2.3
  native_severity: P2
  normalization_reason: 'Major: generalized P2.3 concentration conversion conflict;
    exact supplied chemical formula and current molar mass disagree with the imported
    provider mass conversion.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinispirillum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinivibrio_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f4
  issue_key: culturemech-000930-preserve-supplied-nickel-dihydrate-specificity
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Preserve supplied nickel dihydrate specificity
  description: The primary and API explicitly supply NiCl2 x2H2O, while both local
    term slots point to anhydrous nickel dichloride CHEBI:34887. Current catalog linkage
    of that name to34887 does not add water to the OLS chemical object. Calcium pantothenate
    CHEBI:31345 has stereospecified structure not independently established by the
    generic source name; thiamine is a cation-level identity, not a verified supplied
    counterion.
  target_ids:
  - CultureMech:000930
  field_paths:
  - ingredients[25].term
  - ingredients[25].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/chitinivibrio_medium.yaml::ingredients[22].term
  - data/normalized_yaml/bacterial/chitinivibrio_medium.yaml::ingredients[22].mediaingredientmech_chebi_term
  evidence_ids:
  - dsm1464
  - dsm1465
  - api1464
  - api1465
  - grounding
  rule_id: review-yaml-record/supplied-form
  native_severity: P2
  normalization_reason: 'Major custom supplied-form check at native P2 priority: the
    accession exists, so P2.2 missing-ID is not asserted; the confirmed mismatch is
    chemical hydration represented by that accession.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinispirillum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinivibrio_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f5
  issue_key: culturemech-000930-carry-forward-the-existing-owner-chitin-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Carry forward the existing owner chitin grounding
  description: Both maintained owners already carry current CHEBI:17029 chitin and
    the later grounding event; the target lacks this term. The fresh OLS object and
    exact current Chitin row support preserving that owner repair. Missing secondary
    slots are not automatically wrong chemistry.
  target_ids:
  - CultureMech:000930
  field_paths:
  - ingredients[4].term
  - curation_history
  evidence_ids:
  - grounding
  - writer-grounding
  - history
  - historical-reader
  rule_id: review-yaml-record/generated-staleness
  native_severity: P3
  normalization_reason: 'Minor custom generated-staleness check: the exact primary
    chemical grounding is already repaired in both maintained owners; only the obsolete
    generated copy loses it.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinispirillum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinivibrio_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f6
  issue_key: culturemech-000930-attach-stage-specific-evidence-without-rewriting-prior-reviews
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Attach stage-specific evidence without rewriting prior reviews
  description: Current records lack attached quantity and stock-stage evidence. Both
    current API digests authenticate matching October source bytes and all exact table
    objects; their blanket conflict decisions do not override supported main values.
    September endorsed the sodium-sulfide conversion and described an older merger;
    those conclusions are reassessed rather than silently adopted.
  target_ids:
  - CultureMech:000930
  field_paths:
  - ingredients
  - solutions
  - evidence
  - curation_history
  evidence_ids:
  - historical-reader
  - history
  - api1464
  - api1465
  - dsm1464
  - dsm1465
  rule_id: P4.3
  native_severity: P4
  normalization_reason: 'Minor P4.3 reference/linkage gap: source URLs exist in notes
    but explicit claim/stage evidence is missing; historical conclusions require append-only
    qualification.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinispirillum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinivibrio_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Preserve both maintained variant identities and their current source
    amounts. Regenerate them through the current compatibility guard without collapsing
    unequal formulations or publishing sibling quantities under DSM 1464. Verify the1464
    target against 15/95 and retain the1465 record separately.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000930
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinispirillum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinivibrio_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Model the trace stock, mixed vitamin stock and three subsolutions with
    exact source amounts, forms, solvents and receiving additions. Relocate their
    preparation and replace HEAT with appropriate scoped actions; retain main pH/preparation.
    Preserve the primary 1:1:1 ratio and distinguish optional provider 50 ml aliquot
    scale. Do not retain direct stock-rate ingredients or infer missing stock strengths.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000930
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinispirillum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinivibrio_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Retain the explicit primary 1 mM final concentration and document the
    inconsistent provider mass value. Reconcile formula/molar-mass assumptions before
    any mass representation; do not silently endorse 0.07906 g/L, substitute an unreported
    hydrate or change source-prescribed molarity.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000930
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinispirillum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinivibrio_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action4
  description: Resolve the exact nickel-dihydrate grounding while retaining its supplied
    name and stock amount. Do not substitute hexahydrate or certify the anhydrous
    object as a hydrate. Keep calcium stereochemistry and thiamine supplied-salt specificity
    explicitly unresolved unless exact authoritative evidence is obtained.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:000930
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinispirillum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinivibrio_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action5
  description: Preserve the verified owner chitin term and original later history
    during correct separate regeneration. Do not recreate the grounding as a new unsupported
    chemical claim or erase original events.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:000930
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinispirillum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinivibrio_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action6
  description: Attach exact source-specific ingredient evidence and root evidence
    for named solution/preparation stages. Keep both variants and every original historical
    event unchanged; append a verified current curation event with explicit source
    conflicts and unresolved alternatives.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:000930
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinispirillum_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chitinivibrio_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- DSM 1464 explicitly labels mineral concentrations g/L; DSM 1465 labels those mineral
  amounts g, while its API separately supplies g_l. Main water and provider volumes
  are not silently promoted to a physical final-volume instruction.
- Primary chitin is1–2 g/L from a bare5% solution. Provider 1.5 g/L is a conditional
  midpoint, not the only source prescription; the percentage basis and stock addition
  volume are unreported.
- Primary1 mM sodium sulfide conflicts with provider 0.07906 g/L under the current
  exact Na2S mass. The conflict remains documented rather than hidden by choosing
  convenient provider data.
- The source alternative printed NH4MoO4 is retained without guessing a corrected
  formula, hydrate or replacement amount. Calcium pantothenate stereochemistry and
  thiamine counterion are not independently established by the generic names.
- Original Pfennig and Lippert1965 publication was not retrieved. The DSM reproduced
  stock recipes are the verified primary catalogue source; no original-paper DOI or
  organism-growth claim is fabricated.
- No autoclave duration for the main mineral base, full late-stock strengths/doses,
  titrant volumes or incubation conditions are inferred. Stock 4°C storage and trace
  120°C / 20 min remain separate from main preparation.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
