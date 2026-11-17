# Scientific review: DEFLUVIITOGA medium

- Review: 20261028T164612Z-culturemech-004084-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T16:15:15.871473Z
- Finished UTC: 2026-10-28T16:46:12.611812Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Partial source review identifies three major formulation, preparation and chemical-form issues plus one minor provenance follow-up. Existing DSM preparation and explicit provider rates are credited with their exact stage and denominator limits; no recipe was edited.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch072 index 07
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:004084 | data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml | generated | defluviitoga_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:004084 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:004084 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:004084 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:004084 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact source accession and duplicate scope

identity: concern. Targets: CultureMech:004084.

DSM1328 and the current exact KOMODO catalog row identify the selected source family, but the direct KOMODO detail returns403. Local source-duplicate links do not establish whole-formulation equality; maintained DSM preparation and KOMODO aerobic metadata differ.

### Record classification and organism limits

consistency: supported. Targets: CultureMech:004084.

Liquid, complex and undefined classification is consistent with yeast extract and peptone in the unqualified base. No target organism or strain-growth claim follows from a medium name. Printed strain overrides remain source-only variants.

### Native structure and generated ownership

schema: supported. Targets: CultureMech:004084.

All original canonical checks pass; reference validation checked zero attached references. Structural success does not endorse the stock or chemical assertions. Both maintained owners and current merge code are identified.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:004084.

