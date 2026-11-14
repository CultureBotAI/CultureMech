# Scientific review: DESULFITOBACTERIUM HAFNIENSE medium

- Review: 20261028T174513Z-culturemech-006363-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T17:19:38.449677Z
- Finished UTC: 2026-10-28T17:45:13.782316Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Three major stock-boundary, source-condition and supplied-form issues plus one minor provenance follow-up remain. The DSM owner main rates and preparation are credited at their exact scope; the merged KOMODO branch remains partial. No recipe or historical event was edited.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch073 index 10
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006363 | data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml | generated | desulfitobacterium_hafniense_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:006363 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:006363 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:006363 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:006363 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### DSM accession supported; exact KOMODO version incomplete

identity: concern. Targets: CultureMech:006363.

DSM720 PDF and current provider agree on accession/title. The historical KOMODO row maps720 toDSM720, but current exact detail and catalogue routes returned403; catalogue identity alone does not resolve the condition conflict.

### Complex liquid formulation with conflicting oxygen note

consistency: concern. Targets: CultureMech:006363.

Complex/undefined/liquid agrees with the yeast-containing DSM formulation. Aerobic: Yes is incompatible with that source preparation and remains source-specific unresolved metadata, not an organism-growth assertion.

### Original diagnostics

schema: supported. Targets: CultureMech:006363.

All four original canonical commands passed once; references checked zero. These shape checks do not authenticate formulation equivalence.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:006363.

