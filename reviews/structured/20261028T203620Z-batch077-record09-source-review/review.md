# Desulfonema ishimotoi medium: six preparation stages and repaired stock definitions

- Review: 20261028T203620Z-batch077-record09-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T20:14:54.267626Z
- Finished UTC: 2026-10-28T20:36:20.083438Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The selected target and its two maintained contributors share36 flattened ingredient quantities. DSMZ739 instead assembles six stages A–F, with separate SL-10, selenite-tungstate and10x vitamin stocks. Existing reusable-stock repairs and26 attached claims are credited. Remaining defects concern stage boundaries, isobutyric-acid units, hydrochloric-acid percent basis, two chemical-form assertions, preparation placement and lost generated instructions. Exact live KOMODO739 authentication remains unavailable.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch077 native selection index 09.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006388 | data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml | generated | desulfonema_ishimotoi_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006388 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:006388 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:006388 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:006388 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Exact lineage and independent source limits

identity: supported. Targets: CultureMech:006388.

Exact merged_from stems resolve the KOMODO739 and DSMZ739 contributors. Their36ingredient signatures match locally and the historicalSOURCE_DUPLICATE link records copied DSMZ composition. DSMZ identity is independently authenticated; matching local signatures and the old MediaList row do not establish current KOMODO equivalence after403 responses.

### Repair credit and source stage preservation

completeness: supported. Targets: CultureMech:006388.

Current stocks595/777/5980 have complete declared compositions and no false placeholders. SL-10 preserves0.01L25%HCl, explicit water make-up and withdrawal of generic nickel mapping. Stocks777/5980 preserve1L batch water and all current evidence. DSMZ owner retains four preparation entries, while target/KOMODO omit them. DEFINED,LIQUID and mainpH7 are compatible with inspectedDSMZ739; bacterial filing and generic applications are not growth evidence.

### Historical claims reconciled to current bytes

evidence: supported. Targets: CultureMech:006388.

Twenty-two full reports and selected archive739context were read. Six selected rows/five parent plans retain238claims, including163literal source-quote occurrences. All26current attached stock claims and47history-change quotes join fresh source bytes. Older medium reviews withheld all36flattened rates; unchanged owner hashes confirm they were not repaired. SL-10 initial preview retains nickel mapping later withdrawn in applied/current bytes; S777 preview/current difference is the final-event timestamp, not a new formulation. Old source digests authenticate current byte equality, not historic access time or execution.

### Current writer limitations

ownership: concern. Targets: CultureMech:006388.

