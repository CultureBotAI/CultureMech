# Scientific review: Chopped Meat Medium

- Review: 20261028T085607Z-culturemech-009156-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T08:34:15.790339Z
- Finished UTC: 2026-10-28T08:56:07.921770Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Chopped Meat Medium retains exact source identity but misrepresents extraction stages, liquid/milligram units, optional agar and source preparation. All20 local concentration fields and conditional source controls are accounted for; provider volume and optional K1 discrepancies remain explicit.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch061 index 09
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009156 | data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml | generated | chopped_meat_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:009156 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:009156 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:009156 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:009156 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact record/source and conditional variants

identity: concern. Targets: CultureMech:009156.

TOGO M2588 directly cites DSM78 and matches the selected owner identity. Its source extraction stages and agar branch are not represented faithfully; optional supplements and strain overrides are not general target requirements.

### Original native diagnostics

schema: supported. Targets: CultureMech:009156.

All four original canonical diagnostics passed once; strict zero errors and references zero checks do not authenticate source stage or quantity claims.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:009156.

20 current concentration fields are covered by 35 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b061-quantity-inventory-v1","target":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","quantity_field_count":20,"decisions":[{"quantity_id":"q1","label":"Input water","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1000","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1000","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source specifies an input liquid volume, not a mass or final-medium concentration. Preserve the extraction input separately from later filtrate makeup.","source_stage":"Initial extraction","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 5-5","quote":"Distilled water                                                    1000.0       ml","quote_basis":"derivative text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"NaOH adjustment stock input","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"25","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"25","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source gives a volume of a1N solution. Neither its stock strength nor the input dose is a gram-per-litre amount; do not compute mass without a justified source basis.","source_stage":"Initial extraction","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 6-6","quote":"NaOH 1 N                                                             25.0       ml","quote_basis":"derivative text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"attribute\": \"1 N\",\n                        \"amount\": 25,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"Ground meat extraction input","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"500","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"500","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed mass is material used before boiling, filtering and retaining two fractions. It is not verified as retained beef concentration in final medium; API487.805g_l merely uses its declared1025mL normalization.","source_stage":"Initial extraction","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 4-11","quote":"Ground beef (fat free)                                              500.0        g\nDistilled water                                                    1000.0       ml\nNaOH 1 N                                                             25.0       ml\n\nUse lean beef or horse meat. Remove fat and connective tissue before grinding. Mix\nmeat, water and NaOH, then boil for 15 min with stirring. Cool to room temperature,\nskim fat off surface, and filter, retaining both meat particles and filtrate. To the filtrate\nadd water to a final volume of 1000 ml, and then add:","quote_basis":"derivative text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Ground beef\",\n                        \"compound_id\": 128,\n                        \"attribute\": \"fat free\",\n                        \"amount\": 500,\n                        \"unit\": \"g\",\n                        \"g_l\": 487.805,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"Yeast extract after filtrate makeup","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed batch mass is added after filtrate is made up to1000mL. No subsequent measured final volume is given; local G_PER_L is not independently established as final-medium concentration. API uses a different declared1025mL basis, not proof to substitute its rate.","source_stage":"Post-filtrate preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 11-14","quote":"add water to a final volume of 1000 ml, and then add:\n\nCasitone                                                              30.0       g\nYeast extract                                                          5.0       g","quote_basis":"derivative text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.87805,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"Dipotassium hydrogen phosphate after filtrate makeup","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"Printed batch mass is supported but added after filtrate makeup. Final-medium denominator is not established; API1025mL normalization remains a separate provider assertion.","source_stage":"Post-filtrate preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 11-15","quote":"add water to a final volume of 1000 ml, and then add:\n\nCasitone                                                              30.0       g\nYeast extract                                                          5.0       g\nK2HPO4                                                                 5.0       g","quote_basis":"derivative text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.87805,\n                        \"mmol_l\": 28.0064,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"Resazurin amount","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source gives1mg, not1g. Preserve the milligram batch amount and stage. The1000-fold mass-unit discrepancy is independent of the unresolved later final-medium denominator; do not silently normalize it to an assumed litre.","source_stage":"Post-filtrate preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 16-16","quote":"Resazurin                                                              1.0      mg","quote_basis":"derivative text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00097561,\n                        \"mmol_l\": 0.00425677,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"Casitone after filtrate makeup","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"30","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"Printed batch mass is supported but added after the filtrate makeup. Local final-medium G_PER_L remains unsupported; API1025mL declared normalization must not overwrite the preparation sequence.","source_stage":"Post-filtrate preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 11-13","quote":"add water to a final volume of 1000 ml, and then add:\n\nCasitone                                                              30.0       g","quote_basis":"derivative text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Casitone\",\n                        \"compound_id\": 84,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 29.2683,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Nitrogen gas condition","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"The variable local amount is not a mass concentration. Source specifies a gas atmosphere and handling condition; preserve that in preparation rather than invent a dose or weight/volume percent.","source_stage":"Post-filtrate preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 18-22","quote":"To make medium anoxic bring it to a boil, cool under 100% N2 gas atmosphere, add 0.5\ng/l L-cysteine hydrochloride and adjust pH to 7.0. Dispense under 100% N2 gas\natmosphere by filling 7 ml medium into anoxic Hungate-type tubes (for strains\ndemanding meat particles put those first into the tube (use 1 part meat particles to 4 or\n5 parts fluid)). Autoclave at 121°C for 30 min. For agar slants use 15.0 g agar per","quote_basis":"derivative text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\": 8,\n                        \"step\": \"To make medium anoxic bring it to a boil, cool under 100% N2 gas atmosphere, add 0.5 g/l L-cysteine hydrochloride and adjust pH to 7.0. Dispense under 100% N2 gas atmosphere by filling 7 ml medium into anoxic Hungate-type tubes (for strains demanding meat particles put those first into the tube (use 1 part meat particles to 4 or 5 parts fluid)). Autoclave at 121\\u00b0C for 30 min. For agar slants use 15.0 g agar per 1000.0 ml medium.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"Agar branch","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"15","unit":"G_PER_L"}}],"decision":"correct","rationale":"The explicit15g per1000mL rate is supported only for agar slants. Current unconditional ingredient and SOLID_AGAR classification collapse that variant into the generic record; preserve the branch rather than delete source-supported option.","source_stage":"Conditional agar branch","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 22-23","quote":"5 parts fluid)). Autoclave at 121°C for 30 min. For agar slants use 15.0 g agar per\n1000.0 ml medium.","quote_basis":"derivative text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"for solid medium\",\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 14.6341,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"L-cysteine hydrochloride direct rate","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Primary text explicitly states0.5g/L, supporting the existing rate without inferred volume or hydrate. No attached evidence is present. API table0.487805g_l conflicts with its own preserved instruction and is not substituted.","source_stage":"Post-filtrate preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 18-19","quote":"To make medium anoxic bring it to a boil, cool under 100% N2 gas atmosphere, add 0.5\ng/l L-cysteine hydrochloride and adjust pH to 7.0. Dispense under 100% N2 gas","quote_basis":"derivative text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"L-Cysteine HCl\",\n                        \"compound_id\": 1157,\n                        \"condition\": \"\",\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.487805,\n                        \"mmol_l\": 3.09482,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"Extraction boil duration","local_fields":[],"decision":"evidence_only","rationale":"The initial boil and filtration are a separate extraction operation, not final sterilization.","source_stage":"Source-only preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 8-11","quote":"Use lean beef or horse meat. Remove fat and connective tissue before grinding. Mix\nmeat, water and NaOH, then boil for 15 min with stirring. Cool to room temperature,\nskim fat off surface, and filter, retaining both meat particles and filtrate. To the filtrate\nadd water to a final volume of 1000 ml, and then add:","quote_basis":"derivative text"}]},{"quantity_id":"q12","label":"Filtrate final makeup","local_fields":[],"decision":"evidence_only","rationale":"This is an explicit final volume for the filtrate stage only, before subsequent solutes. It does not certify final combined medium volume.","source_stage":"Source-only preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 10-11","quote":"skim fat off surface, and filter, retaining both meat particles and filtrate. To the filtrate\nadd water to a final volume of 1000 ml, and then add:","quote_basis":"derivative text"}]},{"quantity_id":"q13","label":"Nitrogen atmosphere and cysteine/pH sequence","local_fields":[],"decision":"evidence_only","rationale":"Preserve the gas condition, explicit cysteine rate and generic pH separately; no inferred gas mass or alternative organism-specific condition.","source_stage":"Source-only preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 18-20","quote":"To make medium anoxic bring it to a boil, cool under 100% N2 gas atmosphere, add 0.5\ng/l L-cysteine hydrochloride and adjust pH to 7.0. Dispense under 100% N2 gas\natmosphere by filling 7 ml medium into anoxic Hungate-type tubes (for strains","quote_basis":"derivative text"}]},{"quantity_id":"q14","label":"Dispensing and optional meat-particle ratio","local_fields":[],"decision":"evidence_only","rationale":"Dispensing volume and particle/fluid ratios apply to the stated context only. The ratio is not explicitly a mass fraction and is not converted.","source_stage":"Source-only preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 20-22","quote":"atmosphere by filling 7 ml medium into anoxic Hungate-type tubes (for strains\ndemanding meat particles put those first into the tube (use 1 part meat particles to 4 or\n5 parts fluid)). Autoclave at 121°C for 30 min. For agar slants use 15.0 g agar per","quote_basis":"derivative text"}]},{"quantity_id":"q15","label":"Sterilization stage","local_fields":[],"decision":"evidence_only","rationale":"Final sterilization is distinct from the initial extraction boil. No pressure is inferred from the printed temperature.","source_stage":"Source-only preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 22-23","quote":"5 parts fluid)). Autoclave at 121°C for 30 min. For agar slants use 15.0 g agar per\n1000.0 ml medium.","quote_basis":"derivative text"}]},{"quantity_id":"q16","label":"Optional supplement receiving basis","local_fields":[],"decision":"evidence_only","rationale":"Catalogue-dependent supplements are not unconditional omissions from this generic target. Primary gives equal printed receiving volumes for K1 or K3; API K1 volume differs and remains unresolved.","source_stage":"Conditional source-only stock","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 26-30","quote":"In some cases (as indicated in the catalogue) the addition of Haemin and Vitamin K1 or\nVitamin K3 is necessary. Add to 1000 ml of medium after autoclaving:\n\nHaemin solution (see below)                                         10.00       ml\nVitamin K1 or Vitamin K3 solution (see below)                       10.00       ml","quote_basis":"derivative text"}]},{"quantity_id":"q17","label":"Haemin stock makeup","local_fields":[],"decision":"evidence_only","rationale":"Explicit makeup to100mL supports a stock basis. It is conditional source-only context, not a local ingredient or mandatory dose; no new target stock is prescribed.","source_stage":"Conditional source-only stock","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 32-34","quote":"Haemin solution:\nDissolve 50 mg haemin in 1 ml 1 N NaOH; make up to 100 ml with distilled water and\nfilter sterilize. Store refrigerated.","quote_basis":"derivative text"}]},{"quantity_id":"q18","label":"Vitamin K1 stock solvent and grade","local_fields":[],"decision":"evidence_only","rationale":"Printed vitamin volume and ethanol input are not an explicit final stock makeup. The95% basis is unspecified; no mass, density or final-medium conversion is asserted.","source_stage":"Conditional source-only stock","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 35-37","quote":"Vitamin K1 solution:\nDissolve 0.1 ml of vitamin K1 in 20 ml 95% ethanol and filter sterilize. Store refrigerated\nin a brown bottle.","quote_basis":"derivative text"}]},{"quantity_id":"q19","label":"Vitamin K3 two concentration stages","local_fields":[],"decision":"evidence_only","rationale":"The initial and diluted concentrations are separately explicit; preserve them as stock stages. Do not conflate with K1, infer an ethanol percent basis, or turn an optional stock into a mandatory ingredient.","source_stage":"Source-only preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 38-40","quote":"Vitamin K3 solution:\nDissolve 5 mg/ml of vitamin K3 in 95% ethanol, dilute to 0.05 mg/ml in water and filter\nsterilize. Store refrigerated in a brown bottle.","quote_basis":"derivative text"}]},{"quantity_id":"q20","label":"Excluded strain-specific pH override","local_fields":[],"decision":"evidence_only","rationale":"DSM21650-only instruction is retained as excluded source context. It does not replace the generic pH and no organism-growth inference is made.","source_stage":"Excluded strain variant","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 43-43","quote":"For DSM 21650 adjust pH of complete medium to 8.5.","quote_basis":"derivative text"}]},{"quantity_id":"q21","label":"Provider solution 123 volume","local_fields":[],"decision":"evidence_only","rationale":"Provider-declared volume is retained separately from textual preparation. Main1025mL is not the filtrate1000mL makeup; stock volumes and optional branches do not establish final-medium volume.","source_stage":"Provider metadata comparison","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0]","quote":"{\n                \"id\": 123,\n                \"name\": \"Main sol. 78\",\n                \"volume\": 1025,\n                \"recipe\": [\n                    {\n                        \"recipe_order\": 1,\n                        \"compound\": \"Ground beef\",\n                        \"compound_id\": 128,\n                        \"attribute\": \"fat free\",\n                        \"amount\": 500,\n                        \"unit\": \"g\",\n                        \"g_l\": 487.805,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"attribute\": \"1 N\",\n                        \"amount\": 25,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 4,\n                        \"compound\": \"Casitone\",\n                        \"compound_id\": 84,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 29.2683,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 5,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.87805,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 6,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.87805,\n                        \"mmol_l\": 28.0064,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 7,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00097561,\n                        \"mmol_l\": 0.00425677,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 8,\n                        \"compound\": \"L-Cysteine HCl\",\n                        \"compound_id\": 1157,\n                        \"condition\": \"\",\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.487805,\n                        \"mmol_l\": 3.09482,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"for solid medium\",\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 14.6341,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 10,\n                        \"solution\": \"Haemin solution\",\n                        \"solution_id\": 124,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 1\n                    },\n                    {\n                        \"recipe_order\": 11,\n                        \"solution\": \"Vitamin K1 solution\",\n                        \"solution_id\": 125,\n                        \"condition\": \"alternative\",\n                        \"amount\": 0.2,\n                        \"unit\": \"ml\",\n                        \"optional\": 1\n                    },\n                    {\n                        \"recipe_order\": 12,\n                        \"solution\": \"Vitamin K3 solution\",\n                        \"solution_id\": 5540,\n                        \"condition\": \"alternative\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 1\n                    }\n                ],\n                \"steps\": [\n                    {\n                        \"recipe_order\": 8,\n                        \"step\": \"To make medium anoxic bring it to a boil, cool under 100% N2 gas atmosphere, add 0.5 g/l L-cysteine hydrochloride and adjust pH to 7.0. Dispense under 100% N2 gas atmosphere by filling 7 ml medium into anoxic Hungate-type tubes (for strains demanding meat particles put those first into the tube (use 1 part meat particles to 4 or 5 parts fluid)). Autoclave at 121\\u00b0C for 30 min. For agar slants use 15.0 g agar per 1000.0 ml medium.\"\n                    },\n                    {\n                        \"recipe_order\": 10,\n                        \"step\": \"In some cases (as indicated in the catalogue) the addition of Haemin and Vitamin K1 or Vitamin K3 is necessary. Add to 1000 ml of medium after autoclaving:\"\n                    },\n                    {\n                        \"recipe_order\": 4,\n                        \"step\": \"Use lean beef or horse meat. Remove fat and connective tissue before grinding. Mix\\r\\nmeat, water and NaOH, then boil for 15 min with stirring. Cool to room temperature,\\r\\nskim fat off surface, and filter, retaining both meat particles and filtrate. To the filtrate\\r\\nadd water to a final volume of 1000 ml, and then add:\"\n                    }\n                ],\n                \"equipment\": {\n                    \"429\": \"Hungate tubes\",\n                    \"1480\": \"Filter\",\n                    \"3487\": \"Autoclave\",\n                    \"3958\": \"Gassing station\"\n                }\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"Provider solution 124 volume","local_fields":[],"decision":"evidence_only","rationale":"Provider-declared volume is retained separately from textual preparation. Main1025mL is not the filtrate1000mL makeup; stock volumes and optional branches do not establish final-medium volume.","source_stage":"Provider metadata comparison","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[1]","quote":"{\n                \"id\": 124,\n                \"name\": \"Haemin solution\",\n                \"volume\": 100,\n                \"recipe\": [\n                    {\n                        \"recipe_order\": 1,\n                        \"compound\": \"Haemin\",\n                        \"compound_id\": 149,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 0.766989,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"attribute\": \"1 N\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }\n                ],\n                \"steps\": [\n                    {\n                        \"step\": \"Dissolve 50 mg haemin in 1 ml 1 N NaOH; make up to 100 ml with distilled water and filter sterilize. Store refrigerated.\"\n                    }\n                ],\n                \"equipment\": {\n                    \"1875\": \"Filter\"\n                }\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"Provider source-only Haemin solution / Haemin","local_fields":[],"decision":"evidence_only","rationale":"Exact returned amount/unit/g_l/mmol_l/attribute retained as provider assertions only. Scope is optional stock, not a selected local field. Primary-text stage controls take precedence over unsupported final-volume, ethanol density or percentage assumptions.","source_stage":"Conditional provider stock","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Haemin\",\n                        \"compound_id\": 149,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 0.766989,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"Provider source-only Haemin solution / NaOH","local_fields":[],"decision":"evidence_only","rationale":"Exact returned amount/unit/g_l/mmol_l/attribute retained as provider assertions only. Scope is optional stock, not a selected local field. Primary-text stage controls take precedence over unsupported final-volume, ethanol density or percentage assumptions.","source_stage":"Conditional provider stock","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"attribute\": \"1 N\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"Provider source-only Haemin solution / Distilled water","local_fields":[],"decision":"evidence_only","rationale":"Exact returned amount/unit/g_l/mmol_l/attribute retained as provider assertions only. Scope is optional stock, not a selected local field. Primary-text stage controls take precedence over unsupported final-volume, ethanol density or percentage assumptions.","source_stage":"Conditional provider stock","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"Provider solution 125 volume","local_fields":[],"decision":"evidence_only","rationale":"Provider-declared volume is retained separately from textual preparation. Main1025mL is not the filtrate1000mL makeup; stock volumes and optional branches do not establish final-medium volume.","source_stage":"Provider metadata comparison","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[2]","quote":"{\n                \"id\": 125,\n                \"name\": \"Vitamin K1 solution\",\n                \"volume\": 20,\n                \"recipe\": [\n                    {\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin K1\",\n                        \"compound_id\": 150,\n                        \"amount\": 0.1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 2,\n                        \"compound\": \"Ethanol\",\n                        \"compound_id\": 201,\n                        \"attribute\": \"95 %\",\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"g_l\": 950,\n                        \"mmol_l\": 20620.8,\n                        \"optional\": 0\n                    }\n                ],\n                \"steps\": [\n                    {\n                        \"step\": \"Dissolve 0.1 ml of vitamin K1 in 20 ml 95% ethanol and filter sterilize. Store refrigerated in a brown bottle.\"\n                    }\n                ],\n                \"equipment\": {\n                    \"277\": \"Filter\"\n                }\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"Provider source-only Vitamin K1 solution / Vitamin K1","local_fields":[],"decision":"evidence_only","rationale":"Exact returned amount/unit/g_l/mmol_l/attribute retained as provider assertions only. Scope is optional stock, not a selected local field. Primary-text stage controls take precedence over unsupported final-volume, ethanol density or percentage assumptions.","source_stage":"Conditional provider stock","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin K1\",\n                        \"compound_id\": 150,\n                        \"amount\": 0.1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Provider source-only Vitamin K1 solution / Ethanol","local_fields":[],"decision":"evidence_only","rationale":"Exact returned amount/unit/g_l/mmol_l/attribute retained as provider assertions only. Scope is optional stock, not a selected local field. Primary-text stage controls take precedence over unsupported final-volume, ethanol density or percentage assumptions.","source_stage":"Conditional provider stock","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Ethanol\",\n                        \"compound_id\": 201,\n                        \"attribute\": \"95 %\",\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"g_l\": 950,\n                        \"mmol_l\": 20620.8,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"Provider solution 5540 volume","local_fields":[],"decision":"evidence_only","rationale":"Provider-declared volume is retained separately from textual preparation. Main1025mL is not the filtrate1000mL makeup; stock volumes and optional branches do not establish final-medium volume.","source_stage":"Provider metadata comparison","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[3]","quote":"{\n                \"id\": 5540,\n                \"name\": \"Vitamin K3 solution\",\n                \"volume\": 100,\n                \"recipe\": [\n                    {\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin K3\",\n                        \"compound_id\": 2086,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 2,\n                        \"compound\": \"Ethanol\",\n                        \"compound_id\": 201,\n                        \"attribute\": \"95%\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"g_l\": 9.5,\n                        \"mmol_l\": 206.208,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 3,\n                        \"compound\": \"Water\",\n                        \"compound_id\": 754,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }\n                ],\n                \"steps\": [\n                    {\n                        \"step\": \"Dissolve 5 mg vitamin K3 in 1 ml 95% ethanol, dilute to 0.05 mg/ml in water and filter sterilize. Store refrigerated in a brown bottle.\"\n                    }\n                ]\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"Provider source-only Vitamin K3 solution / Vitamin K3","local_fields":[],"decision":"evidence_only","rationale":"Exact returned amount/unit/g_l/mmol_l/attribute retained as provider assertions only. Scope is optional stock, not a selected local field. Primary-text stage controls take precedence over unsupported final-volume, ethanol density or percentage assumptions.","source_stage":"Conditional provider stock","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin K3\",\n                        \"compound_id\": 2086,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"Provider source-only Vitamin K3 solution / Ethanol","local_fields":[],"decision":"evidence_only","rationale":"Exact returned amount/unit/g_l/mmol_l/attribute retained as provider assertions only. Scope is optional stock, not a selected local field. Primary-text stage controls take precedence over unsupported final-volume, ethanol density or percentage assumptions.","source_stage":"Conditional provider stock","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Ethanol\",\n                        \"compound_id\": 201,\n                        \"attribute\": \"95%\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"g_l\": 9.5,\n                        \"mmol_l\": 206.208,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q32","label":"Provider source-only Vitamin K3 solution / Water","local_fields":[],"decision":"evidence_only","rationale":"Exact returned amount/unit/g_l/mmol_l/attribute retained as provider assertions only. Scope is optional stock, not a selected local field. Primary-text stage controls take precedence over unsupported final-volume, ethanol density or percentage assumptions.","source_stage":"Conditional provider stock","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Water\",\n                        \"compound_id\": 754,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q33","label":"Provider optional receiving row 9","local_fields":[],"decision":"evidence_only","rationale":"Preserve optional and alternative flags. API K1 addition0.2mL differs from the primary printed10mL; no recommendation or conversion resolves this source discrepancy. Haemin/K3 rows remain separate.","source_stage":"Conditional receiving dose; provider comparison","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"solution\": \"Haemin solution\",\n                        \"solution_id\": 124,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 1\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 26-30","quote":"In some cases (as indicated in the catalogue) the addition of Haemin and Vitamin K1 or\nVitamin K3 is necessary. Add to 1000 ml of medium after autoclaving:\n\nHaemin solution (see below)                                         10.00       ml\nVitamin K1 or Vitamin K3 solution (see below)                       10.00       ml","quote_basis":"derivative text"}]},{"quantity_id":"q34","label":"Provider optional receiving row 10","local_fields":[],"decision":"evidence_only","rationale":"Preserve optional and alternative flags. API K1 addition0.2mL differs from the primary printed10mL; no recommendation or conversion resolves this source discrepancy. Haemin/K3 rows remain separate.","source_stage":"Conditional receiving dose; provider comparison","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"solution\": \"Vitamin K1 solution\",\n                        \"solution_id\": 125,\n                        \"condition\": \"alternative\",\n                        \"amount\": 0.2,\n                        \"unit\": \"ml\",\n                        \"optional\": 1\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 26-30","quote":"In some cases (as indicated in the catalogue) the addition of Haemin and Vitamin K1 or\nVitamin K3 is necessary. Add to 1000 ml of medium after autoclaving:\n\nHaemin solution (see below)                                         10.00       ml\nVitamin K1 or Vitamin K3 solution (see below)                       10.00       ml","quote_basis":"derivative text"}]},{"quantity_id":"q35","label":"Provider optional receiving row 11","local_fields":[],"decision":"evidence_only","rationale":"Preserve optional and alternative flags. API K1 addition0.2mL differs from the primary printed10mL; no recommendation or conversion resolves this source discrepancy. Haemin/K3 rows remain separate.","source_stage":"Conditional receiving dose; provider comparison","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Vitamin K3 solution\",\n                        \"solution_id\": 5540,\n                        \"condition\": \"alternative\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 1\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt lines 26-30","quote":"In some cases (as indicated in the catalogue) the addition of Haemin and Vitamin K1 or\nVitamin K3 is necessary. Add to 1000 ml of medium after autoclaving:\n\nHaemin solution (see below)                                         10.00       ml\nVitamin K1 or Vitamin K3 solution (see below)                       10.00       ml","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:009156.

All four distinct asserted CHEBI IDs resolve to current nonobsolete scientific objects with exact canonical labels. Water, generic agar and dipotassium hydrogen phosphate are compatible with the printed forms; Resazurin is neutral CHEBI8806 and the source does not explicitly specify sodium salt, so no sodium-form contradiction is invented. L-cysteine hydrochloride has an unresolved legacy key and unspecified hydrate; exact current MIM absence is not a historical mapping verdict. Primary CHEBI presence is8/20 ingredient instances, current secondary CHEBI links8/20, and two legacy slots are counted separately; label agreement does not validate the recipe.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:009156.

All three inspected historical reports were read in full. September source leads and October unassessed quantity rows are derivative review history, not new source captures or native executions. Fresh PDF/API/TOGO sources are independently read; no attached current literal evidence claims exist. The existing migration event correctly records four replaced links and does not certify the unresolved fifth legacy slot. Current importer unit, stock and comment handling is credited; its present code cannot reconstruct the older execution.

## Findings

### f1: Source liquid and milligram units were replaced by mass concentrations

major / open / confirmed; issue key: culturemech-009156-source-unit-errors.

Water and1N NaOH are source input volumes, while resazurin is a milligram batch amount. The target and owner encode all three as G_PER_L. Reconcile the original units and extraction/addition stages, retaining the independently confirmed resazurin mass-unit error without manufacturing a final-medium denominator.

### f2: Flat composition loses the meat-extraction and filtrate stages

major / open / confirmed; issue key: culturemech-009156-extraction-stage-loss.

The initial meat, water and alkaline input precede boiling, filtering and retaining both fractions. Only the filtrate is explicitly made up before the later batch additions. The current flat final-medium ingredients cannot establish retained meat concentration or the later denominator. Model the source sequence and preserve unresolved total volume; do not adopt API1025mL normalization as measured final volume.

### f3: Agar-slant option is made unconditional

major / open / confirmed; issue key: culturemech-009156-agar-variant-collapse.

The source explicitly qualifies agar as an agar-slant branch, whereas current owner and target assert SOLID_AGAR and unconditional agar. Preserve base versus agar variant scope without inferring organism suitability or transferring optional vitamin/haemin additions.

### f4: Source preparation and pH are absent

major / open / confirmed; issue key: culturemech-009156-missing-preparation.

Current records omit the source preparation sequence, including the extraction, later gas handling, explicit cysteine addition, generic pH, dispensing and sterilization. Preserve the complete generic sequence with conditional particle and agar scope. The DSM21650 override is excluded, and catalogue-dependent haemin/vitamin stocks remain optional source context with an unresolved K1 provider discrepancy. Current importer already retains comment steps and separates stock sections; this does not prove historical execution or solve source-stage arithmetic. Its pH reader expects root ph while this payload has meta.ph.

### f5: One legacy ingredient identifier remains unresolved

minor / open / confirmed; issue key: culturemech-009156-legacy-cysteine-scope.

The current L-cysteine hydrochloride slot still uses legacy MediaIngredientMech000459 without a primary CHEBI term. The packaged current index cannot authenticate a historical numeric key by its absence; source does not specify hydrate. Current migration deliberately leaves unresolved entries unchanged, so retain its history and seek exact form/stereochemistry evidence before any future mapping. Do not guess a hydrate or generic cysteine replacement.

## Recommended Actions And Acceptance Checks

### a1

Water and1N NaOH are source input volumes, while resazurin is a milligram batch amount. The target and owner encode all three as G_PER_L. Reconcile the original units and extraction/addition stages, retaining the independently confirmed resazurin mass-unit error without manufacturing a final-medium denominator.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

The initial meat, water and alkaline input precede boiling, filtering and retaining both fractions. Only the filtrate is explicitly made up before the later batch additions. The current flat final-medium ingredients cannot establish retained meat concentration or the later denominator. Model the source sequence and preserve unresolved total volume; do not adopt API1025mL normalization as measured final volume.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The source explicitly qualifies agar as an agar-slant branch, whereas current owner and target assert SOLID_AGAR and unconditional agar. Preserve base versus agar variant scope without inferring organism suitability or transferring optional vitamin/haemin additions.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

Current records omit the source preparation sequence, including the extraction, later gas handling, explicit cysteine addition, generic pH, dispensing and sterilization. Preserve the complete generic sequence with conditional particle and agar scope. The DSM21650 override is excluded, and catalogue-dependent haemin/vitamin stocks remain optional source context with an unresolved K1 provider discrepancy. Current importer already retains comment steps and separates stock sections; this does not prove historical execution or solve source-stage arithmetic. Its pH reader expects root ph while this payload has meta.ph.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

The current L-cysteine hydrochloride slot still uses legacy MediaIngredientMech000459 without a primary CHEBI term. The packaged current index cannot authenticate a historical numeric key by its absence; source does not specify hydrate. Current migration deliberately leaves unresolved entries unchanged, so retain its history and seek exact form/stereochemistry evidence before any future mapping. Do not guess a hydrate or generic cysteine replacement.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsm78 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf; REVIEW_WORK/batch061/source07-09/dsm78.json; exact original raw/text/hash/time metadata | context_only | Exact cited primary medium78 and source scope; no organism-growth inference. |
| api78 | https://mediadive.dsmz.de/rest/medium/78; REVIEW_WORK/batch061/source07-09/api78.json; exact original raw/text/hash/time metadata | context_only | Exact cited provider78; declared recipe stages distinct from variants. |
| togo2588 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2588; REVIEW_WORK/batch061/source07-09/togo2588.json; exact original raw/text/hash/time metadata | context_only | Exact TOGO2588 identity and source scope; assess safety context before operational conclusions. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377; REVIEW_WORK/batch061/source07-09/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Exact supplied-form and canonical identity for ordinary CHM source review. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527; REVIEW_WORK/batch061/source07-09/chebi131527.json; exact original raw/text/hash/time metadata | context_only | Exact existing ordinary DSM78/TOGO2588 chemical identifier and supplied-form scope; no organism-specific cultivation inference. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; REVIEW_WORK/batch061/source07-09/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Exact existing ordinary DSM78/TOGO2588 chemical identifier and supplied-form scope; no organism-specific cultivation inference. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:2509; REVIEW_WORK/batch061/source07-09/chebi2509.json; exact original raw/text/hash/time metadata | context_only | Exact existing ordinary DSM78/TOGO2588 chemical identifier and supplied-form scope; no organism-specific cultivation inference. |
| target | data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-17 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-18 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-19 | reports/yaml_record_review/20260922T075541Z-CHOPPED_MEAT_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| writer-togo | src/culturemech/import/togo_importer.py; _extract_primary_components, _ingredient_from_item, _parse_unit, _extract_preparation_steps, _extract_ph | context_only | Current importer already separates local stock sections and retains comment preparation. It maps ml to ML_PER_L, mg to MG_PER_L and l to L, while bare masses still acquire per-litre units without proof of final volume. _extract_ph reads root ph whereas this exact payload carries meta.ph. Credit current behavior without claiming it produced the historical record or fixes extraction stages automatically. |
| writer-mim | scripts/migrate_legacy_mim_to_chebi.py; _resolve_chebi, _rewrite_entry, migrate_file | context_only | Current migration prefers an existing CHEBI mapping, uses exact name/synonym plus stereochemical guard otherwise, and deliberately leaves unresolved legacy slots intact. A past migration event does not prove every current ingredient was migrated. |
| writer-default | src/culturemech/validation/schema_defaulter.py; apply_defaults and ingredient defaults | context_only | Current defaulting preserves record shape and fills missing concentrations with placeholders. The declared historical gas-default event is provenance, not source confirmation. |
| quantities | REVIEW_WORK/batch061/record09/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch061/record09/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch061/record09/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch061/record09/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch061/record09/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch061/record09/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch061/record09/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch061/record09/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch061/record09/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch061/record09/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch061/record09/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Full current DSM78 PDF consists of one page, read as text and rendered image. No second page or paper is claimed.
- API main volume1025mL and its normalized g_l conflict with preparation-stage bases and the explicit cysteine rate. API K1 receiving volume differs from the PDF. These provider discrepancies remain unresolved; no speculative normalization is recommended.
- Optional haemin and alternative K stocks are source-only controls, not mandatory missing ingredients. The DSM21650-specific override is excluded from generic findings.
- No species, strain growth, optimization or experimental suitability is inferred from this generic source.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T085607Z-culturemech-009156-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: Chopped Meat Medium'
started_at: '2026-10-28T08:34:15.790339Z'
finished_at: '2026-10-28T08:56:07.921770Z'
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
summary: Chopped Meat Medium retains exact source identity but misrepresents extraction
  stages, liquid/milligram units, optional agar and source preparation. All20 local
  concentration fields and conditional source controls are accounted for; provider
  volume and optional K1 discrepancies remain explicit.
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
  - path: data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml
    sha256: 6ac08a8108b92bf9cf7e0cefef7a28142173087b1364368cf6996250f87488bb
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml
    sha256: 4c6946754252ce4f6dd9f30b9d02aaaaaa8e8de569f0008af9c8812e203c4fbc
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.md
    sha256: c42a888bbeef6211ce4afa6ef7e31fe7f90878cbfd00a7f2426ee6fd3b4b3344
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.md
    sha256: 55d8ed0e73a795bf249384bffa162a3b7fc7090a58c376d5b0b56817fecaf9a5
    role: context
  - path: reports/yaml_record_review/20260922T075541Z-CHOPPED_MEAT_MEDIUM.md
    sha256: a55c034998e5e0f083675729c36d2feb03bd48e964b03a3048a9bca6d8b36c2b
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
  - path: scripts/enrich_with_kg_microbe_matches.py
    sha256: 61351f99ef2cb0cef03e74ad92d21dcf3b38df77a06602bdac814974e7728eeb
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
  - path: scripts/repair_ccap_instruction_rows.py
    sha256: eb1a4c8c46eb45dcdde6a5d2f0f6833792dd0802c45603eefa1b63a3ff96fca5
    role: context
  - path: scripts/repair_ccap_sources_score10.py
    sha256: f518688ae99e154f490af337dab30b9038657a814db72861e0b53658a2541ae6
    role: context
  - path: scripts/repair_mediadive_jcm_structure.py
    sha256: 5bff4c2d1900051bdea1b8e0f655049147c85cc9c61da4c348a6d60a8d0fd509
    role: context
  - path: scripts/repair_official_simple_score20.py
    sha256: 689ef1b008090eba5ce1ef4083ef25245565ba2f3ff8b9a34372c049590e75f1
    role: context
  - path: scripts/repair_togo_commercial_score20.py
    sha256: d5e34df82098bf7558fcdd103d24d00218513488ea860952881c73240596c822
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
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
    role: context
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
    role: context
  - path: src/culturemech/match/kg_media_matcher.py
    sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
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
  selection: Authoritative batch061 index 09
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009156
targets:
- target_id: CultureMech:009156
  path: data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml
  label: chopped_meat_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml
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
  - CultureMech:009156
  command: just validate-schema data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml
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
  - CultureMech:009156
  command: just validate-strict data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml --out
    REVIEW_WORK/batch061/record09/strict.tsv --workers 1 --quiet
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
  - CultureMech:009156
  command: just validate-terms data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml
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
  - CultureMech:009156
  command: just validate-references data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsm78
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf
  accessed_at: '2026-10-28T08:34:08.688561Z'
  locator: REVIEW_WORK/batch061/source07-09/dsm78.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact cited primary medium78 and source scope; no organism-growth inference.
  snapshot_sha256: 4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0
- evidence_id: api78
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/78
  accessed_at: '2026-10-28T08:34:08.480040Z'
  locator: REVIEW_WORK/batch061/source07-09/api78.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact cited provider78; declared recipe stages distinct from variants.
  snapshot_sha256: 9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f
- evidence_id: togo2588
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2588
  accessed_at: '2026-10-28T08:34:08.050622Z'
  locator: REVIEW_WORK/batch061/source07-09/togo2588.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact TOGO2588 identity and source scope; assess safety context before
    operational conclusions.
  snapshot_sha256: 4ea53780ea689f5eda3570d8ea148c9c7ad7c90be976b205f43d71365285ef0c
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377
  accessed_at: '2026-10-28T08:34:09.085725Z'
  locator: REVIEW_WORK/batch061/source07-09/chebi15377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact supplied-form and canonical identity for ordinary CHM source review.
  snapshot_sha256: a5ab66402b598c137daa8e5c8ba95811f1619db3e0f8b4f9bd0214161bafa0fe
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527
  accessed_at: '2026-10-28T08:39:10.569237Z'
  locator: REVIEW_WORK/batch061/source07-09/chebi131527.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact existing ordinary DSM78/TOGO2588 chemical identifier and supplied-form
    scope; no organism-specific cultivation inference.
  snapshot_sha256: 0a5297c84ea9dd82508960482211f6b3c993fd8e2b83fe755dd2b23316cc4068
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806
  accessed_at: '2026-10-28T08:39:10.535254Z'
  locator: REVIEW_WORK/batch061/source07-09/chebi8806.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact existing ordinary DSM78/TOGO2588 chemical identifier and supplied-form
    scope; no organism-specific cultivation inference.
  snapshot_sha256: f2530ec9c15f59a3d132a466c9c3a899497bab0f85b996d3e27bef8612f89982
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:2509
  accessed_at: '2026-10-28T08:39:10.544308Z'
  locator: REVIEW_WORK/batch061/source07-09/chebi2509.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact existing ordinary DSM78/TOGO2588 chemical identifier and supplied-form
    scope; no organism-specific cultivation inference.
  snapshot_sha256: e3f17ac3223021a957a5e3fffb5b118a0854f9ddbc537f51f70dd61ae23ff7a7
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T08:47:52.584750Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 6ac08a8108b92bf9cf7e0cefef7a28142173087b1364368cf6996250f87488bb
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T08:47:52.584919Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 4c6946754252ce4f6dd9f30b9d02aaaaaa8e8de569f0008af9c8812e203c4fbc
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T08:47:52.584945Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T08:47:52.585262Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T08:47:52.585286Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T08:47:52.585308Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-17
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T08:47:52.585333Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: c42a888bbeef6211ce4afa6ef7e31fe7f90878cbfd00a7f2426ee6fd3b4b3344
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T08:47:52.585360Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 55d8ed0e73a795bf249384bffa162a3b7fc7090a58c376d5b0b56817fecaf9a5
- evidence_id: report-19
  kind: prior_review
  reference: reports/yaml_record_review/20260922T075541Z-CHOPPED_MEAT_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T08:47:52.585383Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: a55c034998e5e0f083675729c36d2feb03bd48e964b03a3048a9bca6d8b36c2b
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_primary_components, _ingredient_from_item, _parse_unit, _extract_preparation_steps,
    _extract_ph
  accessed_at: '2026-10-28T08:47:52.585405Z'
  support: context_only
  summary: Current importer already separates local stock sections and retains comment
    preparation. It maps ml to ML_PER_L, mg to MG_PER_L and l to L, while bare masses
    still acquire per-litre units without proof of final volume. _extract_ph reads
    root ph whereas this exact payload carries meta.ph. Credit current behavior without
    claiming it produced the historical record or fixes extraction stages automatically.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-mim
  kind: record_content
  reference: scripts/migrate_legacy_mim_to_chebi.py
  locator: _resolve_chebi, _rewrite_entry, migrate_file
  accessed_at: '2026-10-28T08:47:52.585438Z'
  support: context_only
  summary: Current migration prefers an existing CHEBI mapping, uses exact name/synonym
    plus stereochemical guard otherwise, and deliberately leaves unresolved legacy
    slots intact. A past migration event does not prove every current ingredient was
    migrated.
  snapshot_sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
- evidence_id: writer-default
  kind: record_content
  reference: src/culturemech/validation/schema_defaulter.py
  locator: apply_defaults and ingredient defaults
  accessed_at: '2026-10-28T08:47:52.585461Z'
  support: context_only
  summary: Current defaulting preserves record shape and fills missing concentrations
    with placeholders. The declared historical gas-default event is provenance, not
    source confirmation.
  snapshot_sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch061/record09/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T08:47:52.619473Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: c35b148f84d62b881c29238aaba1e1640198dbb3a78f7afcf0a99e2f5b97baa1
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch061/record09/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T08:47:52.619545Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 9805df959370ff95d0773fe14ecdfcd63a154e198d0523bffc7dd7131d647da0
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch061/record09/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T08:47:52.619597Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: c7d56672e5bbfc59b4f49f7fcafd541f28bf05d578778b501e4e182f3736eeea
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch061/record09/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T08:47:52.619636Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 96c645bf3842140fe01759610aafc54e12aca99f8b3c238cd72023a9a7e3567e
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch061/record09/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T08:47:52.619675Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 1681581c852d92b5ba229ada07f84deefe72fa59446f9584829881799f34c404
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch061/record09/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T08:47:52.619710Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 247ea0d03b925b83d523e1870fb678b411cb396a59fb89e3c458199eb4405b80
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch061/record09/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T08:47:52.619747Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch061/record09/schema-result.json
  accessed_at: '2026-10-28T08:34:16.829176Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 3e23c0e13c3a3cd22b3b7ae6853e8c967f8ad61af84c3ba9141809b504c6b87a
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch061/record09/strict-result.json
  accessed_at: '2026-10-28T08:34:17.751215Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 183856885eb7f91015eeb3a56962daf03af85fefde26b84474786007a7ab2306
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch061/record09/terms-result.json
  accessed_at: '2026-10-28T08:34:18.772755Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: fd7027573659036f228874023ee01614d62a2032704927232c3a19ce9b6e3280
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch061/record09/references-result.json
  accessed_at: '2026-10-28T08:34:19.431764Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: df2cc466a69ec0338960cbd634f6122b51d27b590d203bf55719435a2a2a876d
assessments:
- assessment_id: identity
  area: identity
  topic: Exact record/source and conditional variants
  outcome: concern
  summary: TOGO M2588 directly cites DSM78 and matches the selected owner identity.
    Its source extraction stages and agar branch are not represented faithfully; optional
    supplements and strain overrides are not general target requirements.
  target_ids:
  - CultureMech:009156
  evidence_ids:
  - target
  - owner
  - togo2588
  - dsm78
  - api78
- assessment_id: schema
  area: schema
  topic: Original native diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed once; strict zero errors
    and references zero checks do not authenticate source stage or quantity claims.
  target_ids:
  - CultureMech:009156
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 20 current concentration fields are covered by 35 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:009156
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b061-quantity-inventory-v1","target":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","quantity_field_count":20,"decisions":[{"quantity_id":"q1","label":"Input
    water","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1000","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1000","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source
    specifies an input liquid volume, not a mass or final-medium concentration. Preserve
    the extraction input separately from later filtrate makeup.","source_stage":"Initial
    extraction","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 5-5","quote":"Distilled water                                                    1000.0       ml","quote_basis":"derivative
    text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q2","label":"NaOH adjustment stock input","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"25","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"25","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source
    gives a volume of a1N solution. Neither its stock strength nor the input dose
    is a gram-per-litre amount; do not compute mass without a justified source basis.","source_stage":"Initial
    extraction","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 6-6","quote":"NaOH 1 N                                                             25.0       ml","quote_basis":"derivative
    text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"attribute\": \"1 N\",\n                        \"amount\":
    25,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"Ground
    meat extraction input","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"500","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"500","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed mass is material used before boiling, filtering and retaining two fractions.
    It is not verified as retained beef concentration in final medium; API487.805g_l
    merely uses its declared1025mL normalization.","source_stage":"Initial extraction","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 4-11","quote":"Ground beef (fat free)                                              500.0        g\nDistilled
    water                                                    1000.0       ml\nNaOH
    1 N                                                             25.0       ml\n\nUse
    lean beef or horse meat. Remove fat and connective tissue before grinding. Mix\nmeat,
    water and NaOH, then boil for 15 min with stirring. Cool to room temperature,\nskim
    fat off surface, and filter, retaining both meat particles and filtrate. To the
    filtrate\nadd water to a final volume of 1000 ml, and then add:","quote_basis":"derivative
    text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Ground beef\",\n                        \"compound_id\":
    128,\n                        \"attribute\": \"fat free\",\n                        \"amount\":
    500,\n                        \"unit\": \"g\",\n                        \"g_l\":
    487.805,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q4","label":"Yeast extract after filtrate makeup","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed batch mass is added after filtrate is made up to1000mL. No subsequent
    measured final volume is given; local G_PER_L is not independently established
    as final-medium concentration. API uses a different declared1025mL basis, not
    proof to substitute its rate.","source_stage":"Post-filtrate preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 11-14","quote":"add water to a final volume of 1000 ml, and then add:\n\nCasitone                                                              30.0       g\nYeast
    extract                                                          5.0       g","quote_basis":"derivative
    text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4.87805,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"Dipotassium
    hydrogen phosphate after filtrate makeup","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"Printed
    batch mass is supported but added after filtrate makeup. Final-medium denominator
    is not established; API1025mL normalization remains a separate provider assertion.","source_stage":"Post-filtrate
    preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 11-15","quote":"add water to a final volume of 1000 ml, and then add:\n\nCasitone                                                              30.0       g\nYeast
    extract                                                          5.0       g\nK2HPO4                                                                 5.0       g","quote_basis":"derivative
    text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4.87805,\n                        \"mmol_l\":
    28.0064,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q6","label":"Resazurin amount","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source
    gives1mg, not1g. Preserve the milligram batch amount and stage. The1000-fold mass-unit
    discrepancy is independent of the unresolved later final-medium denominator; do
    not silently normalize it to an assumed litre.","source_stage":"Post-filtrate
    preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 16-16","quote":"Resazurin                                                              1.0      mg","quote_basis":"derivative
    text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\":
    25,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.00097561,\n                        \"mmol_l\":
    0.00425677,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q7","label":"Casitone after filtrate makeup","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"30","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"Printed
    batch mass is supported but added after the filtrate makeup. Local final-medium
    G_PER_L remains unsupported; API1025mL declared normalization must not overwrite
    the preparation sequence.","source_stage":"Post-filtrate preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 11-13","quote":"add water to a final volume of 1000 ml, and then add:\n\nCasitone                                                              30.0       g","quote_basis":"derivative
    text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Casitone\",\n                        \"compound_id\":
    84,\n                        \"amount\": 30,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 29.2683,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Nitrogen
    gas condition","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"The
    variable local amount is not a mass concentration. Source specifies a gas atmosphere
    and handling condition; preserve that in preparation rather than invent a dose
    or weight/volume percent.","source_stage":"Post-filtrate preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 18-22","quote":"To make medium anoxic bring it to a boil, cool under 100%
    N2 gas atmosphere, add 0.5\ng/l L-cysteine hydrochloride and adjust pH to 7.0.
    Dispense under 100% N2 gas\natmosphere by filling 7 ml medium into anoxic Hungate-type
    tubes (for strains\ndemanding meat particles put those first into the tube (use
    1 part meat particles to 4 or\n5 parts fluid)). Autoclave at 121°C for 30 min.
    For agar slants use 15.0 g agar per","quote_basis":"derivative text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"step\": \"To make medium anoxic bring it to a boil,
    cool under 100% N2 gas atmosphere, add 0.5 g/l L-cysteine hydrochloride and adjust
    pH to 7.0. Dispense under 100% N2 gas atmosphere by filling 7 ml medium into anoxic
    Hungate-type tubes (for strains demanding meat particles put those first into
    the tube (use 1 part meat particles to 4 or 5 parts fluid)). Autoclave at 121\\u00b0C
    for 30 min. For agar slants use 15.0 g agar per 1000.0 ml medium.\"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q9","label":"Agar branch","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"15","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    explicit15g per1000mL rate is supported only for agar slants. Current unconditional
    ingredient and SOLID_AGAR classification collapse that variant into the generic
    record; preserve the branch rather than delete source-supported option.","source_stage":"Conditional
    agar branch","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 22-23","quote":"5 parts fluid)). Autoclave at 121°C for 30 min. For agar
    slants use 15.0 g agar per\n1000.0 ml medium.","quote_basis":"derivative text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"condition\": \"for solid medium\",\n                        \"amount\":
    15,\n                        \"unit\": \"g\",\n                        \"g_l\":
    14.6341,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q10","label":"L-cysteine hydrochloride direct rate","local_fields":[{"path":"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Primary
    text explicitly states0.5g/L, supporting the existing rate without inferred volume
    or hydrate. No attached evidence is present. API table0.487805g_l conflicts with
    its own preserved instruction and is not substituted.","source_stage":"Post-filtrate
    preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 18-19","quote":"To make medium anoxic bring it to a boil, cool under 100%
    N2 gas atmosphere, add 0.5\ng/l L-cysteine hydrochloride and adjust pH to 7.0.
    Dispense under 100% N2 gas","quote_basis":"derivative text"},{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"L-Cysteine HCl\",\n                        \"compound_id\":
    1157,\n                        \"condition\": \"\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.487805,\n                        \"mmol_l\": 3.09482,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"Extraction
    boil duration","local_fields":[],"decision":"evidence_only","rationale":"The initial
    boil and filtration are a separate extraction operation, not final sterilization.","source_stage":"Source-only
    preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 8-11","quote":"Use lean beef or horse meat. Remove fat and connective tissue
    before grinding. Mix\nmeat, water and NaOH, then boil for 15 min with stirring.
    Cool to room temperature,\nskim fat off surface, and filter, retaining both meat
    particles and filtrate. To the filtrate\nadd water to a final volume of 1000 ml,
    and then add:","quote_basis":"derivative text"}]},{"quantity_id":"q12","label":"Filtrate
    final makeup","local_fields":[],"decision":"evidence_only","rationale":"This is
    an explicit final volume for the filtrate stage only, before subsequent solutes.
    It does not certify final combined medium volume.","source_stage":"Source-only
    preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 10-11","quote":"skim fat off surface, and filter, retaining both meat particles
    and filtrate. To the filtrate\nadd water to a final volume of 1000 ml, and then
    add:","quote_basis":"derivative text"}]},{"quantity_id":"q13","label":"Nitrogen
    atmosphere and cysteine/pH sequence","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    the gas condition, explicit cysteine rate and generic pH separately; no inferred
    gas mass or alternative organism-specific condition.","source_stage":"Source-only
    preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 18-20","quote":"To make medium anoxic bring it to a boil, cool under 100%
    N2 gas atmosphere, add 0.5\ng/l L-cysteine hydrochloride and adjust pH to 7.0.
    Dispense under 100% N2 gas\natmosphere by filling 7 ml medium into anoxic Hungate-type
    tubes (for strains","quote_basis":"derivative text"}]},{"quantity_id":"q14","label":"Dispensing
    and optional meat-particle ratio","local_fields":[],"decision":"evidence_only","rationale":"Dispensing
    volume and particle/fluid ratios apply to the stated context only. The ratio is
    not explicitly a mass fraction and is not converted.","source_stage":"Source-only
    preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 20-22","quote":"atmosphere by filling 7 ml medium into anoxic Hungate-type
    tubes (for strains\ndemanding meat particles put those first into the tube (use
    1 part meat particles to 4 or\n5 parts fluid)). Autoclave at 121°C for 30 min.
    For agar slants use 15.0 g agar per","quote_basis":"derivative text"}]},{"quantity_id":"q15","label":"Sterilization
    stage","local_fields":[],"decision":"evidence_only","rationale":"Final sterilization
    is distinct from the initial extraction boil. No pressure is inferred from the
    printed temperature.","source_stage":"Source-only preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 22-23","quote":"5 parts fluid)). Autoclave at 121°C for 30 min. For agar
    slants use 15.0 g agar per\n1000.0 ml medium.","quote_basis":"derivative text"}]},{"quantity_id":"q16","label":"Optional
    supplement receiving basis","local_fields":[],"decision":"evidence_only","rationale":"Catalogue-dependent
    supplements are not unconditional omissions from this generic target. Primary
    gives equal printed receiving volumes for K1 or K3; API K1 volume differs and
    remains unresolved.","source_stage":"Conditional source-only stock","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 26-30","quote":"In some cases (as indicated in the catalogue) the addition
    of Haemin and Vitamin K1 or\nVitamin K3 is necessary. Add to 1000 ml of medium
    after autoclaving:\n\nHaemin solution (see below)                                         10.00       ml\nVitamin
    K1 or Vitamin K3 solution (see below)                       10.00       ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q17","label":"Haemin stock makeup","local_fields":[],"decision":"evidence_only","rationale":"Explicit
    makeup to100mL supports a stock basis. It is conditional source-only context,
    not a local ingredient or mandatory dose; no new target stock is prescribed.","source_stage":"Conditional
    source-only stock","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 32-34","quote":"Haemin solution:\nDissolve 50 mg haemin in 1 ml 1 N NaOH;
    make up to 100 ml with distilled water and\nfilter sterilize. Store refrigerated.","quote_basis":"derivative
    text"}]},{"quantity_id":"q18","label":"Vitamin K1 stock solvent and grade","local_fields":[],"decision":"evidence_only","rationale":"Printed
    vitamin volume and ethanol input are not an explicit final stock makeup. The95%
    basis is unspecified; no mass, density or final-medium conversion is asserted.","source_stage":"Conditional
    source-only stock","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 35-37","quote":"Vitamin K1 solution:\nDissolve 0.1 ml of vitamin K1 in 20
    ml 95% ethanol and filter sterilize. Store refrigerated\nin a brown bottle.","quote_basis":"derivative
    text"}]},{"quantity_id":"q19","label":"Vitamin K3 two concentration stages","local_fields":[],"decision":"evidence_only","rationale":"The
    initial and diluted concentrations are separately explicit; preserve them as stock
    stages. Do not conflate with K1, infer an ethanol percent basis, or turn an optional
    stock into a mandatory ingredient.","source_stage":"Source-only preparation","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 38-40","quote":"Vitamin K3 solution:\nDissolve 5 mg/ml of vitamin K3 in
    95% ethanol, dilute to 0.05 mg/ml in water and filter\nsterilize. Store refrigerated
    in a brown bottle.","quote_basis":"derivative text"}]},{"quantity_id":"q20","label":"Excluded
    strain-specific pH override","local_fields":[],"decision":"evidence_only","rationale":"DSM21650-only
    instruction is retained as excluded source context. It does not replace the generic
    pH and no organism-growth inference is made.","source_stage":"Excluded strain
    variant","sources":[{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 43-43","quote":"For DSM 21650 adjust pH of complete medium to 8.5.","quote_basis":"derivative
    text"}]},{"quantity_id":"q21","label":"Provider solution 123 volume","local_fields":[],"decision":"evidence_only","rationale":"Provider-declared
    volume is retained separately from textual preparation. Main1025mL is not the
    filtrate1000mL makeup; stock volumes and optional branches do not establish final-medium
    volume.","source_stage":"Provider metadata comparison","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0]","quote":"{\n                \"id\":
    123,\n                \"name\": \"Main sol. 78\",\n                \"volume\":
    1025,\n                \"recipe\": [\n                    {\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Ground beef\",\n                        \"compound_id\":
    128,\n                        \"attribute\": \"fat free\",\n                        \"amount\":
    500,\n                        \"unit\": \"g\",\n                        \"g_l\":
    487.805,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"attribute\": \"1 N\",\n                        \"amount\":
    25,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    },\n                    {\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Casitone\",\n                        \"compound_id\":
    84,\n                        \"amount\": 30,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 29.2683,\n                        \"optional\":
    0\n                    },\n                    {\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4.87805,\n                        \"optional\":
    0\n                    },\n                    {\n                        \"recipe_order\":
    6,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4.87805,\n                        \"mmol_l\":
    28.0064,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\":
    25,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.00097561,\n                        \"mmol_l\":
    0.00425677,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    8,\n                        \"compound\": \"L-Cysteine HCl\",\n                        \"compound_id\":
    1157,\n                        \"condition\": \"\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.487805,\n                        \"mmol_l\": 3.09482,\n                        \"optional\":
    0\n                    },\n                    {\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"condition\": \"for solid medium\",\n                        \"amount\":
    15,\n                        \"unit\": \"g\",\n                        \"g_l\":
    14.6341,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    10,\n                        \"solution\": \"Haemin solution\",\n                        \"solution_id\":
    124,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 1\n                    },\n                    {\n                        \"recipe_order\":
    11,\n                        \"solution\": \"Vitamin K1 solution\",\n                        \"solution_id\":
    125,\n                        \"condition\": \"alternative\",\n                        \"amount\":
    0.2,\n                        \"unit\": \"ml\",\n                        \"optional\":
    1\n                    },\n                    {\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Vitamin K3 solution\",\n                        \"solution_id\":
    5540,\n                        \"condition\": \"alternative\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"optional\":
    1\n                    }\n                ],\n                \"steps\": [\n                    {\n                        \"recipe_order\":
    8,\n                        \"step\": \"To make medium anoxic bring it to a boil,
    cool under 100% N2 gas atmosphere, add 0.5 g/l L-cysteine hydrochloride and adjust
    pH to 7.0. Dispense under 100% N2 gas atmosphere by filling 7 ml medium into anoxic
    Hungate-type tubes (for strains demanding meat particles put those first into
    the tube (use 1 part meat particles to 4 or 5 parts fluid)). Autoclave at 121\\u00b0C
    for 30 min. For agar slants use 15.0 g agar per 1000.0 ml medium.\"\n                    },\n                    {\n                        \"recipe_order\":
    10,\n                        \"step\": \"In some cases (as indicated in the catalogue)
    the addition of Haemin and Vitamin K1 or Vitamin K3 is necessary. Add to 1000
    ml of medium after autoclaving:\"\n                    },\n                    {\n                        \"recipe_order\":
    4,\n                        \"step\": \"Use lean beef or horse meat. Remove fat
    and connective tissue before grinding. Mix\\r\\nmeat, water and NaOH, then boil
    for 15 min with stirring. Cool to room temperature,\\r\\nskim fat off surface,
    and filter, retaining both meat particles and filtrate. To the filtrate\\r\\nadd
    water to a final volume of 1000 ml, and then add:\"\n                    }\n                ],\n                \"equipment\":
    {\n                    \"429\": \"Hungate tubes\",\n                    \"1480\":
    \"Filter\",\n                    \"3487\": \"Autoclave\",\n                    \"3958\":
    \"Gassing station\"\n                }\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"Provider
    solution 124 volume","local_fields":[],"decision":"evidence_only","rationale":"Provider-declared
    volume is retained separately from textual preparation. Main1025mL is not the
    filtrate1000mL makeup; stock volumes and optional branches do not establish final-medium
    volume.","source_stage":"Provider metadata comparison","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[1]","quote":"{\n                \"id\":
    124,\n                \"name\": \"Haemin solution\",\n                \"volume\":
    100,\n                \"recipe\": [\n                    {\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Haemin\",\n                        \"compound_id\":
    149,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    0.766989,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    2,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"attribute\": \"1 N\",\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    },\n                    {\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 100,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }\n                ],\n                \"steps\":
    [\n                    {\n                        \"step\": \"Dissolve 50 mg haemin
    in 1 ml 1 N NaOH; make up to 100 ml with distilled water and filter sterilize.
    Store refrigerated.\"\n                    }\n                ],\n                \"equipment\":
    {\n                    \"1875\": \"Filter\"\n                }\n            }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q23","label":"Provider source-only Haemin solution /
    Haemin","local_fields":[],"decision":"evidence_only","rationale":"Exact returned
    amount/unit/g_l/mmol_l/attribute retained as provider assertions only. Scope is
    optional stock, not a selected local field. Primary-text stage controls take precedence
    over unsupported final-volume, ethanol density or percentage assumptions.","source_stage":"Conditional
    provider stock","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Haemin\",\n                        \"compound_id\":
    149,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    0.766989,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q24","label":"Provider source-only Haemin solution /
    NaOH","local_fields":[],"decision":"evidence_only","rationale":"Exact returned
    amount/unit/g_l/mmol_l/attribute retained as provider assertions only. Scope is
    optional stock, not a selected local field. Primary-text stage controls take precedence
    over unsupported final-volume, ethanol density or percentage assumptions.","source_stage":"Conditional
    provider stock","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"attribute\": \"1 N\",\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"Provider
    source-only Haemin solution / Distilled water","local_fields":[],"decision":"evidence_only","rationale":"Exact
    returned amount/unit/g_l/mmol_l/attribute retained as provider assertions only.
    Scope is optional stock, not a selected local field. Primary-text stage controls
    take precedence over unsupported final-volume, ethanol density or percentage assumptions.","source_stage":"Conditional
    provider stock","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 100,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q26","label":"Provider solution 125 volume","local_fields":[],"decision":"evidence_only","rationale":"Provider-declared
    volume is retained separately from textual preparation. Main1025mL is not the
    filtrate1000mL makeup; stock volumes and optional branches do not establish final-medium
    volume.","source_stage":"Provider metadata comparison","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[2]","quote":"{\n                \"id\":
    125,\n                \"name\": \"Vitamin K1 solution\",\n                \"volume\":
    20,\n                \"recipe\": [\n                    {\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Vitamin K1\",\n                        \"compound_id\":
    150,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Ethanol\",\n                        \"compound_id\":
    201,\n                        \"attribute\": \"95 %\",\n                        \"amount\":
    20,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    950,\n                        \"mmol_l\": 20620.8,\n                        \"optional\":
    0\n                    }\n                ],\n                \"steps\": [\n                    {\n                        \"step\":
    \"Dissolve 0.1 ml of vitamin K1 in 20 ml 95% ethanol and filter sterilize. Store
    refrigerated in a brown bottle.\"\n                    }\n                ],\n                \"equipment\":
    {\n                    \"277\": \"Filter\"\n                }\n            }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q27","label":"Provider source-only Vitamin K1 solution
    / Vitamin K1","local_fields":[],"decision":"evidence_only","rationale":"Exact
    returned amount/unit/g_l/mmol_l/attribute retained as provider assertions only.
    Scope is optional stock, not a selected local field. Primary-text stage controls
    take precedence over unsupported final-volume, ethanol density or percentage assumptions.","source_stage":"Conditional
    provider stock","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Vitamin K1\",\n                        \"compound_id\":
    150,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q28","label":"Provider source-only Vitamin K1 solution
    / Ethanol","local_fields":[],"decision":"evidence_only","rationale":"Exact returned
    amount/unit/g_l/mmol_l/attribute retained as provider assertions only. Scope is
    optional stock, not a selected local field. Primary-text stage controls take precedence
    over unsupported final-volume, ethanol density or percentage assumptions.","source_stage":"Conditional
    provider stock","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Ethanol\",\n                        \"compound_id\":
    201,\n                        \"attribute\": \"95 %\",\n                        \"amount\":
    20,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    950,\n                        \"mmol_l\": 20620.8,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"Provider
    solution 5540 volume","local_fields":[],"decision":"evidence_only","rationale":"Provider-declared
    volume is retained separately from textual preparation. Main1025mL is not the
    filtrate1000mL makeup; stock volumes and optional branches do not establish final-medium
    volume.","source_stage":"Provider metadata comparison","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[3]","quote":"{\n                \"id\":
    5540,\n                \"name\": \"Vitamin K3 solution\",\n                \"volume\":
    100,\n                \"recipe\": [\n                    {\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Vitamin K3\",\n                        \"compound_id\":
    2086,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"optional\":
    0\n                    },\n                    {\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Ethanol\",\n                        \"compound_id\":
    201,\n                        \"attribute\": \"95%\",\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    9.5,\n                        \"mmol_l\": 206.208,\n                        \"optional\":
    0\n                    },\n                    {\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Water\",\n                        \"compound_id\":
    754,\n                        \"amount\": 100,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }\n                ],\n                \"steps\":
    [\n                    {\n                        \"step\": \"Dissolve 5 mg vitamin
    K3 in 1 ml 95% ethanol, dilute to 0.05 mg/ml in water and filter sterilize. Store
    refrigerated in a brown bottle.\"\n                    }\n                ]\n            }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q30","label":"Provider source-only Vitamin K3 solution
    / Vitamin K3","local_fields":[],"decision":"evidence_only","rationale":"Exact
    returned amount/unit/g_l/mmol_l/attribute retained as provider assertions only.
    Scope is optional stock, not a selected local field. Primary-text stage controls
    take precedence over unsupported final-volume, ethanol density or percentage assumptions.","source_stage":"Conditional
    provider stock","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Vitamin K3\",\n                        \"compound_id\":
    2086,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"Provider
    source-only Vitamin K3 solution / Ethanol","local_fields":[],"decision":"evidence_only","rationale":"Exact
    returned amount/unit/g_l/mmol_l/attribute retained as provider assertions only.
    Scope is optional stock, not a selected local field. Primary-text stage controls
    take precedence over unsupported final-volume, ethanol density or percentage assumptions.","source_stage":"Conditional
    provider stock","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Ethanol\",\n                        \"compound_id\":
    201,\n                        \"attribute\": \"95%\",\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    9.5,\n                        \"mmol_l\": 206.208,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q32","label":"Provider
    source-only Vitamin K3 solution / Water","local_fields":[],"decision":"evidence_only","rationale":"Exact
    returned amount/unit/g_l/mmol_l/attribute retained as provider assertions only.
    Scope is optional stock, not a selected local field. Primary-text stage controls
    take precedence over unsupported final-volume, ethanol density or percentage assumptions.","source_stage":"Conditional
    provider stock","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Water\",\n                        \"compound_id\":
    754,\n                        \"amount\": 100,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q33","label":"Provider optional receiving row 9","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    optional and alternative flags. API K1 addition0.2mL differs from the primary
    printed10mL; no recommendation or conversion resolves this source discrepancy.
    Haemin/K3 rows remain separate.","source_stage":"Conditional receiving dose; provider
    comparison","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"solution\": \"Haemin solution\",\n                        \"solution_id\":
    124,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 1\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 26-30","quote":"In some cases (as indicated in the catalogue) the addition
    of Haemin and Vitamin K1 or\nVitamin K3 is necessary. Add to 1000 ml of medium
    after autoclaving:\n\nHaemin solution (see below)                                         10.00       ml\nVitamin
    K1 or Vitamin K3 solution (see below)                       10.00       ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q34","label":"Provider optional receiving row 10","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    optional and alternative flags. API K1 addition0.2mL differs from the primary
    printed10mL; no recommendation or conversion resolves this source discrepancy.
    Haemin/K3 rows remain separate.","source_stage":"Conditional receiving dose; provider
    comparison","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"solution\": \"Vitamin K1 solution\",\n                        \"solution_id\":
    125,\n                        \"condition\": \"alternative\",\n                        \"amount\":
    0.2,\n                        \"unit\": \"ml\",\n                        \"optional\":
    1\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 26-30","quote":"In some cases (as indicated in the catalogue) the addition
    of Haemin and Vitamin K1 or\nVitamin K3 is necessary. Add to 1000 ml of medium
    after autoclaving:\n\nHaemin solution (see below)                                         10.00       ml\nVitamin
    K1 or Vitamin K3 solution (see below)                       10.00       ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q35","label":"Provider optional receiving row 11","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    optional and alternative flags. API K1 addition0.2mL differs from the primary
    printed10mL; no recommendation or conversion resolves this source discrepancy.
    Haemin/K3 rows remain separate.","source_stage":"Conditional receiving dose; provider
    comparison","sources":[{"evidence_id":"api78","reference":"https://mediadive.dsmz.de/rest/medium/78","raw_path":"REVIEW_WORK/batch061/source07-09/api78.raw","raw_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","text_sha256":"9b98095d28058f8064d0da708ee20318ac3daa3d62348174d60b699483f1761f","accessed_at":"2026-10-28T08:34:08.480040Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Vitamin K3 solution\",\n                        \"solution_id\":
    5540,\n                        \"condition\": \"alternative\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"optional\":
    1\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm78","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/dsm78.raw","raw_sha256":"4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0","text_sha256":"4e8b1639db45080ec2095a9af2b2bdc3af3a602e7f29ef0993ee6bb7cb1e2a97","accessed_at":"2026-10-28T08:34:08.688561Z","locator":"dsm78.txt
    lines 26-30","quote":"In some cases (as indicated in the catalogue) the addition
    of Haemin and Vitamin K1 or\nVitamin K3 is necessary. Add to 1000 ml of medium
    after autoclaving:\n\nHaemin solution (see below)                                         10.00       ml\nVitamin
    K1 or Vitamin K3 solution (see below)                       10.00       ml","quote_basis":"derivative
    text"}]}],"document_scopes":{"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All four distinct asserted CHEBI IDs resolve to current nonobsolete scientific
    objects with exact canonical labels. Water, generic agar and dipotassium hydrogen
    phosphate are compatible with the printed forms; Resazurin is neutral CHEBI8806
    and the source does not explicitly specify sodium salt, so no sodium-form contradiction
    is invented. L-cysteine hydrochloride has an unresolved legacy key and unspecified
    hydrate; exact current MIM absence is not a historical mapping verdict. Primary
    CHEBI presence is8/20 ingredient instances, current secondary CHEBI links8/20,
    and two legacy slots are counted separately; label agreement does not validate
    the recipe.
  target_ids:
  - CultureMech:009156
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: All three inspected historical reports were read in full. September source
    leads and October unassessed quantity rows are derivative review history, not
    new source captures or native executions. Fresh PDF/API/TOGO sources are independently
    read; no attached current literal evidence claims exist. The existing migration
    event correctly records four replaced links and does not certify the unresolved
    fifth legacy slot. Current importer unit, stock and comment handling is credited;
    its present code cannot reconstruct the older execution.
  target_ids:
  - CultureMech:009156
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-009156-source-unit-errors
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Source liquid and milligram units were replaced by mass concentrations
  description: Water and1N NaOH are source input volumes, while resazurin is a milligram
    batch amount. The target and owner encode all three as G_PER_L. Reconcile the
    original units and extraction/addition stages, retaining the independently confirmed
    resazurin mass-unit error without manufacturing a final-medium denominator.
  target_ids:
  - CultureMech:009156
  field_paths:
  - ingredients[0].concentration
  - ingredients[1].concentration
  - ingredients[5].concentration
  evidence_ids:
  - target
  - owner
  - dsm78
  - togo2588
  - api78
  - quantities
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-009156-extraction-stage-loss
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Flat composition loses the meat-extraction and filtrate stages
  description: The initial meat, water and alkaline input precede boiling, filtering
    and retaining both fractions. Only the filtrate is explicitly made up before the
    later batch additions. The current flat final-medium ingredients cannot establish
    retained meat concentration or the later denominator. Model the source sequence
    and preserve unresolved total volume; do not adopt API1025mL normalization as
    measured final volume.
  target_ids:
  - CultureMech:009156
  field_paths:
  - ingredients
  - preparation_steps
  evidence_ids:
  - dsm78
  - togo2588
  - api78
  - quantities
  - writer-togo
  rule_id: review-yaml-record/representation
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-009156-agar-variant-collapse
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Agar-slant option is made unconditional
  description: The source explicitly qualifies agar as an agar-slant branch, whereas
    current owner and target assert SOLID_AGAR and unconditional agar. Preserve base
    versus agar variant scope without inferring organism suitability or transferring
    optional vitamin/haemin additions.
  target_ids:
  - CultureMech:009156
  field_paths:
  - physical_state
  - ingredients[8]
  evidence_ids:
  - target
  - owner
  - dsm78
  - api78
  - quantities
  rule_id: review-yaml-record/identity
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-009156-missing-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source preparation and pH are absent
  description: Current records omit the source preparation sequence, including the
    extraction, later gas handling, explicit cysteine addition, generic pH, dispensing
    and sterilization. Preserve the complete generic sequence with conditional particle
    and agar scope. The DSM21650 override is excluded, and catalogue-dependent haemin/vitamin
    stocks remain optional source context with an unresolved K1 provider discrepancy.
    Current importer already retains comment steps and separates stock sections; this
    does not prove historical execution or solve source-stage arithmetic. Its pH reader
    expects root ph while this payload has meta.ph.
  target_ids:
  - CultureMech:009156
  field_paths:
  - preparation_steps
  - ph_value
  - sterilization
  - ingredients[7]
  evidence_ids:
  - dsm78
  - togo2588
  - api78
  - quantities
  - writer-togo
  rule_id: review-yaml-record/completeness
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml
    role: maintained source
- finding_id: f5
  issue_key: culturemech-009156-legacy-cysteine-scope
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: One legacy ingredient identifier remains unresolved
  description: The current L-cysteine hydrochloride slot still uses legacy MediaIngredientMech000459
    without a primary CHEBI term. The packaged current index cannot authenticate a
    historical numeric key by its absence; source does not specify hydrate. Current
    migration deliberately leaves unresolved entries unchanged, so retain its history
    and seek exact form/stereochemistry evidence before any future mapping. Do not
    guess a hydrate or generic cysteine replacement.
  target_ids:
  - CultureMech:009156
  field_paths:
  - ingredients[9].mediaingredientmech_term
  evidence_ids:
  - target
  - owner
  - groundings
  - mim
  - mim-meta
  - writer-mim
  - dsm78
  rule_id: review-yaml-record/grounding
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml
    role: maintained source
actions:
- action_id: a1
  description: Water and1N NaOH are source input volumes, while resazurin is a milligram
    batch amount. The target and owner encode all three as G_PER_L. Reconcile the
    original units and extraction/addition stages, retaining the independently confirmed
    resazurin mass-unit error without manufacturing a final-medium denominator.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009156
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml
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
  description: The initial meat, water and alkaline input precede boiling, filtering
    and retaining both fractions. Only the filtrate is explicitly made up before the
    later batch additions. The current flat final-medium ingredients cannot establish
    retained meat concentration or the later denominator. Model the source sequence
    and preserve unresolved total volume; do not adopt API1025mL normalization as
    measured final volume.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009156
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml
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
  description: The source explicitly qualifies agar as an agar-slant branch, whereas
    current owner and target assert SOLID_AGAR and unconditional agar. Preserve base
    versus agar variant scope without inferring organism suitability or transferring
    optional vitamin/haemin additions.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009156
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml
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
  description: Current records omit the source preparation sequence, including the
    extraction, later gas handling, explicit cysteine addition, generic pH, dispensing
    and sterilization. Preserve the complete generic sequence with conditional particle
    and agar scope. The DSM21650 override is excluded, and catalogue-dependent haemin/vitamin
    stocks remain optional source context with an unresolved K1 provider discrepancy.
    Current importer already retains comment steps and separates stock sections; this
    does not prove historical execution or solve source-stage arithmetic. Its pH reader
    expects root ph while this payload has meta.ph.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009156
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml
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
  description: The current L-cysteine hydrochloride slot still uses legacy MediaIngredientMech000459
    without a primary CHEBI term. The packaged current index cannot authenticate a
    historical numeric key by its absence; source does not specify hydrate. Current
    migration deliberately leaves unresolved entries unchanged, so retain its history
    and seek exact form/stereochemistry evidence before any future mapping. Do not
    guess a hydrate or generic cysteine replacement.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009156
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml
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
- Full current DSM78 PDF consists of one page, read as text and rendered image. No
  second page or paper is claimed.
- API main volume1025mL and its normalized g_l conflict with preparation-stage bases
  and the explicit cysteine rate. API K1 receiving volume differs from the PDF. These
  provider discrepancies remain unresolved; no speculative normalization is recommended.
- Optional haemin and alternative K stocks are source-only controls, not mandatory
  missing ingredients. The DSM21650-specific override is excluded from generic findings.
- No species, strain growth, optimization or experimental suitability is inferred
  from this generic source.
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
