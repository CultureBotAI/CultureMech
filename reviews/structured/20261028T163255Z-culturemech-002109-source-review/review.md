# Scientific review: DEFERRIBACTER DESULFURICANS MEDIUM

- Review: 20261028T163255Z-culturemech-002109-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T16:12:02.493019Z
- Finished UTC: 2026-10-28T16:32:55.285297Z
- Reviewer: Codex batch006_validation (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The record needs accession/variant reconciliation, separation of two stocks and mixed-stage calcium/sodium sums, stock-local preparation repair and nickel-hydrate grounding. Fresh 935a explicitly supports 1011 ml final volume and the unchanged basal rates, while 935b and 935 remain distinct sources. Exact KOMODO variants are unavailable, so completion is partial. All four original canonical checks passed without establishing scientific equivalence.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch072 index 02
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002109 | data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml | generated | deferribacter_desulfuricans_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:002109 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:002109 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:002109 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:002109 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Accession and variant scope

identity: concern. Targets: CultureMech:002109.

935a source identity is distinguishable from the 935b linked PDF and 935 base. Catalogue DSM 14813 and 14783 identities are different and do not by themselves validate either wrapper recipe.

### Basic record classification

scope: supported. Targets: CultureMech:002109.

Bacterial liquid complex/semi-defined representation is consistent with the selected 935a recipe containing yeast extract. Optional growth assertions are not inferred from names.

### Unchanged supported rates and missing attached claims

evidence: concern. Targets: CultureMech:002109.

Nine unsummed basal quantities have direct 935a primary-final-volume/provider support. Ca/Na mixed-stage sums and all stock-only root rates require correction; no existing attached quantity evidence can be credited as verified.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:002109.

170 current concentration fields are covered by 96 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b072-quantity-inventory-v1","target":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","quantity_field_count":170,"decisions":[{"quantity_id":"q1","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 7-7","quote":"NH4Cl                                                  0.33       g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\": 6.10225,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."}]},{"quantity_id":"q2","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 8-8","quote":"KCl                                                    0.33       g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\": 4.3784,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."}]},{"quantity_id":"q3","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.42640900000000004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.42640900000000004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.42640900000000004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.42640900000000004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.42640900000000004","unit":"G_PER_L"}}],"decision":"conflict","rationale":"Stored 0.42640900000000004 G_PER_L is the historical sum of the main rate 0.326409 and the full mineral-stock rate 0.1. The units look alike but the solution-stage bases differ, so the sum is invalid as a final-medium total. Preserve the two source additions separately; the mineral stock is received at 10 ml and the primary declares final main volume 1011 ml. No full-strength stock contribution can be added directly.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 9-9","quote":"CaCl2 x 2 H2O                                          0.33       g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\": 2.22025,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 40-40","quote":"CaCl2 x 2 H2O                                          0.10        g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 13-13","quote":"Modified Wolin's mineral solution                     10.00      ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"conflict","rationale":"Stored 0.42640900000000004 G_PER_L is the historical sum of the main rate 0.326409 and the full mineral-stock rate 0.1. The units look alike but the solution-stage bases differ, so the sum is invalid as a final-medium total. Preserve the two source additions separately; the mineral stock is received at 10 ml and the primary declares final main volume 1011 ml. No full-strength stock contribution can be added directly."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[2].concentration","decision":"conflict","rationale":"Stored 0.42640900000000004 G_PER_L is the historical sum of the main rate 0.326409 and the full mineral-stock rate 0.1. The units look alike but the solution-stage bases differ, so the sum is invalid as a final-medium total. Preserve the two source additions separately; the mineral stock is received at 10 ml and the primary declares final main volume 1011 ml. No full-strength stock contribution can be added directly."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[2].concentration","decision":"conflict","rationale":"Stored 0.42640900000000004 G_PER_L is the historical sum of the main rate 0.326409 and the full mineral-stock rate 0.1. The units look alike but the solution-stage bases differ, so the sum is invalid as a final-medium total. Preserve the two source additions separately; the mineral stock is received at 10 ml and the primary declares final main volume 1011 ml. No full-strength stock contribution can be added directly."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[2].concentration","decision":"conflict","rationale":"Stored 0.42640900000000004 G_PER_L is the historical sum of the main rate 0.326409 and the full mineral-stock rate 0.1. The units look alike but the solution-stage bases differ, so the sum is invalid as a final-medium total. Preserve the two source additions separately; the mineral stock is received at 10 ml and the primary declares final main volume 1011 ml. No full-strength stock contribution can be added directly."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[2].concentration","decision":"conflict","rationale":"Stored 0.42640900000000004 G_PER_L is the historical sum of the main rate 0.326409 and the full mineral-stock rate 0.1. The units look alike but the solution-stage bases differ, so the sum is invalid as a final-medium total. Preserve the two source additions separately; the mineral stock is received at 10 ml and the primary declares final main volume 1011 ml. No full-strength stock contribution can be added directly."}]},{"quantity_id":"q4","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 10-10","quote":"MgCl2 x 6 H2O                                          0.33       g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\": 1.60553,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."}]},{"quantity_id":"q5","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 11-11","quote":"KH2PO4                                                 0.33       g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\": 2.39857,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."}]},{"quantity_id":"q6","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"25.728","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"25.728","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"25.728","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[5].concentration","stored":{"value":"25.728","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[5].concentration","stored":{"value":"25.728","unit":"G_PER_L"}}],"decision":"conflict","rationale":"Stored 25.728 G_PER_L is the historical sum of the main rate 24.728 and the full mineral-stock rate 1. The units look alike but the solution-stage bases differ, so the sum is invalid as a final-medium total. Preserve the two source additions separately; the mineral stock is received at 10 ml and the primary declares final main volume 1011 ml. No full-strength stock contribution can be added directly.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 12-12","quote":"NaCl                                                  25.00       g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 25,\n                        \"unit\": \"g\",\n                        \"g_l\": 24.728,\n                        \"mmol_l\": 423.135,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 37-37","quote":"NaCl                                                   1.00        g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative text"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 13-13","quote":"Modified Wolin's mineral solution                     10.00      ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"conflict","rationale":"Stored 25.728 G_PER_L is the historical sum of the main rate 24.728 and the full mineral-stock rate 1. The units look alike but the solution-stage bases differ, so the sum is invalid as a final-medium total. Preserve the two source additions separately; the mineral stock is received at 10 ml and the primary declares final main volume 1011 ml. No full-strength stock contribution can be added directly."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[5].concentration","decision":"conflict","rationale":"Stored 25.728 G_PER_L is the historical sum of the main rate 24.728 and the full mineral-stock rate 1. The units look alike but the solution-stage bases differ, so the sum is invalid as a final-medium total. Preserve the two source additions separately; the mineral stock is received at 10 ml and the primary declares final main volume 1011 ml. No full-strength stock contribution can be added directly."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[5].concentration","decision":"conflict","rationale":"Stored 25.728 G_PER_L is the historical sum of the main rate 24.728 and the full mineral-stock rate 1. The units look alike but the solution-stage bases differ, so the sum is invalid as a final-medium total. Preserve the two source additions separately; the mineral stock is received at 10 ml and the primary declares final main volume 1011 ml. No full-strength stock contribution can be added directly."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[5].concentration","decision":"conflict","rationale":"Stored 25.728 G_PER_L is the historical sum of the main rate 24.728 and the full mineral-stock rate 1. The units look alike but the solution-stage bases differ, so the sum is invalid as a final-medium total. Preserve the two source additions separately; the mineral stock is received at 10 ml and the primary declares final main volume 1011 ml. No full-strength stock contribution can be added directly."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[5].concentration","decision":"conflict","rationale":"Stored 25.728 G_PER_L is the historical sum of the main rate 24.728 and the full mineral-stock rate 1. The units look alike but the solution-stage bases differ, so the sum is invalid as a final-medium total. Preserve the two source additions separately; the mineral stock is received at 10 ml and the primary declares final main volume 1011 ml. No full-strength stock contribution can be added directly."}]},{"quantity_id":"q7","label":"KNO3","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary 0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 14-14","quote":"KNO3                                                   0.50       g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"KNO3\",\n                        \"compound_id\": 191,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.49456,\n                        \"mmol_l\": 4.89164,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary 0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary 0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary 0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary 0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary 0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."}]},{"quantity_id":"q8","label":"Na-acetate","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.791296","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.791296","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.791296","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.791296","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.791296","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The unchanged 0.791296 G_PER_L agrees with the explicit provider main g_l and the primary 0.8 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 15-15","quote":"Na-acetate                                             0.80       g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\": 23,\n                        \"amount\": 0.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.791296,\n                        \"mmol_l\": 9.64597,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The unchanged 0.791296 G_PER_L agrees with the explicit provider main g_l and the primary 0.8 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The unchanged 0.791296 G_PER_L agrees with the explicit provider main g_l and the primary 0.8 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The unchanged 0.791296 G_PER_L agrees with the explicit provider main g_l and the primary 0.8 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The unchanged 0.791296 G_PER_L agrees with the explicit provider main g_l and the primary 0.8 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The unchanged 0.791296 G_PER_L agrees with the explicit provider main g_l and the primary 0.8 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."}]},{"quantity_id":"q9","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary 0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 16-16","quote":"Yeast extract                                          0.50       g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.49456,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary 0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary 0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary 0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary 0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary 0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."}]},{"quantity_id":"q10","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary 0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 17-17","quote":"Na2CO3                                                 0.50       g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.49456,\n                        \"mmol_l\": 4.66619,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary 0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary 0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary 0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary 0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary 0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."}]},{"quantity_id":"q11","label":"Na2S","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.296736","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.296736","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.296736","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.296736","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.296736","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The unchanged 0.296736 G_PER_L agrees with the explicit provider main g_l and the primary 0.3 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 19-19","quote":"Na2S                                                   0.30       g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na2S\",\n                        \"compound_id\": 490,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.296736,\n                        \"mmol_l\": 3.7533,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The unchanged 0.296736 G_PER_L agrees with the explicit provider main g_l and the primary 0.3 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The unchanged 0.296736 G_PER_L agrees with the explicit provider main g_l and the primary 0.3 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The unchanged 0.296736 G_PER_L agrees with the explicit provider main g_l and the primary 0.3 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The unchanged 0.296736 G_PER_L agrees with the explicit provider main g_l and the primary 0.3 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The unchanged 0.296736 G_PER_L agrees with the explicit provider main g_l and the primary 0.3 g batch amount divided by the explicitly printed 1.011 L final volume, to provider precision. Credit the DSM935a target/owner on that actual basis, not on input water. The three KOMODO copies are not independently supported by this distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently verified."}]},{"quantity_id":"q12","label":"Nitrilotriacetic acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Nitrilotriacetic acid in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Modified Wolin's mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 34-34","quote":"Nitrilotriacetic acid                                  1.50        g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Nitrilotriacetic acid in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[11].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Nitrilotriacetic acid in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[11].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Nitrilotriacetic acid in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[11].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Nitrilotriacetic acid in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[11].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Nitrilotriacetic acid in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q13","label":"MgSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for MgSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Modified Wolin's mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 35-35","quote":"MgSO4 x 7 H2O                                          3.00        g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 12.1716,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for MgSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for MgSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for MgSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for MgSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for MgSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q14","label":"MnSO4 x H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for MnSO4 x H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Modified Wolin's mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 36-36","quote":"MnSO4 x H2O                                            0.50        g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.9583,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for MnSO4 x H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for MnSO4 x H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for MnSO4 x H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for MnSO4 x H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for MnSO4 x H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q15","label":"FeSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for FeSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Modified Wolin's mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 38-38","quote":"FeSO4 x 7 H2O                                          0.10        g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.359693,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for FeSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for FeSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for FeSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for FeSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for FeSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q16","label":"CoSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.18","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for CoSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Modified Wolin's mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 39-39","quote":"CoSO4 x 7 H2O                                          0.18        g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\": 198,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 1.16132,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for CoSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for CoSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for CoSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for CoSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for CoSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q17","label":"ZnSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.18","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for ZnSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Modified Wolin's mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 41-41","quote":"ZnSO4 x 7 H2O                                          0.18        g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 0.625954,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for ZnSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for ZnSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for ZnSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for ZnSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for ZnSO4 x 7 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q18","label":"CuSO4 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for CuSO4 x 5 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Modified Wolin's mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 42-42","quote":"CuSO4 x 5 H2O                                          0.01        g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0400503,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for CuSO4 x 5 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for CuSO4 x 5 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for CuSO4 x 5 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for CuSO4 x 5 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for CuSO4 x 5 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q19","label":"AlK(SO4)2 x 12 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for AlK(SO4)2 x 12 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Modified Wolin's mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 43-43","quote":"AlK(SO4)2 x 12 H2O                                     0.02        g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0421596,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for AlK(SO4)2 x 12 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for AlK(SO4)2 x 12 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for AlK(SO4)2 x 12 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for AlK(SO4)2 x 12 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for AlK(SO4)2 x 12 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q20","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for H3BO3 in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Modified Wolin's mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 44-44","quote":"H3BO3                                                  0.01        g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for H3BO3 in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for H3BO3 in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for H3BO3 in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for H3BO3 in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for H3BO3 in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q21","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Na2MoO4 x 2 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Modified Wolin's mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 45-45","quote":"Na2MoO4 x 2 H2O                                        0.01        g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0413309,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Na2MoO4 x 2 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Na2MoO4 x 2 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Na2MoO4 x 2 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Na2MoO4 x 2 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Na2MoO4 x 2 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q22","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for NiCl2 x 6 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml. The primary explicitly supplies nickel hexahydrate; the local anhydrous ontology term is a separate error.","source_stage":"Modified Wolin's mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 46-46","quote":"NiCl2 x 6 H2O                                          0.03        g","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.231483,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for NiCl2 x 6 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml. The primary explicitly supplies nickel hexahydrate; the local anhydrous ontology term is a separate error."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for NiCl2 x 6 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml. The primary explicitly supplies nickel hexahydrate; the local anhydrous ontology term is a separate error."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for NiCl2 x 6 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml. The primary explicitly supplies nickel hexahydrate; the local anhydrous ontology term is a separate error."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for NiCl2 x 6 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml. The primary explicitly supplies nickel hexahydrate; the local anhydrous ontology term is a separate error."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for NiCl2 x 6 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml. The primary explicitly supplies nickel hexahydrate; the local anhydrous ontology term is a separate error."}]},{"quantity_id":"q23","label":"Na2SeO3 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.0003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.0003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.0003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.0003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.0003","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Na2SeO3 x 5 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Modified Wolin's mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 56-56","quote":"Na2SeO3 x 5 H2O                                           0.30       mg","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 0.3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\": 0.00114062,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Na2SeO3 x 5 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Na2SeO3 x 5 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Na2SeO3 x 5 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Na2SeO3 x 5 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Na2SeO3 x 5 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q24","label":"Na2WO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.0004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.0004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.0004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.0004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.0004","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Na2WO4 x 2 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Modified Wolin's mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 57-57","quote":"Na2WO4 x 2 H2O                                            0.40       mg","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[14]","quote":"{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 0.4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0004,\n                        \"mmol_l\": 0.00121267,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Na2WO4 x 2 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Na2WO4 x 2 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Na2WO4 x 2 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Na2WO4 x 2 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Na2WO4 x 2 H2O in Modified Wolin's mineral solution, but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q25","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Biotin in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Wolin's vitamin solution (10x); no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 66-66","quote":"Biotin                                                   20.00       mg","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Biotin in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Biotin in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Biotin in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Biotin in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Biotin in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q26","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Folic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Wolin's vitamin solution (10x); no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 67-67","quote":"Folic acid                                               20.00       mg","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Folic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Folic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Folic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Folic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Folic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q27","label":"Pyridoxine hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Pyridoxine hydrochloride in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Wolin's vitamin solution (10x); no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 68-68","quote":"Pyridoxine hydrochloride                                100.00       mg","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Pyridoxine hydrochloride in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Pyridoxine hydrochloride in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Pyridoxine hydrochloride in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Pyridoxine hydrochloride in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Pyridoxine hydrochloride in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q28","label":"Thiamine HCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Thiamine HCl in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Wolin's vitamin solution (10x); no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 69-69","quote":"Thiamine HCl                                             50.00       mg","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Thiamine HCl in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Thiamine HCl in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Thiamine HCl in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Thiamine HCl in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Thiamine HCl in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q29","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Riboflavin in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Wolin's vitamin solution (10x); no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 70-70","quote":"Riboflavin                                               50.00       mg","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Riboflavin in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Riboflavin in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Riboflavin in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Riboflavin in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Riboflavin in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q30","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Nicotinic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Wolin's vitamin solution (10x); no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 71-71","quote":"Nicotinic acid                                           50.00       mg","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Nicotinic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Nicotinic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Nicotinic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Nicotinic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Nicotinic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q31","label":"Calcium D-(+)-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Calcium D-(+)-pantothenate in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml. D-calcium pantothenate identity is supported by the current stereochemical ontology object; no mass-convention correction is inferred.","source_stage":"Wolin's vitamin solution (10x); no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 72-72","quote":"Calcium D-(+)-pantothenate                               50.00       mg","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Calcium D-(+)-pantothenate in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml. D-calcium pantothenate identity is supported by the current stereochemical ontology object; no mass-convention correction is inferred."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Calcium D-(+)-pantothenate in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml. D-calcium pantothenate identity is supported by the current stereochemical ontology object; no mass-convention correction is inferred."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Calcium D-(+)-pantothenate in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml. D-calcium pantothenate identity is supported by the current stereochemical ontology object; no mass-convention correction is inferred."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Calcium D-(+)-pantothenate in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml. D-calcium pantothenate identity is supported by the current stereochemical ontology object; no mass-convention correction is inferred."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Calcium D-(+)-pantothenate in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml. D-calcium pantothenate identity is supported by the current stereochemical ontology object; no mass-convention correction is inferred."}]},{"quantity_id":"q32","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.001","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Vitamin B12 in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Wolin's vitamin solution (10x); no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 73-73","quote":"Vitamin B12                                               1.00       mg","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Vitamin B12 in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Vitamin B12 in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Vitamin B12 in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Vitamin B12 in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for Vitamin B12 in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q33","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for p-Aminobenzoic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Wolin's vitamin solution (10x); no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 74-74","quote":"p-Aminobenzoic acid                                      50.00       mg","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for p-Aminobenzoic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for p-Aminobenzoic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for p-Aminobenzoic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for p-Aminobenzoic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for p-Aminobenzoic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q34","label":"(DL)-alpha-Lipoic acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for (DL)-alpha-Lipoic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml. A non-stereospecific lipoic-acid term is compatible with the explicit DL source designation.","source_stage":"Wolin's vitamin solution (10x); no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 75-75","quote":"(DL)-alpha-Lipoic acid                                   50.00       mg","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for (DL)-alpha-Lipoic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml. A non-stereospecific lipoic-acid term is compatible with the explicit DL source designation."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for (DL)-alpha-Lipoic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml. A non-stereospecific lipoic-acid term is compatible with the explicit DL source designation."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for (DL)-alpha-Lipoic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml. A non-stereospecific lipoic-acid term is compatible with the explicit DL source designation."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for (DL)-alpha-Lipoic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml. A non-stereospecific lipoic-acid term is compatible with the explicit DL source designation."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The unchanged number equals the provider stock g_l for (DL)-alpha-Lipoic acid in Wolin's vitamin solution (10x), but its placement in main ingredients is wrong. Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock); no full stock strength is a final-medium concentration. The primary prints stock input water, while the provider explicitly normalizes the stock to 1000 ml. A non-stereospecific lipoic-acid term is compatible with the explicit DL source designation."}]},{"quantity_id":"q35","label":"Modified Wolin's mineral solution 0","local_fields":[],"decision":"evidence_only","rationale":"Exact source-only receiving addition or solvent input; preserve its own stock/main stage and printed unit. Main final volume is explicitly 1011 ml; stock input water is not independently a measured final volume.","source_stage":"Main sol. 935a","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 13-13","quote":"Modified Wolin's mineral solution                     10.00      ml","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q36","label":"Wolin's vitamin solution (10x) 0","local_fields":[],"decision":"evidence_only","rationale":"Exact source-only receiving addition or solvent input; preserve its own stock/main stage and printed unit. Main final volume is explicitly 1011 ml; stock input water is not independently a measured final volume.","source_stage":"Main sol. 935a","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 18-18","quote":"Wolin's vitamin solution (10x)                         1.00      ml","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q37","label":"Distilled water 0","local_fields":[],"decision":"evidence_only","rationale":"Exact source-only receiving addition or solvent input; preserve its own stock/main stage and printed unit. Main final volume is explicitly 1011 ml; stock input water is not independently a measured final volume.","source_stage":"Main sol. 935a","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 20-20","quote":"Distilled water                                     1000.00      ml","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q38","label":"Distilled water 1","local_fields":[],"decision":"evidence_only","rationale":"Exact source-only receiving addition or solvent input; preserve its own stock/main stage and printed unit. Main final volume is explicitly 1011 ml; stock input water is not independently a measured final volume.","source_stage":"Modified Wolin's mineral solution","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 58-58","quote":"Distilled water                                        1000.00       ml","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[15]","quote":"{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q39","label":"Distilled water 2","local_fields":[],"decision":"evidence_only","rationale":"Exact source-only receiving addition or solvent input; preserve its own stock/main stage and printed unit. Main final volume is explicitly 1011 ml; stock input water is not independently a measured final volume.","source_stage":"Wolin's vitamin solution (10x)","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 76-76","quote":"Distilled water                                        1000.00       ml","quote_basis":"derivative text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q40","label":"Explicit DSM935a final volume","local_fields":[],"decision":"evidence_only","rationale":"Unlike the bare solvent inputs, this primary header explicitly states final volume 1011 ml. It supports main batch-to-rate arithmetic; do not replace it with an assumed 1 L. This basis is not transferred to DSM935, DSM935b or unavailable KOMODO variants.","source_stage":"DSM935a final main medium","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 1-4","quote":"935a: DEFERRIBACTER DESULFURICANS MEDIUM\n\nFinal pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q41","label":"DSM935a preparation and numeric controls","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve ingredients (except carbonate, vitamins and sulfide), then sparge medium with  80% H2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials to 30% of their volume and autoclave. Add vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration. Add carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. The pH of the complete medium should be 6.5."}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve ingredients (except carbonate, vitamins and sulfide), then sparge medium with  80% H2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under the same gas atmosphere into anoxic Hungate-type tubes or serum vials to 30% of their volume and autoclave. Add vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration. Add carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. The pH of the complete medium should be 6.5."}}],"decision":"evidence_only","rationale":"Existing prose retains the correct 80/20 H2/CO2, 30–45 min, 30% vessel-fill, late additions, 100% nitrogen stock and 80/20 nitrogen/carbon-dioxide carbonate contexts, and pH6.5. Preserve those numeric controls; split the single AUTOCLAVE action into appropriately scoped actions. Unstated autoclave settings and late-stock strengths/volumes remain unknown. Do not substitute the differing935 or935b preparation.","source_stage":"DSM935a main preparation","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 22-28","quote":"Dissolve ingredients (except carbonate, vitamins and sulfide), then sparge medium with\n80% H2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium\nunder the same gas atmosphere into anoxic Hungate-type tubes or serum vials to 30% of\ntheir volume and autoclave. Add vitamins and sulfide from sterile anoxic stock solutions\nprepared under 100% N2 gas. Vitamins should be sterilized by filtration. Add carbonate\nfrom a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere.\nThe pH of the complete medium should be 6.5.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"Existing prose retains the correct 80/20 H2/CO2, 30–45 min, 30% vessel-fill, late additions, 100% nitrogen stock and 80/20 nitrogen/carbon-dioxide carbonate contexts, and pH6.5. Preserve those numeric controls; split the single AUTOCLAVE action into appropriately scoped actions. Unstated autoclave settings and late-stock strengths/volumes remain unknown. Do not substitute the differing935 or935b preparation."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"Existing prose retains the correct 80/20 H2/CO2, 30–45 min, 30% vessel-fill, late additions, 100% nitrogen stock and 80/20 nitrogen/carbon-dioxide carbonate contexts, and pH6.5. Preserve those numeric controls; split the single AUTOCLAVE action into appropriately scoped actions. Unstated autoclave settings and late-stock strengths/volumes remain unknown. Do not substitute the differing935 or935b preparation."}]},{"quantity_id":"q42","label":"Mineral stock pH preparation","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"ADJUST_PH","description":"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH."}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"ADJUST_PH","description":"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH."}}],"decision":"conflict","rationale":"The retained pH6.5 then7.0 sequence with KOH is supported for the mineral stock, not the final medium. Move its scope without changing source digits. KOH amount/strength is unspecified; do not invent either.","source_stage":"Modified Wolin mineral stock only","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 60-61","quote":"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust\nfinal to pH 7.0 with KOH.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"preparation_steps[1]","decision":"conflict","rationale":"The retained pH6.5 then7.0 sequence with KOH is supported for the mineral stock, not the final medium. Move its scope without changing source digits. KOH amount/strength is unspecified; do not invent either."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"preparation_steps[1]","decision":"conflict","rationale":"The retained pH6.5 then7.0 sequence with KOH is supported for the mineral stock, not the final medium. Move its scope without changing source digits. KOH amount/strength is unspecified; do not invent either."}]},{"quantity_id":"q43","label":"Separate pH assertions","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ph_value","stored":6.5},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ph_value","stored":7.0},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ph_value","stored":6.5},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ph_value","stored":7.0},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ph_value","stored":6.5}],"decision":"mixed","rationale":"DSM935a target/owner pH6.5 is supported. The copied wrapper values6.5/7.0 require their own exact source; fresh KOMODO routes are403. DSM935 gives6.5–6.7 and935b gives7.0, so neither is an interchangeable correction.","source_stage":"Independent accession-specific pH","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt lines 3-3","quote":"Final pH: 6.5","quote_basis":"derivative text"},{"evidence_id":"dsmz935","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935.bin","raw_sha256":"51e46137cd5697af28a63697cffca147b1496c494bbe2d726fc11e60040a75dc","text_sha256":"f440ea58c8d679c4b2f2b2340b66ef07d1ae24854cea34b98225058bb56c89c5","accessed_at":"2026-10-28T16:12:45.021337Z","locator":"Exact primary pH sentence","quote":"complete medium should be 6.5 - 6.7.","quote_basis":"derivative text"},{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt lines 18-23","quote":"Dissolve ingredients (except bicarbonate and vitamins), then sparge medium with 100%\nN2 gas for 30 – 45 min to make it anoxic. Adjust pH to 7.0 and dispense medium under\nsame gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add\nvitamins from an anoxic stock solution prepared under 100% N2 gas and sterilized by\nfiltration and bicarbonate from a sterile anoxic stock solution prepared under 80% N2\nand 20% CO2 gas atmosphere. The pH of the complete medium should be 7.0.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"DSM935a target/owner pH6.5 is supported. The copied wrapper values6.5/7.0 require their own exact source; fresh KOMODO routes are403. DSM935 gives6.5–6.7 and935b gives7.0, so neither is an interchangeable correction."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ph_value","decision":"unsupported","rationale":"DSM935a target/owner pH6.5 is supported. The copied wrapper values6.5/7.0 require their own exact source; fresh KOMODO routes are403. DSM935 gives6.5–6.7 and935b gives7.0, so neither is an interchangeable correction."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"DSM935a target/owner pH6.5 is supported. The copied wrapper values6.5/7.0 require their own exact source; fresh KOMODO routes are403. DSM935 gives6.5–6.7 and935b gives7.0, so neither is an interchangeable correction."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ph_value","decision":"unsupported","rationale":"DSM935a target/owner pH6.5 is supported. The copied wrapper values6.5/7.0 require their own exact source; fresh KOMODO routes are403. DSM935 gives6.5–6.7 and935b gives7.0, so neither is an interchangeable correction."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ph_value","decision":"unsupported","rationale":"DSM935a target/owner pH6.5 is supported. The copied wrapper values6.5/7.0 require their own exact source; fresh KOMODO routes are403. DSM935 gives6.5–6.7 and935b gives7.0, so neither is an interchangeable correction."}]},{"quantity_id":"q44","label":"DSM935b comparison: NH4Cl                                                        0.33       g","local_fields":[],"decision":"evidence_only","rationale":"Exact distinct935b batch row, inventoried to expose the wrong linked PDF. It does not override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt lines 4-4","quote":"NH4Cl                                                        0.33       g","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q45","label":"DSM935b comparison: KCl                                                          0.33       g","local_fields":[],"decision":"evidence_only","rationale":"Exact distinct935b batch row, inventoried to expose the wrong linked PDF. It does not override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt lines 5-5","quote":"KCl                                                          0.33       g","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q46","label":"DSM935b comparison: CaCl2 x 2 H2O                                                0.33       g","local_fields":[],"decision":"evidence_only","rationale":"Exact distinct935b batch row, inventoried to expose the wrong linked PDF. It does not override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt lines 6-6","quote":"CaCl2 x 2 H2O                                                0.33       g","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q47","label":"DSM935b comparison: MgCl2 x 6 H2O                                                0.33       g","local_fields":[],"decision":"evidence_only","rationale":"Exact distinct935b batch row, inventoried to expose the wrong linked PDF. It does not override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt lines 7-7","quote":"MgCl2 x 6 H2O                                                0.33       g","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q48","label":"DSM935b comparison: KH2PO4                                                       0.33       g","local_fields":[],"decision":"evidence_only","rationale":"Exact distinct935b batch row, inventoried to expose the wrong linked PDF. It does not override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt lines 8-8","quote":"KH2PO4                                                       0.33       g","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q49","label":"DSM935b comparison: NaCl                                                        25.00       g","local_fields":[],"decision":"evidence_only","rationale":"Exact distinct935b batch row, inventoried to expose the wrong linked PDF. It does not override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt lines 9-9","quote":"NaCl                                                        25.00       g","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q50","label":"DSM935b comparison: Modified Wolin’s mineral solution (see medium 141)          10.00      ml","local_fields":[],"decision":"evidence_only","rationale":"Exact distinct935b batch row, inventoried to expose the wrong linked PDF. It does not override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt lines 10-10","quote":"Modified Wolin’s mineral solution (see medium 141)          10.00      ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q51","label":"DSM935b comparison: KNO3                                                         0.50       g","local_fields":[],"decision":"evidence_only","rationale":"Exact distinct935b batch row, inventoried to expose the wrong linked PDF. It does not override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt lines 11-11","quote":"KNO3                                                         0.50       g","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q52","label":"DSM935b comparison: Na-acetate                                                   2.00       g","local_fields":[],"decision":"evidence_only","rationale":"Exact distinct935b batch row, inventoried to expose the wrong linked PDF. It does not override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt lines 12-12","quote":"Na-acetate                                                   2.00       g","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q53","label":"DSM935b comparison: Yeast extract                                                0.15       g","local_fields":[],"decision":"evidence_only","rationale":"Exact distinct935b batch row, inventoried to expose the wrong linked PDF. It does not override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt lines 13-13","quote":"Yeast extract                                                0.15       g","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q54","label":"DSM935b comparison: NaHCO3                                                       0.30       g","local_fields":[],"decision":"evidence_only","rationale":"Exact distinct935b batch row, inventoried to expose the wrong linked PDF. It does not override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt lines 14-14","quote":"NaHCO3                                                       0.30       g","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q55","label":"DSM935b comparison: Wolin's vitamin solution (see medium 141)                   10.00      ml","local_fields":[],"decision":"evidence_only","rationale":"Exact distinct935b batch row, inventoried to expose the wrong linked PDF. It does not override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt lines 15-15","quote":"Wolin's vitamin solution (see medium 141)                   10.00      ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q56","label":"DSM935b comparison: Distilled water                                           1000.00      ml","local_fields":[],"decision":"evidence_only","rationale":"Exact distinct935b batch row, inventoried to expose the wrong linked PDF. It does not override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt lines 16-16","quote":"Distilled water                                           1000.00      ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q57","label":"DSM935b preparation comparison","local_fields":[],"decision":"evidence_only","rationale":"This distinct source uses nitrogen-based preparation and pH7.0; it does not support replacing935a hydrogen/carbon-dioxide preparation. Preserve the difference and the exact source link mismatch.","source_stage":"Comparison-only DSM935b","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt lines 18-23","quote":"Dissolve ingredients (except bicarbonate and vitamins), then sparge medium with 100%\nN2 gas for 30 – 45 min to make it anoxic. Adjust pH to 7.0 and dispense medium under\nsame gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add\nvitamins from an anoxic stock solution prepared under 100% N2 gas and sterilized by\nfiltration and bicarbonate from a sterile anoxic stock solution prepared under 80% N2\nand 20% CO2 gas atmosphere. The pH of the complete medium should be 7.0.","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q58","label":"DSM935 comparison: NH4Cl","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\": 18.6392,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q59","label":"DSM935 comparison: K2HPO4","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.08,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0797607,\n                        \"mmol_l\": 0.457932,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q60","label":"DSM935 comparison: MgCl2 x 6 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 4.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.48654,\n                        \"mmol_l\": 22.0682,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q61","label":"DSM935 comparison: CaCl2 x 2 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.38,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.378863,\n                        \"mmol_l\": 2.57704,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q62","label":"DSM935 comparison: NaCl","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 29.9103,\n                        \"mmol_l\": 511.812,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q63","label":"DSM935 comparison: KNO3","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"KNO3\",\n                        \"compound_id\": 191,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\": 4.93066,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q64","label":"DSM935 comparison: Trace element solution SL-10","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q65","label":"DSM935 comparison: Selenite-tungstate solution","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q66","label":"DSM935 comparison: Yeast extract","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.99402,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q67","label":"DSM935 comparison: Na2CO3","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.49551,\n                        \"mmol_l\": 14.1102,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q68","label":"DSM935 comparison: Na-pyruvate","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na-pyruvate\",\n                        \"compound_id\": 113,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\": 4.53005,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q69","label":"DSM935 comparison: Wolin's vitamin solution (10x)","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q70","label":"DSM935 comparison: Distilled water","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q71","label":"DSM935 comparison: HCl","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q72","label":"DSM935 comparison: FeCl2 x 4 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q73","label":"DSM935 comparison: ZnCl2","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q74","label":"DSM935 comparison: MnCl2 x 4 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q75","label":"DSM935 comparison: H3BO3","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q76","label":"DSM935 comparison: CoCl2 x 6 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q77","label":"DSM935 comparison: CuCl2 x 2 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q78","label":"DSM935 comparison: NiCl2 x 6 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q79","label":"DSM935 comparison: Na2MoO4 x 2 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q80","label":"DSM935 comparison: Distilled water","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q81","label":"DSM935 comparison: NaOH","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Selenite-tungstate solution","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q82","label":"DSM935 comparison: Na2SeO3 x 5 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Selenite-tungstate solution","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q83","label":"DSM935 comparison: Na2WO4 x 2 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Selenite-tungstate solution","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q84","label":"DSM935 comparison: Distilled water","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Selenite-tungstate solution","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q85","label":"DSM935 comparison: Biotin","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Wolin's vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q86","label":"DSM935 comparison: Folic acid","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Wolin's vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q87","label":"DSM935 comparison: Pyridoxine hydrochloride","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Wolin's vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q88","label":"DSM935 comparison: Thiamine HCl","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Wolin's vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q89","label":"DSM935 comparison: Riboflavin","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Wolin's vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q90","label":"DSM935 comparison: Nicotinic acid","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Wolin's vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q91","label":"DSM935 comparison: Calcium D-(+)-pantothenate","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Wolin's vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q92","label":"DSM935 comparison: Vitamin B12","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Wolin's vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q93","label":"DSM935 comparison: p-Aminobenzoic acid","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Wolin's vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q94","label":"DSM935 comparison: (DL)-alpha-Lipoic acid","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Wolin's vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q95","label":"DSM935 comparison: Distilled water","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935 source row, retained with its own main/stock stage. Different basal salts, pyruvate and three receiving stocks demonstrate that matching a number without its accession/suffix is insufficient. Provider g_l is explicit but primary final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only Wolin's vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q96","label":"DSM935 primary source controls","local_fields":[],"decision":"evidence_only","rationale":"The complete primary counterpart preserves all935 input amounts, solvent/stocks, gas/duration/pH and the stock-local final make-up. These are compared only as a distinct variant; the SL-10 final1000ml is not a main-medium final-volume statement.","source_stage":"Comparison-only complete DSM935","sources":[{"evidence_id":"dsmz935","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935.bin","raw_sha256":"51e46137cd5697af28a63697cffca147b1496c494bbe2d726fc11e60040a75dc","text_sha256":"f440ea58c8d679c4b2f2b2340b66ef07d1ae24854cea34b98225058bb56c89c5","accessed_at":"2026-10-28T16:12:45.021337Z","locator":"Complete derivative text retaining original form-feed separators","quote":"935: DEFERRIBACTER MEDIUM\n\n   NH4Cl                                                      1.00         g\n   K2HPO4                                                     0.08         g\n   MgCl2 x 6 H2O                                              4.50         g\n   CaCl2 x 2 H2O                                              0.38         g\n   NaCl                                                      30.00         g\n   KNO3                                                       0.50         g\n   Trace element solution SL-10                               1.00        ml\n   Selenite-tungstate solution                                1.00        ml\n   Yeast extract                                              2.00         g\n   Na2CO3                                                     1.50         g\n   Na-pyruvate                                                0.50         g\n   Wolin's vitamin solution (10x)                             1.00        ml\n   Distilled water                                         1000.00        ml\n\nDissolve ingredients (except carbonate, pyruvate and vitamins), then sparge medium with\n80% N2 and 20% CO2 gas mixture for 30-45 min to make it anoxic. Dispense medium\nunder same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.\nAdd pyruvate and vitamins from anoxic stock solutions prepared under 100% N2 gas and\ncarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas\natmosphere. The pyruvate and vitamins solutions are sterilized by filtration. The pH of the\ncomplete medium should be 6.5 - 6.7.\n\n\n\n\nTrace element solution SL-10 (from medium 320)\n   HCl (25%)                                                  10.00      ml\n   FeCl2 x 4 H2O                                               1.50       g\n   ZnCl2                                                      70.00      mg\n   MnCl2 x 4 H2O                                             100.00      mg\n   H3BO3                                                       6.00      mg\n   CoCl2 x 6 H2O                                             190.00      mg\n   CuCl2 x 2 H2O                                               2.00      mg\n   NiCl2 x 6 H2O                                              24.00      mg\n   Na2MoO4 x 2 H2O                                            36.00      mg\n   Distilled water                                           990.00      ml\n\nFirst dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.\n\n\n\nSelenite-tungstate solution (from medium 385)\n   NaOH                                                        0.50       g\n   Na2SeO3 x 5 H2O                                             3.00      mg\n\n\n© 2022 DSMZ - All rights reserved                                                  Page 1 of 2\n\f935: DEFERRIBACTER MEDIUM\n\n\n\n   Na2WO4 x 2 H2O                              4.00   mg\n   Distilled water                          1000.00   ml\n\n\nWolin's vitamin solution (10x) (from medium 120)\n   Biotin                                     20.00   mg\n   Folic acid                                 20.00   mg\n   Pyridoxine hydrochloride                  100.00   mg\n   Thiamine HCl                               50.00   mg\n   Riboflavin                                 50.00   mg\n   Nicotinic acid                             50.00   mg\n   Calcium D-(+)-pantothenate                 50.00   mg\n   Vitamin B12                                 1.00   mg\n   p-Aminobenzoic acid                        50.00   mg\n   (DL)-alpha-Lipoic acid                     50.00   mg\n   Distilled water                          1000.00   ml\n\n\n\n\n© 2022 DSMZ - All rights reserved                          Page 2 of 2","quote_basis":"derivative text"}],"layer_assessments":[]}],"document_scopes":{"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml":null,"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml":null,"data/normalized_yaml/bacterial/for_dsm_14813.yaml":null,"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:002109.

All current asserted CHEBI objects and MIM exact rows are covered. Nickel hexahydrate is wrongly represented by anhydrous CHEBI:34887 in two slots; other explicit sulfate hydrates, Na2S, D-calcium pantothenate and DL-compatible generic lipoic acid are retained. Valid canonical labels do not erase a supplied-form error. Legacy nitrate and missing yeast/calcium secondary links are bounded separately.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:002109.

Read all ten original reports, four selected parent rows, all current owner events and current repair/resolver/import/cleanup/merge bodies. October source objects/digests are independently joined; earlier conflict statuses were not proof of accepted curation. September 935b comparison-target advice is not blindly transferred. The topology repair is credited as an actual stored update while its signature-based source-equivalence inference remains unverified; current scientific-field merge comparison would preserve differing notes, pH, preparation and relationships.

## Findings

### f1: Resolve the 935a identifier versus 935b link and distinct 935 family

major / open / confirmed; issue key: culturemech-002109-accession-variant-conflict.

The selected target/DSM owner identifies 935a, but its notes and current API link point to the chemically different 935b PDF. Fresh primary 935a matches the retained basal formula/preparation and explicitly gives 1011 ml final volume; 935b differs in acetate, yeast, carbonate species, vitamins, sulfide and atmosphere/pH. DSM 935 differs again. September owners improve local topology, but classifying KOMODO 935 as a 935a duplicate and both strain wrappers under 935a relies on copied signatures, not recovered variant recipes. Exact KOMODO routes remain 403. Preserve all accessions, distinct catalogue strain identities and historical events; resolve the source-link and duplicate/variant claims before regeneration.

### f2: Undo mixed-stage calcium/sodium sums and flattened stocks

major / open / confirmed; issue key: culturemech-002109-stock-stage-and-sums.

All five layers combine main and mineral-stock CaCl2/NaCl rates into 0.42640900000000004 and 25.728 G_PER_L. Equal units do not make different solution-stage denominators additive. Another 23 mineral/vitamin constituents remain at full stock strength in main ingredients. Preserve the primary 935a main masses and explicit 1011 ml final volume, the two separate receiving doses, stock compositions and solvent inputs. Reconcile each accession before curating the copied KOMODO layers. Current cleanup no longer sums differing duplicates and current import separates primary compounds/stocks; those present behaviors do not justify older output.

### f3: Separate retained main and mineral-stock preparation

major / open / confirmed; issue key: culturemech-002109-preparation-stock-context.

The DSM owner/target correctly retains substantial 935a source text, including gas mixtures, 30–45 min and 30% vessel fill. Preserve it while separating actions from the single AUTOCLAVE tag. The stock-local pH 6.5→7.0 KOH step is currently an unqualified main preparation step; attach it to Modified Wolin mineral stock. Unknown KOH amount and autoclave settings remain unknown. Do not copy 935a preparation into unresolved KOMODO variants or replace it with 935b conditions.

### f4: Match nickel hexahydrate in both ontology slots

major / open / confirmed; issue key: culturemech-002109-nickel-hydrate-grounding.

NiCl2 x 6H2O is explicitly supplied by the 935a mineral stock, but ingredients[21] asserts anhydrous CHEBI:34887 in primary and secondary slots. Verify an exact hydrate object and canonical label while retaining the source stock amount. MIM lists the CHEBI:53542 preferred row as REJECTED and an exact synonym as MAPPED; preserve that distinction rather than treating either status as chemical proof. The other named sulfate hydrates, sodium-sulfide formula, D-calcium pantothenate and non-stereospecific lipoic acid are compatible with the exact 935a forms.

### f5: Resolve bounded legacy and missing ingredient links

minor / open / confirmed; issue key: culturemech-002109-secondary-link-gaps.

The primary KNO3 CHEBI:63043 is correct, but its legacy MediaIngredientMech:000170 secondary ID is absent from the exact packaged current index. Yeast extract has no primary/secondary linkage and calcium D-pantothenate lacks a secondary link. Reconcile exact current candidates without changing supported amounts or claiming historical invalidity from current snapshot absence.

### f6: Preserve original history and qualify historical source claims

minor / open / confirmed; issue key: culturemech-002109-claim-history-context.

There are no attached ingredient claims. All ten full reports remain derivative historical evidence; current matching API bytes authenticate content, not the original access event. The September report targets a separate TOGO 935b cluster, so its proposed collapse and 935b conditions are not adopted for this 935a target. KOMODO import .fZ and timezone-naive resolver events must remain byte-preserved; append verified context rather than rewrite their timestamps. Local topology fixes/curated flags do not establish external variant equivalence.

## Recommended Actions And Acceptance Checks

### a1

The selected target/DSM owner identifies 935a, but its notes and current API link point to the chemically different 935b PDF. Fresh primary 935a matches the retained basal formula/preparation and explicitly gives 1011 ml final volume; 935b differs in acetate, yeast, carbonate species, vitamins, sulfide and atmosphere/pH. DSM 935 differs again. September owners improve local topology, but classifying KOMODO 935 as a 935a duplicate and both strain wrappers under 935a relies on copied signatures, not recovered variant recipes. Exact KOMODO routes remain 403. Preserve all accessions, distinct catalogue strain identities and historical events; resolve the source-link and duplicate/variant claims before regeneration.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

All five layers combine main and mineral-stock CaCl2/NaCl rates into 0.42640900000000004 and 25.728 G_PER_L. Equal units do not make different solution-stage denominators additive. Another 23 mineral/vitamin constituents remain at full stock strength in main ingredients. Preserve the primary 935a main masses and explicit 1011 ml final volume, the two separate receiving doses, stock compositions and solvent inputs. Reconcile each accession before curating the copied KOMODO layers. Current cleanup no longer sums differing duplicates and current import separates primary compounds/stocks; those present behaviors do not justify older output.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The DSM owner/target correctly retains substantial 935a source text, including gas mixtures, 30–45 min and 30% vessel fill. Preserve it while separating actions from the single AUTOCLAVE tag. The stock-local pH 6.5→7.0 KOH step is currently an unqualified main preparation step; attach it to Modified Wolin mineral stock. Unknown KOH amount and autoclave settings remain unknown. Do not copy 935a preparation into unresolved KOMODO variants or replace it with 935b conditions.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

NiCl2 x 6H2O is explicitly supplied by the 935a mineral stock, but ingredients[21] asserts anhydrous CHEBI:34887 in primary and secondary slots. Verify an exact hydrate object and canonical label while retaining the source stock amount. MIM lists the CHEBI:53542 preferred row as REJECTED and an exact synonym as MAPPED; preserve that distinction rather than treating either status as chemical proof. The other named sulfate hydrates, sodium-sulfide formula, D-calcium pantothenate and non-stereospecific lipoic acid are compatible with the exact 935a forms.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

The primary KNO3 CHEBI:63043 is correct, but its legacy MediaIngredientMech:000170 secondary ID is absent from the exact packaged current index. Yeast extract has no primary/secondary linkage and calcium D-pantothenate lacks a secondary link. Reconcile exact current candidates without changing supported amounts or claiming historical invalidity from current snapshot absence.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a6

There are no attached ingredient claims. All ten full reports remain derivative historical evidence; current matching API bytes authenticate content, not the original access event. The September report targets a separate TOGO 935b cluster, so its proposed collapse and 935b conditions are not adopted for this 935a target. KOMODO import .fZ and timezone-naive resolver events must remain byte-preserved; append verified context rather than rewrite their timestamps. Local topology fixes/curated flags do not establish external variant equivalence.

- Retain all original events and old reports unchanged; append any new verified historical context in a new curation event.
- Attach literal source claims with exact accession, raw digest and actual access time; do not convert prior report prose into an original retrieval receipt.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsmz935a | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf; REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| dsmz935 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935.pdf; REVIEW_WORK/batch072/source01-03-supplement/dsmz935.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| dsmz935b | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf; REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| api935a | https://mediadive.dsmz.de/rest/medium/935a; REVIEW_WORK/batch072/source01-03-supplement/api935a.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| api935 | https://mediadive.dsmz.de/rest/medium/935; REVIEW_WORK/batch072/source01-03-supplement/api935.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| api935b | https://mediadive.dsmz.de/rest/medium/935b; REVIEW_WORK/batch072/source01-03-supplement/api935b.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| komodo935 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=935; REVIEW_WORK/batch072/source01-03-supplement/komodo935.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| komodo935dot1 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=935.1; REVIEW_WORK/batch072/source01-03-supplement/komodo935dot1.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| komodo935dash14783 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=935_14783; REVIEW_WORK/batch072/source01-03-supplement/komodo935dash14783.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| komodoList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; REVIEW_WORK/batch072/source01-03-supplement/komodoList.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| dsm14813 | https://www.dsmz.de/collection/catalogue/details/culture/DSM-14813; REVIEW_WORK/batch072/source01-03-preflight/dsm14813.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Exact selected-source identity preflight. Organism/source context screened before any operational assessment; no source transfer between variants. |
| dsm14783 | https://www.dsmz.de/collection/catalogue/details/culture/DSM-14783; REVIEW_WORK/batch072/source01-03-preflight/dsm14783.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Exact selected-source identity preflight. Organism/source context screened before any operational assessment; no source transfer between variants. |
| target | data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| owner-2 | data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| owner-3 | data/normalized_yaml/bacterial/for_dsm_14813.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| owner-4 | data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| report-19 | reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-20 | reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/for_dsm_14813.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-22 | reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/medium_935_modified_for_dsm_14783.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-24 | reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/deferribacter_desulfuricans_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-26 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-27 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-28 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_14813.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-29 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-30 | reports/yaml_record_review/20260922T141339Z-deferribacter_desulfuricans_medium__99f27aac.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch072/record02/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete text of ten scoped historical reports; September comparison-target claims remain separate from the selected current record. |
| historical-selected-parent-rows | REVIEW_WORK/batch072/record02/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch072/record02/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact selected target and all four maintained contributor documents, including full histories. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| writer-cleanup | scripts/cleanup_media_quality.py; MediaQualityFixer._merge_ingredient_group | context_only | Current _merge_ingredient_group keeps identical duplicate amounts and flags disagreements; it no longer sums duplicate quantities. It cannot establish compatible stock/main bases or repair a historical flattened sum. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _normalize_unit; _classify_preparation_action | context_only | Current parsing retains primary compounds and separate receiving stocks, excluding flattened stock composition. It prefers explicit g_l and skips input water; fallback unit conversion alone does not establish a denominator. The classifier chooses AUTOCLAVE before later filtration in a mixed paragraph. |
| writer-resolver | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.extract_dsmz_id; DSMZCompositionResolver.merge_composition | context_only | Current DSMZCompositionResolver strips letter suffixes from extracted accessions and copies ingredients/solutions; it does not establish source equivalence or copy full preparation. Historical events separately record DSMZ935 copies and must not be treated as proof that current code executed then. |
| writer-repair | scripts/repair_komodo_935_deferribacter_score10.py; Complete fixed signature, repair_parent and repair_child bodies | context_only | Current exact repair requires the shared 34-ingredient local signature, then promotes DSM935a and classifies KOMODO935 as duplicate and its strain wrappers as variants. It leaves distinct DSM935 out. This is local topology repair credit, not external accession or strain-formulation authentication. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch072/source01-03-supplement/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; REVIEW_WORK/batch072/source01-03-supplement/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158; REVIEW_WORK/batch072/source01-03-supplement/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; REVIEW_WORK/batch072/source01-03-supplement/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; REVIEW_WORK/batch072/source01-03-supplement/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch072/source01-03-supplement/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi63043 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63043; REVIEW_WORK/batch072/source01-03-supplement/chebi63043.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32954; REVIEW_WORK/batch072/source01-03-supplement/chebi32954.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377; REVIEW_WORK/batch072/source01-03-supplement/chebi29377.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi76208 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76208; REVIEW_WORK/batch072/source01-03-supplement/chebi76208.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:44557; REVIEW_WORK/batch072/source01-03-supplement/chebi44557.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31795; REVIEW_WORK/batch072/source01-03-supplement/chebi31795.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86364; REVIEW_WORK/batch072/source01-03-supplement/chebi86364.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75836; REVIEW_WORK/batch072/source01-03-supplement/chebi75836.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91244; REVIEW_WORK/batch072/source01-03-supplement/chebi91244.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312; REVIEW_WORK/batch072/source01-03-supplement/chebi32312.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31440; REVIEW_WORK/batch072/source01-03-supplement/chebi31440.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86465; REVIEW_WORK/batch072/source01-03-supplement/chebi86465.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch072/source01-03-supplement/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch072/source01-03-supplement/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; REVIEW_WORK/batch072/source01-03-supplement/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
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
| quantities | REVIEW_WORK/batch072/record02/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch072/record02/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch072/record02/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch072/record02/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch072/record02/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch072/record02/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch072/record02/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch072/record02/validate-schema.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch072/record02/validate-strict.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch072/record02/validate-terms.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch072/record02/validate-references.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Exact KOMODO 935,935.1,935_14783 and catalogue requests returned 403. No formulation or growth transfer is inferred from their strain identifiers or catalogue medium links.
- DSM 935a explicitly declares final main volume 1011 ml. This positive basis is retained;935 and 935b input water do not inherit it. Provider stock volumes/rates remain separate from primary stock input-water descriptions.
- The 935b REST endpoint returned 404, but its exact primary PDF was recovered and visually read. Its full component/condition differences are comparison-only; unprinted stock composition from its external 141 reference is not silently imported.
- Provider mmol_l values are not used to certify hydrate-sensitive molar conversions; primary mass and explicit g_l evidence are the assessed quantities.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T163255Z-culturemech-002109-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: DEFERRIBACTER DESULFURICANS MEDIUM'
started_at: '2026-10-28T16:12:02.493019Z'
finished_at: '2026-10-28T16:32:55.285297Z'
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
summary: The record needs accession/variant reconciliation, separation of two stocks
  and mixed-stage calcium/sodium sums, stock-local preparation repair and nickel-hydrate
  grounding. Fresh 935a explicitly supports 1011 ml final volume and the unchanged
  basal rates, while 935b and 935 remain distinct sources. Exact KOMODO variants are
  unavailable, so completion is partial. All four original canonical checks passed
  without establishing scientific equivalence.
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
  - path: data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml
    sha256: a2b4f9cce996f35bd9da5d9bd12830abea7ac68180cc036f8a1e336cba9f35bb
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml
    sha256: 7ab424969123f8773724ce678eeb0e0041d5476e7299f3b3257926a7a50d435b
    role: context
  - path: data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml
    sha256: 333e3af0864878a346746dce0d5ab1ef564b14d97828d12a18e941f1db199b8e
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_14813.yaml
    sha256: 0e9fa8185ca1d711b93606914aa0294de80c6312d696909e14b900d56a55885f
    role: context
  - path: data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml
    sha256: 73d3afe521e3a9412be956db4b45c046d3351615a278bea362cd517625337ac3
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml.md
    sha256: 71abceea7264b1e221738ef08a36e3baf3838157c149d75cfdb0eb8ec1984fb4
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/for_dsm_14813.yaml.md
    sha256: c16a53980b4aaf78c379acb0695681cf2fcc08869a73626c2c40935119ee1daf
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/medium_935_modified_for_dsm_14783.yaml.md
    sha256: b6efd51f7d7b1f1f9c32dc9b837ca2c1cfc4aa4acf3c6c9b03e11531d1d87b99
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/plan.json
    sha256: 94e89303f14558d9b0d485aa6cb4eb646050837864ab920d759763a3a483b94f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/deferribacter_desulfuricans_medium.yaml.md
    sha256: 377c275e5792e1377a9941ca4df580afe91d786b5f93ead9d67bba9c5e5cc596
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.md
    sha256: da4d2aba500bb2249d8d5cf642439d417fb02c9a9413bef159041d43d1227b8b
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.md
    sha256: 3f4553b6f7417e06413b23a5551e3f58cf15220399ec13dc5cbf3903a44de57f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.md
    sha256: d55e45715915e3671cddd31b8d3cde0b767dfce29b9154262d616e4795bed55c
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_14813.md
    sha256: 4dc1285ed3fcef05c976223a30f336567c2c1e96a0b3fdfeefe3399466811318
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.md
    sha256: a231393b6c40a1396db016fe96f75a7cd8105415ba541f1990a093598e086bfb
    role: context
  - path: reports/yaml_record_review/20260922T141339Z-deferribacter_desulfuricans_medium__99f27aac.md
    sha256: 32bbac9ddb1c4f5cf5a3af068d568ea9c13f04377470fda99aabdec40cb2a134
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
  - path: scripts/repair_komodo_935_deferribacter_score10.py
    sha256: 184a38264b2d89df9178ce6f669b254d3b649040ed2d07c36afdd1210abe8cb6
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
  selection: Authoritative batch072 index 02
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:002109
targets:
- target_id: CultureMech:002109
  path: data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml
  label: deferribacter_desulfuricans_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14813.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml
    role: maintained normalized contributor
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:002109
  command: just validate-schema data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml
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
  - CultureMech:002109
  command: just validate-strict data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml
    --out REVIEW_WORK/batch072/record02/strict.tsv --workers 1 --quiet
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
  - CultureMech:002109
  command: just validate-terms data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml
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
  - CultureMech:002109
  command: just validate-references data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsmz935a
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf
  accessed_at: '2026-10-28T16:12:45.001549Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d
- evidence_id: dsmz935
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935.pdf
  accessed_at: '2026-10-28T16:12:45.021337Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/dsmz935.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 51e46137cd5697af28a63697cffca147b1496c494bbe2d726fc11e60040a75dc
- evidence_id: dsmz935b
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf
  accessed_at: '2026-10-28T16:12:44.846225Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439
- evidence_id: api935a
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/935a
  accessed_at: '2026-10-28T16:12:46.362826Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/api935a.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7
- evidence_id: api935
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/935
  accessed_at: '2026-10-28T16:12:45.923379Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/api935.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1
- evidence_id: api935b
  kind: search
  reference: https://mediadive.dsmz.de/rest/medium/935b
  accessed_at: '2026-10-28T16:12:46.307526Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/api935b.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: b5c9493e66496fb2c5d5e64c4bcf9675dd01382531706e8697e6092dc99dd8f1
  search_scope: One exact public GET of https://mediadive.dsmz.de/rest/medium/935b;
    retained status 404. No exhaustive repository or literature absence claim.
- evidence_id: komodo935
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=935
  accessed_at: '2026-10-28T16:12:46.561363Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/komodo935.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 6d0bd50a6bbede39b61f9af1ad428f2b5ea6d16040aa7ffea1760d6883923eab
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=935;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodo935dot1
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=935.1
  accessed_at: '2026-10-28T16:12:46.594920Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/komodo935dot1.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: cf777fc69c510155d04e40e965b0bcf7bf49cd7a5c293018c3e14b4cea045900
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=935.1;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodo935dash14783
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=935_14783
  accessed_at: '2026-10-28T16:12:46.563172Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/komodo935dash14783.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 61b70d2efe9f353d7d2faeae203da1e69ac6eb185212e1cf6607e17a90e382c4
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=935_14783;
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
- evidence_id: dsm14813
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-14813
  accessed_at: '2026-10-28T16:11:59.096402Z'
  locator: REVIEW_WORK/batch072/source01-03-preflight/dsm14813.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Exact selected-source identity preflight. Organism/source
    context screened before any operational assessment; no source transfer between
    variants.
  snapshot_sha256: 9fea7d4efcf3b63c20115632ae6de48e4352d87dfd8b3291558c541466a51755
- evidence_id: dsm14783
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-14783
  accessed_at: '2026-10-28T16:11:59.223194Z'
  locator: REVIEW_WORK/batch072/source01-03-preflight/dsm14783.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Exact selected-source identity preflight. Organism/source
    context screened before any operational assessment; no source transfer between
    variants.
  snapshot_sha256: c5919e401d2691751a2e39c29eeae9751e2b9632576fdd9deabbad8a3ed5c58e
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T16:29:46.531863Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: a2b4f9cce996f35bd9da5d9bd12830abea7ac68180cc036f8a1e336cba9f35bb
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T16:29:46.532054Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 7ab424969123f8773724ce678eeb0e0041d5476e7299f3b3257926a7a50d435b
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T16:29:46.532091Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T16:29:46.532440Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T16:29:46.532464Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T16:29:46.532487Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T16:29:46.532517Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: 333e3af0864878a346746dce0d5ab1ef564b14d97828d12a18e941f1db199b8e
- evidence_id: owner-3
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_14813.yaml
  locator: Complete file
  accessed_at: '2026-10-28T16:29:46.532540Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: 0e9fa8185ca1d711b93606914aa0294de80c6312d696909e14b900d56a55885f
- evidence_id: owner-4
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml
  locator: Complete file
  accessed_at: '2026-10-28T16:29:46.532562Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: 73d3afe521e3a9412be956db4b45c046d3351615a278bea362cd517625337ac3
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T16:29:46.532586Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T16:29:46.540268Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 71abceea7264b1e221738ef08a36e3baf3838157c149d75cfdb0eb8ec1984fb4
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/for_dsm_14813.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T16:29:46.540330Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: c16a53980b4aaf78c379acb0695681cf2fcc08869a73626c2c40935119ee1daf
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/medium_935_modified_for_dsm_14783.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T16:29:46.540370Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: b6efd51f7d7b1f1f9c32dc9b837ca2c1cfc4aa4acf3c6c9b03e11531d1d87b99
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T16:29:46.540408Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 94e89303f14558d9b0d485aa6cb4eb646050837864ab920d759763a3a483b94f
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/deferribacter_desulfuricans_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T16:29:46.546199Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 377c275e5792e1377a9941ca4df580afe91d786b5f93ead9d67bba9c5e5cc596
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T16:29:46.546286Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: da4d2aba500bb2249d8d5cf642439d417fb02c9a9413bef159041d43d1227b8b
- evidence_id: report-26
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T16:29:46.546324Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 3f4553b6f7417e06413b23a5551e3f58cf15220399ec13dc5cbf3903a44de57f
- evidence_id: report-27
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T16:29:46.546352Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: d55e45715915e3671cddd31b8d3cde0b767dfce29b9154262d616e4795bed55c
- evidence_id: report-28
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_14813.md
  locator: Complete report
  accessed_at: '2026-10-28T16:29:46.546376Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 4dc1285ed3fcef05c976223a30f336567c2c1e96a0b3fdfeefe3399466811318
- evidence_id: report-29
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.md
  locator: Complete report
  accessed_at: '2026-10-28T16:29:46.546399Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: a231393b6c40a1396db016fe96f75a7cd8105415ba541f1990a093598e086bfb
- evidence_id: report-30
  kind: prior_review
  reference: reports/yaml_record_review/20260922T141339Z-deferribacter_desulfuricans_medium__99f27aac.md
  locator: Complete report
  accessed_at: '2026-10-28T16:29:46.546422Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 32bbac9ddb1c4f5cf5a3af068d568ea9c13f04377470fda99aabdec40cb2a134
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch072/record02/historical-reading.json
  accessed_at: '2026-10-28T16:29:46.546453Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete text of ten scoped historical reports; September comparison-target
    claims remain separate from the selected current record.
  snapshot_sha256: 9aa50e4879a0e38f833027af763cfbefdce0972f2f0b35784f71cc2838042d9a
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch072/record02/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T16:29:46.546577Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 52ad870cab237ad00202009664187ae872329de9bb17a5c5c65d606fa082b0d7
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch072/record02/complete-document-reader.json
  accessed_at: '2026-10-28T16:29:46.546685Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact selected target and all four maintained contributor documents,
    including full histories.
  snapshot_sha256: a18e68b0a29420f28cef45d490e5bfcfae949ecca0c5134fcd457895319b6879
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T16:29:46.546783Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: MediaQualityFixer._merge_ingredient_group
  accessed_at: '2026-10-28T16:29:46.546844Z'
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
  accessed_at: '2026-10-28T16:29:46.546872Z'
  support: context_only
  summary: Current parsing retains primary compounds and separate receiving stocks,
    excluding flattened stock composition. It prefers explicit g_l and skips input
    water; fallback unit conversion alone does not establish a denominator. The classifier
    chooses AUTOCLAVE before later filtration in a mixed paragraph.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.extract_dsmz_id; DSMZCompositionResolver.merge_composition
  accessed_at: '2026-10-28T16:29:46.546901Z'
  support: context_only
  summary: Current DSMZCompositionResolver strips letter suffixes from extracted accessions
    and copies ingredients/solutions; it does not establish source equivalence or
    copy full preparation. Historical events separately record DSMZ935 copies and
    must not be treated as proof that current code executed then.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-repair
  kind: record_content
  reference: scripts/repair_komodo_935_deferribacter_score10.py
  locator: Complete fixed signature, repair_parent and repair_child bodies
  accessed_at: '2026-10-28T16:29:46.546929Z'
  support: context_only
  summary: Current exact repair requires the shared 34-ingredient local signature,
    then promotes DSM935a and classifies KOMODO935 as duplicate and its strain wrappers
    as variants. It leaves distinct DSM935 out. This is local topology repair credit,
    not external accession or strain-formulation authentication.
  snapshot_sha256: 184a38264b2d89df9178ce6f669b254d3b649040ed2d07c36afdd1210abe8cb6
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
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158
  accessed_at: '2026-10-28T16:12:54.798368Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi86158.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: eacf58308fa876cb17661b82d08a64d9be24814fde8014ac82da7696b3684841
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
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  accessed_at: '2026-10-28T16:12:53.381988Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi63036.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
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
- evidence_id: chebi76208
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76208
  accessed_at: '2026-10-28T16:12:54.288491Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi76208.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 377325fb8ac82e955a97bfc7f530bb79edc66dcb329e791a28e3e907b27f11ba
- evidence_id: chebi44557
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:44557
  accessed_at: '2026-10-28T16:12:52.525515Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi44557.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 25e8fb689e4dfc294e2823ca36290cdce6d21ad174238e0e958ebe09d4c1262b
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31795
  accessed_at: '2026-10-28T16:12:50.948379Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi31795.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: ceb0c93d1964844e99454d74730971855710441d92eec74aff5c873c833e324a
- evidence_id: chebi86364
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86364
  accessed_at: '2026-10-28T16:12:55.729124Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi86364.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 6e685ea7654bc1f4e16b3e3a05d73d8541e84cddcc28de59c4ae57ac288a1505
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75836
  accessed_at: '2026-10-28T16:12:54.128376Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi75836.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: ab9922083bab0fb07df977855094d11fe3a5ca1f14bc6bddd10dc80ad9055569
- evidence_id: chebi91244
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91244
  accessed_at: '2026-10-28T16:12:56.363871Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi91244.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: c8bf30f1c2b4e9c2bcc10bd256b68a090795c083c207baf2d9d9ebb201d0d3c5
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312
  accessed_at: '2026-10-28T16:12:51.520793Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi32312.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 19bbc18dfc582e76457c6f08d51bb777a2f7a2cbd2f810cb3b58bdb0004b4d60
- evidence_id: chebi31440
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31440
  accessed_at: '2026-10-28T16:12:50.708708Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi31440.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: a0af950191bab322f858a701486e40e51a4780a18d9d03913d351b383f05cb7d
- evidence_id: chebi86465
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86465
  accessed_at: '2026-10-28T16:12:56.023443Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi86465.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 76cce7fa8230c57138e3569858ecf6a79119be85281bd5d2864ada3223785dc1
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
  reference: REVIEW_WORK/batch072/record02/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:29:46.854426Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 8bf9664ce48e6dd0eb25fe935e5b03781f9b1cc46442be0ed4752597d97908de
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch072/record02/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:29:46.854604Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: e6f3ee731d21d491ade6dfa27e7461a3af09e5f7d57c9123167dba594be2ab5f
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch072/record02/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:29:46.854833Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 3ff094d6e31b2ba869fb8f2e7091d79d9ed9b0ed40347ed7f6b4cd4ff4cede09
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch072/record02/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:29:46.854962Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: ce0e6b4832d4cd682da2ee08f214f4a44256d722cd30e859d06b7edf678e2dea
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch072/record02/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:29:46.855083Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: c281cd79cd9f0929b976e1b10de6e4f763d6686883ec1f87214829053e6c1390
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch072/record02/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:29:46.855121Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 9fc465916de2a57f64be9bcca0bafec2e9a2dca5cdc3a2537278e6c8dde5f352
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch072/record02/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:29:46.855145Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch072/record02/validate-schema.json
  accessed_at: '2026-10-28T16:12:03.549676Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 42a8c2b1278c2e64aa1962ef1ca8b56bc71245e801ffe75228d2f552a7cc1e07
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch072/record02/validate-strict.json
  accessed_at: '2026-10-28T16:12:04.515677Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: c1ec6df745119c5faab73b5c011a233a64befeffbfd254daa827e2aa02e9d108
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch072/record02/validate-terms.json
  accessed_at: '2026-10-28T16:12:05.588154Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: fb0380d513db10c799abc3712cb4bb54770e65d611b4996db81c4f8bfa711419
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch072/record02/validate-references.json
  accessed_at: '2026-10-28T16:12:06.355740Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: dc61fa7bcf2afa415efbd07ac4967f61b31e0ee0f9a0f541a16449ac5fff5db8
assessments:
- assessment_id: identity
  area: identity
  topic: Accession and variant scope
  outcome: concern
  summary: 935a source identity is distinguishable from the 935b linked PDF and 935
    base. Catalogue DSM 14813 and 14783 identities are different and do not by themselves
    validate either wrapper recipe.
  target_ids:
  - CultureMech:002109
  evidence_ids:
  - dsmz935a
  - dsmz935b
  - dsmz935
  - dsm14813
  - dsm14783
- assessment_id: classification
  area: scope
  topic: Basic record classification
  outcome: supported
  summary: Bacterial liquid complex/semi-defined representation is consistent with
    the selected 935a recipe containing yeast extract. Optional growth assertions
    are not inferred from names.
  target_ids:
  - CultureMech:002109
  evidence_ids:
  - target
  - dsmz935a
- assessment_id: evidence
  area: evidence
  topic: Unchanged supported rates and missing attached claims
  outcome: concern
  summary: Nine unsummed basal quantities have direct 935a primary-final-volume/provider
    support. Ca/Na mixed-stage sums and all stock-only root rates require correction;
    no existing attached quantity evidence can be credited as verified.
  target_ids:
  - CultureMech:002109
  evidence_ids:
  - quantities
  - dsmz935a
  - api935a
  - old-claims
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 170 current concentration fields are covered by 96 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:002109
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b072-quantity-inventory-v1","target":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","quantity_field_count":170,"decisions":[{"quantity_id":"q1","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 7-7","quote":"NH4Cl                                                  0.33       g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\":
    6.10225,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."}]},{"quantity_id":"q2","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 8-8","quote":"KCl                                                    0.33       g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\":
    4.3784,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."}]},{"quantity_id":"q3","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.42640900000000004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.42640900000000004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.42640900000000004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.42640900000000004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.42640900000000004","unit":"G_PER_L"}}],"decision":"conflict","rationale":"Stored
    0.42640900000000004 G_PER_L is the historical sum of the main rate 0.326409 and
    the full mineral-stock rate 0.1. The units look alike but the solution-stage bases
    differ, so the sum is invalid as a final-medium total. Preserve the two source
    additions separately; the mineral stock is received at 10 ml and the primary declares
    final main volume 1011 ml. No full-strength stock contribution can be added directly.","source_stage":"Main
    sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 9-9","quote":"CaCl2 x 2 H2O                                          0.33       g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\":
    2.22025,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 40-40","quote":"CaCl2 x 2 H2O                                          0.10        g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.680203,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative
    text"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 13-13","quote":"Modified Wolin''s mineral solution                     10.00      ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"conflict","rationale":"Stored
    0.42640900000000004 G_PER_L is the historical sum of the main rate 0.326409 and
    the full mineral-stock rate 0.1. The units look alike but the solution-stage bases
    differ, so the sum is invalid as a final-medium total. Preserve the two source
    additions separately; the mineral stock is received at 10 ml and the primary declares
    final main volume 1011 ml. No full-strength stock contribution can be added directly."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[2].concentration","decision":"conflict","rationale":"Stored
    0.42640900000000004 G_PER_L is the historical sum of the main rate 0.326409 and
    the full mineral-stock rate 0.1. The units look alike but the solution-stage bases
    differ, so the sum is invalid as a final-medium total. Preserve the two source
    additions separately; the mineral stock is received at 10 ml and the primary declares
    final main volume 1011 ml. No full-strength stock contribution can be added directly."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[2].concentration","decision":"conflict","rationale":"Stored
    0.42640900000000004 G_PER_L is the historical sum of the main rate 0.326409 and
    the full mineral-stock rate 0.1. The units look alike but the solution-stage bases
    differ, so the sum is invalid as a final-medium total. Preserve the two source
    additions separately; the mineral stock is received at 10 ml and the primary declares
    final main volume 1011 ml. No full-strength stock contribution can be added directly."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[2].concentration","decision":"conflict","rationale":"Stored
    0.42640900000000004 G_PER_L is the historical sum of the main rate 0.326409 and
    the full mineral-stock rate 0.1. The units look alike but the solution-stage bases
    differ, so the sum is invalid as a final-medium total. Preserve the two source
    additions separately; the mineral stock is received at 10 ml and the primary declares
    final main volume 1011 ml. No full-strength stock contribution can be added directly."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[2].concentration","decision":"conflict","rationale":"Stored
    0.42640900000000004 G_PER_L is the historical sum of the main rate 0.326409 and
    the full mineral-stock rate 0.1. The units look alike but the solution-stage bases
    differ, so the sum is invalid as a final-medium total. Preserve the two source
    additions separately; the mineral stock is received at 10 ml and the primary declares
    final main volume 1011 ml. No full-strength stock contribution can be added directly."}]},{"quantity_id":"q4","label":"MgCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 10-10","quote":"MgCl2 x 6 H2O                                          0.33       g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\":
    1.60553,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."}]},{"quantity_id":"q5","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.326409","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 11-11","quote":"KH2PO4                                                 0.33       g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\":
    2.39857,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The
    unchanged 0.326409 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.33 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."}]},{"quantity_id":"q6","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"25.728","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"25.728","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"25.728","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[5].concentration","stored":{"value":"25.728","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[5].concentration","stored":{"value":"25.728","unit":"G_PER_L"}}],"decision":"conflict","rationale":"Stored
    25.728 G_PER_L is the historical sum of the main rate 24.728 and the full mineral-stock
    rate 1. The units look alike but the solution-stage bases differ, so the sum is
    invalid as a final-medium total. Preserve the two source additions separately;
    the mineral stock is received at 10 ml and the primary declares final main volume
    1011 ml. No full-strength stock contribution can be added directly.","source_stage":"Main
    sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 12-12","quote":"NaCl                                                  25.00       g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 24.728,\n                        \"mmol_l\":
    423.135,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 37-37","quote":"NaCl                                                   1.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    17.1116,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative
    text"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 13-13","quote":"Modified Wolin''s mineral solution                     10.00      ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"conflict","rationale":"Stored
    25.728 G_PER_L is the historical sum of the main rate 24.728 and the full mineral-stock
    rate 1. The units look alike but the solution-stage bases differ, so the sum is
    invalid as a final-medium total. Preserve the two source additions separately;
    the mineral stock is received at 10 ml and the primary declares final main volume
    1011 ml. No full-strength stock contribution can be added directly."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[5].concentration","decision":"conflict","rationale":"Stored
    25.728 G_PER_L is the historical sum of the main rate 24.728 and the full mineral-stock
    rate 1. The units look alike but the solution-stage bases differ, so the sum is
    invalid as a final-medium total. Preserve the two source additions separately;
    the mineral stock is received at 10 ml and the primary declares final main volume
    1011 ml. No full-strength stock contribution can be added directly."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[5].concentration","decision":"conflict","rationale":"Stored
    25.728 G_PER_L is the historical sum of the main rate 24.728 and the full mineral-stock
    rate 1. The units look alike but the solution-stage bases differ, so the sum is
    invalid as a final-medium total. Preserve the two source additions separately;
    the mineral stock is received at 10 ml and the primary declares final main volume
    1011 ml. No full-strength stock contribution can be added directly."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[5].concentration","decision":"conflict","rationale":"Stored
    25.728 G_PER_L is the historical sum of the main rate 24.728 and the full mineral-stock
    rate 1. The units look alike but the solution-stage bases differ, so the sum is
    invalid as a final-medium total. Preserve the two source additions separately;
    the mineral stock is received at 10 ml and the primary declares final main volume
    1011 ml. No full-strength stock contribution can be added directly."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[5].concentration","decision":"conflict","rationale":"Stored
    25.728 G_PER_L is the historical sum of the main rate 24.728 and the full mineral-stock
    rate 1. The units look alike but the solution-stage bases differ, so the sum is
    invalid as a final-medium total. Preserve the two source additions separately;
    the mineral stock is received at 10 ml and the primary declares final main volume
    1011 ml. No full-strength stock contribution can be added directly."}]},{"quantity_id":"q7","label":"KNO3","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary
    0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to
    provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 14-14","quote":"KNO3                                                   0.50       g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"KNO3\",\n                        \"compound_id\":
    191,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.49456,\n                        \"mmol_l\":
    4.89164,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The
    unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary
    0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to
    provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The
    unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary
    0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to
    provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The
    unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary
    0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to
    provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The
    unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary
    0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to
    provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The
    unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary
    0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to
    provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."}]},{"quantity_id":"q8","label":"Na-acetate","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.791296","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.791296","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.791296","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.791296","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.791296","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    unchanged 0.791296 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.8 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 15-15","quote":"Na-acetate                                             0.80       g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\":
    23,\n                        \"amount\": 0.8,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.791296,\n                        \"mmol_l\":
    9.64597,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The
    unchanged 0.791296 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.8 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The
    unchanged 0.791296 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.8 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The
    unchanged 0.791296 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.8 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The
    unchanged 0.791296 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.8 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The
    unchanged 0.791296 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.8 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."}]},{"quantity_id":"q9","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary
    0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to
    provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 16-16","quote":"Yeast extract                                          0.50       g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.49456,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The
    unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary
    0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to
    provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The
    unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary
    0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to
    provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"The
    unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary
    0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to
    provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The
    unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary
    0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to
    provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The
    unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary
    0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to
    provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."}]},{"quantity_id":"q10","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.49456","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary
    0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to
    provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 17-17","quote":"Na2CO3                                                 0.50       g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.49456,\n                        \"mmol_l\":
    4.66619,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The
    unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary
    0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to
    provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The
    unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary
    0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to
    provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"The
    unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary
    0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to
    provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The
    unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary
    0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to
    provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The
    unchanged 0.49456 G_PER_L agrees with the explicit provider main g_l and the primary
    0.5 g batch amount divided by the explicitly printed 1.011 L final volume, to
    provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."}]},{"quantity_id":"q11","label":"Na2S","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.296736","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.296736","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.296736","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.296736","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.296736","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    unchanged 0.296736 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.3 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source.","source_stage":"Main sol. 935a; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 19-19","quote":"Na2S                                                   0.30       g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Na2S\",\n                        \"compound_id\":
    490,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.296736,\n                        \"mmol_l\":
    3.7533,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 3-4","quote":"Final pH: 6.5\nFinal volume: 1011 ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The
    unchanged 0.296736 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.3 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The
    unchanged 0.296736 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.3 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"The
    unchanged 0.296736 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.3 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Exact selected DSM935a source support; no attached claim."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The
    unchanged 0.296736 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.3 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The
    unchanged 0.296736 G_PER_L agrees with the explicit provider main g_l and the
    primary 0.3 g batch amount divided by the explicitly printed 1.011 L final volume,
    to provider precision. Credit the DSM935a target/owner on that actual basis, not
    on input water. The three KOMODO copies are not independently supported by this
    distinct source. Unavailable exact KOMODO recipe; copied935a values are not independently
    verified."}]},{"quantity_id":"q12","label":"Nitrilotriacetic acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Nitrilotriacetic acid in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml.","source_stage":"Modified Wolin''s mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 34-34","quote":"Nitrilotriacetic acid                                  1.50        g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\":
    189,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.84765,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Nitrilotriacetic acid in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[11].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Nitrilotriacetic acid in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[11].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Nitrilotriacetic acid in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[11].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Nitrilotriacetic acid in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[11].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Nitrilotriacetic acid in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."}]},{"quantity_id":"q13","label":"MgSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[12].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for MgSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Modified
    Wolin''s mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 35-35","quote":"MgSO4 x 7 H2O                                          3.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    12.1716,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for MgSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for MgSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for MgSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for MgSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for MgSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q14","label":"MnSO4
    x H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for MnSO4 x H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Modified
    Wolin''s mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 36-36","quote":"MnSO4 x H2O                                            0.50        g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\":
    14,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.9583,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for MnSO4 x H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for MnSO4 x H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for MnSO4 x H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for MnSO4 x H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for MnSO4 x H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q15","label":"FeSO4
    x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for FeSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Modified
    Wolin''s mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 38-38","quote":"FeSO4 x 7 H2O                                          0.10        g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.359693,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for FeSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for FeSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for FeSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for FeSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for FeSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q16","label":"CoSO4
    x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.18","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for CoSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Modified
    Wolin''s mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 39-39","quote":"CoSO4 x 7 H2O                                          0.18        g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\":
    198,\n                        \"amount\": 0.18,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\":
    1.16132,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for CoSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for CoSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for CoSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for CoSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for CoSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q17","label":"ZnSO4
    x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.18","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for ZnSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Modified
    Wolin''s mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 41-41","quote":"ZnSO4 x 7 H2O                                          0.18        g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":
    35,\n                        \"amount\": 0.18,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\":
    0.625954,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for ZnSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for ZnSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for ZnSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for ZnSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for ZnSO4 x 7 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q18","label":"CuSO4
    x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for CuSO4 x 5 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Modified
    Wolin''s mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 42-42","quote":"CuSO4 x 5 H2O                                          0.01        g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\":
    121,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0400503,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for CuSO4 x 5 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for CuSO4 x 5 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for CuSO4 x 5 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for CuSO4 x 5 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for CuSO4 x 5 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q19","label":"AlK(SO4)2
    x 12 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for AlK(SO4)2 x 12 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml.","source_stage":"Modified Wolin''s mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 43-43","quote":"AlK(SO4)2 x 12 H2O                                     0.02        g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\":
    908,\n                        \"amount\": 0.02,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0421596,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for AlK(SO4)2 x 12 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for AlK(SO4)2 x 12 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for AlK(SO4)2 x 12 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for AlK(SO4)2 x 12 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for AlK(SO4)2 x 12 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."}]},{"quantity_id":"q20","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for H3BO3 in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Modified
    Wolin''s mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 44-44","quote":"H3BO3                                                  0.01        g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.161708,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for H3BO3 in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for H3BO3 in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for H3BO3 in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for H3BO3 in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for H3BO3 in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q21","label":"Na2MoO4
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Na2MoO4 x 2 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml.","source_stage":"Modified Wolin''s mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 45-45","quote":"Na2MoO4 x 2 H2O                                        0.01        g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0413309,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Na2MoO4 x 2 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Na2MoO4 x 2 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Na2MoO4 x 2 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Na2MoO4 x 2 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Na2MoO4 x 2 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."}]},{"quantity_id":"q22","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for NiCl2 x 6 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml. The
    primary explicitly supplies nickel hexahydrate; the local anhydrous ontology term
    is a separate error.","source_stage":"Modified Wolin''s mineral solution; no KOMODO
    variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 46-46","quote":"NiCl2 x 6 H2O                                          0.03        g","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.231483,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for NiCl2 x 6 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml. The
    primary explicitly supplies nickel hexahydrate; the local anhydrous ontology term
    is a separate error."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for NiCl2 x 6 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml. The
    primary explicitly supplies nickel hexahydrate; the local anhydrous ontology term
    is a separate error."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for NiCl2 x 6 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml. The
    primary explicitly supplies nickel hexahydrate; the local anhydrous ontology term
    is a separate error."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for NiCl2 x 6 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml. The
    primary explicitly supplies nickel hexahydrate; the local anhydrous ontology term
    is a separate error."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for NiCl2 x 6 H2O in Modified Wolin''s
    mineral solution, but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml. The
    primary explicitly supplies nickel hexahydrate; the local anhydrous ontology term
    is a separate error."}]},{"quantity_id":"q23","label":"Na2SeO3 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.0003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.0003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.0003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.0003","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.0003","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Na2SeO3 x 5 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml.","source_stage":"Modified Wolin''s mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 56-56","quote":"Na2SeO3 x 5 H2O                                           0.30       mg","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\":
    0.00114062,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Na2SeO3 x 5 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Na2SeO3 x 5 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Na2SeO3 x 5 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Na2SeO3 x 5 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Na2SeO3 x 5 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."}]},{"quantity_id":"q24","label":"Na2WO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.0004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.0004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.0004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.0004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.0004","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Na2WO4 x 2 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml.","source_stage":"Modified Wolin''s mineral solution; no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 57-57","quote":"Na2WO4 x 2 H2O                                            0.40       mg","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[14]","quote":"{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0004,\n                        \"mmol_l\":
    0.00121267,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Na2WO4 x 2 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Na2WO4 x 2 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Na2WO4 x 2 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Na2WO4 x 2 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Na2WO4 x 2 H2O in Modified
    Wolin''s mineral solution, but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."}]},{"quantity_id":"q25","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Biotin in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Wolin''s
    vitamin solution (10x); no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 66-66","quote":"Biotin                                                   20.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Biotin in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Biotin in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Biotin in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Biotin in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Biotin in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q26","label":"Folic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Folic acid in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Wolin''s
    vitamin solution (10x); no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 67-67","quote":"Folic acid                                               20.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Folic acid in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Folic acid in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Folic acid in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Folic acid in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Folic acid in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q27","label":"Pyridoxine
    hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Pyridoxine hydrochloride in
    Wolin''s vitamin solution (10x), but its placement in main ingredients is wrong.
    Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml
    vitamin stock); no full stock strength is a final-medium concentration. The primary
    prints stock input water, while the provider explicitly normalizes the stock to
    1000 ml.","source_stage":"Wolin''s vitamin solution (10x); no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 68-68","quote":"Pyridoxine hydrochloride                                100.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Pyridoxine hydrochloride in
    Wolin''s vitamin solution (10x), but its placement in main ingredients is wrong.
    Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml
    vitamin stock); no full stock strength is a final-medium concentration. The primary
    prints stock input water, while the provider explicitly normalizes the stock to
    1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Pyridoxine hydrochloride in
    Wolin''s vitamin solution (10x), but its placement in main ingredients is wrong.
    Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml
    vitamin stock); no full stock strength is a final-medium concentration. The primary
    prints stock input water, while the provider explicitly normalizes the stock to
    1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Pyridoxine hydrochloride in
    Wolin''s vitamin solution (10x), but its placement in main ingredients is wrong.
    Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml
    vitamin stock); no full stock strength is a final-medium concentration. The primary
    prints stock input water, while the provider explicitly normalizes the stock to
    1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Pyridoxine hydrochloride in
    Wolin''s vitamin solution (10x), but its placement in main ingredients is wrong.
    Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml
    vitamin stock); no full stock strength is a final-medium concentration. The primary
    prints stock input water, while the provider explicitly normalizes the stock to
    1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Pyridoxine hydrochloride in
    Wolin''s vitamin solution (10x), but its placement in main ingredients is wrong.
    Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml
    vitamin stock); no full stock strength is a final-medium concentration. The primary
    prints stock input water, while the provider explicitly normalizes the stock to
    1000 ml."}]},{"quantity_id":"q28","label":"Thiamine HCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Thiamine HCl in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Wolin''s
    vitamin solution (10x); no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 69-69","quote":"Thiamine HCl                                             50.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Thiamine HCl in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Thiamine HCl in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Thiamine HCl in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Thiamine HCl in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Thiamine HCl in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q29","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Riboflavin in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Wolin''s
    vitamin solution (10x); no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 70-70","quote":"Riboflavin                                               50.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Riboflavin in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Riboflavin in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Riboflavin in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Riboflavin in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Riboflavin in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q30","label":"Nicotinic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Nicotinic acid in Wolin''s
    vitamin solution (10x), but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml.","source_stage":"Wolin''s vitamin solution (10x); no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 71-71","quote":"Nicotinic acid                                           50.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Nicotinic acid in Wolin''s
    vitamin solution (10x), but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Nicotinic acid in Wolin''s
    vitamin solution (10x), but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Nicotinic acid in Wolin''s
    vitamin solution (10x), but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Nicotinic acid in Wolin''s
    vitamin solution (10x), but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Nicotinic acid in Wolin''s
    vitamin solution (10x), but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."}]},{"quantity_id":"q31","label":"Calcium D-(+)-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[30].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Calcium D-(+)-pantothenate
    in Wolin''s vitamin solution (10x), but its placement in main ingredients is wrong.
    Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml
    vitamin stock); no full stock strength is a final-medium concentration. The primary
    prints stock input water, while the provider explicitly normalizes the stock to
    1000 ml. D-calcium pantothenate identity is supported by the current stereochemical
    ontology object; no mass-convention correction is inferred.","source_stage":"Wolin''s
    vitamin solution (10x); no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 72-72","quote":"Calcium D-(+)-pantothenate                               50.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Calcium D-(+)-pantothenate
    in Wolin''s vitamin solution (10x), but its placement in main ingredients is wrong.
    Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml
    vitamin stock); no full stock strength is a final-medium concentration. The primary
    prints stock input water, while the provider explicitly normalizes the stock to
    1000 ml. D-calcium pantothenate identity is supported by the current stereochemical
    ontology object; no mass-convention correction is inferred."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Calcium D-(+)-pantothenate
    in Wolin''s vitamin solution (10x), but its placement in main ingredients is wrong.
    Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml
    vitamin stock); no full stock strength is a final-medium concentration. The primary
    prints stock input water, while the provider explicitly normalizes the stock to
    1000 ml. D-calcium pantothenate identity is supported by the current stereochemical
    ontology object; no mass-convention correction is inferred."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Calcium D-(+)-pantothenate
    in Wolin''s vitamin solution (10x), but its placement in main ingredients is wrong.
    Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml
    vitamin stock); no full stock strength is a final-medium concentration. The primary
    prints stock input water, while the provider explicitly normalizes the stock to
    1000 ml. D-calcium pantothenate identity is supported by the current stereochemical
    ontology object; no mass-convention correction is inferred."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Calcium D-(+)-pantothenate
    in Wolin''s vitamin solution (10x), but its placement in main ingredients is wrong.
    Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml
    vitamin stock); no full stock strength is a final-medium concentration. The primary
    prints stock input water, while the provider explicitly normalizes the stock to
    1000 ml. D-calcium pantothenate identity is supported by the current stereochemical
    ontology object; no mass-convention correction is inferred."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Calcium D-(+)-pantothenate
    in Wolin''s vitamin solution (10x), but its placement in main ingredients is wrong.
    Retain the stock amount and its distinct receiving dose (10 ml mineral or 1 ml
    vitamin stock); no full stock strength is a final-medium concentration. The primary
    prints stock input water, while the provider explicitly normalizes the stock to
    1000 ml. D-calcium pantothenate identity is supported by the current stereochemical
    ontology object; no mass-convention correction is inferred."}]},{"quantity_id":"q32","label":"Vitamin
    B12","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.001","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Vitamin B12 in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml.","source_stage":"Wolin''s
    vitamin solution (10x); no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 73-73","quote":"Vitamin B12                                               1.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Vitamin B12 in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Vitamin B12 in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Vitamin B12 in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Vitamin B12 in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for Vitamin B12 in Wolin''s vitamin
    solution (10x), but its placement in main ingredients is wrong. Retain the stock
    amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin stock);
    no full stock strength is a final-medium concentration. The primary prints stock
    input water, while the provider explicitly normalizes the stock to 1000 ml."}]},{"quantity_id":"q33","label":"p-Aminobenzoic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for p-Aminobenzoic acid in Wolin''s
    vitamin solution (10x), but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml.","source_stage":"Wolin''s vitamin solution (10x); no KOMODO variant transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 74-74","quote":"p-Aminobenzoic acid                                      50.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for p-Aminobenzoic acid in Wolin''s
    vitamin solution (10x), but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for p-Aminobenzoic acid in Wolin''s
    vitamin solution (10x), but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for p-Aminobenzoic acid in Wolin''s
    vitamin solution (10x), but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for p-Aminobenzoic acid in Wolin''s
    vitamin solution (10x), but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for p-Aminobenzoic acid in Wolin''s
    vitamin solution (10x), but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml."}]},{"quantity_id":"q34","label":"(DL)-alpha-Lipoic acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for (DL)-alpha-Lipoic acid in Wolin''s
    vitamin solution (10x), but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml. A non-stereospecific lipoic-acid term is compatible with the explicit DL source
    designation.","source_stage":"Wolin''s vitamin solution (10x); no KOMODO variant
    transfer","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 75-75","quote":"(DL)-alpha-Lipoic acid                                   50.00       mg","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for (DL)-alpha-Lipoic acid in Wolin''s
    vitamin solution (10x), but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml. A non-stereospecific lipoic-acid term is compatible with the explicit DL source
    designation."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for (DL)-alpha-Lipoic acid in Wolin''s
    vitamin solution (10x), but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml. A non-stereospecific lipoic-acid term is compatible with the explicit DL source
    designation."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for (DL)-alpha-Lipoic acid in Wolin''s
    vitamin solution (10x), but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml. A non-stereospecific lipoic-acid term is compatible with the explicit DL source
    designation."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for (DL)-alpha-Lipoic acid in Wolin''s
    vitamin solution (10x), but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml. A non-stereospecific lipoic-acid term is compatible with the explicit DL source
    designation."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The
    unchanged number equals the provider stock g_l for (DL)-alpha-Lipoic acid in Wolin''s
    vitamin solution (10x), but its placement in main ingredients is wrong. Retain
    the stock amount and its distinct receiving dose (10 ml mineral or 1 ml vitamin
    stock); no full stock strength is a final-medium concentration. The primary prints
    stock input water, while the provider explicitly normalizes the stock to 1000
    ml. A non-stereospecific lipoic-acid term is compatible with the explicit DL source
    designation."}]},{"quantity_id":"q35","label":"Modified Wolin''s mineral solution
    0","local_fields":[],"decision":"evidence_only","rationale":"Exact source-only
    receiving addition or solvent input; preserve its own stock/main stage and printed
    unit. Main final volume is explicitly 1011 ml; stock input water is not independently
    a measured final volume.","source_stage":"Main sol. 935a","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 13-13","quote":"Modified Wolin''s mineral solution                     10.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Modified Wolin''s mineral solution\",\n                        \"solution_id\":
    241,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q36","label":"Wolin''s vitamin
    solution (10x) 0","local_fields":[],"decision":"evidence_only","rationale":"Exact
    source-only receiving addition or solvent input; preserve its own stock/main stage
    and printed unit. Main final volume is explicitly 1011 ml; stock input water is
    not independently a measured final volume.","source_stage":"Main sol. 935a","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 18-18","quote":"Wolin''s vitamin solution (10x)                         1.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q37","label":"Distilled water
    0","local_fields":[],"decision":"evidence_only","rationale":"Exact source-only
    receiving addition or solvent input; preserve its own stock/main stage and printed
    unit. Main final volume is explicitly 1011 ml; stock input water is not independently
    a measured final volume.","source_stage":"Main sol. 935a","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 20-20","quote":"Distilled water                                     1000.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q38","label":"Distilled water
    1","local_fields":[],"decision":"evidence_only","rationale":"Exact source-only
    receiving addition or solvent input; preserve its own stock/main stage and printed
    unit. Main final volume is explicitly 1011 ml; stock input water is not independently
    a measured final volume.","source_stage":"Modified Wolin''s mineral solution","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 58-58","quote":"Distilled water                                        1000.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[1].recipe[15]","quote":"{\n                        \"recipe_order\":
    16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q39","label":"Distilled water
    2","local_fields":[],"decision":"evidence_only","rationale":"Exact source-only
    receiving addition or solvent input; preserve its own stock/main stage and printed
    unit. Main final volume is explicitly 1011 ml; stock input water is not independently
    a measured final volume.","source_stage":"Wolin''s vitamin solution (10x)","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 76-76","quote":"Distilled water                                        1000.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api935a","reference":"https://mediadive.dsmz.de/rest/medium/935a","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935a.bin","raw_sha256":"d911c06556e069455bbcfd580397f4c1f8cd065db00d2d282c7d626edbc185e7","text_sha256":"1c85d270e8ddb9a2affd4c6dff826033d3a3939016e65e57f98d67da51870312","accessed_at":"2026-10-28T16:12:46.362826Z","locator":"data.solutions[2].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q40","label":"Explicit DSM935a
    final volume","local_fields":[],"decision":"evidence_only","rationale":"Unlike
    the bare solvent inputs, this primary header explicitly states final volume 1011
    ml. It supports main batch-to-rate arithmetic; do not replace it with an assumed
    1 L. This basis is not transferred to DSM935, DSM935b or unavailable KOMODO variants.","source_stage":"DSM935a
    final main medium","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 1-4","quote":"935a: DEFERRIBACTER DESULFURICANS MEDIUM\n\nFinal pH: 6.5\nFinal
    volume: 1011 ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q41","label":"DSM935a
    preparation and numeric controls","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve
    ingredients (except carbonate, vitamins and sulfide), then sparge medium with  80%
    H2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium
    under the same gas atmosphere into anoxic Hungate-type tubes or serum vials to
    30% of their volume and autoclave. Add vitamins and sulfide from sterile anoxic
    stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration.
    Add carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20%
    CO2 gas atmosphere. The pH of the complete medium should be 6.5."}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve
    ingredients (except carbonate, vitamins and sulfide), then sparge medium with  80%
    H2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium
    under the same gas atmosphere into anoxic Hungate-type tubes or serum vials to
    30% of their volume and autoclave. Add vitamins and sulfide from sterile anoxic
    stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration.
    Add carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20%
    CO2 gas atmosphere. The pH of the complete medium should be 6.5."}}],"decision":"evidence_only","rationale":"Existing
    prose retains the correct 80/20 H2/CO2, 30–45 min, 30% vessel-fill, late additions,
    100% nitrogen stock and 80/20 nitrogen/carbon-dioxide carbonate contexts, and
    pH6.5. Preserve those numeric controls; split the single AUTOCLAVE action into
    appropriately scoped actions. Unstated autoclave settings and late-stock strengths/volumes
    remain unknown. Do not substitute the differing935 or935b preparation.","source_stage":"DSM935a
    main preparation","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 22-28","quote":"Dissolve ingredients (except carbonate, vitamins and sulfide),
    then sparge medium with\n80% H2 and 20% CO2 gas mixture for 30 - 45 min to make
    it anoxic. Dispense medium\nunder the same gas atmosphere into anoxic Hungate-type
    tubes or serum vials to 30% of\ntheir volume and autoclave. Add vitamins and sulfide
    from sterile anoxic stock solutions\nprepared under 100% N2 gas. Vitamins should
    be sterilized by filtration. Add carbonate\nfrom a sterile anoxic stock solution
    prepared under 80% N2 and 20% CO2 gas atmosphere.\nThe pH of the complete medium
    should be 6.5.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"Existing
    prose retains the correct 80/20 H2/CO2, 30–45 min, 30% vessel-fill, late additions,
    100% nitrogen stock and 80/20 nitrogen/carbon-dioxide carbonate contexts, and
    pH6.5. Preserve those numeric controls; split the single AUTOCLAVE action into
    appropriately scoped actions. Unstated autoclave settings and late-stock strengths/volumes
    remain unknown. Do not substitute the differing935 or935b preparation."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"Existing
    prose retains the correct 80/20 H2/CO2, 30–45 min, 30% vessel-fill, late additions,
    100% nitrogen stock and 80/20 nitrogen/carbon-dioxide carbonate contexts, and
    pH6.5. Preserve those numeric controls; split the single AUTOCLAVE action into
    appropriately scoped actions. Unstated autoclave settings and late-stock strengths/volumes
    remain unknown. Do not substitute the differing935 or935b preparation."}]},{"quantity_id":"q42","label":"Mineral
    stock pH preparation","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"ADJUST_PH","description":"First
    dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals.
    Adjust final to pH 7.0 with KOH."}},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"ADJUST_PH","description":"First
    dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals.
    Adjust final to pH 7.0 with KOH."}}],"decision":"conflict","rationale":"The retained
    pH6.5 then7.0 sequence with KOH is supported for the mineral stock, not the final
    medium. Move its scope without changing source digits. KOH amount/strength is
    unspecified; do not invent either.","source_stage":"Modified Wolin mineral stock
    only","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 60-61","quote":"First dissolve nitrilotriacetic acid and adjust pH to 6.5
    with KOH, then add minerals. Adjust\nfinal to pH 7.0 with KOH.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"preparation_steps[1]","decision":"conflict","rationale":"The
    retained pH6.5 then7.0 sequence with KOH is supported for the mineral stock, not
    the final medium. Move its scope without changing source digits. KOH amount/strength
    is unspecified; do not invent either."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"preparation_steps[1]","decision":"conflict","rationale":"The
    retained pH6.5 then7.0 sequence with KOH is supported for the mineral stock, not
    the final medium. Move its scope without changing source digits. KOH amount/strength
    is unspecified; do not invent either."}]},{"quantity_id":"q43","label":"Separate
    pH assertions","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ph_value","stored":6.5},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ph_value","stored":7.0},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ph_value","stored":6.5},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ph_value","stored":7.0},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ph_value","stored":6.5}],"decision":"mixed","rationale":"DSM935a
    target/owner pH6.5 is supported. The copied wrapper values6.5/7.0 require their
    own exact source; fresh KOMODO routes are403. DSM935 gives6.5–6.7 and935b gives7.0,
    so neither is an interchangeable correction.","source_stage":"Independent accession-specific
    pH","sources":[{"evidence_id":"dsmz935a","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935a.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935a.bin","raw_sha256":"e32d5c03dc0866f594adbf9267d0b0a1539ee1dd029350fbd04226aa0f35921d","text_sha256":"ec825888fe61d71a2a417745519f611d1a11533e5a3ba55d9652ec44512c3826","accessed_at":"2026-10-28T16:12:45.001549Z","locator":"dsmz935a.txt
    lines 3-3","quote":"Final pH: 6.5","quote_basis":"derivative text"},{"evidence_id":"dsmz935","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935.bin","raw_sha256":"51e46137cd5697af28a63697cffca147b1496c494bbe2d726fc11e60040a75dc","text_sha256":"f440ea58c8d679c4b2f2b2340b66ef07d1ae24854cea34b98225058bb56c89c5","accessed_at":"2026-10-28T16:12:45.021337Z","locator":"Exact
    primary pH sentence","quote":"complete medium should be 6.5 - 6.7.","quote_basis":"derivative
    text"},{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt
    lines 18-23","quote":"Dissolve ingredients (except bicarbonate and vitamins),
    then sparge medium with 100%\nN2 gas for 30 – 45 min to make it anoxic. Adjust
    pH to 7.0 and dispense medium under\nsame gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave. Add\nvitamins from an anoxic stock solution
    prepared under 100% N2 gas and sterilized by\nfiltration and bicarbonate from
    a sterile anoxic stock solution prepared under 80% N2\nand 20% CO2 gas atmosphere.
    The pH of the complete medium should be 7.0.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"DSM935a
    target/owner pH6.5 is supported. The copied wrapper values6.5/7.0 require their
    own exact source; fresh KOMODO routes are403. DSM935 gives6.5–6.7 and935b gives7.0,
    so neither is an interchangeable correction."},{"path":"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml","field_path":"ph_value","decision":"unsupported","rationale":"DSM935a
    target/owner pH6.5 is supported. The copied wrapper values6.5/7.0 require their
    own exact source; fresh KOMODO routes are403. DSM935 gives6.5–6.7 and935b gives7.0,
    so neither is an interchangeable correction."},{"path":"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"DSM935a
    target/owner pH6.5 is supported. The copied wrapper values6.5/7.0 require their
    own exact source; fresh KOMODO routes are403. DSM935 gives6.5–6.7 and935b gives7.0,
    so neither is an interchangeable correction."},{"path":"data/normalized_yaml/bacterial/for_dsm_14813.yaml","field_path":"ph_value","decision":"unsupported","rationale":"DSM935a
    target/owner pH6.5 is supported. The copied wrapper values6.5/7.0 require their
    own exact source; fresh KOMODO routes are403. DSM935 gives6.5–6.7 and935b gives7.0,
    so neither is an interchangeable correction."},{"path":"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml","field_path":"ph_value","decision":"unsupported","rationale":"DSM935a
    target/owner pH6.5 is supported. The copied wrapper values6.5/7.0 require their
    own exact source; fresh KOMODO routes are403. DSM935 gives6.5–6.7 and935b gives7.0,
    so neither is an interchangeable correction."}]},{"quantity_id":"q44","label":"DSM935b
    comparison: NH4Cl                                                        0.33       g","local_fields":[],"decision":"evidence_only","rationale":"Exact
    distinct935b batch row, inventoried to expose the wrong linked PDF. It does not
    override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion
    differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only
    DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt
    lines 4-4","quote":"NH4Cl                                                        0.33       g","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q45","label":"DSM935b comparison:
    KCl                                                          0.33       g","local_fields":[],"decision":"evidence_only","rationale":"Exact
    distinct935b batch row, inventoried to expose the wrong linked PDF. It does not
    override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion
    differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only
    DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt
    lines 5-5","quote":"KCl                                                          0.33       g","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q46","label":"DSM935b comparison:
    CaCl2 x 2 H2O                                                0.33       g","local_fields":[],"decision":"evidence_only","rationale":"Exact
    distinct935b batch row, inventoried to expose the wrong linked PDF. It does not
    override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion
    differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only
    DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt
    lines 6-6","quote":"CaCl2 x 2 H2O                                                0.33       g","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q47","label":"DSM935b comparison:
    MgCl2 x 6 H2O                                                0.33       g","local_fields":[],"decision":"evidence_only","rationale":"Exact
    distinct935b batch row, inventoried to expose the wrong linked PDF. It does not
    override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion
    differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only
    DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt
    lines 7-7","quote":"MgCl2 x 6 H2O                                                0.33       g","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q48","label":"DSM935b comparison:
    KH2PO4                                                       0.33       g","local_fields":[],"decision":"evidence_only","rationale":"Exact
    distinct935b batch row, inventoried to expose the wrong linked PDF. It does not
    override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion
    differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only
    DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt
    lines 8-8","quote":"KH2PO4                                                       0.33       g","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q49","label":"DSM935b comparison:
    NaCl                                                        25.00       g","local_fields":[],"decision":"evidence_only","rationale":"Exact
    distinct935b batch row, inventoried to expose the wrong linked PDF. It does not
    override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion
    differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only
    DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt
    lines 9-9","quote":"NaCl                                                        25.00       g","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q50","label":"DSM935b comparison:
    Modified Wolin’s mineral solution (see medium 141)          10.00      ml","local_fields":[],"decision":"evidence_only","rationale":"Exact
    distinct935b batch row, inventoried to expose the wrong linked PDF. It does not
    override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion
    differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only
    DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt
    lines 10-10","quote":"Modified Wolin’s mineral solution (see medium 141)          10.00      ml","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q51","label":"DSM935b comparison:
    KNO3                                                         0.50       g","local_fields":[],"decision":"evidence_only","rationale":"Exact
    distinct935b batch row, inventoried to expose the wrong linked PDF. It does not
    override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion
    differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only
    DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt
    lines 11-11","quote":"KNO3                                                         0.50       g","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q52","label":"DSM935b comparison:
    Na-acetate                                                   2.00       g","local_fields":[],"decision":"evidence_only","rationale":"Exact
    distinct935b batch row, inventoried to expose the wrong linked PDF. It does not
    override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion
    differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only
    DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt
    lines 12-12","quote":"Na-acetate                                                   2.00       g","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q53","label":"DSM935b comparison:
    Yeast extract                                                0.15       g","local_fields":[],"decision":"evidence_only","rationale":"Exact
    distinct935b batch row, inventoried to expose the wrong linked PDF. It does not
    override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion
    differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only
    DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt
    lines 13-13","quote":"Yeast extract                                                0.15       g","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q54","label":"DSM935b comparison:
    NaHCO3                                                       0.30       g","local_fields":[],"decision":"evidence_only","rationale":"Exact
    distinct935b batch row, inventoried to expose the wrong linked PDF. It does not
    override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion
    differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only
    DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt
    lines 14-14","quote":"NaHCO3                                                       0.30       g","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q55","label":"DSM935b comparison:
    Wolin''s vitamin solution (see medium 141)                   10.00      ml","local_fields":[],"decision":"evidence_only","rationale":"Exact
    distinct935b batch row, inventoried to expose the wrong linked PDF. It does not
    override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion
    differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only
    DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt
    lines 15-15","quote":"Wolin''s vitamin solution (see medium 141)                   10.00      ml","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q56","label":"DSM935b comparison:
    Distilled water                                           1000.00      ml","local_fields":[],"decision":"evidence_only","rationale":"Exact
    distinct935b batch row, inventoried to expose the wrong linked PDF. It does not
    override935a: acetate, yeast, bicarbonate, vitamin dose/form and sulfide inclusion
    differ. The printed1000ml is input water, not an explicit final-volume statement.","source_stage":"Comparison-only
    DSM935b; not transferred","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt
    lines 16-16","quote":"Distilled water                                           1000.00      ml","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q57","label":"DSM935b preparation
    comparison","local_fields":[],"decision":"evidence_only","rationale":"This distinct
    source uses nitrogen-based preparation and pH7.0; it does not support replacing935a
    hydrogen/carbon-dioxide preparation. Preserve the difference and the exact source
    link mismatch.","source_stage":"Comparison-only DSM935b","sources":[{"evidence_id":"dsmz935b","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935b.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935b.bin","raw_sha256":"13e3d37833cdcef6dde802a28993f5afdd643420e59a1532cb4c5fe96f055439","text_sha256":"48b4fb3ecfac3f195141c213ac0510b423d6c4fde9c734ac5a3691d83b3c6d26","accessed_at":"2026-10-28T16:12:44.846225Z","locator":"dsmz935b.txt
    lines 18-23","quote":"Dissolve ingredients (except bicarbonate and vitamins),
    then sparge medium with 100%\nN2 gas for 30 – 45 min to make it anoxic. Adjust
    pH to 7.0 and dispense medium under\nsame gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave. Add\nvitamins from an anoxic stock solution
    prepared under 100% N2 gas and sterilized by\nfiltration and bicarbonate from
    a sterile anoxic stock solution prepared under 80% N2\nand 20% CO2 gas atmosphere.
    The pH of the complete medium should be 7.0.","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q58","label":"DSM935
    comparison: NH4Cl","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.997009,\n                        \"mmol_l\":
    18.6392,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q59","label":"DSM935 comparison:
    K2HPO4","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935
    source row, retained with its own main/stock stage. Different basal salts, pyruvate
    and three receiving stocks demonstrate that matching a number without its accession/suffix
    is insufficient. Provider g_l is explicit but primary final main volume is not;
    no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.08,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0797607,\n                        \"mmol_l\":
    0.457932,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q60","label":"DSM935 comparison:
    MgCl2 x 6 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 4.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4.48654,\n                        \"mmol_l\":
    22.0682,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q61","label":"DSM935 comparison:
    CaCl2 x 2 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.38,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.378863,\n                        \"mmol_l\":
    2.57704,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q62","label":"DSM935 comparison:
    NaCl","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935
    source row, retained with its own main/stock stage. Different basal salts, pyruvate
    and three receiving stocks demonstrate that matching a number without its accession/suffix
    is insufficient. Provider g_l is explicit but primary final main volume is not;
    no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 30,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 29.9103,\n                        \"mmol_l\":
    511.812,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q63","label":"DSM935 comparison:
    KNO3","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935
    source row, retained with its own main/stock stage. Different basal salts, pyruvate
    and three receiving stocks demonstrate that matching a number without its accession/suffix
    is insufficient. Provider g_l is explicit but primary final main volume is not;
    no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"KNO3\",\n                        \"compound_id\":
    191,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\":
    4.93066,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q64","label":"DSM935 comparison:
    Trace element solution SL-10","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q65","label":"DSM935 comparison:
    Selenite-tungstate solution","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q66","label":"DSM935 comparison:
    Yeast extract","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.99402,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q67","label":"DSM935
    comparison: Na2CO3","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.49551,\n                        \"mmol_l\":
    14.1102,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q68","label":"DSM935 comparison:
    Na-pyruvate","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935
    source row, retained with its own main/stock stage. Different basal salts, pyruvate
    and three receiving stocks demonstrate that matching a number without its accession/suffix
    is insufficient. Provider g_l is explicit but primary final main volume is not;
    no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Na-pyruvate\",\n                        \"compound_id\":
    113,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\":
    4.53005,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q69","label":"DSM935 comparison:
    Wolin''s vitamin solution (10x)","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q70","label":"DSM935 comparison:
    Distilled water","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Main sol. 935","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q71","label":"DSM935 comparison:
    HCl","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935
    source row, retained with its own main/stock stage. Different basal salts, pyruvate
    and three receiving stocks demonstrate that matching a number without its accession/suffix
    is insufficient. Provider g_l is explicit but primary final main volume is not;
    no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q72","label":"DSM935
    comparison: FeCl2 x 4 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q73","label":"DSM935 comparison:
    ZnCl2","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935
    source row, retained with its own main/stock stage. Different basal salts, pyruvate
    and three receiving stocks demonstrate that matching a number without its accession/suffix
    is insufficient. Provider g_l is explicit but primary final main volume is not;
    no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q74","label":"DSM935 comparison:
    MnCl2 x 4 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q75","label":"DSM935 comparison:
    H3BO3","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935
    source row, retained with its own main/stock stage. Different basal salts, pyruvate
    and three receiving stocks demonstrate that matching a number without its accession/suffix
    is insufficient. Provider g_l is explicit but primary final main volume is not;
    no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q76","label":"DSM935 comparison:
    CoCl2 x 6 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q77","label":"DSM935 comparison:
    CuCl2 x 2 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q78","label":"DSM935 comparison:
    NiCl2 x 6 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q79","label":"DSM935 comparison:
    Na2MoO4 x 2 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q80","label":"DSM935 comparison:
    Distilled water","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Trace element solution SL-10","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 990,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q81","label":"DSM935 comparison:
    NaOH","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935
    source row, retained with its own main/stock stage. Different basal salts, pyruvate
    and three receiving stocks demonstrate that matching a number without its accession/suffix
    is insufficient. Provider g_l is explicit but primary final main volume is not;
    no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Selenite-tungstate solution","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    12.5009,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q82","label":"DSM935 comparison:
    Na2SeO3 x 5 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Selenite-tungstate solution","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\":
    0.0114062,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q83","label":"DSM935 comparison:
    Na2WO4 x 2 H2O","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Selenite-tungstate solution","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\":
    0.0121267,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q84","label":"DSM935 comparison:
    Distilled water","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Selenite-tungstate solution","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q85","label":"DSM935 comparison:
    Biotin","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935
    source row, retained with its own main/stock stage. Different basal salts, pyruvate
    and three receiving stocks demonstrate that matching a number without its accession/suffix
    is insufficient. Provider g_l is explicit but primary final main volume is not;
    no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Wolin''s vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q86","label":"DSM935 comparison:
    Folic acid","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935
    source row, retained with its own main/stock stage. Different basal salts, pyruvate
    and three receiving stocks demonstrate that matching a number without its accession/suffix
    is insufficient. Provider g_l is explicit but primary final main volume is not;
    no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Wolin''s vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q87","label":"DSM935 comparison:
    Pyridoxine hydrochloride","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Wolin''s vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q88","label":"DSM935 comparison:
    Thiamine HCl","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Wolin''s vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q89","label":"DSM935 comparison:
    Riboflavin","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935
    source row, retained with its own main/stock stage. Different basal salts, pyruvate
    and three receiving stocks demonstrate that matching a number without its accession/suffix
    is insufficient. Provider g_l is explicit but primary final main volume is not;
    no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Wolin''s vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q90","label":"DSM935 comparison:
    Nicotinic acid","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Wolin''s vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q91","label":"DSM935 comparison:
    Calcium D-(+)-pantothenate","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Wolin''s vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q92","label":"DSM935 comparison:
    Vitamin B12","local_fields":[],"decision":"evidence_only","rationale":"Exact separate935
    source row, retained with its own main/stock stage. Different basal salts, pyruvate
    and three receiving stocks demonstrate that matching a number without its accession/suffix
    is insufficient. Provider g_l is explicit but primary final main volume is not;
    no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Wolin''s vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q93","label":"DSM935 comparison:
    p-Aminobenzoic acid","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Wolin''s vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q94","label":"DSM935 comparison:
    (DL)-alpha-Lipoic acid","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Wolin''s vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q95","label":"DSM935 comparison:
    Distilled water","local_fields":[],"decision":"evidence_only","rationale":"Exact
    separate935 source row, retained with its own main/stock stage. Different basal
    salts, pyruvate and three receiving stocks demonstrate that matching a number
    without its accession/suffix is insufficient. Provider g_l is explicit but primary
    final main volume is not; no transfer to935a or strain wrappers is endorsed.","source_stage":"Comparison-only
    Wolin''s vitamin solution (10x)","sources":[{"evidence_id":"api935","reference":"https://mediadive.dsmz.de/rest/medium/935","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/api935.bin","raw_sha256":"ea6af227835b25b411e2026aa5f4e461e5f13366e6f39d6d2e6432733a76e1d1","text_sha256":"ec0c1fad2180e799f9b92245b279786ac34c4279d4693f54d0d82fec83df7150","accessed_at":"2026-10-28T16:12:45.923379Z","locator":"data.solutions[3].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q96","label":"DSM935 primary
    source controls","local_fields":[],"decision":"evidence_only","rationale":"The
    complete primary counterpart preserves all935 input amounts, solvent/stocks, gas/duration/pH
    and the stock-local final make-up. These are compared only as a distinct variant;
    the SL-10 final1000ml is not a main-medium final-volume statement.","source_stage":"Comparison-only
    complete DSM935","sources":[{"evidence_id":"dsmz935","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium935.pdf","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/dsmz935.bin","raw_sha256":"51e46137cd5697af28a63697cffca147b1496c494bbe2d726fc11e60040a75dc","text_sha256":"f440ea58c8d679c4b2f2b2340b66ef07d1ae24854cea34b98225058bb56c89c5","accessed_at":"2026-10-28T16:12:45.021337Z","locator":"Complete
    derivative text retaining original form-feed separators","quote":"935: DEFERRIBACTER
    MEDIUM\n\n   NH4Cl                                                      1.00         g\n   K2HPO4                                                     0.08         g\n   MgCl2
    x 6 H2O                                              4.50         g\n   CaCl2
    x 2 H2O                                              0.38         g\n   NaCl                                                      30.00         g\n   KNO3                                                       0.50         g\n   Trace
    element solution SL-10                               1.00        ml\n   Selenite-tungstate
    solution                                1.00        ml\n   Yeast extract                                              2.00         g\n   Na2CO3                                                     1.50         g\n   Na-pyruvate                                                0.50         g\n   Wolin''s
    vitamin solution (10x)                             1.00        ml\n   Distilled
    water                                         1000.00        ml\n\nDissolve ingredients
    (except carbonate, pyruvate and vitamins), then sparge medium with\n80% N2 and
    20% CO2 gas mixture for 30-45 min to make it anoxic. Dispense medium\nunder same
    gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.\nAdd
    pyruvate and vitamins from anoxic stock solutions prepared under 100% N2 gas and\ncarbonate
    from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas\natmosphere.
    The pyruvate and vitamins solutions are sterilized by filtration. The pH of the\ncomplete
    medium should be 6.5 - 6.7.\n\n\n\n\nTrace element solution SL-10 (from medium
    320)\n   HCl (25%)                                                  10.00      ml\n   FeCl2
    x 4 H2O                                               1.50       g\n   ZnCl2                                                      70.00      mg\n   MnCl2
    x 4 H2O                                             100.00      mg\n   H3BO3                                                       6.00      mg\n   CoCl2
    x 6 H2O                                             190.00      mg\n   CuCl2 x
    2 H2O                                               2.00      mg\n   NiCl2 x 6
    H2O                                              24.00      mg\n   Na2MoO4 x 2
    H2O                                            36.00      mg\n   Distilled water                                           990.00      ml\n\nFirst
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally\nmake up to 1000.00 ml.\n\n\n\nSelenite-tungstate solution (from medium
    385)\n   NaOH                                                        0.50       g\n   Na2SeO3
    x 5 H2O                                             3.00      mg\n\n\n© 2022 DSMZ
    - All rights reserved                                                  Page 1
    of 2\n\f935: DEFERRIBACTER MEDIUM\n\n\n\n   Na2WO4 x 2 H2O                              4.00   mg\n   Distilled
    water                          1000.00   ml\n\n\nWolin''s vitamin solution (10x)
    (from medium 120)\n   Biotin                                     20.00   mg\n   Folic
    acid                                 20.00   mg\n   Pyridoxine hydrochloride                  100.00   mg\n   Thiamine
    HCl                               50.00   mg\n   Riboflavin                                 50.00   mg\n   Nicotinic
    acid                             50.00   mg\n   Calcium D-(+)-pantothenate                 50.00   mg\n   Vitamin
    B12                                 1.00   mg\n   p-Aminobenzoic acid                        50.00   mg\n   (DL)-alpha-Lipoic
    acid                     50.00   mg\n   Distilled water                          1000.00   ml\n\n\n\n\n©
    2022 DSMZ - All rights reserved                          Page 2 of 2","quote_basis":"derivative
    text"}],"layer_assessments":[]}],"document_scopes":{"data/merge_yaml/merged/DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml":null,"data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml":null,"data/normalized_yaml/bacterial/for_dsm_14813.yaml":null,"data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All current asserted CHEBI objects and MIM exact rows are covered. Nickel
    hexahydrate is wrongly represented by anhydrous CHEBI:34887 in two slots; other
    explicit sulfate hydrates, Na2S, D-calcium pantothenate and DL-compatible generic
    lipoic acid are retained. Valid canonical labels do not erase a supplied-form
    error. Legacy nitrate and missing yeast/calcium secondary links are bounded separately.
  target_ids:
  - CultureMech:002109
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: Read all ten original reports, four selected parent rows, all current owner
    events and current repair/resolver/import/cleanup/merge bodies. October source
    objects/digests are independently joined; earlier conflict statuses were not proof
    of accepted curation. September 935b comparison-target advice is not blindly transferred.
    The topology repair is credited as an actual stored update while its signature-based
    source-equivalence inference remains unverified; current scientific-field merge
    comparison would preserve differing notes, pH, preparation and relationships.
  target_ids:
  - CultureMech:002109
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-002109-accession-variant-conflict
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Resolve the 935a identifier versus 935b link and distinct 935 family
  description: The selected target/DSM owner identifies 935a, but its notes and current
    API link point to the chemically different 935b PDF. Fresh primary 935a matches
    the retained basal formula/preparation and explicitly gives 1011 ml final volume;
    935b differs in acetate, yeast, carbonate species, vitamins, sulfide and atmosphere/pH.
    DSM 935 differs again. September owners improve local topology, but classifying
    KOMODO 935 as a 935a duplicate and both strain wrappers under 935a relies on copied
    signatures, not recovered variant recipes. Exact KOMODO routes remain 403. Preserve
    all accessions, distinct catalogue strain identities and historical events; resolve
    the source-link and duplicate/variant claims before regeneration.
  target_ids:
  - CultureMech:002109
  field_paths:
  - media_term
  - notes
  - synonyms
  - merged_from
  - parent_media
  - variant_relationship
  - variant_modifications
  evidence_ids:
  - dsmz935a
  - dsmz935b
  - dsmz935
  - api935a
  - api935
  - komodo935
  - komodo935dot1
  - komodo935dash14783
  - dsm14813
  - dsm14783
  - writer-resolver
  - writer-repair
  rule_id: review-yaml-record/custom-accession-variant-conflict
  native_severity: P2
  normalization_reason: 'Custom identity rule: material source, stage or supplied-form
    discrepancy; major curation needed.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14813.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-002109-stock-stage-and-sums
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Undo mixed-stage calcium/sodium sums and flattened stocks
  description: All five layers combine main and mineral-stock CaCl2/NaCl rates into
    0.42640900000000004 and 25.728 G_PER_L. Equal units do not make different solution-stage
    denominators additive. Another 23 mineral/vitamin constituents remain at full
    stock strength in main ingredients. Preserve the primary 935a main masses and
    explicit 1011 ml final volume, the two separate receiving doses, stock compositions
    and solvent inputs. Reconcile each accession before curating the copied KOMODO
    layers. Current cleanup no longer sums differing duplicates and current import
    separates primary compounds/stocks; those present behaviors do not justify older
    output.
  target_ids:
  - CultureMech:002109
  field_paths:
  - ingredients
  - solutions
  - evidence
  evidence_ids:
  - quantities
  - dsmz935a
  - api935a
  - writer-cleanup
  - writer-mediadive
  rule_id: review-yaml-record/custom-stock-stage-and-sums
  native_severity: P2
  normalization_reason: 'Custom quantity rule: material source, stage or supplied-form
    discrepancy; major curation needed.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14813.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-002109-preparation-stock-context
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Separate retained main and mineral-stock preparation
  description: The DSM owner/target correctly retains substantial 935a source text,
    including gas mixtures, 30–45 min and 30% vessel fill. Preserve it while separating
    actions from the single AUTOCLAVE tag. The stock-local pH 6.5→7.0 KOH step is
    currently an unqualified main preparation step; attach it to Modified Wolin mineral
    stock. Unknown KOH amount and autoclave settings remain unknown. Do not copy 935a
    preparation into unresolved KOMODO variants or replace it with 935b conditions.
  target_ids:
  - CultureMech:002109
  field_paths:
  - preparation_steps
  - solutions
  - evidence
  evidence_ids:
  - dsmz935a
  - api935a
  - writer-mediadive
  rule_id: review-yaml-record/custom-preparation-stock-context
  native_severity: P2
  normalization_reason: 'Custom completeness rule: material source, stage or supplied-form
    discrepancy; major curation needed.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14813.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-002109-nickel-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Match nickel hexahydrate in both ontology slots
  description: NiCl2 x 6H2O is explicitly supplied by the 935a mineral stock, but
    ingredients[21] asserts anhydrous CHEBI:34887 in primary and secondary slots.
    Verify an exact hydrate object and canonical label while retaining the source
    stock amount. MIM lists the CHEBI:53542 preferred row as REJECTED and an exact
    synonym as MAPPED; preserve that distinction rather than treating either status
    as chemical proof. The other named sulfate hydrates, sodium-sulfide formula, D-calcium
    pantothenate and non-stereospecific lipoic acid are compatible with the exact
    935a forms.
  target_ids:
  - CultureMech:002109
  field_paths:
  - ingredients[21].term
  - ingredients[21].mediaingredientmech_chebi_term
  evidence_ids:
  - chebi34887
  - groundings
  - dsmz935a
  - api935a
  rule_id: review-yaml-record/custom-nickel-hydrate-grounding
  native_severity: P2
  normalization_reason: 'Custom grounding rule: material source, stage or supplied-form
    discrepancy; major curation needed.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14813.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml
    role: maintained normalized contributor