Current MediaDive API composition uses only the first solution and preserves referenced solution descriptors; its rawml-toML_PER_L conversion still needs a batch denominator, and its preparation function still combines steps across solutions. The currentKOMODO converter writes aerobic metadata and uses strftime%f; this is a mechanism reference without historical execution proof. Use current compatible-formulation merge safeguards after maintained-source curation.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:006388.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "Stage Solution A: NaCl", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 25,\n                        \"unit\": \"g\",\n                        \"g_l\": 26.2605,\n                        \"mmol_l\": 449.358,\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "Literal 25 g belongs to Solution A (provider volume952ml); source g_l=26.2605 is stage-scoped. Retain the batch input and boundary. No measured final volume or whole-medium rate is inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "26.2605", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "26.2605", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "26.2605", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}]}, {"quantity_id": "q2", "topic": "Stage Solution A: MgCl2 x 6 H2O", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 5.6,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.88235,\n                        \"mmol_l\": 28.9339,\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "Literal 5.6 g belongs to Solution A (provider volume952ml); source g_l=5.88235 is stage-scoped. Retain the batch input and boundary. No measured final volume or whole-medium rate is inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "5.88235", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "5.88235", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "5.88235", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}]}, {"quantity_id": "q3", "topic": "Stage Solution A: MgSO4 x 7 H2O", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 6.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 7.14286,\n                        \"mmol_l\": 28.9799,\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "Literal 6.8 g belongs to Solution A (provider volume952ml); source g_l=7.14286 is stage-scoped. Retain the batch input and boundary. No measured final volume or whole-medium rate is inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "7.14286", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "7.14286", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "7.14286", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}]}, {"quantity_id": "q4", "topic": "Stage Solution A: CaCl2 x 2 H2O", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[1].recipe[3]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 1.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.47059,\n                        \"mmol_l\": 10.003,\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "Literal 1.4 g belongs to Solution A (provider volume952ml); source g_l=1.47059 is stage-scoped. Retain the batch input and boundary. No measured final volume or whole-medium rate is inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "1.47059", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "1.47059", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "1.47059", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}]}, {"quantity_id": "q5", "topic": "Stage Solution A: KCl", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[1].recipe[4]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.72,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.756303,\n                        \"mmol_l\": 10.1449,\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "Literal 0.72 g belongs to Solution A (provider volume952ml); source g_l=0.756303 is stage-scoped. Retain the batch input and boundary. No measured final volume or whole-medium rate is inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.756303", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.756303", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.756303", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}]}, {"quantity_id": "q6", "topic": "Stage Solution A: KH2PO4", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[1].recipe[5]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.14,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.147059,\n                        \"mmol_l\": 1.08064,\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "Literal 0.14 g belongs to Solution A (provider volume952ml); source g_l=0.147059 is stage-scoped. Retain the batch input and boundary. No measured final volume or whole-medium rate is inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.147059", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.147059", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.147059", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}]}, {"quantity_id": "q7", "topic": "Stage Solution A: NH4Cl", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.262605,\n                        \"mmol_l\": 4.90942,\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "Literal 0.25 g belongs to Solution A (provider volume952ml); source g_l=0.262605 is stage-scoped. Retain the batch input and boundary. No measured final volume or whole-medium rate is inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.262605", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.262605", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.262605", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}]}, {"quantity_id": "q8", "topic": "Stage Solution A: Sodium resazurin", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[1].recipe[9]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00052521,\n                        \"mmol_l\": 0.00209105,\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "StageA receives0.5ml of0.1%w/v sodium-resazurin stock. Explicit basis gives1mg/ml stock and0.5mg delivered. Provider0.00052521g/L uses stageA952ml; it is not an assembled-medium rate. Preserve sodium identity, strength and dose separately.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00052521", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00052521", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00052521", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}]}, {"quantity_id": "q9", "topic": "Stage Solution B: Na-acetate x 3 H2O", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na-acetate x 3 H2O\",\n                        \"compound_id\": 294,\n                        \"amount\": 2.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 250,\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "Literal 2.5 g belongs to Solution B (provider volume10ml); source g_l=250 is stage-scoped. Retain the batch input and boundary. No measured final volume or whole-medium rate is inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "250", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "250", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "250", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}]}, {"quantity_id": "q10", "topic": "Stage Solution B: Disodium succinate", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[2].recipe[1]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Disodium succinate\",\n                        \"compound_id\": 1189,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 61.7094,\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "Literal 0.1 g belongs to Solution B (provider volume10ml); source g_l=10 is stage-scoped. Retain the batch input and boundary. No measured final volume or whole-medium rate is inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}]}, {"quantity_id": "q11", "topic": "Stage Solution B: Isobutyric acid", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[2].recipe[2]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Isobutyric acid\",\n                        \"compound_id\": 222,\n                        \"amount\": 0.19,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "The literal liquid input is0.19ml =0.00019L in stageB. No density is stated; molecular mass is not density. Preserve the batch volume and stage, not a mass concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.19", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Source states0.19ml isobutyric acid in stageB;0.19G_PER_L has no supported mass conversion or receiving-volume basis."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.19", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source states0.19ml isobutyric acid in stageB;0.19G_PER_L has no supported mass conversion or receiving-volume basis."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.19", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Source states0.19ml isobutyric acid in stageB;0.19G_PER_L has no supported mass conversion or receiving-volume basis."}]}, {"quantity_id": "q12", "topic": "Stage Solution D: AlK(SO4)2 x 12 H2O", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[4].recipe[0]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\": 0.48,\n                        \"unit\": \"g\",\n                        \"g_l\": 48,\n                        \"mmol_l\": 101.183,\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "Literal 0.48 g belongs to Solution D (provider volume10ml); source g_l=48 is stage-scoped. Retain the batch input and boundary. No measured final volume or whole-medium rate is inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "48", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "48", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "48", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}]}, {"quantity_id": "q13", "topic": "Stage Solution E: Na2CO3", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[5].recipe[0]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\": 471.752,\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "Literal 1 g belongs to Solution E (provider volume20ml); source g_l=50 is stage-scoped. Retain the batch input and boundary. No measured final volume or whole-medium rate is inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "50", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "50", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "50", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}]}, {"quantity_id": "q14", "topic": "Stage Solution F: Na2S x 9 H2O", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[6].recipe[0]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 124.905,\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "Literal 0.3 g belongs to Solution F (provider volume10ml); source g_l=30 is stage-scoped. Retain the batch input and boundary. No measured final volume or whole-medium rate is inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "30", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "30", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "30", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium concentration; exact KOMODO source identity remains separately unresolved."}]}, {"quantity_id": "q15", "topic": "Stock595: HCl", "source": {"evidence_id": "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab", "locator": "$.data.recipe[0]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"HCl\",\n                \"compound_id\": 68,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": \"25%\",\n                \"amount\": 10,\n                \"unit\": \"ml\",\n                \"g_l\": 2.5,\n                \"mmol_l\": 68.5683,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Literal10ml HCl with attribute25% is0.01L batch input, already repaired in currentSL-10. The source does not identify percent basis or density; provider2.5g/L cannot establish pure-HCl mass. Medium layers still carry that value without scope.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "2.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "2.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "2.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml", "field_path": "composition[0].concentration", "stored_value": {"value": "0.01", "unit": "L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q16", "topic": "Stock595: FeCl2 x 4 H2O", "source": {"evidence_id": "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab", "locator": "$.data.recipe[1]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"FeCl2 x 4 H2O\",\n                \"compound_id\": 260,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1.5,\n                \"unit\": \"g\",\n                \"g_l\": 1.5,\n                \"mmol_l\": 7.54482,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 1.5 g and provider g_l=1.5 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml", "field_path": "composition[1].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q17", "topic": "Stock595: ZnCl2", "source": {"evidence_id": "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab", "locator": "$.data.recipe[2]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"ZnCl2\",\n                \"compound_id\": 64,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 70,\n                \"unit\": \"mg\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.513573,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 70 mg and provider g_l=0.07 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.07", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.07", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.07", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml", "field_path": "composition[2].concentration", "stored_value": {"value": "0.07", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q18", "topic": "Stock595: MnCl2 x 4 H2O", "source": {"evidence_id": "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab", "locator": "$.data.recipe[3]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.505293,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 100 mg and provider g_l=0.1 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml", "field_path": "composition[3].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q19", "topic": "Stock595: H3BO3", "source": {"evidence_id": "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab", "locator": "$.data.recipe[4]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"H3BO3\",\n                \"compound_id\": 37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 6,\n                \"unit\": \"mg\",\n                \"g_l\": 0.006,\n                \"mmol_l\": 0.0970246,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 6 mg and provider g_l=0.006 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.006", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.006", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.006", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml", "field_path": "composition[4].concentration", "stored_value": {"value": "0.006", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q20", "topic": "Stock595: CoCl2 x 6 H2O", "source": {"evidence_id": "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab", "locator": "$.data.recipe[5]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 190,\n                \"unit\": \"mg\",\n                \"g_l\": 0.19,\n                \"mmol_l\": 1.46335,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 190 mg and provider g_l=0.19 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.19", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.19", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.19", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml", "field_path": "composition[5].concentration", "stored_value": {"value": "0.19", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q21", "topic": "Stock595: CuCl2 x 2 H2O", "source": {"evidence_id": "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab", "locator": "$.data.recipe[6]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote": "{\n                \"recipe_order\": 7,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\": 39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\": \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0117314,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 2 mg and provider g_l=0.002 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.002", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.002", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.002", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml", "field_path": "composition[6].concentration", "stored_value": {"value": "0.002", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q22", "topic": "Stock595: NiCl2 x 6 H2O", "source": {"evidence_id": "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab", "locator": "$.data.recipe[7]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote": "{\n                \"recipe_order\": 8,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\": 40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 24,\n                \"unit\": \"mg\",\n                \"g_l\": 0.024,\n                \"mmol_l\": 0.185187,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 24 mg and provider g_l=0.024 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.024", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.024", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.024", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml", "field_path": "composition[7].concentration", "stored_value": {"value": "0.024", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q23", "topic": "Stock595: Na2MoO4 x 2 H2O", "source": {"evidence_id": "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab", "locator": "$.data.recipe[8]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote": "{\n                \"recipe_order\": 9,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 36,\n                \"unit\": \"mg\",\n                \"g_l\": 0.036,\n                \"mmol_l\": 0.148791,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 36 mg and provider g_l=0.036 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.036", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.036", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.036", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml", "field_path": "composition[8].concentration", "stored_value": {"value": "0.036", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q24", "topic": "Stock595: Distilled water", "source": {"evidence_id": "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab", "locator": "$.data.recipe[9]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote": "{\n                \"recipe_order\": 10,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 990,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }"}, "decision": "verified", "rationale": "SL-10 starts with990ml water and explicitly makes up to1000ml; currentVARIABLE to1L final volume is correct. Do not replace with a fixed990ml dose or a percentage.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml", "field_path": "composition[9].concentration", "stored_value": {"value": "to 1 L final volume", "unit": "VARIABLE"}, "decision": "verified", "rationale": "Preserve the source-backed existing water repair and evidence."}], "additional_sources": [{"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[7].steps[0]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }"}]}, {"quantity_id": "q25", "topic": "Stock777: NaOH", "source": {"evidence_id": "solution777", "reference": "https://mediadive.dsmz.de/rest/solution/777", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution777.raw", "raw_sha256": "3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2", "locator": "$.data.recipe[0]", "accessed_at": "2026-10-28T20:15:43.329648Z", "quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"NaOH\",\n                \"compound_id\": 256,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.5,\n                \"unit\": \"g\",\n                \"g_l\": 0.5,\n                \"mmol_l\": 12.5009,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 0.5 g and provider g_l=0.5 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml", "field_path": "composition[0].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q26", "topic": "Stock777: Na2SeO3 x 5 H2O", "source": {"evidence_id": "solution777", "reference": "https://mediadive.dsmz.de/rest/solution/777", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution777.raw", "raw_sha256": "3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2", "locator": "$.data.recipe[1]", "accessed_at": "2026-10-28T20:15:43.329648Z", "quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Na2SeO3 x 5 H2O\",\n                \"compound_id\": 107,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 3,\n                \"unit\": \"mg\",\n                \"g_l\": 0.003,\n                \"mmol_l\": 0.0114062,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 3 mg and provider g_l=0.003 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.003", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.003", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.003", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml", "field_path": "composition[1].concentration", "stored_value": {"value": "0.003", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q27", "topic": "Stock777: Na2WO4 x 2 H2O", "source": {"evidence_id": "solution777", "reference": "https://mediadive.dsmz.de/rest/solution/777", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution777.raw", "raw_sha256": "3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2", "locator": "$.data.recipe[2]", "accessed_at": "2026-10-28T20:15:43.329648Z", "quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"Na2WO4 x 2 H2O\",\n                \"compound_id\": 249,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\": \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0121267,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 4 mg and provider g_l=0.004 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.004", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.004", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.004", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml", "field_path": "composition[2].concentration", "stored_value": {"value": "0.004", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q28", "topic": "Stock777: Distilled water", "source": {"evidence_id": "solution777", "reference": "https://mediadive.dsmz.de/rest/solution/777", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution777.raw", "raw_sha256": "3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2", "locator": "$.data.recipe[3]", "accessed_at": "2026-10-28T20:15:43.329648Z", "quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }"}, "decision": "verified", "rationale": "Literal1000ml water is a1L batch input, correctly stored asL. Provider1000ml volume is separate metadata, not independent measured-final-volume evidence; no competing make-up step is present.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml", "field_path": "composition[3].concentration", "stored_value": {"value": "1", "unit": "L"}, "decision": "verified", "rationale": "Preserve the source-backed existing water repair and evidence."}]}, {"quantity_id": "q29", "topic": "Stock5980: Biotin", "source": {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator": "$.data.recipe[0]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\": \"mg\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.0818632,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 20 mg and provider g_l=0.02 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[0].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q30", "topic": "Stock5980: Folic acid", "source": {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator": "$.data.recipe[1]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Folic acid\",\n                \"compound_id\": 138,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\": \"mg\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.0453104,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 20 mg and provider g_l=0.02 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[27].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[27].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[27].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[1].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q31", "topic": "Stock5980: Pyridoxine hydrochloride", "source": {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator": "$.data.recipe[2]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"Pyridoxine hydrochloride\",\n                \"compound_id\": 519,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.486287,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 100 mg and provider g_l=0.1 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[28].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[28].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[28].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[2].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q32", "topic": "Stock5980: Thiamine HCl", "source": {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator": "$.data.recipe[3]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.148236,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 50 mg and provider g_l=0.05 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[29].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[29].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[29].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[3].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q33", "topic": "Stock5980: Riboflavin", "source": {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator": "$.data.recipe[4]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"Riboflavin\",\n                \"compound_id\": 136,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.132837,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 50 mg and provider g_l=0.05 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[30].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[30].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[30].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[4].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q34", "topic": "Stock5980: Nicotinic acid", "source": {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator": "$.data.recipe[5]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"Nicotinic acid\",\n                \"compound_id\": 139,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.406141,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 50 mg and provider g_l=0.05 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[31].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[31].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[31].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[5].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q35", "topic": "Stock5980: Calcium D-(+)-pantothenate", "source": {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator": "$.data.recipe[6]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\": 7,\n                \"compound\": \"Calcium D-(+)-pantothenate\",\n                \"compound_id\": 1512,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.209846,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 50 mg and provider g_l=0.05 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[32].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[32].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[32].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[6].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q36", "topic": "Stock5980: Vitamin B12", "source": {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator": "$.data.recipe[7]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\": 8,\n                \"compound\": \"Vitamin B12\",\n                \"compound_id\": 18,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1,\n                \"unit\": \"mg\",\n                \"g_l\": 0.001,\n                \"mmol_l\": 0.00073779,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 1 mg and provider g_l=0.001 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[33].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[33].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[33].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[7].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q37", "topic": "Stock5980: p-Aminobenzoic acid", "source": {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator": "$.data.recipe[8]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\": 9,\n                \"compound\": \"p-Aminobenzoic acid\",\n                \"compound_id\": 47,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.364591,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 50 mg and provider g_l=0.05 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[34].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[34].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[34].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[8].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q38", "topic": "Stock5980: (DL)-alpha-Lipoic acid", "source": {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator": "$.data.recipe[9]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\": 10,\n                \"compound\": \"(DL)-alpha-Lipoic acid\",\n                \"compound_id\": 252,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.24233,\n                \"optional\": 0\n            }"}, "decision": "mixed", "rationale": "Source 50 mg and provider g_l=0.05 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml; other stocks retain provider normalization without independent final-volume certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[35].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[35].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "ingredients[35].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately prepared stock, not the receiving assembled medium. Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[9].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock quantity and attached evidence preserve the source scope; retain the existing repair."}]}, {"quantity_id": "q39", "topic": "Stock5980: Distilled water", "source": {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980", "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256": "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator": "$.data.recipe[10]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\": 11,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }"}, "decision": "verified", "rationale": "Literal1000ml water is a1L batch input, correctly stored asL. Provider1000ml volume is separate metadata, not independent measured-final-volume evidence; no competing make-up step is present.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml", "field_path": "composition[10].concentration", "stored_value": {"value": "1", "unit": "L"}, "decision": "verified", "rationale": "Preserve the source-backed existing water repair and evidence."}]}, {"quantity_id": "q40", "topic": "Assembled-medium addition: Solution A", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 1513,\n                        \"amount\": 952,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "Source addition952ml ofSolution A. Six stated doses952+10+1+10+20+10 total1003ml nominally, matching provider metadata, but are not an independently measured final-volume declaration. Do not label literal dosesML_PER_L without an explicit denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Missing named A–F receiving descriptor; preserve literal batch volume and source stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Missing named A–F receiving descriptor; preserve literal batch volume and source stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing": true}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Missing named A–F receiving descriptor; preserve literal batch volume and source stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing": true}]}, {"quantity_id": "q41", "topic": "Assembled-medium addition: Solution B", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\": 1514,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "Source addition10ml ofSolution B. Six stated doses952+10+1+10+20+10 total1003ml nominally, matching provider metadata, but are not an independently measured final-volume declaration. Do not label literal dosesML_PER_L without an explicit denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Missing named A–F receiving descriptor; preserve literal batch volume and source stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Missing named A–F receiving descriptor; preserve literal batch volume and source stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing": true}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Missing named A–F receiving descriptor; preserve literal batch volume and source stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing": true}]}, {"quantity_id": "q42", "topic": "Assembled-medium addition: Solution C", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 1515,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "Source addition1ml ofSolution C. Six stated doses952+10+1+10+20+10 total1003ml nominally, matching provider metadata, but are not an independently measured final-volume declaration. Do not label literal dosesML_PER_L without an explicit denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Missing named A–F receiving descriptor; preserve literal batch volume and source stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Missing named A–F receiving descriptor; preserve literal batch volume and source stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing": true}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Missing named A–F receiving descriptor; preserve literal batch volume and source stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing": true}]}, {"quantity_id": "q43", "topic": "Assembled-medium addition: Solution D", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\": 1516,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "Source addition10ml ofSolution D. Six stated doses952+10+1+10+20+10 total1003ml nominally, matching provider metadata, but are not an independently measured final-volume declaration. Do not label literal dosesML_PER_L without an explicit denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Missing named A–F receiving descriptor; preserve literal batch volume and source stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Missing named A–F receiving descriptor; preserve literal batch volume and source stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing": true}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Missing named A–F receiving descriptor; preserve literal batch volume and source stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing": true}]}, {"quantity_id": "q44", "topic": "Assembled-medium addition: Solution E", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"solution\": \"Solution E\",\n                        \"solution_id\": 1517,\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "Source addition20ml ofSolution E. Six stated doses952+10+1+10+20+10 total1003ml nominally, matching provider metadata, but are not an independently measured final-volume declaration. Do not label literal dosesML_PER_L without an explicit denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Missing named A–F receiving descriptor; preserve literal batch volume and source stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Missing named A–F receiving descriptor; preserve literal batch volume and source stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing": true}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Missing named A–F receiving descriptor; preserve literal batch volume and source stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing": true}]}, {"quantity_id": "q45", "topic": "Assembled-medium addition: Solution F", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Solution F\",\n                        \"solution_id\": 1518,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }"}, "decision": "mixed", "rationale": "Source addition10ml ofSolution F. Six stated doses952+10+1+10+20+10 total1003ml nominally, matching provider metadata, but are not an independently measured final-volume declaration. Do not label literal dosesML_PER_L without an explicit denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Missing named A–F receiving descriptor; preserve literal batch volume and source stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Missing named A–F receiving descriptor; preserve literal batch volume and source stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing": true}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Missing named A–F receiving descriptor; preserve literal batch volume and source stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing": true}]}, {"quantity_id": "q46", "topic": "Solution A nested stock addition", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[1].recipe[7]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }"}, "decision": "add", "rationale": "Source1ml ofTrace element solution SL-10 belongs insideSolution A; this receiving edge is missing from the flattened record. Existing reusable stock definitions can be linked after exact source and identifier reconciliation. StageA recipe liquid entries sum952.5ml while its declared stage volume/delivery is952ml; retain both source statements without silently repairing the source.", "layer_assessments": []}, {"quantity_id": "q47", "topic": "Solution A nested stock addition", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[1].recipe[8]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }"}, "decision": "add", "rationale": "Source1ml ofSelenite-tungstate solution belongs insideSolution A; this receiving edge is missing from the flattened record. Existing reusable stock definitions can be linked after exact source and identifier reconciliation. StageA recipe liquid entries sum952.5ml while its declared stage volume/delivery is952ml; retain both source statements without silently repairing the source.", "layer_assessments": []}, {"quantity_id": "q48", "topic": "Solution A water input", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[1].recipe[10]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 950,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }"}, "decision": "add", "rationale": "Literal950ml water belongs toSolution A. It is a batch solvent input, not a mass, percent or measured final-volume denominator. Preserve the source-stage water amount with the preparation.", "layer_assessments": []}, {"quantity_id": "q49", "topic": "Solution B water input", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[2].recipe[3]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }"}, "decision": "add", "rationale": "Literal10ml water belongs toSolution B. It is a batch solvent input, not a mass, percent or measured final-volume denominator. Preserve the source-stage water amount with the preparation.", "layer_assessments": []}, {"quantity_id": "q50", "topic": "Solution C nested stock addition", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[3].recipe[0]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }"}, "decision": "add", "rationale": "Source1ml ofWolin's vitamin solution (10x) belongs insideSolution C; this receiving edge is missing from the flattened record. Existing reusable stock definitions can be linked after exact source and identifier reconciliation.", "layer_assessments": []}, {"quantity_id": "q51", "topic": "Solution D water input", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[4].recipe[1]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }"}, "decision": "add", "rationale": "Literal10ml water belongs toSolution D. It is a batch solvent input, not a mass, percent or measured final-volume denominator. Preserve the source-stage water amount with the preparation.", "layer_assessments": []}, {"quantity_id": "q52", "topic": "Solution E water input", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[5].recipe[1]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }"}, "decision": "add", "rationale": "Literal20ml water belongs toSolution E. It is a batch solvent input, not a mass, percent or measured final-volume denominator. Preserve the source-stage water amount with the preparation.", "layer_assessments": []}, {"quantity_id": "q53", "topic": "Solution F water input", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[6].recipe[1]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }"}, "decision": "add", "rationale": "Literal10ml water belongs toSolution F. It is a batch solvent input, not a mass, percent or measured final-volume denominator. Preserve the source-stage water amount with the preparation.", "layer_assessments": []}, {"quantity_id": "q54", "topic": "StageB adjustment", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[2].steps[0]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"step\": \"Adjust to pH 7.0 with 1 N NaOH.\"\n                    }"}, "decision": "not_quantified", "rationale": "Source1NNaOH is a titrant strength, not a delivered amount. No amount is stated; preserve variable addition and stageB pH7.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "preparation_steps[2]", "stored_value": {"step_number": 3, "action": "MIX", "description": "Adjust to pH 7.0 with 1 N NaOH."}, "decision": "relocate", "rationale": "Existing pH7/1NNaOH instruction belongs to stageB, not a second unspecified whole-medium adjustment."}]}, {"quantity_id": "q55", "topic": "SL-10 preparation and final make-up", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[7].steps[0]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }"}, "decision": "not_quantified", "rationale": "Stock595 already retains its preparation_notes and repaired variable water field. Move source context to the stock boundary while preserving its evidence; do not apply make-up to the receiving medium.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "preparation_steps[3]", "stored_value": {"step_number": 4, "action": "DISSOLVE", "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}, "decision": "relocate", "rationale": "Existing FeCl2/HCl dissolution and1000ml make-up instruction belongs only toSL-10."}]}, {"quantity_id": "q56", "topic": "Main A–F preparation and conditions", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"step\": \"Sparge solution A with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic and reach a pH of around 6, then distribute under the same gas atmosphere into anoxic Hungate-type tubes and autoclave. Solutions B and C are prepared under 100% N2 gas atmosphere and sterilized by filtration. Solutions D and F are autoclaved separately under 100% N2 gas. Solution E is prepared under 80% N2 and 20% CO2 gas gas atmosphere. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be at 7.0. After combining solutions the medium should equilibrate overnight and a white precipitate should be apparent.\"\n                    }"}, "decision": "not_quantified", "rationale": "A uses80/20N2/CO2 for30–45minutes, near pH6 before autoclaving; B/C use100%N2 and filtration; D/F use100%N2 and autoclaving; E uses80/20N2/CO2. Add B–F in order; final mediumpH7 after overnight equilibration and white precipitate are source context. No unstated sterilization temperature/time is supplied.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "preparation_steps[0]", "stored_value": {"step_number": 1, "action": "AUTOCLAVE", "description": "Sparge solution A with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic and reach a pH of around 6, then distribute under the same gas atmosphere into anoxic Hungate-type tubes and autoclave. Solutions B and C are prepared under 100% N2 gas atmosphere and sterilized by filtration. Solutions D and F are autoclaved separately under 100% N2 gas. Solution E is prepared under 80% N2 and 20% CO2 gas gas atmosphere. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be at 7.0. After combining solutions the medium should equilibrate overnight and a white precipitate should be apparent."}, "decision": "evidence_only", "rationale": "Full original main preparation is already retained in this owner; preserve while clarifying stage boundaries. The unchanged text is source-supported, but this owner has no attached field-level claim; attach evidence without changing the instruction."}, {"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Generated target lacks retained DSMZ preparation; exactKOMODO route remains inaccessible.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "unsupported", "rationale": "Generated target lacks retained DSMZ preparation; exactKOMODO route remains inaccessible.", "missing": true}]}, {"quantity_id": "q57", "topic": "Optional reduction and inoculum", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f", "locator": "$.data.solutions[0].steps[1]", "accessed_at": "2026-10-28T20:14:12.383714Z", "quote": "{\n                        \"step\": \"Note: Addition of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v) solution freshly prepared under N2 and filter-sterilized) just before inoculation may stimulate growth at the beginning. For transfers use 5 - 10% (v/v) inoculum.\"\n                    }"}, "decision": "not_quantified", "rationale": "The source optionally adds10–20mg/L dithionite from a freshly prepared5%w/v solution made underN2 and filter sterilized; a hypothetical dose would be0.2–0.4ml/L from50mg/ml, conditional on that explicit strength. Source inoculum is5–10%v/v. These do not establish a mandatory formulation component, strain growth evidence or new stock identity.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml", "field_path": "preparation_steps[1]", "stored_value": {"step_number": 2, "action": "FILTER_STERILIZE", "description": "Note: Addition of 10 - 20 mg sodium dithionite per liter (e.g. from 5% (w/v) solution freshly prepared under N2 and filter-sterilized) just before inoculation may stimulate growth at the beginning. For transfers use 5 - 10% (v/v) inoculum."}, "decision": "evidence_only", "rationale": "Retain source optional wording and inoculum guidance; these are already present in the maintainedDSMZ owner. The unchanged text is source-supported, but this owner has no attached field-level claim; attach evidence without changing the instruction."}]}]

### Current ontology and MIM correspondence

grounding: concern. Targets: CultureMech:006388.

All262recursive current ID/label slots and795exact packaged rows were read;38OLS scientific objects cover all36asserted accessions plus water and nickel-hexahydrate candidate. No current numeric legacyMIM assertions remain. The two sodium/hydrate contradictions are confirmed. Explicit calciumD-pantothenate31345, alum dodecahydrate86465 and other stated hydrates are preserved. Primary disodium succinate does not independently establish anhydrous specificity from provider mmol_l; generic lipoic acid16494 does not certify the DL mixture, so preserve literal source labels and uncertainty. Rejected aliases are separate from mapped identifier rows.

### History and evidence scope

provenance: concern. Targets: CultureMech:006388.

Complete current histories,26attached stock claims,22full reports, selected archive739context and238claims from six rows/five parent plans were assessed.163parent quote occurrences and47historical change quotes match current source bytes. AppliedSL-10 nickel withdrawal andS777 event-time difference are explicitly separated from older previews. Current source byte equality does not authenticate historical access times or executions.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:006388.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:006388.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

### High-metal classification remains unverified

evidence: unknown. Targets: CultureMech:006388.