72 current concentration fields are covered by 32 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b072-quantity-inventory-v1","target":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","quantity_field_count":72,"decisions":[{"quantity_id":"q1","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The provider explicitly reports this nominal main-medium g_l value. The primary gives a batch contribution with 1000 mL input water; neither that input nor API volume 1001 establishes measured final volume. Retain only the provider-declared rate with its source basis; no attached amount claim currently exists.","source_stage":"main receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 3-3","quote":"KH2PO4                                                 0.30       g","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 2.2045,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The provider explicitly reports this nominal main-medium g_l value. The primary gives a batch contribution with 1000 mL input water; neither that input nor API volume 1001 establishes measured final volume. Retain only the provider-declared rate with its source basis; no attached amount claim currently exists.","source_stage":"main receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 4-4","quote":"K2HPO4                                                 0.30       g","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.7224,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The provider explicitly reports this nominal main-medium g_l value. The primary gives a batch contribution with 1000 mL input water; neither that input nor API volume 1001 establishes measured final volume. Retain only the provider-declared rate with its source basis; no attached amount claim currently exists.","source_stage":"main receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 5-5","quote":"NH4Cl                                                  1.00       g","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 18.6951,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The provider explicitly reports this nominal main-medium g_l value. The primary gives a batch contribution with 1000 mL input water; neither that input nor API volume 1001 establishes measured final volume. Retain only the provider-declared rate with its source basis; no attached amount claim currently exists.","source_stage":"main receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 6-6","quote":"NaCl                                                   1.00       g","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The provider explicitly reports this nominal main-medium g_l value. The primary gives a batch contribution with 1000 mL input water; neither that input nor API volume 1001 establishes measured final volume. Retain only the provider-declared rate with its source basis; no attached amount claim currently exists.","source_stage":"main receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 7-7","quote":"KCl                                                    0.10       g","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 1.34138,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The provider explicitly reports this nominal main-medium g_l value. The primary gives a batch contribution with 1000 mL input water; neither that input nor API volume 1001 establishes measured final volume. Retain only the provider-declared rate with its source basis; no attached amount claim currently exists.","source_stage":"main receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 8-8","quote":"MgCl2 x 6 H2O                                          0.50       g","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.45938,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The provider explicitly reports this nominal main-medium g_l value. The primary gives a batch contribution with 1000 mL input water; neither that input nor API volume 1001 establishes measured final volume. Retain only the provider-declared rate with its source basis; no attached amount claim currently exists.","source_stage":"main receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 9-9","quote":"CaCl2 x 2 H2O                                          0.10       g","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The provider explicitly reports this nominal main-medium g_l value. The primary gives a batch contribution with 1000 mL input water; neither that input nor API volume 1001 establishes measured final volume. Retain only the provider-declared rate with its source basis; no attached amount claim currently exists.","source_stage":"main receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 11-11","quote":"Yeast extract (OXOID)                                  1.00       g","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"OXOID\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"Sodium resazurin","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.0005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.0005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.0005","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary adds 0.50 mL of explicitly 0.1% w/v sodium-resazurin stock; the provider scalar 0.0005 g/L loses the stock label and dose. It corresponds to 0.0005 g per listed batch, not independently proven final g/L. Preserve the explicit percentage basis and dose without assuming final volume.","source_stage":"main receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 12-12","quote":"Sodium resazurin (0.1% w/v)                            0.50      ml","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"Sulfur","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The provider explicitly reports this nominal main-medium g_l value. The primary gives a batch contribution with 1000 mL input water; neither that input nor API volume 1001 establishes measured final volume. Retain only the provider-declared rate with its source basis; no attached amount claim currently exists.","source_stage":"main receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 13-13","quote":"Sulfur (powdered)                                     10.00       g","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Sulfur\",\n                        \"compound_id\": 80,\n                        \"condition\": \"\",\n                        \"attribute\": \"powdered\",\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 311.818,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"L-Cysteine HCl x H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The provider explicitly reports this nominal main-medium g_l value. The primary gives a batch contribution with 1000 mL input water; neither that input nor API volume 1001 establishes measured final volume. Retain only the provider-declared rate with its source basis; no attached amount claim currently exists.","source_stage":"main receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 14-14","quote":"L-Cysteine HCl x H2O                                   0.50       g","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.8468,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"Trypticase peptone","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The provider explicitly reports this nominal main-medium g_l value. The primary gives a batch contribution with 1000 mL input water; neither that input nor API volume 1001 establishes measured final volume. Retain only the provider-declared rate with its source basis; no attached amount claim currently exists.","source_stage":"main receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 15-15","quote":"Trypticase peptone (BD BBL)                            2.00       g","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\": 124,\n                        \"attribute\": \"BD BBL\",\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"Na2-fumarate","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3.2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The provider explicitly reports this nominal main-medium g_l value. The primary gives a batch contribution with 1000 mL input water; neither that input nor API volume 1001 establishes measured final volume. Retain only the provider-declared rate with its source basis; no attached amount claim currently exists.","source_stage":"main receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 16-16","quote":"Na2-fumarate                                           3.20       g","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2-fumarate\",\n                        \"compound_id\": 276,\n                        \"amount\": 3.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.2,\n                        \"mmol_l\": 19.9955,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The provider explicitly reports this nominal main-medium g_l value. The primary gives a batch contribution with 1000 mL input water; neither that input nor API volume 1001 establishes measured final volume. Retain only the provider-declared rate with its source basis; no attached amount claim currently exists.","source_stage":"main receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 17-17","quote":"Na2CO3                                                 1.00       g","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 9.43503,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The provider explicitly reports this nominal main-medium g_l value. The primary gives a batch contribution with 1000 mL input water; neither that input nor API volume 1001 establishes measured final volume. Retain only the provider-declared rate with its source basis; no attached amount claim currently exists.","source_stage":"main receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 18-18","quote":"Na2S x 9 H2O                                           0.50       g","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[15]","quote":"{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.08175,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"This value is an SL-10 stock component, not a direct main-medium rate. The primary explicitly makes SL-10 up to 1000 mL; retain its stock concentration and separately represent the 1 mL receiving-batch addition. Do not multiply or divide by an unestablished final-medium volume. The HCl is 10 mL of a 25%-labelled reagent with unspecified percent basis; provider 2.5 g/L is not a verified mass conversion.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 45-45","quote":"HCl (25%)                                             10.00      ml","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 44-46","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                             10.00      ml\n   FeCl2 x 4 H2O                                          1.50       g","quote_basis":"derivative text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative text"}]},{"quantity_id":"q17","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"This value is an SL-10 stock component, not a direct main-medium rate. The primary explicitly makes SL-10 up to 1000 mL; retain its stock concentration and separately represent the 1 mL receiving-batch addition. Do not multiply or divide by an unestablished final-medium volume.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 46-46","quote":"FeCl2 x 4 H2O                                          1.50       g","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 44-46","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                             10.00      ml\n   FeCl2 x 4 H2O                                          1.50       g","quote_basis":"derivative text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative text"}]},{"quantity_id":"q18","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"This value is an SL-10 stock component, not a direct main-medium rate. The primary explicitly makes SL-10 up to 1000 mL; retain its stock concentration and separately represent the 1 mL receiving-batch addition. Do not multiply or divide by an unestablished final-medium volume.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 56-56","quote":"ZnCl2                                                      70.00      mg","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 44-46","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                             10.00      ml\n   FeCl2 x 4 H2O                                          1.50       g","quote_basis":"derivative text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative text"}]},{"quantity_id":"q19","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This value is an SL-10 stock component, not a direct main-medium rate. The primary explicitly makes SL-10 up to 1000 mL; retain its stock concentration and separately represent the 1 mL receiving-batch addition. Do not multiply or divide by an unestablished final-medium volume.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 57-57","quote":"MnCl2 x 4 H2O                                             100.00      mg","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 44-46","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                             10.00      ml\n   FeCl2 x 4 H2O                                          1.50       g","quote_basis":"derivative text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative text"}]},{"quantity_id":"q20","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"This value is an SL-10 stock component, not a direct main-medium rate. The primary explicitly makes SL-10 up to 1000 mL; retain its stock concentration and separately represent the 1 mL receiving-batch addition. Do not multiply or divide by an unestablished final-medium volume.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 58-58","quote":"H3BO3                                                       6.00      mg","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 44-46","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                             10.00      ml\n   FeCl2 x 4 H2O                                          1.50       g","quote_basis":"derivative text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative text"}]},{"quantity_id":"q21","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"This value is an SL-10 stock component, not a direct main-medium rate. The primary explicitly makes SL-10 up to 1000 mL; retain its stock concentration and separately represent the 1 mL receiving-batch addition. Do not multiply or divide by an unestablished final-medium volume.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 59-59","quote":"CoCl2 x 6 H2O                                             190.00      mg","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 44-46","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                             10.00      ml\n   FeCl2 x 4 H2O                                          1.50       g","quote_basis":"derivative text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative text"}]},{"quantity_id":"q22","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"This value is an SL-10 stock component, not a direct main-medium rate. The primary explicitly makes SL-10 up to 1000 mL; retain its stock concentration and separately represent the 1 mL receiving-batch addition. Do not multiply or divide by an unestablished final-medium volume.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 60-60","quote":"CuCl2 x 2 H2O                                               2.00      mg","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 44-46","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                             10.00      ml\n   FeCl2 x 4 H2O                                          1.50       g","quote_basis":"derivative text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative text"}]},{"quantity_id":"q23","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"This value is an SL-10 stock component, not a direct main-medium rate. The primary explicitly makes SL-10 up to 1000 mL; retain its stock concentration and separately represent the 1 mL receiving-batch addition. Do not multiply or divide by an unestablished final-medium volume.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 61-61","quote":"NiCl2 x 6 H2O                                              24.00      mg","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 44-46","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                             10.00      ml\n   FeCl2 x 4 H2O                                          1.50       g","quote_basis":"derivative text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative text"}]},{"quantity_id":"q24","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"This value is an SL-10 stock component, not a direct main-medium rate. The primary explicitly makes SL-10 up to 1000 mL; retain its stock concentration and separately represent the 1 mL receiving-batch addition. Do not multiply or divide by an unestablished final-medium volume.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 62-62","quote":"Na2MoO4 x 2 H2O                                            36.00      mg","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 44-46","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                             10.00      ml\n   FeCl2 x 4 H2O                                          1.50       g","quote_basis":"derivative text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative text"}]},{"quantity_id":"q25","label":"Existing pH","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ph_value","stored":7.0},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ph_value","stored":7.0},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ph_value","stored":7.0}],"decision":"evidence_only","rationale":"All three pH 7.0 values agree with the primary complete-medium adjustment; no attached scoped claim exists.","source_stage":"completed medium pH","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 28-28","quote":"Adjust pH of the complete medium to 7.0.","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.medium","quote":"{\n            \"id\": 1328,\n            \"name\": \"DEFLUVIITOGA MEDIUM\",\n            \"complex_medium\": \"yes\",\n            \"min_pH\": 7,\n            \"max_pH\": 7,\n            \"source\": \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf\"\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"Retained DSM preparation 1","local_fields":[{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"preparation_steps[0].description","stored":"Dissolve ingredients (except sulfur, cysteine, peptone, fumarate, carbonate and sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissove cysteine, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials containing already the appropriate amount of sulfur and autoclave at 121°C for 20 min. Add peptone, fumarate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Adjust pH of the complete medium to 7.0."}],"decision":"evidence_only","rationale":"The complete current DSM owner text retains these numeric controls and stock boundary accurately. The generated target and KOMODO owner omit preparation; retain the supported owner statement, without calling absence an existing-value error.","source_stage":"main preparation","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 21-28","quote":"Dissolve ingredients (except sulfur, cysteine, peptone, fumarate, carbonate and sulfide)\nand sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it\nanoxic. Add and dissove cysteine, then dispense under 80% N2 and 20% CO2 gas\natmosphere into anoxic Hungate-type tubes or serum vials containing already the\nappropriate amount of sulfur and autoclave at 121°C for 20 min. Add peptone, fumarate\nand sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate\nfrom a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture.\nAdjust pH of the complete medium to 7.0.","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Dissolve ingredients (except sulfur, cysteine, peptone, fumarate, carbonate and sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissove cysteine, then dispense under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials containing already the appropriate amount of sulfur and autoclave at 121\\u00b0C for 20 min. Add peptone, fumarate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Adjust pH of the complete medium to 7.0.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"Retained DSM preparation 2","local_fields":[{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"preparation_steps[1].description","stored":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}],"decision":"correct","rationale":"The retained wording and 1000.00 ml makeup are supported for the SL-10 stock. Their current placement as unqualified DSM owner preparation_steps[1], beside the main method and without a stock container, does not preserve that boundary. Retain the exact supported text and numeric control while explicitly scoping this step to SL-10. The generated target and KOMODO owner omit preparation; no amount or quote is changed.","source_stage":"SL-10 stock final makeup","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Main water","local_fields":[],"decision":"evidence_only","rationale":"1000 mL is input water, not measured final-medium volume.","source_stage":"source-only controls or variant boundary","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 19-19","quote":"Distilled water                                     1000.00      ml","quote_basis":"derivative text"}]},{"quantity_id":"q29","label":"SL-10 dose","local_fields":[],"decision":"evidence_only","rationale":"1 mL is the explicit receiving-batch dose; local direct stock components do not represent that topology.","source_stage":"source-only controls or variant boundary","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative text"}]},{"quantity_id":"q30","label":"SL-10 input water","local_fields":[],"decision":"evidence_only","rationale":"990 mL input water and explicit makeup to 1000 mL belong to the trace stock only.","source_stage":"source-only controls or variant boundary","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 63-66","quote":"Distilled water                                           990.00      ml\n\nFirst dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q31","label":"Base atmosphere and sterilization","local_fields":[],"decision":"evidence_only","rationale":"Retain exact gas percentages, 30–45 min sparging, 121 C/20 min autoclaving, post-addition stages and pH7.0 from the base paragraph; no additional growth conditions inferred.","source_stage":"source-only controls or variant boundary","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 21-28","quote":"Dissolve ingredients (except sulfur, cysteine, peptone, fumarate, carbonate and sulfide)\nand sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it\nanoxic. Add and dissove cysteine, then dispense under 80% N2 and 20% CO2 gas\natmosphere into anoxic Hungate-type tubes or serum vials containing already the\nappropriate amount of sulfur and autoclave at 121°C for 20 min. Add peptone, fumarate\nand sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate\nfrom a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture.\nAdjust pH of the complete medium to 7.0.","quote_basis":"derivative text"}]},{"quantity_id":"q32","label":"Printed strain-specific variants","local_fields":[],"decision":"evidence_only","rationale":"These explicitly named DSM overrides are separate source variants. Their amounts are not substituted into the selected unqualified base; no target-organism assertion is inferred.","source_stage":"source-only controls or variant boundary","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt lines 31-39","quote":"For DSM 24444: Omit Trypticase peptone and fumarate. Increase amount of yeast extract\nto 2.0 g/l and supplement medium with 0.2 g/l Na-acetate and 0.6 g/l DL-lactate added\nafter autoclaving from sterile anoxic stock solutions prepared under 100% N2 gas.\nFor DSM 25546: Omit Trypticase peptone and fumarate. Increase amount of yeast extract\nto 2.0 g/l, supplement medium with 0.2 g/l Na-acetate and add 3.0 g/l D-xylose after\nautoclaving from anoxic stock solutions prepared under 100% N2 gas and sterilized by\nfiltration.\nFor DSM 29926: Supplement medium with 6.0 g/l D-glucose added to the medium after\nautoclaving from a sterile anoxic stock solution prepared under 100% N2 gas.","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml":null,"data/normalized_yaml/bacterial/defluviitoga_medium.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:004084.

All current asserted CHEBI objects and exact MIM rows are independently joined. Label agreement does not verify supplied forms: sodium resazurin and nickel hexahydrate conflict with their current IDs. CHEBI:26833 includes elemental-sulfur synonyms but denotes an atom; preserve powdered elemental material and resolve granularity without assuming a specific allotrope. Coverage metrics are ingredient-instance linkage, not scientific accuracy.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:004084.

Read both complete October source reviews and three complete October diagnostic reports, plus the archive method and exact1328 source-duplicate row. Current API1328 raw digest equals historical 74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb; current catalog raw equals historical d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. This authenticates equal content now, not recovery of the old access event. Historical unsupported/conflict decisions were unchanged, and no attached owner amount claims are present. Current conservative merger and stock-preserving importer improvements are credited; the old generated omission is not a current ingredient-only merger claim.

## Findings

### f1: Restore main-versus-SL-10 structure and resazurin stock identity

major / open / confirmed; issue key: culturemech-004084-stock-stage.

Restore nine SL-10 stock components to their separate stock stage and record the receiving dose. Preserve the explicit sodium-resazurin stock dose and w/v label. HCl 25% remains basis-ambiguous; do not treat provider 2.5 g/L as verified mass or infer final-medium rates from input water.

### f2: Reconcile aerobic metadata and retain preparation without unsafe merging

major / open / confirmed; issue key: culturemech-004084-anoxic-preparation.

The target and KOMODO owner say Aerobic: Yes, conflicting with the base primary anoxic preparation. The maintained DSM owner retains the supported base-method and SL-10 makeup text, whereas the generated target drops both. Its SL-10 instruction is an unqualified main preparation step without a stock container; preserve the wording and numeric makeup while explicitly placing it in the SL-10 stock scope. Qualify the imported catalog boolean and keep printed strain overrides separate. Current merger rejects these unequal notes/preparation; reconcile maintained source identities before regenerating rather than forcing a duplicate merge.

### f3: Correct sodium-resazurin and nickel-hydrate identifiers

major / open / confirmed; issue key: culturemech-004084-supplied-forms.

The source explicitly supplies sodium resazurin, but CHEBI:8806 denotes neutral C12H7NO4. Nickel chloride hexahydrate is asserted as anhydrous CHEBI:34887 in both primary and secondary slots; freshly inspected CHEBI:53542 denotes the hexahydrate. Correct exact supplied-form links after curation review without rescaling source masses. Sulfur-atom versus elemental-powder granularity remains an explicitly bounded ontology concern, not a fabricated allotrope assertion.

### f4: Attach scoped claims and correct future timestamp formatting

minor / open / confirmed; issue key: culturemech-004084-claim-provenance.

No selected concentration has an attached exact amount claim despite two historical source reviews. Preserve those unchanged historical decisions and dates, attach new scoped evidence to reconciled maintained assertions, and retain the malformed historical .fZ timestamp as history. Fix the current KOMODO writer time.strftime %f formatting for future events; do not rewrite the historical event.

## Recommended Actions And Acceptance Checks

### a1

Restore nine SL-10 stock components to their separate stock stage and record the receiving dose. Preserve the explicit sodium-resazurin stock dose and w/v label. HCl 25% remains basis-ambiguous; do not treat provider 2.5 g/L as verified mass or infer final-medium rates from input water.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

The target and KOMODO owner say Aerobic: Yes, conflicting with the base primary anoxic preparation. The maintained DSM owner retains the supported base-method and SL-10 makeup text, whereas the generated target drops both. Its SL-10 instruction is an unqualified main preparation step without a stock container; preserve the wording and numeric makeup while explicitly placing it in the SL-10 stock scope. Qualify the imported catalog boolean and keep printed strain overrides separate. Current merger rejects these unequal notes/preparation; reconcile maintained source identities before regenerating rather than forcing a duplicate merge.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The source explicitly supplies sodium resazurin, but CHEBI:8806 denotes neutral C12H7NO4. Nickel chloride hexahydrate is asserted as anhydrous CHEBI:34887 in both primary and secondary slots; freshly inspected CHEBI:53542 denotes the hexahydrate. Correct exact supplied-form links after curation review without rescaling source masses. Sulfur-atom versus elemental-powder granularity remains an explicitly bounded ontology concern, not a fabricated allotrope assertion.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

No selected concentration has an attached exact amount claim despite two historical source reviews. Preserve those unchanged historical decisions and dates, attach new scoped evidence to reconciled maintained assertions, and retain the malformed historical .fZ timestamp as history. Fix the current KOMODO writer time.strftime %f formatting for future events; do not rewrite the historical event.

- New claim evidence is field- and stage-specific, prior history remains byte-preserved, and a new event records actual curation.
- The future KOMODO converter emits a valid UTC timestamp using a supported datetime formatter; do not backdate or replace the old .fZ event.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsm1328 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf; REVIEW_WORK/batch072/source07-08-10/dsm1328.json; exact original raw/text/hash/time metadata | context_only | Exact DSM1328 primary; base recipe assessed separately from printed strain overrides. |
| api1328 | https://mediadive.dsmz.de/rest/medium/1328; REVIEW_WORK/batch072/source07-08-10/api1328.json; exact original raw/text/hash/time metadata | context_only | Current provider1328 source version and composition stages. |
| komodo1328 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1328; REVIEW_WORK/batch072/source07-08-10/komodo1328.json; exact original raw/text/hash/time metadata | context_only | Exact historical literal route; no assumption that unavailable detail agrees with DSM1328. |
| komodoList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; REVIEW_WORK/batch072/source07-08-10/komodoList.json; exact original raw/text/hash/time metadata | context_only | Exact historical catalog identity route. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; REVIEW_WORK/batch072/source07-08-10/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi33403 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33403; REVIEW_WORK/batch072/source07-08-10/chebi33403.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| target | data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| owner-2 | data/normalized_yaml/bacterial/defluviitoga_medium.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| report-18 | reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-19 | reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-20 | reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/defluviitoga_medium.yaml.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/inspected-candidate-context.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-22 | reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-23 | reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-26 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/defluviitoga_medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| writer-komodo | src/culturemech/import/komodo_web_importer.py; KomodoWebImporter._convert_to_culturemech | context_only | The current converter copies is_aerobic into notes and uses time.strftime with unsupported %f. This is present code behavior, not proof of the original run. |
| historical-reading | REVIEW_WORK/batch072/record07/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch072/record07/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch072/record07/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser excludes percent-stock additions from primary ingredients, preserves referenced stock amounts/attributes separately and prioritizes explicit provider g_l. It skips source water; bare units alone do not establish a final-volume basis. Current code is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| historical-object-joins | REVIEW_WORK/batch072/record07/historical-current-object-joins.json; Complete exact decoded-object comparisons | context_only | Historical object correspondence is distinct from raw-response authentication. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; REVIEW_WORK/batch072/source07-08-10/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; REVIEW_WORK/batch072/source07-08-10/chebi131527.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; REVIEW_WORK/batch072/source07-08-10/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; REVIEW_WORK/batch072/source07-08-10/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; REVIEW_WORK/batch072/source07-08-10/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; REVIEW_WORK/batch072/source07-08-10/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; REVIEW_WORK/batch072/source07-08-10/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; REVIEW_WORK/batch072/source07-08-10/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi26833 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26833; REVIEW_WORK/batch072/source07-08-10/chebi26833.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; REVIEW_WORK/batch072/source07-08-10/chebi91248.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi115156 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_115156; REVIEW_WORK/batch072/source07-08-10/chebi115156.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; REVIEW_WORK/batch072/source07-08-10/chebi29377.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; REVIEW_WORK/batch072/source07-08-10/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; REVIEW_WORK/batch072/source07-08-10/chebi17883.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; REVIEW_WORK/batch072/source07-08-10/chebi86249.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; REVIEW_WORK/batch072/source07-08-10/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; REVIEW_WORK/batch072/source07-08-10/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; REVIEW_WORK/batch072/source07-08-10/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; REVIEW_WORK/batch072/source07-08-10/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; REVIEW_WORK/batch072/source07-08-10/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; REVIEW_WORK/batch072/source07-08-10/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; REVIEW_WORK/batch072/source07-08-10/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| quantities | REVIEW_WORK/batch072/record07/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch072/record07/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch072/record07/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch072/record07/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch072/record07/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch072/record07/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch072/record07/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch072/record07/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch072/record07/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch072/record07/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch072/record07/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Direct KOMODO1328 detail is unavailable (403); current catalog identity and DSM primary do not independently recover its full detail page.
- The source-duplicate archive is reviewed only for its method and selected1328 row; other hundreds of pairs are outside scope.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T164612Z-culturemech-004084-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: DEFLUVIITOGA medium'
started_at: '2026-10-28T16:15:15.871473Z'
finished_at: '2026-10-28T16:46:12.611812Z'
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
summary: Partial source review identifies three major formulation, preparation and
  chemical-form issues plus one minor provenance follow-up. Existing DSM preparation
  and explicit provider rates are credited with their exact stage and denominator
  limits; no recipe was edited.
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
  - path: data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml
    sha256: 169d185d943c5482d3f5d773d4a3da44c2c93b1796253f8b5eb49828f1506063
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml
    sha256: 33b3a1e099b948b5e092122b1eeb56be39bde7f42554286ca7473cf510fbe8f2
    role: context
  - path: data/normalized_yaml/bacterial/defluviitoga_medium.yaml
    sha256: 0d22fde9618019fefd7c4bb8188535a8ea75e1a60473e0b76340e2ccf9b71fd4
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/plan.json
    sha256: 94e89303f14558d9b0d485aa6cb4eb646050837864ab920d759763a3a483b94f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/defluviitoga_medium.yaml.md
    sha256: 5965a1080570d6cbd62d5efb31906a33055c8f8ce4ac317ebcaefbe705f70d48
    role: context
  - path: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/inspected-candidate-context.json
    sha256: bef58d348ed78c4694bd9876429eea22eed599556ff8a9f9b79f4858745bd02e
    role: context
  - path: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/plan.json
    sha256: 0fc7158ec48d1b0c75efa149070b46b677bb3389d969a1440267f43e21b3d3c8
    role: context
  - path: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml.md
    sha256: 164ccc40b251753d507cbd1d051948f6dac0de9a5f0bf814fbe9056cbfa2ddde
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.md
    sha256: 0a2ae4f4455082b36d449ed9b9f1675883ac326e3d4b1eb4a0cbf3595c9467c1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.md
    sha256: dcc189d8617d6b9ada8ba411aaf9e25e5e837d485ec154e41f4a3ef552689a39
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/defluviitoga_medium.md
    sha256: cbe5a47f081468a27de9786634ecb5f190d47cba0b87208e87f798f84d00bf45
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
  selection: Authoritative batch072 index 07
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:004084
targets:
- target_id: CultureMech:004084
  path: data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml
  label: defluviitoga_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/defluviitoga_medium.yaml
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
  - CultureMech:004084
  command: just validate-schema data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml
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
  - CultureMech:004084
  command: just validate-strict data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml --out
    REVIEW_WORK/batch072/record07/strict.tsv --workers 1 --quiet
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
  - CultureMech:004084
  command: just validate-terms data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml
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
  - CultureMech:004084
  command: just validate-references data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsm1328
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf
  accessed_at: '2026-10-28T16:14:43.945511Z'
  locator: REVIEW_WORK/batch072/source07-08-10/dsm1328.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact DSM1328 primary; base recipe assessed separately from printed strain
    overrides.
  snapshot_sha256: 5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5
- evidence_id: api1328
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1328
  accessed_at: '2026-10-28T16:14:43.614284Z'
  locator: REVIEW_WORK/batch072/source07-08-10/api1328.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Current provider1328 source version and composition stages.
  snapshot_sha256: 74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb
- evidence_id: komodo1328
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1328
  accessed_at: '2026-10-28T16:14:43.138001Z'
  locator: REVIEW_WORK/batch072/source07-08-10/komodo1328.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact historical literal route; no assumption that unavailable detail agrees
    with DSM1328.
  snapshot_sha256: a741f9d8d479dec87dd674d4b9053b831053874405793bd247b5efa8cdb06bd5
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1328;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodoList
  kind: primary_source
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  accessed_at: '2026-10-28T16:14:44.729596Z'
  locator: REVIEW_WORK/batch072/source07-08-10/komodoList.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact historical catalog identity route.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  accessed_at: '2026-10-28T16:14:50.065835Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi53542.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
- evidence_id: chebi33403
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33403
  accessed_at: '2026-10-28T16:14:49.261338Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi33403.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b349493be5d8cb371d1e71751510f9205880ab9d0a14f560191e05606c127a60
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T16:19:29.080084Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 169d185d943c5482d3f5d773d4a3da44c2c93b1796253f8b5eb49828f1506063
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T16:19:29.080240Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 33b3a1e099b948b5e092122b1eeb56be39bde7f42554286ca7473cf510fbe8f2
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T16:19:29.080263Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T16:19:29.080541Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T16:19:29.080561Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T16:19:29.080580Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/defluviitoga_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T16:19:29.080601Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: 0d22fde9618019fefd7c4bb8188535a8ea75e1a60473e0b76340e2ccf9b71fd4
- evidence_id: report-18
  kind: prior_review
  reference: reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md
  locator: Complete report
  accessed_at: '2026-10-28T16:19:29.080621Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: a723d4b7950bf4ac296a8a7fe4890d4d0881199a5d17c12a5fe39c2afbc40a10
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T16:19:29.080683Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 94e89303f14558d9b0d485aa6cb4eb646050837864ab920d759763a3a483b94f
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/defluviitoga_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T16:19:29.086723Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 5965a1080570d6cbd62d5efb31906a33055c8f8ce4ac317ebcaefbe705f70d48
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/inspected-candidate-context.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T16:19:29.086788Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: bef58d348ed78c4694bd9876429eea22eed599556ff8a9f9b79f4858745bd02e
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T16:19:29.087506Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 0fc7158ec48d1b0c75efa149070b46b677bb3389d969a1440267f43e21b3d3c8
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T16:19:29.091605Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 164ccc40b251753d507cbd1d051948f6dac0de9a5f0bf814fbe9056cbfa2ddde
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T16:19:29.091664Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 0a2ae4f4455082b36d449ed9b9f1675883ac326e3d4b1eb4a0cbf3595c9467c1
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T16:19:29.091690Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: dcc189d8617d6b9ada8ba411aaf9e25e5e837d485ec154e41f4a3ef552689a39
- evidence_id: report-26
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/defluviitoga_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T16:19:29.091713Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: cbe5a47f081468a27de9786634ecb5f190d47cba0b87208e87f798f84d00bf45
- evidence_id: writer-komodo
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: KomodoWebImporter._convert_to_culturemech
  accessed_at: '2026-10-28T16:19:29.100936Z'
  support: context_only
  summary: The current converter copies is_aerobic into notes and uses time.strftime
    with unsupported %f. This is present code behavior, not proof of the original
    run.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch072/record07/historical-reading.json
  accessed_at: '2026-10-28T16:19:29.103136Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: ef1dfa2d2327fa457c2d97c37d82849ed2fa96365ae6c36aadf62c4145da40f4
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch072/record07/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T16:19:29.103243Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 71fe0a0a1dd053632c10b0e78cb642fb12b7ba33eaf0d6a20c89156b52f5008f
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch072/record07/complete-document-reader.json
  accessed_at: '2026-10-28T16:19:29.103451Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: be8671ab37ebcaef47818ee08ec27bcb9592db5eb1f844fe48072ffbd2797a33
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T16:19:29.103501Z'
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
  accessed_at: '2026-10-28T16:19:29.103540Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: historical-object-joins
  kind: prior_review
  reference: REVIEW_WORK/batch072/record07/historical-current-object-joins.json
  accessed_at: '2026-10-28T16:19:29.103569Z'
  locator: Complete exact decoded-object comparisons
  support: context_only
  summary: Historical object correspondence is distinct from raw-response authentication.
  snapshot_sha256: 5cb45e920bc94a9e65030403551e5c481c2a959a19767d90e27051cf473b00e1
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  accessed_at: '2026-10-28T16:14:50.538205Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi63036.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  accessed_at: '2026-10-28T16:14:45.396574Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi131527.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  accessed_at: '2026-10-28T16:14:48.051825Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi31206.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  accessed_at: '2026-10-28T16:14:46.965218Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi26710.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  accessed_at: '2026-10-28T16:14:48.834887Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi32588.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  accessed_at: '2026-10-28T16:14:51.723753Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi86345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  accessed_at: '2026-10-28T16:14:51.174910Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi86158.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  accessed_at: '2026-10-28T16:14:51.753409Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi8806.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi26833
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26833
  accessed_at: '2026-10-28T16:14:47.304205Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi26833.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 34952547270a6bcbbfa3a3699082c8d5359e51d0f90518ab9ca5400494a8ae33
- evidence_id: chebi91248
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248
  accessed_at: '2026-10-28T16:14:51.923044Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi91248.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683
- evidence_id: chebi115156
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_115156
  accessed_at: '2026-10-28T16:14:44.933126Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi115156.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 5ff8efa80c6b0a7a4a764e6c2b95eaf39e97073440e33b02d6dd2b3affd79452
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377
  accessed_at: '2026-10-28T16:14:47.550695Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi29377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  accessed_at: '2026-10-28T16:14:51.075822Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi76209.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  accessed_at: '2026-10-28T16:14:46.833373Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi17883.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  accessed_at: '2026-10-28T16:14:51.248707Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi86249.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  accessed_at: '2026-10-28T16:14:49.865653Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi49976.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  accessed_at: '2026-10-28T16:14:51.731255Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi86368.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  accessed_at: '2026-10-28T16:14:49.231985Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi33118.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  accessed_at: '2026-10-28T16:14:50.065954Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi53503.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  accessed_at: '2026-10-28T16:14:51.294598Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi86318.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  accessed_at: '2026-10-28T16:14:49.374218Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi34887.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  accessed_at: '2026-10-28T16:14:50.654856Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi75213.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch072/record07/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:46:12.611812Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 788ec111d9e04282b0a2482b590865b415e4663ae9accb6c8aeeae4962f21af2
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch072/record07/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:19:29.222189Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: e7200219dd610a6ee860575f97044272ffd49c25b203dabe08ecbceb2aab9712
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch072/record07/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:19:29.222301Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 638112b6f416a19484b9ac755c0da8b44a77f408d9e4b61771cb9a27d4d8b2ba
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch072/record07/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:19:29.222357Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 33205115c7fec78f678fae559f5ff38d3b2577e703e99dce2b405d923081e16c
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch072/record07/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:19:29.222409Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: aede211cbcb962e853d58af03e78564d66d7980a4294bae9daf1e061ff8b6d47
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch072/record07/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:19:29.222430Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 9b7ce8b54390d4eb8113b257de06fc9a1844006eef95be2b6400f0a04cf089cc
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch072/record07/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:19:29.222449Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch072/record07/schema-result.json
  accessed_at: '2026-10-28T16:15:16.970417Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 763e4851e2abaa8e2eac7f89680a78262205373c9f3b39ff66033b8acdfd90f7
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch072/record07/strict-result.json
  accessed_at: '2026-10-28T16:15:17.880357Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: e06d3895cde1a356925fdd70cc7babea883b34f4934ee989907925030db4430b
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch072/record07/terms-result.json
  accessed_at: '2026-10-28T16:15:18.880525Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 864f35478f9b468a4aa4b68956ffb79f13e7e128571d38549a4f4ff0e2471572
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch072/record07/references-result.json
  accessed_at: '2026-10-28T16:15:19.582003Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 4c2d1acb8fcd061dada52f30ef09af1b67132884258cebeafab68b082cde6219
assessments:
- assessment_id: identity
  area: identity
  topic: Exact source accession and duplicate scope
  outcome: concern
  summary: DSM1328 and the current exact KOMODO catalog row identify the selected
    source family, but the direct KOMODO detail returns403. Local source-duplicate
    links do not establish whole-formulation equality; maintained DSM preparation
    and KOMODO aerobic metadata differ.
  target_ids:
  - CultureMech:004084
  evidence_ids:
  - target
  - owner
  - owner-2
  - komodoList
  - komodo1328
  - dsm1328
- assessment_id: classification
  area: consistency
  topic: Record classification and organism limits
  outcome: supported
  summary: Liquid, complex and undefined classification is consistent with yeast extract
    and peptone in the unqualified base. No target organism or strain-growth claim
    follows from a medium name. Printed strain overrides remain source-only variants.
  target_ids:
  - CultureMech:004084
  evidence_ids:
  - dsm1328
  - api1328
- assessment_id: structure
  area: schema
  topic: Native structure and generated ownership
  outcome: supported
  summary: All original canonical checks pass; reference validation checked zero attached
    references. Structural success does not endorse the stock or chemical assertions.
    Both maintained owners and current merge code are identified.
  target_ids:
  - CultureMech:004084
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
  - writer-merger
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 72 current concentration fields are covered by 32 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:004084
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b072-quantity-inventory-v1","target":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","quantity_field_count":72,"decisions":[{"quantity_id":"q1","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    provider explicitly reports this nominal main-medium g_l value. The primary gives
    a batch contribution with 1000 mL input water; neither that input nor API volume
    1001 establishes measured final volume. Retain only the provider-declared rate
    with its source basis; no attached amount claim currently exists.","source_stage":"main
    receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 3-3","quote":"KH2PO4                                                 0.30       g","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    2.2045,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q2","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    provider explicitly reports this nominal main-medium g_l value. The primary gives
    a batch contribution with 1000 mL input water; neither that input nor API volume
    1001 establishes measured final volume. Retain only the provider-declared rate
    with its source basis; no attached amount claim currently exists.","source_stage":"main
    receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 4-4","quote":"K2HPO4                                                 0.30       g","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    1.7224,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    provider explicitly reports this nominal main-medium g_l value. The primary gives
    a batch contribution with 1000 mL input water; neither that input nor API volume
    1001 establishes measured final volume. Retain only the provider-declared rate
    with its source basis; no attached amount claim currently exists.","source_stage":"main
    receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 5-5","quote":"NH4Cl                                                  1.00       g","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    18.6951,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q4","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    provider explicitly reports this nominal main-medium g_l value. The primary gives
    a batch contribution with 1000 mL input water; neither that input nor API volume
    1001 establishes measured final volume. Retain only the provider-declared rate
    with its source basis; no attached amount claim currently exists.","source_stage":"main
    receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 6-6","quote":"NaCl                                                   1.00       g","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    17.1116,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q5","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    provider explicitly reports this nominal main-medium g_l value. The primary gives
    a batch contribution with 1000 mL input water; neither that input nor API volume
    1001 establishes measured final volume. Retain only the provider-declared rate
    with its source basis; no attached amount claim currently exists.","source_stage":"main
    receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 7-7","quote":"KCl                                                    0.10       g","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    1.34138,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q6","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    provider explicitly reports this nominal main-medium g_l value. The primary gives
    a batch contribution with 1000 mL input water; neither that input nor API volume
    1001 establishes measured final volume. Retain only the provider-declared rate
    with its source basis; no attached amount claim currently exists.","source_stage":"main
    receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 8-8","quote":"MgCl2 x 6 H2O                                          0.50       g","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.45938,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q7","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    provider explicitly reports this nominal main-medium g_l value. The primary gives
    a batch contribution with 1000 mL input water; neither that input nor API volume
    1001 establishes measured final volume. Retain only the provider-declared rate
    with its source basis; no attached amount claim currently exists.","source_stage":"main
    receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 9-9","quote":"CaCl2 x 2 H2O                                          0.10       g","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.680203,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q8","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    provider explicitly reports this nominal main-medium g_l value. The primary gives
    a batch contribution with 1000 mL input water; neither that input nor API volume
    1001 establishes measured final volume. Retain only the provider-declared rate
    with its source basis; no attached amount claim currently exists.","source_stage":"main
    receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 11-11","quote":"Yeast extract (OXOID)                                  1.00       g","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"attribute\": \"OXOID\",\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q9","label":"Sodium resazurin","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.0005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.0005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.0005","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary adds 0.50 mL of explicitly 0.1% w/v sodium-resazurin stock; the provider
    scalar 0.0005 g/L loses the stock label and dose. It corresponds to 0.0005 g per
    listed batch, not independently proven final g/L. Preserve the explicit percentage
    basis and dose without assuming final volume.","source_stage":"main receiving
    batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 12-12","quote":"Sodium resazurin (0.1% w/v)                            0.50      ml","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.0005,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q10","label":"Sulfur","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    provider explicitly reports this nominal main-medium g_l value. The primary gives
    a batch contribution with 1000 mL input water; neither that input nor API volume
    1001 establishes measured final volume. Retain only the provider-declared rate
    with its source basis; no attached amount claim currently exists.","source_stage":"main
    receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 13-13","quote":"Sulfur (powdered)                                     10.00       g","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Sulfur\",\n                        \"compound_id\":
    80,\n                        \"condition\": \"\",\n                        \"attribute\":
    \"powdered\",\n                        \"amount\": 10,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\":
    311.818,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q11","label":"L-Cysteine HCl x H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    provider explicitly reports this nominal main-medium g_l value. The primary gives
    a batch contribution with 1000 mL input water; neither that input nor API volume
    1001 establishes measured final volume. Retain only the provider-declared rate
    with its source basis; no attached amount claim currently exists.","source_stage":"main
    receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 14-14","quote":"L-Cysteine HCl x H2O                                   0.50       g","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\":
    770,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.8468,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q12","label":"Trypticase peptone","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    provider explicitly reports this nominal main-medium g_l value. The primary gives
    a batch contribution with 1000 mL input water; neither that input nor API volume
    1001 establishes measured final volume. Retain only the provider-declared rate
    with its source basis; no attached amount claim currently exists.","source_stage":"main
    receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 15-15","quote":"Trypticase peptone (BD BBL)                            2.00       g","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\":
    124,\n                        \"attribute\": \"BD BBL\",\n                        \"amount\":
    2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    2,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q13","label":"Na2-fumarate","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3.2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    provider explicitly reports this nominal main-medium g_l value. The primary gives
    a batch contribution with 1000 mL input water; neither that input nor API volume
    1001 establishes measured final volume. Retain only the provider-declared rate
    with its source basis; no attached amount claim currently exists.","source_stage":"main
    receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 16-16","quote":"Na2-fumarate                                           3.20       g","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na2-fumarate\",\n                        \"compound_id\":
    276,\n                        \"amount\": 3.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.2,\n                        \"mmol_l\":
    19.9955,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q14","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    provider explicitly reports this nominal main-medium g_l value. The primary gives
    a batch contribution with 1000 mL input water; neither that input nor API volume
    1001 establishes measured final volume. Retain only the provider-declared rate
    with its source basis; no attached amount claim currently exists.","source_stage":"main
    receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 17-17","quote":"Na2CO3                                                 1.00       g","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    9.43503,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q15","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    provider explicitly reports this nominal main-medium g_l value. The primary gives
    a batch contribution with 1000 mL input water; neither that input nor API volume
    1001 establishes measured final volume. Retain only the provider-declared rate
    with its source basis; no attached amount claim currently exists.","source_stage":"main
    receiving batch/provider nominal normalization","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 18-18","quote":"Na2S x 9 H2O                                           0.50       g","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].recipe[15]","quote":"{\n                        \"recipe_order\":
    16,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.08175,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q16","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    value is an SL-10 stock component, not a direct main-medium rate. The primary
    explicitly makes SL-10 up to 1000 mL; retain its stock concentration and separately
    represent the 1 mL receiving-batch addition. Do not multiply or divide by an unestablished
    final-medium volume. The HCl is 10 mL of a 25%-labelled reagent with unspecified
    percent basis; provider 2.5 g/L is not a verified mass conversion.","source_stage":"SL-10
    stock","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 45-45","quote":"HCl (25%)                                             10.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 44-46","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                             10.00      ml\n   FeCl2
    x 4 H2O                                          1.50       g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q17","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    value is an SL-10 stock component, not a direct main-medium rate. The primary
    explicitly makes SL-10 up to 1000 mL; retain its stock concentration and separately
    represent the 1 mL receiving-batch addition. Do not multiply or divide by an unestablished
    final-medium volume.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 46-46","quote":"FeCl2 x 4 H2O                                          1.50       g","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 44-46","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                             10.00      ml\n   FeCl2
    x 4 H2O                                          1.50       g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q18","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    value is an SL-10 stock component, not a direct main-medium rate. The primary
    explicitly makes SL-10 up to 1000 mL; retain its stock concentration and separately
    represent the 1 mL receiving-batch addition. Do not multiply or divide by an unestablished
    final-medium volume.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 56-56","quote":"ZnCl2                                                      70.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 44-46","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                             10.00      ml\n   FeCl2
    x 4 H2O                                          1.50       g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q19","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    value is an SL-10 stock component, not a direct main-medium rate. The primary
    explicitly makes SL-10 up to 1000 mL; retain its stock concentration and separately
    represent the 1 mL receiving-batch addition. Do not multiply or divide by an unestablished
    final-medium volume.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 57-57","quote":"MnCl2 x 4 H2O                                             100.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 44-46","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                             10.00      ml\n   FeCl2
    x 4 H2O                                          1.50       g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q20","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    value is an SL-10 stock component, not a direct main-medium rate. The primary
    explicitly makes SL-10 up to 1000 mL; retain its stock concentration and separately
    represent the 1 mL receiving-batch addition. Do not multiply or divide by an unestablished
    final-medium volume.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 58-58","quote":"H3BO3                                                       6.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 44-46","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                             10.00      ml\n   FeCl2
    x 4 H2O                                          1.50       g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q21","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    value is an SL-10 stock component, not a direct main-medium rate. The primary
    explicitly makes SL-10 up to 1000 mL; retain its stock concentration and separately
    represent the 1 mL receiving-batch addition. Do not multiply or divide by an unestablished
    final-medium volume.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 59-59","quote":"CoCl2 x 6 H2O                                             190.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 44-46","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                             10.00      ml\n   FeCl2
    x 4 H2O                                          1.50       g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q22","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    value is an SL-10 stock component, not a direct main-medium rate. The primary
    explicitly makes SL-10 up to 1000 mL; retain its stock concentration and separately
    represent the 1 mL receiving-batch addition. Do not multiply or divide by an unestablished
    final-medium volume.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 60-60","quote":"CuCl2 x 2 H2O                                               2.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 44-46","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                             10.00      ml\n   FeCl2
    x 4 H2O                                          1.50       g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q23","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    value is an SL-10 stock component, not a direct main-medium rate. The primary
    explicitly makes SL-10 up to 1000 mL; retain its stock concentration and separately
    represent the 1 mL receiving-batch addition. Do not multiply or divide by an unestablished
    final-medium volume.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 61-61","quote":"NiCl2 x 6 H2O                                              24.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 44-46","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                             10.00      ml\n   FeCl2
    x 4 H2O                                          1.50       g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q24","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    value is an SL-10 stock component, not a direct main-medium rate. The primary
    explicitly makes SL-10 up to 1000 mL; retain its stock concentration and separately
    represent the 1 mL receiving-batch addition. Do not multiply or divide by an unestablished
    final-medium volume.","source_stage":"SL-10 stock","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 62-62","quote":"Na2MoO4 x 2 H2O                                            36.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 44-46","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                             10.00      ml\n   FeCl2
    x 4 H2O                                          1.50       g","quote_basis":"derivative
    text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"},{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q25","label":"Existing pH","local_fields":[{"path":"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml","field_path":"ph_value","stored":7.0},{"path":"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml","field_path":"ph_value","stored":7.0},{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"ph_value","stored":7.0}],"decision":"evidence_only","rationale":"All
    three pH 7.0 values agree with the primary complete-medium adjustment; no attached
    scoped claim exists.","source_stage":"completed medium pH","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 28-28","quote":"Adjust pH of the complete medium to 7.0.","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.medium","quote":"{\n            \"id\":
    1328,\n            \"name\": \"DEFLUVIITOGA MEDIUM\",\n            \"complex_medium\":
    \"yes\",\n            \"min_pH\": 7,\n            \"max_pH\": 7,\n            \"source\":
    \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf\"\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q26","label":"Retained DSM preparation 1","local_fields":[{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"preparation_steps[0].description","stored":"Dissolve
    ingredients (except sulfur, cysteine, peptone, fumarate, carbonate and sulfide)
    and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make
    it anoxic. Add and dissove cysteine, then dispense under 80% N2 and 20% CO2 gas
    atmosphere into anoxic Hungate-type tubes or serum vials containing already the
    appropriate amount of sulfur and autoclave at 121°C for 20 min. Add peptone, fumarate
    and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and
    carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2
    gas mixture. Adjust pH of the complete medium to 7.0."}],"decision":"evidence_only","rationale":"The
    complete current DSM owner text retains these numeric controls and stock boundary
    accurately. The generated target and KOMODO owner omit preparation; retain the
    supported owner statement, without calling absence an existing-value error.","source_stage":"main
    preparation","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 21-28","quote":"Dissolve ingredients (except sulfur, cysteine, peptone,
    fumarate, carbonate and sulfide)\nand sparge medium with 80% N2 and 20% CO2 gas
    mixture for 30 - 45 min to make it\nanoxic. Add and dissove cysteine, then dispense
    under 80% N2 and 20% CO2 gas\natmosphere into anoxic Hungate-type tubes or serum
    vials containing already the\nappropriate amount of sulfur and autoclave at 121°C
    for 20 min. Add peptone, fumarate\nand sulfide from sterile anoxic stock solutions
    prepared under 100% N2 gas and carbonate\nfrom a sterile anoxic stock solution
    prepared under 80% N2 and 20% CO2 gas mixture.\nAdjust pH of the complete medium
    to 7.0.","quote_basis":"derivative text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Dissolve ingredients (except sulfur, cysteine, peptone, fumarate, carbonate
    and sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45
    min to make it anoxic. Add and dissove cysteine, then dispense under 80% N2 and
    20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials containing
    already the appropriate amount of sulfur and autoclave at 121\\u00b0C for 20 min.
    Add peptone, fumarate and sulfide from sterile anoxic stock solutions prepared
    under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared
    under 80% N2 and 20% CO2 gas mixture. Adjust pH of the complete medium to 7.0.\"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q27","label":"Retained DSM preparation 2","local_fields":[{"path":"data/normalized_yaml/bacterial/defluviitoga_medium.yaml","field_path":"preparation_steps[1].description","stored":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally make up to 1000.00 ml."}],"decision":"correct","rationale":"The retained
    wording and 1000.00 ml makeup are supported for the SL-10 stock. Their current
    placement as unqualified DSM owner preparation_steps[1], beside the main method
    and without a stock container, does not preserve that boundary. Retain the exact
    supported text and numeric control while explicitly scoping this step to SL-10.
    The generated target and KOMODO owner omit preparation; no amount or quote is
    changed.","source_stage":"SL-10 stock final makeup","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 65-66","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"},{"evidence_id":"api1328","reference":"https://mediadive.dsmz.de/rest/medium/1328","raw_path":"REVIEW_WORK/batch072/source07-08-10/api1328.raw","raw_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","text_sha256":"74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb","accessed_at":"2026-10-28T16:14:43.614284Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q28","label":"Main water","local_fields":[],"decision":"evidence_only","rationale":"1000
    mL is input water, not measured final-medium volume.","source_stage":"source-only
    controls or variant boundary","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 19-19","quote":"Distilled water                                     1000.00      ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q29","label":"SL-10 dose","local_fields":[],"decision":"evidence_only","rationale":"1
    mL is the explicit receiving-batch dose; local direct stock components do not
    represent that topology.","source_stage":"source-only controls or variant boundary","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 10-10","quote":"Trace element solution SL-10                           1.00      ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q30","label":"SL-10 input water","local_fields":[],"decision":"evidence_only","rationale":"990
    mL input water and explicit makeup to 1000 mL belong to the trace stock only.","source_stage":"source-only
    controls or variant boundary","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 63-66","quote":"Distilled water                                           990.00      ml\n\nFirst
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q31","label":"Base
    atmosphere and sterilization","local_fields":[],"decision":"evidence_only","rationale":"Retain
    exact gas percentages, 30–45 min sparging, 121 C/20 min autoclaving, post-addition
    stages and pH7.0 from the base paragraph; no additional growth conditions inferred.","source_stage":"source-only
    controls or variant boundary","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 21-28","quote":"Dissolve ingredients (except sulfur, cysteine, peptone,
    fumarate, carbonate and sulfide)\nand sparge medium with 80% N2 and 20% CO2 gas
    mixture for 30 - 45 min to make it\nanoxic. Add and dissove cysteine, then dispense
    under 80% N2 and 20% CO2 gas\natmosphere into anoxic Hungate-type tubes or serum
    vials containing already the\nappropriate amount of sulfur and autoclave at 121°C
    for 20 min. Add peptone, fumarate\nand sulfide from sterile anoxic stock solutions
    prepared under 100% N2 gas and carbonate\nfrom a sterile anoxic stock solution
    prepared under 80% N2 and 20% CO2 gas mixture.\nAdjust pH of the complete medium
    to 7.0.","quote_basis":"derivative text"}]},{"quantity_id":"q32","label":"Printed
    strain-specific variants","local_fields":[],"decision":"evidence_only","rationale":"These
    explicitly named DSM overrides are separate source variants. Their amounts are
    not substituted into the selected unqualified base; no target-organism assertion
    is inferred.","source_stage":"source-only controls or variant boundary","sources":[{"evidence_id":"dsm1328","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1328.pdf","raw_path":"REVIEW_WORK/batch072/source07-08-10/dsm1328.raw","raw_sha256":"5d7399bd2b3a6fb6a40787e646cebe613e5165b8860ebda6002e938222c9a5b5","text_sha256":"87ffe66526893844dd59c518b87e1a6db4f28eebf22896e74808b2353e4d77a7","accessed_at":"2026-10-28T16:14:43.945511Z","locator":"dsm1328.txt
    lines 31-39","quote":"For DSM 24444: Omit Trypticase peptone and fumarate. Increase
    amount of yeast extract\nto 2.0 g/l and supplement medium with 0.2 g/l Na-acetate
    and 0.6 g/l DL-lactate added\nafter autoclaving from sterile anoxic stock solutions
    prepared under 100% N2 gas.\nFor DSM 25546: Omit Trypticase peptone and fumarate.
    Increase amount of yeast extract\nto 2.0 g/l, supplement medium with 0.2 g/l Na-acetate
    and add 3.0 g/l D-xylose after\nautoclaving from anoxic stock solutions prepared
    under 100% N2 gas and sterilized by\nfiltration.\nFor DSM 29926: Supplement medium
    with 6.0 g/l D-glucose added to the medium after\nautoclaving from a sterile anoxic
    stock solution prepared under 100% N2 gas.","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/DEFLUVIITOGA_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml":null,"data/normalized_yaml/bacterial/defluviitoga_medium.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: 'All current asserted CHEBI objects and exact MIM rows are independently
    joined. Label agreement does not verify supplied forms: sodium resazurin and nickel
    hexahydrate conflict with their current IDs. CHEBI:26833 includes elemental-sulfur
    synonyms but denotes an atom; preserve powdered elemental material and resolve
    granularity without assuming a specific allotrope. Coverage metrics are ingredient-instance
    linkage, not scientific accuracy.'
  target_ids:
  - CultureMech:004084
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: Read both complete October source reviews and three complete October diagnostic
    reports, plus the archive method and exact1328 source-duplicate row. Current API1328
    raw digest equals historical 74e28cbd17599eb0cae7f51c98018eb6013a1e51e7d6a781f108a286aa37c1eb;
    current catalog raw equals historical d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.
    This authenticates equal content now, not recovery of the old access event. Historical
    unsupported/conflict decisions were unchanged, and no attached owner amount claims
    are present. Current conservative merger and stock-preserving importer improvements
    are credited; the old generated omission is not a current ingredient-only merger
    claim.
  target_ids:
  - CultureMech:004084
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-004084-stock-stage
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore main-versus-SL-10 structure and resazurin stock identity
  description: Restore nine SL-10 stock components to their separate stock stage and
    record the receiving dose. Preserve the explicit sodium-resazurin stock dose and
    w/v label. HCl 25% remains basis-ambiguous; do not treat provider 2.5 g/L as verified
    mass or infer final-medium rates from input water.
  target_ids:
  - CultureMech:004084
  field_paths:
  - ingredients[8].concentration
  - ingredients[15].concentration
  - ingredients[16].concentration
  - ingredients[17].concentration
  - ingredients[18].concentration
  - ingredients[19].concentration
  - ingredients[20].concentration
  - ingredients[21].concentration
  - ingredients[22].concentration
  - ingredients[23].concentration
  - solutions
  evidence_ids:
  - dsm1328
  - api1328
  - quantities
  - writer-mediadive
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/defluviitoga_medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-004084-anoxic-preparation
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile aerobic metadata and retain preparation without unsafe merging
  description: 'The target and KOMODO owner say Aerobic: Yes, conflicting with the
    base primary anoxic preparation. The maintained DSM owner retains the supported
    base-method and SL-10 makeup text, whereas the generated target drops both. Its
    SL-10 instruction is an unqualified main preparation step without a stock container;
    preserve the wording and numeric makeup while explicitly placing it in the SL-10
    stock scope. Qualify the imported catalog boolean and keep printed strain overrides
    separate. Current merger rejects these unequal notes/preparation; reconcile maintained
    source identities before regenerating rather than forcing a duplicate merge.'
  target_ids:
  - CultureMech:004084
  field_paths:
  - notes
  - preparation_steps
  - parent_media
  - variant_relationship
  evidence_ids:
  - dsm1328
  - api1328
  - komodoList
  - owner-2
  - writer-formulation
  - writer-merger
  rule_id: review-yaml-record/representation
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/defluviitoga_medium.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-004084-supplied-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Correct sodium-resazurin and nickel-hydrate identifiers
  description: The source explicitly supplies sodium resazurin, but CHEBI:8806 denotes
    neutral C12H7NO4. Nickel chloride hexahydrate is asserted as anhydrous CHEBI:34887
    in both primary and secondary slots; freshly inspected CHEBI:53542 denotes the
    hexahydrate. Correct exact supplied-form links after curation review without rescaling
    source masses. Sulfur-atom versus elemental-powder granularity remains an explicitly
    bounded ontology concern, not a fabricated allotrope assertion.
  target_ids:
  - CultureMech:004084
  field_paths:
  - ingredients[8].term
  - ingredients[22].term
  - ingredients[22].mediaingredientmech_chebi_term
  evidence_ids:
  - dsm1328
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
    path: data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/defluviitoga_medium.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-004084-claim-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Attach scoped claims and correct future timestamp formatting
  description: No selected concentration has an attached exact amount claim despite
    two historical source reviews. Preserve those unchanged historical decisions and
    dates, attach new scoped evidence to reconciled maintained assertions, and retain
    the malformed historical .fZ timestamp as history. Fix the current KOMODO writer
    time.strftime %f formatting for future events; do not rewrite the historical event.
  target_ids:
  - CultureMech:004084
  field_paths:
  - evidence
  - references
  - curation_history
  evidence_ids:
  - old-reports
  - old-claims
  - writer-komodo
  rule_id: review-yaml-record/provenance
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/defluviitoga_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: maintained timestamp writer
actions:
- action_id: a1
  description: Restore nine SL-10 stock components to their separate stock stage and
    record the receiving dose. Preserve the explicit sodium-resazurin stock dose and
    w/v label. HCl 25% remains basis-ambiguous; do not treat provider 2.5 g/L as verified
    mass or infer final-medium rates from input water.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:004084
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/defluviitoga_medium.yaml
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
  description: 'The target and KOMODO owner say Aerobic: Yes, conflicting with the
    base primary anoxic preparation. The maintained DSM owner retains the supported
    base-method and SL-10 makeup text, whereas the generated target drops both. Its
    SL-10 instruction is an unqualified main preparation step without a stock container;
    preserve the wording and numeric makeup while explicitly placing it in the SL-10
    stock scope. Qualify the imported catalog boolean and keep printed strain overrides
    separate. Current merger rejects these unequal notes/preparation; reconcile maintained
    source identities before regenerating rather than forcing a duplicate merge.'
  finding_ids:
  - f2
  target_ids:
  - CultureMech:004084
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/defluviitoga_medium.yaml
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
  description: The source explicitly supplies sodium resazurin, but CHEBI:8806 denotes
    neutral C12H7NO4. Nickel chloride hexahydrate is asserted as anhydrous CHEBI:34887
    in both primary and secondary slots; freshly inspected CHEBI:53542 denotes the
    hexahydrate. Correct exact supplied-form links after curation review without rescaling
    source masses. Sulfur-atom versus elemental-powder granularity remains an explicitly
    bounded ontology concern, not a fabricated allotrope assertion.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:004084
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/defluviitoga_medium.yaml
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
  description: No selected concentration has an attached exact amount claim despite
    two historical source reviews. Preserve those unchanged historical decisions and
    dates, attach new scoped evidence to reconciled maintained assertions, and retain
    the malformed historical .fZ timestamp as history. Fix the current KOMODO writer
    time.strftime %f formatting for future events; do not rewrite the historical event.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:004084
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/defluviitoga_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: maintained timestamp writer
  acceptance_checks:
  - New claim evidence is field- and stage-specific, prior history remains byte-preserved,
    and a new event records actual curation.
  - The future KOMODO converter emits a valid UTC timestamp using a supported datetime
    formatter; do not backdate or replace the old .fZ event.
  generator: Maintained-input curation and repository merge regeneration
limitations:
- Direct KOMODO1328 detail is unavailable (403); current catalog identity and DSM
  primary do not independently recover its full detail page.
- The source-duplicate archive is reviewed only for its method and selected1328 row;
  other hundreds of pairs are outside scope.
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
