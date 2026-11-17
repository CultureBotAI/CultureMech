# Scientific review: DEFERRIBACTER AUTOTROPHICUS MEDIUM

- Review: 20261028T162846Z-culturemech-002167-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T16:11:57.446477Z
- Finished UTC: 2026-10-28T16:28:46.234303Z
- Reviewer: Codex batch006_validation (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The selected record needs source-identity reconciliation, stock-stage restoration and supplied-form correction. Fresh KOMODO 985 disagrees with DSM 985, while 985.1 remains unavailable. Preserve supported DSM basal provider rates and the existing preparation text, separate all stock quantities and doses, retain exact variant uncertainty, and attach claim-level evidence before regeneration. Four original canonical checks passed; these shape checks do not certify formulation equivalence.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch072 index 01
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002167 | data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml | generated | deferribacter_autotrophicus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:002167 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:002167 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:002167 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:002167 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Distinct source identities and current catalogue check

identity: concern. Targets: CultureMech:002167.

DSM985, KOMODO985 and KOMODO985.1 are not interchangeable merely because copied local ingredient signatures match. Fresh KOMODO985 shows a distinct formula, and exact985.1 remains inaccessible. DSM19306 is currently Clostridium tepidiprofundi; this is identity context only.

### Record type and category

scope: supported. Targets: CultureMech:002167.

Bacterial liquid complex/semi-defined representation is consistent with the selected DSM source and yeast-extract component. No target-organism growth or optimal condition is inferred from the name.

### Existing support and newly captured sources

evidence: concern. Targets: CultureMech:002167.

The source PDFs, exact provider objects and current KOMODO page are kept separately; the complete stored recipe has no attached claims. Numeric agreement with a provider stock does not verify main-medium placement.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:002167.

140 current concentration fields are covered by 80 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b072-quantity-inventory-v1","target":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","quantity_field_count":140,"decisions":[{"quantity_id":"q1","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"17.9462","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"17.9462","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[0].concentration","stored":{"value":"17.9462","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"17.9462","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The stored 17.9462 G_PER_L equals the explicit current DSMZ provider g_l for NaCl in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985 Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 3-3","quote":"NaCl                                                      18.00        g","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 18,\n                        \"unit\": \"g\",\n                        \"g_l\": 17.9462,\n                        \"mmol_l\": 307.087,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 17.9462 G_PER_L equals the explicit current DSMZ provider g_l for NaCl in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 17.9462 G_PER_L equals the explicit current DSMZ provider g_l for NaCl in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"The exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[0].concentration","decision":"conflict","rationale":"The current exact KOMODO985 table uses a distinct formulation and different declared rates or forms. The local copied DSM985 value is not endorsed as equivalent merely because some rounded numbers resemble it."}]},{"quantity_id":"q2","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.98804","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.98804","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.98804","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.98804","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The stored 3.98804 G_PER_L equals the explicit current DSMZ provider g_l for MgCl2 x 6 H2O in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985 Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 4-4","quote":"MgCl2 x 6 H2O                                              4.00        g","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.98804,\n                        \"mmol_l\": 19.6162,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 3.98804 G_PER_L equals the explicit current DSMZ provider g_l for MgCl2 x 6 H2O in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 3.98804 G_PER_L equals the explicit current DSMZ provider g_l for MgCl2 x 6 H2O in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[1].concentration","decision":"conflict","rationale":"The current exact KOMODO985 table uses a distinct formulation and different declared rates or forms. The local copied DSM985 value is not endorsed as equivalent merely because some rounded numbers resemble it."}]},{"quantity_id":"q3","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.338983","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.338983","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.338983","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.338983","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The stored 0.338983 G_PER_L equals the explicit current DSMZ provider g_l for KCl in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985 Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 5-5","quote":"KCl                                                        0.34        g","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.34,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.338983,\n                        \"mmol_l\": 4.54706,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 0.338983 G_PER_L equals the explicit current DSMZ provider g_l for KCl in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 0.338983 G_PER_L equals the explicit current DSMZ provider g_l for KCl in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[2].concentration","decision":"conflict","rationale":"The current exact KOMODO985 table uses a distinct formulation and different declared rates or forms. The local copied DSM985 value is not endorsed as equivalent merely because some rounded numbers resemble it."}]},{"quantity_id":"q4","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.249252","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.249252","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.249252","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.249252","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The stored 0.249252 G_PER_L equals the explicit current DSMZ provider g_l for NH4Cl in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985 Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 6-6","quote":"NH4Cl                                                      0.25        g","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.249252,\n                        \"mmol_l\": 4.65979,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 0.249252 G_PER_L equals the explicit current DSMZ provider g_l for NH4Cl in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 0.249252 G_PER_L equals the explicit current DSMZ provider g_l for NH4Cl in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[3].concentration","decision":"conflict","rationale":"The current exact KOMODO985 table uses a distinct formulation and different declared rates or forms. The local copied DSM985 value is not endorsed as equivalent merely because some rounded numbers resemble it."}]},{"quantity_id":"q5","label":"CaCl2","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.109671","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.109671","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.109671","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.109671","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The stored 0.109671 G_PER_L equals the explicit current DSMZ provider g_l for CaCl2 in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985 Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 7-7","quote":"CaCl2                                                      0.11        g","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2\",\n                        \"compound_id\": 81,\n                        \"amount\": 0.11,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.109671,\n                        \"mmol_l\": 0.988205,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 0.109671 G_PER_L equals the explicit current DSMZ provider g_l for CaCl2 in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 0.109671 G_PER_L equals the explicit current DSMZ provider g_l for CaCl2 in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[4].concentration","decision":"conflict","rationale":"The current exact KOMODO985 table uses a distinct formulation and different declared rates or forms. The local copied DSM985 value is not endorsed as equivalent merely because some rounded numbers resemble it."}]},{"quantity_id":"q6","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.179462","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.179462","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.179462","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.179462","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The stored 0.179462 G_PER_L equals the explicit current DSMZ provider g_l for K2HPO4 in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985 Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 8-8","quote":"K2HPO4                                                     0.18        g","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.179462,\n                        \"mmol_l\": 1.03035,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 0.179462 G_PER_L equals the explicit current DSMZ provider g_l for K2HPO4 in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 0.179462 G_PER_L equals the explicit current DSMZ provider g_l for K2HPO4 in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[5].concentration","decision":"conflict","rationale":"The current exact KOMODO985 table uses a distinct formulation and different declared rates or forms. The local copied DSM985 value is not endorsed as equivalent merely because some rounded numbers resemble it."}]},{"quantity_id":"q7","label":"Fe(NH4)2(SO4)2 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.0199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.0199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.0199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.0199402","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The stored 0.0199402 G_PER_L equals the explicit current DSMZ provider g_l for Fe(NH4)2(SO4)2 x 7 H2O in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985 Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 9-9","quote":"Fe(NH4)2(SO4)2 x 7 H2O                                    20.00       mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Fe(NH4)2(SO4)2 x 7 H2O\",\n                        \"compound_id\": 456,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0199402,\n                        \"mmol_l\": 0.0486161,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 0.0199402 G_PER_L equals the explicit current DSMZ provider g_l for Fe(NH4)2(SO4)2 x 7 H2O in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 0.0199402 G_PER_L equals the explicit current DSMZ provider g_l for Fe(NH4)2(SO4)2 x 7 H2O in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[6].concentration","decision":"conflict","rationale":"The current exact KOMODO985 table uses a distinct formulation and different declared rates or forms. The local copied DSM985 value is not endorsed as equivalent merely because some rounded numbers resemble it."}]},{"quantity_id":"q8","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.199402","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The stored 0.199402 G_PER_L equals the explicit current DSMZ provider g_l for Yeast extract in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985 Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 12-12","quote":"Yeast extract                                              0.20        g","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.199402,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 0.199402 G_PER_L equals the explicit current DSMZ provider g_l for Yeast extract in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 0.199402 G_PER_L equals the explicit current DSMZ provider g_l for Yeast extract in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[7].concentration","decision":"conflict","rationale":"The current exact KOMODO985 table uses a distinct formulation and different declared rates or forms. The local copied DSM985 value is not endorsed as equivalent merely because some rounded numbers resemble it."}]},{"quantity_id":"q9","label":"Sodium resazurin","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The stored 0.000498504 G_PER_L equals the explicit current DSMZ provider g_l for Sodium resazurin in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation. The primary specifies a 0.1% w/v sodium-resazurin stock and 0.50 ml addition; preserve both and review the neutral primary ID separately.","source_stage":"DSMZ985 Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 13-13","quote":"Sodium resazurin (0.1% w/v)                                0.50       ml","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 0.000498504 G_PER_L equals the explicit current DSMZ provider g_l for Sodium resazurin in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation. The primary specifies a 0.1% w/v sodium-resazurin stock and 0.50 ml addition; preserve both and review the neutral primary ID separately."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 0.000498504 G_PER_L equals the explicit current DSMZ provider g_l for Sodium resazurin in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation. The primary specifies a 0.1% w/v sodium-resazurin stock and 0.50 ml addition; preserve both and review the neutral primary ID separately."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[8].concentration","decision":"conflict","rationale":"The current exact KOMODO985 table uses a distinct formulation and different declared rates or forms. The local copied DSM985 value is not endorsed as equivalent merely because some rounded numbers resemble it."}]},{"quantity_id":"q10","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1.49551","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1.49551","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1.49551","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1.49551","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The stored 1.49551 G_PER_L equals the explicit current DSMZ provider g_l for Na2CO3 in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985 Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 14-14","quote":"Na2CO3                                                     1.50        g","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.49551,\n                        \"mmol_l\": 14.1102,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 1.49551 G_PER_L equals the explicit current DSMZ provider g_l for Na2CO3 in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 1.49551 G_PER_L equals the explicit current DSMZ provider g_l for Na2CO3 in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[9].concentration","decision":"conflict","rationale":"The current exact KOMODO985 table uses a distinct formulation and different declared rates or forms. The local copied DSM985 value is not endorsed as equivalent merely because some rounded numbers resemble it."}]},{"quantity_id":"q11","label":"KNO3","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The stored 0.997009 G_PER_L equals the explicit current DSMZ provider g_l for KNO3 in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985 Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 15-15","quote":"KNO3                                                       1.00        g","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"KNO3\",\n                        \"compound_id\": 191,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\": 9.86132,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 0.997009 G_PER_L equals the explicit current DSMZ provider g_l for KNO3 in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 0.997009 G_PER_L equals the explicit current DSMZ provider g_l for KNO3 in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[10].concentration","decision":"conflict","rationale":"The current exact KOMODO985 table uses a distinct formulation and different declared rates or forms. The local copied DSM985 value is not endorsed as equivalent merely because some rounded numbers resemble it."}]},{"quantity_id":"q12","label":"Na-acetate","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.59521","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.59521","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.59521","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.59521","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The stored 1.59521 G_PER_L equals the explicit current DSMZ provider g_l for Na-acetate in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985 Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 16-16","quote":"Na-acetate                                                 1.60        g","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\": 23,\n                        \"amount\": 1.6,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.59521,\n                        \"mmol_l\": 19.4458,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 1.59521 G_PER_L equals the explicit current DSMZ provider g_l for Na-acetate in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[11].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 1.59521 G_PER_L equals the explicit current DSMZ provider g_l for Na-acetate in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"The exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[11].concentration","decision":"conflict","rationale":"The current exact KOMODO985 table uses a distinct formulation and different declared rates or forms. The local copied DSM985 value is not endorsed as equivalent merely because some rounded numbers resemble it."}]},{"quantity_id":"q13","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The stored 0.498504 G_PER_L equals the explicit current DSMZ provider g_l for Na2S x 9 H2O in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985 Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 18-18","quote":"Na2S x 9 H2O                                               0.50        g","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[15]","quote":"{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\": 2.07553,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 0.498504 G_PER_L equals the explicit current DSMZ provider g_l for Na2S x 9 H2O in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[12].concentration","decision":"evidence_only","rationale":"Exact DSM985 provider g_l supports the unchanged basal value on its stated normalization basis; no attached claim exists and the primary final volume is unresolved. The stored 0.498504 G_PER_L equals the explicit current DSMZ provider g_l for Na2S x 9 H2O in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider volume 1003 ml is a separate normalization convention, not an explicit primary final make-up. Credit this rate only for the DSM source layer. The copied KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[12].concentration","decision":"unsupported","rationale":"The exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The current exact KOMODO985 table uses a distinct formulation and different declared rates or forms. The local copied DSM985 value is not endorsed as equivalent merely because some rounded numbers resemble it."}]},{"quantity_id":"q14","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[13].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 2.5 G_PER_L equals the explicit current DSMZ provider g_l for HCl in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. Primary 25% HCl has no stated percent basis; the provider reports 2.5 g_l, but this review does not independently derive that mass from the bare percentage.","source_stage":"DSMZ985 Trace element solution SL-10; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 33-33","quote":"HCl (25%)                                                  10.00      ml","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The stored 2.5 G_PER_L equals the explicit current DSMZ provider g_l for HCl in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. Primary 25% HCl has no stated percent basis; the provider reports 2.5 g_l, but this review does not independently derive that mass from the bare percentage."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The stored 2.5 G_PER_L equals the explicit current DSMZ provider g_l for HCl in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. Primary 25% HCl has no stated percent basis; the provider reports 2.5 g_l, but this review does not independently derive that mass from the bare percentage."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The stored 2.5 G_PER_L equals the explicit current DSMZ provider g_l for HCl in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. Primary 25% HCl has no stated percent basis; the provider reports 2.5 g_l, but this review does not independently derive that mass from the bare percentage."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The stored 2.5 G_PER_L equals the explicit current DSMZ provider g_l for HCl in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. Primary 25% HCl has no stated percent basis; the provider reports 2.5 g_l, but this review does not independently derive that mass from the bare percentage."}]},{"quantity_id":"q15","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[14].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 1.5 G_PER_L equals the explicit current DSMZ provider g_l for FeCl2 x 4 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution.","source_stage":"DSMZ985 Trace element solution SL-10; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 34-34","quote":"FeCl2 x 4 H2O                                               1.50       g","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The stored 1.5 G_PER_L equals the explicit current DSMZ provider g_l for FeCl2 x 4 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The stored 1.5 G_PER_L equals the explicit current DSMZ provider g_l for FeCl2 x 4 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The stored 1.5 G_PER_L equals the explicit current DSMZ provider g_l for FeCl2 x 4 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The stored 1.5 G_PER_L equals the explicit current DSMZ provider g_l for FeCl2 x 4 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."}]},{"quantity_id":"q16","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.07 G_PER_L equals the explicit current DSMZ provider g_l for ZnCl2 in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution.","source_stage":"DSMZ985 Trace element solution SL-10; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 35-35","quote":"ZnCl2                                                      70.00      mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The stored 0.07 G_PER_L equals the explicit current DSMZ provider g_l for ZnCl2 in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The stored 0.07 G_PER_L equals the explicit current DSMZ provider g_l for ZnCl2 in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The stored 0.07 G_PER_L equals the explicit current DSMZ provider g_l for ZnCl2 in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The stored 0.07 G_PER_L equals the explicit current DSMZ provider g_l for ZnCl2 in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."}]},{"quantity_id":"q17","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for MnCl2 x 4 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution.","source_stage":"DSMZ985 Trace element solution SL-10; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 36-36","quote":"MnCl2 x 4 H2O                                             100.00      mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for MnCl2 x 4 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for MnCl2 x 4 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for MnCl2 x 4 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for MnCl2 x 4 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."}]},{"quantity_id":"q18","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.006 G_PER_L equals the explicit current DSMZ provider g_l for H3BO3 in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution.","source_stage":"DSMZ985 Trace element solution SL-10; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 37-37","quote":"H3BO3                                                       6.00      mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The stored 0.006 G_PER_L equals the explicit current DSMZ provider g_l for H3BO3 in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The stored 0.006 G_PER_L equals the explicit current DSMZ provider g_l for H3BO3 in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The stored 0.006 G_PER_L equals the explicit current DSMZ provider g_l for H3BO3 in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The stored 0.006 G_PER_L equals the explicit current DSMZ provider g_l for H3BO3 in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."}]},{"quantity_id":"q19","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.19 G_PER_L equals the explicit current DSMZ provider g_l for CoCl2 x 6 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution.","source_stage":"DSMZ985 Trace element solution SL-10; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 38-38","quote":"CoCl2 x 6 H2O                                             190.00      mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The stored 0.19 G_PER_L equals the explicit current DSMZ provider g_l for CoCl2 x 6 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The stored 0.19 G_PER_L equals the explicit current DSMZ provider g_l for CoCl2 x 6 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The stored 0.19 G_PER_L equals the explicit current DSMZ provider g_l for CoCl2 x 6 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The stored 0.19 G_PER_L equals the explicit current DSMZ provider g_l for CoCl2 x 6 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."}]},{"quantity_id":"q20","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.002 G_PER_L equals the explicit current DSMZ provider g_l for CuCl2 x 2 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution.","source_stage":"DSMZ985 Trace element solution SL-10; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 39-39","quote":"CuCl2 x 2 H2O                                               2.00      mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The stored 0.002 G_PER_L equals the explicit current DSMZ provider g_l for CuCl2 x 2 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The stored 0.002 G_PER_L equals the explicit current DSMZ provider g_l for CuCl2 x 2 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The stored 0.002 G_PER_L equals the explicit current DSMZ provider g_l for CuCl2 x 2 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The stored 0.002 G_PER_L equals the explicit current DSMZ provider g_l for CuCl2 x 2 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."}]},{"quantity_id":"q21","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.024 G_PER_L equals the explicit current DSMZ provider g_l for NiCl2 x 6 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. The supplied nickel hexahydrate is not the anhydrous CHEBI:34887 assertion; amount and grounding decisions are separate.","source_stage":"DSMZ985 Trace element solution SL-10; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 40-40","quote":"NiCl2 x 6 H2O                                              24.00      mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The stored 0.024 G_PER_L equals the explicit current DSMZ provider g_l for NiCl2 x 6 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. The supplied nickel hexahydrate is not the anhydrous CHEBI:34887 assertion; amount and grounding decisions are separate."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The stored 0.024 G_PER_L equals the explicit current DSMZ provider g_l for NiCl2 x 6 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. The supplied nickel hexahydrate is not the anhydrous CHEBI:34887 assertion; amount and grounding decisions are separate."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The stored 0.024 G_PER_L equals the explicit current DSMZ provider g_l for NiCl2 x 6 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. The supplied nickel hexahydrate is not the anhydrous CHEBI:34887 assertion; amount and grounding decisions are separate."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The stored 0.024 G_PER_L equals the explicit current DSMZ provider g_l for NiCl2 x 6 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. The supplied nickel hexahydrate is not the anhydrous CHEBI:34887 assertion; amount and grounding decisions are separate."}]},{"quantity_id":"q22","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.036 G_PER_L equals the explicit current DSMZ provider g_l for Na2MoO4 x 2 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution.","source_stage":"DSMZ985 Trace element solution SL-10; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 41-41","quote":"Na2MoO4 x 2 H2O                                            36.00      mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The stored 0.036 G_PER_L equals the explicit current DSMZ provider g_l for Na2MoO4 x 2 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The stored 0.036 G_PER_L equals the explicit current DSMZ provider g_l for Na2MoO4 x 2 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The stored 0.036 G_PER_L equals the explicit current DSMZ provider g_l for Na2MoO4 x 2 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The stored 0.036 G_PER_L equals the explicit current DSMZ provider g_l for Na2MoO4 x 2 H2O in Trace element solution SL-10. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."}]},{"quantity_id":"q23","label":"NaOH","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.5 G_PER_L equals the explicit current DSMZ provider g_l for NaOH in Selenite-tungstate solution. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution.","source_stage":"DSMZ985 Selenite-tungstate solution; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 57-57","quote":"NaOH                                        0.50    g","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The stored 0.5 G_PER_L equals the explicit current DSMZ provider g_l for NaOH in Selenite-tungstate solution. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The stored 0.5 G_PER_L equals the explicit current DSMZ provider g_l for NaOH in Selenite-tungstate solution. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The stored 0.5 G_PER_L equals the explicit current DSMZ provider g_l for NaOH in Selenite-tungstate solution. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The stored 0.5 G_PER_L equals the explicit current DSMZ provider g_l for NaOH in Selenite-tungstate solution. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."}]},{"quantity_id":"q24","label":"Na2SeO3 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.003","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.003 G_PER_L equals the explicit current DSMZ provider g_l for Na2SeO3 x 5 H2O in Selenite-tungstate solution. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution.","source_stage":"DSMZ985 Selenite-tungstate solution; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 58-58","quote":"Na2SeO3 x 5 H2O                             3.00   mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The stored 0.003 G_PER_L equals the explicit current DSMZ provider g_l for Na2SeO3 x 5 H2O in Selenite-tungstate solution. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The stored 0.003 G_PER_L equals the explicit current DSMZ provider g_l for Na2SeO3 x 5 H2O in Selenite-tungstate solution. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The stored 0.003 G_PER_L equals the explicit current DSMZ provider g_l for Na2SeO3 x 5 H2O in Selenite-tungstate solution. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The stored 0.003 G_PER_L equals the explicit current DSMZ provider g_l for Na2SeO3 x 5 H2O in Selenite-tungstate solution. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."}]},{"quantity_id":"q25","label":"Na2WO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.004 G_PER_L equals the explicit current DSMZ provider g_l for Na2WO4 x 2 H2O in Selenite-tungstate solution. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution.","source_stage":"DSMZ985 Selenite-tungstate solution; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 59-59","quote":"Na2WO4 x 2 H2O                              4.00   mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The stored 0.004 G_PER_L equals the explicit current DSMZ provider g_l for Na2WO4 x 2 H2O in Selenite-tungstate solution. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The stored 0.004 G_PER_L equals the explicit current DSMZ provider g_l for Na2WO4 x 2 H2O in Selenite-tungstate solution. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The stored 0.004 G_PER_L equals the explicit current DSMZ provider g_l for Na2WO4 x 2 H2O in Selenite-tungstate solution. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The stored 0.004 G_PER_L equals the explicit current DSMZ provider g_l for Na2WO4 x 2 H2O in Selenite-tungstate solution. This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."}]},{"quantity_id":"q26","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Biotin in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution.","source_stage":"DSMZ985 Wolin's vitamin solution (10x); KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 64-64","quote":"Biotin                                     20.00   mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Biotin in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Biotin in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Biotin in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Biotin in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."}]},{"quantity_id":"q27","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Folic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution.","source_stage":"DSMZ985 Wolin's vitamin solution (10x); KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 65-65","quote":"Folic acid                                 20.00   mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Folic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Folic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Folic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Folic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."}]},{"quantity_id":"q28","label":"Pyridoxine hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for Pyridoxine hydrochloride in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution.","source_stage":"DSMZ985 Wolin's vitamin solution (10x); KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 66-66","quote":"Pyridoxine hydrochloride                  100.00   mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for Pyridoxine hydrochloride in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for Pyridoxine hydrochloride in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for Pyridoxine hydrochloride in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for Pyridoxine hydrochloride in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."}]},{"quantity_id":"q29","label":"Thiamine HCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Thiamine HCl in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution.","source_stage":"DSMZ985 Wolin's vitamin solution (10x); KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 67-67","quote":"Thiamine HCl                               50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Thiamine HCl in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Thiamine HCl in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Thiamine HCl in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Thiamine HCl in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."}]},{"quantity_id":"q30","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Riboflavin in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution.","source_stage":"DSMZ985 Wolin's vitamin solution (10x); KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 68-68","quote":"Riboflavin                                 50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Riboflavin in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Riboflavin in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Riboflavin in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Riboflavin in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."}]},{"quantity_id":"q31","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Nicotinic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution.","source_stage":"DSMZ985 Wolin's vitamin solution (10x); KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 69-69","quote":"Nicotinic acid                             50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Nicotinic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Nicotinic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Nicotinic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Nicotinic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."}]},{"quantity_id":"q32","label":"Calcium D-(+)-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Calcium D-(+)-pantothenate in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. The primary explicitly supplies the D-calcium salt, consistent with the current stereochemical CHEBI:31345 object; no hemicalcium or full-salt mass conversion is proposed.","source_stage":"DSMZ985 Wolin's vitamin solution (10x); KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 70-70","quote":"Calcium D-(+)-pantothenate                 50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Calcium D-(+)-pantothenate in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. The primary explicitly supplies the D-calcium salt, consistent with the current stereochemical CHEBI:31345 object; no hemicalcium or full-salt mass conversion is proposed."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Calcium D-(+)-pantothenate in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. The primary explicitly supplies the D-calcium salt, consistent with the current stereochemical CHEBI:31345 object; no hemicalcium or full-salt mass conversion is proposed."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Calcium D-(+)-pantothenate in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. The primary explicitly supplies the D-calcium salt, consistent with the current stereochemical CHEBI:31345 object; no hemicalcium or full-salt mass conversion is proposed."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Calcium D-(+)-pantothenate in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. The primary explicitly supplies the D-calcium salt, consistent with the current stereochemical CHEBI:31345 object; no hemicalcium or full-salt mass conversion is proposed."}]},{"quantity_id":"q33","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.001","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.001 G_PER_L equals the explicit current DSMZ provider g_l for Vitamin B12 in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution.","source_stage":"DSMZ985 Wolin's vitamin solution (10x); KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 71-71","quote":"Vitamin B12                                 1.00   mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The stored 0.001 G_PER_L equals the explicit current DSMZ provider g_l for Vitamin B12 in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The stored 0.001 G_PER_L equals the explicit current DSMZ provider g_l for Vitamin B12 in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The stored 0.001 G_PER_L equals the explicit current DSMZ provider g_l for Vitamin B12 in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The stored 0.001 G_PER_L equals the explicit current DSMZ provider g_l for Vitamin B12 in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."}]},{"quantity_id":"q34","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for p-Aminobenzoic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution.","source_stage":"DSMZ985 Wolin's vitamin solution (10x); KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 72-72","quote":"p-Aminobenzoic acid                        50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for p-Aminobenzoic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for p-Aminobenzoic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for p-Aminobenzoic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for p-Aminobenzoic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution."}]},{"quantity_id":"q35","label":"(DL)-alpha-Lipoic acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[34].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[34].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[34].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[34].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for (DL)-alpha-Lipoic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. Generic non-stereospecific CHEBI:16494 does not contradict the explicit DL designation.","source_stage":"DSMZ985 Wolin's vitamin solution (10x); KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 73-73","quote":"(DL)-alpha-Lipoic acid                     50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[34].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for (DL)-alpha-Lipoic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. Generic non-stereospecific CHEBI:16494 does not contradict the explicit DL designation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[34].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for (DL)-alpha-Lipoic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. Generic non-stereospecific CHEBI:16494 does not contradict the explicit DL designation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[34].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for (DL)-alpha-Lipoic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. Generic non-stereospecific CHEBI:16494 does not contradict the explicit DL designation."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[34].concentration","decision":"conflict","rationale":"The stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for (DL)-alpha-Lipoic acid in Wolin's vitamin solution (10x). This is stock strength flattened into main ingredients; numerical agreement with a stock does not make it a final-medium concentration. Keep stock composition and the separate receiving addition, without inventing a final-medium dilution. Generic non-stereospecific CHEBI:16494 does not contradict the explicit DL designation."}]},{"quantity_id":"q36","label":"Trace element solution SL-10 receiving addition","local_fields":[],"decision":"evidence_only","rationale":"The exact primary supplies this 1 ml stock addition; it is absent as a structured receiving stock. Preserve its separate identity and batch dose. Neither the printed input water nor the provider volume establishes measured final volume.","source_stage":"DSM985 receiving batch only","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 10-10","quote":"Trace element solution SL-10                               1.00       ml","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q37","label":"Selenite-tungstate solution receiving addition","local_fields":[],"decision":"evidence_only","rationale":"The exact primary supplies this 1 ml stock addition; it is absent as a structured receiving stock. Preserve its separate identity and batch dose. Neither the printed input water nor the provider volume establishes measured final volume.","source_stage":"DSM985 receiving batch only","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 11-11","quote":"Selenite-tungstate solution                                1.00       ml","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q38","label":"Wolin's vitamin solution (10x) receiving addition","local_fields":[],"decision":"evidence_only","rationale":"The exact primary supplies this 1 ml stock addition; it is absent as a structured receiving stock. Preserve its separate identity and batch dose. Neither the printed input water nor the provider volume establishes measured final volume.","source_stage":"DSM985 receiving batch only","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 17-17","quote":"Wolin's vitamin solution (10x)                             1.00       ml","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\": 15,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q39","label":"Main sol. 985 water","local_fields":[],"decision":"evidence_only","rationale":"Retain this exact solvent input separately. SL-10 alone has an explicit final make-up instruction, assessed in the stock-preparation row; the other printed water inputs are not independent final-volume measurements.","source_stage":"Main sol. 985","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 19-19","quote":"Distilled water                                         1000.00       ml","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[16]","quote":"{\n                        \"recipe_order\": 17,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q40","label":"Trace element solution SL-10 water","local_fields":[],"decision":"evidence_only","rationale":"Retain this exact solvent input separately. SL-10 alone has an explicit final make-up instruction, assessed in the stock-preparation row; the other printed water inputs are not independent final-volume measurements.","source_stage":"Trace element solution SL-10","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 42-42","quote":"Distilled water                                           990.00      ml","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q41","label":"Selenite-tungstate solution water","local_fields":[],"decision":"evidence_only","rationale":"Retain this exact solvent input separately. SL-10 alone has an explicit final make-up instruction, assessed in the stock-preparation row; the other printed water inputs are not independent final-volume measurements.","source_stage":"Selenite-tungstate solution","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 60-60","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q42","label":"Wolin's vitamin solution (10x) water","local_fields":[],"decision":"evidence_only","rationale":"Retain this exact solvent input separately. SL-10 alone has an explicit final make-up instruction, assessed in the stock-preparation row; the other printed water inputs are not independent final-volume measurements.","source_stage":"Wolin's vitamin solution (10x)","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 74-74","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q43","label":"DSM basal preparation and numeric controls","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve ingredients (except carbonate, nitrate, acetate, vitamins and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add vitamins (sterilized by filtration), nitrate, acetate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. The pH of the complete medium should be 6.5 -7.0."}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve ingredients (except carbonate, nitrate, acetate, vitamins and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add vitamins (sterilized by filtration), nitrate, acetate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. The pH of the complete medium should be 6.5 -7.0."}}],"decision":"evidence_only","rationale":"The existing full paragraph correctly retains the primary exclusions, 80/20 gas mixture, 30–45 min sparging, later 100% nitrogen stock context, filtration and pH 6.5–7.0. AUTOCLAVE labels the whole multi-action paragraph, so structure should separate actions while preserving the supported text. No autoclave temperature/time or missing late-stock strength/addition volume is supplied. Do not transfer these conditions to an unresolved KOMODO variant.","source_stage":"DSM985 only; main and later-stock stages distinguished","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 21-27","quote":"Dissolve ingredients (except carbonate, nitrate, acetate, vitamins and sulfide), then sparge\nmedium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense\nmedium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and\nautoclave. Add vitamins (sterilized by filtration), nitrate, acetate and sulfide from sterile\nanoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile anoxic\nstock solution prepared under 80% N2 and 20% CO2 gas atmosphere. The pH of the\ncomplete medium should be 6.5 -7.0.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The existing full paragraph correctly retains the primary exclusions, 80/20 gas mixture, 30–45 min sparging, later 100% nitrogen stock context, filtration and pH 6.5–7.0. AUTOCLAVE labels the whole multi-action paragraph, so structure should separate actions while preserving the supported text. No autoclave temperature/time or missing late-stock strength/addition volume is supplied. Do not transfer these conditions to an unresolved KOMODO variant."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The existing full paragraph correctly retains the primary exclusions, 80/20 gas mixture, 30–45 min sparging, later 100% nitrogen stock context, filtration and pH 6.5–7.0. AUTOCLAVE labels the whole multi-action paragraph, so structure should separate actions while preserving the supported text. No autoclave temperature/time or missing late-stock strength/addition volume is supplied. Do not transfer these conditions to an unresolved KOMODO variant."}]},{"quantity_id":"q44","label":"SL-10 final make-up and stock-local preparation","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}}],"decision":"conflict","rationale":"The retained wording is exactly supported for SL-10: dissolve iron in HCl first and finally make up to 1000 ml. It is misplaced as an unqualified main-medium step; this final volume must stay within the SL-10 stock. The primary 990 ml water input and 10 ml acid input remain separate.","source_stage":"SL-10 stock only","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 32-45","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                                  10.00      ml\n   FeCl2 x 4 H2O                                               1.50       g\n   ZnCl2                                                      70.00      mg\n   MnCl2 x 4 H2O                                             100.00      mg\n   H3BO3                                                       6.00      mg\n   CoCl2 x 6 H2O                                             190.00      mg\n   CuCl2 x 2 H2O                                               2.00      mg\n   NiCl2 x 6 H2O                                              24.00      mg\n   Na2MoO4 x 2 H2O                                            36.00      mg\n   Distilled water                                           990.00      ml\n\nFirst dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"preparation_steps[1]","decision":"conflict","rationale":"The retained wording is exactly supported for SL-10: dissolve iron in HCl first and finally make up to 1000 ml. It is misplaced as an unqualified main-medium step; this final volume must stay within the SL-10 stock. The primary 990 ml water input and 10 ml acid input remain separate."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"preparation_steps[1]","decision":"conflict","rationale":"The retained wording is exactly supported for SL-10: dissolve iron in HCl first and finally make up to 1000 ml. It is misplaced as an unqualified main-medium step; this final volume must stay within the SL-10 stock. The primary 990 ml water input and 10 ml acid input remain separate."}]},{"quantity_id":"q45","label":"pH range","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ph_range","stored":{"min":6.5,"max":7.0}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ph_range","stored":{"min":6.5,"max":7.0}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ph_range","stored":{"min":6.5,"max":7.0}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ph_range","stored":{"min":6.5,"max":7.0}}],"decision":"mixed","rationale":"DSM985 primary and current KOMODO985 both report 6.5–7.0, supporting the generated/DSM/base values independently. Exact 985.1 is unavailable, so that strain-wrapper value is not independently verified.","source_stage":"Separate DSM985 and KOMODO985 sources; not strain transfer","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt lines 26-27","quote":"stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. The pH of the\ncomplete medium should be 6.5 -7.0.","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 10-23","quote":"Medium: TEPIDIBACTER medium\nMedium features\nID:\n985\nName:\nTEPIDIBACTER medium\nPH Info:\n6.5 - 7.0\nIs Complex:\ntrue\nIs Aerobic:\ntrue\nIs SubMedium:\nfalse","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"DSM985 primary and current KOMODO985 both report 6.5–7.0, supporting the generated/DSM/base values independently. Exact 985.1 is unavailable, so that strain-wrapper value is not independently verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"DSM985 primary and current KOMODO985 both report 6.5–7.0, supporting the generated/DSM/base values independently. Exact 985.1 is unavailable, so that strain-wrapper value is not independently verified."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ph_range","decision":"unsupported","rationale":"DSM985 primary and current KOMODO985 both report 6.5–7.0, supporting the generated/DSM/base values independently. Exact 985.1 is unavailable, so that strain-wrapper value is not independently verified."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"DSM985 primary and current KOMODO985 both report 6.5–7.0, supporting the generated/DSM/base values independently. Exact 985.1 is unavailable, so that strain-wrapper value is not independently verified."}]},{"quantity_id":"q46","label":"KOMODO985 source row: NaHCO3","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 34-38","quote":"NaHCO3\nsodium bicarbonate\nSEED-cpd00242#cpd00971#cpd09249#\n4.95\n0.06","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q47","label":"KOMODO985 source row: D-Ca-pantothenate","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 39-43","quote":"D-Ca-pantothenate\nD-Ca-pantothenate\nSEED-cpd00063#cpd00644##\n4.95E-5\n1.92E-7","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q48","label":"KOMODO985 source row: Lipoic acid","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 44-48","quote":"Lipoic acid\nLipoic acid\nSEED-cpd00541###\n4.95E-5\n2.41E-7","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q49","label":"KOMODO985 source row: Na2S x 9 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 49-53","quote":"Na2S x 9 H2O\nSodium sulfide hydrate\nSEED-cpd00239#cpd00971##\n0.49\n0.00","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q50","label":"KOMODO985 source row: CO2","local_fields":[],"decision":"not_quantified","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 54-58","quote":"CO2\nCO2\nSEED-cpd00011###\nnull\nnull","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q51","label":"KOMODO985 source row: Nicotinic acid","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 59-63","quote":"Nicotinic acid\nNiacin\nSEED-cpd00218###\n4.95E-5\n4.05E-7","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q52","label":"KOMODO985 source row: Riboflavin","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 64-68","quote":"Riboflavin\nRiboflavin\nSEED-cpd00220###\n4.95E-5\n1.32E-7","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q53","label":"KOMODO985 source row: MgCl2 x 6 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 69-73","quote":"MgCl2 x 6 H2O\nMagnesium chloride\nSEED-cpd00099#cpd00254#cpd04877#\n3.96\n0.02","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q54","label":"KOMODO985 source row: K2HPO4","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 74-78","quote":"K2HPO4\ndi Potassium hydrogen phosphate\nSEED-cpd00009#cpd00205##\n0.18\n0.00","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q55","label":"KOMODO985 source row: CoCl2 x 6 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 79-83","quote":"CoCl2 x 6 H2O\nCoCl2\nSEED-cpd00099#cpd00149##\n1.87E-4\n7.88E-7","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q56","label":"KOMODO985 source row: CuCl2 x 2 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 84-88","quote":"CuCl2 x 2 H2O\nCuCl2\nSEED-cpd00058#cpd00099##\n1.97E-6\n1.17E-8","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q57","label":"KOMODO985 source row: Vitamin B12","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 89-93","quote":"Vitamin B12\nCoenzyme B12\nSEED-cpd00166###\n9.89E-7\n6.26E-10","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q58","label":"KOMODO985 source row: FeCl2 x 4 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 94-98","quote":"FeCl2 x 4 H2O\nIron chloride\nSEED-cpd00099#cpd10516##\n1.48E-3\n7.45E-6","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q59","label":"KOMODO985 source row: Fe(NH4)2(SO4)2 x 7 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 99-103","quote":"Fe(NH4)2(SO4)2 x 7 H2O\n(NH4)2Fe(SO4)2\nSEED-cpd00013#cpd00048#cpd10515#\n0.02\n0.00","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q60","label":"KOMODO985 source row: Folic acid","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 104-108","quote":"Folic acid\nFolic acid\nSEED-cpd00393###\n1.98E-5\n4.51E-8","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q61","label":"KOMODO985 source row: Thiamine-HCl x 2 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 109-113","quote":"Thiamine-HCl x 2 H2O\nThiamine-HCl\nSEED-cpd00099#cpd00305##\n4.95E-5\n1.47E-7","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q62","label":"KOMODO985 source row: HCl","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 114-118","quote":"HCl\nHCl\nSEED-cpd00099###\n6.65E-4\n1.90E-5","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q63","label":"KOMODO985 source row: ZnCl2","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 119-123","quote":"ZnCl2\nZnCl2\nSEED-cpd00034#cpd00099##\n6.91E-5\n5.12E-7","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q64","label":"KOMODO985 source row: MnCl2 x 4 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 124-128","quote":"MnCl2 x 4 H2O\nMnCl2\nSEED-cpd00030#cpd00099##\n9.87E-5\n4.99E-7","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q65","label":"KOMODO985 source row: Yeast extract","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 129-133","quote":"Yeast extract\nYeast extract\nrich-peptone#\n0.20\nnull","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q66","label":"KOMODO985 source row: Pyridoxine HCl","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 134-138","quote":"Pyridoxine HCl\nPyridoxine HCl\nSEED-cpd00099#cpd00263##\n9.89E-5\n4.85E-7","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q67","label":"KOMODO985 source row: Na2MoO4 x 2 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 139-143","quote":"Na2MoO4 x 2 H2O\nNa2MoO4\nSEED-cpd00971#cpd11145##\n3.55E-5\n1.47E-7","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q68","label":"KOMODO985 source row: KCl","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 144-148","quote":"KCl\nKCl\nSEED-cpd00099#cpd00205##\n0.34\n0.00","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q69","label":"KOMODO985 source row: CaCl2","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 149-153","quote":"CaCl2\nCalcium chloride\nSEED-cpd00063#cpd00099##\n0.11\n0.00","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q70","label":"KOMODO985 source row: Resazurin","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 154-158","quote":"Resazurin\nResazurin\nSEED-cpd08053###\n9.89E-4\n4.32E-6","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q71","label":"KOMODO985 source row: p-Aminobenzoic acid","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 159-163","quote":"p-Aminobenzoic acid\np Aminobenzoic acid (PABA)\nSEED-cpd00443###\n4.95E-5\n3.64E-7","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q72","label":"KOMODO985 source row: H2O","local_fields":[],"decision":"not_quantified","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 164-168","quote":"H2O\nH2O\nSEED-cpd00001###\nnull\nnull","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q73","label":"KOMODO985 source row: N2","local_fields":[],"decision":"not_quantified","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 169-173","quote":"N2\nN2\nSEED-cpd00528###\nnull\nnull","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q74","label":"KOMODO985 source row: Distilled water","local_fields":[],"decision":"not_quantified","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 174-178","quote":"Distilled water\nH2O\nSEED-cpd00001###\nnull\nnull","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q75","label":"KOMODO985 source row: casein","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 179-183","quote":"casein\nCasein\nSEED-cpd11656###\n9.89\n0.05","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q76","label":"KOMODO985 source row: Biotin","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 184-188","quote":"Biotin\nBiotin\nSEED-cpd00104###\n1.98E-5\n8.14E-8","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q77","label":"KOMODO985 source row: NH4Cl","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 189-193","quote":"NH4Cl\nAmmonium chloride\nSEED-cpd00013#cpd00099##\n0.25\n0.00","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q78","label":"KOMODO985 source row: NiCl2 x 6 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 194-198","quote":"NiCl2 x 6 H2O\nNiCl2\nSEED-cpd00099#cpd00244##\n2.37E-5\n9.95E-8","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q79","label":"KOMODO985 source row: H3BO3","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 199-203","quote":"H3BO3\nBoric acid\nSEED-cpd09225###\n5.92E-6\n9.55E-8","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q80","label":"KOMODO985 source row: NaCl","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985 declares the displayed gram amounts per litre. This is a source-version observation, not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form and source digits; the separate model-derived SEED aggregation and rounded molar column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their compound names. Gram &amp; Mol amounts are per Liter of medium. Trace metabolites &amp; gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt lines 204-208","quote":"NaCl\nNaCl\nSEED-cpd00099#cpd00971##\n17.80\n0.31","quote_basis":"derivative text"}],"layer_assessments":[]}],"document_scopes":{"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml":null,"data/normalized_yaml/bacterial/for_dsm_19306.yaml":null,"data/normalized_yaml/bacterial/tepidibacter_medium.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:002167.

All asserted ontology objects and exact current MIM links are inventoried. Current labels agree, but sodium-resazurin salt and nickel hexahydrate are chemically mismatched despite valid IDs. D-calcium pantothenate stereochemistry, ferrous ammonium sulfate heptahydrate and generic lipoic acid are compatible with the primary. Cobalt/nickel preferred REJECTED rows and MAPPED synonym alternatives remain explicitly distinct; no chemical-form endorsement follows from row status alone.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:002167.

All seven scoped reports and exact selected parent rows were read with the complete current histories. Current raw/decoded excerpt equality authenticates content only, not historical access events. October stock-conflict findings remain relevant; September topology repair reflects the copied local signature and is contradicted by the freshly recovered KOMODO985 formulation. Current conservative merger would retain scientific differences, and the current importer no longer flattens these stocks. Original malformed/naive events must remain append-only.

## Findings

### f1: Reconcile DSM985, KOMODO985 and the DSM19306 wrapper before merging

major / open / confirmed; issue key: culturemech-002167-source-variant-conflation.

The generated record combines three source identities and retains an obsolete SOURCE_DUPLICATE parent to the DSM19306 wrapper. September owners distinguish a base and strain wrapper, but still declare DSM985 a duplicate from a copied local signature. Fresh exact KOMODO985 is a different formula: bicarbonate and casein occur, nitrate/acetate are absent from its compound table, stock-derived rates and thiamine hydrate differ, and its aerobic flag conflicts with DSM985 anoxic preparation. Do not collapse these versions or silently replace either. DSM19306 currently identifies Clostridium tepidiprofundi; its catalogue identity does not prove this historical medium variant or growth. Preserve the original resolver/repair events and append a source-backed reconciliation. Regenerate only after owner identity and relationships are resolved.

### f2: Restore three stock scopes and their receiving doses

major / open / confirmed; issue key: culturemech-002167-stock-stage-flattening.

All four layers place 22 SL-10, selenite–tungstate and vitamin stock constituents directly among main ingredients at full stock strength. Preserve their exact stock quantities and separate receiving additions rather than endorsing them as final-medium rates. Retain the supported DSM basal provider rates with their explicit normalization basis; do not substitute a presumed one-litre denominator. Add the primary solvent inputs and sodium-resazurin stock strength/dose in their correct scopes. The current importer already separates primary compounds and stocks; current behavior does not authenticate or justify the older flattened output.

### f3: Keep the SL-10 make-up separate from main-medium preparation

major / open / confirmed; issue key: culturemech-002167-preparation-stage-scope.

The DSM owner and generated target retain useful complete source preparation text, but the SL-10 instruction to make up to 1000 ml sits at main preparation_steps[1], and the entire basal multi-action paragraph is labelled AUTOCLAVE. Place the stock instruction within its stock context and distinguish supported sequential actions without discarding the existing gas, duration, exclusion, filtration or pH controls. Missing autoclave settings and late-stock strengths/doses remain unknown. KOMODO owners lack this DSM text and have conflicting source atmosphere metadata; first resolve their variant identity rather than copying DSM conditions into them.

### f4: Correct the sodium-resazurin and nickel-hydrate assertions

major / open / confirmed; issue key: culturemech-002167-supplied-form-grounding.

Sodium resazurin is currently assigned neutral CHEBI:8806; the exact primary and API specify the sodium salt. NiCl2 x 6 H2O is assigned anhydrous CHEBI:34887 in both primary and secondary slots. Reconcile these supplied forms to exact current ontology objects and canonical labels while retaining supported stock amounts and source distinctions. The MIM sodium-resazurin synonym does not override the neutral ontology formula. The nickel preferred row is REJECTED while an exact synonym maps to 53542; neither status alone validates a replacement. Calcium D-pantothenate, ferrous ammonium sulfate heptahydrate and non-stereospecific lipoic acid are explicitly retained as compatible with their DSM source forms.

### f5: Resolve remaining bounded secondary-link gaps

minor / open / confirmed; issue key: culturemech-002167-grounding-linkage-followup.

KNO3 retains MediaIngredientMech:000170, absent from the exact packaged current snapshot, while its primary CHEBI:63043 remains correct. Yeast extract has no primary or secondary term and sodium resazurin/calcium pantothenate lack secondary links. Review current exact MIM candidates without treating snapshot absence as historical invalidity or treating synonym rows as supplied-form proof. The scientific form errors are separately tracked; these linkage gaps do not justify changing supported amounts.

### f6: Attach scoped claims and preserve malformed historical events

minor / open / confirmed; issue key: culturemech-002167-claim-history-provenance.

No retained ingredient claim authenticates these current quantities; all source support found here is newly linked review evidence. The complete seven reports contain prior conflict/unsupported decisions and derivative source excerpts, not proof of completed source curation. Both KOMODO owners retain malformed .fZ import timestamps and timezone-naive resolver timestamps. Keep original events byte-preserved; append verified context or corrections only when authoritative event provenance is recovered. September topology updates and ingredients_curated flags do not certify current external formula equality.

## Recommended Actions And Acceptance Checks

### a1

The generated record combines three source identities and retains an obsolete SOURCE_DUPLICATE parent to the DSM19306 wrapper. September owners distinguish a base and strain wrapper, but still declare DSM985 a duplicate from a copied local signature. Fresh exact KOMODO985 is a different formula: bicarbonate and casein occur, nitrate/acetate are absent from its compound table, stock-derived rates and thiamine hydrate differ, and its aerobic flag conflicts with DSM985 anoxic preparation. Do not collapse these versions or silently replace either. DSM19306 currently identifies Clostridium tepidiprofundi; its catalogue identity does not prove this historical medium variant or growth. Preserve the original resolver/repair events and append a source-backed reconciliation. Regenerate only after owner identity and relationships are resolved.

- Preserve each exact accession, source recipe and historical event; document the recovered KOMODO985 versus DSM985 differences and unresolved985.1 boundary.
- Remove unsupported duplicate/equivalence claims only through reviewed maintained-owner curation; do not infer strain growth from catalogue identity.
- Regenerate from reconciled owners and verify conservative merge compatibility and all original diagnostics.

### a2

All four layers place 22 SL-10, selenite–tungstate and vitamin stock constituents directly among main ingredients at full stock strength. Preserve their exact stock quantities and separate receiving additions rather than endorsing them as final-medium rates. Retain the supported DSM basal provider rates with their explicit normalization basis; do not substitute a presumed one-litre denominator. Add the primary solvent inputs and sodium-resazurin stock strength/dose in their correct scopes. The current importer already separates primary compounds and stocks; current behavior does not authenticate or justify the older flattened output.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The DSM owner and generated target retain useful complete source preparation text, but the SL-10 instruction to make up to 1000 ml sits at main preparation_steps[1], and the entire basal multi-action paragraph is labelled AUTOCLAVE. Place the stock instruction within its stock context and distinguish supported sequential actions without discarding the existing gas, duration, exclusion, filtration or pH controls. Missing autoclave settings and late-stock strengths/doses remain unknown. KOMODO owners lack this DSM text and have conflicting source atmosphere metadata; first resolve their variant identity rather than copying DSM conditions into them.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

Sodium resazurin is currently assigned neutral CHEBI:8806; the exact primary and API specify the sodium salt. NiCl2 x 6 H2O is assigned anhydrous CHEBI:34887 in both primary and secondary slots. Reconcile these supplied forms to exact current ontology objects and canonical labels while retaining supported stock amounts and source distinctions. The MIM sodium-resazurin synonym does not override the neutral ontology formula. The nickel preferred row is REJECTED while an exact synonym maps to 53542; neither status alone validates a replacement. Calcium D-pantothenate, ferrous ammonium sulfate heptahydrate and non-stereospecific lipoic acid are explicitly retained as compatible with their DSM source forms.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

KNO3 retains MediaIngredientMech:000170, absent from the exact packaged current snapshot, while its primary CHEBI:63043 remains correct. Yeast extract has no primary or secondary term and sodium resazurin/calcium pantothenate lack secondary links. Review current exact MIM candidates without treating snapshot absence as historical invalidity or treating synonym rows as supplied-form proof. The scientific form errors are separately tracked; these linkage gaps do not justify changing supported amounts.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a6

No retained ingredient claim authenticates these current quantities; all source support found here is newly linked review evidence. The complete seven reports contain prior conflict/unsupported decisions and derivative source excerpts, not proof of completed source curation. Both KOMODO owners retain malformed .fZ import timestamps and timezone-naive resolver timestamps. Keep original events byte-preserved; append verified context or corrections only when authoritative event provenance is recovered. September topology updates and ingredients_curated flags do not certify current external formula equality.

- Keep original history events byte-preserved; append new verified provenance in a new event rather than rewriting malformed timestamps.
- Attach exact source URLs, raw digests, original access times and scoped snippets without calling derivative report prose an original retrieval receipt.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsmz985 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf; REVIEW_WORK/batch072/source01-03-supplement/dsmz985.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| api985 | https://mediadive.dsmz.de/rest/medium/985; REVIEW_WORK/batch072/source01-03-supplement/api985.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| komodo985 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985; REVIEW_WORK/batch072/source01-03-supplement/komodo985.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| komodo985dot1 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985.1; REVIEW_WORK/batch072/source01-03-supplement/komodo985dot1.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| komodoList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; REVIEW_WORK/batch072/source01-03-supplement/komodoList.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| dsm19306 | https://www.dsmz.de/collection/catalogue/details/culture/DSM-19306; REVIEW_WORK/batch072/source01-03-preflight/dsm19306.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Exact selected-source identity preflight. Organism/source context screened before any operational assessment; no source transfer between variants. |
| target | data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| owner-2 | data/normalized_yaml/bacterial/for_dsm_19306.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| owner-3 | data/normalized_yaml/bacterial/tepidibacter_medium.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| report-18 | reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-19 | reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/for_dsm_19306.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-20 | reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/tepidibacter_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-22 | reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/deferribacter_autotrophicus_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_19306.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-26 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/tepidibacter_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch072/record01/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete original text of all seven scoped historical reports; current object/digest joins are separately recorded. |
| historical-selected-parent-rows | REVIEW_WORK/batch072/record01/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch072/record01/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete parsed target and all three maintained owner documents, with exact original file hashes. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| writer-cleanup | scripts/cleanup_media_quality.py; MediaQualityFixer._merge_ingredient_group | context_only | Current _merge_ingredient_group keeps identical duplicate amounts and flags disagreements; it no longer sums duplicate quantities. It cannot establish compatible stock/main bases or repair a historical flattened sum. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _normalize_unit; _classify_preparation_action | context_only | Current primary-compound parsing excludes referenced stocks and percentage stock additions; stocks are retained separately. Explicit g_l is preferred, but fallback bare units do not prove final volume. The action classifier matches autoclave before filtration and does not split this mixed paragraph. This current behavior is distinct from the documented historical import. |
| writer-resolver | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.extract_dsmz_id; DSMZCompositionResolver.merge_composition | context_only | Current DSMZCompositionResolver extracts a base accession after removing letter suffixes and copies ingredients/solutions without source-formulation equivalence testing. The actual historical events here separately record copying DSMZ 985; current code is not evidence of the exact historical executable. |
| writer-repair | scripts/repair_komodo_985_tepidibacter_score10.py; Complete file; fixed signature and topology updates | context_only | Current repair script tests the copied local ingredient signature and pH before assigning base/variant/duplicate relationships and curated flags. That establishes the local repair mechanics, not external identity equivalence; the newly captured KOMODO 985 recipe contradicts the duplicate formulation premise. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch072/source01-03-supplement/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; REVIEW_WORK/batch072/source01-03-supplement/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; REVIEW_WORK/batch072/source01-03-supplement/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch072/source01-03-supplement/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi3312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:3312; REVIEW_WORK/batch072/source01-03-supplement/chebi3312.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527; REVIEW_WORK/batch072/source01-03-supplement/chebi131527.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi131378 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131378; REVIEW_WORK/batch072/source01-03-supplement/chebi131378.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; REVIEW_WORK/batch072/source01-03-supplement/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377; REVIEW_WORK/batch072/source01-03-supplement/chebi29377.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi63043 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63043; REVIEW_WORK/batch072/source01-03-supplement/chebi63043.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32954; REVIEW_WORK/batch072/source01-03-supplement/chebi32954.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209; REVIEW_WORK/batch072/source01-03-supplement/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883; REVIEW_WORK/batch072/source01-03-supplement/chebi17883.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249; REVIEW_WORK/batch072/source01-03-supplement/chebi86249.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976; REVIEW_WORK/batch072/source01-03-supplement/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; REVIEW_WORK/batch072/source01-03-supplement/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch072/source01-03-supplement/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; REVIEW_WORK/batch072/source01-03-supplement/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; REVIEW_WORK/batch072/source01-03-supplement/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; REVIEW_WORK/batch072/source01-03-supplement/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch072/source01-03-supplement/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145; REVIEW_WORK/batch072/source01-03-supplement/chebi32145.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131361; REVIEW_WORK/batch072/source01-03-supplement/chebi131361.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63939; REVIEW_WORK/batch072/source01-03-supplement/chebi63939.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956; REVIEW_WORK/batch072/source01-03-supplement/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470; REVIEW_WORK/batch072/source01-03-supplement/chebi27470.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961; REVIEW_WORK/batch072/source01-03-supplement/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105; REVIEW_WORK/batch072/source01-03-supplement/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015; REVIEW_WORK/batch072/source01-03-supplement/chebi17015.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940; REVIEW_WORK/batch072/source01-03-supplement/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345; REVIEW_WORK/batch072/source01-03-supplement/chebi31345.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843; REVIEW_WORK/batch072/source01-03-supplement/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753; REVIEW_WORK/batch072/source01-03-supplement/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494; REVIEW_WORK/batch072/source01-03-supplement/chebi16494.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| quantities | REVIEW_WORK/batch072/record01/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch072/record01/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch072/record01/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch072/record01/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch072/record01/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch072/record01/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch072/record01/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch072/record01/validate-schema.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch072/record01/validate-strict.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch072/record01/validate-terms.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch072/record01/validate-references.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- The exact KOMODO985.1 recipe and catalogue request returned 403; the fresh985 recipe succeeded. The strain-wrapper formula is unresolved and no DSM19306 medium growth inference is made.
- The full KOMODO compound table is inventoried as its own source version. Model-derived SEED component aggregates and rounded molar values are not independently revalidated or transferred to curated chemistry.
- Provider mmol_l conversions are not used to validate local mass concentrations; hydrate-sensitive molar conversions would need their own assessment. Bare HCl25% has no stated percentage basis.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T162846Z-culturemech-002167-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: DEFERRIBACTER AUTOTROPHICUS MEDIUM'
started_at: '2026-10-28T16:11:57.446477Z'
finished_at: '2026-10-28T16:28:46.234303Z'
reviewer:
  identity: Codex batch006_validation
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Read-only independent review of maintained source records, exact
    captured sources, fresh scoped primary sources and original diagnostics.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: true
summary: The selected record needs source-identity reconciliation, stock-stage restoration
  and supplied-form correction. Fresh KOMODO 985 disagrees with DSM 985, while 985.1
  remains unavailable. Preserve supported DSM basal provider rates and the existing
  preparation text, separate all stock quantities and doses, retain exact variant
  uncertainty, and attach claim-level evidence before regeneration. Four original
  canonical checks passed; these shape checks do not certify formulation equivalence.
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
  - path: data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml
    sha256: c07c41bbd873d2694cac4472382fb9efe900a2c10d2b36b1544e68239e81ad67
    role: target
  - path: data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml
    sha256: f8cd7c05af22e0e0dd9b1e4bff61ad90d9de66266c54fb9291b57b5ba5b5d099
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_19306.yaml
    sha256: 113b55192dedeaa93ed705d26aadbcd54528d8db24896cdfc85c09f5aaec0038
    role: context
  - path: data/normalized_yaml/bacterial/tepidibacter_medium.yaml
    sha256: 0efdb2df36079a5a1c14d57100c07c37042f942b5b90692de8fd0a931bc296d1
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json
    sha256: 1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/for_dsm_19306.yaml.md
    sha256: cefd78b94fed6a2700a0bf70ba597b963c1645bfaf156689f28504ba99a359b8
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/tepidibacter_medium.yaml.md
    sha256: f10a35b5c5dd7f3817fa50612113b4c7f37dac85333d0aee8f1883afb7f6ab36
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/plan.json
    sha256: 94e89303f14558d9b0d485aa6cb4eb646050837864ab920d759763a3a483b94f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/deferribacter_autotrophicus_medium.yaml.md
    sha256: 0a14c935521a1ef3aa01692425bb0d8ee8aa377836575b0cbf7d95a034c559cd
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.md
    sha256: 914b023c3643843036d87181965d7f1e47cb9889d2f8c8fbf5a9fc352c92395f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.md
    sha256: 6b752c4115f45606aac4304d90d3cd6b937505b26a03300135c54a23f64f9283
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_19306.md
    sha256: 4c94315b5b34cda7b889f75db7e28ed792b20a917febb891f8a25d417e563645
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/tepidibacter_medium.md
    sha256: 9d9e50508a3dac3433f98a2b8cd3ac9b9dd93dae7e20fe5f925d674301d412f1
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
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
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
    role: context
  - path: scripts/repair_komodo_985_tepidibacter_score10.py
    sha256: 7be7d97a2c95b2c75e451f37a8126cff95bf30356f4189859c508ec8c90250a7
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
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
  - path: src/culturemech/import/mediadb_importer.py
    sha256: 5c2d98caf450ee8bb2f73f112e4edab7c3e0f2fa5f2aa7bd2a34e6fd2fdfd4d0
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
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: Whole exact target/owner with explicit scoped dependencies, current
    sources and historical claims.
  selection: Authoritative batch072 index 01
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:002167
targets:
- target_id: CultureMech:002167
  path: data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml
  label: deferribacter_autotrophicus_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_19306.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/tepidibacter_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:002167
  command: just validate-schema data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml
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
  - CultureMech:002167
  command: just validate-strict data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml
    --out REVIEW_WORK/batch072/record01/strict.tsv --workers 1 --quiet
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
  - CultureMech:002167
  command: just validate-terms data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml
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
  - CultureMech:002167
  command: just validate-references data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsmz985
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf
  accessed_at: '2026-10-28T16:12:45.024127Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/dsmz985.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e
- evidence_id: api985
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/985
  accessed_at: '2026-10-28T16:12:45.915612Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/api985.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6
- evidence_id: komodo985
  kind: primary_source
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985
  accessed_at: '2026-10-28T16:12:46.724943Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/komodo985.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf
- evidence_id: komodo985dot1
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985.1
  accessed_at: '2026-10-28T16:12:46.484156Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/komodo985dot1.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: b97778f4db10370568a279f54758e20aa041e363dbf1ede54ec29ca4c95cedcf
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985.1;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodoList
  kind: search
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  accessed_at: '2026-10-28T16:12:46.490169Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/komodoList.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 7e3e56a44da28f8e2ed0359c80e0d7a71fc9dee7b0254420a34c99faf4bd8bb1
  search_scope: One exact public GET of https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: dsm19306
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-19306
  accessed_at: '2026-10-28T16:11:59.217791Z'
  locator: REVIEW_WORK/batch072/source01-03-preflight/dsm19306.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Exact selected-source identity preflight. Organism/source
    context screened before any operational assessment; no source transfer between
    variants.
  snapshot_sha256: bcff195a494a55e5ca82b47589caa7472d929ae71ef16f22ceab04bc8427eccb
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T16:22:24.832735Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: c07c41bbd873d2694cac4472382fb9efe900a2c10d2b36b1544e68239e81ad67
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T16:22:24.832894Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: f8cd7c05af22e0e0dd9b1e4bff61ad90d9de66266c54fb9291b57b5ba5b5d099
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T16:22:24.832922Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T16:22:24.833219Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T16:22:24.833242Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T16:22:24.833263Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_19306.yaml
  locator: Complete file
  accessed_at: '2026-10-28T16:22:24.833285Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: 113b55192dedeaa93ed705d26aadbcd54528d8db24896cdfc85c09f5aaec0038
- evidence_id: owner-3
  kind: record_content
  reference: data/normalized_yaml/bacterial/tepidibacter_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T16:22:24.833305Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: 0efdb2df36079a5a1c14d57100c07c37042f942b5b90692de8fd0a931bc296d1
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T16:22:24.833326Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/for_dsm_19306.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T16:22:24.840596Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: cefd78b94fed6a2700a0bf70ba597b963c1645bfaf156689f28504ba99a359b8
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/tepidibacter_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T16:22:24.840666Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: f10a35b5c5dd7f3817fa50612113b4c7f37dac85333d0aee8f1883afb7f6ab36
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T16:22:24.840703Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 94e89303f14558d9b0d485aa6cb4eb646050837864ab920d759763a3a483b94f
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/deferribacter_autotrophicus_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T16:22:24.846156Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 0a14c935521a1ef3aa01692425bb0d8ee8aa377836575b0cbf7d95a034c559cd
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T16:22:24.846225Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 914b023c3643843036d87181965d7f1e47cb9889d2f8c8fbf5a9fc352c92395f
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T16:22:24.846256Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 6b752c4115f45606aac4304d90d3cd6b937505b26a03300135c54a23f64f9283
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_19306.md
  locator: Complete report
  accessed_at: '2026-10-28T16:22:24.846285Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 4c94315b5b34cda7b889f75db7e28ed792b20a917febb891f8a25d417e563645
- evidence_id: report-26
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/tepidibacter_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T16:22:24.846308Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 9d9e50508a3dac3433f98a2b8cd3ac9b9dd93dae7e20fe5f925d674301d412f1
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch072/record01/historical-reading.json
  accessed_at: '2026-10-28T16:22:24.846336Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete original text of all seven scoped historical reports; current
    object/digest joins are separately recorded.
  snapshot_sha256: 78718a69e3555cff8cfab588380ff909fe0c7635e05163c4dc7e21c9cf4d324b
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch072/record01/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T16:22:24.846689Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 2024cb160064d7b5d13245d4414ad29bea7fe980bb50454e749d542425477a11
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch072/record01/complete-document-reader.json
  accessed_at: '2026-10-28T16:22:24.846792Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete parsed target and all three maintained owner documents, with exact
    original file hashes.
  snapshot_sha256: 7d6f5a0d9f6244b72749f4bdcf81d4dbf7a38d57ee81bb8e6ce185d2925115d4
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T16:22:24.847059Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: MediaQualityFixer._merge_ingredient_group
  accessed_at: '2026-10-28T16:22:24.847123Z'
  support: context_only
  summary: Current _merge_ingredient_group keeps identical duplicate amounts and flags
    disagreements; it no longer sums duplicate quantities. It cannot establish compatible
    stock/main bases or repair a historical flattened sum.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _normalize_unit;
    _classify_preparation_action
  accessed_at: '2026-10-28T16:22:24.847153Z'
  support: context_only
  summary: Current primary-compound parsing excludes referenced stocks and percentage
    stock additions; stocks are retained separately. Explicit g_l is preferred, but
    fallback bare units do not prove final volume. The action classifier matches autoclave
    before filtration and does not split this mixed paragraph. This current behavior
    is distinct from the documented historical import.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.extract_dsmz_id; DSMZCompositionResolver.merge_composition
  accessed_at: '2026-10-28T16:22:24.847181Z'
  support: context_only
  summary: Current DSMZCompositionResolver extracts a base accession after removing
    letter suffixes and copies ingredients/solutions without source-formulation equivalence
    testing. The actual historical events here separately record copying DSMZ 985;
    current code is not evidence of the exact historical executable.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-repair
  kind: record_content
  reference: scripts/repair_komodo_985_tepidibacter_score10.py
  locator: Complete file; fixed signature and topology updates
  accessed_at: '2026-10-28T16:22:24.847206Z'
  support: context_only
  summary: Current repair script tests the copied local ingredient signature and pH
    before assigning base/variant/duplicate relationships and curated flags. That
    establishes the local repair mechanics, not external identity equivalence; the
    newly captured KOMODO 985 recipe contradicts the duplicate formulation premise.
  snapshot_sha256: 7be7d97a2c95b2c75e451f37a8126cff95bf30356f4189859c508ec8c90250a7
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  accessed_at: '2026-10-28T16:12:49.287455Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi26710.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345
  accessed_at: '2026-10-28T16:12:55.549204Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi86345.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 94b600ced6e98743e2d1b02c73e1756f8f81b639407a8fdd080c96d8fa563c70
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  accessed_at: '2026-10-28T16:12:51.568341Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi32588.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  accessed_at: '2026-10-28T16:12:50.520682Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi31206.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi3312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:3312
  accessed_at: '2026-10-28T16:12:52.123383Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi3312.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: c468d22946b95659970843fef50c7cce0f87796940350baacca568c52aa5744e
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527
  accessed_at: '2026-10-28T16:12:47.205740Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi131527.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 0a5297c84ea9dd82508960482211f6b3c993fd8e2b83fe755dd2b23316cc4068
- evidence_id: chebi131378
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131378
  accessed_at: '2026-10-28T16:12:47.205895Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi131378.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e1dd9fff0f7cf00f7161a7c81242211edeea989668f3881cb468e67b6e33a325
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806
  accessed_at: '2026-10-28T16:12:56.152044Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi8806.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f2530ec9c15f59a3d132a466c9c3a899497bab0f85b996d3e27bef8612f89982
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377
  accessed_at: '2026-10-28T16:12:49.889499Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi29377.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e0c2a85ab7be9313c564f96ee47b87e1bf3e01ad1e9fd627d1dbddced5d068c4
- evidence_id: chebi63043
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63043
  accessed_at: '2026-10-28T16:12:53.510135Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi63043.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4f99aa30339e54a5e41bd6af7ca64c10888d50c3aa9e76cff2dfb1d52ec9885a
- evidence_id: chebi32954
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32954
  accessed_at: '2026-10-28T16:12:51.795775Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi32954.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 6718762e0aceec57316f70ff5a6264c973f1f2b235e6d5bbe077a9c349394fb8
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209
  accessed_at: '2026-10-28T16:12:54.403428Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi76209.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4896ec517123ebeb1afcbac7bc30a7103976f03891af0c86c992196b5f0db969
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883
  accessed_at: '2026-10-28T16:12:48.660713Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi17883.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e5ab164ef9ff955da1a504ca34ab4d3b69539d9bf721936c9dd563ccbbd0e3b0
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249
  accessed_at: '2026-10-28T16:12:55.100601Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi86249.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4d7f48f88badcba85a62e59842c6ec921f5478eb76695098b17847ed62c8530a
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976
  accessed_at: '2026-10-28T16:12:52.906488Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi49976.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d3bdc4c6f01d01422fafe433df4e4011e01cf7e55e0329ab341a60ece780946f
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  accessed_at: '2026-10-28T16:12:55.819301Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi86368.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  accessed_at: '2026-10-28T16:12:51.860778Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi33118.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503
  accessed_at: '2026-10-28T16:12:53.078674Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi53503.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: a626d2aa210aafd9572221d4893cd206310d5df507e474e1528997048f522250
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318
  accessed_at: '2026-10-28T16:12:55.416720Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi86318.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: bd88e1499f370a9f474b29fa7a9a83aa5c42c69d0b6772ece8c89d646dfda8d8
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  accessed_at: '2026-10-28T16:12:52.177011Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi34887.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 3a37ef35991d24faf578286a7d7557ee1b0646c286dd3f8a555d833e6bf82a57
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  accessed_at: '2026-10-28T16:12:53.992464Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi75213.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145
  accessed_at: '2026-10-28T16:12:51.249495Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi32145.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 089212e8c86e2d4a4b145366c8bc67e0056565ef6970dcdc3df63ad20dac234d
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131361
  accessed_at: '2026-10-28T16:12:47.231270Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi131361.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d88b30f797a300c3935e550a4770cb598bbed342a9c2a343f77bdce496e99db9
- evidence_id: chebi63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63939
  accessed_at: '2026-10-28T16:12:53.671577Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi63939.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 01f41117ab89dbd1d514a894850dc06afd5d95c0bee7fd89f7dfdb54c309c514
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956
  accessed_at: '2026-10-28T16:12:47.877940Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi15956.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 5135a39e8b52c878896db22443f00507125db80e5ce4bb1dcc97914b9bdd7316
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470
  accessed_at: '2026-10-28T16:12:49.346362Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi27470.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e1820a7a704794fa20995eea5037e03c2b22b847817c28bb2f45f80762c275d1
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961
  accessed_at: '2026-10-28T16:12:50.329857Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi30961.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 855ea2cf0e89d25ab4a560ab1c2dab6ac861d215bc5473cb4d3a0a2d4cdff438
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105
  accessed_at: '2026-10-28T16:12:52.756154Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi49105.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f9dbae8cd2dcbd38d914abb99730e341ff280d3a44f20f95b2663e47664780cf
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015
  accessed_at: '2026-10-28T16:12:48.576382Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi17015.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 17f7ac7c03d75b85a96f951321902906266f3ce8fa44faea4814fac46560e3e6
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940
  accessed_at: '2026-10-28T16:12:48.040019Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi15940.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: c291a1c1bb0d6af05ac4005af0957534f430db47e7df9cec874f8a94d961dba1
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345
  accessed_at: '2026-10-28T16:12:50.639058Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi31345.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: c3341e7cf8a7ea0768d505265376c1514f161c9048b6e878314e204341d702eb
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843
  accessed_at: '2026-10-28T16:12:48.675502Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi176843.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9c73ea31864abce6b9ed6328e9ed491bc1cad2ba27f40adb5c00f0f192838e63
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753
  accessed_at: '2026-10-28T16:12:50.104805Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi30753.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1340e054634ce960494b9388f6e3fd231d9e7d66969c3c11932ee2058171fd2c
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494
  accessed_at: '2026-10-28T16:12:47.854714Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi16494.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 192c51f672f633c6071a3397d5785fb2bca6eaf8f9b787f7aaaa6c2aeb3b1a2f
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch072/record01/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:28:46.234303Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 5e303fd7b313e304e7883ec5b81e9ddddc1e03348720283a1ce0e97b7b3835d5
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch072/record01/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:22:25.096073Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 5697d016b4238f0706eeecbbe79b28928d07f903d9ecb81c8cf875c62dd1e124
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch072/record01/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:22:25.096250Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 79e3ebc1cd4a9d6c22400f0547fe69b8d4ec84047e31f2fa95747816c8b898ef
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch072/record01/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:22:25.096371Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 68d014d8ae303b6dbc6653252e25c42b88153bf108b472d3c7fc6211ff6c85a6
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch072/record01/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:22:25.096479Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: cff2eceee4e5a5ddf04fc4857bd08a56107dfec3868b4f774607b58f79175b40
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch072/record01/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:22:25.096520Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 3d87fe3dabde4c88e8f412ff50291f5d9ef505792db98b7622eebbc379eaa461
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch072/record01/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:22:25.096557Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch072/record01/validate-schema.json
  accessed_at: '2026-10-28T16:11:58.584627Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 0011de914ad8c0d88abea083eef98709a3dda419529965067bfc09b363e3af34
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch072/record01/validate-strict.json
  accessed_at: '2026-10-28T16:11:59.518911Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 53a1a1b5dad61df1ec986910c877381d828d9e89842c63bbc7c974d54b72e8f3
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch072/record01/validate-terms.json
  accessed_at: '2026-10-28T16:12:01.009429Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 774491a67badb0c9efee9fa94bcf069f0906f4d61b500862b244f7911de1dc24
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch072/record01/validate-references.json
  accessed_at: '2026-10-28T16:12:01.886504Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: ad0e192235f55a359a1dbe0896d6c0f6d9b97d93b451d0abbc508d683ba2f296
assessments:
- assessment_id: identity
  area: identity
  topic: Distinct source identities and current catalogue check
  outcome: concern
  summary: DSM985, KOMODO985 and KOMODO985.1 are not interchangeable merely because
    copied local ingredient signatures match. Fresh KOMODO985 shows a distinct formula,
    and exact985.1 remains inaccessible. DSM19306 is currently Clostridium tepidiprofundi;
    this is identity context only.
  target_ids:
  - CultureMech:002167
  evidence_ids:
  - dsmz985
  - api985
  - komodo985
  - komodo985dot1
  - dsm19306
- assessment_id: classification
  area: scope
  topic: Record type and category
  outcome: supported
  summary: Bacterial liquid complex/semi-defined representation is consistent with
    the selected DSM source and yeast-extract component. No target-organism growth
    or optimal condition is inferred from the name.
  target_ids:
  - CultureMech:002167
  evidence_ids:
  - target
  - dsmz985
- assessment_id: claims
  area: evidence
  topic: Existing support and newly captured sources
  outcome: concern
  summary: The source PDFs, exact provider objects and current KOMODO page are kept
    separately; the complete stored recipe has no attached claims. Numeric agreement
    with a provider stock does not verify main-medium placement.
  target_ids:
  - CultureMech:002167
  evidence_ids:
  - dsmz985
  - api985
  - komodo985
  - old-claims
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 140 current concentration fields are covered by 80 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:002167
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b072-quantity-inventory-v1","target":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","quantity_field_count":140,"decisions":[{"quantity_id":"q1","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"17.9462","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"17.9462","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[0].concentration","stored":{"value":"17.9462","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"17.9462","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    stored 17.9462 G_PER_L equals the explicit current DSMZ provider g_l for NaCl
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985
    Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 3-3","quote":"NaCl                                                      18.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 18,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 17.9462,\n                        \"mmol_l\":
    307.087,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 17.9462 G_PER_L equals the explicit current DSMZ provider g_l for NaCl
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 17.9462 G_PER_L equals the explicit current DSMZ provider g_l for NaCl
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"The
    exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent
    evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[0].concentration","decision":"conflict","rationale":"The
    current exact KOMODO985 table uses a distinct formulation and different declared
    rates or forms. The local copied DSM985 value is not endorsed as equivalent merely
    because some rounded numbers resemble it."}]},{"quantity_id":"q2","label":"MgCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.98804","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.98804","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.98804","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.98804","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    stored 3.98804 G_PER_L equals the explicit current DSMZ provider g_l for MgCl2
    x 6 H2O in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water;
    provider volume 1003 ml is a separate normalization convention, not an explicit
    primary final make-up. Credit this rate only for the DSM source layer. The copied
    KOMODO base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985
    Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 4-4","quote":"MgCl2 x 6 H2O                                              4.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.98804,\n                        \"mmol_l\":
    19.6162,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 3.98804 G_PER_L equals the explicit current DSMZ provider g_l for MgCl2
    x 6 H2O in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water;
    provider volume 1003 ml is a separate normalization convention, not an explicit
    primary final make-up. Credit this rate only for the DSM source layer. The copied
    KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 3.98804 G_PER_L equals the explicit current DSMZ provider g_l for MgCl2
    x 6 H2O in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water;
    provider volume 1003 ml is a separate normalization convention, not an explicit
    primary final make-up. Credit this rate only for the DSM source layer. The copied
    KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The
    exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent
    evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[1].concentration","decision":"conflict","rationale":"The
    current exact KOMODO985 table uses a distinct formulation and different declared
    rates or forms. The local copied DSM985 value is not endorsed as equivalent merely
    because some rounded numbers resemble it."}]},{"quantity_id":"q3","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.338983","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.338983","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.338983","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.338983","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    stored 0.338983 G_PER_L equals the explicit current DSMZ provider g_l for KCl
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985
    Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 5-5","quote":"KCl                                                        0.34        g","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.34,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.338983,\n                        \"mmol_l\":
    4.54706,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 0.338983 G_PER_L equals the explicit current DSMZ provider g_l for KCl
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 0.338983 G_PER_L equals the explicit current DSMZ provider g_l for KCl
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The
    exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent
    evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[2].concentration","decision":"conflict","rationale":"The
    current exact KOMODO985 table uses a distinct formulation and different declared
    rates or forms. The local copied DSM985 value is not endorsed as equivalent merely
    because some rounded numbers resemble it."}]},{"quantity_id":"q4","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.249252","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.249252","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.249252","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.249252","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    stored 0.249252 G_PER_L equals the explicit current DSMZ provider g_l for NH4Cl
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985
    Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 6-6","quote":"NH4Cl                                                      0.25        g","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.249252,\n                        \"mmol_l\":
    4.65979,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 0.249252 G_PER_L equals the explicit current DSMZ provider g_l for NH4Cl
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 0.249252 G_PER_L equals the explicit current DSMZ provider g_l for NH4Cl
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The
    exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent
    evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[3].concentration","decision":"conflict","rationale":"The
    current exact KOMODO985 table uses a distinct formulation and different declared
    rates or forms. The local copied DSM985 value is not endorsed as equivalent merely
    because some rounded numbers resemble it."}]},{"quantity_id":"q5","label":"CaCl2","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.109671","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.109671","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.109671","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.109671","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    stored 0.109671 G_PER_L equals the explicit current DSMZ provider g_l for CaCl2
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985
    Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 7-7","quote":"CaCl2                                                      0.11        g","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"CaCl2\",\n                        \"compound_id\":
    81,\n                        \"amount\": 0.11,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.109671,\n                        \"mmol_l\":
    0.988205,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 0.109671 G_PER_L equals the explicit current DSMZ provider g_l for CaCl2
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 0.109671 G_PER_L equals the explicit current DSMZ provider g_l for CaCl2
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The
    exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent
    evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[4].concentration","decision":"conflict","rationale":"The
    current exact KOMODO985 table uses a distinct formulation and different declared
    rates or forms. The local copied DSM985 value is not endorsed as equivalent merely
    because some rounded numbers resemble it."}]},{"quantity_id":"q6","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.179462","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.179462","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.179462","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.179462","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    stored 0.179462 G_PER_L equals the explicit current DSMZ provider g_l for K2HPO4
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985
    Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 8-8","quote":"K2HPO4                                                     0.18        g","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.18,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.179462,\n                        \"mmol_l\":
    1.03035,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 0.179462 G_PER_L equals the explicit current DSMZ provider g_l for K2HPO4
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 0.179462 G_PER_L equals the explicit current DSMZ provider g_l for K2HPO4
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The
    exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent
    evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[5].concentration","decision":"conflict","rationale":"The
    current exact KOMODO985 table uses a distinct formulation and different declared
    rates or forms. The local copied DSM985 value is not endorsed as equivalent merely
    because some rounded numbers resemble it."}]},{"quantity_id":"q7","label":"Fe(NH4)2(SO4)2
    x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.0199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.0199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.0199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.0199402","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    stored 0.0199402 G_PER_L equals the explicit current DSMZ provider g_l for Fe(NH4)2(SO4)2
    x 7 H2O in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water;
    provider volume 1003 ml is a separate normalization convention, not an explicit
    primary final make-up. Credit this rate only for the DSM source layer. The copied
    KOMODO base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985
    Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 9-9","quote":"Fe(NH4)2(SO4)2 x 7 H2O                                    20.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Fe(NH4)2(SO4)2 x 7 H2O\",\n                        \"compound_id\":
    456,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0199402,\n                        \"mmol_l\":
    0.0486161,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 0.0199402 G_PER_L equals the explicit current DSMZ provider g_l for Fe(NH4)2(SO4)2
    x 7 H2O in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water;
    provider volume 1003 ml is a separate normalization convention, not an explicit
    primary final make-up. Credit this rate only for the DSM source layer. The copied
    KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 0.0199402 G_PER_L equals the explicit current DSMZ provider g_l for Fe(NH4)2(SO4)2
    x 7 H2O in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water;
    provider volume 1003 ml is a separate normalization convention, not an explicit
    primary final make-up. Credit this rate only for the DSM source layer. The copied
    KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The
    exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent
    evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[6].concentration","decision":"conflict","rationale":"The
    current exact KOMODO985 table uses a distinct formulation and different declared
    rates or forms. The local copied DSM985 value is not endorsed as equivalent merely
    because some rounded numbers resemble it."}]},{"quantity_id":"q8","label":"Yeast
    extract","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.199402","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.199402","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    stored 0.199402 G_PER_L equals the explicit current DSMZ provider g_l for Yeast
    extract in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water;
    provider volume 1003 ml is a separate normalization convention, not an explicit
    primary final make-up. Credit this rate only for the DSM source layer. The copied
    KOMODO base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985
    Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 12-12","quote":"Yeast extract                                              0.20        g","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.199402,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 0.199402 G_PER_L equals the explicit current DSMZ provider g_l for Yeast
    extract in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water;
    provider volume 1003 ml is a separate normalization convention, not an explicit
    primary final make-up. Credit this rate only for the DSM source layer. The copied
    KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 0.199402 G_PER_L equals the explicit current DSMZ provider g_l for Yeast
    extract in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water;
    provider volume 1003 ml is a separate normalization convention, not an explicit
    primary final make-up. Credit this rate only for the DSM source layer. The copied
    KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The
    exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent
    evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[7].concentration","decision":"conflict","rationale":"The
    current exact KOMODO985 table uses a distinct formulation and different declared
    rates or forms. The local copied DSM985 value is not endorsed as equivalent merely
    because some rounded numbers resemble it."}]},{"quantity_id":"q9","label":"Sodium
    resazurin","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.000498504","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    stored 0.000498504 G_PER_L equals the explicit current DSMZ provider g_l for Sodium
    resazurin in Main sol. 985. The PDF supplies a batch amount with 1000 ml input
    water; provider volume 1003 ml is a separate normalization convention, not an
    explicit primary final make-up. Credit this rate only for the DSM source layer.
    The copied KOMODO base and strain wrapper require independent source reconciliation.
    The primary specifies a 0.1% w/v sodium-resazurin stock and 0.50 ml addition;
    preserve both and review the neutral primary ID separately.","source_stage":"DSMZ985
    Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 13-13","quote":"Sodium resazurin (0.1% w/v)                                0.50       ml","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 0.000498504 G_PER_L equals the explicit current DSMZ provider g_l for Sodium
    resazurin in Main sol. 985. The PDF supplies a batch amount with 1000 ml input
    water; provider volume 1003 ml is a separate normalization convention, not an
    explicit primary final make-up. Credit this rate only for the DSM source layer.
    The copied KOMODO base and strain wrapper require independent source reconciliation.
    The primary specifies a 0.1% w/v sodium-resazurin stock and 0.50 ml addition;
    preserve both and review the neutral primary ID separately."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 0.000498504 G_PER_L equals the explicit current DSMZ provider g_l for Sodium
    resazurin in Main sol. 985. The PDF supplies a batch amount with 1000 ml input
    water; provider volume 1003 ml is a separate normalization convention, not an
    explicit primary final make-up. Credit this rate only for the DSM source layer.
    The copied KOMODO base and strain wrapper require independent source reconciliation.
    The primary specifies a 0.1% w/v sodium-resazurin stock and 0.50 ml addition;
    preserve both and review the neutral primary ID separately."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The
    exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent
    evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[8].concentration","decision":"conflict","rationale":"The
    current exact KOMODO985 table uses a distinct formulation and different declared
    rates or forms. The local copied DSM985 value is not endorsed as equivalent merely
    because some rounded numbers resemble it."}]},{"quantity_id":"q10","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1.49551","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1.49551","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1.49551","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1.49551","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    stored 1.49551 G_PER_L equals the explicit current DSMZ provider g_l for Na2CO3
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985
    Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 14-14","quote":"Na2CO3                                                     1.50        g","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.49551,\n                        \"mmol_l\":
    14.1102,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 1.49551 G_PER_L equals the explicit current DSMZ provider g_l for Na2CO3
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 1.49551 G_PER_L equals the explicit current DSMZ provider g_l for Na2CO3
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The
    exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent
    evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[9].concentration","decision":"conflict","rationale":"The
    current exact KOMODO985 table uses a distinct formulation and different declared
    rates or forms. The local copied DSM985 value is not endorsed as equivalent merely
    because some rounded numbers resemble it."}]},{"quantity_id":"q11","label":"KNO3","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.997009","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    stored 0.997009 G_PER_L equals the explicit current DSMZ provider g_l for KNO3
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985
    Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 15-15","quote":"KNO3                                                       1.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"KNO3\",\n                        \"compound_id\":
    191,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\":
    9.86132,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 0.997009 G_PER_L equals the explicit current DSMZ provider g_l for KNO3
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 0.997009 G_PER_L equals the explicit current DSMZ provider g_l for KNO3
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The
    exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent
    evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[10].concentration","decision":"conflict","rationale":"The
    current exact KOMODO985 table uses a distinct formulation and different declared
    rates or forms. The local copied DSM985 value is not endorsed as equivalent merely
    because some rounded numbers resemble it."}]},{"quantity_id":"q12","label":"Na-acetate","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.59521","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.59521","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.59521","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.59521","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    stored 1.59521 G_PER_L equals the explicit current DSMZ provider g_l for Na-acetate
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985
    Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 16-16","quote":"Na-acetate                                                 1.60        g","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\":
    23,\n                        \"amount\": 1.6,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.59521,\n                        \"mmol_l\":
    19.4458,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 1.59521 G_PER_L equals the explicit current DSMZ provider g_l for Na-acetate
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[11].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 1.59521 G_PER_L equals the explicit current DSMZ provider g_l for Na-acetate
    in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water; provider
    volume 1003 ml is a separate normalization convention, not an explicit primary
    final make-up. Credit this rate only for the DSM source layer. The copied KOMODO
    base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"The
    exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent
    evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[11].concentration","decision":"conflict","rationale":"The
    current exact KOMODO985 table uses a distinct formulation and different declared
    rates or forms. The local copied DSM985 value is not endorsed as equivalent merely
    because some rounded numbers resemble it."}]},{"quantity_id":"q13","label":"Na2S
    x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.498504","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    stored 0.498504 G_PER_L equals the explicit current DSMZ provider g_l for Na2S
    x 9 H2O in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water;
    provider volume 1003 ml is a separate normalization convention, not an explicit
    primary final make-up. Credit this rate only for the DSM source layer. The copied
    KOMODO base and strain wrapper require independent source reconciliation.","source_stage":"DSMZ985
    Main sol. 985; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 18-18","quote":"Na2S x 9 H2O                                               0.50        g","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[15]","quote":"{\n                        \"recipe_order\":
    16,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\":
    2.07553,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 0.498504 G_PER_L equals the explicit current DSMZ provider g_l for Na2S
    x 9 H2O in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water;
    provider volume 1003 ml is a separate normalization convention, not an explicit
    primary final make-up. Credit this rate only for the DSM source layer. The copied
    KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[12].concentration","decision":"evidence_only","rationale":"Exact
    DSM985 provider g_l supports the unchanged basal value on its stated normalization
    basis; no attached claim exists and the primary final volume is unresolved. The
    stored 0.498504 G_PER_L equals the explicit current DSMZ provider g_l for Na2S
    x 9 H2O in Main sol. 985. The PDF supplies a batch amount with 1000 ml input water;
    provider volume 1003 ml is a separate normalization convention, not an explicit
    primary final make-up. Credit this rate only for the DSM source layer. The copied
    KOMODO base and strain wrapper require independent source reconciliation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[12].concentration","decision":"unsupported","rationale":"The
    exact KOMODO985.1 route is unavailable. DSM985 copied ingredients are not independent
    evidence for this strain wrapper; no variant transfer is accepted."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The
    current exact KOMODO985 table uses a distinct formulation and different declared
    rates or forms. The local copied DSM985 value is not endorsed as equivalent merely
    because some rounded numbers resemble it."}]},{"quantity_id":"q14","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[13].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 2.5 G_PER_L equals the explicit current DSMZ provider g_l for HCl in Trace
    element solution SL-10. This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution. Primary 25% HCl has no stated percent basis; the provider
    reports 2.5 g_l, but this review does not independently derive that mass from
    the bare percentage.","source_stage":"DSMZ985 Trace element solution SL-10; KOMODO
    identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 33-33","quote":"HCl (25%)                                                  10.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The
    stored 2.5 G_PER_L equals the explicit current DSMZ provider g_l for HCl in Trace
    element solution SL-10. This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution. Primary 25% HCl has no stated percent basis; the provider
    reports 2.5 g_l, but this review does not independently derive that mass from
    the bare percentage."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The
    stored 2.5 G_PER_L equals the explicit current DSMZ provider g_l for HCl in Trace
    element solution SL-10. This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution. Primary 25% HCl has no stated percent basis; the provider
    reports 2.5 g_l, but this review does not independently derive that mass from
    the bare percentage."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The
    stored 2.5 G_PER_L equals the explicit current DSMZ provider g_l for HCl in Trace
    element solution SL-10. This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution. Primary 25% HCl has no stated percent basis; the provider
    reports 2.5 g_l, but this review does not independently derive that mass from
    the bare percentage."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The
    stored 2.5 G_PER_L equals the explicit current DSMZ provider g_l for HCl in Trace
    element solution SL-10. This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution. Primary 25% HCl has no stated percent basis; the provider
    reports 2.5 g_l, but this review does not independently derive that mass from
    the bare percentage."}]},{"quantity_id":"q15","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[14].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 1.5 G_PER_L equals the explicit current DSMZ provider g_l for FeCl2 x 4
    H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution.","source_stage":"DSMZ985 Trace element solution
    SL-10; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 34-34","quote":"FeCl2 x 4 H2O                                               1.50       g","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The
    stored 1.5 G_PER_L equals the explicit current DSMZ provider g_l for FeCl2 x 4
    H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The
    stored 1.5 G_PER_L equals the explicit current DSMZ provider g_l for FeCl2 x 4
    H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The
    stored 1.5 G_PER_L equals the explicit current DSMZ provider g_l for FeCl2 x 4
    H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The
    stored 1.5 G_PER_L equals the explicit current DSMZ provider g_l for FeCl2 x 4
    H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."}]},{"quantity_id":"q16","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.07 G_PER_L equals the explicit current DSMZ provider g_l for ZnCl2 in
    Trace element solution SL-10. This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution.","source_stage":"DSMZ985 Trace element solution SL-10;
    KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 35-35","quote":"ZnCl2                                                      70.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The
    stored 0.07 G_PER_L equals the explicit current DSMZ provider g_l for ZnCl2 in
    Trace element solution SL-10. This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The
    stored 0.07 G_PER_L equals the explicit current DSMZ provider g_l for ZnCl2 in
    Trace element solution SL-10. This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The
    stored 0.07 G_PER_L equals the explicit current DSMZ provider g_l for ZnCl2 in
    Trace element solution SL-10. This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The
    stored 0.07 G_PER_L equals the explicit current DSMZ provider g_l for ZnCl2 in
    Trace element solution SL-10. This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution."}]},{"quantity_id":"q17","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for MnCl2 x 4
    H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution.","source_stage":"DSMZ985 Trace element solution
    SL-10; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 36-36","quote":"MnCl2 x 4 H2O                                             100.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The
    stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for MnCl2 x 4
    H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The
    stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for MnCl2 x 4
    H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The
    stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for MnCl2 x 4
    H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The
    stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for MnCl2 x 4
    H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."}]},{"quantity_id":"q18","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.006 G_PER_L equals the explicit current DSMZ provider g_l for H3BO3 in
    Trace element solution SL-10. This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution.","source_stage":"DSMZ985 Trace element solution SL-10;
    KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 37-37","quote":"H3BO3                                                       6.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The
    stored 0.006 G_PER_L equals the explicit current DSMZ provider g_l for H3BO3 in
    Trace element solution SL-10. This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The
    stored 0.006 G_PER_L equals the explicit current DSMZ provider g_l for H3BO3 in
    Trace element solution SL-10. This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The
    stored 0.006 G_PER_L equals the explicit current DSMZ provider g_l for H3BO3 in
    Trace element solution SL-10. This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The
    stored 0.006 G_PER_L equals the explicit current DSMZ provider g_l for H3BO3 in
    Trace element solution SL-10. This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution."}]},{"quantity_id":"q19","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.19 G_PER_L equals the explicit current DSMZ provider g_l for CoCl2 x
    6 H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution.","source_stage":"DSMZ985 Trace element solution
    SL-10; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 38-38","quote":"CoCl2 x 6 H2O                                             190.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The
    stored 0.19 G_PER_L equals the explicit current DSMZ provider g_l for CoCl2 x
    6 H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The
    stored 0.19 G_PER_L equals the explicit current DSMZ provider g_l for CoCl2 x
    6 H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The
    stored 0.19 G_PER_L equals the explicit current DSMZ provider g_l for CoCl2 x
    6 H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The
    stored 0.19 G_PER_L equals the explicit current DSMZ provider g_l for CoCl2 x
    6 H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."}]},{"quantity_id":"q20","label":"CuCl2 x 2
    H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.002 G_PER_L equals the explicit current DSMZ provider g_l for CuCl2 x
    2 H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution.","source_stage":"DSMZ985 Trace element solution
    SL-10; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 39-39","quote":"CuCl2 x 2 H2O                                               2.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The
    stored 0.002 G_PER_L equals the explicit current DSMZ provider g_l for CuCl2 x
    2 H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The
    stored 0.002 G_PER_L equals the explicit current DSMZ provider g_l for CuCl2 x
    2 H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The
    stored 0.002 G_PER_L equals the explicit current DSMZ provider g_l for CuCl2 x
    2 H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The
    stored 0.002 G_PER_L equals the explicit current DSMZ provider g_l for CuCl2 x
    2 H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."}]},{"quantity_id":"q21","label":"NiCl2 x 6
    H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.024 G_PER_L equals the explicit current DSMZ provider g_l for NiCl2 x
    6 H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution. The supplied nickel hexahydrate is not the
    anhydrous CHEBI:34887 assertion; amount and grounding decisions are separate.","source_stage":"DSMZ985
    Trace element solution SL-10; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 40-40","quote":"NiCl2 x 6 H2O                                              24.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The
    stored 0.024 G_PER_L equals the explicit current DSMZ provider g_l for NiCl2 x
    6 H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution. The supplied nickel hexahydrate is not the
    anhydrous CHEBI:34887 assertion; amount and grounding decisions are separate."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The
    stored 0.024 G_PER_L equals the explicit current DSMZ provider g_l for NiCl2 x
    6 H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution. The supplied nickel hexahydrate is not the
    anhydrous CHEBI:34887 assertion; amount and grounding decisions are separate."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The
    stored 0.024 G_PER_L equals the explicit current DSMZ provider g_l for NiCl2 x
    6 H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution. The supplied nickel hexahydrate is not the
    anhydrous CHEBI:34887 assertion; amount and grounding decisions are separate."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The
    stored 0.024 G_PER_L equals the explicit current DSMZ provider g_l for NiCl2 x
    6 H2O in Trace element solution SL-10. This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution. The supplied nickel hexahydrate is not the
    anhydrous CHEBI:34887 assertion; amount and grounding decisions are separate."}]},{"quantity_id":"q22","label":"Na2MoO4
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.036 G_PER_L equals the explicit current DSMZ provider g_l for Na2MoO4
    x 2 H2O in Trace element solution SL-10. This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution.","source_stage":"DSMZ985 Trace element solution
    SL-10; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 41-41","quote":"Na2MoO4 x 2 H2O                                            36.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The
    stored 0.036 G_PER_L equals the explicit current DSMZ provider g_l for Na2MoO4
    x 2 H2O in Trace element solution SL-10. This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The
    stored 0.036 G_PER_L equals the explicit current DSMZ provider g_l for Na2MoO4
    x 2 H2O in Trace element solution SL-10. This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The
    stored 0.036 G_PER_L equals the explicit current DSMZ provider g_l for Na2MoO4
    x 2 H2O in Trace element solution SL-10. This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The
    stored 0.036 G_PER_L equals the explicit current DSMZ provider g_l for Na2MoO4
    x 2 H2O in Trace element solution SL-10. This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."}]},{"quantity_id":"q23","label":"NaOH","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.5 G_PER_L equals the explicit current DSMZ provider g_l for NaOH in Selenite-tungstate
    solution. This is stock strength flattened into main ingredients; numerical agreement
    with a stock does not make it a final-medium concentration. Keep stock composition
    and the separate receiving addition, without inventing a final-medium dilution.","source_stage":"DSMZ985
    Selenite-tungstate solution; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 57-57","quote":"NaOH                                        0.50    g","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    12.5009,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The
    stored 0.5 G_PER_L equals the explicit current DSMZ provider g_l for NaOH in Selenite-tungstate
    solution. This is stock strength flattened into main ingredients; numerical agreement
    with a stock does not make it a final-medium concentration. Keep stock composition
    and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The
    stored 0.5 G_PER_L equals the explicit current DSMZ provider g_l for NaOH in Selenite-tungstate
    solution. This is stock strength flattened into main ingredients; numerical agreement
    with a stock does not make it a final-medium concentration. Keep stock composition
    and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The
    stored 0.5 G_PER_L equals the explicit current DSMZ provider g_l for NaOH in Selenite-tungstate
    solution. This is stock strength flattened into main ingredients; numerical agreement
    with a stock does not make it a final-medium concentration. Keep stock composition
    and the separate receiving addition, without inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The
    stored 0.5 G_PER_L equals the explicit current DSMZ provider g_l for NaOH in Selenite-tungstate
    solution. This is stock strength flattened into main ingredients; numerical agreement
    with a stock does not make it a final-medium concentration. Keep stock composition
    and the separate receiving addition, without inventing a final-medium dilution."}]},{"quantity_id":"q24","label":"Na2SeO3
    x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.003","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.003 G_PER_L equals the explicit current DSMZ provider g_l for Na2SeO3
    x 5 H2O in Selenite-tungstate solution. This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution.","source_stage":"DSMZ985 Selenite-tungstate
    solution; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 58-58","quote":"Na2SeO3 x 5 H2O                             3.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\":
    0.0114062,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The
    stored 0.003 G_PER_L equals the explicit current DSMZ provider g_l for Na2SeO3
    x 5 H2O in Selenite-tungstate solution. This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The
    stored 0.003 G_PER_L equals the explicit current DSMZ provider g_l for Na2SeO3
    x 5 H2O in Selenite-tungstate solution. This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The
    stored 0.003 G_PER_L equals the explicit current DSMZ provider g_l for Na2SeO3
    x 5 H2O in Selenite-tungstate solution. This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The
    stored 0.003 G_PER_L equals the explicit current DSMZ provider g_l for Na2SeO3
    x 5 H2O in Selenite-tungstate solution. This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."}]},{"quantity_id":"q25","label":"Na2WO4 x
    2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.004 G_PER_L equals the explicit current DSMZ provider g_l for Na2WO4
    x 2 H2O in Selenite-tungstate solution. This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution.","source_stage":"DSMZ985 Selenite-tungstate
    solution; KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 59-59","quote":"Na2WO4 x 2 H2O                              4.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\":
    0.0121267,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The
    stored 0.004 G_PER_L equals the explicit current DSMZ provider g_l for Na2WO4
    x 2 H2O in Selenite-tungstate solution. This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The
    stored 0.004 G_PER_L equals the explicit current DSMZ provider g_l for Na2WO4
    x 2 H2O in Selenite-tungstate solution. This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The
    stored 0.004 G_PER_L equals the explicit current DSMZ provider g_l for Na2WO4
    x 2 H2O in Selenite-tungstate solution. This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The
    stored 0.004 G_PER_L equals the explicit current DSMZ provider g_l for Na2WO4
    x 2 H2O in Selenite-tungstate solution. This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."}]},{"quantity_id":"q26","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Biotin in
    Wolin''s vitamin solution (10x). This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution.","source_stage":"DSMZ985 Wolin''s vitamin solution (10x);
    KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 64-64","quote":"Biotin                                     20.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The
    stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Biotin in
    Wolin''s vitamin solution (10x). This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The
    stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Biotin in
    Wolin''s vitamin solution (10x). This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The
    stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Biotin in
    Wolin''s vitamin solution (10x). This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The
    stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Biotin in
    Wolin''s vitamin solution (10x). This is stock strength flattened into main ingredients;
    numerical agreement with a stock does not make it a final-medium concentration.
    Keep stock composition and the separate receiving addition, without inventing
    a final-medium dilution."}]},{"quantity_id":"q27","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Folic acid
    in Wolin''s vitamin solution (10x). This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution.","source_stage":"DSMZ985 Wolin''s vitamin solution
    (10x); KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 65-65","quote":"Folic acid                                 20.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The
    stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Folic acid
    in Wolin''s vitamin solution (10x). This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The
    stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Folic acid
    in Wolin''s vitamin solution (10x). This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The
    stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Folic acid
    in Wolin''s vitamin solution (10x). This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The
    stored 0.02 G_PER_L equals the explicit current DSMZ provider g_l for Folic acid
    in Wolin''s vitamin solution (10x). This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."}]},{"quantity_id":"q28","label":"Pyridoxine
    hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for Pyridoxine
    hydrochloride in Wolin''s vitamin solution (10x). This is stock strength flattened
    into main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution.","source_stage":"DSMZ985 Wolin''s vitamin solution
    (10x); KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 66-66","quote":"Pyridoxine hydrochloride                  100.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The
    stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for Pyridoxine
    hydrochloride in Wolin''s vitamin solution (10x). This is stock strength flattened
    into main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The
    stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for Pyridoxine
    hydrochloride in Wolin''s vitamin solution (10x). This is stock strength flattened
    into main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The
    stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for Pyridoxine
    hydrochloride in Wolin''s vitamin solution (10x). This is stock strength flattened
    into main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The
    stored 0.1 G_PER_L equals the explicit current DSMZ provider g_l for Pyridoxine
    hydrochloride in Wolin''s vitamin solution (10x). This is stock strength flattened
    into main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."}]},{"quantity_id":"q29","label":"Thiamine
    HCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Thiamine
    HCl in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution.","source_stage":"DSMZ985 Wolin''s vitamin solution
    (10x); KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 67-67","quote":"Thiamine HCl                               50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Thiamine
    HCl in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Thiamine
    HCl in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Thiamine
    HCl in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Thiamine
    HCl in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."}]},{"quantity_id":"q30","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Riboflavin
    in Wolin''s vitamin solution (10x). This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution.","source_stage":"DSMZ985 Wolin''s vitamin solution
    (10x); KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 68-68","quote":"Riboflavin                                 50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Riboflavin
    in Wolin''s vitamin solution (10x). This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Riboflavin
    in Wolin''s vitamin solution (10x). This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Riboflavin
    in Wolin''s vitamin solution (10x). This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Riboflavin
    in Wolin''s vitamin solution (10x). This is stock strength flattened into main
    ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."}]},{"quantity_id":"q31","label":"Nicotinic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Nicotinic
    acid in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution.","source_stage":"DSMZ985 Wolin''s vitamin solution
    (10x); KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 69-69","quote":"Nicotinic acid                             50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Nicotinic
    acid in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Nicotinic
    acid in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Nicotinic
    acid in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Nicotinic
    acid in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."}]},{"quantity_id":"q32","label":"Calcium D-(+)-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Calcium
    D-(+)-pantothenate in Wolin''s vitamin solution (10x). This is stock strength
    flattened into main ingredients; numerical agreement with a stock does not make
    it a final-medium concentration. Keep stock composition and the separate receiving
    addition, without inventing a final-medium dilution. The primary explicitly supplies
    the D-calcium salt, consistent with the current stereochemical CHEBI:31345 object;
    no hemicalcium or full-salt mass conversion is proposed.","source_stage":"DSMZ985
    Wolin''s vitamin solution (10x); KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 70-70","quote":"Calcium D-(+)-pantothenate                 50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Calcium
    D-(+)-pantothenate in Wolin''s vitamin solution (10x). This is stock strength
    flattened into main ingredients; numerical agreement with a stock does not make
    it a final-medium concentration. Keep stock composition and the separate receiving
    addition, without inventing a final-medium dilution. The primary explicitly supplies
    the D-calcium salt, consistent with the current stereochemical CHEBI:31345 object;
    no hemicalcium or full-salt mass conversion is proposed."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Calcium
    D-(+)-pantothenate in Wolin''s vitamin solution (10x). This is stock strength
    flattened into main ingredients; numerical agreement with a stock does not make
    it a final-medium concentration. Keep stock composition and the separate receiving
    addition, without inventing a final-medium dilution. The primary explicitly supplies
    the D-calcium salt, consistent with the current stereochemical CHEBI:31345 object;
    no hemicalcium or full-salt mass conversion is proposed."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Calcium
    D-(+)-pantothenate in Wolin''s vitamin solution (10x). This is stock strength
    flattened into main ingredients; numerical agreement with a stock does not make
    it a final-medium concentration. Keep stock composition and the separate receiving
    addition, without inventing a final-medium dilution. The primary explicitly supplies
    the D-calcium salt, consistent with the current stereochemical CHEBI:31345 object;
    no hemicalcium or full-salt mass conversion is proposed."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for Calcium
    D-(+)-pantothenate in Wolin''s vitamin solution (10x). This is stock strength
    flattened into main ingredients; numerical agreement with a stock does not make
    it a final-medium concentration. Keep stock composition and the separate receiving
    addition, without inventing a final-medium dilution. The primary explicitly supplies
    the D-calcium salt, consistent with the current stereochemical CHEBI:31345 object;
    no hemicalcium or full-salt mass conversion is proposed."}]},{"quantity_id":"q33","label":"Vitamin
    B12","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.001","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.001 G_PER_L equals the explicit current DSMZ provider g_l for Vitamin
    B12 in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution.","source_stage":"DSMZ985 Wolin''s vitamin solution
    (10x); KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 71-71","quote":"Vitamin B12                                 1.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The
    stored 0.001 G_PER_L equals the explicit current DSMZ provider g_l for Vitamin
    B12 in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The
    stored 0.001 G_PER_L equals the explicit current DSMZ provider g_l for Vitamin
    B12 in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The
    stored 0.001 G_PER_L equals the explicit current DSMZ provider g_l for Vitamin
    B12 in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The
    stored 0.001 G_PER_L equals the explicit current DSMZ provider g_l for Vitamin
    B12 in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."}]},{"quantity_id":"q34","label":"p-Aminobenzoic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for p-Aminobenzoic
    acid in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution.","source_stage":"DSMZ985 Wolin''s vitamin solution
    (10x); KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 72-72","quote":"p-Aminobenzoic acid                        50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for p-Aminobenzoic
    acid in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for p-Aminobenzoic
    acid in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for p-Aminobenzoic
    acid in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for p-Aminobenzoic
    acid in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution."}]},{"quantity_id":"q35","label":"(DL)-alpha-Lipoic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[34].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[34].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[34].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[34].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for (DL)-alpha-Lipoic
    acid in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution. Generic non-stereospecific CHEBI:16494 does
    not contradict the explicit DL designation.","source_stage":"DSMZ985 Wolin''s
    vitamin solution (10x); KOMODO identities separately bounded","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 73-73","quote":"(DL)-alpha-Lipoic acid                     50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ingredients[34].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for (DL)-alpha-Lipoic
    acid in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution. Generic non-stereospecific CHEBI:16494 does
    not contradict the explicit DL designation."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ingredients[34].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for (DL)-alpha-Lipoic
    acid in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution. Generic non-stereospecific CHEBI:16494 does
    not contradict the explicit DL designation."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ingredients[34].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for (DL)-alpha-Lipoic
    acid in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution. Generic non-stereospecific CHEBI:16494 does
    not contradict the explicit DL designation."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ingredients[34].concentration","decision":"conflict","rationale":"The
    stored 0.05 G_PER_L equals the explicit current DSMZ provider g_l for (DL)-alpha-Lipoic
    acid in Wolin''s vitamin solution (10x). This is stock strength flattened into
    main ingredients; numerical agreement with a stock does not make it a final-medium
    concentration. Keep stock composition and the separate receiving addition, without
    inventing a final-medium dilution. Generic non-stereospecific CHEBI:16494 does
    not contradict the explicit DL designation."}]},{"quantity_id":"q36","label":"Trace
    element solution SL-10 receiving addition","local_fields":[],"decision":"evidence_only","rationale":"The
    exact primary supplies this 1 ml stock addition; it is absent as a structured
    receiving stock. Preserve its separate identity and batch dose. Neither the printed
    input water nor the provider volume establishes measured final volume.","source_stage":"DSM985
    receiving batch only","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 10-10","quote":"Trace element solution SL-10                               1.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q37","label":"Selenite-tungstate
    solution receiving addition","local_fields":[],"decision":"evidence_only","rationale":"The
    exact primary supplies this 1 ml stock addition; it is absent as a structured
    receiving stock. Preserve its separate identity and batch dose. Neither the printed
    input water nor the provider volume establishes measured final volume.","source_stage":"DSM985
    receiving batch only","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 11-11","quote":"Selenite-tungstate solution                                1.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q38","label":"Wolin''s vitamin
    solution (10x) receiving addition","local_fields":[],"decision":"evidence_only","rationale":"The
    exact primary supplies this 1 ml stock addition; it is absent as a structured
    receiving stock. Preserve its separate identity and batch dose. Neither the printed
    input water nor the provider volume establishes measured final volume.","source_stage":"DSM985
    receiving batch only","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 17-17","quote":"Wolin''s vitamin solution (10x)                             1.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\":
    15,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q39","label":"Main sol. 985 water","local_fields":[],"decision":"evidence_only","rationale":"Retain
    this exact solvent input separately. SL-10 alone has an explicit final make-up
    instruction, assessed in the stock-preparation row; the other printed water inputs
    are not independent final-volume measurements.","source_stage":"Main sol. 985","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 19-19","quote":"Distilled water                                         1000.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[0].recipe[16]","quote":"{\n                        \"recipe_order\":
    17,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q40","label":"Trace element solution
    SL-10 water","local_fields":[],"decision":"evidence_only","rationale":"Retain
    this exact solvent input separately. SL-10 alone has an explicit final make-up
    instruction, assessed in the stock-preparation row; the other printed water inputs
    are not independent final-volume measurements.","source_stage":"Trace element
    solution SL-10","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 42-42","quote":"Distilled water                                           990.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 990,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q41","label":"Selenite-tungstate
    solution water","local_fields":[],"decision":"evidence_only","rationale":"Retain
    this exact solvent input separately. SL-10 alone has an explicit final make-up
    instruction, assessed in the stock-preparation row; the other printed water inputs
    are not independent final-volume measurements.","source_stage":"Selenite-tungstate
    solution","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 60-60","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q42","label":"Wolin''s vitamin
    solution (10x) water","local_fields":[],"decision":"evidence_only","rationale":"Retain
    this exact solvent input separately. SL-10 alone has an explicit final make-up
    instruction, assessed in the stock-preparation row; the other printed water inputs
    are not independent final-volume measurements.","source_stage":"Wolin''s vitamin
    solution (10x)","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 74-74","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative
    text"},{"evidence_id":"api985","reference":"https://mediadive.dsmz.de/rest/medium/985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api985.bin","raw_sha256":"a59f34ea1be73d0c9a1283af2a42dbfae4531bf363e999b4ec95d10d896dc7c6","text_sha256":"30da5c73f120a552b772b904a4385d1e50f0ed866b999ce3802246eacb7e1fe2","accessed_at":"2026-10-28T16:12:45.915612Z","locator":"data.solutions[3].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q43","label":"DSM basal preparation
    and numeric controls","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve
    ingredients (except carbonate, nitrate, acetate, vitamins and sulfide), then sparge
    medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic.
    Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum
    vials and autoclave. Add vitamins (sterilized by filtration), nitrate, acetate
    and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and
    carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2
    gas atmosphere. The pH of the complete medium should be 6.5 -7.0."}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve
    ingredients (except carbonate, nitrate, acetate, vitamins and sulfide), then sparge
    medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic.
    Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum
    vials and autoclave. Add vitamins (sterilized by filtration), nitrate, acetate
    and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and
    carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2
    gas atmosphere. The pH of the complete medium should be 6.5 -7.0."}}],"decision":"evidence_only","rationale":"The
    existing full paragraph correctly retains the primary exclusions, 80/20 gas mixture,
    30–45 min sparging, later 100% nitrogen stock context, filtration and pH 6.5–7.0.
    AUTOCLAVE labels the whole multi-action paragraph, so structure should separate
    actions while preserving the supported text. No autoclave temperature/time or
    missing late-stock strength/addition volume is supplied. Do not transfer these
    conditions to an unresolved KOMODO variant.","source_stage":"DSM985 only; main
    and later-stock stages distinguished","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 21-27","quote":"Dissolve ingredients (except carbonate, nitrate, acetate,
    vitamins and sulfide), then sparge\nmedium with 80% N2 and 20% CO2 gas mixture
    for 30 - 45 min to make it anoxic. Dispense\nmedium under same gas atmosphere
    into anoxic Hungate-type tubes or serum vials and\nautoclave. Add vitamins (sterilized
    by filtration), nitrate, acetate and sulfide from sterile\nanoxic stock solutions
    prepared under 100% N2 gas and carbonate from a sterile anoxic\nstock solution
    prepared under 80% N2 and 20% CO2 gas atmosphere. The pH of the\ncomplete medium
    should be 6.5 -7.0.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The
    existing full paragraph correctly retains the primary exclusions, 80/20 gas mixture,
    30–45 min sparging, later 100% nitrogen stock context, filtration and pH 6.5–7.0.
    AUTOCLAVE labels the whole multi-action paragraph, so structure should separate
    actions while preserving the supported text. No autoclave temperature/time or
    missing late-stock strength/addition volume is supplied. Do not transfer these
    conditions to an unresolved KOMODO variant."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The
    existing full paragraph correctly retains the primary exclusions, 80/20 gas mixture,
    30–45 min sparging, later 100% nitrogen stock context, filtration and pH 6.5–7.0.
    AUTOCLAVE labels the whole multi-action paragraph, so structure should separate
    actions while preserving the supported text. No autoclave temperature/time or
    missing late-stock strength/addition volume is supplied. Do not transfer these
    conditions to an unresolved KOMODO variant."}]},{"quantity_id":"q44","label":"SL-10
    final make-up and stock-local preparation","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally make up to 1000.00 ml."}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally make up to 1000.00 ml."}}],"decision":"conflict","rationale":"The retained
    wording is exactly supported for SL-10: dissolve iron in HCl first and finally
    make up to 1000 ml. It is misplaced as an unqualified main-medium step; this final
    volume must stay within the SL-10 stock. The primary 990 ml water input and 10
    ml acid input remain separate.","source_stage":"SL-10 stock only","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 32-45","quote":"Trace element solution SL-10 (from medium 320)\n   HCl (25%)                                                  10.00      ml\n   FeCl2
    x 4 H2O                                               1.50       g\n   ZnCl2                                                      70.00      mg\n   MnCl2
    x 4 H2O                                             100.00      mg\n   H3BO3                                                       6.00      mg\n   CoCl2
    x 6 H2O                                             190.00      mg\n   CuCl2 x
    2 H2O                                               2.00      mg\n   NiCl2 x 6
    H2O                                              24.00      mg\n   Na2MoO4 x 2
    H2O                                            36.00      mg\n   Distilled water                                           990.00      ml\n\nFirst
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"preparation_steps[1]","decision":"conflict","rationale":"The
    retained wording is exactly supported for SL-10: dissolve iron in HCl first and
    finally make up to 1000 ml. It is misplaced as an unqualified main-medium step;
    this final volume must stay within the SL-10 stock. The primary 990 ml water input
    and 10 ml acid input remain separate."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"preparation_steps[1]","decision":"conflict","rationale":"The
    retained wording is exactly supported for SL-10: dissolve iron in HCl first and
    finally make up to 1000 ml. It is misplaced as an unqualified main-medium step;
    this final volume must stay within the SL-10 stock. The primary 990 ml water input
    and 10 ml acid input remain separate."}]},{"quantity_id":"q45","label":"pH range","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ph_range","stored":{"min":6.5,"max":7.0}},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ph_range","stored":{"min":6.5,"max":7.0}},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ph_range","stored":{"min":6.5,"max":7.0}},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ph_range","stored":{"min":6.5,"max":7.0}}],"decision":"mixed","rationale":"DSM985
    primary and current KOMODO985 both report 6.5–7.0, supporting the generated/DSM/base
    values independently. Exact 985.1 is unavailable, so that strain-wrapper value
    is not independently verified.","source_stage":"Separate DSM985 and KOMODO985
    sources; not strain transfer","sources":[{"evidence_id":"dsmz985","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium985.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz985.bin","raw_sha256":"54a9af0fedb99ebdf471850da8ad857eccb42b4e71f32ea12d634ec47ae2d11e","text_sha256":"81b7431a559eb1136b4b4adedd5316f9a13ec3ac3d9c0f3877fb59b22acd0e8b","accessed_at":"2026-10-28T16:12:45.024127Z","locator":"dsmz985.txt
    lines 26-27","quote":"stock solution prepared under 80% N2 and 20% CO2 gas atmosphere.
    The pH of the\ncomplete medium should be 6.5 -7.0.","quote_basis":"derivative
    text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 10-23","quote":"Medium: TEPIDIBACTER medium\nMedium features\nID:\n985\nName:\nTEPIDIBACTER
    medium\nPH Info:\n6.5 - 7.0\nIs Complex:\ntrue\nIs Aerobic:\ntrue\nIs SubMedium:\nfalse","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"DSM985
    primary and current KOMODO985 both report 6.5–7.0, supporting the generated/DSM/base
    values independently. Exact 985.1 is unavailable, so that strain-wrapper value
    is not independently verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"DSM985
    primary and current KOMODO985 both report 6.5–7.0, supporting the generated/DSM/base
    values independently. Exact 985.1 is unavailable, so that strain-wrapper value
    is not independently verified."},{"path":"data/normalized_yaml/bacterial/for_dsm_19306.yaml","field_path":"ph_range","decision":"unsupported","rationale":"DSM985
    primary and current KOMODO985 both report 6.5–7.0, supporting the generated/DSM/base
    values independently. Exact 985.1 is unavailable, so that strain-wrapper value
    is not independently verified."},{"path":"data/normalized_yaml/bacterial/tepidibacter_medium.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"DSM985
    primary and current KOMODO985 both report 6.5–7.0, supporting the generated/DSM/base
    values independently. Exact 985.1 is unavailable, so that strain-wrapper value
    is not independently verified."}]},{"quantity_id":"q46","label":"KOMODO985 source
    row: NaHCO3","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 34-38","quote":"NaHCO3\nsodium bicarbonate\nSEED-cpd00242#cpd00971#cpd09249#\n4.95\n0.06","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q47","label":"KOMODO985 source
    row: D-Ca-pantothenate","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 39-43","quote":"D-Ca-pantothenate\nD-Ca-pantothenate\nSEED-cpd00063#cpd00644##\n4.95E-5\n1.92E-7","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q48","label":"KOMODO985 source
    row: Lipoic acid","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 44-48","quote":"Lipoic acid\nLipoic acid\nSEED-cpd00541###\n4.95E-5\n2.41E-7","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q49","label":"KOMODO985 source
    row: Na2S x 9 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 49-53","quote":"Na2S x 9 H2O\nSodium sulfide hydrate\nSEED-cpd00239#cpd00971##\n0.49\n0.00","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q50","label":"KOMODO985 source
    row: CO2","local_fields":[],"decision":"not_quantified","rationale":"Current KOMODO985
    declares the displayed gram amounts per litre. This is a source-version observation,
    not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form
    and source digits; the separate model-derived SEED aggregation and rounded molar
    column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985
    complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 54-58","quote":"CO2\nCO2\nSEED-cpd00011###\nnull\nnull","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q51","label":"KOMODO985 source
    row: Nicotinic acid","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 59-63","quote":"Nicotinic acid\nNiacin\nSEED-cpd00218###\n4.95E-5\n4.05E-7","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q52","label":"KOMODO985 source
    row: Riboflavin","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 64-68","quote":"Riboflavin\nRiboflavin\nSEED-cpd00220###\n4.95E-5\n1.32E-7","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q53","label":"KOMODO985 source
    row: MgCl2 x 6 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 69-73","quote":"MgCl2 x 6 H2O\nMagnesium chloride\nSEED-cpd00099#cpd00254#cpd04877#\n3.96\n0.02","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q54","label":"KOMODO985 source
    row: K2HPO4","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 74-78","quote":"K2HPO4\ndi Potassium hydrogen phosphate\nSEED-cpd00009#cpd00205##\n0.18\n0.00","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q55","label":"KOMODO985 source
    row: CoCl2 x 6 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 79-83","quote":"CoCl2 x 6 H2O\nCoCl2\nSEED-cpd00099#cpd00149##\n1.87E-4\n7.88E-7","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q56","label":"KOMODO985 source
    row: CuCl2 x 2 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 84-88","quote":"CuCl2 x 2 H2O\nCuCl2\nSEED-cpd00058#cpd00099##\n1.97E-6\n1.17E-8","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q57","label":"KOMODO985 source
    row: Vitamin B12","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 89-93","quote":"Vitamin B12\nCoenzyme B12\nSEED-cpd00166###\n9.89E-7\n6.26E-10","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q58","label":"KOMODO985 source
    row: FeCl2 x 4 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 94-98","quote":"FeCl2 x 4 H2O\nIron chloride\nSEED-cpd00099#cpd10516##\n1.48E-3\n7.45E-6","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q59","label":"KOMODO985 source
    row: Fe(NH4)2(SO4)2 x 7 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 99-103","quote":"Fe(NH4)2(SO4)2 x 7 H2O\n(NH4)2Fe(SO4)2\nSEED-cpd00013#cpd00048#cpd10515#\n0.02\n0.00","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q60","label":"KOMODO985 source
    row: Folic acid","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 104-108","quote":"Folic acid\nFolic acid\nSEED-cpd00393###\n1.98E-5\n4.51E-8","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q61","label":"KOMODO985 source
    row: Thiamine-HCl x 2 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 109-113","quote":"Thiamine-HCl x 2 H2O\nThiamine-HCl\nSEED-cpd00099#cpd00305##\n4.95E-5\n1.47E-7","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q62","label":"KOMODO985 source
    row: HCl","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985
    declares the displayed gram amounts per litre. This is a source-version observation,
    not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form
    and source digits; the separate model-derived SEED aggregation and rounded molar
    column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985
    complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 114-118","quote":"HCl\nHCl\nSEED-cpd00099###\n6.65E-4\n1.90E-5","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q63","label":"KOMODO985 source
    row: ZnCl2","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 119-123","quote":"ZnCl2\nZnCl2\nSEED-cpd00034#cpd00099##\n6.91E-5\n5.12E-7","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q64","label":"KOMODO985 source
    row: MnCl2 x 4 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 124-128","quote":"MnCl2 x 4 H2O\nMnCl2\nSEED-cpd00030#cpd00099##\n9.87E-5\n4.99E-7","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q65","label":"KOMODO985 source
    row: Yeast extract","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 129-133","quote":"Yeast extract\nYeast extract\nrich-peptone#\n0.20\nnull","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q66","label":"KOMODO985 source
    row: Pyridoxine HCl","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 134-138","quote":"Pyridoxine HCl\nPyridoxine HCl\nSEED-cpd00099#cpd00263##\n9.89E-5\n4.85E-7","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q67","label":"KOMODO985 source
    row: Na2MoO4 x 2 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 139-143","quote":"Na2MoO4 x 2 H2O\nNa2MoO4\nSEED-cpd00971#cpd11145##\n3.55E-5\n1.47E-7","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q68","label":"KOMODO985 source
    row: KCl","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985
    declares the displayed gram amounts per litre. This is a source-version observation,
    not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form
    and source digits; the separate model-derived SEED aggregation and rounded molar
    column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985
    complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 144-148","quote":"KCl\nKCl\nSEED-cpd00099#cpd00205##\n0.34\n0.00","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q69","label":"KOMODO985 source
    row: CaCl2","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 149-153","quote":"CaCl2\nCalcium chloride\nSEED-cpd00063#cpd00099##\n0.11\n0.00","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q70","label":"KOMODO985 source
    row: Resazurin","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 154-158","quote":"Resazurin\nResazurin\nSEED-cpd08053###\n9.89E-4\n4.32E-6","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q71","label":"KOMODO985 source
    row: p-Aminobenzoic acid","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 159-163","quote":"p-Aminobenzoic acid\np Aminobenzoic acid (PABA)\nSEED-cpd00443###\n4.95E-5\n3.64E-7","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q72","label":"KOMODO985 source
    row: H2O","local_fields":[],"decision":"not_quantified","rationale":"Current KOMODO985
    declares the displayed gram amounts per litre. This is a source-version observation,
    not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form
    and source digits; the separate model-derived SEED aggregation and rounded molar
    column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985
    complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 164-168","quote":"H2O\nH2O\nSEED-cpd00001###\nnull\nnull","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q73","label":"KOMODO985 source
    row: N2","local_fields":[],"decision":"not_quantified","rationale":"Current KOMODO985
    declares the displayed gram amounts per litre. This is a source-version observation,
    not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form
    and source digits; the separate model-derived SEED aggregation and rounded molar
    column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985
    complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 169-173","quote":"N2\nN2\nSEED-cpd00528###\nnull\nnull","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q74","label":"KOMODO985 source
    row: Distilled water","local_fields":[],"decision":"not_quantified","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 174-178","quote":"Distilled water\nH2O\nSEED-cpd00001###\nnull\nnull","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q75","label":"KOMODO985 source
    row: casein","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 179-183","quote":"casein\nCasein\nSEED-cpd11656###\n9.89\n0.05","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q76","label":"KOMODO985 source
    row: Biotin","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 184-188","quote":"Biotin\nBiotin\nSEED-cpd00104###\n1.98E-5\n8.14E-8","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q77","label":"KOMODO985 source
    row: NH4Cl","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 189-193","quote":"NH4Cl\nAmmonium chloride\nSEED-cpd00013#cpd00099##\n0.25\n0.00","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q78","label":"KOMODO985 source
    row: NiCl2 x 6 H2O","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 194-198","quote":"NiCl2 x 6 H2O\nNiCl2\nSEED-cpd00099#cpd00244##\n2.37E-5\n9.95E-8","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q79","label":"KOMODO985 source
    row: H3BO3","local_fields":[],"decision":"evidence_only","rationale":"Current
    KOMODO985 declares the displayed gram amounts per litre. This is a source-version
    observation, not permission to replace DSM985 or apply it to 985.1. Preserve the
    exact component/form and source digits; the separate model-derived SEED aggregation
    and rounded molar column are not chemically revalidated here. Null gas/water entries
    remain unquantified.","source_stage":"KOMODO985 complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 199-203","quote":"H3BO3\nBoric acid\nSEED-cpd09225###\n5.92E-6\n9.55E-8","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q80","label":"KOMODO985 source
    row: NaCl","local_fields":[],"decision":"evidence_only","rationale":"Current KOMODO985
    declares the displayed gram amounts per litre. This is a source-version observation,
    not permission to replace DSM985 or apply it to 985.1. Preserve the exact component/form
    and source digits; the separate model-derived SEED aggregation and rounded molar
    column are not chemically revalidated here. Null gas/water entries remain unquantified.","source_stage":"KOMODO985
    complete compound table only","sources":[{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 27-33","quote":"Metabolites list\nCompounds in the medium listed by their
    compound names. Gram & Mol amounts are per Liter of medium. Trace metabolites
    & gases usually do not have amounts\nName\nSemi unique name\nUnique Name\nGram
    Amount\nMol Amount","quote_basis":"derivative text"},{"evidence_id":"komodo985","reference":"https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=985","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/komodo985.bin","raw_sha256":"366e7d3ca01eb5bcc5929f25e3c08fe50f89ccde64992b9ddaad8493f85edbaf","text_sha256":"ac22b468b888e1f1047beb52a768df29ee3bcf0d50af385f12c830bf41d7cd9e","accessed_at":"2026-10-28T16:12:46.724943Z","locator":"komodo985.txt
    lines 204-208","quote":"NaCl\nNaCl\nSEED-cpd00099#cpd00971##\n17.80\n0.31","quote_basis":"derivative
    text"}],"layer_assessments":[]}],"document_scopes":{"data/merge_yaml/merged/DEFERRIBACTER_AUTOTROPHICUS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml":null,"data/normalized_yaml/bacterial/for_dsm_19306.yaml":null,"data/normalized_yaml/bacterial/tepidibacter_medium.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All asserted ontology objects and exact current MIM links are inventoried.
    Current labels agree, but sodium-resazurin salt and nickel hexahydrate are chemically
    mismatched despite valid IDs. D-calcium pantothenate stereochemistry, ferrous
    ammonium sulfate heptahydrate and generic lipoic acid are compatible with the
    primary. Cobalt/nickel preferred REJECTED rows and MAPPED synonym alternatives
    remain explicitly distinct; no chemical-form endorsement follows from row status
    alone.
  target_ids:
  - CultureMech:002167
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: All seven scoped reports and exact selected parent rows were read with
    the complete current histories. Current raw/decoded excerpt equality authenticates
    content only, not historical access events. October stock-conflict findings remain
    relevant; September topology repair reflects the copied local signature and is
    contradicted by the freshly recovered KOMODO985 formulation. Current conservative
    merger would retain scientific differences, and the current importer no longer
    flattens these stocks. Original malformed/naive events must remain append-only.
  target_ids:
  - CultureMech:002167
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-002167-source-variant-conflation
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile DSM985, KOMODO985 and the DSM19306 wrapper before merging
  description: 'The generated record combines three source identities and retains
    an obsolete SOURCE_DUPLICATE parent to the DSM19306 wrapper. September owners
    distinguish a base and strain wrapper, but still declare DSM985 a duplicate from
    a copied local signature. Fresh exact KOMODO985 is a different formula: bicarbonate
    and casein occur, nitrate/acetate are absent from its compound table, stock-derived
    rates and thiamine hydrate differ, and its aerobic flag conflicts with DSM985
    anoxic preparation. Do not collapse these versions or silently replace either.
    DSM19306 currently identifies Clostridium tepidiprofundi; its catalogue identity
    does not prove this historical medium variant or growth. Preserve the original
    resolver/repair events and append a source-backed reconciliation. Regenerate only
    after owner identity and relationships are resolved.'
  target_ids:
  - CultureMech:002167
  field_paths:
  - media_term
  - synonyms
  - merged_from
  - parent_media
  - variant_relationship
  - variant_modifications
  - notes
  evidence_ids:
  - target
  - owner
  - owner-2
  - owner-3
  - dsmz985
  - api985
  - komodo985
  - komodo985dot1
  - dsm19306
  - writer-resolver
  - writer-repair
  - writer-formulation
  rule_id: review-yaml-record/custom-source-variant-conflation
  native_severity: P2
  normalization_reason: 'Custom identity rule: material source identity, supplied
    form or stage error requires curation; normalized major.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_19306.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/tepidibacter_medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-002167-stock-stage-flattening
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore three stock scopes and their receiving doses
  description: All four layers place 22 SL-10, selenite–tungstate and vitamin stock
    constituents directly among main ingredients at full stock strength. Preserve
    their exact stock quantities and separate receiving additions rather than endorsing
    them as final-medium rates. Retain the supported DSM basal provider rates with
    their explicit normalization basis; do not substitute a presumed one-litre denominator.
    Add the primary solvent inputs and sodium-resazurin stock strength/dose in their
    correct scopes. The current importer already separates primary compounds and stocks;
    current behavior does not authenticate or justify the older flattened output.
  target_ids:
  - CultureMech:002167
  field_paths:
  - ingredients
  - solutions
  - evidence
  evidence_ids:
  - quantities
  - dsmz985
  - api985
  - writer-mediadive
  rule_id: review-yaml-record/custom-stock-stage-flattening
  native_severity: P2
  normalization_reason: 'Custom quantity rule: material source identity, supplied
    form or stage error requires curation; normalized major.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_19306.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/tepidibacter_medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-002167-preparation-stage-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Keep the SL-10 make-up separate from main-medium preparation
  description: The DSM owner and generated target retain useful complete source preparation
    text, but the SL-10 instruction to make up to 1000 ml sits at main preparation_steps[1],
    and the entire basal multi-action paragraph is labelled AUTOCLAVE. Place the stock
    instruction within its stock context and distinguish supported sequential actions
    without discarding the existing gas, duration, exclusion, filtration or pH controls.
    Missing autoclave settings and late-stock strengths/doses remain unknown. KOMODO
    owners lack this DSM text and have conflicting source atmosphere metadata; first
    resolve their variant identity rather than copying DSM conditions into them.
  target_ids:
  - CultureMech:002167
  field_paths:
  - preparation_steps
  - solutions
  - evidence
  evidence_ids:
  - target
  - owner
  - dsmz985
  - api985
  - komodo985
  - writer-mediadive
  rule_id: review-yaml-record/custom-preparation-stage-scope
  native_severity: P2
  normalization_reason: 'Custom completeness rule: material source identity, supplied
    form or stage error requires curation; normalized major.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_19306.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/tepidibacter_medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-002167-supplied-form-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Correct the sodium-resazurin and nickel-hydrate assertions
  description: Sodium resazurin is currently assigned neutral CHEBI:8806; the exact
    primary and API specify the sodium salt. NiCl2 x 6 H2O is assigned anhydrous CHEBI:34887
    in both primary and secondary slots. Reconcile these supplied forms to exact current
    ontology objects and canonical labels while retaining supported stock amounts
    and source distinctions. The MIM sodium-resazurin synonym does not override the
    neutral ontology formula. The nickel preferred row is REJECTED while an exact
    synonym maps to 53542; neither status alone validates a replacement. Calcium D-pantothenate,
    ferrous ammonium sulfate heptahydrate and non-stereospecific lipoic acid are explicitly
    retained as compatible with their DSM source forms.
  target_ids:
  - CultureMech:002167
  field_paths:
  - ingredients[8].term
  - ingredients[20].term
  - ingredients[20].mediaingredientmech_chebi_term
  evidence_ids:
  - dsmz985
  - api985
  - chebi8806
  - chebi34887
  - groundings
  rule_id: review-yaml-record/custom-supplied-form-grounding
  native_severity: P2
  normalization_reason: 'Custom grounding rule: material source identity, supplied
    form or stage error requires curation; normalized major.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_19306.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/tepidibacter_medium.yaml
    role: maintained normalized contributor