All three medium layers assert high_metal: true. The inspected DSMZ739 primary recipe and API do not explicitly classify the medium as high-metal or state a criterion for that flag. Trace-metal salts alone do not establish this classification. Retain this as unresolved metadata pending an explicit source or documented classification rule; absence of source support does not establish high_metal: false.

## Findings

### f1: Preparation-stage concentrations are flattened into the whole medium

major / open / confirmed; issue key: culturemech-006388-preparation-stage-concentrations-are-flattened-into-the-whole-medium.

All36root ingredient rates in the generated target and both contributors come from distinct A/B/D/E/F stages or reusable stocks. DSMZ739 assembles A–F and nests595/777 inA and5980 inC. Restore these boundaries and literal batch doses; numerical agreement with a stage g_l does not validate a whole-medium rate. Preserve all current reusable-stock repairs and do not infer measured final volume from the nominal1003ml sum.

### f2: Liquid doses lack supported mass conversions

major / open / confirmed; issue key: culturemech-006388-liquid-doses-lack-supported-mass-conversions.

Root isobutyric acid0.19G_PER_L conflicts with the literal0.19ml input inB, and HCl2.5G_PER_L lacks both the25%basis/density and receiving-stage scope. Preserve explicit volumes and stock strengths. The standaloneSL-10 HCl0.01L repair is correct and should be reused, not reopened.

### f3: Generated preparation is missing and stock steps lack scope

major / open / confirmed; issue key: culturemech-006388-generated-preparation-is-missing-and-stock-steps-lack-scope.

The DSMZ contributor retains the complete mainA–F preparation and optional reduction/inoculum note. Target/KOMODO have no preparation_steps. Its third entry is B pH7 adjustment with 1N NaOH, labeled MIX; its fourth is SL-10 dissolution/make-up, labeled DISSOLVE. Both are unscoped root preparation steps. Preserve the first two source texts, move stock instructions to their proper boundary, and carry supported preparation through regeneration.

### f4: Explicit sodium and hydrate forms are not preserved by two identifiers

major / open / confirmed; issue key: culturemech-006388-explicit-sodium-and-hydrate-forms-are-not-preserved-by-two-identifiers.

Sodium resazurin carries neutral resazurinCHEBI8806, and NiCl2x6H2O carries anhydrous nickel dichlorideCHEBI34887 in all three medium layers. CurrentOLS53542 supports nickel chloride hexahydrate as a candidate; MIM has both a mapped preferred-name row and a separately rejected source-spelling alias. CurrentSL-10 already withdrewCHEBI34887, retaining upstream compound40 and the hexahydrate label. Preserve this repair and resolve exact replacements using the current catalog; do not reinstate a rejected alias or infer mass equivalents.

### f5: Medium claims lack direct evidence and retain malformed imported times

minor / open / confirmed; issue key: culturemech-006388-medium-claims-lack-direct-evidence-and-retain-malformed-imported-times.

All26attached current claims belong to reusable stocks; the three medium layers lack field-level formulation evidence. Attach the verifiedDSMZ claims with exact stage scope while keeping KOMODO equivalence unresolved. Literal.fZ and timezone-less imported history values need bounded follow-up; preserve original append-only events and do not invent replacement times from current writer behavior.

## Recommended Actions And Acceptance Checks

### action1

All36root ingredient rates in the generated target and both contributors come from distinct A/B/D/E/F stages or reusable stocks. DSMZ739 assembles A–F and nests595/777 inA and5980 inC. Restore these boundaries and literal batch doses; numerical agreement with a stage g_l does not validate a whole-medium rate. Preserve all current reusable-stock repairs and do not infer measured final volume from the nominal1003ml sum.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Root isobutyric acid0.19G_PER_L conflicts with the literal0.19ml input inB, and HCl2.5G_PER_L lacks both the25%basis/density and receiving-stage scope. Preserve explicit volumes and stock strengths. The standaloneSL-10 HCl0.01L repair is correct and should be reused, not reopened.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

The DSMZ contributor retains the complete mainA–F preparation and optional reduction/inoculum note. Target/KOMODO have no preparation_steps. Its third entry is B pH7 adjustment with 1N NaOH, labeled MIX; its fourth is SL-10 dissolution/make-up, labeled DISSOLVE. Both are unscoped root preparation steps. Preserve the first two source texts, move stock instructions to their proper boundary, and carry supported preparation through regeneration.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action4

Sodium resazurin carries neutral resazurinCHEBI8806, and NiCl2x6H2O carries anhydrous nickel dichlorideCHEBI34887 in all three medium layers. CurrentOLS53542 supports nickel chloride hexahydrate as a candidate; MIM has both a mapped preferred-name row and a separately rejected source-spelling alias. CurrentSL-10 already withdrewCHEBI34887, retaining upstream compound40 and the hexahydrate label. Preserve this repair and resolve exact replacements using the current catalog; do not reinstate a rejected alias or infer mass equivalents.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action5

All26attached current claims belong to reusable stocks; the three medium layers lack field-level formulation evidence. Attach the verifiedDSMZ claims with exact stage scope while keeping KOMODO equivalence unresolved. Literal.fZ and timezone-less imported history values need bounded follow-up; preserve original append-only events and do not invent replacement times from current writer behavior.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-2 | data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| identity-search | REVIEW_WORK/batch077/record09/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| stock-595 | data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml; Complete document | context_only | Entire current stock record, composition, preparation, references, attached claims and append-only history read. Only this exact stock definition is assessed; other receiving media are excluded. |
| stock-777 | data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml; Complete document | context_only | Entire current stock record, composition, preparation, references, attached claims and append-only history read. Only this exact stock definition is assessed; other receiving media are excluded. |
| stock-5980 | data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml; Complete document | context_only | Entire current stock record, composition, preparation, references, attached claims and append-only history read. Only this exact stock definition is assessed; other receiving media are excluded. |
| dsm739 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium739.pdf; Exact source identity and scoped formulation/preparation | supports | All three PDF pages visually and textually read: literal A–F preparation amounts, source stock definitions, gas and sterilization stages, final pH7, optional reducing addition and inoculum note. No independently measured final volume is stated. |
| api739 | https://mediadive.dsmz.de/rest/medium/739; Exact source identity and scoped formulation/preparation | supports | Complete medium identity and all ten solution objects read, including all recipe, preparation and provider metadata. Main1512 reports1003ml; A1513 reports952ml. These provider volumes are separate from measured final volume and do not make nested stock rates whole-medium rates. |
| solution595 | https://mediadive.dsmz.de/rest/solution/595; Exact source identity and scoped formulation/preparation | supports | Full standalone SL-10 JSON read, including10ml HCl25%, eight salt masses,990ml starting water and explicit make-up to1000ml. Source digest equals historical records. Percent basis and density are not supplied. |
| solution777 | https://mediadive.dsmz.de/rest/solution/777; Exact source identity and scoped formulation/preparation | supports | Full current stock JSON scientific scope read through exact-byte equality to root-read076 capture: three solutes,1000ml water, provider1000ml stock volume, no steps. Current YAML and history also match the earlier fully read bytes. |
| solution5980 | https://mediadive.dsmz.de/rest/solution/5980; Exact source identity and scoped formulation/preparation | supports | Full current10x vitamin stock JSON read through exact-byte equality to root-read076 capture: ten vitamins and1000ml water, source-explicit D-calcium pantothenate and DL-lipoic acid. Current stock YAML, claims and history match earlier fully read bytes. |
| api161 | https://mediadive.dsmz.de/rest/medium/161; Exact source identity and scoped formulation/preparation | supports | Only medium identity, solution inventory and exact solution5980 object are assessed to authenticate existing stock evidence. Its raw capture exactly matches the earlier root-read capture; other recipe and growth claims are excluded. |
| komodo739 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=739; Exact current accession endpoint | unknown | HTTP403 challenge body read. Current source formulation and cross-source equivalence cannot be authenticated from this attempt; historical mapping remains attributed context. |
| komodoList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact current accession endpoint | unknown | HTTP403 challenge body read. Current source formulation and cross-source equivalence cannot be authenticated from this attempt; historical mapping remains attributed context. |
| historical-0 | reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md; All non-table text plus exact739row | context_only | Selected archive methodology and exact739pair read; unrelated table rows excluded. |
| historical-1 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-2 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfonema_ishimotoi_medium.yaml.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-3 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-0500-1000/records/bacterial/mediadive_777_Selenite-tungstate_solution.yaml.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-4 | reports/ingredient_concentration_curation/20261007-mediadive-stocks/mediadive_595_Trace_element_solution_SL-10.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-5 | reports/ingredient_concentration_curation/20261007-mediadive-stocks/mediadive_5980_Wolin_s_vitamin_solution_10x.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-6 | reports/ingredient_concentration_curation/20261009-methanofollis-family/applied-records/S5980.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-7 | reports/ingredient_concentration_curation/20261009-methanofollis-family/records/S5980.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-8 | reports/ingredient_concentration_curation/20261009-synthrophomonas-family/applied-records/S595.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-9 | reports/ingredient_concentration_curation/20261009-synthrophomonas-family/applied-records/S777.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-10 | reports/ingredient_concentration_curation/20261009-synthrophomonas-family/records-ledgers-successor/S595.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-11 | reports/ingredient_concentration_curation/20261009-synthrophomonas-family/records-ledgers-successor/S777.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-12 | reports/ingredient_concentration_curation/20261009-synthrophomonas-family/records/S595.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-13 | reports/ingredient_concentration_curation/20261009-synthrophomonas-family/records/S777.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-14 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-15 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-16 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-17 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-18 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-19 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-20 | reports/yaml_record_review/20260921T142652Z-ARCHAEOGLOBUS_SULFATICALLIDUS_MEDIUM.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-21 | reports/yaml_record_review/20260921T161921Z-asw_hd_1_10_diluted.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| historical-22 | reports/yaml_record_review/20260922T034655Z-CARBOXYDOCELLA_MANGANICA_MEDIUM.md; Complete report; historical-reading-cells.json reconstructs original bytes | context_only | Complete per-record report read through lossless cell reconstruction; earlier findings are reassessed against current source and record bytes. Unrelated receiving-medium conclusions are context only. |
| parent-plan-0 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json; Exact selected rows in selected-parent-plan-reading.json | context_only | Six exact selected owner/dependency rows across five plans were read, including all238 claims and before/after comparisons. Unrelated records and global conclusions excluded. |
| parent-plan-1 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json; Exact selected rows in selected-parent-plan-reading.json | context_only | Six exact selected owner/dependency rows across five plans were read, including all238 claims and before/after comparisons. Unrelated records and global conclusions excluded. |
| parent-plan-2 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-0500-1000/plan.json; Exact selected rows in selected-parent-plan-reading.json | context_only | Six exact selected owner/dependency rows across five plans were read, including all238 claims and before/after comparisons. Unrelated records and global conclusions excluded. |
| parent-plan-3 | reports/ingredient_concentration_curation/20261009-methanofollis-family/plan.json; Exact selected rows in selected-parent-plan-reading.json | context_only | Six exact selected owner/dependency rows across five plans were read, including all238 claims and before/after comparisons. Unrelated records and global conclusions excluded. |
| parent-plan-4 | reports/ingredient_concentration_curation/20261009-synthrophomonas-family/plan.json; Exact selected rows in selected-parent-plan-reading.json | context_only | Six exact selected owner/dependency rows across five plans were read, including all238 claims and before/after comparisons. Unrelated records and global conclusions excluded. |
| writer-0 | src/culturemech/import/mediadive_importer.py; MediaDive API composition/solution/unit/preparation functions; KOMODO conversion; merge/formulation relevant functions | context_only | Current relevant source conversion or merge compatibility functions read; exact prior-reading proof is retained for unchanged merge functions. Current code is not proof of historical execution. |
| writer-1 | src/culturemech/import/komodo_web_importer.py; MediaDive API composition/solution/unit/preparation functions; KOMODO conversion; merge/formulation relevant functions | context_only | Current relevant source conversion or merge compatibility functions read; exact prior-reading proof is retained for unchanged merge functions. Current code is not proof of historical execution. |
| writer-2 | src/culturemech/merge/merger.py; MediaDive API composition/solution/unit/preparation functions; KOMODO conversion; merge/formulation relevant functions | context_only | Current relevant source conversion or merge compatibility functions read; exact prior-reading proof is retained for unchanged merge functions. Current code is not proof of historical execution. |
| writer-3 | src/culturemech/merge/formulation.py; MediaDive API composition/solution/unit/preparation functions; KOMODO conversion; merge/formulation relevant functions | context_only | Current relevant source conversion or merge compatibility functions read; exact prior-reading proof is retained for unchanged merge functions. Current code is not proof of historical execution. |
| parent-claims | REVIEW_WORK/batch077/record09/selected-parent-plan-reading.json | context_only | Six selected rows/five plans;238 historical claims,163 literal current-source quote occurrences. S595 preview retains nickel mapping subsequently withdrawn; S777 preview timestamp differs from applied record. Both differences are explicitly retained. |
| attached-claims | REVIEW_WORK/batch077/record09/current-claim-and-history-source-joins.json | context_only | All26 current attached stock claims and47 historical JSON change quotes join exact freshly captured source bytes and decoded source nodes. |
| full-catalog | REVIEW_WORK/batch077/record09/complete-current-grounding-reading.json | context_only | All262 recursive current ID/label slots and795 exact packaged rows read, including rejected aliases and candidate-form context; no current numeric legacy MIM assertions found. |
| reading-proof | REVIEW_WORK/batch077/record09/root-reading-reuse-proof.json | context_only | Byte-exact prior-reading reuse is bounded to actual root-read scientific scopes.353 new historical cells plus384 exact prior values reconstruct22 full reports;250 new MIM rows plus545 prior exact rows are retained. |
| ols53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; _embedded.terms exact accession scientific fields | supports | Exact current ontology accession, label, obsolete flag, definition, synonyms and chemical annotations read. Chemical identity only; no recipe or growth inference. |
| ols34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; _embedded.terms exact accession scientific fields | supports | Exact current ontology accession, label, obsolete flag, definition, synonyms and chemical annotations read. Chemical identity only; no recipe or growth inference. |
| ols8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; _embedded.terms exact accession scientific fields | supports | Exact current ontology accession, label, obsolete flag, definition, synonyms and chemical annotations read. Chemical identity only; no recipe or growth inference. |
| ols26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols32138 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32138; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols63675 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63675; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols16135 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16135; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch077/record09/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch077/record09/grounding-inventory.json | context_only | All selected target/owner recursive asserted identifier/label slots and explicitly scoped dependency slots; current OLS scientific objects and packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch077/record09/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch077/record09/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch077/record09/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch077/record09/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch077/record09/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch077/record09/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch077/record09/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- Completion is partial because current exactKOMODO739 andMediaList requests return403. Local target and owners are resolved; copiedDSMZ ingredients do not authenticate live cross-source identity.
- Only reusable stocks595/777/5980 are assessed dependencies. Other normalized stage records, receiving media and unrelated parent-plan/archive rows are outside scope. API161 is restricted to identity/inventory and stock5980 evidence.
- The source gives stage doses and provider volumes, includingA952ml despite952.5ml summed liquid entries; no independently measured final-medium volume is established. No density, unknown percentage basis, mmol_l conversion or silent source correction is inferred.
- No strain-specific growth or taxonomic curation is performed. Generic applications and source names do not prove growth. iModulonDB is inapplicable to this formulation review.
- Four original canonical target diagnostics passed once; the reference validator performed zero checks. No dedicated focused embedded-history validator is documented; standalone history checks are a different scope. No corpus-wide gate or historical execution replay is claimed.
- Exact-byte reading reuse is explicitly documented; all new scientific values were directly read. No recipe, generated product or prior review was edited.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- This draft authoring step performed no formal review validation/save, Git mutation or publication.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T203620Z-batch077-record09-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Desulfonema ishimotoi medium: six preparation stages and repaired stock definitions'
started_at: '2026-10-28T20:14:54.267626Z'
finished_at: '2026-10-28T20:36:20.083438Z'
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
summary: The selected target and its two maintained contributors share36 flattened
  ingredient quantities. DSMZ739 instead assembles six stages A–F, with separate SL-10,
  selenite-tungstate and10x vitamin stocks. Existing reusable-stock repairs and26
  attached claims are credited. Remaining defects concern stage boundaries, isobutyric-acid
  units, hydrochloric-acid percent basis, two chemical-form assertions, preparation
  placement and lost generated instructions. Exact live KOMODO739 authentication remains
  unavailable.
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
  - path: data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
    sha256: 9dff1704cd890a8b71767516ae311fceb8f31c1c2fb5ad3eb891cb9f1f5ca2fd
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
    sha256: 44e9c12ab6fed0694500d3ff4c0d02743d4693325c12441df1ea1748d9f8a345
    role: context
  - path: data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml
    sha256: 66b8e6720786901f81711a61963715d62a00f251ea964593cc61edd05fd0415c
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml
    sha256: 6d335bc921a8e8a99bae829fda6e81ae023de16a5c19a71b881fb54a9c14e082
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml
    sha256: b8b5efd085ffa7d0f4e3da6ccf82c0de49b364082867d531beefa757fa3c5950
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml
    sha256: 9153ff2e0d3d0c3a28989b2de6264998a0b09c845f531d6e6b366353e215ebba
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json
    sha256: f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml.md
    sha256: 0db3f0e8187093192f064079135823c6e1c24377eda94c07c91f29d66dce0889
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
    sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfonema_ishimotoi_medium.yaml.md
    sha256: 96717c28dbaaa274ff8361963b67acce2e5e3077859797a2059a495ed113e1ae
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-0500-1000/plan.json
    sha256: ad06448655bb31d1ec7e44000e12c974cdb8ab41ce407fd799ca67b925f5eead
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-0500-1000/records/bacterial/mediadive_777_Selenite-tungstate_solution.yaml.md
    sha256: c6e53cf03c3b24e7bcd57766397f4c30db7aa156e2c722d4291b40e319389f65
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-stocks/mediadive_595_Trace_element_solution_SL-10.md
    sha256: 3dde849738132c179026f204cf3990ec822c4dbaa7def52c1b259ed9a187c00e
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-stocks/mediadive_5980_Wolin_s_vitamin_solution_10x.md
    sha256: f2fe262502bc7b014e102df78f0d05196f15c28c02908757d89ab110de98be56
    role: context
  - path: reports/ingredient_concentration_curation/20261009-methanofollis-family/applied-records/S5980.md
    sha256: c73b7cc5dca7e8446e5dcac3c02cecbf25ba80fc42e07f36bae71d94199e5167
    role: context
  - path: reports/ingredient_concentration_curation/20261009-methanofollis-family/plan.json
    sha256: dc2a0e96231feac52125245dc55f41d3deb937970a06d151fba10d2fd63d7a4a
    role: context
  - path: reports/ingredient_concentration_curation/20261009-methanofollis-family/records/S5980.md
    sha256: aa3090fb45f4fdc77f7dcba19ecee2f4268b73c414fbae71a749ee83df10701b
    role: context
  - path: reports/ingredient_concentration_curation/20261009-synthrophomonas-family/applied-records/S595.md
    sha256: 32d47c5797df30da5a85d3b027d70cb73c51e16c892e8c38093f7cfb9a24864b
    role: context
  - path: reports/ingredient_concentration_curation/20261009-synthrophomonas-family/applied-records/S777.md
    sha256: 3960c9febd1df25319e8032d64c3c0702db2d60edeab1e9375074c5d9aeb1f25
    role: context
  - path: reports/ingredient_concentration_curation/20261009-synthrophomonas-family/plan.json
    sha256: 83fdebb5c629773b4b0ec2c5b810a66dc226602ab0df9aed0728eba35a14276d
    role: context
  - path: reports/ingredient_concentration_curation/20261009-synthrophomonas-family/records-ledgers-successor/S595.md
    sha256: 3cbe1213299583de50f08212e026bb27ee12ebdbf6a15e9aea40328a93f7623a
    role: context
  - path: reports/ingredient_concentration_curation/20261009-synthrophomonas-family/records-ledgers-successor/S777.md
    sha256: bb4cd6991e128cfe1ead03b460132dbcf87a7d6f5c1aa12a97302a108d7827ff
    role: context
  - path: reports/ingredient_concentration_curation/20261009-synthrophomonas-family/records/S595.md
    sha256: 3950476a9f134781b3bff175e864b14d62be146e8a5fe3192b85d00a84f4ab19
    role: context
  - path: reports/ingredient_concentration_curation/20261009-synthrophomonas-family/records/S777.md
    sha256: 87a48210ef544ac3f8df3dfe3c281a32a4f97b77669ee8eb5f3ed55e512d2be4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.md
    sha256: 57a94497e2905512066e5d9aa156a18a5b0da709b6b837e9d99498999527f315
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.md
    sha256: 6b47571b29365062251fa8503f1c47cb41898d57a6af34071484373ea31c2cc7
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.md
    sha256: b02195ca5cd7fc565da3ceb561be5e3866521722e981d94b2bda9ebf7c1f9b45
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.md
    sha256: db229dbf7b276e175ded3328d5f1c6940826c5787f6101e5278a80faf0488e4c
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.md
    sha256: 22e4d09decbfb67f326989cc36b747521220cf6a03747698257efdd00c8609d4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.md
    sha256: 8d27a0f8e65712e1261dc6073aa8d2dfe8e97a96343e2e3de70cac57b642d21c
    role: context
  - path: reports/label_plausibility_2026-07-19.tsv
    sha256: eda647ffbb87d5ea90db812858b2d1d9388393c4d1abc8dec78672324c1509d9
    role: context
  - path: reports/media_content_review_manifest.tsv
    sha256: e5ff2f1241ba046ae7a5dc0d543d340bdba10d31fa1fdc3e36203600cf1ec0ce
    role: context
  - path: reports/yaml_record_review/20260921T142652Z-ARCHAEOGLOBUS_SULFATICALLIDUS_MEDIUM.md
    sha256: a70e823102253cda09135e831823875b2f45c3b82fd13016c0b2552e968b149b
    role: context
  - path: reports/yaml_record_review/20260921T161921Z-asw_hd_1_10_diluted.md
    sha256: b8f0b97426cab4d9e8139684ef3a37ffcb2449ea343d971a2c60dcbfd3646686
    role: context
  - path: reports/yaml_record_review/20260922T034655Z-CARBOXYDOCELLA_MANGANICA_MEDIUM.md
    sha256: 901ff56ba505f5131022332e1eb13d6f5ae9cb2c8225cdcd2453a9d28bbe4c51
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
  - path: scripts/fix_primary_term_grounding.py
    sha256: 9d35bef88897003d1ae3af0789103052d8574a3d33b4d1e504e431184d2681b6
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
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
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
    role: context
  - path: scripts/repair_jcm_stock_preparations.py
    sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
    role: context
  - path: scripts/review_solution_concentration_evidence.py
    sha256: 40a5bb439caf0791caff746a1eac8d5069525f381c7f3b52556c26937741f65a
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
  selection: Actual batch077 native selection index 09.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006388
