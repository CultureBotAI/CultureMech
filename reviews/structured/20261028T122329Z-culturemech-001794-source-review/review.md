# Scientific review: COW MANURE AGAR

- Review: 20261028T122329Z-culturemech-001794-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T12:02:49.854477Z
- Finished UTC: 2026-10-28T12:23:29.927443Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The maintained owner already separates extraction inputs from prepared extract and retains authenticated agar evidence. The generated target is stale and still mislabels mechanical cloth/paper filtration as sterile filtration. One major generated-boundary finding and one minor classifier finding require bounded follow-up; all native diagnostics passed without establishing source truth.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch066 index 07
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001794 | data/merge_yaml/merged/COW_MANURE_AGAR.yaml | generated | cow_manure_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:001794 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:001794 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:001794 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:001794 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact DSM657 identity

identity: supported. Targets: CultureMech:001794.

Stable target/owner identity, declared DSM657 source and current API657/PDF title agree. The source supplies no strain or organism-specific growth claim.

### Extraction and processing scope

representation: concern. Targets: CultureMech:001794.

Full primary PDF page visually read. The owner preserves all ordered extraction instructions and supported make-up; the generated action code overstates filtration. Source does not specify pH, autoclave conditions or extraction yield, so none is supplied.

### Native structure and selected ownership

schema: supported. Targets: CultureMech:001794.

Original schema, strict and terms passed; reference validator performed zero checks. The append-only inspection preserves all original inputs and adds exact extraction report context; these diagnostics do not establish scientific correctness.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:001794.