- finding_id: f5
  issue_key: culturemech-002167-grounding-linkage-followup
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve remaining bounded secondary-link gaps
  description: KNO3 retains MediaIngredientMech:000170, absent from the exact packaged
    current snapshot, while its primary CHEBI:63043 remains correct. Yeast extract
    has no primary or secondary term and sodium resazurin/calcium pantothenate lack
    secondary links. Review current exact MIM candidates without treating snapshot
    absence as historical invalidity or treating synonym rows as supplied-form proof.
    The scientific form errors are separately tracked; these linkage gaps do not justify
    changing supported amounts.
  target_ids:
  - CultureMech:002167
  field_paths:
  - ingredients[10].mediaingredientmech_term
  - ingredients[7]
  - ingredients[8]
  - ingredients[31]
  evidence_ids:
  - groundings
  - mim
  - mim-meta
  - chebi63043
  rule_id: review-yaml-record/custom-grounding-linkage-followup
  native_severity: P3
  normalization_reason: 'Custom grounding rule: bounded linkage or event/claim provenance
    gap; normalized minor. No false attribution to a narrower native P-number rule.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_19306.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/tepidibacter_medium.yaml
    role: maintained normalized contributor
- finding_id: f6
  issue_key: culturemech-002167-claim-history-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Attach scoped claims and preserve malformed historical events
  description: No retained ingredient claim authenticates these current quantities;
    all source support found here is newly linked review evidence. The complete seven
    reports contain prior conflict/unsupported decisions and derivative source excerpts,
    not proof of completed source curation. Both KOMODO owners retain malformed .fZ
    import timestamps and timezone-naive resolver timestamps. Keep original events
    byte-preserved; append verified context or corrections only when authoritative
    event provenance is recovered. September topology updates and ingredients_curated
    flags do not certify current external formula equality.
  target_ids:
  - CultureMech:002167
  field_paths:
  - evidence
  - curation_history
  - data/normalized_yaml/bacterial/for_dsm_19306.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/for_dsm_19306.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/tepidibacter_medium.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/tepidibacter_medium.yaml::curation_history[1].timestamp
  evidence_ids:
  - old-reports
  - old-claims
  - history
  - writer-repair
  rule_id: review-yaml-record/custom-claim-history-provenance
  native_severity: P3
  normalization_reason: 'Custom provenance rule: bounded linkage or event/claim provenance
    gap; normalized minor. No false attribution to a narrower native P-number rule.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_19306.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/tepidibacter_medium.yaml
    role: maintained normalized contributor