targets:
- target_id: CultureMech:006388
  path: data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
  label: desulfonema_ishimotoi_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:006388
  command: just validate-schema data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
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
  - CultureMech:006388
  command: just validate-strict data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
    --out REVIEW_WORK/batch077/record09/strict.tsv --workers 1 --quiet
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
  - CultureMech:006388
  command: just validate-terms data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
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
  - CultureMech:006388
  command: just validate-references data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 9dff1704cd890a8b71767516ae311fceb8f31c1c2fb5ad3eb891cb9f1f5ca2fd
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 44e9c12ab6fed0694500d3ff4c0d02743d4693325c12441df1ea1748d9f8a345
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 66b8e6720786901f81711a61963715d62a00f251ea964593cc61edd05fd0415c
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch077/record09/identity-search.json
  accessed_at: '2026-10-28T20:27:16.060407Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems and stable identity resolve the owner;
    only exact resolved owner matches are retained in this result. Similar names and
    source accessions are not promoted to owners.
  snapshot_sha256: 4f4f5147437630d692359498dbdd12712225dd9639c3324779b6c0647b6ff716
- evidence_id: stock-595
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml
  locator: Complete document
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Entire current stock record, composition, preparation, references, attached
    claims and append-only history read. Only this exact stock definition is assessed;
    other receiving media are excluded.
  snapshot_sha256: 6d335bc921a8e8a99bae829fda6e81ae023de16a5c19a71b881fb54a9c14e082
- evidence_id: stock-777
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml
  locator: Complete document
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Entire current stock record, composition, preparation, references, attached
    claims and append-only history read. Only this exact stock definition is assessed;
    other receiving media are excluded.
  snapshot_sha256: 9153ff2e0d3d0c3a28989b2de6264998a0b09c845f531d6e6b366353e215ebba
- evidence_id: stock-5980
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml
  locator: Complete document
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Entire current stock record, composition, preparation, references, attached
    claims and append-only history read. Only this exact stock definition is assessed;
    other receiving media are excluded.
  snapshot_sha256: b8b5efd085ffa7d0f4e3da6ccf82c0de49b364082867d531beefa757fa3c5950
- evidence_id: dsm739
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium739.pdf
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T20:14:12.525590Z'
  support: supports
  summary: 'All three PDF pages visually and textually read: literal A–F preparation
    amounts, source stock definitions, gas and sterilization stages, final pH7, optional
    reducing addition and inoculum note. No independently measured final volume is
    stated.'
  snapshot_sha256: 8f6995c8cd98aa733aaeedf0cf338c9652d9af09dc4532e8850c8f0479a052be
- evidence_id: api739
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/739
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T20:14:12.383714Z'
  support: supports
  summary: Complete medium identity and all ten solution objects read, including all
    recipe, preparation and provider metadata. Main1512 reports1003ml; A1513 reports952ml.
    These provider volumes are separate from measured final volume and do not make
    nested stock rates whole-medium rates.
  snapshot_sha256: 8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f
- evidence_id: solution595
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/595
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T20:15:43.312764Z'
  support: supports
  summary: Full standalone SL-10 JSON read, including10ml HCl25%, eight salt masses,990ml
    starting water and explicit make-up to1000ml. Source digest equals historical
    records. Percent basis and density are not supplied.
  snapshot_sha256: 5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab
- evidence_id: solution777
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/777
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T20:15:43.329648Z'
  support: supports
  summary: 'Full current stock JSON scientific scope read through exact-byte equality
    to root-read076 capture: three solutes,1000ml water, provider1000ml stock volume,
    no steps. Current YAML and history also match the earlier fully read bytes.'
  snapshot_sha256: 3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2
- evidence_id: solution5980
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5980
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T20:15:43.320784Z'
  support: supports
  summary: 'Full current10x vitamin stock JSON read through exact-byte equality to
    root-read076 capture: ten vitamins and1000ml water, source-explicit D-calcium
    pantothenate and DL-lipoic acid. Current stock YAML, claims and history match
    earlier fully read bytes.'
  snapshot_sha256: 2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c
- evidence_id: api161
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/161
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T20:15:43.500443Z'
  support: supports
  summary: Only medium identity, solution inventory and exact solution5980 object
    are assessed to authenticate existing stock evidence. Its raw capture exactly
    matches the earlier root-read capture; other recipe and growth claims are excluded.
  snapshot_sha256: 53d710b65b9a45b9d21c2fddd18a86b41de41d18c0a4c2cbd7de44b0a2ef8666
- evidence_id: komodo739
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=739
  locator: Exact current accession endpoint
  accessed_at: '2026-10-28T20:14:11.832260Z'
  support: unknown
  summary: HTTP403 challenge body read. Current source formulation and cross-source
    equivalence cannot be authenticated from this attempt; historical mapping remains
    attributed context.
  search_scope: Exact accession and MediaList endpoints from current identity/historical
    mapping; no absence inferred from access failure.
  snapshot_sha256: b4ed8a40c133092934facf824fe4bdd87158edbbab76f57c6d0c28ddcb37c166
- evidence_id: komodoList
  kind: search
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact current accession endpoint
  accessed_at: '2026-10-28T20:14:11.807925Z'
  support: unknown
  summary: HTTP403 challenge body read. Current source formulation and cross-source
    equivalence cannot be authenticated from this attempt; historical mapping remains
    attributed context.
  search_scope: Exact accession and MediaList endpoints from current identity/historical
    mapping; no absence inferred from access failure.
  snapshot_sha256: 0e65b77081b408a9ca05b7663c19adccd907fe2533534177064627f661c26eda
- evidence_id: historical-0
  kind: record_content
  reference: reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md
  locator: All non-table text plus exact739row
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Selected archive methodology and exact739pair read; unrelated table rows
    excluded.
  snapshot_sha256: a723d4b7950bf4ac296a8a7fe4890d4d0881199a5d17c12a5fe39c2afbc40a10
- evidence_id: historical-1
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: 0db3f0e8187093192f064079135823c6e1c24377eda94c07c91f29d66dce0889
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfonema_ishimotoi_medium.yaml.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: 96717c28dbaaa274ff8361963b67acce2e5e3077859797a2059a495ed113e1ae
- evidence_id: historical-3
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-0500-1000/records/bacterial/mediadive_777_Selenite-tungstate_solution.yaml.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: c6e53cf03c3b24e7bcd57766397f4c30db7aa156e2c722d4291b40e319389f65
- evidence_id: historical-4
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-stocks/mediadive_595_Trace_element_solution_SL-10.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: 3dde849738132c179026f204cf3990ec822c4dbaa7def52c1b259ed9a187c00e
- evidence_id: historical-5
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-stocks/mediadive_5980_Wolin_s_vitamin_solution_10x.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: f2fe262502bc7b014e102df78f0d05196f15c28c02908757d89ab110de98be56
- evidence_id: historical-6
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261009-methanofollis-family/applied-records/S5980.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: c73b7cc5dca7e8446e5dcac3c02cecbf25ba80fc42e07f36bae71d94199e5167
- evidence_id: historical-7
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261009-methanofollis-family/records/S5980.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: aa3090fb45f4fdc77f7dcba19ecee2f4268b73c414fbae71a749ee83df10701b
- evidence_id: historical-8
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261009-synthrophomonas-family/applied-records/S595.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: 32d47c5797df30da5a85d3b027d70cb73c51e16c892e8c38093f7cfb9a24864b
- evidence_id: historical-9
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261009-synthrophomonas-family/applied-records/S777.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: 3960c9febd1df25319e8032d64c3c0702db2d60edeab1e9375074c5d9aeb1f25
- evidence_id: historical-10
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261009-synthrophomonas-family/records-ledgers-successor/S595.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: 3cbe1213299583de50f08212e026bb27ee12ebdbf6a15e9aea40328a93f7623a
- evidence_id: historical-11
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261009-synthrophomonas-family/records-ledgers-successor/S777.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: bb4cd6991e128cfe1ead03b460132dbcf87a7d6f5c1aa12a97302a108d7827ff
- evidence_id: historical-12
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261009-synthrophomonas-family/records/S595.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: 3950476a9f134781b3bff175e864b14d62be146e8a5fe3192b85d00a84f4ab19
- evidence_id: historical-13
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261009-synthrophomonas-family/records/S777.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: 87a48210ef544ac3f8df3dfe3c281a32a4f97b77669ee8eb5f3ed55e512d2be4
- evidence_id: historical-14
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: 57a94497e2905512066e5d9aa156a18a5b0da709b6b837e9d99498999527f315
- evidence_id: historical-15
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: 6b47571b29365062251fa8503f1c47cb41898d57a6af34071484373ea31c2cc7
- evidence_id: historical-16
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: b02195ca5cd7fc565da3ceb561be5e3866521722e981d94b2bda9ebf7c1f9b45
- evidence_id: historical-17
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: db229dbf7b276e175ded3328d5f1c6940826c5787f6101e5278a80faf0488e4c
- evidence_id: historical-18
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: 22e4d09decbfb67f326989cc36b747521220cf6a03747698257efdd00c8609d4
- evidence_id: historical-19
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: 8d27a0f8e65712e1261dc6073aa8d2dfe8e97a96343e2e3de70cac57b642d21c
- evidence_id: historical-20
  kind: record_content
  reference: reports/yaml_record_review/20260921T142652Z-ARCHAEOGLOBUS_SULFATICALLIDUS_MEDIUM.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: a70e823102253cda09135e831823875b2f45c3b82fd13016c0b2552e968b149b
