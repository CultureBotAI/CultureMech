# Scientific review: CLOSTRIDIUM ACETOBUTYLICUM medium

- Review: 20261028T095814Z-culturemech-005233-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T09:30:21.677411Z
- Finished UTC: 2026-10-28T09:58:14.510810Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM411 main and milk formulations are collapsed in the generated target and maintained ingredient lists; pH and indicator stages must be separated. The review credits the DSM preparation text and current cleanup/merge safeguards, documents the sodium-resazurin form mismatch and malformed history, and inventories every amount with explicit source-basis limits.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch062 index 08
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:005233 | data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml | generated | clostridium_acetobutylicum_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:005233 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:005233 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:005233 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:005233 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### DSM411 correspondence and unresolved KOMODO branch

identity: concern. Targets: CultureMech:005233.

The source mapping and exact maintained IDs establish DSM411 correspondence, but historical KOMODO pH 7.1 and the collapsed main/milk formulation require explicit variant accounting. Exact historical MediaInfo411 and current MediaList requests returned 403; those failures do not erase the preserved historical mapping row.

### Complex liquid formulation and organism scope

scope: supported. Targets: CultureMech:005233.

Fresh potatoes/milk make the formulations chemically undefined. The source names no specific strain and does not establish a strain-growth association; no organism or incubation claim is inferred from the medium title.

### Native structural checks

schema: supported. Targets: CultureMech:005233.

All four canonical checks passed once, including zero strict errors and zero reference checks; this does not authenticate recipe identity or stages.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:005233.