99 current concentration fields are covered by 56 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b073-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","quantity_field_count":99,"decisions":[{"quantity_id":"q1","label":"NH4Cl DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The uncited rate matches the explicit current provider g_l normalization at1003 mL. The primary independently supports its batch mass or stock dose, but1 L input water is not an experimental final-volume statement. Retain both bases without inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 3-3","quote":"NH4Cl                                                    1.00        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\": 18.6392,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"NH4Cl unresolved KOMODO/selected layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The number matches copied DSM provider data, but exact KOMODO conditions/version remain unresolved: current detail and catalogue routes returned403, and historical review explicitly retained the pH/source-boundary conflict. Equal copied numbers do not authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 3-3","quote":"NH4Cl                                                    1.00        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\": 18.6392,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"NaCl DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.0997009","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The uncited rate matches the explicit current provider g_l normalization at1003 mL. The primary independently supports its batch mass or stock dose, but1 L input water is not an experimental final-volume statement. Retain both bases without inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 4-4","quote":"NaCl                                                     0.10        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0997009,\n                        \"mmol_l\": 1.70604,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"NaCl unresolved KOMODO/selected layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.0997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.0997009","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The number matches copied DSM provider data, but exact KOMODO conditions/version remain unresolved: current detail and catalogue routes returned403, and historical review explicitly retained the pH/source-boundary conflict. Equal copied numbers do not authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 4-4","quote":"NaCl                                                     0.10        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0997009,\n                        \"mmol_l\": 1.70604,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"MgCl2 x 6 H2O DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.0997009","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The uncited rate matches the explicit current provider g_l normalization at1003 mL. The primary independently supports its batch mass or stock dose, but1 L input water is not an experimental final-volume statement. Retain both bases without inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 5-5","quote":"MgCl2 x 6 H2O                                            0.10        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0997009,\n                        \"mmol_l\": 0.490405,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"MgCl2 x 6 H2O unresolved KOMODO/selected layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.0997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.0997009","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The number matches copied DSM provider data, but exact KOMODO conditions/version remain unresolved: current detail and catalogue routes returned403, and historical review explicitly retained the pH/source-boundary conflict. Equal copied numbers do not authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 5-5","quote":"MgCl2 x 6 H2O                                            0.10        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0997009,\n                        \"mmol_l\": 0.490405,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"CaCl2 x 2 H2O DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.0498504","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The uncited rate matches the explicit current provider g_l normalization at1003 mL. The primary independently supports its batch mass or stock dose, but1 L input water is not an experimental final-volume statement. Retain both bases without inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 6-6","quote":"CaCl2 x 2 H2O                                            0.05        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0498504,\n                        \"mmol_l\": 0.339084,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"CaCl2 x 2 H2O unresolved KOMODO/selected layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.0498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.0498504","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The number matches copied DSM provider data, but exact KOMODO conditions/version remain unresolved: current detail and catalogue routes returned403, and historical review explicitly retained the pH/source-boundary conflict. Equal copied numbers do not authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 6-6","quote":"CaCl2 x 2 H2O                                            0.05        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0498504,\n                        \"mmol_l\": 0.339084,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"K2HPO4 x 3 H2O DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.398804","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The uncited rate matches the explicit current provider g_l normalization at1003 mL. The primary independently supports its batch mass or stock dose, but1 L input water is not an experimental final-volume statement. Retain both bases without inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 7-7","quote":"K2HPO4 x 3 H2O                                           0.40        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"K2HPO4 x 3 H2O\",\n                        \"compound_id\": 244,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.398804,\n                        \"mmol_l\": 2.28966,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"K2HPO4 x 3 H2O unresolved KOMODO/selected layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.398804","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.398804","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The number matches copied DSM provider data, but exact KOMODO conditions/version remain unresolved: current detail and catalogue routes returned403, and historical review explicitly retained the pH/source-boundary conflict. Equal copied numbers do not authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 7-7","quote":"K2HPO4 x 3 H2O                                           0.40        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"K2HPO4 x 3 H2O\",\n                        \"compound_id\": 244,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.398804,\n                        \"mmol_l\": 2.28966,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"Yeast extract DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The uncited rate matches the explicit current provider g_l normalization at1003 mL. The primary independently supports its batch mass or stock dose, but1 L input water is not an experimental final-volume statement. Retain both bases without inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 10-10","quote":"Yeast extract                                            1.00        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"Yeast extract unresolved KOMODO/selected layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The number matches copied DSM provider data, but exact KOMODO conditions/version remain unresolved: current detail and catalogue routes returned403, and historical review explicitly retained the pH/source-boundary conflict. Equal copied numbers do not authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 10-10","quote":"Yeast extract                                            1.00        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"Sodium resazurin DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The uncited rate matches the explicit current provider g_l normalization at1003 mL. The primary independently supports its batch mass or stock dose, but1 L input water is not an experimental final-volume statement. Retain both bases without inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 11-11","quote":"Sodium resazurin (0.1% w/v)                              0.50       ml","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"Sodium resazurin unresolved KOMODO/selected layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The number matches copied DSM provider data, but exact KOMODO conditions/version remain unresolved: current detail and catalogue routes returned403, and historical review explicitly retained the pH/source-boundary conflict. Equal copied numbers do not authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 11-11","quote":"Sodium resazurin (0.1% w/v)                              0.50       ml","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"NaHCO3 DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"2.59222","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The uncited rate matches the explicit current provider g_l normalization at1003 mL. The primary independently supports its batch mass or stock dose, but1 L input water is not an experimental final-volume statement. Retain both bases without inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 12-12","quote":"NaHCO3                                                   2.60        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 2.6,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.59222,\n                        \"mmol_l\": 30.8572,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"NaHCO3 unresolved KOMODO/selected layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"2.59222","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"2.59222","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The number matches copied DSM provider data, but exact KOMODO conditions/version remain unresolved: current detail and catalogue routes returned403, and historical review explicitly retained the pH/source-boundary conflict. Equal copied numbers do not authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 12-12","quote":"NaHCO3                                                   2.60        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 2.6,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.59222,\n                        \"mmol_l\": 30.8572,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q17","label":"Na-pyruvate DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"2.49252","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The uncited rate matches the explicit current provider g_l normalization at1003 mL. The primary independently supports its batch mass or stock dose, but1 L input water is not an experimental final-volume statement. Retain both bases without inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 13-13","quote":"Na-pyruvate                                              2.50        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na-pyruvate\",\n                        \"compound_id\": 113,\n                        \"amount\": 2.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.49252,\n                        \"mmol_l\": 22.6502,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q18","label":"Na-pyruvate unresolved KOMODO/selected layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"2.49252","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"2.49252","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The number matches copied DSM provider data, but exact KOMODO conditions/version remain unresolved: current detail and catalogue routes returned403, and historical review explicitly retained the pH/source-boundary conflict. Equal copied numbers do not authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 13-13","quote":"Na-pyruvate                                              2.50        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na-pyruvate\",\n                        \"compound_id\": 113,\n                        \"amount\": 2.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.49252,\n                        \"mmol_l\": 22.6502,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q19","label":"Na2S2O3 x 5 H2O DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1.24626","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The uncited rate matches the explicit current provider g_l normalization at1003 mL. The primary independently supports its batch mass or stock dose, but1 L input water is not an experimental final-volume statement. Retain both bases without inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 14-14","quote":"Na2S2O3 x 5 H2O                                          1.25        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2S2O3 x 5 H2O\",\n                        \"compound_id\": 65,\n                        \"amount\": 1.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.24626,\n                        \"mmol_l\": 5.02148,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q20","label":"Na2S2O3 x 5 H2O unresolved KOMODO/selected layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1.24626","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1.24626","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The number matches copied DSM provider data, but exact KOMODO conditions/version remain unresolved: current detail and catalogue routes returned403, and historical review explicitly retained the pH/source-boundary conflict. Equal copied numbers do not authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 14-14","quote":"Na2S2O3 x 5 H2O                                          1.25        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2S2O3 x 5 H2O\",\n                        \"compound_id\": 65,\n                        \"amount\": 1.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.24626,\n                        \"mmol_l\": 5.02148,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q21","label":"Na2S x 9 H2O DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.299103","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The uncited rate matches the explicit current provider g_l normalization at1003 mL. The primary independently supports its batch mass or stock dose, but1 L input water is not an experimental final-volume statement. Retain both bases without inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 16-16","quote":"Na2S x 9 H2O                                             0.30        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\": 1.24532,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"Na2S x 9 H2O unresolved KOMODO/selected layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.299103","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.299103","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The number matches copied DSM provider data, but exact KOMODO conditions/version remain unresolved: current detail and catalogue routes returned403, and historical review explicitly retained the pH/source-boundary conflict. Equal copied numbers do not authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 16-16","quote":"Na2S x 9 H2O                                             0.30        g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\": 1.24532,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"Na2-EDTA x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"5.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"5.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"5.2","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an SL11 stock rate, flattened into the receiving medium. The primary explicitly makes this stock up to1000 mL, supporting its stock g/L values; retain the separate1 mL receiving dose, not direct-medium stock strength. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"SL11 stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 30-30","quote":"Na2-EDTA x 2 H2O                                         5.20       g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\": 676,\n                        \"amount\": 5.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\": 15.4667,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\": 1474,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an SL11 stock rate, flattened into the receiving medium. The primary explicitly makes this stock up to1000 mL, supporting its stock g/L values; retain the separate1 mL receiving dose, not direct-medium stock strength. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"SL11 stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 31-31","quote":"FeCl2 x 4 H2O                                            1.50       g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\": 1474,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an SL11 stock rate, flattened into the receiving medium. The primary explicitly makes this stock up to1000 mL, supporting its stock g/L values; retain the separate1 mL receiving dose, not direct-medium stock strength. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"SL11 stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 32-32","quote":"ZnCl2                                                   70.00      mg","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\": 1474,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an SL11 stock rate, flattened into the receiving medium. The primary explicitly makes this stock up to1000 mL, supporting its stock g/L values; retain the separate1 mL receiving dose, not direct-medium stock strength. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"SL11 stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 33-33","quote":"MnCl2 x 4 H2O                                          100.00      mg","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\": 1474,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an SL11 stock rate, flattened into the receiving medium. The primary explicitly makes this stock up to1000 mL, supporting its stock g/L values; retain the separate1 mL receiving dose, not direct-medium stock strength. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"SL11 stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 34-34","quote":"H3BO3                                                    6.00      mg","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\": 1474,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an SL11 stock rate, flattened into the receiving medium. The primary explicitly makes this stock up to1000 mL, supporting its stock g/L values; retain the separate1 mL receiving dose, not direct-medium stock strength. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"SL11 stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 35-35","quote":"CoCl2 x 6 H2O                                          190.00      mg","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\": 1474,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an SL11 stock rate, flattened into the receiving medium. The primary explicitly makes this stock up to1000 mL, supporting its stock g/L values; retain the separate1 mL receiving dose, not direct-medium stock strength. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"SL11 stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 36-36","quote":"CuCl2 x 2 H2O                                            2.00      mg","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\": 1474,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an SL11 stock rate, flattened into the receiving medium. The primary explicitly makes this stock up to1000 mL, supporting its stock g/L values; retain the separate1 mL receiving dose, not direct-medium stock strength. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"SL11 stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 37-37","quote":"NiCl2 x 6 H2O                                           24.00      mg","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\": 1474,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is an SL11 stock rate, flattened into the receiving medium. The primary explicitly makes this stock up to1000 mL, supporting its stock g/L values; retain the separate1 mL receiving dose, not direct-medium stock strength. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"SL11 stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 38-38","quote":"Na2MoO4 x 2 H2O                                         36.00      mg","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\": 1474,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q32","label":"NaOH","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is a Se/W stock input/provider stock g_l value, flattened into the receiving medium. The primary lists1000 mL input water without a separate final makeup. Preserve its source mass/stage and1 mL receiving dose without final-medium arithmetic. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"Se/W stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 56-56","quote":"NaOH                                        0.50    g","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q33","label":"Na2SeO3 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.003","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is a Se/W stock input/provider stock g_l value, flattened into the receiving medium. The primary lists1000 mL input water without a separate final makeup. Preserve its source mass/stage and1 mL receiving dose without final-medium arithmetic. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"Se/W stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 57-57","quote":"Na2SeO3 x 5 H2O                             3.00   mg","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q34","label":"Na2WO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is a Se/W stock input/provider stock g_l value, flattened into the receiving medium. The primary lists1000 mL input water without a separate final makeup. Preserve its source mass/stage and1 mL receiving dose without final-medium arithmetic. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"Se/W stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 58-58","quote":"Na2WO4 x 2 H2O                              4.00   mg","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q35","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to Wolin vitamin stock10x, not the receiving medium at stock strength. Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000 mL water is input, not an independent final-stock-volume statement. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 63-63","quote":"Biotin                                     20.00   mg","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q36","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to Wolin vitamin stock10x, not the receiving medium at stock strength. Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000 mL water is input, not an independent final-stock-volume statement. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 64-64","quote":"Folic acid                                 20.00   mg","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q37","label":"Pyridoxine hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to Wolin vitamin stock10x, not the receiving medium at stock strength. Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000 mL water is input, not an independent final-stock-volume statement. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 65-65","quote":"Pyridoxine hydrochloride                  100.00   mg","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q38","label":"Thiamine HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to Wolin vitamin stock10x, not the receiving medium at stock strength. Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000 mL water is input, not an independent final-stock-volume statement. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 66-66","quote":"Thiamine HCl                               50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to Wolin vitamin stock10x, not the receiving medium at stock strength. Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000 mL water is input, not an independent final-stock-volume statement. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 67-67","quote":"Riboflavin                                 50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q40","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to Wolin vitamin stock10x, not the receiving medium at stock strength. Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000 mL water is input, not an independent final-stock-volume statement. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 68-68","quote":"Nicotinic acid                             50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q41","label":"Calcium D-(+)-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to Wolin vitamin stock10x, not the receiving medium at stock strength. Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000 mL water is input, not an independent final-stock-volume statement. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 69-69","quote":"Calcium D-(+)-pantothenate                 50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q42","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.001","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to Wolin vitamin stock10x, not the receiving medium at stock strength. Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000 mL water is input, not an independent final-stock-volume statement. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 70-70","quote":"Vitamin B12                                 1.00   mg","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q43","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to Wolin vitamin stock10x, not the receiving medium at stock strength. Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000 mL water is input, not an independent final-stock-volume statement. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 71-71","quote":"p-Aminobenzoic acid                        50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q44","label":"(DL)-alpha-Lipoic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to Wolin vitamin stock10x, not the receiving medium at stock strength. Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000 mL water is input, not an independent final-stock-volume statement. The KOMODO source branch still requires identity/condition reconciliation; its copied entries are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 72-72","quote":"(DL)-alpha-Lipoic acid                     50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q45","label":"DSM pH range","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ph_range.min","stored":7.0},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ph_range.max","stored":7.2}],"decision":"evidence_only","rationale":"The existing7.0–7.2 range is supported and must be retained at the main-medium stage. It is distinct from SL11 pH7 then6.0.","source_stage":"main pH","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 19-24","quote":"Dissolve ingredients (except bicarbonate, pyruvate, thiosulfate, vitamins and sulfide), then\nsparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic.\nAdd bicarbonate and adjust pH to 7.0 - 7.2, then dispense under 80% N2 and 20% CO2 gas\natmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Prior to use add\npyruvate, thiosulfate, vitamins, and sulfide from sterile anoxic stock solutions prepared\nunder 100% N2 gas. Stock solutions of pyruvate and vitamins are sterilized by filtration.","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Dissolve ingredients (except bicarbonate, pyruvate, thiosulfate, vitamins and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add bicarbonate and adjust pH to 7.0 - 7.2, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Prior to use add pyruvate, thiosulfate, vitamins, and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Stock solutions of pyruvate and vitamins are sterilized by filtration.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q46","label":"Selected/KOMODO pH7","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ph_value","stored":7.0},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ph_value","stored":7.0}],"decision":"unsupported","rationale":"7.0 lies inside the DSM range but does not establish equivalence of the KOMODO branch or justify losing the DSM range. Historical catalogue pH is derivative identity context; exact current route is unavailable.","source_stage":"source-specific pH reconciliation","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 19-24","quote":"Dissolve ingredients (except bicarbonate, pyruvate, thiosulfate, vitamins and sulfide), then\nsparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic.\nAdd bicarbonate and adjust pH to 7.0 - 7.2, then dispense under 80% N2 and 20% CO2 gas\natmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Prior to use add\npyruvate, thiosulfate, vitamins, and sulfide from sterile anoxic stock solutions prepared\nunder 100% N2 gas. Stock solutions of pyruvate and vitamins are sterilized by filtration.","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.medium","quote":"{\n            \"id\": 720,\n            \"name\": \"DESULFITOBACTERIUM HAFNIENSE MEDIUM\",\n            \"complex_medium\": \"yes\",\n            \"min_pH\": 7,\n            \"max_pH\": 7.2,\n            \"source\": \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf\"\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q47","label":"Retained DSM main preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"preparation_steps[0].description","stored":"Dissolve ingredients (except bicarbonate, pyruvate, thiosulfate, vitamins and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add bicarbonate and adjust pH to 7.0 - 7.2, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Prior to use add pyruvate, thiosulfate, vitamins, and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Stock solutions of pyruvate and vitamins are sterilized by filtration."}],"decision":"evidence_only","rationale":"The full existing description is source-supported: retain its80/20 gas mixture,30–45 min sparging, pH range, separate100% N2 stocks and filter-sterilization exceptions. The generated record loses this description; do not call it absent from the maintained DSM owner.","source_stage":"DSM main preparation","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 19-24","quote":"Dissolve ingredients (except bicarbonate, pyruvate, thiosulfate, vitamins and sulfide), then\nsparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic.\nAdd bicarbonate and adjust pH to 7.0 - 7.2, then dispense under 80% N2 and 20% CO2 gas\natmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Prior to use add\npyruvate, thiosulfate, vitamins, and sulfide from sterile anoxic stock solutions prepared\nunder 100% N2 gas. Stock solutions of pyruvate and vitamins are sterilized by filtration.","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Dissolve ingredients (except bicarbonate, pyruvate, thiosulfate, vitamins and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add bicarbonate and adjust pH to 7.0 - 7.2, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Prior to use add pyruvate, thiosulfate, vitamins, and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Stock solutions of pyruvate and vitamins are sterilized by filtration.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q48","label":"Retained unqualified SL11 preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"preparation_steps[1].description","stored":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0 and bring volume to 1000 ml."}],"decision":"correct","rationale":"The numeric text is source-supported, including800 mL initial water,2 N NaOH, pH7 then6 and final1000 mL makeup. Its unqualified main preparation-step placement loses the SL11 stock boundary; preserve the words inside that stock. NaOH volume remains unquantified and no normality-to-molarity conversion is needed.","source_stage":"SL11 stock preparation currently placed at main level","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 41-43","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\": \"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0 and bring volume to 1000 ml. \"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q49","label":"Main water input","local_fields":[],"decision":"evidence_only","rationale":"The1000 mL is main solvent input, not an independently stated final medium volume.","source_stage":"source-only solvent/stock control","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 17-17","quote":"Distilled water                                       1000.00       ml","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q50","label":"SL11 receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The1 mL stock addition is distinct from its nine component strengths.","source_stage":"source-only solvent/stock control","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 8-8","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\": 1474,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q51","label":"Se/W receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The1 mL stock addition is distinct from its three component strengths.","source_stage":"source-only solvent/stock control","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 9-9","quote":"Selenite-tungstate solution                              1.00       ml","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q52","label":"Wolin10x receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The1 mL10x vitamin-stock addition is distinct from its ten component strengths.","source_stage":"source-only solvent/stock control","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 15-15","quote":"Wolin's vitamin solution (10x)                           1.00       ml","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q53","label":"Sodium resazurin liquid stock","local_fields":[],"decision":"evidence_only","rationale":"The primary explicitly specifies0.5 mL of0.1% w/v sodium resazurin; retain that basis and stock identity alongside the provider rate.","source_stage":"source-only solvent/stock control","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 11-11","quote":"Sodium resazurin (0.1% w/v)                              0.50       ml","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q54","label":"SL11 final water","local_fields":[],"decision":"evidence_only","rationale":"The separate preparation explicitly makes SL11 up to1000 mL, unlike an unqualified solvent-input row.","source_stage":"source-only solvent/stock control","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 39-39","quote":"Distilled water                                       1000.00      ml","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 41-43","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q55","label":"Se/W input water","local_fields":[],"decision":"evidence_only","rationale":"Input1000 mL water does not independently state final volume.","source_stage":"source-only solvent/stock control","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 59-59","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q56","label":"Wolin10x input water","local_fields":[],"decision":"evidence_only","rationale":"Input1000 mL water does not independently state final volume.","source_stage":"source-only solvent/stock control","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt lines 73-73","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml":null,"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:006363.

Every primary/secondary slot is joined to current exact ontology objects and packaged MIM rows. Three supplied-form contradictions are confirmed. CHEBI31345 has the D stereochemistry present in the primary calcium D-pantothenate label; CHEBI16494 does not assert a contrary lipoic-acid enantiomer. Vitamin B12 remains a broad class. Provider mmol_l values are not used to infer molecular formulas, masses or new concentration conversions.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:006363.

All five report bodies and two exact historical plan rows were read. The current API digest equals14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae, authenticating content quoted in both October7 reviews without recovering their access event. The KOMODO mapping row remains a decoded historical quote with its own inaccessible raw catalogue. Current formulation-aware merger and stock-aware primary parsing are credited; current preparation collection and timestamp generation need the specifically identified fixes.

## Findings

### f1: Keep three stock compositions and their receiving doses distinct

major / open / confirmed; issue key: culturemech-006363-stock-topology.

All22 components of SL11, Se/W and Wolin10x are direct medium ingredients at stock strength. Restore the three named stocks and their separate1 mL doses. SL11 has explicit final1000 mL makeup; Se/W and vitamins only list input water, so keep provider rates as provider data without invented final-medium normalization. Preserve the source sodium-resazurin0.5 mL0.1%w/v addition and late sterile-stock stages.

### f2: Separate unresolved KOMODO conditions from the supported DSM formulation

major / open / confirmed; issue key: culturemech-006363-source-condition-merge.

The selected target retained KOMODO pH7.0 and Aerobic: Yes while losing the maintained DSM pH7.0–7.2 and preparation. The DSM source explicitly requires anoxic preparation. Current exact KOMODO detail/catalogue access failed403, so retain the identity lead but do not endorse the condition-mismatched combined formulation. Preserve the DSM owner main procedure, scope its second step to SL11, and reconcile source-specific formulation boundaries before regeneration. Current exact-formulation merge guards already protect differing notes/preparation and should be retained.

### f3: Correct three supplied-form contradictions in all affected slots

major / open / confirmed; issue key: culturemech-006363-supplied-forms.

The source explicitly supplies K2HPO4 trihydrate, sodium resazurin and NiCl2 hexahydrate, whereas phosphate and nickel primary and secondary slots assert anhydrous dipotassium hydrogen phosphate CHEBI131527 and nickel dichloride CHEBI34887, and the resazurin primary slot alone asserts neutral resazurin CHEBI8806; no secondary resazurin slot is present. Correct the exact supplied forms without changing source amounts. Existing cobalt hexahydrate, EDTA dihydrate, calcium D-pantothenate and non-stereospecific lipoic-acid identity are credited; do not add an invented vitamer or stereochemical conversion.

### f4: Attach scoped evidence and preserve append-only history

minor / open / confirmed; issue key: culturemech-006363-evidence-history.

The old reviews left all concentrations unchanged because stock topology and source conditions remained unresolved. Equal current API bytes authenticate their literal content, not the original retrieval event; current exact KOMODO catalogue bytes were not recovered. Attach source-scoped claims after curation, preserve malformed historical timestamps as history, and fix future timestamp generation in the inspected KOMODO importer without inventing old times.

## Recommended Actions And Acceptance Checks

### a1

All22 components of SL11, Se/W and Wolin10x are direct medium ingredients at stock strength. Restore the three named stocks and their separate1 mL doses. SL11 has explicit final1000 mL makeup; Se/W and vitamins only list input water, so keep provider rates as provider data without invented final-medium normalization. Preserve the source sodium-resazurin0.5 mL0.1%w/v addition and late sterile-stock stages.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

The selected target retained KOMODO pH7.0 and Aerobic: Yes while losing the maintained DSM pH7.0–7.2 and preparation. The DSM source explicitly requires anoxic preparation. Current exact KOMODO detail/catalogue access failed403, so retain the identity lead but do not endorse the condition-mismatched combined formulation. Preserve the DSM owner main procedure, scope its second step to SL11, and reconcile source-specific formulation boundaries before regeneration. Current exact-formulation merge guards already protect differing notes/preparation and should be retained.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The source explicitly supplies K2HPO4 trihydrate, sodium resazurin and NiCl2 hexahydrate, whereas phosphate and nickel primary and secondary slots assert anhydrous dipotassium hydrogen phosphate CHEBI131527 and nickel dichloride CHEBI34887, and the resazurin primary slot alone asserts neutral resazurin CHEBI8806; no secondary resazurin slot is present. Correct the exact supplied forms without changing source amounts. Existing cobalt hexahydrate, EDTA dihydrate, calcium D-pantothenate and non-stereospecific lipoic-acid identity are credited; do not add an invented vitamer or stereochemical conversion.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

The old reviews left all concentrations unchanged because stock topology and source conditions remained unresolved. Equal current API bytes authenticate their literal content, not the original retrieval event; current exact KOMODO catalogue bytes were not recovered. Attach source-scoped claims after curation, preserve malformed historical timestamps as history, and fix future timestamp generation in the inspected KOMODO importer without inventing old times.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.
- Use a UTC-aware datetime formatter for future importer events; retain existing historical event bytes and append an explicit explanation rather than backdating them.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsm720 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf; REVIEW_WORK/batch073/source07-08-10/dsm720.json; exact original raw/text/hash/time metadata | context_only | Exact DSM720 primary, printed variants remain conditional. |
| api720 | https://mediadive.dsmz.de/rest/medium/720; REVIEW_WORK/batch073/source07-08-10/api720.json; exact original raw/text/hash/time metadata | context_only | Current provider720 source and exact ingredient/stock stages. |
| komodo720 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=720; REVIEW_WORK/batch073/source07-08-10/komodo720.json; exact original raw/text/hash/time metadata | context_only | Exact historical detail route; no equivalent recipe assumed if unavailable. |
| komodoList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; REVIEW_WORK/batch073/source07-08-10/komodoList.json; exact original raw/text/hash/time metadata | context_only | Historical catalog identity route only. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; REVIEW_WORK/batch073/source07-08-10/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| target | data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| owner-2 | data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| report-18 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-19 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-20 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-22 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfitobacterium_hafniense_medium.yaml.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| writer-komodo | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech lines150–224 | context_only | Current _convert_to_culturemech retains catalogue pH/aerobic flags, creates empty ingredients and writes time.strftime with unsupported %f. The observed malformed historical timestamp is retained, not silently repaired or replayed. |
| writer-preparation | src/culturemech/import/mediadive_importer.py; _parse_preparation_steps; _parse_api_composition; _parse_api_solutions | context_only | Current _parse_preparation_steps appends steps across all provider solutions without their source-solution container. This explains a current stage-loss risk, not proof of the historical run. Current primary composition/stock-addition handling has been improved and is credited. |
| historical-reading | REVIEW_WORK/batch073/record10/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch073/record10/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch073/record10/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser excludes percent-stock additions from primary ingredients, preserves referenced stock amounts/attributes separately and prioritizes explicit provider g_l. It skips source water; bare units alone do not establish a final-volume basis. Current code is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| historical-object-joins | REVIEW_WORK/batch073/record10/historical-current-object-joins.json; Complete exact decoded-object comparisons | context_only | Historical object correspondence is distinct from raw-response authentication. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; REVIEW_WORK/batch073/source07-08-10/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; REVIEW_WORK/batch073/source07-08-10/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; REVIEW_WORK/batch073/source07-08-10/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; REVIEW_WORK/batch073/source07-08-10/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; REVIEW_WORK/batch073/source07-08-10/chebi131527.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; REVIEW_WORK/batch073/source07-08-10/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; REVIEW_WORK/batch073/source07-08-10/chebi32139.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi50144 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144; REVIEW_WORK/batch073/source07-08-10/chebi50144.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32150 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32150; REVIEW_WORK/batch073/source07-08-10/chebi32150.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; REVIEW_WORK/batch073/source07-08-10/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi64758 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64758; REVIEW_WORK/batch073/source07-08-10/chebi64758.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; REVIEW_WORK/batch073/source07-08-10/chebi86249.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; REVIEW_WORK/batch073/source07-08-10/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; REVIEW_WORK/batch073/source07-08-10/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; REVIEW_WORK/batch073/source07-08-10/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; REVIEW_WORK/batch073/source07-08-10/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; REVIEW_WORK/batch073/source07-08-10/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; REVIEW_WORK/batch073/source07-08-10/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; REVIEW_WORK/batch073/source07-08-10/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; REVIEW_WORK/batch073/source07-08-10/chebi32145.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; REVIEW_WORK/batch073/source07-08-10/chebi131361.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; REVIEW_WORK/batch073/source07-08-10/chebi63939.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; REVIEW_WORK/batch073/source07-08-10/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; REVIEW_WORK/batch073/source07-08-10/chebi27470.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; REVIEW_WORK/batch073/source07-08-10/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; REVIEW_WORK/batch073/source07-08-10/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; REVIEW_WORK/batch073/source07-08-10/chebi17015.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; REVIEW_WORK/batch073/source07-08-10/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; REVIEW_WORK/batch073/source07-08-10/chebi31345.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; REVIEW_WORK/batch073/source07-08-10/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; REVIEW_WORK/batch073/source07-08-10/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; REVIEW_WORK/batch073/source07-08-10/chebi16494.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| quantities | REVIEW_WORK/batch073/record10/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch073/record10/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch073/record10/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch073/record10/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch073/record10/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch073/record10/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch073/record10/existing-claim-authentication.json; Complete sidecar | context_only | The scoped existing-claim authentication sidecar is empty: no attached claims are asserted or authenticated here. Historical source-object correspondence is documented separately by historical-object-joins. |
| check-schema | REVIEW_WORK/batch073/record10/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch073/record10/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch073/record10/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch073/record10/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Completion is partial because the exact KOMODO detail/catalogue source branch remains unavailable. DSM720 evidence does not automatically settle the copied KOMODO formulation, pH or oxygen flag.
- The full DSM720 PDF was read on both pages, including all three embedded stock recipes. No parent medium722/385/120 formulation is transferred beyond the tables printed in720.
- The main1003 mL provider normalization is preserved as provider data; no independently measured final main volume is asserted.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T174513Z-culturemech-006363-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: DESULFITOBACTERIUM HAFNIENSE medium'
started_at: '2026-10-28T17:19:38.449677Z'
finished_at: '2026-10-28T17:45:13.782316Z'
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
summary: Three major stock-boundary, source-condition and supplied-form issues plus
  one minor provenance follow-up remain. The DSM owner main rates and preparation
  are credited at their exact scope; the merged KOMODO branch remains partial. No
  recipe or historical event was edited.
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
  - path: data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml
    sha256: 898ba3e37167d5a3d8dc1d27d6c51660e0f625b6ffcfc6e6747ba53f46c12e05
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml
    sha256: bab80fd4c0304e7937fd135b4e5ad0be03fca45d7271d988d6ba306efee2c8f6
    role: context
  - path: data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml
    sha256: 9bb5167565d92560d3614f118d4b19b3e0ff6b671ce03a0419531e79879c3766
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json
    sha256: 65c1b3085c5b2101fd274a184820f9de1dd1fa7f7f7d7d0068d6acb67b587934
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json
    sha256: f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml.md
    sha256: 3060c4f1e8622458aaa76644396dc309ab80a5881a8ae32f78bd816ad61ae6af
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
    sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfitobacterium_hafniense_medium.yaml.md
    sha256: 412b39257993271670477f7011accf0acc5568fe4fd1f6c3ffc2dde0a88ef092
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.md
    sha256: 6c1eec24f22c46fa10a378db3fb2fecadc165e41df83672fdf58508313d04199
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.md
    sha256: ee0de3472d3e3b133c073feaf40c0f47f8fdf62098b14707a4106841a353614b
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.md
    sha256: 59b585f30c145769b2a8b49b69317e0b6314c7b29254bce99ed09ad76329176b
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
  - path: scripts/propose_media_variant_links.py
    sha256: bd5b0b86c9457e42ca52ba2b253e5842c7f414093ba15aaeb4f9f0d682b5f4c2
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
  - path: scripts/repair_jcm_stock_preparations.py
    sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/resolve_komodo_compositions.py
    sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
    role: context
  - path: scripts/review_komodo_concentration_evidence.py
    sha256: 4470019965d068a53587be3668c3872daedc1505dab1bc6e2d1ed937ba409658
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
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
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
  selection: Authoritative batch073 index 10
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006363
targets:
- target_id: CultureMech:006363
  path: data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml
  label: desulfitobacterium_hafniense_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml
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
  - CultureMech:006363
  command: just validate-schema data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml
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
  - CultureMech:006363
  command: just validate-strict data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml
    --out REVIEW_WORK/batch073/record10/strict.tsv --workers 1 --quiet
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
  - CultureMech:006363
  command: just validate-terms data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml
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
  - CultureMech:006363
  command: just validate-references data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsm720
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf
  accessed_at: '2026-10-28T17:19:19.333929Z'
  locator: REVIEW_WORK/batch073/source07-08-10/dsm720.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact DSM720 primary, printed variants remain conditional.
  snapshot_sha256: 4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73
- evidence_id: api720
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/720
  accessed_at: '2026-10-28T17:19:19.662064Z'
  locator: REVIEW_WORK/batch073/source07-08-10/api720.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Current provider720 source and exact ingredient/stock stages.
  snapshot_sha256: 14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae
- evidence_id: komodo720
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=720
  accessed_at: '2026-10-28T17:19:19.084454Z'
  locator: REVIEW_WORK/batch073/source07-08-10/komodo720.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact historical detail route; no equivalent recipe assumed if unavailable.
  snapshot_sha256: 76facba367a4ba3a047a22921dab2cc5f1416e02353d8439db35ab47b5b766ab
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=720;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodoList
  kind: search
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  accessed_at: '2026-10-28T17:19:19.134572Z'
  locator: REVIEW_WORK/batch073/source07-08-10/komodoList.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Historical catalog identity route only.
  snapshot_sha256: b5030f8363981050a9072b1e2b0b3fc3e7ffaad29de2ab1a125ce69c31336d74
  search_scope: One exact public GET of https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  accessed_at: '2026-10-28T17:19:26.471716Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi53542.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T17:37:38.260312Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 898ba3e37167d5a3d8dc1d27d6c51660e0f625b6ffcfc6e6747ba53f46c12e05
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T17:37:38.260595Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: bab80fd4c0304e7937fd135b4e5ad0be03fca45d7271d988d6ba306efee2c8f6
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T17:37:38.260706Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T17:37:38.261155Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T17:37:38.261207Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T17:37:38.261244Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T17:37:38.261275Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: 9bb5167565d92560d3614f118d4b19b3e0ff6b671ce03a0419531e79879c3766
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T17:37:38.261334Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 65c1b3085c5b2101fd274a184820f9de1dd1fa7f7f7d7d0068d6acb67b587934
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T17:37:38.262355Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T17:37:38.269993Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 3060c4f1e8622458aaa76644396dc309ab80a5881a8ae32f78bd816ad61ae6af
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T17:37:38.270149Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfitobacterium_hafniense_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T17:37:38.278311Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 412b39257993271670477f7011accf0acc5568fe4fd1f6c3ffc2dde0a88ef092
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T17:37:38.278410Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 6c1eec24f22c46fa10a378db3fb2fecadc165e41df83672fdf58508313d04199
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T17:37:38.278461Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: ee0de3472d3e3b133c073feaf40c0f47f8fdf62098b14707a4106841a353614b
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T17:37:38.278520Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 59b585f30c145769b2a8b49b69317e0b6314c7b29254bce99ed09ad76329176b
- evidence_id: writer-komodo
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech lines150–224
  accessed_at: '2026-10-28T17:37:38.291316Z'
  support: context_only
  summary: Current _convert_to_culturemech retains catalogue pH/aerobic flags, creates
    empty ingredients and writes time.strftime with unsupported %f. The observed malformed
    historical timestamp is retained, not silently repaired or replayed.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer-preparation
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_preparation_steps; _parse_api_composition; _parse_api_solutions
  accessed_at: '2026-10-28T17:37:38.291428Z'
  support: context_only
  summary: Current _parse_preparation_steps appends steps across all provider solutions
    without their source-solution container. This explains a current stage-loss risk,
    not proof of the historical run. Current primary composition/stock-addition handling
    has been improved and is credited.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch073/record10/historical-reading.json
  accessed_at: '2026-10-28T17:37:38.295566Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: b7e232863d035bcd9296a720a82a723753e5b3160a0deda6257fdfb38447c782
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch073/record10/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T17:37:38.295659Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: d04998224f8f87c08e3347cfd9f085cf592ca1c444867cb956adf898e8092004
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch073/record10/complete-document-reader.json
  accessed_at: '2026-10-28T17:37:38.295933Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 861f9ec75813caabff2899eb30ca3f0bbc4541954b38b81805c9c2f123c50685
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T17:37:38.296044Z'
  support: context_only
  summary: Current parser excludes percent-stock additions from primary ingredients,
    preserves referenced stock amounts/attributes separately and prioritizes explicit
    provider g_l. It skips source water; bare units alone do not establish a final-volume
    basis. Current code is not historical execution proof.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T17:37:38.296101Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: historical-object-joins
  kind: prior_review
  reference: REVIEW_WORK/batch073/record10/historical-current-object-joins.json
  accessed_at: '2026-10-28T17:37:38.296138Z'
  locator: Complete exact decoded-object comparisons
  support: context_only
  summary: Historical object correspondence is distinct from raw-response authentication.
  snapshot_sha256: 26c12df1cfac83724472c4f28e5257b64c857017ba484bd9e2639fb20e1a86a8
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  accessed_at: '2026-10-28T17:19:23.622990Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi31206.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  accessed_at: '2026-10-28T17:19:22.812373Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi26710.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  accessed_at: '2026-10-28T17:19:28.629595Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi86345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  accessed_at: '2026-10-28T17:19:28.367230Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi86158.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  accessed_at: '2026-10-28T17:19:21.009309Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi131527.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  accessed_at: '2026-10-28T17:19:29.224916Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi8806.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  accessed_at: '2026-10-28T17:19:24.029286Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi32139.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi50144
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144
  accessed_at: '2026-10-28T17:19:26.227004Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi50144.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 457ed29adfdea68c420ea0c094d7d75593958fc70f908f6809348e4e12e7e15d
- evidence_id: chebi32150
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32150
  accessed_at: '2026-10-28T17:19:24.444624Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi32150.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 910d65eb9be29c9371cb79a32bcbe81bdb57d8143d21fbf7c4a1a915b5a79999
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  accessed_at: '2026-10-28T17:19:27.772720Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi76209.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi64758
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64758
  accessed_at: '2026-10-28T17:19:27.379130Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi64758.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 5432921ff4fea3479e93ce6392a2654e3d5560255beb96022793102e776d9647
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  accessed_at: '2026-10-28T17:19:28.392855Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi86249.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  accessed_at: '2026-10-28T17:19:26.271153Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi49976.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  accessed_at: '2026-10-28T17:19:28.992862Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi86368.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  accessed_at: '2026-10-28T17:19:25.039275Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi33118.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  accessed_at: '2026-10-28T17:19:26.461390Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi53503.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  accessed_at: '2026-10-28T17:19:28.626261Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi86318.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  accessed_at: '2026-10-28T17:19:25.468816Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi34887.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  accessed_at: '2026-10-28T17:19:27.404126Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi75213.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  accessed_at: '2026-10-28T17:19:24.229685Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi32145.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  accessed_at: '2026-10-28T17:19:20.911763Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi131361.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  accessed_at: '2026-10-28T17:19:27.058297Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi63939.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  accessed_at: '2026-10-28T17:19:21.108519Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi15956.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  accessed_at: '2026-10-28T17:19:23.124185Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi27470.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  accessed_at: '2026-10-28T17:19:23.420652Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi30961.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  accessed_at: '2026-10-28T17:19:26.185826Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi49105.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  accessed_at: '2026-10-28T17:19:21.842850Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi17015.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  accessed_at: '2026-10-28T17:19:21.150849Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi15940.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  accessed_at: '2026-10-28T17:19:23.858459Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi31345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  accessed_at: '2026-10-28T17:19:22.206136Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi176843.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  accessed_at: '2026-10-28T17:19:23.189753Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi30753.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  accessed_at: '2026-10-28T17:19:21.528598Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi16494.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch073/record10/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:37:38.570929Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 887349e0c041c1c922af3accf0967e9e60bc2a00590f5e477e4ece0bb896eb30
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch073/record10/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:37:38.571138Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: d8792bc2db6c943d0cdf6aee8a6bede509d2f3930fbd7e77f8365a3792d3d426
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch073/record10/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:37:38.571435Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 0d654163cb6cf5cdecd6db782e642a6b91d47e7b08791776accdda8c0e6e3e9d
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch073/record10/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:37:38.571625Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 8348275685423a5dd4256c34c4130d13df44a0fe81688871afd657b9ef8f650e
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch073/record10/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:37:38.571768Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 52986856c0c4721b244e26241a8169301899ab7260084038ee0bf8e2087863ae
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch073/record10/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:37:38.571849Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 82082fb5c59b6ea46c0ac4148c60dfbe4c15532af9cf7222895389a599903e6f
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch073/record10/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:37:38.571928Z'
  support: context_only
  summary: 'The scoped existing-claim authentication sidecar is empty: no attached
    claims are asserted or authenticated here. Historical source-object correspondence
    is documented separately by historical-object-joins.'
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch073/record10/schema-result.json
  accessed_at: '2026-10-28T17:19:39.566505Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: b71146c6f72391bdae014d526154d21c628221c0413b3e51793003a7333e647d
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch073/record10/strict-result.json
  accessed_at: '2026-10-28T17:19:40.525460Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: b51e0614d80991e690695d1a7202099526ffe6f0fbc587f01f1248a56d7f1de9
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch073/record10/terms-result.json
  accessed_at: '2026-10-28T17:19:41.578448Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 7f4853776ed9a51a8a4b8bfc7a394d72e6050671dfdcdfd86dbdbfbf9bf500f8
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch073/record10/references-result.json
  accessed_at: '2026-10-28T17:19:42.332978Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 51799e96399de67ab772fcc877f173351679416e44609e0c27a9d7071a028667
assessments:
- assessment_id: identity
  area: identity
  topic: DSM accession supported; exact KOMODO version incomplete
  outcome: concern
  summary: DSM720 PDF and current provider agree on accession/title. The historical
    KOMODO row maps720 toDSM720, but current exact detail and catalogue routes returned403;
    catalogue identity alone does not resolve the condition conflict.
  target_ids:
  - CultureMech:006363
  evidence_ids:
  - dsm720
  - api720
  - komodo720
  - komodoList
  - old-reports
- assessment_id: classification
  area: consistency
  topic: Complex liquid formulation with conflicting oxygen note
  outcome: concern
  summary: 'Complex/undefined/liquid agrees with the yeast-containing DSM formulation.
    Aerobic: Yes is incompatible with that source preparation and remains source-specific
    unresolved metadata, not an organism-growth assertion.'
  target_ids:
  - CultureMech:006363
  evidence_ids:
  - dsm720
  - api720
  - target
  - owner
- assessment_id: native
  area: schema
  topic: Original diagnostics
  outcome: supported
  summary: All four original canonical commands passed once; references checked zero.
    These shape checks do not authenticate formulation equivalence.
  target_ids:
  - CultureMech:006363
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 99 current concentration fields are covered by 56 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:006363
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b073-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","quantity_field_count":99,"decisions":[{"quantity_id":"q1","label":"NH4Cl
    DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    uncited rate matches the explicit current provider g_l normalization at1003 mL.
    The primary independently supports its batch mass or stock dose, but1 L input
    water is not an experimental final-volume statement. Retain both bases without
    inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 3-3","quote":"NH4Cl                                                    1.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\":
    18.6392,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q2","label":"NH4Cl unresolved KOMODO/selected layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    number matches copied DSM provider data, but exact KOMODO conditions/version remain
    unresolved: current detail and catalogue routes returned403, and historical review
    explicitly retained the pH/source-boundary conflict. Equal copied numbers do not
    authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 3-3","quote":"NH4Cl                                                    1.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\":
    18.6392,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q3","label":"NaCl DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.0997009","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    uncited rate matches the explicit current provider g_l normalization at1003 mL.
    The primary independently supports its batch mass or stock dose, but1 L input
    water is not an experimental final-volume statement. Retain both bases without
    inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 4-4","quote":"NaCl                                                     0.10        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0997009,\n                        \"mmol_l\":
    1.70604,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q4","label":"NaCl unresolved KOMODO/selected layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.0997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.0997009","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    number matches copied DSM provider data, but exact KOMODO conditions/version remain
    unresolved: current detail and catalogue routes returned403, and historical review
    explicitly retained the pH/source-boundary conflict. Equal copied numbers do not
    authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 4-4","quote":"NaCl                                                     0.10        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0997009,\n                        \"mmol_l\":
    1.70604,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q5","label":"MgCl2 x 6 H2O DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.0997009","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    uncited rate matches the explicit current provider g_l normalization at1003 mL.
    The primary independently supports its batch mass or stock dose, but1 L input
    water is not an experimental final-volume statement. Retain both bases without
    inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 5-5","quote":"MgCl2 x 6 H2O                                            0.10        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0997009,\n                        \"mmol_l\":
    0.490405,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q6","label":"MgCl2 x 6 H2O unresolved KOMODO/selected
    layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.0997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.0997009","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    number matches copied DSM provider data, but exact KOMODO conditions/version remain
    unresolved: current detail and catalogue routes returned403, and historical review
    explicitly retained the pH/source-boundary conflict. Equal copied numbers do not
    authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 5-5","quote":"MgCl2 x 6 H2O                                            0.10        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0997009,\n                        \"mmol_l\":
    0.490405,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q7","label":"CaCl2 x 2 H2O DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.0498504","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    uncited rate matches the explicit current provider g_l normalization at1003 mL.
    The primary independently supports its batch mass or stock dose, but1 L input
    water is not an experimental final-volume statement. Retain both bases without
    inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 6-6","quote":"CaCl2 x 2 H2O                                            0.05        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.05,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0498504,\n                        \"mmol_l\":
    0.339084,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q8","label":"CaCl2 x 2 H2O unresolved KOMODO/selected
    layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.0498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.0498504","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    number matches copied DSM provider data, but exact KOMODO conditions/version remain
    unresolved: current detail and catalogue routes returned403, and historical review
    explicitly retained the pH/source-boundary conflict. Equal copied numbers do not
    authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 6-6","quote":"CaCl2 x 2 H2O                                            0.05        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.05,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0498504,\n                        \"mmol_l\":
    0.339084,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q9","label":"K2HPO4 x 3 H2O DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.398804","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    uncited rate matches the explicit current provider g_l normalization at1003 mL.
    The primary independently supports its batch mass or stock dose, but1 L input
    water is not an experimental final-volume statement. Retain both bases without
    inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 7-7","quote":"K2HPO4 x 3 H2O                                           0.40        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"K2HPO4 x 3 H2O\",\n                        \"compound_id\":
    244,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.398804,\n                        \"mmol_l\":
    2.28966,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q10","label":"K2HPO4 x 3 H2O unresolved KOMODO/selected
    layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.398804","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.398804","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    number matches copied DSM provider data, but exact KOMODO conditions/version remain
    unresolved: current detail and catalogue routes returned403, and historical review
    explicitly retained the pH/source-boundary conflict. Equal copied numbers do not
    authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 7-7","quote":"K2HPO4 x 3 H2O                                           0.40        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"K2HPO4 x 3 H2O\",\n                        \"compound_id\":
    244,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.398804,\n                        \"mmol_l\":
    2.28966,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q11","label":"Yeast extract DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    uncited rate matches the explicit current provider g_l normalization at1003 mL.
    The primary independently supports its batch mass or stock dose, but1 L input
    water is not an experimental final-volume statement. Retain both bases without
    inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 10-10","quote":"Yeast extract                                            1.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.997009,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"Yeast
    extract unresolved KOMODO/selected layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    number matches copied DSM provider data, but exact KOMODO conditions/version remain
    unresolved: current detail and catalogue routes returned403, and historical review
    explicitly retained the pH/source-boundary conflict. Equal copied numbers do not
    authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 10-10","quote":"Yeast extract                                            1.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.997009,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"Sodium
    resazurin DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    uncited rate matches the explicit current provider g_l normalization at1003 mL.
    The primary independently supports its batch mass or stock dose, but1 L input
    water is not an experimental final-volume statement. Retain both bases without
    inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 11-11","quote":"Sodium resazurin (0.1% w/v)                              0.50       ml","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"Sodium
    resazurin unresolved KOMODO/selected layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    number matches copied DSM provider data, but exact KOMODO conditions/version remain
    unresolved: current detail and catalogue routes returned403, and historical review
    explicitly retained the pH/source-boundary conflict. Equal copied numbers do not
    authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 11-11","quote":"Sodium resazurin (0.1% w/v)                              0.50       ml","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"NaHCO3
    DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"2.59222","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    uncited rate matches the explicit current provider g_l normalization at1003 mL.
    The primary independently supports its batch mass or stock dose, but1 L input
    water is not an experimental final-volume statement. Retain both bases without
    inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 12-12","quote":"NaHCO3                                                   2.60        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"amount\": 2.6,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.59222,\n                        \"mmol_l\":
    30.8572,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q16","label":"NaHCO3 unresolved KOMODO/selected layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"2.59222","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"2.59222","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    number matches copied DSM provider data, but exact KOMODO conditions/version remain
    unresolved: current detail and catalogue routes returned403, and historical review
    explicitly retained the pH/source-boundary conflict. Equal copied numbers do not
    authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 12-12","quote":"NaHCO3                                                   2.60        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"amount\": 2.6,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.59222,\n                        \"mmol_l\":
    30.8572,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q17","label":"Na-pyruvate DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"2.49252","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    uncited rate matches the explicit current provider g_l normalization at1003 mL.
    The primary independently supports its batch mass or stock dose, but1 L input
    water is not an experimental final-volume statement. Retain both bases without
    inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 13-13","quote":"Na-pyruvate                                              2.50        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Na-pyruvate\",\n                        \"compound_id\":
    113,\n                        \"amount\": 2.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.49252,\n                        \"mmol_l\":
    22.6502,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q18","label":"Na-pyruvate unresolved KOMODO/selected
    layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"2.49252","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"2.49252","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    number matches copied DSM provider data, but exact KOMODO conditions/version remain
    unresolved: current detail and catalogue routes returned403, and historical review
    explicitly retained the pH/source-boundary conflict. Equal copied numbers do not
    authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 13-13","quote":"Na-pyruvate                                              2.50        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Na-pyruvate\",\n                        \"compound_id\":
    113,\n                        \"amount\": 2.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.49252,\n                        \"mmol_l\":
    22.6502,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q19","label":"Na2S2O3 x 5 H2O DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1.24626","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    uncited rate matches the explicit current provider g_l normalization at1003 mL.
    The primary independently supports its batch mass or stock dose, but1 L input
    water is not an experimental final-volume statement. Retain both bases without
    inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 14-14","quote":"Na2S2O3 x 5 H2O                                          1.25        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2S2O3 x 5 H2O\",\n                        \"compound_id\":
    65,\n                        \"amount\": 1.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.24626,\n                        \"mmol_l\":
    5.02148,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q20","label":"Na2S2O3 x 5 H2O unresolved KOMODO/selected
    layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1.24626","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1.24626","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    number matches copied DSM provider data, but exact KOMODO conditions/version remain
    unresolved: current detail and catalogue routes returned403, and historical review
    explicitly retained the pH/source-boundary conflict. Equal copied numbers do not
    authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 14-14","quote":"Na2S2O3 x 5 H2O                                          1.25        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2S2O3 x 5 H2O\",\n                        \"compound_id\":
    65,\n                        \"amount\": 1.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.24626,\n                        \"mmol_l\":
    5.02148,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q21","label":"Na2S x 9 H2O DSM owner","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.299103","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    uncited rate matches the explicit current provider g_l normalization at1003 mL.
    The primary independently supports its batch mass or stock dose, but1 L input
    water is not an experimental final-volume statement. Retain both bases without
    inventing a conversion.","source_stage":"DSM720 main provider nominal rate","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 16-16","quote":"Na2S x 9 H2O                                             0.30        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\":
    1.24532,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q22","label":"Na2S x 9 H2O unresolved KOMODO/selected
    layer","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.299103","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.299103","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    number matches copied DSM provider data, but exact KOMODO conditions/version remain
    unresolved: current detail and catalogue routes returned403, and historical review
    explicitly retained the pH/source-boundary conflict. Equal copied numbers do not
    authenticate the combined formulation.","source_stage":"unresolved KOMODO branch","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 16-16","quote":"Na2S x 9 H2O                                             0.30        g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\":
    1.24532,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q23","label":"Na2-EDTA x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"5.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"5.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"5.2","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an SL11 stock rate, flattened into the receiving medium. The primary explicitly
    makes this stock up to1000 mL, supporting its stock g/L values; retain the separate1
    mL receiving dose, not direct-medium stock strength. The KOMODO source branch
    still requires identity/condition reconciliation; its copied entries are not independently
    endorsed.","source_stage":"SL11 stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 30-30","quote":"Na2-EDTA x 2 H2O                                         5.20       g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\":
    676,\n                        \"amount\": 5.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\":
    15.4667,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\":
    1474,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q24","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an SL11 stock rate, flattened into the receiving medium. The primary explicitly
    makes this stock up to1000 mL, supporting its stock g/L values; retain the separate1
    mL receiving dose, not direct-medium stock strength. The KOMODO source branch
    still requires identity/condition reconciliation; its copied entries are not independently
    endorsed.","source_stage":"SL11 stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 31-31","quote":"FeCl2 x 4 H2O                                            1.50       g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\":
    1474,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q25","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an SL11 stock rate, flattened into the receiving medium. The primary explicitly
    makes this stock up to1000 mL, supporting its stock g/L values; retain the separate1
    mL receiving dose, not direct-medium stock strength. The KOMODO source branch
    still requires identity/condition reconciliation; its copied entries are not independently
    endorsed.","source_stage":"SL11 stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 32-32","quote":"ZnCl2                                                   70.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\":
    1474,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q26","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an SL11 stock rate, flattened into the receiving medium. The primary explicitly
    makes this stock up to1000 mL, supporting its stock g/L values; retain the separate1
    mL receiving dose, not direct-medium stock strength. The KOMODO source branch
    still requires identity/condition reconciliation; its copied entries are not independently
    endorsed.","source_stage":"SL11 stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 33-33","quote":"MnCl2 x 4 H2O                                          100.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\":
    1474,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q27","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an SL11 stock rate, flattened into the receiving medium. The primary explicitly
    makes this stock up to1000 mL, supporting its stock g/L values; retain the separate1
    mL receiving dose, not direct-medium stock strength. The KOMODO source branch
    still requires identity/condition reconciliation; its copied entries are not independently
    endorsed.","source_stage":"SL11 stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 34-34","quote":"H3BO3                                                    6.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\":
    1474,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q28","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an SL11 stock rate, flattened into the receiving medium. The primary explicitly
    makes this stock up to1000 mL, supporting its stock g/L values; retain the separate1
    mL receiving dose, not direct-medium stock strength. The KOMODO source branch
    still requires identity/condition reconciliation; its copied entries are not independently
    endorsed.","source_stage":"SL11 stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 35-35","quote":"CoCl2 x 6 H2O                                          190.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\":
    1474,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q29","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an SL11 stock rate, flattened into the receiving medium. The primary explicitly
    makes this stock up to1000 mL, supporting its stock g/L values; retain the separate1
    mL receiving dose, not direct-medium stock strength. The KOMODO source branch
    still requires identity/condition reconciliation; its copied entries are not independently
    endorsed.","source_stage":"SL11 stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 36-36","quote":"CuCl2 x 2 H2O                                            2.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\":
    1474,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q30","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an SL11 stock rate, flattened into the receiving medium. The primary explicitly
    makes this stock up to1000 mL, supporting its stock g/L values; retain the separate1
    mL receiving dose, not direct-medium stock strength. The KOMODO source branch
    still requires identity/condition reconciliation; its copied entries are not independently
    endorsed.","source_stage":"SL11 stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 37-37","quote":"NiCl2 x 6 H2O                                           24.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\":
    1474,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q31","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is an SL11 stock rate, flattened into the receiving medium. The primary explicitly
    makes this stock up to1000 mL, supporting its stock g/L values; retain the separate1
    mL receiving dose, not direct-medium stock strength. The KOMODO source branch
    still requires identity/condition reconciliation; its copied entries are not independently
    endorsed.","source_stage":"SL11 stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 38-38","quote":"Na2MoO4 x 2 H2O                                         36.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\":
    1474,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q32","label":"NaOH","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is a Se/W stock input/provider stock g_l value, flattened into the receiving medium.
    The primary lists1000 mL input water without a separate final makeup. Preserve
    its source mass/stage and1 mL receiving dose without final-medium arithmetic.
    The KOMODO source branch still requires identity/condition reconciliation; its
    copied entries are not independently endorsed.","source_stage":"Se/W stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 56-56","quote":"NaOH                                        0.50    g","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    12.5009,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q33","label":"Na2SeO3 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.003","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is a Se/W stock input/provider stock g_l value, flattened into the receiving medium.
    The primary lists1000 mL input water without a separate final makeup. Preserve
    its source mass/stage and1 mL receiving dose without final-medium arithmetic.
    The KOMODO source branch still requires identity/condition reconciliation; its
    copied entries are not independently endorsed.","source_stage":"Se/W stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 57-57","quote":"Na2SeO3 x 5 H2O                             3.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\":
    0.0114062,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q34","label":"Na2WO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is a Se/W stock input/provider stock g_l value, flattened into the receiving medium.
    The primary lists1000 mL input water without a separate final makeup. Preserve
    its source mass/stage and1 mL receiving dose without final-medium arithmetic.
    The KOMODO source branch still requires identity/condition reconciliation; its
    copied entries are not independently endorsed.","source_stage":"Se/W stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 58-58","quote":"Na2WO4 x 2 H2O                              4.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\":
    0.0121267,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q35","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to Wolin vitamin stock10x, not the receiving medium at stock strength.
    Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000
    mL water is input, not an independent final-stock-volume statement. The KOMODO
    source branch still requires identity/condition reconciliation; its copied entries
    are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 63-63","quote":"Biotin                                     20.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q36","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to Wolin vitamin stock10x, not the receiving medium at stock strength.
    Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000
    mL water is input, not an independent final-stock-volume statement. The KOMODO
    source branch still requires identity/condition reconciliation; its copied entries
    are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 64-64","quote":"Folic acid                                 20.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q37","label":"Pyridoxine hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to Wolin vitamin stock10x, not the receiving medium at stock strength.
    Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000
    mL water is input, not an independent final-stock-volume statement. The KOMODO
    source branch still requires identity/condition reconciliation; its copied entries
    are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 65-65","quote":"Pyridoxine hydrochloride                  100.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q38","label":"Thiamine HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to Wolin vitamin stock10x, not the receiving medium at stock strength.
    Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000
    mL water is input, not an independent final-stock-volume statement. The KOMODO
    source branch still requires identity/condition reconciliation; its copied entries
    are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 66-66","quote":"Thiamine HCl                               50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q39","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to Wolin vitamin stock10x, not the receiving medium at stock strength.
    Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000
    mL water is input, not an independent final-stock-volume statement. The KOMODO
    source branch still requires identity/condition reconciliation; its copied entries
    are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 67-67","quote":"Riboflavin                                 50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q40","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to Wolin vitamin stock10x, not the receiving medium at stock strength.
    Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000
    mL water is input, not an independent final-stock-volume statement. The KOMODO
    source branch still requires identity/condition reconciliation; its copied entries
    are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 68-68","quote":"Nicotinic acid                             50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q41","label":"Calcium D-(+)-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to Wolin vitamin stock10x, not the receiving medium at stock strength.
    Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000
    mL water is input, not an independent final-stock-volume statement. The KOMODO
    source branch still requires identity/condition reconciliation; its copied entries
    are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 69-69","quote":"Calcium D-(+)-pantothenate                 50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q42","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.001","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to Wolin vitamin stock10x, not the receiving medium at stock strength.
    Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000
    mL water is input, not an independent final-stock-volume statement. The KOMODO
    source branch still requires identity/condition reconciliation; its copied entries
    are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 70-70","quote":"Vitamin B12                                 1.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q43","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to Wolin vitamin stock10x, not the receiving medium at stock strength.
    Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000
    mL water is input, not an independent final-stock-volume statement. The KOMODO
    source branch still requires identity/condition reconciliation; its copied entries
    are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 71-71","quote":"p-Aminobenzoic acid                        50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q44","label":"(DL)-alpha-Lipoic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to Wolin vitamin stock10x, not the receiving medium at stock strength.
    Retain the provider stock g_l, primary mg input and separate1 mL dose. The printed1000
    mL water is input, not an independent final-stock-volume statement. The KOMODO
    source branch still requires identity/condition reconciliation; its copied entries
    are not independently endorsed.","source_stage":"Wolin10x vitamin stock","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 72-72","quote":"(DL)-alpha-Lipoic acid                     50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q45","label":"DSM pH range","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ph_range.min","stored":7.0},{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"ph_range.max","stored":7.2}],"decision":"evidence_only","rationale":"The
    existing7.0–7.2 range is supported and must be retained at the main-medium stage.
    It is distinct from SL11 pH7 then6.0.","source_stage":"main pH","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 19-24","quote":"Dissolve ingredients (except bicarbonate, pyruvate, thiosulfate,
    vitamins and sulfide), then\nsparge medium with 80% N2 and 20% CO2 gas mixture
    for 30 - 45 min to make it anoxic.\nAdd bicarbonate and adjust pH to 7.0 - 7.2,
    then dispense under 80% N2 and 20% CO2 gas\natmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave. Prior to use add\npyruvate, thiosulfate, vitamins,
    and sulfide from sterile anoxic stock solutions prepared\nunder 100% N2 gas. Stock
    solutions of pyruvate and vitamins are sterilized by filtration.","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Dissolve ingredients (except bicarbonate, pyruvate, thiosulfate, vitamins and
    sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min
    to make it anoxic. Add bicarbonate and adjust pH to 7.0 - 7.2, then dispense under
    80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials
    and autoclave. Prior to use add pyruvate, thiosulfate, vitamins, and sulfide from
    sterile anoxic stock solutions prepared under 100% N2 gas. Stock solutions of
    pyruvate and vitamins are sterilized by filtration.\"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q46","label":"Selected/KOMODO pH7","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml","field_path":"ph_value","stored":7.0},{"path":"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml","field_path":"ph_value","stored":7.0}],"decision":"unsupported","rationale":"7.0
    lies inside the DSM range but does not establish equivalence of the KOMODO branch
    or justify losing the DSM range. Historical catalogue pH is derivative identity
    context; exact current route is unavailable.","source_stage":"source-specific
    pH reconciliation","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 19-24","quote":"Dissolve ingredients (except bicarbonate, pyruvate, thiosulfate,
    vitamins and sulfide), then\nsparge medium with 80% N2 and 20% CO2 gas mixture
    for 30 - 45 min to make it anoxic.\nAdd bicarbonate and adjust pH to 7.0 - 7.2,
    then dispense under 80% N2 and 20% CO2 gas\natmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave. Prior to use add\npyruvate, thiosulfate, vitamins,
    and sulfide from sterile anoxic stock solutions prepared\nunder 100% N2 gas. Stock
    solutions of pyruvate and vitamins are sterilized by filtration.","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.medium","quote":"{\n            \"id\":
    720,\n            \"name\": \"DESULFITOBACTERIUM HAFNIENSE MEDIUM\",\n            \"complex_medium\":
    \"yes\",\n            \"min_pH\": 7,\n            \"max_pH\": 7.2,\n            \"source\":
    \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf\"\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q47","label":"Retained DSM main preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"preparation_steps[0].description","stored":"Dissolve
    ingredients (except bicarbonate, pyruvate, thiosulfate, vitamins and sulfide),
    then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make
    it anoxic. Add bicarbonate and adjust pH to 7.0 - 7.2, then dispense under 80%
    N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and
    autoclave. Prior to use add pyruvate, thiosulfate, vitamins, and sulfide from
    sterile anoxic stock solutions prepared under 100% N2 gas. Stock solutions of
    pyruvate and vitamins are sterilized by filtration."}],"decision":"evidence_only","rationale":"The
    full existing description is source-supported: retain its80/20 gas mixture,30–45
    min sparging, pH range, separate100% N2 stocks and filter-sterilization exceptions.
    The generated record loses this description; do not call it absent from the maintained
    DSM owner.","source_stage":"DSM main preparation","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 19-24","quote":"Dissolve ingredients (except bicarbonate, pyruvate, thiosulfate,
    vitamins and sulfide), then\nsparge medium with 80% N2 and 20% CO2 gas mixture
    for 30 - 45 min to make it anoxic.\nAdd bicarbonate and adjust pH to 7.0 - 7.2,
    then dispense under 80% N2 and 20% CO2 gas\natmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave. Prior to use add\npyruvate, thiosulfate, vitamins,
    and sulfide from sterile anoxic stock solutions prepared\nunder 100% N2 gas. Stock
    solutions of pyruvate and vitamins are sterilized by filtration.","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Dissolve ingredients (except bicarbonate, pyruvate, thiosulfate, vitamins and
    sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min
    to make it anoxic. Add bicarbonate and adjust pH to 7.0 - 7.2, then dispense under
    80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials
    and autoclave. Prior to use add pyruvate, thiosulfate, vitamins, and sulfide from
    sterile anoxic stock solutions prepared under 100% N2 gas. Stock solutions of
    pyruvate and vitamins are sterilized by filtration.\"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q48","label":"Retained unqualified SL11 preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml","field_path":"preparation_steps[1].description","stored":"Dissolve
    EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous
    chloride. After ferrous chloride has dissolved add other compounds. Finally adjust
    pH to 6.0 and bring volume to 1000 ml."}],"decision":"correct","rationale":"The
    numeric text is source-supported, including800 mL initial water,2 N NaOH, pH7
    then6 and final1000 mL makeup. Its unqualified main preparation-step placement
    loses the SL11 stock boundary; preserve the words inside that stock. NaOH volume
    remains unquantified and no normality-to-molarity conversion is needed.","source_stage":"SL11
    stock preparation currently placed at main level","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 41-43","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\":
    \"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add
    ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally
    adjust pH to 6.0 and bring volume to 1000 ml. \"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q49","label":"Main water input","local_fields":[],"decision":"evidence_only","rationale":"The1000
    mL is main solvent input, not an independently stated final medium volume.","source_stage":"source-only
    solvent/stock control","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 17-17","quote":"Distilled water                                       1000.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q50","label":"SL11 receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The1
    mL stock addition is distinct from its nine component strengths.","source_stage":"source-only
    solvent/stock control","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 8-8","quote":"Trace element solution SL-11                             1.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\":
    1474,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q51","label":"Se/W receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The1
    mL stock addition is distinct from its three component strengths.","source_stage":"source-only
    solvent/stock control","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 9-9","quote":"Selenite-tungstate solution                              1.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q52","label":"Wolin10x receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The1
    mL10x vitamin-stock addition is distinct from its ten component strengths.","source_stage":"source-only
    solvent/stock control","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 15-15","quote":"Wolin''s vitamin solution (10x)                           1.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q53","label":"Sodium resazurin liquid stock","local_fields":[],"decision":"evidence_only","rationale":"The
    primary explicitly specifies0.5 mL of0.1% w/v sodium resazurin; retain that basis
    and stock identity alongside the provider rate.","source_stage":"source-only solvent/stock
    control","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 11-11","quote":"Sodium resazurin (0.1% w/v)                              0.50       ml","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q54","label":"SL11
    final water","local_fields":[],"decision":"evidence_only","rationale":"The separate
    preparation explicitly makes SL11 up to1000 mL, unlike an unqualified solvent-input
    row.","source_stage":"source-only solvent/stock control","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 39-39","quote":"Distilled water                                       1000.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 41-43","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q55","label":"Se/W input water","local_fields":[],"decision":"evidence_only","rationale":"Input1000
    mL water does not independently state final volume.","source_stage":"source-only
    solvent/stock control","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 59-59","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q56","label":"Wolin10x input water","local_fields":[],"decision":"evidence_only","rationale":"Input1000
    mL water does not independently state final volume.","source_stage":"source-only
    solvent/stock control","sources":[{"evidence_id":"dsm720","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium720.pdf","raw_path":"REVIEW_WORK/batch073/source07-08-10/dsm720.raw","raw_sha256":"4eb736e80dee0b29f345c4e5022230df74e9ee70539864c84dcf8f33a0c79c73","text_sha256":"d216f7f578f6e94842f8897bae4c6e3f12cc54b235d0cd68fe5f95153695cc88","accessed_at":"2026-10-28T17:19:19.333929Z","locator":"dsm720.txt
    lines 73-73","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative
    text"},{"evidence_id":"api720","reference":"https://mediadive.dsmz.de/rest/medium/720","raw_path":"REVIEW_WORK/batch073/source07-08-10/api720.raw","raw_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","text_sha256":"14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae","accessed_at":"2026-10-28T17:19:19.662064Z","locator":"data.solutions[3].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/DESULFITOBACTERIUM_HAFNIENSE_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml":null,"data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: Every primary/secondary slot is joined to current exact ontology objects
    and packaged MIM rows. Three supplied-form contradictions are confirmed. CHEBI31345
    has the D stereochemistry present in the primary calcium D-pantothenate label;
    CHEBI16494 does not assert a contrary lipoic-acid enantiomer. Vitamin B12 remains
    a broad class. Provider mmol_l values are not used to infer molecular formulas,
    masses or new concentration conversions.
  target_ids:
  - CultureMech:006363
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: All five report bodies and two exact historical plan rows were read. The
    current API digest equals14931dbe178624629b6db9468e025c7ebdaeae104238e06dfbeeb7b0584eaaae,
    authenticating content quoted in both October7 reviews without recovering their
    access event. The KOMODO mapping row remains a decoded historical quote with its
    own inaccessible raw catalogue. Current formulation-aware merger and stock-aware
    primary parsing are credited; current preparation collection and timestamp generation
    need the specifically identified fixes.
  target_ids:
  - CultureMech:006363
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-006363-stock-topology
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Keep three stock compositions and their receiving doses distinct
  description: All22 components of SL11, Se/W and Wolin10x are direct medium ingredients
    at stock strength. Restore the three named stocks and their separate1 mL doses.
    SL11 has explicit final1000 mL makeup; Se/W and vitamins only list input water,
    so keep provider rates as provider data without invented final-medium normalization.
    Preserve the source sodium-resazurin0.5 mL0.1%w/v addition and late sterile-stock
    stages.
  target_ids:
  - CultureMech:006363
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - dsm720
  - api720
  - quantities
  - writer-mediadive
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-006363-source-condition-merge
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Separate unresolved KOMODO conditions from the supported DSM formulation
  description: 'The selected target retained KOMODO pH7.0 and Aerobic: Yes while losing
    the maintained DSM pH7.0–7.2 and preparation. The DSM source explicitly requires
    anoxic preparation. Current exact KOMODO detail/catalogue access failed403, so
    retain the identity lead but do not endorse the condition-mismatched combined
    formulation. Preserve the DSM owner main procedure, scope its second step to SL11,
    and reconcile source-specific formulation boundaries before regeneration. Current
    exact-formulation merge guards already protect differing notes/preparation and
    should be retained.'
  target_ids:
  - CultureMech:006363
  field_paths:
  - notes
  - ph_value
  - ph_range
  - preparation_steps
  - data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml::preparation_steps[1]
  evidence_ids:
  - dsm720
  - api720
  - komodo720
  - komodoList
  - old-reports
  - writer-formulation
  - writer-merger
  - writer-preparation
  rule_id: review-yaml-record/representation
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-006363-supplied-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Correct three supplied-form contradictions in all affected slots
  description: The source explicitly supplies K2HPO4 trihydrate, sodium resazurin
    and NiCl2 hexahydrate, whereas phosphate and nickel primary and secondary slots
    assert anhydrous dipotassium hydrogen phosphate CHEBI131527 and nickel dichloride
    CHEBI34887, and the resazurin primary slot alone asserts neutral resazurin CHEBI8806;
    no secondary resazurin slot is present. Correct the exact supplied forms without
    changing source amounts. Existing cobalt hexahydrate, EDTA dihydrate, calcium
    D-pantothenate and non-stereospecific lipoic-acid identity are credited; do not
    add an invented vitamer or stereochemical conversion.
  target_ids:
  - CultureMech:006363
  field_paths:
  - ingredients[4].term
  - ingredients[4].mediaingredientmech_chebi_term
  - ingredients[6].term
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  evidence_ids:
  - dsm720
  - api720
  - chebi131527
  - chebi8806
  - chebi34887
  - chebi53542
  - groundings
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-006363-evidence-history
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Attach scoped evidence and preserve append-only history
  description: The old reviews left all concentrations unchanged because stock topology
    and source conditions remained unresolved. Equal current API bytes authenticate
    their literal content, not the original retrieval event; current exact KOMODO
    catalogue bytes were not recovered. Attach source-scoped claims after curation,
    preserve malformed historical timestamps as history, and fix future timestamp
    generation in the inspected KOMODO importer without inventing old times.
  target_ids:
  - CultureMech:006363
  field_paths:
  - evidence
  - references
  - curation_history
  evidence_ids:
  - old-reports
  - old-claims
  - historical-object-joins
  - writer-komodo
  rule_id: review-yaml-record/provenance
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: maintained timestamp writer
actions:
- action_id: a1
  description: All22 components of SL11, Se/W and Wolin10x are direct medium ingredients
    at stock strength. Restore the three named stocks and their separate1 mL doses.
    SL11 has explicit final1000 mL makeup; Se/W and vitamins only list input water,
    so keep provider rates as provider data without invented final-medium normalization.
    Preserve the source sodium-resazurin0.5 mL0.1%w/v addition and late sterile-stock
    stages.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006363
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml
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
  description: 'The selected target retained KOMODO pH7.0 and Aerobic: Yes while losing
    the maintained DSM pH7.0–7.2 and preparation. The DSM source explicitly requires
    anoxic preparation. Current exact KOMODO detail/catalogue access failed403, so
    retain the identity lead but do not endorse the condition-mismatched combined
    formulation. Preserve the DSM owner main procedure, scope its second step to SL11,
    and reconcile source-specific formulation boundaries before regeneration. Current
    exact-formulation merge guards already protect differing notes/preparation and
    should be retained.'
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006363
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml
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
  description: The source explicitly supplies K2HPO4 trihydrate, sodium resazurin
    and NiCl2 hexahydrate, whereas phosphate and nickel primary and secondary slots
    assert anhydrous dipotassium hydrogen phosphate CHEBI131527 and nickel dichloride
    CHEBI34887, and the resazurin primary slot alone asserts neutral resazurin CHEBI8806;
    no secondary resazurin slot is present. Correct the exact supplied forms without
    changing source amounts. Existing cobalt hexahydrate, EDTA dihydrate, calcium
    D-pantothenate and non-stereospecific lipoic-acid identity are credited; do not
    add an invented vitamer or stereochemical conversion.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006363
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml
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
  description: The old reviews left all concentrations unchanged because stock topology
    and source conditions remained unresolved. Equal current API bytes authenticate
    their literal content, not the original retrieval event; current exact KOMODO
    catalogue bytes were not recovered. Attach source-scoped claims after curation,
    preserve malformed historical timestamps as history, and fix future timestamp
    generation in the inspected KOMODO importer without inventing old times.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006363
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_720_DESULFITOBACTERIUM_HAFNIENSE_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfitobacterium_hafniense_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: maintained timestamp writer
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  - Use a UTC-aware datetime formatter for future importer events; retain existing
    historical event bytes and append an explicit explanation rather than backdating
    them.
  generator: Maintained-input curation and repository merge regeneration
limitations:
- Completion is partial because the exact KOMODO detail/catalogue source branch remains
  unavailable. DSM720 evidence does not automatically settle the copied KOMODO formulation,
  pH or oxygen flag.
- The full DSM720 PDF was read on both pages, including all three embedded stock recipes.
  No parent medium722/385/120 formulation is transferred beyond the tables printed
  in720.
- The main1003 mL provider normalization is preserved as provider data; no independently
  measured final main volume is asserted.
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
