# Scientific review: CMA

- Review: 20261028T111223Z-culturemech-000061-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T10:59:45.034265Z
- Finished UTC: 2026-10-28T11:12:23.617558Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

CMA’s three per-litre input rates are supported unchanged, but generated preparation/source loss, whole-premix grounding as agar, and unsupported generic growth defaults require curation. Existing owner repairs and equal historical API content are credited with their exact limits.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch064 index 09
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000061 | data/merge_yaml/merged/CMA.yaml | generated | cma |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:000061 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:000061 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:000061 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:000061 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### CCAP CMA and C24 source correspondence

identity: supported. Targets: CultureMech:000061.

The current CCAP PDF is CMA (Corn Meal Glucose Agar), Revision002 approved29May2026, with Freshwater Protozoa scope. API C24 identifies CCAP and the exact same PDF URL. Both maintained owners denote that source identity despite incompatible current representation.

### Complex composition and physical form

consistency: concern. Targets: CultureMech:000061.

COMPLEX/UNDEFINED is supported by premix and yeast extract. The source describes molten agar; LIQUID and generic algae-growth guidance in the generated/algae layers need scoped correction. No specific target organism or strain is inferred.

### Canonical diagnostics

schema: supported. Targets: CultureMech:000061.

All four diagnostics passed once; strict had zero errors and references performed zero checks. Passing structure does not verify the source-supported identity or repair lost scientific content.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:000061.