- evidence_id: historical-21
  kind: record_content
  reference: reports/yaml_record_review/20260921T161921Z-asw_hd_1_10_diluted.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: b8f0b97426cab4d9e8139684ef3a37ffcb2449ea343d971a2c60dcbfd3646686
- evidence_id: historical-22
  kind: record_content
  reference: reports/yaml_record_review/20260922T034655Z-CARBOXYDOCELLA_MANGANICA_MEDIUM.md
  locator: Complete report; historical-reading-cells.json reconstructs original bytes
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Complete per-record report read through lossless cell reconstruction; earlier
    findings are reassessed against current source and record bytes. Unrelated receiving-medium
    conclusions are context only.
  snapshot_sha256: 901ff56ba505f5131022332e1eb13d6f5ae9cb2c8225cdcd2453a9d28bbe4c51
- evidence_id: parent-plan-0
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json
  locator: Exact selected rows in selected-parent-plan-reading.json
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Six exact selected owner/dependency rows across five plans were read, including
    all238 claims and before/after comparisons. Unrelated records and global conclusions
    excluded.
  snapshot_sha256: f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823
- evidence_id: parent-plan-1
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
  locator: Exact selected rows in selected-parent-plan-reading.json
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Six exact selected owner/dependency rows across five plans were read, including
    all238 claims and before/after comparisons. Unrelated records and global conclusions
    excluded.
  snapshot_sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
- evidence_id: parent-plan-2
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-0500-1000/plan.json
  locator: Exact selected rows in selected-parent-plan-reading.json
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Six exact selected owner/dependency rows across five plans were read, including
    all238 claims and before/after comparisons. Unrelated records and global conclusions
    excluded.
  snapshot_sha256: ad06448655bb31d1ec7e44000e12c974cdb8ab41ce407fd799ca67b925f5eead
- evidence_id: parent-plan-3
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261009-methanofollis-family/plan.json
  locator: Exact selected rows in selected-parent-plan-reading.json
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Six exact selected owner/dependency rows across five plans were read, including
    all238 claims and before/after comparisons. Unrelated records and global conclusions
    excluded.
  snapshot_sha256: dc2a0e96231feac52125245dc55f41d3deb937970a06d151fba10d2fd63d7a4a
- evidence_id: parent-plan-4
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261009-synthrophomonas-family/plan.json
  locator: Exact selected rows in selected-parent-plan-reading.json
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Six exact selected owner/dependency rows across five plans were read, including
    all238 claims and before/after comparisons. Unrelated records and global conclusions
    excluded.
  snapshot_sha256: 83fdebb5c629773b4b0ec2c5b810a66dc226602ab0df9aed0728eba35a14276d
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: MediaDive API composition/solution/unit/preparation functions; KOMODO conversion;
    merge/formulation relevant functions
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Current relevant source conversion or merge compatibility functions read;
    exact prior-reading proof is retained for unchanged merge functions. Current code
    is not proof of historical execution.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: MediaDive API composition/solution/unit/preparation functions; KOMODO conversion;
    merge/formulation relevant functions
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Current relevant source conversion or merge compatibility functions read;
    exact prior-reading proof is retained for unchanged merge functions. Current code
    is not proof of historical execution.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: MediaDive API composition/solution/unit/preparation functions; KOMODO conversion;
    merge/formulation relevant functions
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Current relevant source conversion or merge compatibility functions read;
    exact prior-reading proof is retained for unchanged merge functions. Current code
    is not proof of historical execution.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: MediaDive API composition/solution/unit/preparation functions; KOMODO conversion;
    merge/formulation relevant functions
  accessed_at: '2026-10-28T20:27:15.995886Z'
  support: context_only
  summary: Current relevant source conversion or merge compatibility functions read;
    exact prior-reading proof is retained for unchanged merge functions. Current code
    is not proof of historical execution.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: parent-claims
  kind: record_content
  reference: REVIEW_WORK/batch077/record09/selected-parent-plan-reading.json
  accessed_at: '2026-10-28T20:27:16.134371Z'
  support: context_only
  summary: Six selected rows/five plans;238 historical claims,163 literal current-source
    quote occurrences. S595 preview retains nickel mapping subsequently withdrawn;
    S777 preview timestamp differs from applied record. Both differences are explicitly
    retained.
  snapshot_sha256: 13e7041062113690adc65daf75241e500f3c29d260b289daf0330a5699998afa
- evidence_id: attached-claims
  kind: record_content
  reference: REVIEW_WORK/batch077/record09/current-claim-and-history-source-joins.json
  accessed_at: '2026-10-28T20:27:16.134765Z'
  support: context_only
  summary: All26 current attached stock claims and47 historical JSON change quotes
    join exact freshly captured source bytes and decoded source nodes.
  snapshot_sha256: 47cc6021bdc02a5689561c09669447fc5434ba2e916e80d9c8bd350af3a054f7
- evidence_id: full-catalog
  kind: record_content
  reference: REVIEW_WORK/batch077/record09/complete-current-grounding-reading.json
  accessed_at: '2026-10-28T20:27:16.134958Z'
  support: context_only
  summary: All262 recursive current ID/label slots and795 exact packaged rows read,
    including rejected aliases and candidate-form context; no current numeric legacy
    MIM assertions found.
  snapshot_sha256: b852f5a89e34376c416440413905ed8a6e103ce1cfcc2bdb523e165b0c5a931a
- evidence_id: reading-proof
  kind: record_content
  reference: REVIEW_WORK/batch077/record09/root-reading-reuse-proof.json
  accessed_at: '2026-10-28T20:27:16.135217Z'
  support: context_only
  summary: Byte-exact prior-reading reuse is bounded to actual root-read scientific
    scopes.353 new historical cells plus384 exact prior values reconstruct22 full
    reports;250 new MIM rows plus545 prior exact rows are retained.
  snapshot_sha256: 9cb81220e921d1819f2bdfabd9b8587a61a698444d396d233e893c34f0bd257f
- evidence_id: ols53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  locator: _embedded.terms exact accession scientific fields
  accessed_at: '2026-10-28T20:14:12.476389Z'
  support: supports
  summary: Exact current ontology accession, label, obsolete flag, definition, synonyms
    and chemical annotations read. Chemical identity only; no recipe or growth inference.
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
- evidence_id: ols34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: _embedded.terms exact accession scientific fields
  accessed_at: '2026-10-28T20:14:14.835567Z'
  support: supports
  summary: Exact current ontology accession, label, obsolete flag, definition, synonyms
    and chemical annotations read. Chemical identity only; no recipe or growth inference.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: ols8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: _embedded.terms exact accession scientific fields
  accessed_at: '2026-10-28T20:14:16.411348Z'
  support: supports
  summary: Exact current ontology accession, label, obsolete flag, definition, synonyms
    and chemical annotations read. Chemical identity only; no recipe or growth inference.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: ols26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:13.619891Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: ols86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:16.202806Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: ols31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:14.344412Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: ols86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:15.653306Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: ols32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:14.434637Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: ols63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:15.046001Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: ols31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:13.833476Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: ols32138
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32138
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:14.335805Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 74faec6ae9b146967356e528305ebfcaaceca793993fd6cca01e1cf3af2b470b
- evidence_id: ols63675
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63675
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:15.065259Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 4c54df9f2d63f54dea26d64e4ec9fedeb486c2c2abe44b70c5c621512f1fdd3c
- evidence_id: ols16135
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16135
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:13.011470Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 9066add4e624c1d66e8ed2b31b6d8cd83aee6227fe29e0fe5a7bf1d36fedb4ab
- evidence_id: ols86465
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:16.281870Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c
- evidence_id: ols29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:13.709398Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1
- evidence_id: ols76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:15.797645Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: ols17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:13.229871Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
- evidence_id: ols86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:15.674011Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: ols49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:14.948450Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: ols86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:16.253549Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: ols33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:14.436995Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: ols53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:16.015618Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: ols86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:16.032235Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: ols75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:15.573572Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: ols32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:14.408358Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: ols131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:12.488417Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: ols63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:15.434771Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: ols15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:12.557488Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: ols27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:13.749986Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: ols30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:13.833557Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: ols49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:14.992220Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: ols17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:13.223206Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: ols15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:12.624549Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: ols31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:14.231331Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: ols176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:13.140176Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: ols30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:13.803193Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: ols16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:14:13.091883Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: ols15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T20:15:43.410045Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch077/record09/quantity-inventory.json
  accessed_at: '2026-10-28T20:36:20.083438Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: f244b65da350f71092e2ced8428183e398f73024b6bf5bfffd9a8e69867e3682
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch077/record09/grounding-inventory.json
  accessed_at: '2026-10-28T20:27:16.225915Z'
  support: context_only
  summary: All selected target/owner recursive asserted identifier/label slots and
    explicitly scoped dependency slots; current OLS scientific objects and packaged
    MIM preferred-row joins.
  snapshot_sha256: 0e11ffbb70163cb4954301b318ca0f0235d7d78498523c51ff62ad7f375216e8
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch077/record09/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T20:27:16.226189Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: fbbdd74b836450bfee83c40120063767b8c4096b8d59667d20fda0156b82a4fa
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch077/record09/scalar-census.json
  accessed_at: '2026-10-28T20:27:16.226310Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: 2c5cb7a8298e2cea60f8b0ff4ccdfc750b0a021a2a7b2e11b8346f906f2046b8
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch077/record09/validate-schema.json
  accessed_at: '2026-10-28T20:14:55.349365Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: ff50835c2119dff18caca01ec4a522f2f103530b53d895db04295cd234f45274
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch077/record09/validate-strict.json
  accessed_at: '2026-10-28T20:14:56.290655Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch077/record09/strict.tsv\n"
  snapshot_sha256: a0aaa93a912580851228a36390f1f59665866354817e80f83dae67165d36ef69
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch077/record09/validate-terms.json
  accessed_at: '2026-10-28T20:14:57.321018Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: dfeecfa43c14c699fd1178d35a1b3f6352d1fb5f8a71bcb73ebbfe0885addf27
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch077/record09/validate-references.json
  accessed_at: '2026-10-28T20:14:58.089088Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: 6e32ed1bd41c2e3d0f6c24268e042f31ce0957833d91853fa30ff7b48389971a
assessments:
- assessment_id: a1
  area: identity
  topic: Exact lineage and independent source limits
  outcome: supported
  summary: Exact merged_from stems resolve the KOMODO739 and DSMZ739 contributors.
    Their36ingredient signatures match locally and the historicalSOURCE_DUPLICATE
    link records copied DSMZ composition. DSMZ identity is independently authenticated;
    matching local signatures and the old MediaList row do not establish current KOMODO
    equivalence after403 responses.
  target_ids:
  - CultureMech:006388
  evidence_ids:
  - identity-search
  - local-target
  - owner-1
  - owner-2
  - dsm739
  - api739
  - komodo739
  - komodoList
- assessment_id: a2
  area: completeness
  topic: Repair credit and source stage preservation
  outcome: supported
  summary: Current stocks595/777/5980 have complete declared compositions and no false
    placeholders. SL-10 preserves0.01L25%HCl, explicit water make-up and withdrawal
    of generic nickel mapping. Stocks777/5980 preserve1L batch water and all current
    evidence. DSMZ owner retains four preparation entries, while target/KOMODO omit
    them. DEFINED,LIQUID and mainpH7 are compatible with inspectedDSMZ739; bacterial
    filing and generic applications are not growth evidence.
  target_ids:
  - CultureMech:006388
  evidence_ids:
  - stock-595
  - stock-777
  - stock-5980
  - owner-2
  - dsm739
  - api739
- assessment_id: a3
  area: evidence
  topic: Historical claims reconciled to current bytes
  outcome: supported
  summary: Twenty-two full reports and selected archive739context were read. Six selected
    rows/five parent plans retain238claims, including163literal source-quote occurrences.
    All26current attached stock claims and47history-change quotes join fresh source
    bytes. Older medium reviews withheld all36flattened rates; unchanged owner hashes
    confirm they were not repaired. SL-10 initial preview retains nickel mapping later
    withdrawn in applied/current bytes; S777 preview/current difference is the final-event
    timestamp, not a new formulation. Old source digests authenticate current byte
    equality, not historic access time or execution.
  target_ids:
  - CultureMech:006388
  evidence_ids:
  - parent-claims
  - attached-claims
  - reading-proof
  - api739
  - solution595
  - solution777
  - solution5980
  - api161
- assessment_id: a4
  area: ownership
  topic: Current writer limitations
  outcome: concern
  summary: Current MediaDive API composition uses only the first solution and preserves
    referenced solution descriptors; its rawml-toML_PER_L conversion still needs a
    batch denominator, and its preparation function still combines steps across solutions.
    The currentKOMODO converter writes aerobic metadata and uses strftime%f; this
    is a mechanism reference without historical execution proof. Use current compatible-formulation
    merge safeguards after maintained-source curation.
  target_ids:
  - CultureMech:006388
  evidence_ids:
  - writer-0
  - writer-1
  - writer-2
  - writer-3