- finding_id: f5
  issue_key: culturemech-002109-secondary-link-gaps
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve bounded legacy and missing ingredient links
  description: The primary KNO3 CHEBI:63043 is correct, but its legacy MediaIngredientMech:000170
    secondary ID is absent from the exact packaged current index. Yeast extract has
    no primary/secondary linkage and calcium D-pantothenate lacks a secondary link.
    Reconcile exact current candidates without changing supported amounts or claiming
    historical invalidity from current snapshot absence.
  target_ids:
  - CultureMech:002109
  field_paths:
  - ingredients[6].mediaingredientmech_term
  - ingredients[8]
  - ingredients[30]
  evidence_ids:
  - groundings
  - mim
  - mim-meta
  rule_id: review-yaml-record/custom-secondary-link-gaps
  native_severity: P3
  normalization_reason: 'Custom grounding rule: bounded linkage/event-provenance issue;
    minor follow-up, with no invented native rule attribution.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14813.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml
    role: maintained normalized contributor
- finding_id: f6
  issue_key: culturemech-002109-claim-history-context
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Preserve original history and qualify historical source claims
  description: There are no attached ingredient claims. All ten full reports remain
    derivative historical evidence; current matching API bytes authenticate content,
    not the original access event. The September report targets a separate TOGO 935b
    cluster, so its proposed collapse and 935b conditions are not adopted for this
    935a target. KOMODO import .fZ and timezone-naive resolver events must remain
    byte-preserved; append verified context rather than rewrite their timestamps.
    Local topology fixes/curated flags do not establish external variant equivalence.
  target_ids:
  - CultureMech:002109
  field_paths:
  - evidence
  - curation_history
  - data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/for_dsm_14813.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/for_dsm_14813.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml::curation_history[1].timestamp
  evidence_ids:
  - old-reports
  - history
  - old-claims
  - writer-repair
  rule_id: review-yaml-record/custom-claim-history-context
  native_severity: P3
  normalization_reason: 'Custom provenance rule: bounded linkage/event-provenance
    issue; minor follow-up, with no invented native rule attribution.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14813.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml
    role: maintained normalized contributor