18 current concentration fields are covered by 14 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b062-quantity-inventory-v1","target":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","quantity_field_count":18,"decisions":[{"quantity_id":"q1","label":"Potato","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"200","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"200","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"200","unit":"G_PER_L"}}],"decision":"mixed","rationale":"DSM411 explicitly reports the main-formulation g_l=200 and the PDF prints 200 g as a batch input. This supports the DSM owner's nominal recipe basis without attached evidence, not a measured final concentration. The target/KOMODO layer also carries milk-medium pH 7.1 and a collapsed formulation, so its whole-formulation basis remains unresolved. Potato is fresh, washed, peeled and sliced input subsequently filtered; 200 g is not a measured mass of final infusion solids.","source_stage":"DSM411 main formulation; unresolved merged/KOMODO variant","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Potato\",\n                        \"compound_id\": 1606,\n                        \"condition\": \"\",\n                        \"attribute\": \"fresh, washed, peeled and sliced\",\n                        \"amount\": 200,\n                        \"unit\": \"g\",\n                        \"g_l\": 200,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt lines 3-3","quote":"Potato (fresh, washed, peeled and sliced)              200.00         g","quote_basis":"derivative text"}],"layer_decisions":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"Local nominal mass agrees, but current mixed-formulation/pH identity is not authenticated as one recipe."},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"Local nominal mass agrees, but current mixed-formulation/pH identity is not authenticated as one recipe."},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"Explicit provider main-recipe rate, no attached evidence."}]},{"quantity_id":"q2","label":"CaCO3","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"mixed","rationale":"DSM411 explicitly reports the main-formulation g_l=2 and the PDF prints 2 g as a batch input. This supports the DSM owner's nominal recipe basis without attached evidence, not a measured final concentration. The target/KOMODO layer also carries milk-medium pH 7.1 and a collapsed formulation, so its whole-formulation basis remains unresolved.","source_stage":"DSM411 main formulation; unresolved merged/KOMODO variant","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"CaCO3\",\n                        \"compound_id\": 13,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 19.982,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt lines 4-4","quote":"CaCO3                                                    2.00         g","quote_basis":"derivative text"}],"layer_decisions":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"Local nominal mass agrees, but current mixed-formulation/pH identity is not authenticated as one recipe."},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"Local nominal mass agrees, but current mixed-formulation/pH identity is not authenticated as one recipe."},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"Explicit provider main-recipe rate, no attached evidence."}]},{"quantity_id":"q3","label":"D-Glucose","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"6","unit":"G_PER_L"}}],"decision":"mixed","rationale":"DSM411 explicitly reports the main-formulation g_l=6 and the PDF prints 6 g as a batch input. This supports the DSM owner's nominal recipe basis without attached evidence, not a measured final concentration. The target/KOMODO layer also carries milk-medium pH 7.1 and a collapsed formulation, so its whole-formulation basis remains unresolved.","source_stage":"DSM411 main formulation; unresolved merged/KOMODO variant","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\": 211,\n                        \"amount\": 6,\n                        \"unit\": \"g\",\n                        \"g_l\": 6,\n                        \"mmol_l\": 33.3037,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt lines 6-6","quote":"D-Glucose                                                6.00         g","quote_basis":"derivative text"}],"layer_decisions":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"Local nominal mass agrees, but current mixed-formulation/pH identity is not authenticated as one recipe."},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"Local nominal mass agrees, but current mixed-formulation/pH identity is not authenticated as one recipe."},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"Explicit provider main-recipe rate, no attached evidence."}]},{"quantity_id":"q4","label":"L-Cysteine HCl x H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"mixed","rationale":"DSM411 explicitly reports the main-formulation g_l=0.5 and the PDF prints 0.5 g as a batch input. This supports the DSM owner's nominal recipe basis without attached evidence, not a measured final concentration. The target/KOMODO layer also carries milk-medium pH 7.1 and a collapsed formulation, so its whole-formulation basis remains unresolved.","source_stage":"DSM411 main formulation; unresolved merged/KOMODO variant","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.8468,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt lines 7-7","quote":"L-Cysteine HCl x H2O                                     0.50         g","quote_basis":"derivative text"}],"layer_decisions":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"Local nominal mass agrees, but current mixed-formulation/pH identity is not authenticated as one recipe."},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"Local nominal mass agrees, but current mixed-formulation/pH identity is not authenticated as one recipe."},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"Explicit provider main-recipe rate, no attached evidence."}]},{"quantity_id":"q5","label":"Collapsed sodium resazurin","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.0006000000000000001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.0006000000000000001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.0006000000000000001","unit":"G_PER_L"}}],"decision":"correct","rationale":"The 0.0006000000000000001 G_PER_L note explicitly sums 0.0005 and 0.0001 from two distinct formulations. The primary has separate 0.50 ml and 0.10 ml aliquots of 0.1% w/v stock. These are not duplicate additions to one medium, and the provider milk g_l=0.0001 is not a self-consistent final rate for its declared 100 ml recipe. Preserve the aliquots and strength by formulation; do not resolve this by summing or treating the provider number as final-volume proof.","source_stage":"Two independent source formulations","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.1,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0001,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt lines 5-5","quote":"Sodium resazurin (0.1% w/v)                              0.50        ml","quote_basis":"derivative text"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt lines 20-24","quote":"Milk Medium\n   Milk (fresh)                                           100.00        ml\n   Sodium resazurin (0.1% w/v)                              0.10        ml\n\nAdjust pH to 7.1. Tube and autoclave under 100% N2 gas atmosphere for 12 min at 121°C.","quote_basis":"derivative text"}]},{"quantity_id":"q6","label":"Milk volume represented as mass","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source specifies 100 ml fresh milk in the separate Milk Medium, not 100 g/L in the potato formulation. Density is unestablished. Preserve the volume input and independent recipe identity; no mass conversion is justified.","source_stage":"Milk-medium input volume","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Milk\",\n                        \"compound_id\": 467,\n                        \"attribute\": \"fresh\",\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt lines 20-24","quote":"Milk Medium\n   Milk (fresh)                                           100.00        ml\n   Sodium resazurin (0.1% w/v)                              0.10        ml\n\nAdjust pH to 7.1. Tube and autoclave under 100% N2 gas atmosphere for 12 min at 121°C.","quote_basis":"derivative text"}]},{"quantity_id":"q7","label":"Root pH assertions","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ph_value","stored":7.1},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ph_value","stored":7.1},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ph_value","stored":6.8}],"decision":"mixed","rationale":"The primary main formulation ends at pH 6.8, correctly retained by the DSM owner. Target/KOMODO root pH 7.1 belongs to the separate milk formulation. A catalog mapping to DSM411 does not authenticate that mixed formulation; assign pH only within the corresponding recipe branch.","source_stage":"Recipe-specific pH","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Mix potatoes and CaCO3 then autoclave 30 min at 121\\u00b0C. Filter through cheese cloth, add glucose and cysteine, distribute under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave at 121\\u00b0C for 20 min. Adjust pH of complete medium to 6.8.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\": \"Adjust pH to 7.1. Tube and autoclave under 100% N2 gas atmosphere for 12 min at 121\\u00b0C.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt lines 10-15","quote":"1. Mix potatoes and CaCO3 then autoclave 30 min at 121°C. Filter through cheese cloth,\nadd glucose and cysteine, distribute under 100% N2 gas atmosphere into anoxic\nHungate-type tubes or serum vials and autoclave at 121°C for 20 min. Adjust pH of\ncomplete medium to 6.8.\n2. Note: For the reactivation of freeze-dried strains it is recommended to use the following\nsimple milk medium:","quote_basis":"derivative text"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt lines 24-24","quote":"Adjust pH to 7.1. Tube and autoclave under 100% N2 gas atmosphere for 12 min at 121°C.","quote_basis":"derivative text"}],"layer_decisions":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ph_value","decision":"correct","rationale":"7.1 belongs to milk formulation, not main potato medium."},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ph_value","decision":"correct","rationale":"7.1 belongs to milk formulation, not main potato medium."},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"Primary main-recipe pH supported without attached evidence."}]},{"quantity_id":"q8","label":"Existing DSM preparation 1","local_fields":[{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"preparation_steps[0].description","stored":"Mix potatoes and CaCO3 then autoclave 30 min at 121°C. Filter through cheese cloth, add glucose and cysteine, distribute under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave at 121°C for 20 min. Adjust pH of complete medium to 6.8."}],"decision":"evidence_only","rationale":"The DSM owner preserves this exact preparation context, including stage-specific temperature/time/gas/pH where printed. Credit it; separate main versus milk sequence rather than applying all steps to one combined recipe.","source_stage":"Main potato sequence","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Mix potatoes and CaCO3 then autoclave 30 min at 121\\u00b0C. Filter through cheese cloth, add glucose and cysteine, distribute under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave at 121\\u00b0C for 20 min. Adjust pH of complete medium to 6.8.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt lines 10-15","quote":"1. Mix potatoes and CaCO3 then autoclave 30 min at 121°C. Filter through cheese cloth,\nadd glucose and cysteine, distribute under 100% N2 gas atmosphere into anoxic\nHungate-type tubes or serum vials and autoclave at 121°C for 20 min. Adjust pH of\ncomplete medium to 6.8.\n2. Note: For the reactivation of freeze-dried strains it is recommended to use the following\nsimple milk medium:","quote_basis":"derivative text"}]},{"quantity_id":"q9","label":"Existing DSM preparation 2","local_fields":[{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"preparation_steps[1].description","stored":"Note: For the reactivation of freeze-dried strains it is recommended to use the following simple milk medium:"},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"preparation_steps[1].action","stored":"STORE"}],"decision":"mixed","rationale":"The DSM owner preserves this exact preparation context, including stage-specific temperature/time/gas/pH where printed. Credit it; separate main versus milk sequence rather than applying all steps to one combined recipe. The retained description concerns reactivating freeze-dried strains; its STORE action is a classification mismatch, not a storage instruction. Preserve the description and correct only that action after choosing the appropriate source-faithful representation.","source_stage":"Main potato sequence","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\": \"Note: For the reactivation of freeze-dried strains it is recommended to use the following simple milk medium:\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt lines 10-15","quote":"1. Mix potatoes and CaCO3 then autoclave 30 min at 121°C. Filter through cheese cloth,\nadd glucose and cysteine, distribute under 100% N2 gas atmosphere into anoxic\nHungate-type tubes or serum vials and autoclave at 121°C for 20 min. Adjust pH of\ncomplete medium to 6.8.\n2. Note: For the reactivation of freeze-dried strains it is recommended to use the following\nsimple milk medium:","quote_basis":"derivative text"}],"layer_decisions":[{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"preparation_steps[1].description","decision":"evidence_only","rationale":"Exact source description retained."},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"preparation_steps[1].action","decision":"correct","rationale":"Reactivation context is not storage; current classifier matches the word freeze to STORE."}]},{"quantity_id":"q10","label":"Existing DSM preparation 3","local_fields":[{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"preparation_steps[2].description","stored":"Adjust pH to 7.1. Tube and autoclave under 100% N2 gas atmosphere for 12 min at 121°C."}],"decision":"evidence_only","rationale":"The DSM owner preserves this exact preparation context, including stage-specific temperature/time/gas/pH where printed. Credit it; separate main versus milk sequence rather than applying all steps to one combined recipe.","source_stage":"Milk sequence","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\": \"Adjust pH to 7.1. Tube and autoclave under 100% N2 gas atmosphere for 12 min at 121\\u00b0C.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt lines 24-24","quote":"Adjust pH to 7.1. Tube and autoclave under 100% N2 gas atmosphere for 12 min at 121°C.","quote_basis":"derivative text"}]},{"quantity_id":"q11","label":"Main water input","local_fields":[],"decision":"evidence_only","rationale":"1000 ml water is the main recipe input; it is not a measured final volume after extraction and additions.","source_stage":"Main water","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt lines 8-8","quote":"Distilled water                                       1000.00        ml","quote_basis":"derivative text"}]},{"quantity_id":"q12","label":"Main resazurin stock dose/strength","local_fields":[],"decision":"evidence_only","rationale":"0.50 ml of explicitly 0.1% w/v stock belongs to the main recipe. Preserve stock composition separately from receiving volume.","source_stage":"Main indicator stock","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt lines 5-5","quote":"Sodium resazurin (0.1% w/v)                              0.50        ml","quote_basis":"derivative text"}]},{"quantity_id":"q13","label":"Milk resazurin stock dose/strength","local_fields":[],"decision":"evidence_only","rationale":"0.10 ml of explicitly 0.1% w/v stock belongs to Milk Medium. The provider reports g_l=0.0001 alongside volume=100; retain that normalization inconsistency, without converting to an assumed final concentration.","source_stage":"Milk indicator stock","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.1,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0001,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt lines 20-24","quote":"Milk Medium\n   Milk (fresh)                                           100.00        ml\n   Sodium resazurin (0.1% w/v)                              0.10        ml\n\nAdjust pH to 7.1. Tube and autoclave under 100% N2 gas atmosphere for 12 min at 121°C.","quote_basis":"derivative text"}]},{"quantity_id":"q14","label":"Provider declared recipe volumes","local_fields":[],"decision":"evidence_only","rationale":"The provider declares main volume 1000 ml and milk volume 100 ml. These metadata are recorded, not relabelled as measured final volumes; primary water/milk inputs and added indicator volumes remain separate.","source_stage":"Provider normalization metadata","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"$.data.solutions[0].volume","quote":"\"volume\": 1000","quote_basis":"raw UTF-8"},{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"$.data.solutions[1].volume","quote":"\"volume\": 100,","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml":null,"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:005233.

All asserted CHEBI IDs and labels resolve, but Sodium resazurin has the neutral CHEBI:8806 formula. D-glucose, calcium carbonate and L-cysteine hydrochloride monohydrate otherwise correspond to the named forms. Secondary-link presence is three of six ingredient nodes per layer; validity among asserted links is separately checked against the current packaged CSV. Potato and fresh milk are complex ingredients, not forced into invented pure-chemical IDs.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:005233.

October5 reports explicitly did no source verification; October7 reports retained all six values unchanged because stock/formulation and pH conditions were unresolved. Their exact source rows match the fresh API content where recorded. Current cleanup avoids duplicate summation and current merger requires formulation equality; the historical collapsed target is not proof those current safeguards failed. The extant malformed import timestamp remains a confirmed provenance concern.

## Findings

### f1: Potato and milk formulations have been combined

major / open / confirmed; issue key: culturemech-005233-formulation-collapse.

Separate the main DSM411 potato formulation from its explicitly distinct Milk Medium. The current list assigns milk volume to G_PER_L and sums the two indicator entries as if they were additions to one recipe. Restore source-specific ingredient/stock boundaries and preserve the source volume units and unmeasured final-volume limitation. Current cleanup no longer sums disagreeing duplicates; current MediaDive parsing reads the first recipe only, while its preparation parser still pools steps from every solution, so preserve that remaining branch-specific context when regenerating.

### f2: Main and milk-medium pH are not interchangeable

major / open / confirmed; issue key: culturemech-005233-ph-variant.

Resolve target/KOMODO pH 7.1 against the exact formulation identity. The primary assigns 6.8 to the main potato formulation and 7.1 to the separate milk medium; the DSM owner already correctly has main pH 6.8. Preserve that repaired/current distinction and do not copy a source composition while retaining a conflicting root pH.

### f3: Sodium resazurin is grounded as the neutral molecule

major / open / confirmed; issue key: culturemech-005233-resazurin-salt.

The target and both owners assert Sodium resazurin but their primary term is CHEBI:8806, whose fresh OLS formula C12H7NO4 contains no sodium. Reconcile the supplied sodium salt; do not mistake current canonical-label agreement for supplied-form correctness. These nodes have no secondary MIM slot, so no nonexistent secondary field is cited.

### f4: Generated preparation loses the maintained source sequences

minor / open / confirmed; issue key: culturemech-005233-generated-preparation-loss.

The DSM owner retains all three source preparation entries, including the main extraction/sterilization sequence and separate milk instructions; the generated target and KOMODO owner do not. Preserve the correct source-specific process and ingredient grade (fresh prepared potato, fresh milk), without promoting the historical Aerobic: Yes flag into a growth or preparation assertion. Current conservative merging rejects incompatible notes, pH and preparation rather than legitimizing the stale collapsed target. The DSM owner preparation_steps[1] description concerns reactivating freeze-dried strains, but its action STORE is not source-faithful. Preserve that description and correct the action classification. Current _classify_preparation_action maps the substring freeze to STORE; this demonstrates current behavior, not historical execution.

### f5: Import timestamps need an append-only provenance correction

minor / open / confirmed; issue key: culturemech-005233-history-timestamp.

The KOMODO owner and generated history retain 2026-01-27T01:15:02.fZ, and the resolver event is timezone-naive. Current komodo_web_importer uses time.strftime with %f, so the formatting defect is demonstrable in present code. Preserve the old history bytes and append an actual explanatory correction; do not invent the original fraction or timezone. Correct future writer serialization without claiming historical code execution from the current body.

## Recommended Actions And Acceptance Checks

### a1

Separate the main DSM411 potato formulation from its explicitly distinct Milk Medium. The current list assigns milk volume to G_PER_L and sums the two indicator entries as if they were additions to one recipe. Restore source-specific ingredient/stock boundaries and preserve the source volume units and unmeasured final-volume limitation. Current cleanup no longer sums disagreeing duplicates; current MediaDive parsing reads the first recipe only, while its preparation parser still pools steps from every solution, so preserve that remaining branch-specific context when regenerating.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Resolve target/KOMODO pH 7.1 against the exact formulation identity. The primary assigns 6.8 to the main potato formulation and 7.1 to the separate milk medium; the DSM owner already correctly has main pH 6.8. Preserve that repaired/current distinction and do not copy a source composition while retaining a conflicting root pH.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The target and both owners assert Sodium resazurin but their primary term is CHEBI:8806, whose fresh OLS formula C12H7NO4 contains no sodium. Reconcile the supplied sodium salt; do not mistake current canonical-label agreement for supplied-form correctness. These nodes have no secondary MIM slot, so no nonexistent secondary field is cited.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

The DSM owner retains all three source preparation entries, including the main extraction/sterilization sequence and separate milk instructions; the generated target and KOMODO owner do not. Preserve the correct source-specific process and ingredient grade (fresh prepared potato, fresh milk), without promoting the historical Aerobic: Yes flag into a growth or preparation assertion. Current conservative merging rejects incompatible notes, pH and preparation rather than legitimizing the stale collapsed target. The DSM owner preparation_steps[1] description concerns reactivating freeze-dried strains, but its action STORE is not source-faithful. Preserve that description and correct the action classification. Current _classify_preparation_action maps the substring freeze to STORE; this demonstrates current behavior, not historical execution.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

The KOMODO owner and generated history retain 2026-01-27T01:15:02.fZ, and the resolver event is timezone-naive. Current komodo_web_importer uses time.strftime with %f, so the formatting defect is demonstrable in present code. Preserve the old history bytes and append an actual explanatory correction; do not invent the original fraction or timezone. Correct future writer serialization without claiming historical code execution from the current body.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsm411 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf; REVIEW_WORK/batch062/source07-09/dsm411.json; exact original raw/text/hash/time metadata | context_only | Exact selected source identity and complete source stages; inspect organism context before operational assessment. KOMODO catalog is identity only. |
| api411 | https://mediadive.dsmz.de/rest/medium/411; REVIEW_WORK/batch062/source07-09/api411.json; exact original raw/text/hash/time metadata | context_only | Exact selected source identity and complete source stages; inspect organism context before operational assessment. KOMODO catalog is identity only. |
| komodoList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; REVIEW_WORK/batch062/source07-09/komodoList.json; exact original raw/text/hash/time metadata | context_only | Exact selected source identity and complete source stages; inspect organism context before operational assessment. KOMODO catalog is identity only. |
| komodo411 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=411; REVIEW_WORK/batch062/source07-09/komodo411.json; exact original raw/text/hash/time metadata | context_only | Exact historical KOMODO MediaInfo411 route requested once; HTTP403 retained. Failed access does not authenticate the page or any unrelated stock subsection. |
| target | data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| owner-2 | data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| report-18 | reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/inspected-candidate-context.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-19 | reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-20 | reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-22 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/clostridium_acetobutylicum_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch062/record08/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch062/record08/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch062/record08/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _parse_api_solutions, _normalize_unit, _parse_preparation_steps, _classify_preparation_action | context_only | Current _parse_api_composition reads the primary solution only; _is_api_stock_addition recognizes solution_id or percent-labelled ml rows. Molar-only stock attributes are outside that predicate; preparation steps are pooled across solutions. Current code is not proof of historical execution. Current _classify_preparation_action uses substring freeze to choose STORE, so the exact reactivation note requires action-code review. |
| writer-cleanup | scripts/cleanup_media_quality.py; merge_duplicate_ingredients and _merge_ingredient_group | context_only | Current _merge_ingredient_group no longer sums disagreeing duplicate concentrations; keeps first and flags conflicts. Historical summed notes remain separate evidence. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| writer-resolver | src/culturemech/enrich/dsmz_resolver.py; merge_composition and _add_enrichment_metadata | context_only | Current merge_composition copies source ingredients and solutions but only fills missing target pH; it does not establish equivalence of a pre-existing KOMODO pH with the DSM formulation. _add_enrichment_metadata uses a naive current datetime. |
| writer-komodo | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech history timestamp | context_only | Current web importer writes its timestamp using time.strftime with unsupported %f; the literal .fZ history must be preserved as historical provenance with an appended correction, not backdated or erased. |
| chebi3311 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:3311; REVIEW_WORK/batch062/source07-09/chebi3311.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; REVIEW_WORK/batch062/source07-09/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17634; REVIEW_WORK/batch062/source07-09/chebi17634.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91248; REVIEW_WORK/batch062/source07-09/chebi91248.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| quantities | REVIEW_WORK/batch062/record08/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch062/record08/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch062/record08/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch062/record08/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch062/record08/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch062/record08/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch062/record08/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch062/record08/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch062/record08/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch062/record08/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch062/record08/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- This scientific review is partial because the exact current KOMODO branch remains unavailable. The preserved historical mapping and current DSM411 evidence support the bounded findings, but do not resolve whether the KOMODO branch represents the main or milk formulation.
- The Milk Medium provider g_l for resazurin is preserved as conflicting normalization metadata, not used to compute a final concentration. No milk density or extracted potato-solids yield is assumed.
- Both exact KOMODO routes are currently unavailable (403). Historical catalog correspondence is derivative evidence and is not a new authenticated catalog capture.
- DSM411 PDF is one page; both main and Milk Medium sections were visually checked against the extracted text. Unknown individual authors/publication year are not filled from the copyright year.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T095814Z-culturemech-005233-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: CLOSTRIDIUM ACETOBUTYLICUM medium'
started_at: '2026-10-28T09:30:21.677411Z'
finished_at: '2026-10-28T09:58:14.510810Z'
reviewer:
  identity: Codex tsb_source_check
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Read-only independent review of maintained source records, fresh
    sources and original diagnostics.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: true
summary: DSM411 main and milk formulations are collapsed in the generated target and
  maintained ingredient lists; pH and indicator stages must be separated. The review
  credits the DSM preparation text and current cleanup/merge safeguards, documents
  the sodium-resazurin form mismatch and malformed history, and inventories every
  amount with explicit source-basis limits.
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
  - path: conf/oak_config.yaml
    sha256: c0ef0808662f57dc2f57ce9b405485830503653aceee1451c9e1dae42f9e7021
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/culturemech_id_registry.tsv
    sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
    role: context
  - path: data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml
    sha256: 884ed98f0166e1e43ad747e60fb62520f5e60e528d357bd0074b61440884be91
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml
    sha256: e322d3cdf8fd10aee848006830523a4b198d25a6e4454267e62b47002933ff89
    role: context
  - path: data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml
    sha256: f3376b4bdf60b96bb202254f656d7b39df947369e777dec9ea63bff30e8a1d87
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/inspected-candidate-context.json
    sha256: bea184ce1f011e5714cef082c0341aaf001d16024ef7935d004cbc8899f74fd5
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json
    sha256: 5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml.md
    sha256: b8a13b6223d99ffe3db1e5c1392f1d3f5d3ada148d166ad8b4b3a36bee203a32
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
    sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/clostridium_acetobutylicum_medium.yaml.md
    sha256: f9c7a62fa40ca03fe5316f0267faf9979429cfe2d0a1c2345a8e6621f6ffcb38
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.md
    sha256: b38b8da71a36eb5d51f9527b5feb3750e9bef68762a69057e613a2f5cf5111b2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.md
    sha256: 627d0a44c05f722a4ae8bf247e0ea2fe5193f2792b06a8dc3dff74513403adef
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.md
    sha256: 99bc46175b8e10e18034536d3127b6b300c5174a9bdf4a1e35ea6935ace97958
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_cocktail_nesting.py
    sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
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
  - path: scripts/import_from_culturebotht.py
    sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
    role: context
  - path: scripts/migrate_ph_range.py
    sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
    role: context
  - path: scripts/promote_komodo_volume_candidates.py
    sha256: 2423b7e2e04011b31d21eac939714a2db4380f033a69094325dc567e44929cd2
    role: context
  - path: scripts/refill_term_labels.py
    sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
    role: context
  - path: scripts/remove_invalid_chebi_ids.py
    sha256: a6c2f7577812081230fd5fe008182c09eace4ef7818857f8026ec8d5e0b760e0
    role: context
  - path: scripts/repair_dsmz489_stocks.py
    sha256: 0e86a9b273b82de1adf556a1d300f215da3ea64b84fc7eaadc10f77ea79d190e
    role: context
  - path: scripts/repair_mediadive_jcm_structure.py
    sha256: 5bff4c2d1900051bdea1b8e0f655049147c85cc9c61da4c348a6d60a8d0fd509
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
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
  description: Whole exact target/owner with explicit scoped dependencies, current
    sources and historical claims.
  selection: Authoritative batch062 index 08
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:005233
targets:
- target_id: CultureMech:005233
  path: data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml
  label: clostridium_acetobutylicum_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml
    role: maintained source
  ownership_note: Exact declared maintained contributors resolved against stable identity;
    stocks and other source variants remain scoped comparisons.
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:005233
  command: just validate-schema data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-schema
- check_id: strict
  name: Canonical strict
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:005233
  command: just validate-strict data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml
    --out REVIEW_WORK/batch062/record08/strict.tsv --workers 1 --quiet
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-strict
- check_id: terms
  name: Canonical terms
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:005233
  command: just validate-terms data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-terms
- check_id: references
  name: Canonical references
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:005233
  command: just validate-references data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsm411
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf
  accessed_at: '2026-10-28T09:30:19.840962Z'
  locator: REVIEW_WORK/batch062/source07-09/dsm411.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact selected source identity and complete source stages; inspect organism
    context before operational assessment. KOMODO catalog is identity only.
  snapshot_sha256: 44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2
- evidence_id: api411
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/411
  accessed_at: '2026-10-28T09:30:20.201602Z'
  locator: REVIEW_WORK/batch062/source07-09/api411.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact selected source identity and complete source stages; inspect organism
    context before operational assessment. KOMODO catalog is identity only.
  snapshot_sha256: 19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5
- evidence_id: komodoList
  kind: search
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  accessed_at: '2026-10-28T09:30:19.910146Z'
  locator: REVIEW_WORK/batch062/source07-09/komodoList.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact selected source identity and complete source stages; inspect organism
    context before operational assessment. KOMODO catalog is identity only.
  snapshot_sha256: de31b7d1d29d80922cfcfe975db4747b35b04228f8a0531b90353cef02760ad7
  search_scope: One exact public GET of https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodo411
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=411
  accessed_at: '2026-10-28T09:33:08.697514Z'
  locator: REVIEW_WORK/batch062/source07-09/komodo411.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact historical KOMODO MediaInfo411 route requested once; HTTP403 retained.
    Failed access does not authenticate the page or any unrelated stock subsection.
  snapshot_sha256: 4c51984c1851a24ec8b195d345018ee5b6c0f59d2cb7e97c3f2ced33cfa2fc0c
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=411;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T09:41:40.151212Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 884ed98f0166e1e43ad747e60fb62520f5e60e528d357bd0074b61440884be91
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T09:41:40.151356Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: e322d3cdf8fd10aee848006830523a4b198d25a6e4454267e62b47002933ff89
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T09:41:40.151377Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T09:41:40.151670Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T09:41:40.151690Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T09:41:40.151708Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T09:41:40.151730Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: f3376b4bdf60b96bb202254f656d7b39df947369e777dec9ea63bff30e8a1d87
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/inspected-candidate-context.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T09:41:40.151752Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: bea184ce1f011e5714cef082c0341aaf001d16024ef7935d004cbc8899f74fd5
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T09:41:40.152312Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T09:41:40.159233Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: b8a13b6223d99ffe3db1e5c1392f1d3f5d3ada148d166ad8b4b3a36bee203a32
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T09:41:40.159285Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/clostridium_acetobutylicum_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T09:41:40.164752Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: f9c7a62fa40ca03fe5316f0267faf9979429cfe2d0a1c2345a8e6621f6ffcb38
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T09:41:40.164806Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: b38b8da71a36eb5d51f9527b5feb3750e9bef68762a69057e613a2f5cf5111b2
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T09:41:40.164832Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 627d0a44c05f722a4ae8bf247e0ea2fe5193f2792b06a8dc3dff74513403adef
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T09:41:40.164855Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 99bc46175b8e10e18034536d3127b6b300c5174a9bdf4a1e35ea6935ace97958
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch062/record08/historical-reading.json
  accessed_at: '2026-10-28T09:41:40.164881Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 06276cb499bea7af9c3ae1929cda43fb7586b0e4eaec4e516046ada2e97196f7
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch062/record08/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T09:41:40.165126Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: dca46dfe19bfc15a3916003b6df16a4f3124ffd054f7e0a2404efc060f5c0a6b
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch062/record08/complete-document-reader.json
  accessed_at: '2026-10-28T09:41:40.165292Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: d4b27938892f6ff6f2839b1f6618e7bf2d1a4f0a1f6432733bd2d4054da5f8cc
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _parse_api_solutions, _normalize_unit,
    _parse_preparation_steps, _classify_preparation_action
  accessed_at: '2026-10-28T09:52:06.487676Z'
  support: context_only
  summary: Current _parse_api_composition reads the primary solution only; _is_api_stock_addition
    recognizes solution_id or percent-labelled ml rows. Molar-only stock attributes
    are outside that predicate; preparation steps are pooled across solutions. Current
    code is not proof of historical execution. Current _classify_preparation_action
    uses substring freeze to choose STORE, so the exact reactivation note requires
    action-code review.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: merge_duplicate_ingredients and _merge_ingredient_group
  accessed_at: '2026-10-28T09:41:40.165477Z'
  support: context_only
  summary: Current _merge_ingredient_group no longer sums disagreeing duplicate concentrations;
    keeps first and flags conflicts. Historical summed notes remain separate evidence.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T09:41:40.165502Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer-resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: merge_composition and _add_enrichment_metadata
  accessed_at: '2026-10-28T09:41:40.165545Z'
  support: context_only
  summary: Current merge_composition copies source ingredients and solutions but only
    fills missing target pH; it does not establish equivalence of a pre-existing KOMODO
    pH with the DSM formulation. _add_enrichment_metadata uses a naive current datetime.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-komodo
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech history timestamp
  accessed_at: '2026-10-28T09:41:40.165569Z'
  support: context_only
  summary: Current web importer writes its timestamp using time.strftime with unsupported
    %f; the literal .fZ history must be preserved as historical provenance with an
    appended correction, not backdated or erased.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: chebi3311
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:3311
  accessed_at: '2026-10-28T09:30:21.792847Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi3311.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 4ae83765c52d41f4a029e4e3b76d61a15ba0c5d3146cf611ca991e5b03748dd1
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806
  accessed_at: '2026-10-28T09:30:23.822472Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi8806.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: f2530ec9c15f59a3d132a466c9c3a899497bab0f85b996d3e27bef8612f89982
- evidence_id: chebi17634
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17634
  accessed_at: '2026-10-28T09:30:20.623351Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi17634.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 04060738e01fe33b9fc8e5bf54807590127ce391eb8a962d1d013002502169b2
- evidence_id: chebi91248
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91248
  accessed_at: '2026-10-28T09:30:23.852060Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi91248.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: d0959ac455ece32a6e94c13fd8e592403109201b6c61144dccfe0d58f1916380
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch062/record08/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T09:52:06.488433Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: bac0d53e6aaec932cd60074ab782d4248034f8eaa6e465878c839e990fd463d1
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch062/record08/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T09:41:40.210562Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 0a2bbae3e49878e5605a1a622c7b4e3cd04d52c2473613e6aa5044072b95f70e
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch062/record08/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T09:41:40.210598Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: d83ca077059f4ecfbf2a336e0dd7213b755ba1f08587bd73c6f2b78f0fdadf3e
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch062/record08/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T09:41:40.210631Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: ae53403a57d3e27ff3d978f26e675d0f1a04465f5279d8e139225134d252860d
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch062/record08/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T09:41:40.210661Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 06d9d29488bca3d673ee07746ca32be89a317ad50cc9d72adecf9b7b0d004d1e
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch062/record08/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T09:41:40.210682Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 0771f17b13680d47f53245715870938ebbbfcdc15af2dfa3b5abbb2f5ca6df74
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch062/record08/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T09:41:40.210700Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch062/record08/schema-result.json
  accessed_at: '2026-10-28T09:30:22.800653Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 817a91fa70dc2115ad4254dd5f410d057443cc9c50882748bda649b17bd34608
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch062/record08/strict-result.json
  accessed_at: '2026-10-28T09:30:23.720874Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 8b6f8046494ada5f747609ce2f1481e555d5cc14f6b3c7fbb23de55bff4a2a39
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch062/record08/terms-result.json
  accessed_at: '2026-10-28T09:30:24.722320Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 84c4d2f85850f3ca93a70ce0255f4318a80bc3c581a3fb31570a763d5f557e49
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch062/record08/references-result.json
  accessed_at: '2026-10-28T09:30:25.360001Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: ee2ffc81277397f8a21b7b22d04487c5165183cd1e226261ef520dc800618509
assessments:
- assessment_id: identity
  area: identity
  topic: DSM411 correspondence and unresolved KOMODO branch
  outcome: concern
  summary: The source mapping and exact maintained IDs establish DSM411 correspondence,
    but historical KOMODO pH 7.1 and the collapsed main/milk formulation require explicit
    variant accounting. Exact historical MediaInfo411 and current MediaList requests
    returned 403; those failures do not erase the preserved historical mapping row.
  target_ids:
  - CultureMech:005233
  evidence_ids:
  - api411
  - dsm411
  - historical-reading
  - komodo411
  - komodoList
- assessment_id: classification
  area: scope
  topic: Complex liquid formulation and organism scope
  outcome: supported
  summary: Fresh potatoes/milk make the formulations chemically undefined. The source
    names no specific strain and does not establish a strain-growth association; no
    organism or incubation claim is inferred from the medium title.
  target_ids:
  - CultureMech:005233
  evidence_ids:
  - dsm411
  - api411
  - target
- assessment_id: native
  area: schema
  topic: Native structural checks
  outcome: supported
  summary: All four canonical checks passed once, including zero strict errors and
    zero reference checks; this does not authenticate recipe identity or stages.
  target_ids:
  - CultureMech:005233
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 18 current concentration fields are covered by 14 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:005233
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b062-quantity-inventory-v1","target":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","quantity_field_count":18,"decisions":[{"quantity_id":"q1","label":"Potato","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"200","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"200","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"200","unit":"G_PER_L"}}],"decision":"mixed","rationale":"DSM411
    explicitly reports the main-formulation g_l=200 and the PDF prints 200 g as a
    batch input. This supports the DSM owner''s nominal recipe basis without attached
    evidence, not a measured final concentration. The target/KOMODO layer also carries
    milk-medium pH 7.1 and a collapsed formulation, so its whole-formulation basis
    remains unresolved. Potato is fresh, washed, peeled and sliced input subsequently
    filtered; 200 g is not a measured mass of final infusion solids.","source_stage":"DSM411
    main formulation; unresolved merged/KOMODO variant","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Potato\",\n                        \"compound_id\":
    1606,\n                        \"condition\": \"\",\n                        \"attribute\":
    \"fresh, washed, peeled and sliced\",\n                        \"amount\": 200,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 200,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt
    lines 3-3","quote":"Potato (fresh, washed, peeled and sliced)              200.00         g","quote_basis":"derivative
    text"}],"layer_decisions":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"Local
    nominal mass agrees, but current mixed-formulation/pH identity is not authenticated
    as one recipe."},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"Local
    nominal mass agrees, but current mixed-formulation/pH identity is not authenticated
    as one recipe."},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"Explicit
    provider main-recipe rate, no attached evidence."}]},{"quantity_id":"q2","label":"CaCO3","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"mixed","rationale":"DSM411
    explicitly reports the main-formulation g_l=2 and the PDF prints 2 g as a batch
    input. This supports the DSM owner''s nominal recipe basis without attached evidence,
    not a measured final concentration. The target/KOMODO layer also carries milk-medium
    pH 7.1 and a collapsed formulation, so its whole-formulation basis remains unresolved.","source_stage":"DSM411
    main formulation; unresolved merged/KOMODO variant","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"CaCO3\",\n                        \"compound_id\":
    13,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\":
    19.982,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt
    lines 4-4","quote":"CaCO3                                                    2.00         g","quote_basis":"derivative
    text"}],"layer_decisions":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"Local
    nominal mass agrees, but current mixed-formulation/pH identity is not authenticated
    as one recipe."},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"Local
    nominal mass agrees, but current mixed-formulation/pH identity is not authenticated
    as one recipe."},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"Explicit
    provider main-recipe rate, no attached evidence."}]},{"quantity_id":"q3","label":"D-Glucose","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"6","unit":"G_PER_L"}}],"decision":"mixed","rationale":"DSM411
    explicitly reports the main-formulation g_l=6 and the PDF prints 6 g as a batch
    input. This supports the DSM owner''s nominal recipe basis without attached evidence,
    not a measured final concentration. The target/KOMODO layer also carries milk-medium
    pH 7.1 and a collapsed formulation, so its whole-formulation basis remains unresolved.","source_stage":"DSM411
    main formulation; unresolved merged/KOMODO variant","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\":
    211,\n                        \"amount\": 6,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 6,\n                        \"mmol_l\":
    33.3037,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt
    lines 6-6","quote":"D-Glucose                                                6.00         g","quote_basis":"derivative
    text"}],"layer_decisions":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"Local
    nominal mass agrees, but current mixed-formulation/pH identity is not authenticated
    as one recipe."},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"Local
    nominal mass agrees, but current mixed-formulation/pH identity is not authenticated
    as one recipe."},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"Explicit
    provider main-recipe rate, no attached evidence."}]},{"quantity_id":"q4","label":"L-Cysteine
    HCl x H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"mixed","rationale":"DSM411
    explicitly reports the main-formulation g_l=0.5 and the PDF prints 0.5 g as a
    batch input. This supports the DSM owner''s nominal recipe basis without attached
    evidence, not a measured final concentration. The target/KOMODO layer also carries
    milk-medium pH 7.1 and a collapsed formulation, so its whole-formulation basis
    remains unresolved.","source_stage":"DSM411 main formulation; unresolved merged/KOMODO
    variant","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\":
    770,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.8468,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt
    lines 7-7","quote":"L-Cysteine HCl x H2O                                     0.50         g","quote_basis":"derivative
    text"}],"layer_decisions":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"Local
    nominal mass agrees, but current mixed-formulation/pH identity is not authenticated
    as one recipe."},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"Local
    nominal mass agrees, but current mixed-formulation/pH identity is not authenticated
    as one recipe."},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"Explicit
    provider main-recipe rate, no attached evidence."}]},{"quantity_id":"q5","label":"Collapsed
    sodium resazurin","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.0006000000000000001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.0006000000000000001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.0006000000000000001","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    0.0006000000000000001 G_PER_L note explicitly sums 0.0005 and 0.0001 from two
    distinct formulations. The primary has separate 0.50 ml and 0.10 ml aliquots of
    0.1% w/v stock. These are not duplicate additions to one medium, and the provider
    milk g_l=0.0001 is not a self-consistent final rate for its declared 100 ml recipe.
    Preserve the aliquots and strength by formulation; do not resolve this by summing
    or treating the provider number as final-volume proof.","source_stage":"Two independent
    source formulations","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.0005,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.1,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.0001,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt
    lines 5-5","quote":"Sodium resazurin (0.1% w/v)                              0.50        ml","quote_basis":"derivative
    text"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt
    lines 20-24","quote":"Milk Medium\n   Milk (fresh)                                           100.00        ml\n   Sodium
    resazurin (0.1% w/v)                              0.10        ml\n\nAdjust pH
    to 7.1. Tube and autoclave under 100% N2 gas atmosphere for 12 min at 121°C.","quote_basis":"derivative
    text"}]},{"quantity_id":"q6","label":"Milk volume represented as mass","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source specifies 100 ml fresh milk in the separate Milk Medium, not 100 g/L in
    the potato formulation. Density is unestablished. Preserve the volume input and
    independent recipe identity; no mass conversion is justified.","source_stage":"Milk-medium
    input volume","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Milk\",\n                        \"compound_id\":
    467,\n                        \"attribute\": \"fresh\",\n                        \"amount\":
    100,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt
    lines 20-24","quote":"Milk Medium\n   Milk (fresh)                                           100.00        ml\n   Sodium
    resazurin (0.1% w/v)                              0.10        ml\n\nAdjust pH
    to 7.1. Tube and autoclave under 100% N2 gas atmosphere for 12 min at 121°C.","quote_basis":"derivative
    text"}]},{"quantity_id":"q7","label":"Root pH assertions","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ph_value","stored":7.1},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ph_value","stored":7.1},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ph_value","stored":6.8}],"decision":"mixed","rationale":"The
    primary main formulation ends at pH 6.8, correctly retained by the DSM owner.
    Target/KOMODO root pH 7.1 belongs to the separate milk formulation. A catalog
    mapping to DSM411 does not authenticate that mixed formulation; assign pH only
    within the corresponding recipe branch.","source_stage":"Recipe-specific pH","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Mix potatoes and CaCO3 then autoclave 30 min at 121\\u00b0C. Filter through
    cheese cloth, add glucose and cysteine, distribute under 100% N2 gas atmosphere
    into anoxic Hungate-type tubes or serum vials and autoclave at 121\\u00b0C for
    20 min. Adjust pH of complete medium to 6.8.\"\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\":
    \"Adjust pH to 7.1. Tube and autoclave under 100% N2 gas atmosphere for 12 min
    at 121\\u00b0C.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt
    lines 10-15","quote":"1. Mix potatoes and CaCO3 then autoclave 30 min at 121°C.
    Filter through cheese cloth,\nadd glucose and cysteine, distribute under 100%
    N2 gas atmosphere into anoxic\nHungate-type tubes or serum vials and autoclave
    at 121°C for 20 min. Adjust pH of\ncomplete medium to 6.8.\n2. Note: For the reactivation
    of freeze-dried strains it is recommended to use the following\nsimple milk medium:","quote_basis":"derivative
    text"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt
    lines 24-24","quote":"Adjust pH to 7.1. Tube and autoclave under 100% N2 gas atmosphere
    for 12 min at 121°C.","quote_basis":"derivative text"}],"layer_decisions":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml","field_path":"ph_value","decision":"correct","rationale":"7.1
    belongs to milk formulation, not main potato medium."},{"path":"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml","field_path":"ph_value","decision":"correct","rationale":"7.1
    belongs to milk formulation, not main potato medium."},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"Primary
    main-recipe pH supported without attached evidence."}]},{"quantity_id":"q8","label":"Existing
    DSM preparation 1","local_fields":[{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"preparation_steps[0].description","stored":"Mix
    potatoes and CaCO3 then autoclave 30 min at 121°C. Filter through cheese cloth,
    add glucose and cysteine, distribute under 100% N2 gas atmosphere into anoxic
    Hungate-type tubes or serum vials and autoclave at 121°C for 20 min. Adjust pH
    of complete medium to 6.8."}],"decision":"evidence_only","rationale":"The DSM
    owner preserves this exact preparation context, including stage-specific temperature/time/gas/pH
    where printed. Credit it; separate main versus milk sequence rather than applying
    all steps to one combined recipe.","source_stage":"Main potato sequence","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Mix potatoes and CaCO3 then autoclave 30 min at 121\\u00b0C. Filter through
    cheese cloth, add glucose and cysteine, distribute under 100% N2 gas atmosphere
    into anoxic Hungate-type tubes or serum vials and autoclave at 121\\u00b0C for
    20 min. Adjust pH of complete medium to 6.8.\"\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt
    lines 10-15","quote":"1. Mix potatoes and CaCO3 then autoclave 30 min at 121°C.
    Filter through cheese cloth,\nadd glucose and cysteine, distribute under 100%
    N2 gas atmosphere into anoxic\nHungate-type tubes or serum vials and autoclave
    at 121°C for 20 min. Adjust pH of\ncomplete medium to 6.8.\n2. Note: For the reactivation
    of freeze-dried strains it is recommended to use the following\nsimple milk medium:","quote_basis":"derivative
    text"}]},{"quantity_id":"q9","label":"Existing DSM preparation 2","local_fields":[{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"preparation_steps[1].description","stored":"Note:
    For the reactivation of freeze-dried strains it is recommended to use the following
    simple milk medium:"},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"preparation_steps[1].action","stored":"STORE"}],"decision":"mixed","rationale":"The
    DSM owner preserves this exact preparation context, including stage-specific temperature/time/gas/pH
    where printed. Credit it; separate main versus milk sequence rather than applying
    all steps to one combined recipe. The retained description concerns reactivating
    freeze-dried strains; its STORE action is a classification mismatch, not a storage
    instruction. Preserve the description and correct only that action after choosing
    the appropriate source-faithful representation.","source_stage":"Main potato sequence","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\":
    \"Note: For the reactivation of freeze-dried strains it is recommended to use
    the following simple milk medium:\"\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt
    lines 10-15","quote":"1. Mix potatoes and CaCO3 then autoclave 30 min at 121°C.
    Filter through cheese cloth,\nadd glucose and cysteine, distribute under 100%
    N2 gas atmosphere into anoxic\nHungate-type tubes or serum vials and autoclave
    at 121°C for 20 min. Adjust pH of\ncomplete medium to 6.8.\n2. Note: For the reactivation
    of freeze-dried strains it is recommended to use the following\nsimple milk medium:","quote_basis":"derivative
    text"}],"layer_decisions":[{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"preparation_steps[1].description","decision":"evidence_only","rationale":"Exact
    source description retained."},{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"preparation_steps[1].action","decision":"correct","rationale":"Reactivation
    context is not storage; current classifier matches the word freeze to STORE."}]},{"quantity_id":"q10","label":"Existing
    DSM preparation 3","local_fields":[{"path":"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml","field_path":"preparation_steps[2].description","stored":"Adjust
    pH to 7.1. Tube and autoclave under 100% N2 gas atmosphere for 12 min at 121°C."}],"decision":"evidence_only","rationale":"The
    DSM owner preserves this exact preparation context, including stage-specific temperature/time/gas/pH
    where printed. Credit it; separate main versus milk sequence rather than applying
    all steps to one combined recipe.","source_stage":"Milk sequence","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\":
    \"Adjust pH to 7.1. Tube and autoclave under 100% N2 gas atmosphere for 12 min
    at 121\\u00b0C.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt
    lines 24-24","quote":"Adjust pH to 7.1. Tube and autoclave under 100% N2 gas atmosphere
    for 12 min at 121°C.","quote_basis":"derivative text"}]},{"quantity_id":"q11","label":"Main
    water input","local_fields":[],"decision":"evidence_only","rationale":"1000 ml
    water is the main recipe input; it is not a measured final volume after extraction
    and additions.","source_stage":"Main water","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt
    lines 8-8","quote":"Distilled water                                       1000.00        ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q12","label":"Main resazurin stock dose/strength","local_fields":[],"decision":"evidence_only","rationale":"0.50
    ml of explicitly 0.1% w/v stock belongs to the main recipe. Preserve stock composition
    separately from receiving volume.","source_stage":"Main indicator stock","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.0005,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt
    lines 5-5","quote":"Sodium resazurin (0.1% w/v)                              0.50        ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q13","label":"Milk resazurin stock dose/strength","local_fields":[],"decision":"evidence_only","rationale":"0.10
    ml of explicitly 0.1% w/v stock belongs to Milk Medium. The provider reports g_l=0.0001
    alongside volume=100; retain that normalization inconsistency, without converting
    to an assumed final concentration.","source_stage":"Milk indicator stock","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.1,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.0001,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm411","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium411.pdf","raw_path":"REVIEW_WORK/batch062/source07-09/dsm411.raw","raw_sha256":"44e952aa2b0cd1ee8d4e192ecf8e89265bfdca02455e391ebdf1d0a6a3eafdf2","text_sha256":"2d505494c4a264e2cc71f8e50d414ad3c3f16fa45b34fc706c95edf508301adf","accessed_at":"2026-10-28T09:30:19.840962Z","locator":"dsm411.txt
    lines 20-24","quote":"Milk Medium\n   Milk (fresh)                                           100.00        ml\n   Sodium
    resazurin (0.1% w/v)                              0.10        ml\n\nAdjust pH
    to 7.1. Tube and autoclave under 100% N2 gas atmosphere for 12 min at 121°C.","quote_basis":"derivative
    text"}]},{"quantity_id":"q14","label":"Provider declared recipe volumes","local_fields":[],"decision":"evidence_only","rationale":"The
    provider declares main volume 1000 ml and milk volume 100 ml. These metadata are
    recorded, not relabelled as measured final volumes; primary water/milk inputs
    and added indicator volumes remain separate.","source_stage":"Provider normalization
    metadata","sources":[{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"$.data.solutions[0].volume","quote":"\"volume\":
    1000","quote_basis":"raw UTF-8"},{"evidence_id":"api411","reference":"https://mediadive.dsmz.de/rest/medium/411","raw_path":"REVIEW_WORK/batch062/source07-09/api411.raw","raw_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","text_sha256":"19e21b679caa0450d5c862b718a4b72440eb20f64b51cec18e425fd01bccfbb5","accessed_at":"2026-10-28T09:30:20.201602Z","locator":"$.data.solutions[1].volume","quote":"\"volume\":
    100,","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/CLOSTRIDIUM_ACETOBUTYLICUM_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml":null,"data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All asserted CHEBI IDs and labels resolve, but Sodium resazurin has the
    neutral CHEBI:8806 formula. D-glucose, calcium carbonate and L-cysteine hydrochloride
    monohydrate otherwise correspond to the named forms. Secondary-link presence is
    three of six ingredient nodes per layer; validity among asserted links is separately
    checked against the current packaged CSV. Potato and fresh milk are complex ingredients,
    not forced into invented pure-chemical IDs.
  target_ids:
  - CultureMech:005233
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: October5 reports explicitly did no source verification; October7 reports
    retained all six values unchanged because stock/formulation and pH conditions
    were unresolved. Their exact source rows match the fresh API content where recorded.
    Current cleanup avoids duplicate summation and current merger requires formulation
    equality; the historical collapsed target is not proof those current safeguards
    failed. The extant malformed import timestamp remains a confirmed provenance concern.
  target_ids:
  - CultureMech:005233
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-005233-formulation-collapse
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Potato and milk formulations have been combined
  description: Separate the main DSM411 potato formulation from its explicitly distinct
    Milk Medium. The current list assigns milk volume to G_PER_L and sums the two
    indicator entries as if they were additions to one recipe. Restore source-specific
    ingredient/stock boundaries and preserve the source volume units and unmeasured
    final-volume limitation. Current cleanup no longer sums disagreeing duplicates;
    current MediaDive parsing reads the first recipe only, while its preparation parser
    still pools steps from every solution, so preserve that remaining branch-specific
    context when regenerating.
  target_ids:
  - CultureMech:005233
  field_paths:
  - ingredients[2]
  - ingredients[5]
  - solutions
  - preparation_steps
  evidence_ids:
  - dsm411
  - api411
  - writer-cleanup
  - writer-mediadive
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-005233-ph-variant
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Main and milk-medium pH are not interchangeable
  description: Resolve target/KOMODO pH 7.1 against the exact formulation identity.
    The primary assigns 6.8 to the main potato formulation and 7.1 to the separate
    milk medium; the DSM owner already correctly has main pH 6.8. Preserve that repaired/current
    distinction and do not copy a source composition while retaining a conflicting
    root pH.
  target_ids:
  - CultureMech:005233
  field_paths:
  - ph_value
  - data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml::ph_value
  evidence_ids:
  - dsm411
  - api411
  - owner-2
  - writer-resolver
  rule_id: review-yaml-record/consistency
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-005233-resazurin-salt
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Sodium resazurin is grounded as the neutral molecule
  description: The target and both owners assert Sodium resazurin but their primary
    term is CHEBI:8806, whose fresh OLS formula C12H7NO4 contains no sodium. Reconcile
    the supplied sodium salt; do not mistake current canonical-label agreement for
    supplied-form correctness. These nodes have no secondary MIM slot, so no nonexistent
    secondary field is cited.
  target_ids:
  - CultureMech:005233
  field_paths:
  - ingredients[2].term
  evidence_ids:
  - dsm411
  - api411
  - chebi8806
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-005233-generated-preparation-loss
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Generated preparation loses the maintained source sequences
  description: 'The DSM owner retains all three source preparation entries, including
    the main extraction/sterilization sequence and separate milk instructions; the
    generated target and KOMODO owner do not. Preserve the correct source-specific
    process and ingredient grade (fresh prepared potato, fresh milk), without promoting
    the historical Aerobic: Yes flag into a growth or preparation assertion. Current
    conservative merging rejects incompatible notes, pH and preparation rather than
    legitimizing the stale collapsed target. The DSM owner preparation_steps[1] description
    concerns reactivating freeze-dried strains, but its action STORE is not source-faithful.
    Preserve that description and correct the action classification. Current _classify_preparation_action
    maps the substring freeze to STORE; this demonstrates current behavior, not historical
    execution.'
  target_ids:
  - CultureMech:005233
  field_paths:
  - preparation_steps
  - notes
  - data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml::preparation_steps[1].action
  evidence_ids:
  - owner-2
  - dsm411
  - api411
  - writer-formulation
  - writer-merger
  rule_id: review-yaml-record/completeness
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml
    role: maintained source