9 current concentration fields are covered by 10 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b064-quantity-inventory-v1","target":"data/merge_yaml/merged/CMA.yaml","quantity_field_count":9,"decisions":[{"quantity_id":"q1","label":"Corn meal agar","local_fields":[{"path":"data/merge_yaml/merged/CMA.yaml","field_path":"ingredients[0].concentration","stored":{"value":"17.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/algae/cma.yaml","field_path":"ingredients[0].concentration","stored":{"value":"17.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cma.yaml","field_path":"ingredients[0].concentration","stored":{"value":"17","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"CCAP explicitly labels the table per litre, independently corroborated by the exact provider g_l row. The existing value is supported unchanged, but no attached literal concentration evidence exists. For the first row the amount refers to the whole corn-meal agar premix, not pure agar.","source_stage":"CCAP whole-medium explicit per-litre table","sources":[{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt lines 11-11","quote":"Medium                                                                   per litre","quote_basis":"derivative text"},{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt lines 13-13","quote":"Corn meal agar                                                17.0 g","quote_basis":"derivative text"},{"evidence_id":"apiC24","reference":"https://mediadive.dsmz.de/rest/medium/C24","raw_path":"REVIEW_WORK/batch064/source08-10/apiC24.raw","raw_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","text_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","accessed_at":"2026-10-28T11:00:16.550303Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Corn meal agar\",\n                        \"compound_id\": 702,\n                        \"attribute\": \"Oxoid CM103\",\n                        \"amount\": 17,\n                        \"unit\": \"g\",\n                        \"g_l\": 17,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"D-glucose","local_fields":[{"path":"data/merge_yaml/merged/CMA.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/algae/cma.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cma.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"CCAP explicitly labels the table per litre, independently corroborated by the exact provider g_l row. The existing value is supported unchanged, but no attached literal concentration evidence exists. For the first row the amount refers to the whole corn-meal agar premix, not pure agar.","source_stage":"CCAP whole-medium explicit per-litre table","sources":[{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt lines 11-11","quote":"Medium                                                                   per litre","quote_basis":"derivative text"},{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt lines 14-14","quote":"D-glucose                                                     2.0 g","quote_basis":"derivative text"},{"evidence_id":"apiC24","reference":"https://mediadive.dsmz.de/rest/medium/C24","raw_path":"REVIEW_WORK/batch064/source08-10/apiC24.raw","raw_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","text_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","accessed_at":"2026-10-28T11:00:16.550303Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\": 211,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 11.1012,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/CMA.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/algae/cma.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cma.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"CCAP explicitly labels the table per litre, independently corroborated by the exact provider g_l row. The existing value is supported unchanged, but no attached literal concentration evidence exists. For the first row the amount refers to the whole corn-meal agar premix, not pure agar.","source_stage":"CCAP whole-medium explicit per-litre table","sources":[{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt lines 11-11","quote":"Medium                                                                   per litre","quote_basis":"derivative text"},{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt lines 15-15","quote":"Yeast extract                                                 1.0 g","quote_basis":"derivative text"},{"evidence_id":"apiC24","reference":"https://mediadive.dsmz.de/rest/medium/C24","raw_path":"REVIEW_WORK/batch064/source08-10/apiC24.raw","raw_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","text_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","accessed_at":"2026-10-28T11:00:16.550303Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"Oxoid L21\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"Source solvent input","local_fields":[],"decision":"evidence_only","rationale":"API C24 includes an input water volume and CCAP says cold deionised water. Preserve this as preparation context; the three solute rates are already source-explicit per litre and need no inference from this input volume.","source_stage":"Solvent/preparation input","sources":[{"evidence_id":"apiC24","reference":"https://mediadive.dsmz.de/rest/medium/C24","raw_path":"REVIEW_WORK/batch064/source08-10/apiC24.raw","raw_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","text_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","accessed_at":"2026-10-28T11:00:16.550303Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Deionized water\",\n                        \"compound_id\": 418,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt lines 18-20","quote":"Disperse the agar in cold deionised water. Apply heat, stirring constantly. During heating, add\nglucose and yeast extract. Bring contents to boil. Transfer molten agar to suitable vessels.\nSterilise by pressure cooking at 10 psi for 15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q5","label":"Maintained bacterial owner preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/cma.yaml","field_path":"preparation_steps[0].description","stored":"Disperse the agar in cold deionised water. Apply heat, stirring constantly. During heating, add\r\nglucose and yeast extract. Bring contents to boil. Transfer molten agar to suitable vessels.\r\nSterilise by pressure cooking at 10 psi for 15 minutes."}],"decision":"evidence_only","rationale":"The complete maintained description agrees with the source, including 10 psi and 15 minutes. Credit this existing preparation content; HEAT is a coarse action covering a multistage instruction, not evidence that the sterilization text is absent.","source_stage":"Dispersion, heating, addition, transfer and sterilization","sources":[{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt lines 18-20","quote":"Disperse the agar in cold deionised water. Apply heat, stirring constantly. During heating, add\nglucose and yeast extract. Bring contents to boil. Transfer molten agar to suitable vessels.\nSterilise by pressure cooking at 10 psi for 15 minutes.","quote_basis":"derivative text"},{"evidence_id":"apiC24","reference":"https://mediadive.dsmz.de/rest/medium/C24","raw_path":"REVIEW_WORK/batch064/source08-10/apiC24.raw","raw_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","text_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","accessed_at":"2026-10-28T11:00:16.550303Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Disperse the agar in cold deionised water. Apply heat, stirring constantly. During heating, add\\r\\nglucose and yeast extract. Bring contents to boil. Transfer molten agar to suitable vessels.\\r\\nSterilise by pressure cooking at 10 psi for 15 minutes.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"Missing preparation in generated target and algae owner","local_fields":[],"decision":"evidence_only","rationale":"Restore only the exact source-described preparation, crediting the bacterial owner. No pH, incubation temperature or organism-growth regime is supplied in this source.","source_stage":"Source-only preparation for missing layers","sources":[{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt lines 18-20","quote":"Disperse the agar in cold deionised water. Apply heat, stirring constantly. During heating, add\nglucose and yeast extract. Bring contents to boil. Transfer molten agar to suitable vessels.\nSterilise by pressure cooking at 10 psi for 15 minutes.","quote_basis":"derivative text"},{"evidence_id":"apiC24","reference":"https://mediadive.dsmz.de/rest/medium/C24","raw_path":"REVIEW_WORK/batch064/source08-10/apiC24.raw","raw_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","text_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","accessed_at":"2026-10-28T11:00:16.550303Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Disperse the agar in cold deionised water. Apply heat, stirring constantly. During heating, add\\r\\nglucose and yeast extract. Bring contents to boil. Transfer molten agar to suitable vessels.\\r\\nSterilise by pressure cooking at 10 psi for 15 minutes.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"light_intensity","local_fields":[{"path":"data/merge_yaml/merged/CMA.yaml","field_path":"light_intensity","stored":"Varies by species; typically 50-100 µmol photons m⁻² s⁻¹"},{"path":"data/normalized_yaml/algae/cma.yaml","field_path":"light_intensity","stored":"Varies by species; typically 50-100 µmol photons m⁻² s⁻¹"}],"decision":"unsupported","rationale":"These current generic culture ranges are not supported by the complete CCAP recipe or C24 payload. Current CCAP importer inserts these defaults without target-specific evidence. Do not convert their plausibility into a source-specific growth recommendation.","source_stage":"Generic imported growth-condition assertion, not source-certified","sources":[{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt lines 6-20","quote":"CMA (Corn Meal Glucose Agar)\n                                         Freshwater Protozoa\n\n\n\nMedium                                                                   per litre\n\n           Corn meal agar                                                17.0 g\n           D-glucose                                                     2.0 g\n           Yeast extract                                                 1.0 g\n\n\nDisperse the agar in cold deionised water. Apply heat, stirring constantly. During heating, add\nglucose and yeast extract. Bring contents to boil. Transfer molten agar to suitable vessels.\nSterilise by pressure cooking at 10 psi for 15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q8","label":"light_cycle","local_fields":[{"path":"data/merge_yaml/merged/CMA.yaml","field_path":"light_cycle","stored":"Varies by species; commonly 12:12 or 16:8 light:dark"},{"path":"data/normalized_yaml/algae/cma.yaml","field_path":"light_cycle","stored":"Varies by species; commonly 12:12 or 16:8 light:dark"}],"decision":"unsupported","rationale":"These current generic culture ranges are not supported by the complete CCAP recipe or C24 payload. Current CCAP importer inserts these defaults without target-specific evidence. Do not convert their plausibility into a source-specific growth recommendation.","source_stage":"Generic imported growth-condition assertion, not source-certified","sources":[{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt lines 6-20","quote":"CMA (Corn Meal Glucose Agar)\n                                         Freshwater Protozoa\n\n\n\nMedium                                                                   per litre\n\n           Corn meal agar                                                17.0 g\n           D-glucose                                                     2.0 g\n           Yeast extract                                                 1.0 g\n\n\nDisperse the agar in cold deionised water. Apply heat, stirring constantly. During heating, add\nglucose and yeast extract. Bring contents to boil. Transfer molten agar to suitable vessels.\nSterilise by pressure cooking at 10 psi for 15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q9","label":"temperature_range","local_fields":[{"path":"data/merge_yaml/merged/CMA.yaml","field_path":"temperature_range","stored":"15-30°C depending on species"},{"path":"data/normalized_yaml/algae/cma.yaml","field_path":"temperature_range","stored":"15-30°C depending on species"}],"decision":"unsupported","rationale":"These current generic culture ranges are not supported by the complete CCAP recipe or C24 payload. Current CCAP importer inserts these defaults without target-specific evidence. Do not convert their plausibility into a source-specific growth recommendation.","source_stage":"Generic imported growth-condition assertion, not source-certified","sources":[{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt lines 6-20","quote":"CMA (Corn Meal Glucose Agar)\n                                         Freshwater Protozoa\n\n\n\nMedium                                                                   per litre\n\n           Corn meal agar                                                17.0 g\n           D-glucose                                                     2.0 g\n           Yeast extract                                                 1.0 g\n\n\nDisperse the agar in cold deionised water. Apply heat, stirring constantly. During heating, add\nglucose and yeast extract. Bring contents to boil. Transfer molten agar to suitable vessels.\nSterilise by pressure cooking at 10 psi for 15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q10","label":"Whole premix identity compared with manufacturer specification","local_fields":[],"decision":"evidence_only","rationale":"The current official CM0103 specification demonstrates corn-meal extract plus agar as a premix. It is identity context for the API Oxoid CM103 attribute, not an instruction to replace CCAP with the manufacturer preparation, extract an exact historical lot formula, or transfer QC-organism conditions. Keep the whole premix quantity.","source_stage":"Manufacturer composition context only; not added to the medium a second time","sources":[{"evidence_id":"oxoidCM0103","reference":"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0103-V2.pdf","raw_path":"REVIEW_WORK/batch064/source08-10-supplement/oxoidCM0103.raw","raw_sha256":"93926785c704080905aeb5d428a539c28a7431843ead2d2ac393996876cb4b2c","text_sha256":"39e41f18f2ca4309cce75da43942e612a15e97cf7aa9d996497c2cf28b423dbf","accessed_at":"2026-10-28T11:05:20.796307Z","locator":"oxoidCM0103.txt lines 5-14","quote":"OXOID QUALITY ASSURANCE PRODUCT SPECIFICATION\n                                CORN MEAL AGAR CM0103\nCORN MEAL AGAR                                                                       CM0103\n\nTypical Formula*\n\nCorn meal extract (from 50g whole maize) grams per litre                              2.0\nAgar                                                                                 15.0\n\n*adjusted as required to meet performance standards","quote_basis":"derivative text"},{"evidence_id":"apiC24","reference":"https://mediadive.dsmz.de/rest/medium/C24","raw_path":"REVIEW_WORK/batch064/source08-10/apiC24.raw","raw_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","text_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","accessed_at":"2026-10-28T11:00:16.550303Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Corn meal agar\",\n                        \"compound_id\": 702,\n                        \"attribute\": \"Oxoid CM103\",\n                        \"amount\": 17,\n                        \"unit\": \"g\",\n                        \"g_l\": 17,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/CMA.yaml":null,"data/normalized_yaml/algae/cma.yaml":null,"data/normalized_yaml/bacterial/cma.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:000061.

Fresh OLS verifies all three asserted ontology identifiers and canonical labels: CHEBI:2509 agar, CHEBI:17634 D-glucose and FOODON:03315426 yeast extract. Correct labels do not repair the whole-premix versus agar identity mismatch. The exact current MIM snapshot has two secondary links in the bacterial owner and none in the target/algae owner; linkage presence and validity among present slots are separate metrics. No numeric legacy MIM slots are asserted.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:000061.

Four complete prior reports and the exact plan records[422] object were read. Five quoted API objects and the historical raw SHA match the fresh C24 capture exactly; this authenticates current equal content, not a recovered original access event. No attached local ingredient evidence is thereby created. The algae owner’s September source repair and bacterial owner’s full preparation are credited; present merge guards and CCAP generic defaults are direct current-code observations only. The literal batch_process_collection_media curator name was not found in ignored-inclusive scripts/src Python search, so its historical implementation is unresolved.

## Findings

### f1: Generated record drops maintained preparation and source provenance

major / open / confirmed; issue key: culturemech-000061-generated-preparation-staleness.

The generated record takes the algae owner’s LIQUID/default assertions and lacks preparation_steps, while the maintained bacterial C24 owner is SOLID_AGAR and already preserves the complete source preparation. The algae owner now has a structured CCAP sources entry absent from the generated target. Current merger/formulation code rejects incompatible scientific fields; reconcile these exact owners and regenerate without silently discarding their differences. Retain the credited bacterial description, and represent the source-supported agar physical form.

### f2: Corn-meal agar premix is grounded as agar alone

major / open / confirmed; issue key: culturemech-000061-premix-grounding.

All three current documents map the entire Corn meal agar input to CHEBI:2509 agar. The ontology object describes algal polysaccharides, while the provider identifies an Oxoid corn-meal agar product and the official current manufacturer specification describes corn-meal extract plus agar. Preserve the complete premix identity and its supported whole-premix rate; do not equate it with pure agar or duplicate its constituents. No replacement ontology ID or exact historical product-lot expansion is invented.

### f3: Collection membership is overextended into unsupported growth guidance

major / open / confirmed; issue key: culturemech-000061-generic-growth-defaults.

CCAP labels this recipe Freshwater Protozoa. The generated target and algae owner instead advertise algae/phytoplankton use and numeric generic light/temperature ranges not supplied by the recipe. Current ccap_importer.convert_recipe visibly inserts those generic defaults. Retain the exact collection-level source scope without assigning species, strains, a new taxon ID or a universal growth regime. The bacterial category on the other owner is likewise a filing choice, not experimental growth evidence.

### f4: Supported rates and preparation lack attached literal evidence

minor / open / confirmed; issue key: culturemech-000061-field-evidence.

All three per-litre values are directly supported by the current CCAP table and API, but their local source strings and root references are not attached field-specific literal evidence. The older October7 report left them unresolved because it did not establish the collection/link; the fresh PDF/provider join now supports the quantities without rewriting the old report or claiming it already verified them. Attach exact source-stage evidence with present access metadata.

### f5: Current source repair can replace a prior history observation

minor / open / confirmed; issue key: culturemech-000061-append-only-source-history.

The algae owner’s structured-source addition is valid provenance credit. However, the inspected current _ensure_event implementation assigns history[index] when it encounters the same curator/action, replacing prior evidence rather than appending a new correction observation. This is a current writer issue; the review does not claim it was rerun or that a past event was actually destroyed. Preserve the current event and make any future repair append-only.

## Recommended Actions And Acceptance Checks

### a1

The generated record takes the algae owner’s LIQUID/default assertions and lacks preparation_steps, while the maintained bacterial C24 owner is SOLID_AGAR and already preserves the complete source preparation. The algae owner now has a structured CCAP sources entry absent from the generated target. Current merger/formulation code rejects incompatible scientific fields; reconcile these exact owners and regenerate without silently discarding their differences. Retain the credited bacterial description, and represent the source-supported agar physical form.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

All three current documents map the entire Corn meal agar input to CHEBI:2509 agar. The ontology object describes algal polysaccharides, while the provider identifies an Oxoid corn-meal agar product and the official current manufacturer specification describes corn-meal extract plus agar. Preserve the complete premix identity and its supported whole-premix rate; do not equate it with pure agar or duplicate its constituents. No replacement ontology ID or exact historical product-lot expansion is invented.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

CCAP labels this recipe Freshwater Protozoa. The generated target and algae owner instead advertise algae/phytoplankton use and numeric generic light/temperature ranges not supplied by the recipe. Current ccap_importer.convert_recipe visibly inserts those generic defaults. Retain the exact collection-level source scope without assigning species, strains, a new taxon ID or a universal growth regime. The bacterial category on the other owner is likewise a filing choice, not experimental growth evidence.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

All three per-litre values are directly supported by the current CCAP table and API, but their local source strings and root references are not attached field-specific literal evidence. The older October7 report left them unresolved because it did not establish the collection/link; the fresh PDF/provider join now supports the quantities without rewriting the old report or claiming it already verified them. Attach exact source-stage evidence with present access metadata.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

Update scripts/repair_ccap_sources_score10.py::_ensure_event so a future source repair preserves prior curation-history entries and appends a distinct correction observation. Retain the existing owner source evidence. This action concerns the writer and does not request recipe changes or assert a past event was actually destroyed.

- A focused writer check preserves every existing history entry byte-for-byte when the same curator/action already exists and appends a new correction observation with its actual timestamp.
- Retain the existing source-repair identity guards and structured-source evidence; verify that no recipe amount, preparation instruction or source assertion changes as part of this writer correction.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ccapCMA | https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf; REVIEW_WORK/batch064/source08-10/ccapCMA.json; exact original raw/text/hash/time metadata | context_only | 08/09 exact source recipe identity; 10 PubMed/Crossref bibliographic metadata only, operational content excluded. |
| apiC24 | https://mediadive.dsmz.de/rest/medium/C24; REVIEW_WORK/batch064/source08-10/apiC24.json; exact original raw/text/hash/time metadata | context_only | 08/09 exact source recipe identity; 10 PubMed/Crossref bibliographic metadata only, operational content excluded. |
| oxoidCM103 | https://tools.thermofisher.com/content/sfs/brochures/BT-SPEC-0085.pdf; REVIEW_WORK/batch064/source08-10-supplement/oxoidCM103.json; exact original raw/text/hash/time metadata | context_only | Manufacturer identity/composition of the exact Oxoid CM103 premix named by API C24 only; manufacturer QC organism/conditions are excluded and are not transferred to CCAP. |
| oxoidCM0103 | https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0103-V2.pdf; REVIEW_WORK/batch064/source08-10-supplement/oxoidCM0103.json; exact original raw/text/hash/time metadata | context_only | Official current manufacturer premix identity only; no manufacturer QC organism, incubation or preparation transfer to CCAP. Earlier literal CM103 historical-host403 preserved separately. |
| target | data/merge_yaml/merged/CMA.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/algae/cma.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| owner-2 | data/normalized_yaml/bacterial/cma.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| report-18 | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-19 | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/cma.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-20 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CMA.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/algae/cma.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-22 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cma.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch064/record09/historical-reading.json; Complete artifact | context_only | Complete lossless four-report read; three October5 source-incomplete reports and the October7 C24 report. |
| historical-selected-parent-rows | REVIEW_WORK/batch064/record09/historical-selected-parent-rows.json; Complete artifact | context_only | Exact parent plan records[422]; five original snippets join current raw API byte-for-byte. |
| writer-ccap | src/culturemech/import/ccap_importer.py; convert_recipe, _extract_ingredients_from_text, _extract_preparation_from_text | context_only | Current convert_recipe assigns algae/liquid and generic light/temperature/application defaults without recipe-specific evidence. Its PDF extraction is heuristic. This is direct current-code evidence, not historical execution proof. |
| writer-ccap-source | scripts/repair_ccap_sources_score10.py; _require_target, _ensure_source, _ensure_event, repair_record | context_only | Current repair_record validates matching CCAP reference/import IDs, adds structured sources and records a provenance event; _ensure_event replaces a matching prior event instead of appending a new observation. Current owner source repair is credited. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _parse_preparation_steps, _classify_preparation_action | context_only | Current _parse_api_composition retains explicit g_l, excludes solvent rows, and preserves optional flags but does not carry the attribute into ingredient notes. _parse_preparation_steps retains complete text; keyword classification chooses HEAT for this combined instruction. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses exact scientific assertion equality; the two currently incompatible owners must not be silently consolidated. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:2509; REVIEW_WORK/batch064/source08-10/chebi2509.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID/label/scientific object for ordinary08/09 only; no operational grounding review10. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17634; REVIEW_WORK/batch064/source08-10/chebi17634.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID/label/scientific object for ordinary08/09 only; no operational grounding review10. |
| foodon03315426 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON:03315426; REVIEW_WORK/batch064/source08-10/foodon03315426.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID/label/scientific object for ordinary08/09 only; no operational grounding review10. |
| quantities | REVIEW_WORK/batch064/record09/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch064/record09/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch064/record09/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch064/record09/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch064/record09/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch064/record09/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch064/record09/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch064/record09/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch064/record09/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch064/record09/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch064/record09/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- The complete CCAP one-page PDF and complete API were read. Manufacturer CM0103 first-page formula/identity and revision text were read only as premix context; its QC organisms, incubation, pH and sterilization instructions are excluded from this CCAP review. The older exact CM103-host request returned403 and remains preserved.
- Current manufacturer composition is not an authenticated historical product-lot recipe and is not expanded into extra medium ingredients. Source-table per-litre rates need no water-volume inference; no pH or growth conditions are invented.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T111223Z-culturemech-000061-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: CMA'
started_at: '2026-10-28T10:59:45.034265Z'
finished_at: '2026-10-28T11:12:23.617558Z'
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
summary: CMA’s three per-litre input rates are supported unchanged, but generated
  preparation/source loss, whole-premix grounding as agar, and unsupported generic
  growth defaults require curation. Existing owner repairs and equal historical API
  content are credited with their exact limits.
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
  - path: data/merge_yaml/merged/CMA.yaml
    sha256: 6f0ef319f8ef3858c86eb032b669b87b3ffeec6c64c27c7088f8698905671ed8
    role: target
  - path: data/normalized_yaml/algae/cma.yaml
    sha256: acf3a68f763ef74de287d1a2f1d1c0819189ba24fda6facc9e9a37963500d8d1
    role: context
  - path: data/normalized_yaml/bacterial/cma.yaml
    sha256: e27c95d7d89de023a90b707fb00944ec119c162c8efb3ef8409b43160eb6abdd
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json
    sha256: 087b43514367d268b48e568b66203c146b81601303e5c8e3508f3c91e0fcbf26
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/cma.yaml.md
    sha256: 5e69e0b998ba7a388fee9fcbfbb6cf651862df6729c299c6b04c9fe663699c24
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CMA.md
    sha256: 9de22e4fd7459fb8139ea7fdbe0113fc2efb288f8ac536b7edcc3dc3c62d8671
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/algae/cma.md
    sha256: 490d28fd51b0c23b2efb80444b4c28d5fae56232f05e1dc7c47c108b65a7a7fc
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cma.md
    sha256: 51d76fb7a4147ccafd8c827b58633d8ac11089f48ed98b2902fa4800853edc68
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
  - path: scripts/fix_mediadb_leading_compounds.py
    sha256: 2b3b6adfdb298b51b6d87a30151b4f530ac5cd1726fb3763ce7c9fe07cfec729
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
  - path: scripts/repair_ccap_duplicate_compositions.py
    sha256: d6ce21d516f227305d30631f8b04af781946cb40bb87aa8fd0fc47aa5a8caa0c
    role: context
  - path: scripts/repair_ccap_instruction_rows.py
    sha256: eb1a4c8c46eb45dcdde6a5d2f0f6833792dd0802c45603eefa1b63a3ff96fca5
    role: context
  - path: scripts/repair_ccap_missing_compositions.py
    sha256: 84d1ae3d91568fbffc850e88080bdf96fbaad277c3aa61eb371c0da0fc5a2be7
    role: context
  - path: scripts/repair_ccap_sources_score10.py
    sha256: f518688ae99e154f490af337dab30b9038657a814db72861e0b53658a2541ae6
    role: context
  - path: scripts/repair_mediadb_names.py
    sha256: 56ad322b70927ac6dff2de12c63d7bfc640d72a6c2521b55293a788ac3cca4c5
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/import/ccap_importer.py
    sha256: c579c1d8fb62b96e739e5ee5c963453753ebca0bbf50996fb0f0d6eedd75c9ac
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
  selection: Authoritative batch064 index 09
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000061
targets:
- target_id: CultureMech:000061
  path: data/merge_yaml/merged/CMA.yaml
  label: cma
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/cma.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cma.yaml
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
  - CultureMech:000061
  command: just validate-schema data/merge_yaml/merged/CMA.yaml
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
  - CultureMech:000061
  command: just validate-strict data/merge_yaml/merged/CMA.yaml --out REVIEW_WORK/batch064/record09/strict.tsv
    --workers 1 --quiet
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
  - CultureMech:000061
  command: just validate-terms data/merge_yaml/merged/CMA.yaml
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
  - CultureMech:000061
  command: just validate-references data/merge_yaml/merged/CMA.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: ccapCMA
  kind: primary_source
  reference: https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf
  accessed_at: '2026-10-28T11:00:17.065174Z'
  locator: REVIEW_WORK/batch064/source08-10/ccapCMA.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: 08/09 exact source recipe identity; 10 PubMed/Crossref bibliographic metadata
    only, operational content excluded.
  snapshot_sha256: 1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b
- evidence_id: apiC24
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/C24
  accessed_at: '2026-10-28T11:00:16.550303Z'
  locator: REVIEW_WORK/batch064/source08-10/apiC24.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: 08/09 exact source recipe identity; 10 PubMed/Crossref bibliographic metadata
    only, operational content excluded.
  snapshot_sha256: 2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b
- evidence_id: oxoidCM103
  kind: search
  reference: https://tools.thermofisher.com/content/sfs/brochures/BT-SPEC-0085.pdf
  accessed_at: '2026-10-28T11:04:47.552120Z'
  locator: REVIEW_WORK/batch064/source08-10-supplement/oxoidCM103.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Manufacturer identity/composition of the exact Oxoid CM103 premix named
    by API C24 only; manufacturer QC organism/conditions are excluded and are not
    transferred to CCAP.
  snapshot_sha256: 12b791878f05c6838f882197fde0d676ea7d1fe46c34005a8a1646be1c31e5e9
  search_scope: One exact public GET of https://tools.thermofisher.com/content/sfs/brochures/BT-SPEC-0085.pdf;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: oxoidCM0103
  kind: primary_source
  reference: https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0103-V2.pdf
  accessed_at: '2026-10-28T11:05:20.796307Z'
  locator: REVIEW_WORK/batch064/source08-10-supplement/oxoidCM0103.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Official current manufacturer premix identity only; no manufacturer QC
    organism, incubation or preparation transfer to CCAP. Earlier literal CM103 historical-host403
    preserved separately.
  snapshot_sha256: 93926785c704080905aeb5d428a539c28a7431843ead2d2ac393996876cb4b2c
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CMA.yaml
  locator: Complete file
  accessed_at: '2026-10-28T11:06:54.522837Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 6f0ef319f8ef3858c86eb032b669b87b3ffeec6c64c27c7088f8698905671ed8
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/algae/cma.yaml
  locator: Complete file
  accessed_at: '2026-10-28T11:06:54.523013Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: acf3a68f763ef74de287d1a2f1d1c0819189ba24fda6facc9e9a37963500d8d1
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T11:06:54.523042Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T11:06:54.523339Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T11:06:54.523363Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T11:06:54.523385Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/cma.yaml
  locator: Complete file
  accessed_at: '2026-10-28T11:06:54.523409Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: e27c95d7d89de023a90b707fb00944ec119c162c8efb3ef8409b43160eb6abdd
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T11:06:54.523430Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 087b43514367d268b48e568b66203c146b81601303e5c8e3508f3c91e0fcbf26
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/cma.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T11:06:54.528884Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 5e69e0b998ba7a388fee9fcbfbb6cf651862df6729c299c6b04c9fe663699c24
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CMA.md
  locator: Complete report
  accessed_at: '2026-10-28T11:06:54.528940Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 9de22e4fd7459fb8139ea7fdbe0113fc2efb288f8ac536b7edcc3dc3c62d8671
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/algae/cma.md
  locator: Complete report
  accessed_at: '2026-10-28T11:06:54.528966Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 490d28fd51b0c23b2efb80444b4c28d5fae56232f05e1dc7c47c108b65a7a7fc
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cma.md
  locator: Complete report
  accessed_at: '2026-10-28T11:06:54.528988Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 51d76fb7a4147ccafd8c827b58633d8ac11089f48ed98b2902fa4800853edc68
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch064/record09/historical-reading.json
  accessed_at: '2026-10-28T11:06:54.529455Z'
  locator: Complete artifact
  support: context_only
  summary: Complete lossless four-report read; three October5 source-incomplete reports
    and the October7 C24 report.
  snapshot_sha256: 549801a2f1d9ee280e9ac4546a8407dc093072f92c58c8e933af1459c5dddbaa
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch064/record09/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T11:06:54.529498Z'
  locator: Complete artifact
  support: context_only
  summary: Exact parent plan records[422]; five original snippets join current raw
    API byte-for-byte.
  snapshot_sha256: c6daf50f6f3a1cfd594e6001ca468810ff9d99d9e7d1343aad38d9b2c6a26d9f
- evidence_id: writer-ccap
  kind: record_content
  reference: src/culturemech/import/ccap_importer.py
  locator: convert_recipe, _extract_ingredients_from_text, _extract_preparation_from_text
  accessed_at: '2026-10-28T11:06:54.529525Z'
  support: context_only
  summary: Current convert_recipe assigns algae/liquid and generic light/temperature/application
    defaults without recipe-specific evidence. Its PDF extraction is heuristic. This
    is direct current-code evidence, not historical execution proof.
  snapshot_sha256: c579c1d8fb62b96e739e5ee5c963453753ebca0bbf50996fb0f0d6eedd75c9ac
- evidence_id: writer-ccap-source
  kind: record_content
  reference: scripts/repair_ccap_sources_score10.py
  locator: _require_target, _ensure_source, _ensure_event, repair_record
  accessed_at: '2026-10-28T11:06:54.529558Z'
  support: context_only
  summary: Current repair_record validates matching CCAP reference/import IDs, adds
    structured sources and records a provenance event; _ensure_event replaces a matching
    prior event instead of appending a new observation. Current owner source repair
    is credited.
  snapshot_sha256: f518688ae99e154f490af337dab30b9038657a814db72861e0b53658a2541ae6
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _parse_preparation_steps, _classify_preparation_action
  accessed_at: '2026-10-28T11:06:54.529579Z'
  support: context_only
  summary: Current _parse_api_composition retains explicit g_l, excludes solvent rows,
    and preserves optional flags but does not carry the attribute into ingredient
    notes. _parse_preparation_steps retains complete text; keyword classification
    chooses HEAT for this combined instruction.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T11:06:54.529610Z'
  support: context_only
  summary: Current group_formulations uses exact scientific assertion equality; the
    two currently incompatible owners must not be silently consolidated.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:2509
  accessed_at: '2026-10-28T11:00:18.027751Z'
  locator: REVIEW_WORK/batch064/source08-10/chebi2509.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID/label/scientific object for ordinary08/09 only;
    no operational grounding review10.
  snapshot_sha256: e3f17ac3223021a957a5e3fffb5b118a0854f9ddbc537f51f70dd61ae23ff7a7
- evidence_id: chebi17634
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17634
  accessed_at: '2026-10-28T11:00:17.423122Z'
  locator: REVIEW_WORK/batch064/source08-10/chebi17634.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID/label/scientific object for ordinary08/09 only;
    no operational grounding review10.
  snapshot_sha256: 04060738e01fe33b9fc8e5bf54807590127ce391eb8a962d1d013002502169b2
- evidence_id: foodon03315426
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON:03315426
  accessed_at: '2026-10-28T11:00:18.733607Z'
  locator: REVIEW_WORK/batch064/source08-10/foodon03315426.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID/label/scientific object for ordinary08/09 only;
    no operational grounding review10.
  snapshot_sha256: 7812dff5a532367bf78b3a0fa93571cc657e52ec5f4b86f296a4e245aa75ba9b
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch064/record09/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T11:06:54.556291Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 9c6b39d47359d14c3df569d2df40d2fb493cc277866c5cf0e99e74f97a804012
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch064/record09/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T11:06:54.556326Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: eec3ec13238deb8d2e6c5478b6648509e11b19fc8e4e9d552ebed8e06c6c614c
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch064/record09/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T11:06:54.556354Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: bfa6b17f39977afc642eff961b66379cb548e92c2ceea0fcefa7f6f3d0a7be89
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch064/record09/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T11:06:54.556385Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 1472577264c22207972826ff45cae22ad422ed78f61c5a6b8ce8ee8445d7b7fb
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch064/record09/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T11:06:54.556411Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 8c80d5f0d20431073e6491d115d19b47b538b1deb45d31891760d14246bb620b
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch064/record09/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T11:06:54.556431Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 86f4b4d878f6a5d4a7966b3e06aeea1174a8c4dd1c0c6213e9d52835f2fabe09
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch064/record09/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T11:06:54.556449Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch064/record09/schema-result.json
  accessed_at: '2026-10-28T10:59:46.075453Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 0eed031b5f9f98e9da4ecdaf1cea96b1c7f3867df876911dfcef610b870c6218
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch064/record09/strict-result.json
  accessed_at: '2026-10-28T10:59:46.993893Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 03085edf60d99f6f7f6bfc2a06297b06cca1a261deb00c1618fa79c7a4d99453
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch064/record09/terms-result.json
  accessed_at: '2026-10-28T10:59:48.004803Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 66f36f52d7e481d16ce7afb9b9afd95e7914a3f424c6eab3aae6da000818aa89
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch064/record09/references-result.json
  accessed_at: '2026-10-28T10:59:48.645390Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: e048ec04edcd72662a364c579ad56188853e582578aae1d26a428edfd2192208
assessments:
- assessment_id: identity
  area: identity
  topic: CCAP CMA and C24 source correspondence
  outcome: supported
  summary: The current CCAP PDF is CMA (Corn Meal Glucose Agar), Revision002 approved29May2026,
    with Freshwater Protozoa scope. API C24 identifies CCAP and the exact same PDF
    URL. Both maintained owners denote that source identity despite incompatible current
    representation.
  target_ids:
  - CultureMech:000061
  evidence_ids:
  - ccapCMA
  - apiC24
  - target
  - owner
  - owner-2
- assessment_id: classification
  area: consistency
  topic: Complex composition and physical form
  outcome: concern
  summary: COMPLEX/UNDEFINED is supported by premix and yeast extract. The source
    describes molten agar; LIQUID and generic algae-growth guidance in the generated/algae
    layers need scoped correction. No specific target organism or strain is inferred.
  target_ids:
  - CultureMech:000061
  evidence_ids:
  - ccapCMA
  - apiC24
  - target
  - owner-2
- assessment_id: schema
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four diagnostics passed once; strict had zero errors and references
    performed zero checks. Passing structure does not verify the source-supported
    identity or repair lost scientific content.
  target_ids:
  - CultureMech:000061
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 9 current concentration fields are covered by 10 decisions, including unchanged
    support and explicit source-only conditions.
  target_ids:
  - CultureMech:000061
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b064-quantity-inventory-v1","target":"data/merge_yaml/merged/CMA.yaml","quantity_field_count":9,"decisions":[{"quantity_id":"q1","label":"Corn
    meal agar","local_fields":[{"path":"data/merge_yaml/merged/CMA.yaml","field_path":"ingredients[0].concentration","stored":{"value":"17.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/algae/cma.yaml","field_path":"ingredients[0].concentration","stored":{"value":"17.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cma.yaml","field_path":"ingredients[0].concentration","stored":{"value":"17","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"CCAP
    explicitly labels the table per litre, independently corroborated by the exact
    provider g_l row. The existing value is supported unchanged, but no attached literal
    concentration evidence exists. For the first row the amount refers to the whole
    corn-meal agar premix, not pure agar.","source_stage":"CCAP whole-medium explicit
    per-litre table","sources":[{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt
    lines 11-11","quote":"Medium                                                                   per
    litre","quote_basis":"derivative text"},{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt
    lines 13-13","quote":"Corn meal agar                                                17.0
    g","quote_basis":"derivative text"},{"evidence_id":"apiC24","reference":"https://mediadive.dsmz.de/rest/medium/C24","raw_path":"REVIEW_WORK/batch064/source08-10/apiC24.raw","raw_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","text_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","accessed_at":"2026-10-28T11:00:16.550303Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Corn meal agar\",\n                        \"compound_id\":
    702,\n                        \"attribute\": \"Oxoid CM103\",\n                        \"amount\":
    17,\n                        \"unit\": \"g\",\n                        \"g_l\":
    17,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q2","label":"D-glucose","local_fields":[{"path":"data/merge_yaml/merged/CMA.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/algae/cma.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cma.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"CCAP
    explicitly labels the table per litre, independently corroborated by the exact
    provider g_l row. The existing value is supported unchanged, but no attached literal
    concentration evidence exists. For the first row the amount refers to the whole
    corn-meal agar premix, not pure agar.","source_stage":"CCAP whole-medium explicit
    per-litre table","sources":[{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt
    lines 11-11","quote":"Medium                                                                   per
    litre","quote_basis":"derivative text"},{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt
    lines 14-14","quote":"D-glucose                                                     2.0
    g","quote_basis":"derivative text"},{"evidence_id":"apiC24","reference":"https://mediadive.dsmz.de/rest/medium/C24","raw_path":"REVIEW_WORK/batch064/source08-10/apiC24.raw","raw_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","text_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","accessed_at":"2026-10-28T11:00:16.550303Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\":
    211,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\":
    11.1012,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q3","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/CMA.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/algae/cma.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cma.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"CCAP
    explicitly labels the table per litre, independently corroborated by the exact
    provider g_l row. The existing value is supported unchanged, but no attached literal
    concentration evidence exists. For the first row the amount refers to the whole
    corn-meal agar premix, not pure agar.","source_stage":"CCAP whole-medium explicit
    per-litre table","sources":[{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt
    lines 11-11","quote":"Medium                                                                   per
    litre","quote_basis":"derivative text"},{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt
    lines 15-15","quote":"Yeast extract                                                 1.0
    g","quote_basis":"derivative text"},{"evidence_id":"apiC24","reference":"https://mediadive.dsmz.de/rest/medium/C24","raw_path":"REVIEW_WORK/batch064/source08-10/apiC24.raw","raw_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","text_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","accessed_at":"2026-10-28T11:00:16.550303Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"attribute\": \"Oxoid L21\",\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q4","label":"Source solvent input","local_fields":[],"decision":"evidence_only","rationale":"API
    C24 includes an input water volume and CCAP says cold deionised water. Preserve
    this as preparation context; the three solute rates are already source-explicit
    per litre and need no inference from this input volume.","source_stage":"Solvent/preparation
    input","sources":[{"evidence_id":"apiC24","reference":"https://mediadive.dsmz.de/rest/medium/C24","raw_path":"REVIEW_WORK/batch064/source08-10/apiC24.raw","raw_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","text_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","accessed_at":"2026-10-28T11:00:16.550303Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Deionized water\",\n                        \"compound_id\":
    418,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt
    lines 18-20","quote":"Disperse the agar in cold deionised water. Apply heat, stirring
    constantly. During heating, add\nglucose and yeast extract. Bring contents to
    boil. Transfer molten agar to suitable vessels.\nSterilise by pressure cooking
    at 10 psi for 15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q5","label":"Maintained
    bacterial owner preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/cma.yaml","field_path":"preparation_steps[0].description","stored":"Disperse
    the agar in cold deionised water. Apply heat, stirring constantly. During heating,
    add\r\nglucose and yeast extract. Bring contents to boil. Transfer molten agar
    to suitable vessels.\r\nSterilise by pressure cooking at 10 psi for 15 minutes."}],"decision":"evidence_only","rationale":"The
    complete maintained description agrees with the source, including 10 psi and 15
    minutes. Credit this existing preparation content; HEAT is a coarse action covering
    a multistage instruction, not evidence that the sterilization text is absent.","source_stage":"Dispersion,
    heating, addition, transfer and sterilization","sources":[{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt
    lines 18-20","quote":"Disperse the agar in cold deionised water. Apply heat, stirring
    constantly. During heating, add\nglucose and yeast extract. Bring contents to
    boil. Transfer molten agar to suitable vessels.\nSterilise by pressure cooking
    at 10 psi for 15 minutes.","quote_basis":"derivative text"},{"evidence_id":"apiC24","reference":"https://mediadive.dsmz.de/rest/medium/C24","raw_path":"REVIEW_WORK/batch064/source08-10/apiC24.raw","raw_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","text_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","accessed_at":"2026-10-28T11:00:16.550303Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Disperse the agar in cold deionised water. Apply heat, stirring constantly.
    During heating, add\\r\\nglucose and yeast extract. Bring contents to boil. Transfer
    molten agar to suitable vessels.\\r\\nSterilise by pressure cooking at 10 psi
    for 15 minutes.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"Missing
    preparation in generated target and algae owner","local_fields":[],"decision":"evidence_only","rationale":"Restore
    only the exact source-described preparation, crediting the bacterial owner. No
    pH, incubation temperature or organism-growth regime is supplied in this source.","source_stage":"Source-only
    preparation for missing layers","sources":[{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt
    lines 18-20","quote":"Disperse the agar in cold deionised water. Apply heat, stirring
    constantly. During heating, add\nglucose and yeast extract. Bring contents to
    boil. Transfer molten agar to suitable vessels.\nSterilise by pressure cooking
    at 10 psi for 15 minutes.","quote_basis":"derivative text"},{"evidence_id":"apiC24","reference":"https://mediadive.dsmz.de/rest/medium/C24","raw_path":"REVIEW_WORK/batch064/source08-10/apiC24.raw","raw_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","text_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","accessed_at":"2026-10-28T11:00:16.550303Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Disperse the agar in cold deionised water. Apply heat, stirring constantly.
    During heating, add\\r\\nglucose and yeast extract. Bring contents to boil. Transfer
    molten agar to suitable vessels.\\r\\nSterilise by pressure cooking at 10 psi
    for 15 minutes.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"light_intensity","local_fields":[{"path":"data/merge_yaml/merged/CMA.yaml","field_path":"light_intensity","stored":"Varies
    by species; typically 50-100 µmol photons m⁻² s⁻¹"},{"path":"data/normalized_yaml/algae/cma.yaml","field_path":"light_intensity","stored":"Varies
    by species; typically 50-100 µmol photons m⁻² s⁻¹"}],"decision":"unsupported","rationale":"These
    current generic culture ranges are not supported by the complete CCAP recipe or
    C24 payload. Current CCAP importer inserts these defaults without target-specific
    evidence. Do not convert their plausibility into a source-specific growth recommendation.","source_stage":"Generic
    imported growth-condition assertion, not source-certified","sources":[{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt
    lines 6-20","quote":"CMA (Corn Meal Glucose Agar)\n                                         Freshwater
    Protozoa\n\n\n\nMedium                                                                   per
    litre\n\n           Corn meal agar                                                17.0
    g\n           D-glucose                                                     2.0
    g\n           Yeast extract                                                 1.0
    g\n\n\nDisperse the agar in cold deionised water. Apply heat, stirring constantly.
    During heating, add\nglucose and yeast extract. Bring contents to boil. Transfer
    molten agar to suitable vessels.\nSterilise by pressure cooking at 10 psi for
    15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q8","label":"light_cycle","local_fields":[{"path":"data/merge_yaml/merged/CMA.yaml","field_path":"light_cycle","stored":"Varies
    by species; commonly 12:12 or 16:8 light:dark"},{"path":"data/normalized_yaml/algae/cma.yaml","field_path":"light_cycle","stored":"Varies
    by species; commonly 12:12 or 16:8 light:dark"}],"decision":"unsupported","rationale":"These
    current generic culture ranges are not supported by the complete CCAP recipe or
    C24 payload. Current CCAP importer inserts these defaults without target-specific
    evidence. Do not convert their plausibility into a source-specific growth recommendation.","source_stage":"Generic
    imported growth-condition assertion, not source-certified","sources":[{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt
    lines 6-20","quote":"CMA (Corn Meal Glucose Agar)\n                                         Freshwater
    Protozoa\n\n\n\nMedium                                                                   per
    litre\n\n           Corn meal agar                                                17.0
    g\n           D-glucose                                                     2.0
    g\n           Yeast extract                                                 1.0
    g\n\n\nDisperse the agar in cold deionised water. Apply heat, stirring constantly.
    During heating, add\nglucose and yeast extract. Bring contents to boil. Transfer
    molten agar to suitable vessels.\nSterilise by pressure cooking at 10 psi for
    15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q9","label":"temperature_range","local_fields":[{"path":"data/merge_yaml/merged/CMA.yaml","field_path":"temperature_range","stored":"15-30°C
    depending on species"},{"path":"data/normalized_yaml/algae/cma.yaml","field_path":"temperature_range","stored":"15-30°C
    depending on species"}],"decision":"unsupported","rationale":"These current generic
    culture ranges are not supported by the complete CCAP recipe or C24 payload. Current
    CCAP importer inserts these defaults without target-specific evidence. Do not
    convert their plausibility into a source-specific growth recommendation.","source_stage":"Generic
    imported growth-condition assertion, not source-certified","sources":[{"evidence_id":"ccapCMA","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CMA.pdf","raw_path":"REVIEW_WORK/batch064/source08-10/ccapCMA.raw","raw_sha256":"1e6694820ae9ac2a0abad6beb53adb083e1eff1ccc71a1c5800b53da93d1440b","text_sha256":"5b606e90f3b96cdd88e424e08f5b95bfdee35ed290f9f74e5b3071cfd0e3c748","accessed_at":"2026-10-28T11:00:17.065174Z","locator":"ccapCMA.txt
    lines 6-20","quote":"CMA (Corn Meal Glucose Agar)\n                                         Freshwater
    Protozoa\n\n\n\nMedium                                                                   per
    litre\n\n           Corn meal agar                                                17.0
    g\n           D-glucose                                                     2.0
    g\n           Yeast extract                                                 1.0
    g\n\n\nDisperse the agar in cold deionised water. Apply heat, stirring constantly.
    During heating, add\nglucose and yeast extract. Bring contents to boil. Transfer
    molten agar to suitable vessels.\nSterilise by pressure cooking at 10 psi for
    15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q10","label":"Whole
    premix identity compared with manufacturer specification","local_fields":[],"decision":"evidence_only","rationale":"The
    current official CM0103 specification demonstrates corn-meal extract plus agar
    as a premix. It is identity context for the API Oxoid CM103 attribute, not an
    instruction to replace CCAP with the manufacturer preparation, extract an exact
    historical lot formula, or transfer QC-organism conditions. Keep the whole premix
    quantity.","source_stage":"Manufacturer composition context only; not added to
    the medium a second time","sources":[{"evidence_id":"oxoidCM0103","reference":"https://documents.thermofisher.com/TFS-Assets/MBD/Specification-Sheets/PS-CM0103-V2.pdf","raw_path":"REVIEW_WORK/batch064/source08-10-supplement/oxoidCM0103.raw","raw_sha256":"93926785c704080905aeb5d428a539c28a7431843ead2d2ac393996876cb4b2c","text_sha256":"39e41f18f2ca4309cce75da43942e612a15e97cf7aa9d996497c2cf28b423dbf","accessed_at":"2026-10-28T11:05:20.796307Z","locator":"oxoidCM0103.txt
    lines 5-14","quote":"OXOID QUALITY ASSURANCE PRODUCT SPECIFICATION\n                                CORN
    MEAL AGAR CM0103\nCORN MEAL AGAR                                                                       CM0103\n\nTypical
    Formula*\n\nCorn meal extract (from 50g whole maize) grams per litre                              2.0\nAgar                                                                                 15.0\n\n*adjusted
    as required to meet performance standards","quote_basis":"derivative text"},{"evidence_id":"apiC24","reference":"https://mediadive.dsmz.de/rest/medium/C24","raw_path":"REVIEW_WORK/batch064/source08-10/apiC24.raw","raw_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","text_sha256":"2fae46ee1b1c1a52a9d5caa90f8763774a7e956fda5b234b1980560837b02b3b","accessed_at":"2026-10-28T11:00:16.550303Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Corn meal agar\",\n                        \"compound_id\":
    702,\n                        \"attribute\": \"Oxoid CM103\",\n                        \"amount\":
    17,\n                        \"unit\": \"g\",\n                        \"g_l\":
    17,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/CMA.yaml":null,"data/normalized_yaml/algae/cma.yaml":null,"data/normalized_yaml/bacterial/cma.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: 'Fresh OLS verifies all three asserted ontology identifiers and canonical
    labels: CHEBI:2509 agar, CHEBI:17634 D-glucose and FOODON:03315426 yeast extract.
    Correct labels do not repair the whole-premix versus agar identity mismatch. The
    exact current MIM snapshot has two secondary links in the bacterial owner and
    none in the target/algae owner; linkage presence and validity among present slots
    are separate metrics. No numeric legacy MIM slots are asserted.'
  target_ids:
  - CultureMech:000061
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: Four complete prior reports and the exact plan records[422] object were
    read. Five quoted API objects and the historical raw SHA match the fresh C24 capture
    exactly; this authenticates current equal content, not a recovered original access
    event. No attached local ingredient evidence is thereby created. The algae owner’s
    September source repair and bacterial owner’s full preparation are credited; present
    merge guards and CCAP generic defaults are direct current-code observations only.
    The literal batch_process_collection_media curator name was not found in ignored-inclusive
    scripts/src Python search, so its historical implementation is unresolved.
  target_ids:
  - CultureMech:000061
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-000061-generated-preparation-staleness
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Generated record drops maintained preparation and source provenance
  description: The generated record takes the algae owner’s LIQUID/default assertions
    and lacks preparation_steps, while the maintained bacterial C24 owner is SOLID_AGAR
    and already preserves the complete source preparation. The algae owner now has
    a structured CCAP sources entry absent from the generated target. Current merger/formulation
    code rejects incompatible scientific fields; reconcile these exact owners and
    regenerate without silently discarding their differences. Retain the credited
    bacterial description, and represent the source-supported agar physical form.
  target_ids:
  - CultureMech:000061
  field_paths:
  - physical_state
  - preparation_steps
  - sources
  - merged_from
  evidence_ids:
  - target
  - owner
  - owner-2
  - ccapCMA
  - apiC24
  - writer-formulation
  - writer-merger
  - writer-matcher
  rule_id: review-yaml-record/representation
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/cma.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cma.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-000061-premix-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Corn-meal agar premix is grounded as agar alone
  description: All three current documents map the entire Corn meal agar input to
    CHEBI:2509 agar. The ontology object describes algal polysaccharides, while the
    provider identifies an Oxoid corn-meal agar product and the official current manufacturer
    specification describes corn-meal extract plus agar. Preserve the complete premix
    identity and its supported whole-premix rate; do not equate it with pure agar
    or duplicate its constituents. No replacement ontology ID or exact historical
    product-lot expansion is invented.
  target_ids:
  - CultureMech:000061
  field_paths:
  - ingredients[0].term
  - data/normalized_yaml/bacterial/cma.yaml::ingredients[0].mediaingredientmech_chebi_term
  evidence_ids:
  - target
  - owner
  - owner-2
  - apiC24
  - ccapCMA
  - oxoidCM0103
  - chebi2509
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/cma.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cma.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-000061-generic-growth-defaults
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Collection membership is overextended into unsupported growth guidance
  description: CCAP labels this recipe Freshwater Protozoa. The generated target and
    algae owner instead advertise algae/phytoplankton use and numeric generic light/temperature
    ranges not supplied by the recipe. Current ccap_importer.convert_recipe visibly
    inserts those generic defaults. Retain the exact collection-level source scope
    without assigning species, strains, a new taxon ID or a universal growth regime.
    The bacterial category on the other owner is likewise a filing choice, not experimental
    growth evidence.
  target_ids:
  - CultureMech:000061
  field_paths:
  - description
  - applications
  - light_intensity
  - light_cycle
  - temperature_range
  - category
  - categories
  evidence_ids:
  - ccapCMA
  - apiC24
  - target
  - owner
  - owner-2
  - writer-ccap
  rule_id: review-yaml-record/scope
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/cma.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cma.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-000061-field-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Supported rates and preparation lack attached literal evidence
  description: All three per-litre values are directly supported by the current CCAP
    table and API, but their local source strings and root references are not attached
    field-specific literal evidence. The older October7 report left them unresolved
    because it did not establish the collection/link; the fresh PDF/provider join
    now supports the quantities without rewriting the old report or claiming it already
    verified them. Attach exact source-stage evidence with present access metadata.
  target_ids:
  - CultureMech:000061
  field_paths:
  - ingredients
  - evidence
  - references
  evidence_ids:
  - ccapCMA
  - apiC24
  - historical-reading
  - target
  - owner
  - owner-2
  rule_id: review-yaml-record/evidence
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/cma.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cma.yaml
    role: maintained source
- finding_id: f5
  issue_key: culturemech-000061-append-only-source-history
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Current source repair can replace a prior history observation
  description: The algae owner’s structured-source addition is valid provenance credit.
    However, the inspected current _ensure_event implementation assigns history[index]
    when it encounters the same curator/action, replacing prior evidence rather than
    appending a new correction observation. This is a current writer issue; the review
    does not claim it was rerun or that a past event was actually destroyed. Preserve
    the current event and make any future repair append-only.
  target_ids:
  - CultureMech:000061
  field_paths:
  - curation_history
  evidence_ids:
  - writer-ccap-source
  - owner
  rule_id: review-yaml-record/provenance
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: scripts/repair_ccap_sources_score10.py
    role: maintained source-repair writer; _ensure_event
actions:
- action_id: a1
  description: The generated record takes the algae owner’s LIQUID/default assertions
    and lacks preparation_steps, while the maintained bacterial C24 owner is SOLID_AGAR
    and already preserves the complete source preparation. The algae owner now has
    a structured CCAP sources entry absent from the generated target. Current merger/formulation
    code rejects incompatible scientific fields; reconcile these exact owners and
    regenerate without silently discarding their differences. Retain the credited
    bacterial description, and represent the source-supported agar physical form.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000061
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/cma.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cma.yaml
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
  description: All three current documents map the entire Corn meal agar input to
    CHEBI:2509 agar. The ontology object describes algal polysaccharides, while the
    provider identifies an Oxoid corn-meal agar product and the official current manufacturer
    specification describes corn-meal extract plus agar. Preserve the complete premix
    identity and its supported whole-premix rate; do not equate it with pure agar
    or duplicate its constituents. No replacement ontology ID or exact historical
    product-lot expansion is invented.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000061
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/cma.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cma.yaml
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
  description: CCAP labels this recipe Freshwater Protozoa. The generated target and
    algae owner instead advertise algae/phytoplankton use and numeric generic light/temperature
    ranges not supplied by the recipe. Current ccap_importer.convert_recipe visibly
    inserts those generic defaults. Retain the exact collection-level source scope
    without assigning species, strains, a new taxon ID or a universal growth regime.
    The bacterial category on the other owner is likewise a filing choice, not experimental
    growth evidence.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000061
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/cma.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cma.yaml
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
  description: All three per-litre values are directly supported by the current CCAP
    table and API, but their local source strings and root references are not attached
    field-specific literal evidence. The older October7 report left them unresolved
    because it did not establish the collection/link; the fresh PDF/provider join
    now supports the quantities without rewriting the old report or claiming it already
    verified them. Attach exact source-stage evidence with present access metadata.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:000061
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/cma.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cma.yaml
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
  description: Update scripts/repair_ccap_sources_score10.py::_ensure_event so a future
    source repair preserves prior curation-history entries and appends a distinct
    correction observation. Retain the existing owner source evidence. This action
    concerns the writer and does not request recipe changes or assert a past event
    was actually destroyed.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:000061
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: scripts/repair_ccap_sources_score10.py
    role: maintained source-repair writer; _ensure_event
  acceptance_checks:
  - A focused writer check preserves every existing history entry byte-for-byte when
    the same curator/action already exists and appends a new correction observation
    with its actual timestamp.
  - Retain the existing source-repair identity guards and structured-source evidence;
    verify that no recipe amount, preparation instruction or source assertion changes
    as part of this writer correction.
  generator: scripts/repair_ccap_sources_score10.py::_ensure_event
limitations:
- The complete CCAP one-page PDF and complete API were read. Manufacturer CM0103 first-page
  formula/identity and revision text were read only as premix context; its QC organisms,
  incubation, pH and sterilization instructions are excluded from this CCAP review.
  The older exact CM103-host request returned403 and remains preserved.
- Current manufacturer composition is not an authenticated historical product-lot
  recipe and is not expanded into extra medium ingredients. Source-table per-litre
  rates need no water-volume inference; no pH or growth conditions are invented.
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