actions:
- action_id: a1
  description: 'The generated record combines three source identities and retains
    an obsolete SOURCE_DUPLICATE parent to the DSM19306 wrapper. September owners
    distinguish a base and strain wrapper, but still declare DSM985 a duplicate from
    a copied local signature. Fresh exact KOMODO985 is a different formula: bicarbonate
    and casein occur, nitrate/acetate are absent from its compound table, stock-derived
    rates and thiamine hydrate differ, and its aerobic flag conflicts with DSM985
    anoxic preparation. Do not collapse these versions or silently replace either.
    DSM19306 currently identifies Clostridium tepidiprofundi; its catalogue identity
    does not prove this historical medium variant or growth. Preserve the original
    resolver/repair events and append a source-backed reconciliation. Regenerate only
    after owner identity and relationships are resolved.'
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002167
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_19306.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/tepidibacter_medium.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Preserve each exact accession, source recipe and historical event; document the
    recovered KOMODO985 versus DSM985 differences and unresolved985.1 boundary.
  - Remove unsupported duplicate/equivalence claims only through reviewed maintained-owner
    curation; do not infer strain growth from catalogue identity.
  - Regenerate from reconciled owners and verify conservative merge compatibility
    and all original diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a2
  description: All four layers place 22 SL-10, selenite–tungstate and vitamin stock
    constituents directly among main ingredients at full stock strength. Preserve
    their exact stock quantities and separate receiving additions rather than endorsing
    them as final-medium rates. Retain the supported DSM basal provider rates with
    their explicit normalization basis; do not substitute a presumed one-litre denominator.
    Add the primary solvent inputs and sodium-resazurin stock strength/dose in their
    correct scopes. The current importer already separates primary compounds and stocks;
    current behavior does not authenticate or justify the older flattened output.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002167
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_19306.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/tepidibacter_medium.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a3
  description: The DSM owner and generated target retain useful complete source preparation
    text, but the SL-10 instruction to make up to 1000 ml sits at main preparation_steps[1],
    and the entire basal multi-action paragraph is labelled AUTOCLAVE. Place the stock
    instruction within its stock context and distinguish supported sequential actions
    without discarding the existing gas, duration, exclusion, filtration or pH controls.
    Missing autoclave settings and late-stock strengths/doses remain unknown. KOMODO
    owners lack this DSM text and have conflicting source atmosphere metadata; first
    resolve their variant identity rather than copying DSM conditions into them.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002167
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_19306.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/tepidibacter_medium.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a4
  description: Sodium resazurin is currently assigned neutral CHEBI:8806; the exact
    primary and API specify the sodium salt. NiCl2 x 6 H2O is assigned anhydrous CHEBI:34887
    in both primary and secondary slots. Reconcile these supplied forms to exact current
    ontology objects and canonical labels while retaining supported stock amounts
    and source distinctions. The MIM sodium-resazurin synonym does not override the
    neutral ontology formula. The nickel preferred row is REJECTED while an exact
    synonym maps to 53542; neither status alone validates a replacement. Calcium D-pantothenate,
    ferrous ammonium sulfate heptahydrate and non-stereospecific lipoic acid are explicitly
    retained as compatible with their DSM source forms.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:002167
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_19306.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/tepidibacter_medium.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a5
  description: KNO3 retains MediaIngredientMech:000170, absent from the exact packaged
    current snapshot, while its primary CHEBI:63043 remains correct. Yeast extract
    has no primary or secondary term and sodium resazurin/calcium pantothenate lack
    secondary links. Review current exact MIM candidates without treating snapshot
    absence as historical invalidity or treating synonym rows as supplied-form proof.
    The scientific form errors are separately tracked; these linkage gaps do not justify
    changing supported amounts.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:002167
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_19306.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/tepidibacter_medium.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a6
  description: No retained ingredient claim authenticates these current quantities;
    all source support found here is newly linked review evidence. The complete seven
    reports contain prior conflict/unsupported decisions and derivative source excerpts,
    not proof of completed source curation. Both KOMODO owners retain malformed .fZ
    import timestamps and timezone-naive resolver timestamps. Keep original events
    byte-preserved; append verified context or corrections only when authoritative
    event provenance is recovered. September topology updates and ingredients_curated
    flags do not certify current external formula equality.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:002167
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_autotrophicus_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_19306.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/tepidibacter_medium.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Keep original history events byte-preserved; append new verified provenance in
    a new event rather than rewriting malformed timestamps.
  - Attach exact source URLs, raw digests, original access times and scoped snippets
    without calling derivative report prose an original retrieval receipt.
  generator: Maintained-input curation and repository merge regeneration
limitations:
- The exact KOMODO985.1 recipe and catalogue request returned 403; the fresh985 recipe
  succeeded. The strain-wrapper formula is unresolved and no DSM19306 medium growth
  inference is made.
- The full KOMODO compound table is inventoried as its own source version. Model-derived
  SEED component aggregates and rounded molar values are not independently revalidated
  or transferred to curated chemistry.
- Provider mmol_l conversions are not used to validate local mass concentrations;
  hydrate-sensitive molar conversions would need their own assessment. Bare HCl25%
  has no stated percentage basis.
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