- finding_id: f5
  issue_key: culturemech-005233-history-timestamp
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Import timestamps need an append-only provenance correction
  description: The KOMODO owner and generated history retain 2026-01-27T01:15:02.fZ,
    and the resolver event is timezone-naive. Current komodo_web_importer uses time.strftime
    with %f, so the formatting defect is demonstrable in present code. Preserve the
    old history bytes and append an actual explanatory correction; do not invent the
    original fraction or timezone. Correct future writer serialization without claiming
    historical code execution from the current body.
  target_ids:
  - CultureMech:005233
  field_paths:
  - curation_history
  evidence_ids:
  - owner
  - target
  - writer-komodo
  - writer-resolver
  rule_id: review-yaml-record/provenance
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml
    role: maintained source
actions:
- action_id: a1
  description: Separate the main DSM411 potato formulation from its explicitly distinct
    Milk Medium. The current list assigns milk volume to G_PER_L and sums the two
    indicator entries as if they were additions to one recipe. Restore source-specific
    ingredient/stock boundaries and preserve the source volume units and unmeasured
    final-volume limitation. Current cleanup no longer sums disagreeing duplicates;
    current MediaDive parsing reads the first recipe only, while its preparation parser
    still pools steps from every solution, so preserve that remaining branch-specific
    context when regenerating.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:005233
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a2
  description: Resolve target/KOMODO pH 7.1 against the exact formulation identity.
    The primary assigns 6.8 to the main potato formulation and 7.1 to the separate
    milk medium; the DSM owner already correctly has main pH 6.8. Preserve that repaired/current
    distinction and do not copy a source composition while retaining a conflicting
    root pH.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:005233
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a3
  description: The target and both owners assert Sodium resazurin but their primary
    term is CHEBI:8806, whose fresh OLS formula C12H7NO4 contains no sodium. Reconcile
    the supplied sodium salt; do not mistake current canonical-label agreement for
    supplied-form correctness. These nodes have no secondary MIM slot, so no nonexistent
    secondary field is cited.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:005233
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a4
  description: 'The DSM owner retains all three source preparation entries, including
    the main extraction/sterilization sequence and separate milk instructions; the
    generated target and KOMODO owner do not. Preserve the correct source-specific
    process and ingredient grade (fresh prepared potato, fresh milk), without promoting
    the historical Aerobic: Yes flag into a growth or preparation assertion. Current
    conservative merging rejects incompatible notes, pH and preparation rather than
    legitimizing the stale collapsed target. The DSM owner preparation_steps[1] description
    concerns reactivating freeze-dried strains, but its action STORE is not source-faithful.
    Preserve that description and correct the action classification. Current _classify_preparation_action
    maps the substring freeze to STORE; this demonstrates current behavior, not historical
    execution.'
  finding_ids:
  - f4
  target_ids:
  - CultureMech:005233
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_acetobutylicum_medium.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a5
  description: The KOMODO owner and generated history retain 2026-01-27T01:15:02.fZ,
    and the resolver event is timezone-naive. Current komodo_web_importer uses time.strftime
    with %f, so the formatting defect is demonstrable in present code. Preserve the
    old history bytes and append an actual explanatory correction; do not invent the
    original fraction or timezone. Correct future writer serialization without claiming
    historical code execution from the current body.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:005233
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_411_CLOSTRIDIUM_ACETOBUTYLICUM_medium.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
limitations:
- This scientific review is partial because the exact current KOMODO branch remains
  unavailable. The preserved historical mapping and current DSM411 evidence support
  the bounded findings, but do not resolve whether the KOMODO branch represents the
  main or milk formulation.
- The Milk Medium provider g_l for resazurin is preserved as conflicting normalization
  metadata, not used to compute a final concentration. No milk density or extracted
  potato-solids yield is assumed.
- Both exact KOMODO routes are currently unavailable (403). Historical catalog correspondence
  is derivative evidence and is not a new authenticated catalog capture.
- DSM411 PDF is one page; both main and Milk Medium sections were visually checked
  against the extracted text. Unknown individual authors/publication year are not
  filled from the copyright year.
- No strain-growth claim, optimization or experimental recommendation is inferred
  from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent
  rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed
  only on their declared normalization basis; unspecified percent bases and hydrate
  numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was
  performed by this author.
```