6 current concentration fields are covered by 9 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b066-quantity-inventory-v1","target":"data/merge_yaml/merged/COW_MANURE_AGAR.yaml","quantity_field_count":6,"decisions":[{"quantity_id":"q1","label":"Generated dry manure concentration","local_fields":[{"path":"data/merge_yaml/merged/COW_MANURE_AGAR.yaml","field_path":"ingredients[0].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source50g is extraction starting material. Filtration removes solids; it does not establish50g/L retained dissolved material. Withdraw the generated final-ingredient concentration and preserve the already curated owner extraction-input note without inventing yield.","source_stage":"Extraction input, not recovered solute","sources":[{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Dry cow-manure\",\n                        \"compound_id\": 2131,\n                        \"amount\": 50,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first through cheesecloth and then paper. Make up volume to one liter. Add 20 g agar.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm657","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf","raw_path":"REVIEW_WORK/batch066/source07-08-10/dsm657.raw","raw_sha256":"eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930","text_sha256":"26a804b7f79cc60399495c0ec3a8e7564ae7dfeff54f20e3cfb5e9efa544beba","accessed_at":"2026-10-28T12:03:13.855084Z","locator":"dsm657.txt lines 3-4","quote":"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first\nthrough cheesecloth and then paper. Make up volume to one liter. Add 20 g agar.","quote_basis":"derivative text"}]},{"quantity_id":"q2","label":"Generated tap water mass concentration","local_fields":[{"path":"data/merge_yaml/merged/COW_MANURE_AGAR.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1000","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source1000ml is1L initial water; no density or mass concentration is given. Credit the current owner absolute-volume repair and separate the later make-up.","source_stage":"Initial extraction solvent","sources":[{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Tap water\",\n                        \"compound_id\": 322,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first through cheesecloth and then paper. Make up volume to one liter. Add 20 g agar.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm657","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf","raw_path":"REVIEW_WORK/batch066/source07-08-10/dsm657.raw","raw_sha256":"eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930","text_sha256":"26a804b7f79cc60399495c0ec3a8e7564ae7dfeff54f20e3cfb5e9efa544beba","accessed_at":"2026-10-28T12:03:13.855084Z","locator":"dsm657.txt lines 3-4","quote":"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first\nthrough cheesecloth and then paper. Make up volume to one liter. Add 20 g agar.","quote_basis":"derivative text"}]},{"quantity_id":"q3","label":"Generated agar concentration","local_fields":[{"path":"data/merge_yaml/merged/COW_MANURE_AGAR.yaml","field_path":"ingredients[2].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Source20g is added after filtered extract is made up to1L.20g/L is supported on this explicitly prepared extract basis; the target lacks the owner attached evidence and basis note. This is not a measured final agar-medium volume.","source_stage":"Agar per made-up extract","sources":[{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 59.4654,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first through cheesecloth and then paper. Make up volume to one liter. Add 20 g agar.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm657","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf","raw_path":"REVIEW_WORK/batch066/source07-08-10/dsm657.raw","raw_sha256":"eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930","text_sha256":"26a804b7f79cc60399495c0ec3a8e7564ae7dfeff54f20e3cfb5e9efa544beba","accessed_at":"2026-10-28T12:03:13.855084Z","locator":"dsm657.txt lines 3-4","quote":"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first\nthrough cheesecloth and then paper. Make up volume to one liter. Add 20 g agar.","quote_basis":"derivative text"}]},{"quantity_id":"q4","label":"Owner retained agar concentration and basis","local_fields":[{"path":"data/normalized_yaml/bacterial/cow_manure_agar.yaml","field_path":"ingredients[0].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cow_manure_agar.yaml","field_path":"ingredients[0].notes","stored":"20 g added after the filtered extract is made up to one liter; no soil/manure concentration or extraction yield is inferred."}],"decision":"verified","rationale":"The retained20g/L and exact extract-stage note match primary/API text and the attached literal claim/current raw digest. No whole manure yield or final-medium volume inferred.","source_stage":"Agar per made-up extract","sources":[{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 59.4654,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first through cheesecloth and then paper. Make up volume to one liter. Add 20 g agar.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm657","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf","raw_path":"REVIEW_WORK/batch066/source07-08-10/dsm657.raw","raw_sha256":"eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930","text_sha256":"26a804b7f79cc60399495c0ec3a8e7564ae7dfeff54f20e3cfb5e9efa544beba","accessed_at":"2026-10-28T12:03:13.855084Z","locator":"dsm657.txt lines 3-4","quote":"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first\nthrough cheesecloth and then paper. Make up volume to one liter. Add 20 g agar.","quote_basis":"derivative text"}]},{"quantity_id":"q5","label":"Owner initial extraction water","local_fields":[{"path":"data/normalized_yaml/bacterial/cow_manure_agar.yaml","field_path":"solutions[0].composition[1].concentration","stored":{"value":"1","unit":"L"}},{"path":"data/normalized_yaml/bacterial/cow_manure_agar.yaml","field_path":"solutions[0].composition[1].notes","stored":"Initial extraction-water addition: 1000 ml / 1000 ml per L = 1 L, not a mass concentration or a measured recovered volume. The later make-up to one liter is a separate final-volume instruction; its additional water amount is unspecified."}],"decision":"verified","rationale":"1000ml/1000ml per L=1L. The owner explicitly distinguishes initial water from later make-up and has matching attached source evidence.","source_stage":"Initial extraction solvent","sources":[{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Tap water\",\n                        \"compound_id\": 322,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first through cheesecloth and then paper. Make up volume to one liter. Add 20 g agar.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm657","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf","raw_path":"REVIEW_WORK/batch066/source07-08-10/dsm657.raw","raw_sha256":"eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930","text_sha256":"26a804b7f79cc60399495c0ec3a8e7564ae7dfeff54f20e3cfb5e9efa544beba","accessed_at":"2026-10-28T12:03:13.855084Z","locator":"dsm657.txt lines 3-4","quote":"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first\nthrough cheesecloth and then paper. Make up volume to one liter. Add 20 g agar.","quote_basis":"derivative text"}]},{"quantity_id":"q6","label":"Owner made-up recovered extract","local_fields":[{"path":"data/normalized_yaml/bacterial/cow_manure_agar.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"L"}},{"path":"data/normalized_yaml/bacterial/cow_manure_agar.yaml","field_path":"solutions[0].notes","stored":"Curator-described extraction stage, not a separately accessioned stock. Composition lists preparation inputs, not retained solutes. The filtered extract is made up to one liter before agar is added. This is the prepared extract volume, not an extraction yield or a final agar-medium volume measurement."}],"decision":"verified","rationale":"The source explicitly instructs make-up to one liter after cloth/paper filtration. The owner1L describes prepared extract, with matching root evidence; it is neither extraction yield nor measured final agar-medium volume.","source_stage":"Made-up extract","sources":[{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first through cheesecloth and then paper. Make up volume to one liter. Add 20 g agar.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm657","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf","raw_path":"REVIEW_WORK/batch066/source07-08-10/dsm657.raw","raw_sha256":"eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930","text_sha256":"26a804b7f79cc60399495c0ec3a8e7564ae7dfeff54f20e3cfb5e9efa544beba","accessed_at":"2026-10-28T12:03:13.855084Z","locator":"dsm657.txt lines 3-4","quote":"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first\nthrough cheesecloth and then paper. Make up volume to one liter. Add 20 g agar.","quote_basis":"derivative text"}]},{"quantity_id":"q7","label":"Owner starting manure mass and unquantified yield","local_fields":[{"path":"data/normalized_yaml/bacterial/cow_manure_agar.yaml","field_path":"solutions[0].composition[0].notes","stored":"Extraction starting material: 50 g in 1000 ml tap water. Solids are separated before the recovered extract is used. The source does not quantify retained solids or dissolved yield; no numeric extract concentration is asserted."}],"decision":"verified","rationale":"The attached source authenticates the retained50g starting-input note. Absence of a numerical concentration is intentional: no retained-solids or dissolved yield is supplied.","source_stage":"Extraction input only","sources":[{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Dry cow-manure\",\n                        \"compound_id\": 2131,\n                        \"amount\": 50,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first through cheesecloth and then paper. Make up volume to one liter. Add 20 g agar.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm657","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf","raw_path":"REVIEW_WORK/batch066/source07-08-10/dsm657.raw","raw_sha256":"eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930","text_sha256":"26a804b7f79cc60399495c0ec3a8e7564ae7dfeff54f20e3cfb5e9efa544beba","accessed_at":"2026-10-28T12:03:13.855084Z","locator":"dsm657.txt lines 3-4","quote":"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first\nthrough cheesecloth and then paper. Make up volume to one liter. Add 20 g agar.","quote_basis":"derivative text"}]},{"quantity_id":"q8","label":"Complete generated preparation and owner separated stages","local_fields":[{"path":"data/merge_yaml/merged/COW_MANURE_AGAR.yaml","field_path":"preparation_steps[0].description","stored":"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first through cheesecloth and then paper. Make up volume to one liter. Add 20 g agar."},{"path":"data/normalized_yaml/bacterial/cow_manure_agar.yaml","field_path":"solutions[0].preparation_notes","stored":"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first through cheesecloth and then paper. Make up volume to one liter."},{"path":"data/normalized_yaml/bacterial/cow_manure_agar.yaml","field_path":"preparation_steps[0].description","stored":"Add 20 g agar."}],"decision":"mixed","rationale":"All source instructions, including one-hour boiling, cloth then paper filtration, make-up and agar addition, remain in the generated prose and the two owner stages. Owner descriptions and root claim are verified; generated description is evidence_only. Its FILTER_STERILIZE action is addressed separately: mechanical filtration is not proof of sterility.","source_stage":"Ordered extraction and agar addition","sources":[{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first through cheesecloth and then paper. Make up volume to one liter. Add 20 g agar.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm657","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf","raw_path":"REVIEW_WORK/batch066/source07-08-10/dsm657.raw","raw_sha256":"eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930","text_sha256":"26a804b7f79cc60399495c0ec3a8e7564ae7dfeff54f20e3cfb5e9efa544beba","accessed_at":"2026-10-28T12:03:13.855084Z","locator":"dsm657.txt lines 3-4","quote":"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first\nthrough cheesecloth and then paper. Make up volume to one liter. Add 20 g agar.","quote_basis":"derivative text"}]},{"quantity_id":"q9","label":"Unspecified additional make-up water","local_fields":[],"decision":"not_quantified","rationale":"The source supplies the target extract volume, not the additional amount of water required after boiling and filtration. No numerical top-up is proposed.","source_stage":"Post-filtration make-up","sources":[{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first through cheesecloth and then paper. Make up volume to one liter. Add 20 g agar.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm657","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf","raw_path":"REVIEW_WORK/batch066/source07-08-10/dsm657.raw","raw_sha256":"eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930","text_sha256":"26a804b7f79cc60399495c0ec3a8e7564ae7dfeff54f20e3cfb5e9efa544beba","accessed_at":"2026-10-28T12:03:13.855084Z","locator":"dsm657.txt lines 3-4","quote":"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first\nthrough cheesecloth and then paper. Make up volume to one liter. Add 20 g agar.","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/COW_MANURE_AGAR.yaml":null,"data/normalized_yaml/bacterial/cow_manure_agar.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: supported. Targets: CultureMech:001794.

All eight existing CHEBI slots across target and owner are exact current water/agar labels. Both two-of-three ingredient-instance secondary-link populations are reported separately; manure is an undefined mixture and not forced to a chemical ID. Current MIM rows are local snapshot evidence, not source recipe or historical legacy-ID certification. Tap-water qualification is retained; CHEBI water does not specify water grade.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:001794.

The two actual owner concentration/extraction events are credited. Four attached literal API claims and their stated raw digest are independently checked against current bytes, and the historical PDF digest is compared separately. Current equal bytes do not reconstruct the old retrieval event. Historical reports and exact selected plan rows remain derivative provenance. Current extraction repair code and conservative merger are read; no old execution is inferred.

## Findings

### f1: Generated record omits the maintained extraction repair

major / open / confirmed; issue key: culturemech-001794-generated-extraction-staleness.

The target still treats starting manure and tap water as finished-medium mass concentrations and lacks the owner extraction structure and four scoped evidence claims. The current owner has already removed the unsupported manure concentration, represents initial water and made-up extract separately in L, and retains supported agar on the prepared-extract basis. Regenerate from that exact owner and preserve its source-stage notes/evidence; do not repeat the obsolete concentration proposals. Current singleton merger copies the maintained record, and the current multi-record merge gate requires full formulation equality.

### f2: Mechanical filtration is classified as sterile filtration

minor / open / confirmed; issue key: culturemech-001794-mechanical-filtration-classifier.

The target preparation_steps[0].action is FILTER_STERILIZE although the exact source specifies cloth and paper filtration. The current owner already separates extraction notes from ADD_AGAR and makes no sterility claim. For this cloth/paper sentence, the current classifier reaches the filter branch and returns FILTER_STERILIZE; the preceding autoclave/steam-sterilization branch does not apply. Guard the writer for this mechanical extraction language. This current-code observation is not evidence that this exact revision produced the historical target.

## Recommended Actions And Acceptance Checks

### a1

The target still treats starting manure and tap water as finished-medium mass concentrations and lacks the owner extraction structure and four scoped evidence claims. The current owner has already removed the unsupported manure concentration, represents initial water and made-up extract separately in L, and retains supported agar on the prepared-extract basis. Regenerate from that exact owner and preserve its source-stage notes/evidence; do not repeat the obsolete concentration proposals. Current singleton merger copies the maintained record, and the current multi-record merge gate requires full formulation equality.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

The target preparation_steps[0].action is FILTER_STERILIZE although the exact source specifies cloth and paper filtration. The current owner already separates extraction notes from ADD_AGAR and makes no sterility claim. For this cloth/paper sentence, the current classifier reaches the filter branch and returns FILTER_STERILIZE; the preceding autoclave/steam-sterilization branch does not apply. Guard the writer for this mechanical extraction language. This current-code observation is not evidence that this exact revision produced the historical target.

- Preserve the exact extraction and agar descriptions without asserting sterile filtration. Keep the already repaired owner unchanged unless a separately justified curation is needed.
- Test the current classifier against this exact cloth/paper sentence and true sterile-filter instructions; regenerate and verify the selected target from its maintained owner.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsm657 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf; REVIEW_WORK/batch066/source07-08-10/dsm657.json; exact original raw/text/hash/time metadata | context_only | 07 exact primary recipe and extraction-stage evidence. |
| api657 | https://mediadive.dsmz.de/rest/medium/657; REVIEW_WORK/batch066/source07-08-10/api657.json; exact original raw/text/hash/time metadata | context_only | 07 exact current provider recipe and stage objects. |
| target | data/merge_yaml/merged/COW_MANURE_AGAR.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/cow_manure_agar.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-17 | reports/ingredient_concentration_curation/20261007-extraction-boundaries/657.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-18 | reports/ingredient_concentration_curation/20261007-extraction-boundaries/README.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-19 | reports/ingredient_concentration_curation/20261007-extraction-boundaries/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-20 | reports/ingredient_concentration_curation/20261007-extraction-boundaries/validation.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-21 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-22 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/cow_manure_agar.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/COW_MANURE_AGAR.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cow_manure_agar.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch066/record07/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch066/record07/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch066/record07/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser keeps only primary compounds and separately preserves referenced stocks. It still prioritizes provider g_l and normalizes bare g/ml/% to per-litre/w-v enums without independently establishing the basis; the action classifier tests temperature before cool. Current behavior is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| writer-extraction | scripts/repair_extraction_input_boundaries.py; COHORT[657], build, process | context_only | Full build and process source read: exact657/API/PDF/historical-plan guards separate starting solids and water from made-up extract, retain agar and literal evidence, and append the supplied curation event. Current code is not proof of the historical execution. |
| inspection-addendum | REVIEW_WORK/batch066/record07/inspection-addendum-extraction-report/lineage.json; Exact original→effective inspection lineage | supports | Four exact extraction follow-up inputs added; original50 inputs and selected target/owner unchanged. Original canonical checks reused without rerun. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377; REVIEW_WORK/batch066/source07-08-10/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object for ordinary07/10; labels and supplied forms assessed independently. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:2509; REVIEW_WORK/batch066/source07-08-10/chebi2509.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object for ordinary07/10; labels and supplied forms assessed independently. |
| quantities | REVIEW_WORK/batch066/record07/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch066/record07/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch066/record07/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch066/record07/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch066/record07/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch066/record07/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch066/record07/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch066/record07/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch066/record07/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch066/record07/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch066/record07/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- No operational detail beyond this exact generic source is proposed; no strain growth assertion.
- The primary source makes up the filtered extract before agar addition. Its final solid-medium volume, retained extract yield and any additional make-up-water amount remain unspecified.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T122329Z-culturemech-001794-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: COW MANURE AGAR'
started_at: '2026-10-28T12:02:49.854477Z'
finished_at: '2026-10-28T12:23:29.927443Z'
reviewer:
  identity: Codex tsb_source_check
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Read-only independent review of maintained source records, fresh
    sources and original diagnostics.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: The maintained owner already separates extraction inputs from prepared extract
  and retains authenticated agar evidence. The generated target is stale and still
  mislabels mechanical cloth/paper filtration as sterile filtration. One major generated-boundary
  finding and one minor classifier finding require bounded follow-up; all native diagnostics
  passed without establishing source truth.
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
  - path: data/merge_yaml/merged/COW_MANURE_AGAR.yaml
    sha256: e413f52b24f85d2fbd3b9c027d7532710ef5ef77d72286de96f25da98fc5bd27
    role: target
  - path: data/normalized_yaml/bacterial/cow_manure_agar.yaml
    sha256: 0f25051dad672e09b6b25f3de36a6f225763127edbdd59e89c1a11ece118a2ee
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
  - path: reports/ingredient_concentration_curation/20261007-extraction-boundaries/657.md
    sha256: 902e05d563f0fbbb447ccac1ebd044b0767157f1b6459ac3fa0721c28902deb7
    role: context
  - path: reports/ingredient_concentration_curation/20261007-extraction-boundaries/README.md
    sha256: 7472ab1559ad68445c76e0251ac7b86382edae2762f4d25b8248bb9bd72befcb
    role: context
  - path: reports/ingredient_concentration_curation/20261007-extraction-boundaries/plan.json
    sha256: 2d036c265c2c608a6fe382dbf55650e31412c395fea4325be0b9681d70fb5586
    role: context
  - path: reports/ingredient_concentration_curation/20261007-extraction-boundaries/validation.json
    sha256: 0f952b47f08f50d8347ccc28ef25c2f688f3fab834218176407a7aef106a482f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
    sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/cow_manure_agar.yaml.md
    sha256: 682366d991d440963aabbeff81e28bbc00d911ebe24f69b8871eaee9067e83af
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/COW_MANURE_AGAR.md
    sha256: 7f9ef6700e4ed228a54990df2e667c2ac734345b68fb73d607a7ca4c918d878e
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cow_manure_agar.md
    sha256: 26a685822397825becdd55a46389b2e1647b3655ba7fcaf14d58365230e669b1
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
  - path: scripts/migrate_ph_range.py
    sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
    role: context
  - path: scripts/record_io.py
    sha256: bff4715f85d7ff2ff681b88f0a2de2667e5767d7a2c196bd50a37d5d329957ac
    role: context
  - path: scripts/refill_term_labels.py
    sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
    role: context
  - path: scripts/remove_invalid_chebi_ids.py
    sha256: a6c2f7577812081230fd5fe008182c09eace4ef7818857f8026ec8d5e0b760e0
    role: context
  - path: scripts/repair_extraction_input_boundaries.py
    sha256: 6cf990762220c590e897731d91aafe229781c57fd707d4941ac1b37c20b125eb
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/repair_reviewed_medium_stock_boundaries.py
    sha256: fafff4038667c35c62bc6c146996d89f67c724fd3d40d3c9f4c0bc320bb599da
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
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
  selection: Authoritative batch066 index 07
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001794
targets:
- target_id: CultureMech:001794
  path: data/merge_yaml/merged/COW_MANURE_AGAR.yaml
  label: cow_manure_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cow_manure_agar.yaml
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
  - CultureMech:001794
  command: just validate-schema data/merge_yaml/merged/COW_MANURE_AGAR.yaml
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
  - CultureMech:001794
  command: just validate-strict data/merge_yaml/merged/COW_MANURE_AGAR.yaml --out
    REVIEW_WORK/batch066/record07/strict.tsv --workers 1 --quiet
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
  - CultureMech:001794
  command: just validate-terms data/merge_yaml/merged/COW_MANURE_AGAR.yaml
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
  - CultureMech:001794
  command: just validate-references data/merge_yaml/merged/COW_MANURE_AGAR.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsm657
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf
  accessed_at: '2026-10-28T12:03:13.855084Z'
  locator: REVIEW_WORK/batch066/source07-08-10/dsm657.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: 07 exact primary recipe and extraction-stage evidence.
  snapshot_sha256: eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930
- evidence_id: api657
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/657
  accessed_at: '2026-10-28T12:03:13.491521Z'
  locator: REVIEW_WORK/batch066/source07-08-10/api657.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: 07 exact current provider recipe and stage objects.
  snapshot_sha256: 298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/COW_MANURE_AGAR.yaml
  locator: Complete file
  accessed_at: '2026-10-28T12:08:07.995764Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: e413f52b24f85d2fbd3b9c027d7532710ef5ef77d72286de96f25da98fc5bd27
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/cow_manure_agar.yaml
  locator: Complete file
  accessed_at: '2026-10-28T12:08:07.995925Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 0f25051dad672e09b6b25f3de36a6f225763127edbdd59e89c1a11ece118a2ee
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T12:08:07.995956Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T12:08:07.996247Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T12:08:07.996268Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T12:08:07.996289Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-17
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-extraction-boundaries/657.md
  locator: Complete report
  accessed_at: '2026-10-28T12:08:07.996312Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 902e05d563f0fbbb447ccac1ebd044b0767157f1b6459ac3fa0721c28902deb7
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-extraction-boundaries/README.md
  locator: Complete report
  accessed_at: '2026-10-28T12:08:07.996336Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 7472ab1559ad68445c76e0251ac7b86382edae2762f4d25b8248bb9bd72befcb
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-extraction-boundaries/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T12:08:07.996356Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 2d036c265c2c608a6fe382dbf55650e31412c395fea4325be0b9681d70fb5586
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-extraction-boundaries/validation.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T12:08:07.996398Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 0f952b47f08f50d8347ccc28ef25c2f688f3fab834218176407a7aef106a482f
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T12:08:07.996419Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/cow_manure_agar.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T12:08:08.002965Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 682366d991d440963aabbeff81e28bbc00d911ebe24f69b8871eaee9067e83af
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/COW_MANURE_AGAR.md
  locator: Complete report
  accessed_at: '2026-10-28T12:08:08.003006Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 7f9ef6700e4ed228a54990df2e667c2ac734345b68fb73d607a7ca4c918d878e
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cow_manure_agar.md
  locator: Complete report
  accessed_at: '2026-10-28T12:08:08.003032Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 26a685822397825becdd55a46389b2e1647b3655ba7fcaf14d58365230e669b1
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch066/record07/historical-reading.json
  accessed_at: '2026-10-28T12:08:08.003061Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: e1c8e1015c690501d7a246a09cb25cd2228900a19f9491d6a6ace3b61f660efd
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch066/record07/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T12:08:08.003103Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 0ae82d79595ae4ca2c8b25d4db41433f8945e1fdc9fbb9686d6ea0bdd4ab4a01
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch066/record07/complete-document-reader.json
  accessed_at: '2026-10-28T12:08:08.003143Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: d8046237c6250ef90adf161bcb00768661108159234eeb9a2f687f29d38ab1cb
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T12:08:08.003173Z'
  support: context_only
  summary: Current parser keeps only primary compounds and separately preserves referenced
    stocks. It still prioritizes provider g_l and normalizes bare g/ml/% to per-litre/w-v
    enums without independently establishing the basis; the action classifier tests
    temperature before cool. Current behavior is not historical execution proof.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T12:08:08.003206Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer-extraction
  kind: record_content
  reference: scripts/repair_extraction_input_boundaries.py
  locator: COHORT[657], build, process
  accessed_at: '2026-10-28T12:08:08.003230Z'
  support: context_only
  summary: 'Full build and process source read: exact657/API/PDF/historical-plan guards
    separate starting solids and water from made-up extract, retain agar and literal
    evidence, and append the supplied curation event. Current code is not proof of
    the historical execution.'
  snapshot_sha256: 6cf990762220c590e897731d91aafe229781c57fd707d4941ac1b37c20b125eb
- evidence_id: inspection-addendum
  kind: record_content
  reference: REVIEW_WORK/batch066/record07/inspection-addendum-extraction-report/lineage.json
  locator: Exact original→effective inspection lineage
  accessed_at: '2026-10-28T12:08:08.003262Z'
  support: supports
  summary: Four exact extraction follow-up inputs added; original50 inputs and selected
    target/owner unchanged. Original canonical checks reused without rerun.
  snapshot_sha256: 1fbc64af4a5a6ab81624dd3a3289edeb2f2d550de488b809bf59e9ade60e458c
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377
  accessed_at: '2026-10-28T12:04:03.619664Z'
  locator: REVIEW_WORK/batch066/source07-08-10/chebi15377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object for ordinary07/10; labels and supplied forms
    assessed independently.
  snapshot_sha256: a5ab66402b598c137daa8e5c8ba95811f1619db3e0f8b4f9bd0214161bafa0fe
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:2509
  accessed_at: '2026-10-28T12:04:04.857038Z'
  locator: REVIEW_WORK/batch066/source07-08-10/chebi2509.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object for ordinary07/10; labels and supplied forms
    assessed independently.
  snapshot_sha256: e3f17ac3223021a957a5e3fffb5b118a0854f9ddbc537f51f70dd61ae23ff7a7
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch066/record07/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T12:08:08.032134Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 45733334077e5c9d53a9b5fabcc01ca37e89d502118e7c0de97ac515851cbe69
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch066/record07/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T12:08:08.032180Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 78ebc29192d304a8ab0cf2b4aa31f96bc584dcb1a72d9080b2e4afd44a24951b
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch066/record07/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T12:08:08.032209Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: de657685b3dc4e886c639d988a98c9d99fce38fa5d02ed1ecef16c83a538110f
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch066/record07/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T12:08:08.032244Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 08879fd9ecf2e462dc480c69d37c7f8bce4b4a642eff0c389b4b97a6961a2fb3
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch066/record07/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T12:08:08.032281Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 7d26b4f382e66ff36c0addc5eec87f1db8bbed35205d497e41c509b55ebc30bd
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch066/record07/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T12:08:08.032306Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 65721e052e8b243fb12e77f2aa0a1d8926fb5b4ad3c1764286fd45d29c169a45
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch066/record07/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T12:08:08.032327Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 5eaab5ab67e07eeb5c7925889ee34c0ede30d022bab607099f33edd6cf18957a
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch066/record07/schema-result.json
  accessed_at: '2026-10-28T12:02:51.193738Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 0817dcee9983c57bb14e087e753510e7920d0c1a822e1ff20a6b933a134930c5
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch066/record07/strict-result.json
  accessed_at: '2026-10-28T12:02:52.196194Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 4bf986c487c0ccc1cf2e0bc35edbdecfc4e6d17499eedb7afc04aaf722f42064
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch066/record07/terms-result.json
  accessed_at: '2026-10-28T12:02:53.710352Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 012fe524a3ced840945187467da7fce7cbcc8a20204f9416f4903c24a876744d
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch066/record07/references-result.json
  accessed_at: '2026-10-28T12:02:54.497802Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 8dff90c4627e50f9fd3501ad5722d5138553e3819709d3f4b79596ebf1025d25
assessments:
- assessment_id: identity
  area: identity
  topic: Exact DSM657 identity
  outcome: supported
  summary: Stable target/owner identity, declared DSM657 source and current API657/PDF
    title agree. The source supplies no strain or organism-specific growth claim.
  target_ids:
  - CultureMech:001794
  evidence_ids:
  - target
  - owner
  - api657
  - dsm657
- assessment_id: preparation
  area: representation
  topic: Extraction and processing scope
  outcome: concern
  summary: Full primary PDF page visually read. The owner preserves all ordered extraction
    instructions and supported make-up; the generated action code overstates filtration.
    Source does not specify pH, autoclave conditions or extraction yield, so none
    is supplied.
  target_ids:
  - CultureMech:001794
  evidence_ids:
  - dsm657
  - api657
  - owner
  - writer-mediadive
- assessment_id: schema
  area: schema
  topic: Native structure and selected ownership
  outcome: supported
  summary: Original schema, strict and terms passed; reference validator performed
    zero checks. The append-only inspection preserves all original inputs and adds
    exact extraction report context; these diagnostics do not establish scientific
    correctness.
  target_ids:
  - CultureMech:001794
  evidence_ids:
  - inspection-addendum
  - target
  - owner
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 6 current concentration fields are covered by 9 decisions, including unchanged
    support and explicit source-only conditions.
  target_ids:
  - CultureMech:001794
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b066-quantity-inventory-v1","target":"data/merge_yaml/merged/COW_MANURE_AGAR.yaml","quantity_field_count":6,"decisions":[{"quantity_id":"q1","label":"Generated
    dry manure concentration","local_fields":[{"path":"data/merge_yaml/merged/COW_MANURE_AGAR.yaml","field_path":"ingredients[0].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source50g is extraction starting material. Filtration removes solids; it does
    not establish50g/L retained dissolved material. Withdraw the generated final-ingredient
    concentration and preserve the already curated owner extraction-input note without
    inventing yield.","source_stage":"Extraction input, not recovered solute","sources":[{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Dry cow-manure\",\n                        \"compound_id\":
    2131,\n                        \"amount\": 50,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 50,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour.
    Filter, first through cheesecloth and then paper. Make up volume to one liter.
    Add 20 g agar.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm657","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf","raw_path":"REVIEW_WORK/batch066/source07-08-10/dsm657.raw","raw_sha256":"eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930","text_sha256":"26a804b7f79cc60399495c0ec3a8e7564ae7dfeff54f20e3cfb5e9efa544beba","accessed_at":"2026-10-28T12:03:13.855084Z","locator":"dsm657.txt
    lines 3-4","quote":"Suspend 50 g of dry cow-manure in one liter of tap water.
    Boil for one hour. Filter, first\nthrough cheesecloth and then paper. Make up
    volume to one liter. Add 20 g agar.","quote_basis":"derivative text"}]},{"quantity_id":"q2","label":"Generated
    tap water mass concentration","local_fields":[{"path":"data/merge_yaml/merged/COW_MANURE_AGAR.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1000","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source1000ml
    is1L initial water; no density or mass concentration is given. Credit the current
    owner absolute-volume repair and separate the later make-up.","source_stage":"Initial
    extraction solvent","sources":[{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Tap water\",\n                        \"compound_id\":
    322,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour.
    Filter, first through cheesecloth and then paper. Make up volume to one liter.
    Add 20 g agar.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm657","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf","raw_path":"REVIEW_WORK/batch066/source07-08-10/dsm657.raw","raw_sha256":"eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930","text_sha256":"26a804b7f79cc60399495c0ec3a8e7564ae7dfeff54f20e3cfb5e9efa544beba","accessed_at":"2026-10-28T12:03:13.855084Z","locator":"dsm657.txt
    lines 3-4","quote":"Suspend 50 g of dry cow-manure in one liter of tap water.
    Boil for one hour. Filter, first\nthrough cheesecloth and then paper. Make up
    volume to one liter. Add 20 g agar.","quote_basis":"derivative text"}]},{"quantity_id":"q3","label":"Generated
    agar concentration","local_fields":[{"path":"data/merge_yaml/merged/COW_MANURE_AGAR.yaml","field_path":"ingredients[2].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Source20g
    is added after filtered extract is made up to1L.20g/L is supported on this explicitly
    prepared extract basis; the target lacks the owner attached evidence and basis
    note. This is not a measured final agar-medium volume.","source_stage":"Agar per
    made-up extract","sources":[{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"amount\": 20,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\":
    59.4654,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour.
    Filter, first through cheesecloth and then paper. Make up volume to one liter.
    Add 20 g agar.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm657","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf","raw_path":"REVIEW_WORK/batch066/source07-08-10/dsm657.raw","raw_sha256":"eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930","text_sha256":"26a804b7f79cc60399495c0ec3a8e7564ae7dfeff54f20e3cfb5e9efa544beba","accessed_at":"2026-10-28T12:03:13.855084Z","locator":"dsm657.txt
    lines 3-4","quote":"Suspend 50 g of dry cow-manure in one liter of tap water.
    Boil for one hour. Filter, first\nthrough cheesecloth and then paper. Make up
    volume to one liter. Add 20 g agar.","quote_basis":"derivative text"}]},{"quantity_id":"q4","label":"Owner
    retained agar concentration and basis","local_fields":[{"path":"data/normalized_yaml/bacterial/cow_manure_agar.yaml","field_path":"ingredients[0].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cow_manure_agar.yaml","field_path":"ingredients[0].notes","stored":"20
    g added after the filtered extract is made up to one liter; no soil/manure concentration
    or extraction yield is inferred."}],"decision":"verified","rationale":"The retained20g/L
    and exact extract-stage note match primary/API text and the attached literal claim/current
    raw digest. No whole manure yield or final-medium volume inferred.","source_stage":"Agar
    per made-up extract","sources":[{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"amount\": 20,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\":
    59.4654,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour.
    Filter, first through cheesecloth and then paper. Make up volume to one liter.
    Add 20 g agar.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm657","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf","raw_path":"REVIEW_WORK/batch066/source07-08-10/dsm657.raw","raw_sha256":"eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930","text_sha256":"26a804b7f79cc60399495c0ec3a8e7564ae7dfeff54f20e3cfb5e9efa544beba","accessed_at":"2026-10-28T12:03:13.855084Z","locator":"dsm657.txt
    lines 3-4","quote":"Suspend 50 g of dry cow-manure in one liter of tap water.
    Boil for one hour. Filter, first\nthrough cheesecloth and then paper. Make up
    volume to one liter. Add 20 g agar.","quote_basis":"derivative text"}]},{"quantity_id":"q5","label":"Owner
    initial extraction water","local_fields":[{"path":"data/normalized_yaml/bacterial/cow_manure_agar.yaml","field_path":"solutions[0].composition[1].concentration","stored":{"value":"1","unit":"L"}},{"path":"data/normalized_yaml/bacterial/cow_manure_agar.yaml","field_path":"solutions[0].composition[1].notes","stored":"Initial
    extraction-water addition: 1000 ml / 1000 ml per L = 1 L, not a mass concentration
    or a measured recovered volume. The later make-up to one liter is a separate final-volume
    instruction; its additional water amount is unspecified."}],"decision":"verified","rationale":"1000ml/1000ml
    per L=1L. The owner explicitly distinguishes initial water from later make-up
    and has matching attached source evidence.","source_stage":"Initial extraction
    solvent","sources":[{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Tap water\",\n                        \"compound_id\":
    322,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour.
    Filter, first through cheesecloth and then paper. Make up volume to one liter.
    Add 20 g agar.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm657","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf","raw_path":"REVIEW_WORK/batch066/source07-08-10/dsm657.raw","raw_sha256":"eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930","text_sha256":"26a804b7f79cc60399495c0ec3a8e7564ae7dfeff54f20e3cfb5e9efa544beba","accessed_at":"2026-10-28T12:03:13.855084Z","locator":"dsm657.txt
    lines 3-4","quote":"Suspend 50 g of dry cow-manure in one liter of tap water.
    Boil for one hour. Filter, first\nthrough cheesecloth and then paper. Make up
    volume to one liter. Add 20 g agar.","quote_basis":"derivative text"}]},{"quantity_id":"q6","label":"Owner
    made-up recovered extract","local_fields":[{"path":"data/normalized_yaml/bacterial/cow_manure_agar.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"L"}},{"path":"data/normalized_yaml/bacterial/cow_manure_agar.yaml","field_path":"solutions[0].notes","stored":"Curator-described
    extraction stage, not a separately accessioned stock. Composition lists preparation
    inputs, not retained solutes. The filtered extract is made up to one liter before
    agar is added. This is the prepared extract volume, not an extraction yield or
    a final agar-medium volume measurement."}],"decision":"verified","rationale":"The
    source explicitly instructs make-up to one liter after cloth/paper filtration.
    The owner1L describes prepared extract, with matching root evidence; it is neither
    extraction yield nor measured final agar-medium volume.","source_stage":"Made-up
    extract","sources":[{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour.
    Filter, first through cheesecloth and then paper. Make up volume to one liter.
    Add 20 g agar.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm657","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf","raw_path":"REVIEW_WORK/batch066/source07-08-10/dsm657.raw","raw_sha256":"eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930","text_sha256":"26a804b7f79cc60399495c0ec3a8e7564ae7dfeff54f20e3cfb5e9efa544beba","accessed_at":"2026-10-28T12:03:13.855084Z","locator":"dsm657.txt
    lines 3-4","quote":"Suspend 50 g of dry cow-manure in one liter of tap water.
    Boil for one hour. Filter, first\nthrough cheesecloth and then paper. Make up
    volume to one liter. Add 20 g agar.","quote_basis":"derivative text"}]},{"quantity_id":"q7","label":"Owner
    starting manure mass and unquantified yield","local_fields":[{"path":"data/normalized_yaml/bacterial/cow_manure_agar.yaml","field_path":"solutions[0].composition[0].notes","stored":"Extraction
    starting material: 50 g in 1000 ml tap water. Solids are separated before the
    recovered extract is used. The source does not quantify retained solids or dissolved
    yield; no numeric extract concentration is asserted."}],"decision":"verified","rationale":"The
    attached source authenticates the retained50g starting-input note. Absence of
    a numerical concentration is intentional: no retained-solids or dissolved yield
    is supplied.","source_stage":"Extraction input only","sources":[{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Dry cow-manure\",\n                        \"compound_id\":
    2131,\n                        \"amount\": 50,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 50,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour.
    Filter, first through cheesecloth and then paper. Make up volume to one liter.
    Add 20 g agar.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm657","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf","raw_path":"REVIEW_WORK/batch066/source07-08-10/dsm657.raw","raw_sha256":"eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930","text_sha256":"26a804b7f79cc60399495c0ec3a8e7564ae7dfeff54f20e3cfb5e9efa544beba","accessed_at":"2026-10-28T12:03:13.855084Z","locator":"dsm657.txt
    lines 3-4","quote":"Suspend 50 g of dry cow-manure in one liter of tap water.
    Boil for one hour. Filter, first\nthrough cheesecloth and then paper. Make up
    volume to one liter. Add 20 g agar.","quote_basis":"derivative text"}]},{"quantity_id":"q8","label":"Complete
    generated preparation and owner separated stages","local_fields":[{"path":"data/merge_yaml/merged/COW_MANURE_AGAR.yaml","field_path":"preparation_steps[0].description","stored":"Suspend
    50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first
    through cheesecloth and then paper. Make up volume to one liter. Add 20 g agar."},{"path":"data/normalized_yaml/bacterial/cow_manure_agar.yaml","field_path":"solutions[0].preparation_notes","stored":"Suspend
    50 g of dry cow-manure in one liter of tap water. Boil for one hour. Filter, first
    through cheesecloth and then paper. Make up volume to one liter."},{"path":"data/normalized_yaml/bacterial/cow_manure_agar.yaml","field_path":"preparation_steps[0].description","stored":"Add
    20 g agar."}],"decision":"mixed","rationale":"All source instructions, including
    one-hour boiling, cloth then paper filtration, make-up and agar addition, remain
    in the generated prose and the two owner stages. Owner descriptions and root claim
    are verified; generated description is evidence_only. Its FILTER_STERILIZE action
    is addressed separately: mechanical filtration is not proof of sterility.","source_stage":"Ordered
    extraction and agar addition","sources":[{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour.
    Filter, first through cheesecloth and then paper. Make up volume to one liter.
    Add 20 g agar.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm657","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf","raw_path":"REVIEW_WORK/batch066/source07-08-10/dsm657.raw","raw_sha256":"eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930","text_sha256":"26a804b7f79cc60399495c0ec3a8e7564ae7dfeff54f20e3cfb5e9efa544beba","accessed_at":"2026-10-28T12:03:13.855084Z","locator":"dsm657.txt
    lines 3-4","quote":"Suspend 50 g of dry cow-manure in one liter of tap water.
    Boil for one hour. Filter, first\nthrough cheesecloth and then paper. Make up
    volume to one liter. Add 20 g agar.","quote_basis":"derivative text"}]},{"quantity_id":"q9","label":"Unspecified
    additional make-up water","local_fields":[],"decision":"not_quantified","rationale":"The
    source supplies the target extract volume, not the additional amount of water
    required after boiling and filtration. No numerical top-up is proposed.","source_stage":"Post-filtration
    make-up","sources":[{"evidence_id":"api657","reference":"https://mediadive.dsmz.de/rest/medium/657","raw_path":"REVIEW_WORK/batch066/source07-08-10/api657.raw","raw_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","text_sha256":"298ab9f3b5f727ef04f3a45fcaae53e690570b92c7e42e5db332d98144c0ea51","accessed_at":"2026-10-28T12:03:13.491521Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Suspend 50 g of dry cow-manure in one liter of tap water. Boil for one hour.
    Filter, first through cheesecloth and then paper. Make up volume to one liter.
    Add 20 g agar.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm657","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf","raw_path":"REVIEW_WORK/batch066/source07-08-10/dsm657.raw","raw_sha256":"eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930","text_sha256":"26a804b7f79cc60399495c0ec3a8e7564ae7dfeff54f20e3cfb5e9efa544beba","accessed_at":"2026-10-28T12:03:13.855084Z","locator":"dsm657.txt
    lines 3-4","quote":"Suspend 50 g of dry cow-manure in one liter of tap water.
    Boil for one hour. Filter, first\nthrough cheesecloth and then paper. Make up
    volume to one liter. Add 20 g agar.","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/COW_MANURE_AGAR.yaml":null,"data/normalized_yaml/bacterial/cow_manure_agar.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: supported
  summary: All eight existing CHEBI slots across target and owner are exact current
    water/agar labels. Both two-of-three ingredient-instance secondary-link populations
    are reported separately; manure is an undefined mixture and not forced to a chemical
    ID. Current MIM rows are local snapshot evidence, not source recipe or historical
    legacy-ID certification. Tap-water qualification is retained; CHEBI water does
    not specify water grade.
  target_ids:
  - CultureMech:001794
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: The two actual owner concentration/extraction events are credited. Four
    attached literal API claims and their stated raw digest are independently checked
    against current bytes, and the historical PDF digest is compared separately. Current
    equal bytes do not reconstruct the old retrieval event. Historical reports and
    exact selected plan rows remain derivative provenance. Current extraction repair
    code and conservative merger are read; no old execution is inferred.
  target_ids:
  - CultureMech:001794
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-001794-generated-extraction-staleness
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Generated record omits the maintained extraction repair
  description: The target still treats starting manure and tap water as finished-medium
    mass concentrations and lacks the owner extraction structure and four scoped evidence
    claims. The current owner has already removed the unsupported manure concentration,
    represents initial water and made-up extract separately in L, and retains supported
    agar on the prepared-extract basis. Regenerate from that exact owner and preserve
    its source-stage notes/evidence; do not repeat the obsolete concentration proposals.
    Current singleton merger copies the maintained record, and the current multi-record
    merge gate requires full formulation equality.
  target_ids:
  - CultureMech:001794
  field_paths:
  - ingredients
  - solutions
  - evidence
  - references
  - curation_history
  evidence_ids:
  - target
  - owner
  - api657
  - dsm657
  - writer-extraction
  - writer-formulation
  - writer-merger
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cow_manure_agar.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-001794-mechanical-filtration-classifier
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Mechanical filtration is classified as sterile filtration
  description: The target preparation_steps[0].action is FILTER_STERILIZE although
    the exact source specifies cloth and paper filtration. The current owner already
    separates extraction notes from ADD_AGAR and makes no sterility claim. For this
    cloth/paper sentence, the current classifier reaches the filter branch and returns
    FILTER_STERILIZE; the preceding autoclave/steam-sterilization branch does not
    apply. Guard the writer for this mechanical extraction language. This current-code
    observation is not evidence that this exact revision produced the historical target.
  target_ids:
  - CultureMech:001794
  field_paths:
  - preparation_steps[0].action
  evidence_ids:
  - target
  - owner
  - dsm657
  - api657
  - writer-mediadive
  rule_id: review-yaml-record/representation
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cow_manure_agar.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: scoped dependency
actions:
- action_id: a1
  description: The target still treats starting manure and tap water as finished-medium
    mass concentrations and lacks the owner extraction structure and four scoped evidence
    claims. The current owner has already removed the unsupported manure concentration,
    represents initial water and made-up extract separately in L, and retains supported
    agar on the prepared-extract basis. Regenerate from that exact owner and preserve
    its source-stage notes/evidence; do not repeat the obsolete concentration proposals.
    Current singleton merger copies the maintained record, and the current multi-record
    merge gate requires full formulation equality.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001794
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cow_manure_agar.yaml
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
  description: The target preparation_steps[0].action is FILTER_STERILIZE although
    the exact source specifies cloth and paper filtration. The current owner already
    separates extraction notes from ADD_AGAR and makes no sterility claim. For this
    cloth/paper sentence, the current classifier reaches the filter branch and returns
    FILTER_STERILIZE; the preceding autoclave/steam-sterilization branch does not
    apply. Guard the writer for this mechanical extraction language. This current-code
    observation is not evidence that this exact revision produced the historical target.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001794
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cow_manure_agar.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: scoped dependency
  acceptance_checks:
  - Preserve the exact extraction and agar descriptions without asserting sterile
    filtration. Keep the already repaired owner unchanged unless a separately justified
    curation is needed.
  - Test the current classifier against this exact cloth/paper sentence and true sterile-filter
    instructions; regenerate and verify the selected target from its maintained owner.
  generator: Maintained-input curation and repository merge regeneration
limitations:
- No operational detail beyond this exact generic source is proposed; no strain growth
  assertion.
- The primary source makes up the filtered extract before agar addition. Its final
  solid-medium volume, retained extract yield and any additional make-up-water amount
  remain unspecified.
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