actions:
- action_id: a1
  description: The selected target/DSM owner identifies 935a, but its notes and current
    API link point to the chemically different 935b PDF. Fresh primary 935a matches
    the retained basal formula/preparation and explicitly gives 1011 ml final volume;
    935b differs in acetate, yeast, carbonate species, vitamins, sulfide and atmosphere/pH.
    DSM 935 differs again. September owners improve local topology, but classifying
    KOMODO 935 as a 935a duplicate and both strain wrappers under 935a relies on copied
    signatures, not recovered variant recipes. Exact KOMODO routes remain 403. Preserve
    all accessions, distinct catalogue strain identities and historical events; resolve
    the source-link and duplicate/variant claims before regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002109
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14813.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a2
  description: All five layers combine main and mineral-stock CaCl2/NaCl rates into
    0.42640900000000004 and 25.728 G_PER_L. Equal units do not make different solution-stage
    denominators additive. Another 23 mineral/vitamin constituents remain at full
    stock strength in main ingredients. Preserve the primary 935a main masses and
    explicit 1011 ml final volume, the two separate receiving doses, stock compositions
    and solvent inputs. Reconcile each accession before curating the copied KOMODO
    layers. Current cleanup no longer sums differing duplicates and current import
    separates primary compounds/stocks; those present behaviors do not justify older
    output.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002109
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14813.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml
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
  description: The DSM owner/target correctly retains substantial 935a source text,
    including gas mixtures, 30–45 min and 30% vessel fill. Preserve it while separating
    actions from the single AUTOCLAVE tag. The stock-local pH 6.5→7.0 KOH step is
    currently an unqualified main preparation step; attach it to Modified Wolin mineral
    stock. Unknown KOH amount and autoclave settings remain unknown. Do not copy 935a
    preparation into unresolved KOMODO variants or replace it with 935b conditions.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002109
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14813.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml
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
  description: NiCl2 x 6H2O is explicitly supplied by the 935a mineral stock, but
    ingredients[21] asserts anhydrous CHEBI:34887 in primary and secondary slots.
    Verify an exact hydrate object and canonical label while retaining the source
    stock amount. MIM lists the CHEBI:53542 preferred row as REJECTED and an exact
    synonym as MAPPED; preserve that distinction rather than treating either status
    as chemical proof. The other named sulfate hydrates, sodium-sulfide formula, D-calcium
    pantothenate and non-stereospecific lipoic acid are compatible with the exact
    935a forms.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:002109
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14813.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml
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
  description: The primary KNO3 CHEBI:63043 is correct, but its legacy MediaIngredientMech:000170
    secondary ID is absent from the exact packaged current index. Yeast extract has
    no primary/secondary linkage and calcium D-pantothenate lacks a secondary link.
    Reconcile exact current candidates without changing supported amounts or claiming
    historical invalidity from current snapshot absence.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:002109
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14813.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml
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
  description: There are no attached ingredient claims. All ten full reports remain
    derivative historical evidence; current matching API bytes authenticate content,
    not the original access event. The September report targets a separate TOGO 935b
    cluster, so its proposed collapse and 935b conditions are not adopted for this
    935a target. KOMODO import .fZ and timezone-naive resolver events must remain
    byte-preserved; append verified context rather than rewrite their timestamps.
    Local topology fixes/curated flags do not establish external variant equivalence.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:002109
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14813.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Retain all original events and old reports unchanged; append any new verified
    historical context in a new curation event.
  - Attach literal source claims with exact accession, raw digest and actual access
    time; do not convert prior report prose into an original retrieval receipt.
  generator: Maintained-input curation and repository merge regeneration
limitations:
- Exact KOMODO 935,935.1,935_14783 and catalogue requests returned 403. No formulation
  or growth transfer is inferred from their strain identifiers or catalogue medium
  links.
- DSM 935a explicitly declares final main volume 1011 ml. This positive basis is retained;935
  and 935b input water do not inherit it. Provider stock volumes/rates remain separate
  from primary stock input-water descriptions.
- The 935b REST endpoint returned 404, but its exact primary PDF was recovered and
  visually read. Its full component/condition differences are comparison-only; unprinted
  stock composition from its external 141 reference is not silently imported.
- Provider mmol_l values are not used to certify hydrate-sensitive molar conversions;
  primary mass and explicit g_l evidence are the assessed quantities.
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