- assessment_id: a5
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:006388
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "Stage Solution A: NaCl", "source": {"evidence_id":
    "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path":
    "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\":
    25,\n                        \"unit\": \"g\",\n                        \"g_l\":
    26.2605,\n                        \"mmol_l\": 449.358,\n                        \"optional\":
    0\n                    }"}, "decision": "mixed", "rationale": "Literal 25 g belongs
    to Solution A (provider volume952ml); source g_l=26.2605 is stage-scoped. Retain
    the batch input and boundary. No measured final volume or whole-medium rate is
    inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path":
    "ingredients[0].concentration", "stored_value": {"value": "26.2605", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium
    concentration; exact KOMODO source identity remains separately unresolved."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "26.2605",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "26.2605",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}]}, {"quantity_id": "q2", "topic": "Stage Solution A: MgCl2 x 6 H2O",
    "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\":
    5.6,\n                        \"unit\": \"g\",\n                        \"g_l\":
    5.88235,\n                        \"mmol_l\": 28.9339,\n                        \"optional\":
    0\n                    }"}, "decision": "mixed", "rationale": "Literal 5.6 g belongs
    to Solution A (provider volume952ml); source g_l=5.88235 is stage-scoped. Retain
    the batch input and boundary. No measured final volume or whole-medium rate is
    inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path":
    "ingredients[1].concentration", "stored_value": {"value": "5.88235", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium
    concentration; exact KOMODO source identity remains separately unresolved."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "5.88235",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "5.88235",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}]}, {"quantity_id": "q3", "topic": "Stage Solution A: MgSO4 x 7 H2O",
    "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\":
    6.8,\n                        \"unit\": \"g\",\n                        \"g_l\":
    7.14286,\n                        \"mmol_l\": 28.9799,\n                        \"optional\":
    0\n                    }"}, "decision": "mixed", "rationale": "Literal 6.8 g belongs
    to Solution A (provider volume952ml); source g_l=7.14286 is stage-scoped. Retain
    the batch input and boundary. No measured final volume or whole-medium rate is
    inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path":
    "ingredients[2].concentration", "stored_value": {"value": "7.14286", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium
    concentration; exact KOMODO source identity remains separately unresolved."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "7.14286",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "7.14286",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}]}, {"quantity_id": "q4", "topic": "Stage Solution A: CaCl2 x 2 H2O",
    "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[1].recipe[3]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\":
    1.4,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1.47059,\n                        \"mmol_l\": 10.003,\n                        \"optional\":
    0\n                    }"}, "decision": "mixed", "rationale": "Literal 1.4 g belongs
    to Solution A (provider volume952ml); source g_l=1.47059 is stage-scoped. Retain
    the batch input and boundary. No measured final volume or whole-medium rate is
    inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path":
    "ingredients[3].concentration", "stored_value": {"value": "1.47059", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium
    concentration; exact KOMODO source identity remains separately unresolved."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "1.47059",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "1.47059",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}]}, {"quantity_id": "q5", "topic": "Stage Solution A: KCl", "source":
    {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[1].recipe[4]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\":
    0.72,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.756303,\n                        \"mmol_l\": 10.1449,\n                        \"optional\":
    0\n                    }"}, "decision": "mixed", "rationale": "Literal 0.72 g
    belongs to Solution A (provider volume952ml); source g_l=0.756303 is stage-scoped.
    Retain the batch input and boundary. No measured final volume or whole-medium
    rate is inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path":
    "ingredients[4].concentration", "stored_value": {"value": "0.756303", "unit":
    "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not
    a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.756303",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.756303",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}]}, {"quantity_id": "q6", "topic": "Stage Solution A: KH2PO4", "source":
    {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[1].recipe[5]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\":
    0.14,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.147059,\n                        \"mmol_l\": 1.08064,\n                        \"optional\":
    0\n                    }"}, "decision": "mixed", "rationale": "Literal 0.14 g
    belongs to Solution A (provider volume952ml); source g_l=0.147059 is stage-scoped.
    Retain the batch input and boundary. No measured final volume or whole-medium
    rate is inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path":
    "ingredients[5].concentration", "stored_value": {"value": "0.147059", "unit":
    "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not
    a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.147059",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.147059",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}]}, {"quantity_id": "q7", "topic": "Stage Solution A: NH4Cl", "source":
    {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\":
    0.25,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.262605,\n                        \"mmol_l\": 4.90942,\n                        \"optional\":
    0\n                    }"}, "decision": "mixed", "rationale": "Literal 0.25 g
    belongs to Solution A (provider volume952ml); source g_l=0.262605 is stage-scoped.
    Retain the batch input and boundary. No measured final volume or whole-medium
    rate is inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path":
    "ingredients[6].concentration", "stored_value": {"value": "0.262605", "unit":
    "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity is not
    a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.262605",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.262605",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}]}, {"quantity_id": "q8", "topic": "Stage Solution A: Sodium resazurin",
    "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[1].recipe[9]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\":
    \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.00052521,\n                        \"mmol_l\":
    0.00209105,\n                        \"optional\": 0\n                    }"},
    "decision": "mixed", "rationale": "StageA receives0.5ml of0.1%w/v sodium-resazurin
    stock. Explicit basis gives1mg/ml stock and0.5mg delivered. Provider0.00052521g/L
    uses stageA952ml; it is not an assembled-medium rate. Preserve sodium identity,
    strength and dose separately.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00052521",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00052521",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00052521",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}]}, {"quantity_id": "q9", "topic": "Stage Solution B: Na-acetate
    x 3 H2O", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Na-acetate x 3 H2O\",\n                        \"compound_id\": 294,\n                        \"amount\":
    2.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    250,\n                        \"optional\": 0\n                    }"}, "decision":
    "mixed", "rationale": "Literal 2.5 g belongs to Solution B (provider volume10ml);
    source g_l=250 is stage-scoped. Retain the batch input and boundary. No measured
    final volume or whole-medium rate is inferred from nominal stage sums; no provider
    mmol_l is endorsed.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "250",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "250",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "250",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}]}, {"quantity_id": "q10", "topic": "Stage Solution B: Disodium succinate",
    "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[2].recipe[1]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Disodium succinate\",\n                        \"compound_id\": 1189,\n                        \"amount\":
    0.1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    10,\n                        \"mmol_l\": 61.7094,\n                        \"optional\":
    0\n                    }"}, "decision": "mixed", "rationale": "Literal 0.1 g belongs
    to Solution B (provider volume10ml); source g_l=10 is stage-scoped. Retain the
    batch input and boundary. No measured final volume or whole-medium rate is inferred
    from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path":
    "ingredients[9].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium
    concentration; exact KOMODO source identity remains separately unresolved."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "10",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "10",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}]}, {"quantity_id": "q11", "topic": "Stage Solution B: Isobutyric
    acid", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[2].recipe[2]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Isobutyric acid\",\n                        \"compound_id\": 222,\n                        \"amount\":
    0.19,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }"}, "decision": "mixed", "rationale": "The literal liquid
    input is0.19ml =0.00019L in stageB. No density is stated; molecular mass is not
    density. Preserve the batch volume and stage, not a mass concentration.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path":
    "ingredients[10].concentration", "stored_value": {"value": "0.19", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "Source states0.19ml isobutyric acid in stageB;0.19G_PER_L
    has no supported mass conversion or receiving-volume basis."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.19",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source states0.19ml
    isobutyric acid in stageB;0.19G_PER_L has no supported mass conversion or receiving-volume
    basis."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.19",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Source states0.19ml
    isobutyric acid in stageB;0.19G_PER_L has no supported mass conversion or receiving-volume
    basis."}]}, {"quantity_id": "q12", "topic": "Stage Solution D: AlK(SO4)2 x 12
    H2O", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[4].recipe[0]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\":
    0.48,\n                        \"unit\": \"g\",\n                        \"g_l\":
    48,\n                        \"mmol_l\": 101.183,\n                        \"optional\":
    0\n                    }"}, "decision": "mixed", "rationale": "Literal 0.48 g
    belongs to Solution D (provider volume10ml); source g_l=48 is stage-scoped. Retain
    the batch input and boundary. No measured final volume or whole-medium rate is
    inferred from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path":
    "ingredients[11].concentration", "stored_value": {"value": "48", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium
    concentration; exact KOMODO source identity remains separately unresolved."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "48",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "48",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}]}, {"quantity_id": "q13", "topic": "Stage Solution E: Na2CO3", "source":
    {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[5].recipe[0]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    50,\n                        \"mmol_l\": 471.752,\n                        \"optional\":
    0\n                    }"}, "decision": "mixed", "rationale": "Literal 1 g belongs
    to Solution E (provider volume20ml); source g_l=50 is stage-scoped. Retain the
    batch input and boundary. No measured final volume or whole-medium rate is inferred
    from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path":
    "ingredients[12].concentration", "stored_value": {"value": "50", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium
    concentration; exact KOMODO source identity remains separately unresolved."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "50",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "50",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}]}, {"quantity_id": "q14", "topic": "Stage Solution F: Na2S x 9 H2O",
    "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[6].recipe[0]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\":
    0.3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    30,\n                        \"mmol_l\": 124.905,\n                        \"optional\":
    0\n                    }"}, "decision": "mixed", "rationale": "Literal 0.3 g belongs
    to Solution F (provider volume10ml); source g_l=30 is stage-scoped. Retain the
    batch input and boundary. No measured final volume or whole-medium rate is inferred
    from nominal stage sums; no provider mmol_l is endorsed.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path":
    "ingredients[13].concentration", "stored_value": {"value": "30", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "Copied stage quantity is not a whole-medium
    concentration; exact KOMODO source identity remains separately unresolved."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "30",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "30",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Copied stage quantity
    is not a whole-medium concentration; exact KOMODO source identity remains separately
    unresolved."}]}, {"quantity_id": "q15", "topic": "Stock595: HCl", "source": {"evidence_id":
    "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595", "raw_path":
    "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab",
    "locator": "$.data.recipe[0]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote":
    "{\n                \"recipe_order\": 1,\n                \"compound\": \"HCl\",\n                \"compound_id\":
    68,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": \"25%\",\n                \"amount\": 10,\n                \"unit\":
    \"ml\",\n                \"g_l\": 2.5,\n                \"mmol_l\": 68.5683,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Literal10ml HCl with attribute25%
    is0.01L batch input, already repaired in currentSL-10. The source does not identify
    percent basis or density; provider2.5g/L cannot establish pure-HCl mass. Medium
    layers still carry that value without scope.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path": "ingredients[14].concentration",
    "stored_value": {"value": "2.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale":
    "Value belongs to a separately prepared stock, not the receiving assembled medium.
    Exact KOMODO branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "2.5",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "2.5",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[0].concentration", "stored_value": {"value": "0.01",
    "unit": "L"}, "decision": "verified", "rationale": "Current standalone stock quantity
    and attached evidence preserve the source scope; retain the existing repair."}]},
    {"quantity_id": "q16", "topic": "Stock595: FeCl2 x 4 H2O", "source": {"evidence_id":
    "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595", "raw_path":
    "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab",
    "locator": "$.data.recipe[1]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote":
    "{\n                \"recipe_order\": 2,\n                \"compound\": \"FeCl2
    x 4 H2O\",\n                \"compound_id\": 260,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1.5,\n                \"unit\":
    \"g\",\n                \"g_l\": 1.5,\n                \"mmol_l\": 7.54482,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 1.5 g and provider
    g_l=1.5 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml;
    other stocks retain provider normalization without independent final-volume certification.
    DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate
    is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "1.5",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "1.5",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "1.5",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[1].concentration", "stored_value": {"value": "1.5",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q17", "topic": "Stock595: ZnCl2", "source": {"evidence_id":
    "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595", "raw_path":
    "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab",
    "locator": "$.data.recipe[2]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote":
    "{\n                \"recipe_order\": 3,\n                \"compound\": \"ZnCl2\",\n                \"compound_id\":
    64,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 70,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.513573,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 70 mg and provider
    g_l=0.07 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml;
    other stocks retain provider normalization without independent final-volume certification.
    DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate
    is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.07",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.07",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.07",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[2].concentration", "stored_value": {"value": "0.07",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q18", "topic": "Stock595: MnCl2 x 4 H2O", "source":
    {"evidence_id": "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256":
    "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab", "locator":
    "$.data.recipe[3]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote": "{\n                \"recipe_order\":
    4,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\":
    36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.505293,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 100 mg and provider
    g_l=0.1 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml;
    other stocks retain provider normalization without independent final-volume certification.
    DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate
    is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[3].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q19", "topic": "Stock595: H3BO3", "source": {"evidence_id":
    "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595", "raw_path":
    "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256": "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab",
    "locator": "$.data.recipe[4]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote":
    "{\n                \"recipe_order\": 5,\n                \"compound\": \"H3BO3\",\n                \"compound_id\":
    37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 6,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.006,\n                \"mmol_l\": 0.0970246,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 6 mg and provider
    g_l=0.006 apply only to this1000ml-declared stock. SL-10 has explicit make-up
    to1000ml; other stocks retain provider normalization without independent final-volume
    certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted
    stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.006",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.006",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.006",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[4].concentration", "stored_value": {"value": "0.006",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q20", "topic": "Stock595: CoCl2 x 6 H2O", "source":
    {"evidence_id": "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256":
    "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab", "locator":
    "$.data.recipe[5]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote": "{\n                \"recipe_order\":
    6,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\":
    38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 190,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.19,\n                \"mmol_l\": 1.46335,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 190 mg and provider
    g_l=0.19 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml;
    other stocks retain provider normalization without independent final-volume certification.
    DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate
    is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.19",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.19",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.19",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[5].concentration", "stored_value": {"value": "0.19",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q21", "topic": "Stock595: CuCl2 x 2 H2O", "source":
    {"evidence_id": "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256":
    "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab", "locator":
    "$.data.recipe[6]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote": "{\n                \"recipe_order\":
    7,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\":
    39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0117314,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 2 mg and provider
    g_l=0.002 apply only to this1000ml-declared stock. SL-10 has explicit make-up
    to1000ml; other stocks retain provider normalization without independent final-volume
    certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted
    stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.002",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.002",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.002",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[6].concentration", "stored_value": {"value": "0.002",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q22", "topic": "Stock595: NiCl2 x 6 H2O", "source":
    {"evidence_id": "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256":
    "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab", "locator":
    "$.data.recipe[7]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote": "{\n                \"recipe_order\":
    8,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\":
    40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 24,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.024,\n                \"mmol_l\": 0.185187,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 24 mg and provider
    g_l=0.024 apply only to this1000ml-declared stock. SL-10 has explicit make-up
    to1000ml; other stocks retain provider normalization without independent final-volume
    certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted
    stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.024",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.024",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.024",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[7].concentration", "stored_value": {"value": "0.024",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q23", "topic": "Stock595: Na2MoO4 x 2 H2O", "source":
    {"evidence_id": "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256":
    "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab", "locator":
    "$.data.recipe[8]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote": "{\n                \"recipe_order\":
    9,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\":
    9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 36,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.036,\n                \"mmol_l\": 0.148791,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 36 mg and provider
    g_l=0.036 apply only to this1000ml-declared stock. SL-10 has explicit make-up
    to1000ml; other stocks retain provider normalization without independent final-volume
    certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted
    stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.036",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.036",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.036",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[8].concentration", "stored_value": {"value": "0.036",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q24", "topic": "Stock595: Distilled water", "source":
    {"evidence_id": "solution595", "reference": "https://mediadive.dsmz.de/rest/solution/595",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution595.raw", "raw_sha256":
    "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab", "locator":
    "$.data.recipe[9]", "accessed_at": "2026-10-28T20:15:43.312764Z", "quote": "{\n                \"recipe_order\":
    10,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 990,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }"}, "decision": "verified", "rationale": "SL-10 starts with990ml
    water and explicitly makes up to1000ml; currentVARIABLE to1L final volume is correct.
    Do not replace with a fixed990ml dose or a percentage.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/mediadive_595_Trace_element_solution_SL-10.yaml",
    "field_path": "composition[9].concentration", "stored_value": {"value": "to 1
    L final volume", "unit": "VARIABLE"}, "decision": "verified", "rationale": "Preserve
    the source-backed existing water repair and evidence."}], "additional_sources":
    [{"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[7].steps[0]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl,
    then dilute in water, add and dissolve the other salts. Finally make up to 1000.00
    ml.\"\n                    }"}]}, {"quantity_id": "q25", "topic": "Stock777: NaOH",
    "source": {"evidence_id": "solution777", "reference": "https://mediadive.dsmz.de/rest/solution/777",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution777.raw", "raw_sha256":
    "3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2", "locator":
    "$.data.recipe[0]", "accessed_at": "2026-10-28T20:15:43.329648Z", "quote": "{\n                \"recipe_order\":
    1,\n                \"compound\": \"NaOH\",\n                \"compound_id\":
    256,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.5,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.5,\n                \"mmol_l\": 12.5009,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 0.5 g and provider
    g_l=0.5 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml;
    other stocks retain provider normalization without independent final-volume certification.
    DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate
    is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml",
    "field_path": "composition[0].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q26", "topic": "Stock777: Na2SeO3 x 5 H2O", "source":
    {"evidence_id": "solution777", "reference": "https://mediadive.dsmz.de/rest/solution/777",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution777.raw", "raw_sha256":
    "3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2", "locator":
    "$.data.recipe[1]", "accessed_at": "2026-10-28T20:15:43.329648Z", "quote": "{\n                \"recipe_order\":
    2,\n                \"compound\": \"Na2SeO3 x 5 H2O\",\n                \"compound_id\":
    107,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 3,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.003,\n                \"mmol_l\": 0.0114062,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 3 mg and provider
    g_l=0.003 apply only to this1000ml-declared stock. SL-10 has explicit make-up
    to1000ml; other stocks retain provider normalization without independent final-volume
    certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted
    stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.003",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.003",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.003",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml",
    "field_path": "composition[1].concentration", "stored_value": {"value": "0.003",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q27", "topic": "Stock777: Na2WO4 x 2 H2O", "source":
    {"evidence_id": "solution777", "reference": "https://mediadive.dsmz.de/rest/solution/777",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution777.raw", "raw_sha256":
    "3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2", "locator":
    "$.data.recipe[2]", "accessed_at": "2026-10-28T20:15:43.329648Z", "quote": "{\n                \"recipe_order\":
    3,\n                \"compound\": \"Na2WO4 x 2 H2O\",\n                \"compound_id\":
    249,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0121267,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 4 mg and provider
    g_l=0.004 apply only to this1000ml-declared stock. SL-10 has explicit make-up
    to1000ml; other stocks retain provider normalization without independent final-volume
    certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted
    stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.004",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.004",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.004",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml",
    "field_path": "composition[2].concentration", "stored_value": {"value": "0.004",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q28", "topic": "Stock777: Distilled water", "source":
    {"evidence_id": "solution777", "reference": "https://mediadive.dsmz.de/rest/solution/777",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution777.raw", "raw_sha256":
    "3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2", "locator":
    "$.data.recipe[3]", "accessed_at": "2026-10-28T20:15:43.329648Z", "quote": "{\n                \"recipe_order\":
    4,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }"}, "decision": "verified", "rationale": "Literal1000ml water
    is a1L batch input, correctly stored asL. Provider1000ml volume is separate metadata,
    not independent measured-final-volume evidence; no competing make-up step is present.",
    "layer_assessments": [{"path": "data/normalized_yaml/bacterial/mediadive_777_Selenite-tungstate_solution.yaml",
    "field_path": "composition[3].concentration", "stored_value": {"value": "1", "unit":
    "L"}, "decision": "verified", "rationale": "Preserve the source-backed existing
    water repair and evidence."}]}, {"quantity_id": "q29", "topic": "Stock5980: Biotin",
    "source": {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256":
    "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator":
    "$.data.recipe[0]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\":
    1,\n                \"compound\": \"Biotin\",\n                \"compound_id\":
    46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.0818632,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 20 mg and provider
    g_l=0.02 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml;
    other stocks retain provider normalization without independent final-volume certification.
    DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate
    is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[0].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q30", "topic": "Stock5980: Folic acid", "source":
    {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256":
    "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator":
    "$.data.recipe[1]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\":
    2,\n                \"compound\": \"Folic acid\",\n                \"compound_id\":
    138,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.0453104,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 20 mg and provider
    g_l=0.02 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml;
    other stocks retain provider normalization without independent final-volume certification.
    DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate
    is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[27].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[27].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[27].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[1].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q31", "topic": "Stock5980: Pyridoxine hydrochloride",
    "source": {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256":
    "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator":
    "$.data.recipe[2]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\":
    3,\n                \"compound\": \"Pyridoxine hydrochloride\",\n                \"compound_id\":
    519,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.486287,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 100 mg and provider
    g_l=0.1 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml;
    other stocks retain provider normalization without independent final-volume certification.
    DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate
    is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[28].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[28].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[28].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[2].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q32", "topic": "Stock5980: Thiamine HCl", "source":
    {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256":
    "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator":
    "$.data.recipe[3]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\":
    4,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\":
    1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.148236,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 50 mg and provider
    g_l=0.05 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml;
    other stocks retain provider normalization without independent final-volume certification.
    DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate
    is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[29].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[29].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[29].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[3].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q33", "topic": "Stock5980: Riboflavin", "source":
    {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256":
    "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator":
    "$.data.recipe[4]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\":
    5,\n                \"compound\": \"Riboflavin\",\n                \"compound_id\":
    136,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.132837,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 50 mg and provider
    g_l=0.05 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml;
    other stocks retain provider normalization without independent final-volume certification.
    DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate
    is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[30].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[30].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[30].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[4].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q34", "topic": "Stock5980: Nicotinic acid", "source":
    {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256":
    "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator":
    "$.data.recipe[5]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\":
    6,\n                \"compound\": \"Nicotinic acid\",\n                \"compound_id\":
    139,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.406141,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 50 mg and provider
    g_l=0.05 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml;
    other stocks retain provider normalization without independent final-volume certification.
    DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate
    is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[31].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[31].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[31].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[5].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q35", "topic": "Stock5980: Calcium D-(+)-pantothenate",
    "source": {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256":
    "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator":
    "$.data.recipe[6]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\":
    7,\n                \"compound\": \"Calcium D-(+)-pantothenate\",\n                \"compound_id\":
    1512,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.209846,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 50 mg and provider
    g_l=0.05 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml;
    other stocks retain provider normalization without independent final-volume certification.
    DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate
    is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[32].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[32].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[32].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[6].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q36", "topic": "Stock5980: Vitamin B12", "source":
    {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256":
    "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator":
    "$.data.recipe[7]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\":
    8,\n                \"compound\": \"Vitamin B12\",\n                \"compound_id\":
    18,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.001,\n                \"mmol_l\": 0.00073779,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 1 mg and provider
    g_l=0.001 apply only to this1000ml-declared stock. SL-10 has explicit make-up
    to1000ml; other stocks retain provider normalization without independent final-volume
    certification. DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted
    stock rate is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[33].concentration", "stored_value": {"value": "0.001",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[33].concentration", "stored_value": {"value": "0.001",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[33].concentration", "stored_value": {"value": "0.001",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[7].concentration", "stored_value": {"value": "0.001",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q37", "topic": "Stock5980: p-Aminobenzoic acid",
    "source": {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256":
    "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator":
    "$.data.recipe[8]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\":
    9,\n                \"compound\": \"p-Aminobenzoic acid\",\n                \"compound_id\":
    47,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.364591,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 50 mg and provider
    g_l=0.05 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml;
    other stocks retain provider normalization without independent final-volume certification.
    DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate
    is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[34].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[34].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[34].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[8].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q38", "topic": "Stock5980: (DL)-alpha-Lipoic acid",
    "source": {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256":
    "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator":
    "$.data.recipe[9]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\":
    10,\n                \"compound\": \"(DL)-alpha-Lipoic acid\",\n                \"compound_id\":
    252,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.24233,\n                \"optional\":
    0\n            }"}, "decision": "mixed", "rationale": "Source 50 mg and provider
    g_l=0.05 apply only to this1000ml-declared stock. SL-10 has explicit make-up to1000ml;
    other stocks retain provider normalization without independent final-volume certification.
    DSM739 doses1ml of stock595/777 intoA and1ml of5980 asC; no undiluted stock rate
    is a whole-medium rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[35].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "ingredients[35].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Value belongs to
    a separately prepared stock, not the receiving assembled medium. Exact KOMODO
    branch remains unavailable."}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "ingredients[35].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "Value belongs to a separately
    prepared stock, not the receiving assembled medium. Exact KOMODO branch remains
    unavailable."}, {"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[9].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Current standalone stock
    quantity and attached evidence preserve the source scope; retain the existing
    repair."}]}, {"quantity_id": "q39", "topic": "Stock5980: Distilled water", "source":
    {"evidence_id": "solution5980", "reference": "https://mediadive.dsmz.de/rest/solution/5980",
    "raw_path": "REVIEW_WORK/batch077/source09-supplement/solution5980.raw", "raw_sha256":
    "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c", "locator":
    "$.data.recipe[10]", "accessed_at": "2026-10-28T20:15:43.320784Z", "quote": "{\n                \"recipe_order\":
    11,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }"}, "decision": "verified", "rationale": "Literal1000ml water
    is a1L batch input, correctly stored asL. Provider1000ml volume is separate metadata,
    not independent measured-final-volume evidence; no competing make-up step is present.",
    "layer_assessments": [{"path": "data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
    "field_path": "composition[10].concentration", "stored_value": {"value": "1",
    "unit": "L"}, "decision": "verified", "rationale": "Preserve the source-backed
    existing water repair and evidence."}]}, {"quantity_id": "q40", "topic": "Assembled-medium
    addition: Solution A", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\":
    \"Solution A\",\n                        \"solution_id\": 1513,\n                        \"amount\":
    952,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }"}, "decision": "mixed", "rationale": "Source addition952ml
    ofSolution A. Six stated doses952+10+1+10+20+10 total1003ml nominally, matching
    provider metadata, but are not an independently measured final-volume declaration.
    Do not label literal dosesML_PER_L without an explicit denominator.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "Missing named
    A–F receiving descriptor; preserve literal batch volume and source stage. Resolve
    exactKOMODO scope before transferring DSMZ instructions.", "missing": true}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Missing named A–F receiving descriptor; preserve literal batch volume and source
    stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing":
    true}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Missing named A–F receiving descriptor; preserve literal batch volume and source
    stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing":
    true}]}, {"quantity_id": "q41", "topic": "Assembled-medium addition: Solution
    B", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\":
    \"Solution B\",\n                        \"solution_id\": 1514,\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }"}, "decision": "mixed", "rationale": "Source addition10ml
    ofSolution B. Six stated doses952+10+1+10+20+10 total1003ml nominally, matching
    provider metadata, but are not an independently measured final-volume declaration.
    Do not label literal dosesML_PER_L without an explicit denominator.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "Missing named
    A–F receiving descriptor; preserve literal batch volume and source stage. Resolve
    exactKOMODO scope before transferring DSMZ instructions.", "missing": true}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Missing named A–F receiving descriptor; preserve literal batch volume and source
    stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing":
    true}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Missing named A–F receiving descriptor; preserve literal batch volume and source
    stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing":
    true}]}, {"quantity_id": "q42", "topic": "Assembled-medium addition: Solution
    C", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\":
    \"Solution C\",\n                        \"solution_id\": 1515,\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }"}, "decision": "mixed", "rationale": "Source addition1ml
    ofSolution C. Six stated doses952+10+1+10+20+10 total1003ml nominally, matching
    provider metadata, but are not an independently measured final-volume declaration.
    Do not label literal dosesML_PER_L without an explicit denominator.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "Missing named
    A–F receiving descriptor; preserve literal batch volume and source stage. Resolve
    exactKOMODO scope before transferring DSMZ instructions.", "missing": true}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Missing named A–F receiving descriptor; preserve literal batch volume and source
    stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing":
    true}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Missing named A–F receiving descriptor; preserve literal batch volume and source
    stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing":
    true}]}, {"quantity_id": "q43", "topic": "Assembled-medium addition: Solution
    D", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\":
    \"Solution D\",\n                        \"solution_id\": 1516,\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }"}, "decision": "mixed", "rationale": "Source addition10ml
    ofSolution D. Six stated doses952+10+1+10+20+10 total1003ml nominally, matching
    provider metadata, but are not an independently measured final-volume declaration.
    Do not label literal dosesML_PER_L without an explicit denominator.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "Missing named
    A–F receiving descriptor; preserve literal batch volume and source stage. Resolve
    exactKOMODO scope before transferring DSMZ instructions.", "missing": true}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Missing named A–F receiving descriptor; preserve literal batch volume and source
    stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing":
    true}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Missing named A–F receiving descriptor; preserve literal batch volume and source
    stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing":
    true}]}, {"quantity_id": "q44", "topic": "Assembled-medium addition: Solution
    E", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"solution\":
    \"Solution E\",\n                        \"solution_id\": 1517,\n                        \"amount\":
    20,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }"}, "decision": "mixed", "rationale": "Source addition20ml
    ofSolution E. Six stated doses952+10+1+10+20+10 total1003ml nominally, matching
    provider metadata, but are not an independently measured final-volume declaration.
    Do not label literal dosesML_PER_L without an explicit denominator.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "Missing named
    A–F receiving descriptor; preserve literal batch volume and source stage. Resolve
    exactKOMODO scope before transferring DSMZ instructions.", "missing": true}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Missing named A–F receiving descriptor; preserve literal batch volume and source
    stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing":
    true}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Missing named A–F receiving descriptor; preserve literal batch volume and source
    stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing":
    true}]}, {"quantity_id": "q45", "topic": "Assembled-medium addition: Solution
    F", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\":
    \"Solution F\",\n                        \"solution_id\": 1518,\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }"}, "decision": "mixed", "rationale": "Source addition10ml
    ofSolution F. Six stated doses952+10+1+10+20+10 total1003ml nominally, matching
    provider metadata, but are not an independently measured final-volume declaration.
    Do not label literal dosesML_PER_L without an explicit denominator.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "Missing named
    A–F receiving descriptor; preserve literal batch volume and source stage. Resolve
    exactKOMODO scope before transferring DSMZ instructions.", "missing": true}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Missing named A–F receiving descriptor; preserve literal batch volume and source
    stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing":
    true}, {"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Missing named A–F receiving descriptor; preserve literal batch volume and source
    stage. Resolve exactKOMODO scope before transferring DSMZ instructions.", "missing":
    true}]}, {"quantity_id": "q46", "topic": "Solution A nested stock addition", "source":
    {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[1].recipe[7]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\":
    \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }"}, "decision": "add", "rationale": "Source1ml ofTrace
    element solution SL-10 belongs insideSolution A; this receiving edge is missing
    from the flattened record. Existing reusable stock definitions can be linked after
    exact source and identifier reconciliation. StageA recipe liquid entries sum952.5ml
    while its declared stage volume/delivery is952ml; retain both source statements
    without silently repairing the source.", "layer_assessments": []}, {"quantity_id":
    "q47", "topic": "Solution A nested stock addition", "source": {"evidence_id":
    "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739", "raw_path":
    "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[1].recipe[8]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\":
    \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }"}, "decision": "add", "rationale": "Source1ml ofSelenite-tungstate
    solution belongs insideSolution A; this receiving edge is missing from the flattened
    record. Existing reusable stock definitions can be linked after exact source and
    identifier reconciliation. StageA recipe liquid entries sum952.5ml while its declared
    stage volume/delivery is952ml; retain both source statements without silently
    repairing the source.", "layer_assessments": []}, {"quantity_id": "q48", "topic":
    "Solution A water input", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[1].recipe[10]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    950,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }"}, "decision": "add", "rationale": "Literal950ml water
    belongs toSolution A. It is a batch solvent input, not a mass, percent or measured
    final-volume denominator. Preserve the source-stage water amount with the preparation.",
    "layer_assessments": []}, {"quantity_id": "q49", "topic": "Solution B water input",
    "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[2].recipe[3]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }"}, "decision": "add", "rationale": "Literal10ml water
    belongs toSolution B. It is a batch solvent input, not a mass, percent or measured
    final-volume denominator. Preserve the source-stage water amount with the preparation.",
    "layer_assessments": []}, {"quantity_id": "q50", "topic": "Solution C nested stock
    addition", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[3].recipe[0]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\":
    \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }"}, "decision":
    "add", "rationale": "Source1ml ofWolin''s vitamin solution (10x) belongs insideSolution
    C; this receiving edge is missing from the flattened record. Existing reusable
    stock definitions can be linked after exact source and identifier reconciliation.",
    "layer_assessments": []}, {"quantity_id": "q51", "topic": "Solution D water input",
    "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[4].recipe[1]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }"}, "decision": "add", "rationale": "Literal10ml water
    belongs toSolution D. It is a batch solvent input, not a mass, percent or measured
    final-volume denominator. Preserve the source-stage water amount with the preparation.",
    "layer_assessments": []}, {"quantity_id": "q52", "topic": "Solution E water input",
    "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[5].recipe[1]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    20,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }"}, "decision": "add", "rationale": "Literal20ml water
    belongs toSolution E. It is a batch solvent input, not a mass, percent or measured
    final-volume denominator. Preserve the source-stage water amount with the preparation.",
    "layer_assessments": []}, {"quantity_id": "q53", "topic": "Solution F water input",
    "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[6].recipe[1]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }"}, "decision": "add", "rationale": "Literal10ml water
    belongs toSolution F. It is a batch solvent input, not a mass, percent or measured
    final-volume denominator. Preserve the source-stage water amount with the preparation.",
    "layer_assessments": []}, {"quantity_id": "q54", "topic": "StageB adjustment",
    "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[2].steps[0]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"step\": \"Adjust to pH 7.0 with 1 N NaOH.\"\n                    }"},
    "decision": "not_quantified", "rationale": "Source1NNaOH is a titrant strength,
    not a delivered amount. No amount is stated; preserve variable addition and stageB
    pH7.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "preparation_steps[2]", "stored_value": {"step_number": 3, "action":
    "MIX", "description": "Adjust to pH 7.0 with 1 N NaOH."}, "decision": "relocate",
    "rationale": "Existing pH7/1NNaOH instruction belongs to stageB, not a second
    unspecified whole-medium adjustment."}]}, {"quantity_id": "q55", "topic": "SL-10
    preparation and final make-up", "source": {"evidence_id": "api739", "reference":
    "https://mediadive.dsmz.de/rest/medium/739", "raw_path": "REVIEW_WORK/batch077/source09/api739.raw",
    "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[7].steps[0]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl,
    then dilute in water, add and dissolve the other salts. Finally make up to 1000.00
    ml.\"\n                    }"}, "decision": "not_quantified", "rationale": "Stock595
    already retains its preparation_notes and repaired variable water field. Move
    source context to the stock boundary while preserving its evidence; do not apply
    make-up to the receiving medium.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "preparation_steps[3]", "stored_value": {"step_number": 4, "action":
    "DISSOLVE", "description": "First dissolve FeCl2 in the HCl, then dilute in water,
    add and dissolve the other salts. Finally make up to 1000.00 ml."}, "decision":
    "relocate", "rationale": "Existing FeCl2/HCl dissolution and1000ml make-up instruction
    belongs only toSL-10."}]}, {"quantity_id": "q56", "topic": "Main A–F preparation
    and conditions", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"step\": \"Sparge solution A with 80% N2
    and 20% CO2 gas mixture for 30 - 45 min to make it anoxic and reach a pH of around
    6, then distribute under the same gas atmosphere into anoxic Hungate-type tubes
    and autoclave. Solutions B and C are prepared under 100% N2 gas atmosphere and
    sterilized by filtration. Solutions D and F are autoclaved separately under 100%
    N2 gas. Solution E is prepared under 80% N2 and 20% CO2 gas gas atmosphere. To
    complete the medium appropriate amounts of solutions B to F are added to the sterile
    solution A in the sequence as indicated. Final pH of the medium should be at 7.0.
    After combining solutions the medium should equilibrate overnight and a white
    precipitate should be apparent.\"\n                    }"}, "decision": "not_quantified",
    "rationale": "A uses80/20N2/CO2 for30–45minutes, near pH6 before autoclaving;
    B/C use100%N2 and filtration; D/F use100%N2 and autoclaving; E uses80/20N2/CO2.
    Add B–F in order; final mediumpH7 after overnight equilibration and white precipitate
    are source context. No unstated sterilization temperature/time is supplied.",
    "layer_assessments": [{"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "preparation_steps[0]", "stored_value": {"step_number": 1, "action":
    "AUTOCLAVE", "description": "Sparge solution A with 80% N2 and 20% CO2 gas mixture
    for 30 - 45 min to make it anoxic and reach a pH of around 6, then distribute
    under the same gas atmosphere into anoxic Hungate-type tubes and autoclave. Solutions
    B and C are prepared under 100% N2 gas atmosphere and sterilized by filtration.
    Solutions D and F are autoclaved separately under 100% N2 gas. Solution E is prepared
    under 80% N2 and 20% CO2 gas gas atmosphere. To complete the medium appropriate
    amounts of solutions B to F are added to the sterile solution A in the sequence
    as indicated. Final pH of the medium should be at 7.0. After combining solutions
    the medium should equilibrate overnight and a white precipitate should be apparent."},
    "decision": "evidence_only", "rationale": "Full original main preparation is already
    retained in this owner; preserve while clarifying stage boundaries. The unchanged
    text is source-supported, but this owner has no attached field-level claim; attach
    evidence without changing the instruction."}, {"path": "data/merge_yaml/merged/DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Generated target lacks retained DSMZ preparation; exactKOMODO route remains inaccessible.",
    "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "unsupported",
    "rationale": "Generated target lacks retained DSMZ preparation; exactKOMODO route
    remains inaccessible.", "missing": true}]}, {"quantity_id": "q57", "topic": "Optional
    reduction and inoculum", "source": {"evidence_id": "api739", "reference": "https://mediadive.dsmz.de/rest/medium/739",
    "raw_path": "REVIEW_WORK/batch077/source09/api739.raw", "raw_sha256": "8f03c7b6bf4056ca637d24c3eab243f6cdb3003ba33e80eed2201a612ef0cd0f",
    "locator": "$.data.solutions[0].steps[1]", "accessed_at": "2026-10-28T20:14:12.383714Z",
    "quote": "{\n                        \"step\": \"Note: Addition of 10 - 20 mg
    sodium dithionite per liter (e.g. from 5% (w/v) solution freshly prepared under
    N2 and filter-sterilized) just before inoculation may stimulate growth at the
    beginning. For transfers use 5 - 10% (v/v) inoculum.\"\n                    }"},
    "decision": "not_quantified", "rationale": "The source optionally adds10–20mg/L
    dithionite from a freshly prepared5%w/v solution made underN2 and filter sterilized;
    a hypothetical dose would be0.2–0.4ml/L from50mg/ml, conditional on that explicit
    strength. Source inoculum is5–10%v/v. These do not establish a mandatory formulation
    component, strain growth evidence or new stock identity.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml",
    "field_path": "preparation_steps[1]", "stored_value": {"step_number": 2, "action":
    "FILTER_STERILIZE", "description": "Note: Addition of 10 - 20 mg sodium dithionite
    per liter (e.g. from 5% (w/v) solution freshly prepared under N2 and filter-sterilized)
    just before inoculation may stimulate growth at the beginning. For transfers use
    5 - 10% (v/v) inoculum."}, "decision": "evidence_only", "rationale": "Retain source
    optional wording and inoculum guidance; these are already present in the maintainedDSMZ
    owner. The unchanged text is source-supported, but this owner has no attached
    field-level claim; attach evidence without changing the instruction."}]}]'
- assessment_id: a6
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: concern
  summary: All262recursive current ID/label slots and795exact packaged rows were read;38OLS
    scientific objects cover all36asserted accessions plus water and nickel-hexahydrate
    candidate. No current numeric legacyMIM assertions remain. The two sodium/hydrate
    contradictions are confirmed. Explicit calciumD-pantothenate31345, alum dodecahydrate86465
    and other stated hydrates are preserved. Primary disodium succinate does not independently
    establish anhydrous specificity from provider mmol_l; generic lipoic acid16494
    does not certify the DL mixture, so preserve literal source labels and uncertainty.
    Rejected aliases are separate from mapped identifier rows.
  target_ids:
  - CultureMech:006388
  evidence_ids:
  - grounding
  - full-catalog
- assessment_id: a7
  area: provenance
  topic: History and evidence scope
  outcome: concern
  summary: Complete current histories,26attached stock claims,22full reports, selected
    archive739context and238claims from six rows/five parent plans were assessed.163parent
    quote occurrences and47historical change quotes match current source bytes. AppliedSL-10
    nickel withdrawal andS777 event-time difference are explicitly separated from
    older previews. Current source byte equality does not authenticate historical
    access times or executions.
  target_ids:
  - CultureMech:006388
  evidence_ids:
  - history
  - scalars
  - parent-claims
  - attached-claims
  - reading-proof
  - historical-0
  - historical-1
  - historical-2
  - historical-3
  - historical-4
  - historical-5
  - historical-6
  - historical-7
  - historical-8
  - historical-9
  - historical-10
  - historical-11
  - historical-12
  - historical-13
  - historical-14
  - historical-15
  - historical-16
  - historical-17
  - historical-18
  - historical-19
  - historical-20
  - historical-21
  - historical-22
- assessment_id: a8
  area: scope
  topic: Growth and taxonomic evidence
  outcome: unknown
  summary: Generic cultivation applications and bacterial filing are not strain-level
    growth evidence. No organism-specific growth, temperature or atmosphere is inferred
    from names or source catalog identifiers.
  target_ids:
  - CultureMech:006388
  evidence_ids:
  - local-target
- assessment_id: a9
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:006388
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: a10
  area: evidence
  topic: High-metal classification remains unverified
  outcome: unknown
  summary: 'All three medium layers assert high_metal: true. The inspected DSMZ739
    primary recipe and API do not explicitly classify the medium as high-metal or
    state a criterion for that flag. Trace-metal salts alone do not establish this
    classification. Retain this as unresolved metadata pending an explicit source
    or documented classification rule; absence of source support does not establish
    high_metal: false.'
  target_ids:
  - CultureMech:006388
  evidence_ids:
  - local-target
  - owner-1
  - owner-2
  - dsm739
  - api739
findings:
- finding_id: f1
  issue_key: culturemech-006388-preparation-stage-concentrations-are-flattened-into-the-whole-medium
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Preparation-stage concentrations are flattened into the whole medium
  description: All36root ingredient rates in the generated target and both contributors
    come from distinct A/B/D/E/F stages or reusable stocks. DSMZ739 assembles A–F
    and nests595/777 inA and5980 inC. Restore these boundaries and literal batch doses;
    numerical agreement with a stage g_l does not validate a whole-medium rate. Preserve
    all current reusable-stock repairs and do not infer measured final volume from
    the nominal1003ml sum.
  target_ids:
  - CultureMech:006388
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - api739
  - dsm739
  - stock-595
  - stock-777
  - stock-5980
  - quantities
  - writer-0
  rule_id: P2-stage-concentration-scope
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-006388-liquid-doses-lack-supported-mass-conversions
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Liquid doses lack supported mass conversions
  description: Root isobutyric acid0.19G_PER_L conflicts with the literal0.19ml input
    inB, and HCl2.5G_PER_L lacks both the25%basis/density and receiving-stage scope.
    Preserve explicit volumes and stock strengths. The standaloneSL-10 HCl0.01L repair
    is correct and should be reused, not reopened.
  target_ids:
  - CultureMech:006388
  field_paths:
  - ingredients[10].concentration
  - ingredients[14].concentration
  evidence_ids:
  - api739
  - dsm739
  - solution595
  - quantities
  rule_id: P2-liquid-unit-and-percent-basis
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-006388-generated-preparation-is-missing-and-stock-steps-lack-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated preparation is missing and stock steps lack scope
  description: The DSMZ contributor retains the complete mainA–F preparation and optional
    reduction/inoculum note. Target/KOMODO have no preparation_steps. Its third entry
    is B pH7 adjustment with 1N NaOH, labeled MIX; its fourth is SL-10 dissolution/make-up,
    labeled DISSOLVE. Both are unscoped root preparation steps. Preserve the first
    two source texts, move stock instructions to their proper boundary, and carry
    supported preparation through regeneration.
  target_ids:
  - CultureMech:006388
  field_paths:
  - preparation_steps
  - data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml::preparation_steps[2]
  - data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml::preparation_steps[3]
  evidence_ids:
  - dsm739
  - api739
  - owner-2
  - writer-0
  - stock-595
  rule_id: P2-preparation-scope
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f4
  issue_key: culturemech-006388-explicit-sodium-and-hydrate-forms-are-not-preserved-by-two-identifiers
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Explicit sodium and hydrate forms are not preserved by two identifiers
  description: Sodium resazurin carries neutral resazurinCHEBI8806, and NiCl2x6H2O
    carries anhydrous nickel dichlorideCHEBI34887 in all three medium layers. CurrentOLS53542
    supports nickel chloride hexahydrate as a candidate; MIM has both a mapped preferred-name
    row and a separately rejected source-spelling alias. CurrentSL-10 already withdrewCHEBI34887,
    retaining upstream compound40 and the hexahydrate label. Preserve this repair
    and resolve exact replacements using the current catalog; do not reinstate a rejected
    alias or infer mass equivalents.
  target_ids:
  - CultureMech:006388
  field_paths:
  - ingredients[7].term
  - ingredients[21].term
  - ingredients[21].mediaingredientmech_chebi_term
  evidence_ids:
  - ols8806
  - ols34887
  - ols53542
  - full-catalog
  - api739
  - stock-595
  rule_id: P2-salt-hydrate-grounding
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f5
  issue_key: culturemech-006388-medium-claims-lack-direct-evidence-and-retain-malformed-imported-times
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Medium claims lack direct evidence and retain malformed imported times
  description: All26attached current claims belong to reusable stocks; the three medium
    layers lack field-level formulation evidence. Attach the verifiedDSMZ claims with
    exact stage scope while keeping KOMODO equivalence unresolved. Literal.fZ and
    timezone-less imported history values need bounded follow-up; preserve original
    append-only events and do not invent replacement times from current writer behavior.
  target_ids:
  - CultureMech:006388
  field_paths:
  - ingredients
  - references
  - curation_history
  evidence_ids:
  - history
  - scalars
  - attached-claims
  - owner-1
  - owner-2
  - writer-1
  rule_id: P3-evidence-and-time-provenance
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: All36root ingredient rates in the generated target and both contributors
    come from distinct A/B/D/E/F stages or reusable stocks. DSMZ739 assembles A–F
    and nests595/777 inA and5980 inC. Restore these boundaries and literal batch doses;
    numerical agreement with a stage g_l does not validate a whole-medium rate. Preserve
    all current reusable-stock repairs and do not infer measured final volume from
    the nominal1003ml sum.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006388
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Root isobutyric acid0.19G_PER_L conflicts with the literal0.19ml input
    inB, and HCl2.5G_PER_L lacks both the25%basis/density and receiving-stage scope.
    Preserve explicit volumes and stock strengths. The standaloneSL-10 HCl0.01L repair
    is correct and should be reused, not reopened.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006388
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: The DSMZ contributor retains the complete mainA–F preparation and optional
    reduction/inoculum note. Target/KOMODO have no preparation_steps. Its third entry
    is B pH7 adjustment with 1N NaOH, labeled MIX; its fourth is SL-10 dissolution/make-up,
    labeled DISSOLVE. Both are unscoped root preparation steps. Preserve the first
    two source texts, move stock instructions to their proper boundary, and carry
    supported preparation through regeneration.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006388
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action4
  description: Sodium resazurin carries neutral resazurinCHEBI8806, and NiCl2x6H2O
    carries anhydrous nickel dichlorideCHEBI34887 in all three medium layers. CurrentOLS53542
    supports nickel chloride hexahydrate as a candidate; MIM has both a mapped preferred-name
    row and a separately rejected source-spelling alias. CurrentSL-10 already withdrewCHEBI34887,
    retaining upstream compound40 and the hexahydrate label. Preserve this repair
    and resolve exact replacements using the current catalog; do not reinstate a rejected
    alias or infer mass equivalents.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006388
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action5
  description: All26attached current claims belong to reusable stocks; the three medium
    layers lack field-level formulation evidence. Attach the verifiedDSMZ claims with
    exact stage scope while keeping KOMODO equivalence unresolved. Literal.fZ and
    timezone-less imported history values need bounded follow-up; preserve original
    append-only events and do not invent replacement times from current writer behavior.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:006388
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- Completion is partial because current exactKOMODO739 andMediaList requests return403.
  Local target and owners are resolved; copiedDSMZ ingredients do not authenticate
  live cross-source identity.
- Only reusable stocks595/777/5980 are assessed dependencies. Other normalized stage
  records, receiving media and unrelated parent-plan/archive rows are outside scope.
  API161 is restricted to identity/inventory and stock5980 evidence.
- The source gives stage doses and provider volumes, includingA952ml despite952.5ml
  summed liquid entries; no independently measured final-medium volume is established.
  No density, unknown percentage basis, mmol_l conversion or silent source correction
  is inferred.
- No strain-specific growth or taxonomic curation is performed. Generic applications
  and source names do not prove growth. iModulonDB is inapplicable to this formulation
  review.
- Four original canonical target diagnostics passed once; the reference validator
  performed zero checks. No dedicated focused embedded-history validator is documented;
  standalone history checks are a different scope. No corpus-wide gate or historical
  execution replay is claimed.
- Exact-byte reading reuse is explicitly documented; all new scientific values were
  directly read. No recipe, generated product or prior review was edited.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- This draft authoring step performed no formal review validation/save, Git mutation
  or publication.
```
