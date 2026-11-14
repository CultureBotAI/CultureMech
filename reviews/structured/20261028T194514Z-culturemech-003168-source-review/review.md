# Scientific review: DESULFOHALOBIUM MEDIUM

- Review: 20261028T194514Z-culturemech-003168-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T19:38:28.528709Z
- Finished UTC: 2026-10-28T19:45:14.796144Z
- Reviewer: Codex batch006_validation (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM824 needs restoration of its A/B and stock stages, correction of the selenium microgram and late liquid-dose representations, and nickel supplied-form grounding. Existing provider rates and preparation words are credited within their exact source stages; input water is not a final-volume measurement.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch076 index 01
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003168 | data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml | generated | desulfohalobium_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:003168 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:003168 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:003168 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:003168 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact JCM824 source and maintained owner

identity: supported. Targets: CultureMech:003168.

This selected single-owner record is JCM824. TOGO859 is a separately captured same-accession comparison, not a maintained contributor. Same-name DSM499 and historical neighbour records are not substitutes for this formulation. No target-organism growth assertion is inferred.

### Complex liquid classification

representation: supported. Targets: CultureMech:003168.

Yeast extract and Trypticase support the current complex classification. No solidifying ingredient is asserted; liquid state is consistent with the selected formulation. Missing links for complex products do not justify inventing a CHEBI chemical identity.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:003168.

48 current concentration fields are covered by 35 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b076-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","quantity_field_count":48,"decisions":[{"quantity_id":"q1","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 0 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NH&lt;sub&gt;4&lt;/sub&gt;Cl                                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.10865,\n                        \"mmol_l\": 20.7263,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q2","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.332594","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.332594","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 1 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.3&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.332594,\n                        \"mmol_l\": 2.444,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q3","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.332594","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.332594","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 2 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; K&lt;sub&gt;2&lt;/sub&gt;HPO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.3&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.332594,\n                        \"mmol_l\": 1.90953,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q4","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"110.865","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"110.865","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 3 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 100,\n                        \"unit\": \"g\",\n                        \"g_l\": 110.865,\n                        \"mmol_l\": 1897.07,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q5","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"4.43459","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"4.43459","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 4 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; KCl                                                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;4.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.43459,\n                        \"mmol_l\": 59.4848,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q6","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"3.32594","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"3.32594","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 5 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.32594,\n                        \"mmol_l\": 23.4155,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q7","label":"Sodium acetate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 6 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Sodium acetate                                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Sodium acetate\",\n                        \"compound_id\": 731,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.10865,\n                        \"mmol_l\": 13.5151,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q8","label":"Sodium lactate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Sodium lactate                                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Sodium lactate\",\n                        \"compound_id\": 1392,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.10865,\n                        \"mmol_l\": 9.89334,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q9","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 8 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Yeast extract                                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.10865,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q10","label":"Trypticase peptone","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume. Preserve the primary BD-BBL Trypticase product qualifier.","source_stage":"Solution A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 9 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trypticase peptone (BD-BBL)                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\": 124,\n                        \"attribute\": \"BD-BBL\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.10865,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume. Preserve the primary BD-BBL Trypticase product qualifier."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume. Preserve the primary BD-BBL Trypticase product qualifier."}]},{"quantity_id":"q11","label":"Na2SeO3 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"correct","rationale":"Primary JCM824 specifies 3 micrograms in Solution A; current TOGO859 independently preserves the microgram unit. APIJ824 has a corrupted unit string and no g_l value. Stored 3 G_PER_L is not supported. Recover the primary batch microgram amount and its stage without inventing a final-volume conversion.","source_stage":"Solution A batch","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 12 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;SeO&lt;sub&gt;3&lt;/sub&gt;&amp;#183;5H&lt;sub&gt;2&lt;/sub&gt;O                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"\\u00ef\\u00bf\\u00bdg\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"correct","rationale":"Primary JCM824 specifies 3 micrograms in Solution A; current TOGO859 independently preserves the microgram unit. APIJ824 has a corrupted unit string and no g_l value. Stored 3 G_PER_L is not supported. Recover the primary batch microgram amount and its stage without inventing a final-volume conversion."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"correct","rationale":"Primary JCM824 specifies 3 micrograms in Solution A; current TOGO859 independently preserves the microgram unit. APIJ824 has a corrupted unit string and no g_l value. Stored 3 G_PER_L is not supported. Recover the primary batch microgram amount and its stage without inventing a final-volume conversion."}]},{"quantity_id":"q12","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.00110865","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.00110865","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 13 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Resazurin                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00110865,\n                        \"mmol_l\": 0.00483724,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The exact primary batch mass is retained in the source object; the local number agrees with the provider g_l for Solution A on its declared 902 ml computational basis. It is not a final-medium concentration or measured final volume. Restore its Solution A scope before representing a combined-medium amount; do not silently replace the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q13","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"181.818","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"181.818","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary gives 20 g in Solution B with 100 ml input water. The local number agrees with API g_l on its declared 110 ml basis, which also includes the late sulfide dose in that provider section. Primary completion instead adds that dose after combining A/B, per litre. Preserve the primary B batch amount and separate completion; do not treat the provider basis as measured final volume.","source_stage":"Solution B; provider 110 ml computational basis is not the primary receiving stage","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 15 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 181.818,\n                        \"mmol_l\": 894.321,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"jcm824.txt lines 99-108","quote":"To complete the medium, combine Solutions A and B under a N\n2\natmosphere. Then, add per liter the following solution from an anaerobic stock:\n3% Na\n2\nS·9H\n2\nO solution\n10.0\nml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The primary gives 20 g in Solution B with 100 ml input water. The local number agrees with API g_l on its declared 110 ml basis, which also includes the late sulfide dose in that provider section. Primary completion instead adds that dose after combining A/B, per litre. Preserve the primary B batch amount and separate completion; do not treat the provider basis as measured final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The primary gives 20 g in Solution B with 100 ml input water. The local number agrees with API g_l on its declared 110 ml basis, which also includes the late sulfide dose in that provider section. Primary completion instead adds that dose after combining A/B, per litre. Preserve the primary B batch amount and separate completion; do not treat the provider basis as measured final volume."}]},{"quantity_id":"q14","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"24.5455","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"24.5455","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary gives 2.7 g in Solution B with 100 ml input water. The local number agrees with API g_l on its declared 110 ml basis, which also includes the late sulfide dose in that provider section. Primary completion instead adds that dose after combining A/B, per litre. Preserve the primary B batch amount and separate completion; do not treat the provider basis as measured final volume.","source_stage":"Solution B; provider 110 ml computational basis is not the primary receiving stage","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.7&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 2.7,\n                        \"unit\": \"g\",\n                        \"g_l\": 24.5455,\n                        \"mmol_l\": 166.959,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"jcm824.txt lines 99-108","quote":"To complete the medium, combine Solutions A and B under a N\n2\natmosphere. Then, add per liter the following solution from an anaerobic stock:\n3% Na\n2\nS·9H\n2\nO solution\n10.0\nml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The primary gives 2.7 g in Solution B with 100 ml input water. The local number agrees with API g_l on its declared 110 ml basis, which also includes the late sulfide dose in that provider section. Primary completion instead adds that dose after combining A/B, per litre. Preserve the primary B batch amount and separate completion; do not treat the provider basis as measured final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The primary gives 2.7 g in Solution B with 100 ml input water. The local number agrees with API g_l on its declared 110 ml basis, which also includes the late sulfide dose in that provider section. Primary completion instead adds that dose after combining A/B, per litre. Preserve the primary B batch amount and separate completion; do not treat the provider basis as measured final volume."}]},{"quantity_id":"q15","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary specifies 10 ml per litre of a 3% Na2S·9H2O anaerobic stock after A/B are combined. The current 10 G_PER_L is a liquid-dose/unit and stage error. Preserve the explicit receiving basis and source stock percentage; its unspecified percentage convention does not authorize a mass concentration calculation.","source_stage":"Completion after A/B combination; 10 ml stock per litre","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 18 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 3% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O solution                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"jcm824.txt lines 99-108","quote":"To complete the medium, combine Solutions A and B under a N\n2\natmosphere. Then, add per liter the following solution from an anaerobic stock:\n3% Na\n2\nS·9H\n2\nO solution\n10.0\nml","quote_basis":"derivative text"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"attribute\": \"3%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The primary specifies 10 ml per litre of a 3% Na2S·9H2O anaerobic stock after A/B are combined. The current 10 G_PER_L is a liquid-dose/unit and stage error. Preserve the explicit receiving basis and source stock percentage; its unspecified percentage convention does not authorize a mass concentration calculation."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The primary specifies 10 ml per litre of a 3% Na2S·9H2O anaerobic stock after A/B are combined. The current 10 G_PER_L is a liquid-dose/unit and stage error. Preserve the explicit receiving basis and source stock percentage; its unspecified percentage convention does not authorize a mass concentration calculation."}]},{"quantity_id":"q16","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"Primary JCM187 specifies 10 ml of HCl annotated 25% (7.7 M), within the iron stock containing 990 ml input water. The provider reports 2.5 g_l, but that mass conversion is not independently supported by the stated stock annotations and is not endorsed. Restore the stock reagent volume and qualifiers; neither its local root placement nor conversion to final-medium g/L is valid.","source_stage":"Iron stock reagent; 25% unspecified percentage convention and explicit 7.7 M","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 25% HCl (7.7 M)                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"7.7 M, 25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"Primary JCM187 specifies 10 ml of HCl annotated 25% (7.7 M), within the iron stock containing 990 ml input water. The provider reports 2.5 g_l, but that mass conversion is not independently supported by the stated stock annotations and is not endorsed. Restore the stock reagent volume and qualifiers; neither its local root placement nor conversion to final-medium g/L is valid."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"Primary JCM187 specifies 10 ml of HCl annotated 25% (7.7 M), within the iron stock containing 990 ml input water. The provider reports 2.5 g_l, but that mass conversion is not independently supported by the stated stock annotations and is not endorsed. Restore the stock reagent volume and qualifiers; neither its local root placement nor conversion to final-medium g/L is valid."}]},{"quantity_id":"q17","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary supports 1.5 g iron dichloride tetrahydrate in the iron stock. API explicitly gives stock g_l=1.5 on its 1000 ml basis. This support does not validate the current root final-medium placement. Preserve the source stock amount and the separate 1 ml Solution A receiving dose.","source_stage":"Iron stock; API declared 1000 ml basis","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML table row 17 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 10 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeCl&lt;sub&gt;2&lt;/sub&gt; solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The primary supports 1.5 g iron dichloride tetrahydrate in the iron stock. API explicitly gives stock g_l=1.5 on its 1000 ml basis. This support does not validate the current root final-medium placement. Preserve the source stock amount and the separate 1 ml Solution A receiving dose."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The primary supports 1.5 g iron dichloride tetrahydrate in the iron stock. API explicitly gives stock g_l=1.5 on its 1000 ml basis. This support does not validate the current root final-medium placement. Preserve the source stock amount and the separate 1 ml Solution A receiving dose."}]},{"quantity_id":"q18","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support.","source_stage":"Trace stock; API declared 1000 ml basis","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML table row 19 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnCl&lt;sub&gt;2&lt;/sub&gt;                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;70.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[4].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support."}]},{"quantity_id":"q19","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support.","source_stage":"Trace stock; API declared 1000 ml basis","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[4].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support."}]},{"quantity_id":"q20","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support.","source_stage":"Trace stock; API declared 1000 ml basis","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;6.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[4].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support."}]},{"quantity_id":"q21","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support.","source_stage":"Trace stock; API declared 1000 ml basis","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML table row 22 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;190.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[4].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support."}]},{"quantity_id":"q22","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support.","source_stage":"Trace stock; API declared 1000 ml basis","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML table row 23 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[4].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support."}]},{"quantity_id":"q23","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support.","source_stage":"Trace stock; API declared 1000 ml basis","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML table row 24 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;24.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[4].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support."}]},{"quantity_id":"q24","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support.","source_stage":"Trace stock; API declared 1000 ml basis","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML table row 25 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;36.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[4].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"correct","rationale":"The primary trace-stock mass and explicit provider stock g_l agree with this number on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml Solution A dose; do not certify this root amount as a final-medium concentration. Supplied chemical form is reviewed independently of numeric support."}]},{"quantity_id":"q25","label":"Solution A water","local_fields":[],"decision":"evidence_only","rationale":"900 ml is input water, not an explicit measured final volume.","source_stage":"Source-only batch/stock control","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 14 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;900.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[14]","quote":"{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 900,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q26","label":"Solution B water","local_fields":[],"decision":"evidence_only","rationale":"100 ml is input water, not an explicit measured final volume.","source_stage":"Source-only batch/stock control","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 17 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q27","label":"Iron stock water","local_fields":[],"decision":"evidence_only","rationale":"990 ml input water plus 10 ml reagent is not an independently measured final make-up statement.","source_stage":"Source-only batch/stock control","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML table row 18 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q28","label":"Trace stock water","local_fields":[],"decision":"evidence_only","rationale":"One litre is the primary water input; the provider separately declares stock volume and g_l.","source_stage":"Source-only batch/stock control","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML table row 26 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[4].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q29","label":"Iron stock receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The primary adds 1 ml to the Solution A batch, not 1 ml per litre unless a separate receiving basis is established.","source_stage":"Source-only batch/stock control","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 10 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeCl&lt;sub&gt;2&lt;/sub&gt; solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"solution\": \"FeCl2 solution\",\n                        \"solution_id\": 3846,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q30","label":"Trace stock receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The primary adds 1 ml to the Solution A batch; parent JCM187 medium doses are excluded.","source_stage":"Source-only batch/stock control","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 3847,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q31","label":"Retained pH","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ph_value","stored":7.0},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ph_value","stored":7.0}],"decision":"evidence_only","rationale":"The stored pH 7 agrees with the primary Solution A adjustment. Keep the stage qualification; it is not an additional measured final-medium pH observation.","source_stage":"Solution A adjustment","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"jcm824.txt lines 75-77","quote":"Mix components thoroughly and adjust pH to 7.0.  Autoclave under a N\n2\natmosphere.","quote_basis":"derivative text"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\": \"Mix components thoroughly and adjust pH to 7.0. Autoclave under a N2 atmosphere.\"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"The stored pH 7 agrees with the primary Solution A adjustment. Keep the stage qualification; it is not an additional measured final-medium pH observation."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"The stored pH 7 agrees with the primary Solution A adjustment. Keep the stage qualification; it is not an additional measured final-medium pH observation."}]},{"quantity_id":"q32","label":"Existing preparation step 1","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Mix components thoroughly and adjust pH to 7.0. Autoclave under a N2 atmosphere."}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Mix components thoroughly and adjust pH to 7.0. Autoclave under a N2 atmosphere."}}],"decision":"correct","rationale":"Retain the source-supported words and current action, but bind this step to Solution A. Do not apply a separate stock sterilization step indiscriminately to every flattened ingredient.","source_stage":"Named preparation stage","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"jcm824.txt lines 75-77","quote":"Mix components thoroughly and adjust pH to 7.0.  Autoclave under a N\n2\natmosphere.","quote_basis":"derivative text"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\": \"Mix components thoroughly and adjust pH to 7.0. Autoclave under a N2 atmosphere.\"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[0]","decision":"correct","rationale":"Retain the source-supported words and current action, but bind this step to Solution A. Do not apply a separate stock sterilization step indiscriminately to every flattened ingredient."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[0]","decision":"correct","rationale":"Retain the source-supported words and current action, but bind this step to Solution A. Do not apply a separate stock sterilization step indiscriminately to every flattened ingredient."}]},{"quantity_id":"q33","label":"Existing preparation step 2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"AUTOCLAVE","description":"Autoclave under a N2 atmosphere."}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"AUTOCLAVE","description":"Autoclave under a N2 atmosphere."}}],"decision":"correct","rationale":"Retain the source-supported words and current action, but bind this step to Solution B. Do not apply a separate stock sterilization step indiscriminately to every flattened ingredient.","source_stage":"Named preparation stage","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"jcm824.txt lines 96-98","quote":"Autoclave under a N\n2\natmosphere.","quote_basis":"derivative text"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[2].steps[0]","quote":"{\n                        \"step\": \"Autoclave under a N2 atmosphere.\"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"Retain the source-supported words and current action, but bind this step to Solution B. Do not apply a separate stock sterilization step indiscriminately to every flattened ingredient."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"Retain the source-supported words and current action, but bind this step to Solution B. Do not apply a separate stock sterilization step indiscriminately to every flattened ingredient."}]},{"quantity_id":"q34","label":"Existing preparation step 3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[2]","stored":{"step_number":3,"action":"MIX","description":"To complete the medium, combine Solutions A and B under a N2 atmosphere. Then, add per liter the following solution from an anaerobic stock:"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[2]","stored":{"step_number":3,"action":"MIX","description":"To complete the medium, combine Solutions A and B under a N2 atmosphere. Then, add per liter the following solution from an anaerobic stock:"}}],"decision":"correct","rationale":"Retain the source-supported words and current action, but bind this step to A/B completion. The current completion text must include the identified late stock and its explicit per-litre dose.","source_stage":"Named preparation stage","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"jcm824.txt lines 99-108","quote":"To complete the medium, combine Solutions A and B under a N\n2\natmosphere. Then, add per liter the following solution from an anaerobic stock:\n3% Na\n2\nS·9H\n2\nO solution\n10.0\nml","quote_basis":"derivative text"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[2].steps[1]","quote":"{\n                        \"recipe_order\": 4,\n                        \"step\": \"To complete the medium, combine Solutions A and B under a N2 atmosphere. Then, add per liter the following solution from an anaerobic stock: \"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[2]","decision":"correct","rationale":"Retain the source-supported words and current action, but bind this step to A/B completion. The current completion text must include the identified late stock and its explicit per-litre dose."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[2]","decision":"correct","rationale":"Retain the source-supported words and current action, but bind this step to A/B completion. The current completion text must include the identified late stock and its explicit per-litre dose."}]},{"quantity_id":"q35","label":"Page-wide autoclave default","local_fields":[],"decision":"evidence_only","rationale":"The exact JCM824 page gives 121°C for 15 minutes unless otherwise stated. Scope this default to the inherited autoclave operations; it is not an independent cultivation temperature or duration.","source_stage":"JCM824 default sterilization control","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"jcm824.txt lines 4-4","quote":"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.","quote_basis":"derivative text"}],"layer_assessments":[]}],"document_scopes":{"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:003168.

All asserted chemical slots and their current OLS/MIM rows are assessed. Nickel hexahydrate versus anhydrous CHEBI:34887 is the confirmed supplied-form error. The explicit selenium, magnesium, calcium, iron, manganese, cobalt, copper and molybdate hydrates otherwise agree; generic resazurin does not assert the sodium salt. Mixed lexical mapping statuses and broad synonyms are not whole-catalog chemical approval. Complex ingredients remain unassigned; optional FOODON or MICRO candidates are not silently endorsed.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:003168.

The four full reports distinguish the exact J824 owner/target from a separate merged neighbour. The selected October7 parent has 24 unchanged conflicts and 33 source objects; its raw source digest equals the current API bytes. This authenticates content, not the old retrieval event or proof of historical writer execution. No attached claims exist. Current singleton merge preserves the owner and cannot fix its source-stage defects. Old blanket classifications are assessed per source row rather than adopted.

## Findings

### f1: Solution-stage amounts are flattened into the final medium

major / open / confirmed; issue key: culturemech-003168-stage-topology.

Restore the explicit JCM824 Solution A/B structure and the JCM187 iron/trace stock scopes. Existing provider g_l numbers for A (902 ml), B (110 ml) and stocks (1000 ml) are scoped computational rates, not measured final-medium values. Credit those literal rates while correcting their root placement. Preserve the HCl reagent volume/25%/7.7 M annotations without endorsing the provider 2.5 g_l conversion. The current importer only inspects an empty first API recipe here and falls back to separately cached composition or a placeholder; reconcile this exact nested source before regeneration.

### f2: A primary microgram amount became a gram-per-litre assertion

major / open / confirmed; issue key: culturemech-003168-selenite-unit.

Correct ingredients[10] from the unsupported 3 G_PER_L representation to the exact primary 3 microgram Solution A batch quantity, retaining the pentahydrate identity. The API unit is corrupted; current unknown-unit fallback is a present risk, not proof of the historical execution. Establish a denominator before any per-litre conversion.

### f3: The late sulfide stock dose has a mass unit and wrong stage

major / open / confirmed; issue key: culturemech-003168-late-sulfide-dose.

Represent the primary late 3% sulfide stock as its explicit 10 ml per litre receiving dose after A/B combination. Stored 10 G_PER_L and provider placement under B do not preserve that primary instruction. Keep the source percent convention unresolved rather than calculate a mass dose.

### f4: Nickel hexahydrate is linked to anhydrous nickel chloride

major / open / confirmed; issue key: culturemech-003168-nickel-hydrate.

The primary and provider specify NiCl2·6H2O, while both current chemical slots assert anhydrous CHEBI:34887. Correct both supplied-form assertions after exact ID/label verification; CHEBI:53542 has the hexahydrate formula. Preserve the supported trace-stock mass. Catalogue spelling NiCl2 x 6 H2O has a REJECTED preferred row (6703), while Nickel (II) chloride hexahydrate is MAPPED (6668) and the former spelling is also a mapped synonym (6704); these lexical statuses do not reject the whole chemical identifier.

### f5: Retained preparation lacks solution bindings and complete stock context

major / open / confirmed; issue key: culturemech-003168-preparation-scope.

Keep the three supported preparation texts while restoring separate A/B autoclaving, A-specific pH adjustment and the complete final stock addition. Record the page default only for the autoclave steps. Current MediaDive step collection concatenates all solution steps without labels, so it must preserve source stage context when regenerated.

### f6: Source-backed quantities and preparation have no attached claims

minor / open / confirmed; issue key: culturemech-003168-claim-evidence.

Attach exact primary/provider excerpts at valid ingredient evidence fields for ingredient assertions and root evidence with explicit field/stage scope for solution doses, pH and preparation. Historical reports contain authenticatable current source bytes but the selected records themselves have no attached claims. Keep those layers distinct; do not add nonexistent concentration.evidence or solution.evidence fields.

## Recommended Actions And Acceptance Checks

### a1

Restore the explicit JCM824 Solution A/B structure and the JCM187 iron/trace stock scopes. Existing provider g_l numbers for A (902 ml), B (110 ml) and stocks (1000 ml) are scoped computational rates, not measured final-medium values. Credit those literal rates while correcting their root placement. Preserve the HCl reagent volume/25%/7.7 M annotations without endorsing the provider 2.5 g_l conversion. The current importer only inspects an empty first API recipe here and falls back to separately cached composition or a placeholder; reconcile this exact nested source before regeneration.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Correct ingredients[10] from the unsupported 3 G_PER_L representation to the exact primary 3 microgram Solution A batch quantity, retaining the pentahydrate identity. The API unit is corrupted; current unknown-unit fallback is a present risk, not proof of the historical execution. Establish a denominator before any per-litre conversion.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

Represent the primary late 3% sulfide stock as its explicit 10 ml per litre receiving dose after A/B combination. Stored 10 G_PER_L and provider placement under B do not preserve that primary instruction. Keep the source percent convention unresolved rather than calculate a mass dose.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

The primary and provider specify NiCl2·6H2O, while both current chemical slots assert anhydrous CHEBI:34887. Correct both supplied-form assertions after exact ID/label verification; CHEBI:53542 has the hexahydrate formula. Preserve the supported trace-stock mass. Catalogue spelling NiCl2 x 6 H2O has a REJECTED preferred row (6703), while Nickel (II) chloride hexahydrate is MAPPED (6668) and the former spelling is also a mapped synonym (6704); these lexical statuses do not reject the whole chemical identifier.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

Keep the three supported preparation texts while restoring separate A/B autoclaving, A-specific pH adjustment and the complete final stock addition. Record the page default only for the autoclave steps. Current MediaDive step collection concatenates all solution steps without labels, so it must preserve source stage context when regenerated.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a6

Attach exact primary/provider excerpts at valid ingredient evidence fields for ingredient assertions and root evidence with explicit field/stage scope for solution doses, pH and preparation. Historical reports contain authenticatable current source bytes but the selected records themselves have no attached claims. Keep those layers distinct; do not add nonexistent concentration.evidence or solution.evidence fields.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| jcm824 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824; REVIEW_WORK/batch076/source01-03-supplement/jcm824.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| apiJ824 | https://mediadive.dsmz.de/rest/medium/J824; REVIEW_WORK/batch076/source01-03-supplement/apiJ824.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| togo859 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M859; REVIEW_WORK/batch076/source01-03-supplement/togo859.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| jcm187 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187; REVIEW_WORK/batch076/source01-03-supplement/jcm187.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542; REVIEW_WORK/batch076/source01-03-supplement/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| target | data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-16 | reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-17 | reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-18 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-19 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfohalobium_medium__2d1ac1fa.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-20 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch076/record01/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch076/record01/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch076/record01/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _parse_api_solutions; _parse_composition_ingredients; _convert_to_culturemech; _parse_preparation_steps; _normalize_unit | context_only | The current API composition and stock parsers inspect only solutions[0].recipe, which is absent in this exact J824 payload. The composition route then tries separately cached parsed composition, otherwise a placeholder; it does not itself traverse Solutions A/B. Preparation concatenates all solution steps without stage labels. Unknown unit strings default to G_PER_L. These current behaviors are not authenticated historical execution. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch076/source01-03-supplement/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; REVIEW_WORK/batch076/source01-03-supplement/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527; REVIEW_WORK/batch076/source01-03-supplement/chebi131527.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch076/source01-03-supplement/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; REVIEW_WORK/batch076/source01-03-supplement/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149; REVIEW_WORK/batch076/source01-03-supplement/chebi32149.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32954; REVIEW_WORK/batch076/source01-03-supplement/chebi32954.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75228 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75228; REVIEW_WORK/batch076/source01-03-supplement/chebi75228.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131361; REVIEW_WORK/batch076/source01-03-supplement/chebi131361.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; REVIEW_WORK/batch076/source01-03-supplement/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; REVIEW_WORK/batch076/source01-03-supplement/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158; REVIEW_WORK/batch076/source01-03-supplement/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209; REVIEW_WORK/batch076/source01-03-supplement/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883; REVIEW_WORK/batch076/source01-03-supplement/chebi17883.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249; REVIEW_WORK/batch076/source01-03-supplement/chebi86249.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976; REVIEW_WORK/batch076/source01-03-supplement/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; REVIEW_WORK/batch076/source01-03-supplement/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch076/source01-03-supplement/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; REVIEW_WORK/batch076/source01-03-supplement/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; REVIEW_WORK/batch076/source01-03-supplement/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; REVIEW_WORK/batch076/source01-03-supplement/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch076/source01-03-supplement/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| quantities | REVIEW_WORK/batch076/record01/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch076/record01/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch076/record01/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch076/record01/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch076/record01/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch076/record01/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch076/record01/existing-claim-authentication.json; Complete sidecar | context_only | No attached claims to authenticate; historical source objects are separately assessed in historical-source-joins.json. |
| historical-source-joins | REVIEW_WORK/batch076/record01/historical-source-joins.json; Every literal/decoded historical source-object row and exact current-source match | context_only | Historical quoted source content and raw-digest equality where actually matched; independent of attached local claims and original access-event recovery. |
| check-schema | REVIEW_WORK/batch076/record01/validate-schema.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch076/record01/validate-strict.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch076/record01/validate-terms.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch076/record01/validate-references.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Only JCM187 iron and trace definitions are used; its main formulation, vitamins, receiving doses and organism context are excluded. The exact primary supplies no explicit measured final make-up volume for JCM824 A/B.
- Provider mmol_l conversions are not validated or used; the scope is exact primary amounts, explicit provider g_l and the supplied forms. The HCl provider mass conversion is specifically not endorsed.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T194514Z-culturemech-003168-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: DESULFOHALOBIUM MEDIUM'
started_at: '2026-10-28T19:38:28.528709Z'
finished_at: '2026-10-28T19:45:14.796144Z'
reviewer:
  identity: Codex batch006_validation
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Read-only independent review of maintained source records, exact
    captured sources, fresh scoped primary sources and original diagnostics.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: JCM824 needs restoration of its A/B and stock stages, correction of the selenium
  microgram and late liquid-dose representations, and nickel supplied-form grounding.
  Existing provider rates and preparation words are credited within their exact source
  stages; input water is not a final-volume measurement.
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
  - path: data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml
    sha256: 327d4e56bd476e9035e52bdd4a5eabdcf720932d5675b59eda1c5f5f2c4c2957
    role: target
  - path: data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml
    sha256: 6ca5af55a391a49b6c8be022f702d5e5ee9a13662ac320b341f2fe90f3f62953
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/plan.json
    sha256: 1db6b2b69fb7a9a131c95c22d837d6a4c5f10dab810921069496169a06d6f5c2
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml.md
    sha256: 777c9f89c73619d64a124c322bc6dc434ca014ec15e7c3d1c50775a90755dd5e
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.md
    sha256: b9807f529bbd7b862905d8b23b8c4be93f73d21cb57c0760a147b3ab8db047bf
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfohalobium_medium__2d1ac1fa.md
    sha256: ffa84637b49e00db9d37b450acc4672ab33bdffbf41c32c8c5daf3db428ede32
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.md
    sha256: b7bb400d954a839dba028b4b8eb2244d36bc6ef481722e36cb9079340ce93f27
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_cocktail_nesting.py
    sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
    role: context
  - path: scripts/apply_media_variant_links.py
    sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
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
  - path: scripts/propose_cocktail_nesting.py
    sha256: e886c446a8398f08f1cc735b1c3a9812c5fc6371a36b69ef5325f1c53f14e6c0
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
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
  selection: Authoritative batch076 index 01
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003168
targets:
- target_id: CultureMech:003168
  path: data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml
  label: desulfohalobium_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml
    role: maintained normalized contributor
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:003168
  command: just validate-schema data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml
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
  - CultureMech:003168
  command: just validate-strict data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml
    --out REVIEW_WORK/batch076/record01/strict.tsv --workers 1 --quiet
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
  - CultureMech:003168
  command: just validate-terms data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml
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
  - CultureMech:003168
  command: just validate-references data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: jcm824
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824
  accessed_at: '2026-10-28T19:39:09.297631Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/jcm824.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898
- evidence_id: apiJ824
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J824
  accessed_at: '2026-10-28T19:39:08.849687Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/apiJ824.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d
- evidence_id: togo859
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M859
  accessed_at: '2026-10-28T19:39:09.031337Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/togo859.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4413350b8ccfb65f2294822f3730694a0702d01d365af31632b5fc6e5d8c495e
- evidence_id: jcm187
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187
  accessed_at: '2026-10-28T19:39:09.931653Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/jcm187.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542
  accessed_at: '2026-10-28T19:39:16.621013Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi53542.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1e44a068cfe6b98d7bb3b0240ffdc0611e1be59f2d3dab9f04e4162ed94e4444
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T19:45:14.657349Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 327d4e56bd476e9035e52bdd4a5eabdcf720932d5675b59eda1c5f5f2c4c2957
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T19:45:14.657534Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 6ca5af55a391a49b6c8be022f702d5e5ee9a13662ac320b341f2fe90f3f62953
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T19:45:14.657567Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T19:45:14.657873Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T19:45:14.657897Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T19:45:14.657920Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-16
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T19:45:14.657947Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 1db6b2b69fb7a9a131c95c22d837d6a4c5f10dab810921069496169a06d6f5c2
- evidence_id: report-17
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T19:45:14.663004Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 777c9f89c73619d64a124c322bc6dc434ca014ec15e7c3d1c50775a90755dd5e
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T19:45:14.663067Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: b9807f529bbd7b862905d8b23b8c4be93f73d21cb57c0760a147b3ab8db047bf
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfohalobium_medium__2d1ac1fa.md
  locator: Complete report
  accessed_at: '2026-10-28T19:45:14.663097Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: ffa84637b49e00db9d37b450acc4672ab33bdffbf41c32c8c5daf3db428ede32
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T19:45:14.663121Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: b7bb400d954a839dba028b4b8eb2244d36bc6ef481722e36cb9079340ce93f27
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch076/record01/historical-reading.json
  accessed_at: '2026-10-28T19:45:14.663154Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 5d384cce879986e75caf95cc4ff81cd1121106919cb9a89d7080ed473302a638
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch076/record01/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T19:45:14.663452Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: bab8b145082c8be5271219e6afd257eff193e82c92be33780c45da9c74ceb77e
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch076/record01/complete-document-reader.json
  accessed_at: '2026-10-28T19:45:14.663515Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: b2d70ddd1ecde56c39ead9b4596797eea23b5a71304c6dc7a940a289bed5e6f9
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _parse_api_solutions; _parse_composition_ingredients;
    _convert_to_culturemech; _parse_preparation_steps; _normalize_unit
  accessed_at: '2026-10-28T19:45:14.663668Z'
  support: context_only
  summary: The current API composition and stock parsers inspect only solutions[0].recipe,
    which is absent in this exact J824 payload. The composition route then tries separately
    cached parsed composition, otherwise a placeholder; it does not itself traverse
    Solutions A/B. Preparation concatenates all solution steps without stage labels.
    Unknown unit strings default to G_PER_L. These current behaviors are not authenticated
    historical execution.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T19:45:14.663711Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  accessed_at: '2026-10-28T19:39:13.848048Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi31206.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  accessed_at: '2026-10-28T19:39:16.885926Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi63036.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527
  accessed_at: '2026-10-28T19:39:10.994580Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi131527.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 0a5297c84ea9dd82508960482211f6b3c993fd8e2b83fe755dd2b23316cc4068
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  accessed_at: '2026-10-28T19:39:12.979419Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi26710.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  accessed_at: '2026-10-28T19:39:14.820100Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi32588.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149
  accessed_at: '2026-10-28T19:39:14.734019Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi32149.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 96b73aef765e4edc893460a376cfedd136930f253bbeac639827b1daddb65d71
- evidence_id: chebi32954
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32954
  accessed_at: '2026-10-28T19:39:15.059590Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi32954.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 6718762e0aceec57316f70ff5a6264c973f1f2b235e6d5bbe077a9c349394fb8
- evidence_id: chebi75228
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75228
  accessed_at: '2026-10-28T19:39:17.228275Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi75228.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 02869dcf8cd74aa7f8b975f2590e5bdbd4512df6c748979a72d5337751ae5774
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131361
  accessed_at: '2026-10-28T19:39:10.985269Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi131361.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d88b30f797a300c3935e550a4770cb598bbed342a9c2a343f77bdce496e99db9
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806
  accessed_at: '2026-10-28T19:39:18.393979Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi8806.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f2530ec9c15f59a3d132a466c9c3a899497bab0f85b996d3e27bef8612f89982
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345
  accessed_at: '2026-10-28T19:39:18.118804Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi86345.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 94b600ced6e98743e2d1b02c73e1756f8f81b639407a8fdd080c96d8fa563c70
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158
  accessed_at: '2026-10-28T19:39:17.787202Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi86158.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: eacf58308fa876cb17661b82d08a64d9be24814fde8014ac82da7696b3684841
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209
  accessed_at: '2026-10-28T19:39:17.476846Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi76209.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4896ec517123ebeb1afcbac7bc30a7103976f03891af0c86c992196b5f0db969
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883
  accessed_at: '2026-10-28T19:39:12.367891Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi17883.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e5ab164ef9ff955da1a504ca34ab4d3b69539d9bf721936c9dd563ccbbd0e3b0
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249
  accessed_at: '2026-10-28T19:39:17.804695Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi86249.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4d7f48f88badcba85a62e59842c6ec921f5478eb76695098b17847ed62c8530a
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976
  accessed_at: '2026-10-28T19:39:16.274339Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi49976.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d3bdc4c6f01d01422fafe433df4e4011e01cf7e55e0329ab341a60ece780946f
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  accessed_at: '2026-10-28T19:39:18.375094Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi86368.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  accessed_at: '2026-10-28T19:39:15.045270Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi33118.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503
  accessed_at: '2026-10-28T19:39:16.572787Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi53503.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: a626d2aa210aafd9572221d4893cd206310d5df507e474e1528997048f522250
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318
  accessed_at: '2026-10-28T19:39:18.069295Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi86318.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: bd88e1499f370a9f474b29fa7a9a83aa5c42c69d0b6772ece8c89d646dfda8d8
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  accessed_at: '2026-10-28T19:39:15.418119Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi34887.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 3a37ef35991d24faf578286a7d7557ee1b0646c286dd3f8a555d833e6bf82a57
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  accessed_at: '2026-10-28T19:39:17.178522Z'
  locator: REVIEW_WORK/batch076/source01-03-supplement/chebi75213.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch076 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch076/record01/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:45:14.794341Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: afd895558621805a35cc768b76ecea317c6810d8099f300ca6e16c38707dc374
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch076/record01/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:45:14.794420Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: d9dd9c6fe47c7c5e62d80b36654038d4ba2a005a725c9db581b6097b4079d8ff
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch076/record01/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:45:14.794525Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 51a614f65cc30ea8b3bd452aa7e4a952780b1c8117248d7c4b81cb2224142e3e
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch076/record01/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:45:14.794588Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: d1a064aa2c1361ef3c45236b254bc7e68ed22055f7857a92888633261729eef5
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch076/record01/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:45:14.794666Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 02dc7c4b18d95f47730090703ff780f89ee4eac7d736a24f631b9c2d70367faf
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch076/record01/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:45:14.794703Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: b35e649b3e7d2954afc17d86d47b2fe3781ff2b6ef5044978f9686f4db4cb41f
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch076/record01/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:45:14.794740Z'
  support: context_only
  summary: No attached claims to authenticate; historical source objects are separately
    assessed in historical-source-joins.json.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: historical-source-joins
  kind: record_content
  reference: REVIEW_WORK/batch076/record01/historical-source-joins.json
  locator: Every literal/decoded historical source-object row and exact current-source
    match
  accessed_at: '2026-10-28T19:45:14.794771Z'
  support: context_only
  summary: Historical quoted source content and raw-digest equality where actually
    matched; independent of attached local claims and original access-event recovery.
  snapshot_sha256: 3f7053a0e6534496c04aaa79b704420091ba99f32307707494a93f9b46d40b1c
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch076/record01/validate-schema.json
  accessed_at: '2026-10-28T19:38:29.662264Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: aebaf63bbfd0bd0c4c88212c33d13fa173bf7f20336abfb9cfa0cabb409e96ee
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch076/record01/validate-strict.json
  accessed_at: '2026-10-28T19:38:30.624933Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: fc6e992ef78b6ca441d971241b23de5aa38b4d327cd82c506eaa8e8c6ae2e662
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch076/record01/validate-terms.json
  accessed_at: '2026-10-28T19:38:32.130692Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 38bb3bc4153c1509c2ddea4ff1939eb056804502218f34e1000c2972ac3f3908
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch076/record01/validate-references.json
  accessed_at: '2026-10-28T19:38:32.957589Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 59548f254c26dfce05522ee95d16602df010fa2708b3113969d36518415bb696
assessments:
- assessment_id: identity
  area: identity
  topic: Exact JCM824 source and maintained owner
  outcome: supported
  summary: This selected single-owner record is JCM824. TOGO859 is a separately captured
    same-accession comparison, not a maintained contributor. Same-name DSM499 and
    historical neighbour records are not substitutes for this formulation. No target-organism
    growth assertion is inferred.
  target_ids:
  - CultureMech:003168
  evidence_ids:
  - target
  - owner
  - jcm824
  - apiJ824
  - togo859
- assessment_id: classification
  area: representation
  topic: Complex liquid classification
  outcome: supported
  summary: Yeast extract and Trypticase support the current complex classification.
    No solidifying ingredient is asserted; liquid state is consistent with the selected
    formulation. Missing links for complex products do not justify inventing a CHEBI
    chemical identity.
  target_ids:
  - CultureMech:003168
  evidence_ids:
  - target
  - jcm824
  - groundings
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 48 current concentration fields are covered by 35 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:003168
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b076-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","quantity_field_count":48,"decisions":[{"quantity_id":"q1","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution
    A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 0 (zero-based)","quote":"<TR><TD WIDTH=75%> NH<sub>4</sub>Cl                                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.10865,\n                        \"mmol_l\":
    20.7263,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q2","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.332594","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.332594","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution
    A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 1 (zero-based)","quote":"<TR><TD WIDTH=75%> KH<sub>2</sub>PO<sub>4</sub>                                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.3&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.332594,\n                        \"mmol_l\":
    2.444,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q3","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.332594","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.332594","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution
    A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 2 (zero-based)","quote":"<TR><TD WIDTH=75%> K<sub>2</sub>HPO<sub>4</sub>                                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.3&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.332594,\n                        \"mmol_l\":
    1.90953,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q4","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"110.865","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"110.865","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution
    A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 3 (zero-based)","quote":"<TR><TD WIDTH=75%> NaCl                                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 100,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 110.865,\n                        \"mmol_l\":
    1897.07,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q5","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"4.43459","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"4.43459","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution
    A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 4 (zero-based)","quote":"<TR><TD WIDTH=75%> KCl                                                     </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;4.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4.43459,\n                        \"mmol_l\":
    59.4848,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q6","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"3.32594","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"3.32594","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution
    A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 5 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>SO<sub>4</sub>                                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.32594,\n                        \"mmol_l\":
    23.4155,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q7","label":"Sodium
    acetate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution
    A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 6 (zero-based)","quote":"<TR><TD WIDTH=75%> Sodium acetate                                          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Sodium acetate\",\n                        \"compound_id\":
    731,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.10865,\n                        \"mmol_l\":
    13.5151,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q8","label":"Sodium
    lactate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution
    A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Sodium lactate                                          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Sodium lactate\",\n                        \"compound_id\":
    1392,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.10865,\n                        \"mmol_l\":
    9.89334,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q9","label":"Yeast
    extract","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution
    A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 8 (zero-based)","quote":"<TR><TD WIDTH=75%> Yeast extract                                           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.10865,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q10","label":"Trypticase
    peptone","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"1.10865","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume. Preserve
    the primary BD-BBL Trypticase product qualifier.","source_stage":"Solution A;
    declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 9 (zero-based)","quote":"<TR><TD WIDTH=75%> Trypticase peptone (BD-BBL)                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\":
    124,\n                        \"attribute\": \"BD-BBL\",\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1.10865,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume. Preserve
    the primary BD-BBL Trypticase product qualifier."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume. Preserve
    the primary BD-BBL Trypticase product qualifier."}]},{"quantity_id":"q11","label":"Na2SeO3
    x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"correct","rationale":"Primary
    JCM824 specifies 3 micrograms in Solution A; current TOGO859 independently preserves
    the microgram unit. APIJ824 has a corrupted unit string and no g_l value. Stored
    3 G_PER_L is not supported. Recover the primary batch microgram amount and its
    stage without inventing a final-volume conversion.","source_stage":"Solution A
    batch","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 12 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>SeO<sub>3</sub>&#183;5H<sub>2</sub>O                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> &#181;g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 3,\n                        \"unit\":
    \"\\u00ef\\u00bf\\u00bdg\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"correct","rationale":"Primary
    JCM824 specifies 3 micrograms in Solution A; current TOGO859 independently preserves
    the microgram unit. APIJ824 has a corrupted unit string and no g_l value. Stored
    3 G_PER_L is not supported. Recover the primary batch microgram amount and its
    stage without inventing a final-volume conversion."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"correct","rationale":"Primary
    JCM824 specifies 3 micrograms in Solution A; current TOGO859 independently preserves
    the microgram unit. APIJ824 has a corrupted unit string and no g_l value. Stored
    3 G_PER_L is not supported. Recover the primary batch microgram amount and its
    stage without inventing a final-volume conversion."}]},{"quantity_id":"q12","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.00110865","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.00110865","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume.","source_stage":"Solution
    A; declared API volume 902 ml, primary input water 900 ml","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 13 (zero-based)","quote":"<TR><TD WIDTH=75%> Resazurin                                               </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\":
    25,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.00110865,\n                        \"mmol_l\":
    0.00483724,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The
    exact primary batch mass is retained in the source object; the local number agrees
    with the provider g_l for Solution A on its declared 902 ml computational basis.
    It is not a final-medium concentration or measured final volume. Restore its Solution
    A scope before representing a combined-medium amount; do not silently replace
    the source batch mass or equate 900 ml input water with final volume."}]},{"quantity_id":"q13","label":"MgCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"181.818","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"181.818","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary gives 20 g in Solution B with 100 ml input water. The local number agrees
    with API g_l on its declared 110 ml basis, which also includes the late sulfide
    dose in that provider section. Primary completion instead adds that dose after
    combining A/B, per litre. Preserve the primary B batch amount and separate completion;
    do not treat the provider basis as measured final volume.","source_stage":"Solution
    B; provider 110 ml computational basis is not the primary receiving stage","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 15 (zero-based)","quote":"<TR><TD WIDTH=75%> MgCl<sub>2</sub>&#183;6H<sub>2</sub>O                                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 20,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 181.818,\n                        \"mmol_l\":
    894.321,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"jcm824.txt
    lines 99-108","quote":"To complete the medium, combine Solutions A and B under
    a N\n2\natmosphere. Then, add per liter the following solution from an anaerobic
    stock:\n3% Na\n2\nS·9H\n2\nO solution\n10.0\nml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The
    primary gives 20 g in Solution B with 100 ml input water. The local number agrees
    with API g_l on its declared 110 ml basis, which also includes the late sulfide
    dose in that provider section. Primary completion instead adds that dose after
    combining A/B, per litre. Preserve the primary B batch amount and separate completion;
    do not treat the provider basis as measured final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The
    primary gives 20 g in Solution B with 100 ml input water. The local number agrees
    with API g_l on its declared 110 ml basis, which also includes the late sulfide
    dose in that provider section. Primary completion instead adds that dose after
    combining A/B, per litre. Preserve the primary B batch amount and separate completion;
    do not treat the provider basis as measured final volume."}]},{"quantity_id":"q14","label":"CaCl2
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"24.5455","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"24.5455","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary gives 2.7 g in Solution B with 100 ml input water. The local number agrees
    with API g_l on its declared 110 ml basis, which also includes the late sulfide
    dose in that provider section. Primary completion instead adds that dose after
    combining A/B, per litre. Preserve the primary B batch amount and separate completion;
    do not treat the provider basis as measured final volume.","source_stage":"Solution
    B; provider 110 ml computational basis is not the primary receiving stage","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.7&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 2.7,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 24.5455,\n                        \"mmol_l\":
    166.959,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"jcm824.txt
    lines 99-108","quote":"To complete the medium, combine Solutions A and B under
    a N\n2\natmosphere. Then, add per liter the following solution from an anaerobic
    stock:\n3% Na\n2\nS·9H\n2\nO solution\n10.0\nml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The
    primary gives 2.7 g in Solution B with 100 ml input water. The local number agrees
    with API g_l on its declared 110 ml basis, which also includes the late sulfide
    dose in that provider section. Primary completion instead adds that dose after
    combining A/B, per litre. Preserve the primary B batch amount and separate completion;
    do not treat the provider basis as measured final volume."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The
    primary gives 2.7 g in Solution B with 100 ml input water. The local number agrees
    with API g_l on its declared 110 ml basis, which also includes the late sulfide
    dose in that provider section. Primary completion instead adds that dose after
    combining A/B, per litre. Preserve the primary B batch amount and separate completion;
    do not treat the provider basis as measured final volume."}]},{"quantity_id":"q15","label":"Na2S
    x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary specifies 10 ml per litre of a 3% Na2S·9H2O anaerobic stock after A/B
    are combined. The current 10 G_PER_L is a liquid-dose/unit and stage error. Preserve
    the explicit receiving basis and source stock percentage; its unspecified percentage
    convention does not authorize a mass concentration calculation.","source_stage":"Completion
    after A/B combination; 10 ml stock per litre","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 18 (zero-based)","quote":"<TR><TD WIDTH=75%> 3% Na<sub>2</sub>S&#183;9H<sub>2</sub>O
    solution                     </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"jcm824.txt
    lines 99-108","quote":"To complete the medium, combine Solutions A and B under
    a N\n2\natmosphere. Then, add per liter the following solution from an anaerobic
    stock:\n3% Na\n2\nS·9H\n2\nO solution\n10.0\nml","quote_basis":"derivative text"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"attribute\": \"3%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The
    primary specifies 10 ml per litre of a 3% Na2S·9H2O anaerobic stock after A/B
    are combined. The current 10 G_PER_L is a liquid-dose/unit and stage error. Preserve
    the explicit receiving basis and source stock percentage; its unspecified percentage
    convention does not authorize a mass concentration calculation."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The
    primary specifies 10 ml per litre of a 3% Na2S·9H2O anaerobic stock after A/B
    are combined. The current 10 G_PER_L is a liquid-dose/unit and stage error. Preserve
    the explicit receiving basis and source stock percentage; its unspecified percentage
    convention does not authorize a mass concentration calculation."}]},{"quantity_id":"q16","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"Primary
    JCM187 specifies 10 ml of HCl annotated 25% (7.7 M), within the iron stock containing
    990 ml input water. The provider reports 2.5 g_l, but that mass conversion is
    not independently supported by the stated stock annotations and is not endorsed.
    Restore the stock reagent volume and qualifiers; neither its local root placement
    nor conversion to final-medium g/L is valid.","source_stage":"Iron stock reagent;
    25% unspecified percentage convention and explicit 7.7 M","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> 25% HCl (7.7 M)                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"7.7 M, 25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"Primary
    JCM187 specifies 10 ml of HCl annotated 25% (7.7 M), within the iron stock containing
    990 ml input water. The provider reports 2.5 g_l, but that mass conversion is
    not independently supported by the stated stock annotations and is not endorsed.
    Restore the stock reagent volume and qualifiers; neither its local root placement
    nor conversion to final-medium g/L is valid."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"Primary
    JCM187 specifies 10 ml of HCl annotated 25% (7.7 M), within the iron stock containing
    990 ml input water. The provider reports 2.5 g_l, but that mass conversion is
    not independently supported by the stated stock annotations and is not endorsed.
    Restore the stock reagent volume and qualifiers; neither its local root placement
    nor conversion to final-medium g/L is valid."}]},{"quantity_id":"q17","label":"FeCl2
    x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary supports 1.5 g iron dichloride tetrahydrate in the iron stock. API explicitly
    gives stock g_l=1.5 on its 1000 ml basis. This support does not validate the current
    root final-medium placement. Preserve the source stock amount and the separate
    1 ml Solution A receiving dose.","source_stage":"Iron stock; API declared 1000
    ml basis","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML
    table row 17 (zero-based)","quote":"<TR><TD WIDTH=75%> FeCl<sub>2</sub>&#183;4H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 10 (zero-based)","quote":"<TR><TD WIDTH=75%> FeCl<sub>2</sub> solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>)                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The
    primary supports 1.5 g iron dichloride tetrahydrate in the iron stock. API explicitly
    gives stock g_l=1.5 on its 1000 ml basis. This support does not validate the current
    root final-medium placement. Preserve the source stock amount and the separate
    1 ml Solution A receiving dose."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The
    primary supports 1.5 g iron dichloride tetrahydrate in the iron stock. API explicitly
    gives stock g_l=1.5 on its 1000 ml basis. This support does not validate the current
    root final-medium placement. Preserve the source stock amount and the separate
    1 ml Solution A receiving dose."}]},{"quantity_id":"q18","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support.","source_stage":"Trace
    stock; API declared 1000 ml basis","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML
    table row 19 (zero-based)","quote":"<TR><TD WIDTH=75%> ZnCl<sub>2</sub>                                               </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;70.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[4].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>)           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support."}]},{"quantity_id":"q19","label":"MnCl2
    x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support.","source_stage":"Trace
    stock; API declared 1000 ml basis","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML
    table row 20 (zero-based)","quote":"<TR><TD WIDTH=75%> MnCl<sub>2</sub>&#183;4H<sub>2</sub>O                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[4].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>)           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support."}]},{"quantity_id":"q20","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support.","source_stage":"Trace
    stock; API declared 1000 ml basis","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML
    table row 21 (zero-based)","quote":"<TR><TD WIDTH=75%> H<sub>3</sub>BO<sub>3</sub>                                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;6.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[4].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>)           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support."}]},{"quantity_id":"q21","label":"CoCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support.","source_stage":"Trace
    stock; API declared 1000 ml basis","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML
    table row 22 (zero-based)","quote":"<TR><TD WIDTH=75%> CoCl<sub>2</sub>&#183;6H<sub>2</sub>O                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;190.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[4].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>)           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support."}]},{"quantity_id":"q22","label":"CuCl2
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support.","source_stage":"Trace
    stock; API declared 1000 ml basis","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML
    table row 23 (zero-based)","quote":"<TR><TD WIDTH=75%> CuCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[4].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>)           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support."}]},{"quantity_id":"q23","label":"NiCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support.","source_stage":"Trace
    stock; API declared 1000 ml basis","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML
    table row 24 (zero-based)","quote":"<TR><TD WIDTH=75%> NiCl<sub>2</sub>&#183;6H<sub>2</sub>O                                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;24.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[4].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>)           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support."}]},{"quantity_id":"q24","label":"Na2MoO4
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support.","source_stage":"Trace
    stock; API declared 1000 ml basis","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML
    table row 25 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;36.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[4].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>)           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"correct","rationale":"The
    primary trace-stock mass and explicit provider stock g_l agree with this number
    on the provider 1000 ml basis. Restore the trace-stock stage and separate 1 ml
    Solution A dose; do not certify this root amount as a final-medium concentration.
    Supplied chemical form is reviewed independently of numeric support."}]},{"quantity_id":"q25","label":"Solution
    A water","local_fields":[],"decision":"evidence_only","rationale":"900 ml is input
    water, not an explicit measured final volume.","source_stage":"Source-only batch/stock
    control","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 14 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;900.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[14]","quote":"{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 900,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q26","label":"Solution B water","local_fields":[],"decision":"evidence_only","rationale":"100
    ml is input water, not an explicit measured final volume.","source_stage":"Source-only
    batch/stock control","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 17 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 100,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q27","label":"Iron stock water","local_fields":[],"decision":"evidence_only","rationale":"990
    ml input water plus 10 ml reagent is not an independently measured final make-up
    statement.","source_stage":"Source-only batch/stock control","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML
    table row 18 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 990,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q28","label":"Trace stock water","local_fields":[],"decision":"evidence_only","rationale":"One
    litre is the primary water input; the provider separately declares stock volume
    and g_l.","source_stage":"Source-only batch/stock control","sources":[{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm187.bin","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T19:39:09.931653Z","locator":"HTML
    table row 26 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L        </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[4].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q29","label":"Iron stock receiving
    dose","local_fields":[],"decision":"evidence_only","rationale":"The primary adds
    1 ml to the Solution A batch, not 1 ml per litre unless a separate receiving basis
    is established.","source_stage":"Source-only batch/stock control","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 10 (zero-based)","quote":"<TR><TD WIDTH=75%> FeCl<sub>2</sub> solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>)                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"solution\": \"FeCl2 solution\",\n                        \"solution_id\":
    3846,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q30","label":"Trace stock receiving
    dose","local_fields":[],"decision":"evidence_only","rationale":"The primary adds
    1 ml to the Solution A batch; parent JCM187 medium doses are excluded.","source_stage":"Source-only
    batch/stock control","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>)           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\":
    3847,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q31","label":"Retained pH","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ph_value","stored":7.0},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ph_value","stored":7.0}],"decision":"evidence_only","rationale":"The
    stored pH 7 agrees with the primary Solution A adjustment. Keep the stage qualification;
    it is not an additional measured final-medium pH observation.","source_stage":"Solution
    A adjustment","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"jcm824.txt
    lines 75-77","quote":"Mix components thoroughly and adjust pH to 7.0.  Autoclave
    under a N\n2\natmosphere.","quote_basis":"derivative text"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\":
    \"Mix components thoroughly and adjust pH to 7.0. Autoclave under a N2 atmosphere.\"\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"The
    stored pH 7 agrees with the primary Solution A adjustment. Keep the stage qualification;
    it is not an additional measured final-medium pH observation."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"The
    stored pH 7 agrees with the primary Solution A adjustment. Keep the stage qualification;
    it is not an additional measured final-medium pH observation."}]},{"quantity_id":"q32","label":"Existing
    preparation step 1","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Mix
    components thoroughly and adjust pH to 7.0. Autoclave under a N2 atmosphere."}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Mix
    components thoroughly and adjust pH to 7.0. Autoclave under a N2 atmosphere."}}],"decision":"correct","rationale":"Retain
    the source-supported words and current action, but bind this step to Solution
    A. Do not apply a separate stock sterilization step indiscriminately to every
    flattened ingredient.","source_stage":"Named preparation stage","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"jcm824.txt
    lines 75-77","quote":"Mix components thoroughly and adjust pH to 7.0.  Autoclave
    under a N\n2\natmosphere.","quote_basis":"derivative text"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\":
    \"Mix components thoroughly and adjust pH to 7.0. Autoclave under a N2 atmosphere.\"\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[0]","decision":"correct","rationale":"Retain
    the source-supported words and current action, but bind this step to Solution
    A. Do not apply a separate stock sterilization step indiscriminately to every
    flattened ingredient."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[0]","decision":"correct","rationale":"Retain
    the source-supported words and current action, but bind this step to Solution
    A. Do not apply a separate stock sterilization step indiscriminately to every
    flattened ingredient."}]},{"quantity_id":"q33","label":"Existing preparation step
    2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"AUTOCLAVE","description":"Autoclave
    under a N2 atmosphere."}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"AUTOCLAVE","description":"Autoclave
    under a N2 atmosphere."}}],"decision":"correct","rationale":"Retain the source-supported
    words and current action, but bind this step to Solution B. Do not apply a separate
    stock sterilization step indiscriminately to every flattened ingredient.","source_stage":"Named
    preparation stage","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"jcm824.txt
    lines 96-98","quote":"Autoclave under a N\n2\natmosphere.","quote_basis":"derivative
    text"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[2].steps[0]","quote":"{\n                        \"step\":
    \"Autoclave under a N2 atmosphere.\"\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"Retain
    the source-supported words and current action, but bind this step to Solution
    B. Do not apply a separate stock sterilization step indiscriminately to every
    flattened ingredient."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"Retain
    the source-supported words and current action, but bind this step to Solution
    B. Do not apply a separate stock sterilization step indiscriminately to every
    flattened ingredient."}]},{"quantity_id":"q34","label":"Existing preparation step
    3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[2]","stored":{"step_number":3,"action":"MIX","description":"To
    complete the medium, combine Solutions A and B under a N2 atmosphere. Then, add
    per liter the following solution from an anaerobic stock:"}},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[2]","stored":{"step_number":3,"action":"MIX","description":"To
    complete the medium, combine Solutions A and B under a N2 atmosphere. Then, add
    per liter the following solution from an anaerobic stock:"}}],"decision":"correct","rationale":"Retain
    the source-supported words and current action, but bind this step to A/B completion.
    The current completion text must include the identified late stock and its explicit
    per-litre dose.","source_stage":"Named preparation stage","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"jcm824.txt
    lines 99-108","quote":"To complete the medium, combine Solutions A and B under
    a N\n2\natmosphere. Then, add per liter the following solution from an anaerobic
    stock:\n3% Na\n2\nS·9H\n2\nO solution\n10.0\nml","quote_basis":"derivative text"},{"evidence_id":"apiJ824","reference":"https://mediadive.dsmz.de/rest/medium/J824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/apiJ824.bin","raw_sha256":"4e0a648697a4c1f211289daf0b5b55aad4e4b79332791654d8e9603a7846958d","text_sha256":"2c857f5ff08a438ac37d95ab8f6ceb5374454a7ee791f076e509bcd60124a3c5","accessed_at":"2026-10-28T19:39:08.849687Z","locator":"data.solutions[2].steps[1]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"step\": \"To complete the medium, combine Solutions
    A and B under a N2 atmosphere. Then, add per liter the following solution from
    an anaerobic stock: \"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[2]","decision":"correct","rationale":"Retain
    the source-supported words and current action, but bind this step to A/B completion.
    The current completion text must include the identified late stock and its explicit
    per-litre dose."},{"path":"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml","field_path":"preparation_steps[2]","decision":"correct","rationale":"Retain
    the source-supported words and current action, but bind this step to A/B completion.
    The current completion text must include the identified late stock and its explicit
    per-litre dose."}]},{"quantity_id":"q35","label":"Page-wide autoclave default","local_fields":[],"decision":"evidence_only","rationale":"The
    exact JCM824 page gives 121°C for 15 minutes unless otherwise stated. Scope this
    default to the inherited autoclave operations; it is not an independent cultivation
    temperature or duration.","source_stage":"JCM824 default sterilization control","sources":[{"evidence_id":"jcm824","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=824","raw_path":"REVIEW_WORK/batch076/source01-03-supplement/jcm824.bin","raw_sha256":"b72c29ea3576af4aae960b2a3f5783a06753cc920b93b91d3130a63efd1ef898","text_sha256":"2055b0d97450cce06ec226e302f653f2d34665c294a8eac1dd769c20722de48e","accessed_at":"2026-10-28T19:39:09.297631Z","locator":"jcm824.txt
    lines 4-4","quote":"Unless otherwise stated, sterilize media by autoclaving at
    121°C for 15 min.","quote_basis":"derivative text"}],"layer_assessments":[]}],"document_scopes":{"data/merge_yaml/merged/DESULFOHALOBIUM_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All asserted chemical slots and their current OLS/MIM rows are assessed.
    Nickel hexahydrate versus anhydrous CHEBI:34887 is the confirmed supplied-form
    error. The explicit selenium, magnesium, calcium, iron, manganese, cobalt, copper
    and molybdate hydrates otherwise agree; generic resazurin does not assert the
    sodium salt. Mixed lexical mapping statuses and broad synonyms are not whole-catalog
    chemical approval. Complex ingredients remain unassigned; optional FOODON or MICRO
    candidates are not silently endorsed.
  target_ids:
  - CultureMech:003168
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: The four full reports distinguish the exact J824 owner/target from a separate
    merged neighbour. The selected October7 parent has 24 unchanged conflicts and
    33 source objects; its raw source digest equals the current API bytes. This authenticates
    content, not the old retrieval event or proof of historical writer execution.
    No attached claims exist. Current singleton merge preserves the owner and cannot
    fix its source-stage defects. Old blanket classifications are assessed per source
    row rather than adopted.
  target_ids:
  - CultureMech:003168
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
  - historical-source-joins
  - writer-mediadive
  - historical-selected-parent-rows
  - historical-reading
findings:
- finding_id: f1
  issue_key: culturemech-003168-stage-topology
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Solution-stage amounts are flattened into the final medium
  description: Restore the explicit JCM824 Solution A/B structure and the JCM187 iron/trace
    stock scopes. Existing provider g_l numbers for A (902 ml), B (110 ml) and stocks
    (1000 ml) are scoped computational rates, not measured final-medium values. Credit
    those literal rates while correcting their root placement. Preserve the HCl reagent
    volume/25%/7.7 M annotations without endorsing the provider 2.5 g_l conversion.
    The current importer only inspects an empty first API recipe here and falls back
    to separately cached composition or a placeholder; reconcile this exact nested
    source before regeneration.
  target_ids:
  - CultureMech:003168
  field_paths:
  - ingredients[0].concentration
  - ingredients[1].concentration
  - ingredients[2].concentration
  - ingredients[3].concentration
  - ingredients[4].concentration
  - ingredients[5].concentration
  - ingredients[6].concentration
  - ingredients[7].concentration
  - ingredients[8].concentration
  - ingredients[9].concentration
  - ingredients[11].concentration
  - ingredients[12].concentration
  - ingredients[13].concentration
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
  - jcm824
  - jcm187
  - apiJ824
  - quantities
  - writer-mediadive
  rule_id: custom/source-stage-and-declared-basis
  native_severity: P2
  normalization_reason: 'Custom exact-source rule: stage and denominator mismatch;
    normalized major without redefining a narrower native rubric rule.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current API composition, stock and preparation writer
- finding_id: f2
  issue_key: culturemech-003168-selenite-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: A primary microgram amount became a gram-per-litre assertion
  description: Correct ingredients[10] from the unsupported 3 G_PER_L representation
    to the exact primary 3 microgram Solution A batch quantity, retaining the pentahydrate
    identity. The API unit is corrupted; current unknown-unit fallback is a present
    risk, not proof of the historical execution. Establish a denominator before any
    per-litre conversion.
  target_ids:
  - CultureMech:003168
  field_paths:
  - ingredients[10].concentration
  evidence_ids:
  - jcm824
  - apiJ824
  - togo859
  - writer-mediadive
  rule_id: custom/primary-microgram-unit
  native_severity: P2
  normalization_reason: 'Custom exact-source rule: primary microgram versus local
    mass-unit discrepancy; normalized major without redefining a narrower native rubric
    rule.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current API composition, stock and preparation writer
- finding_id: f3
  issue_key: culturemech-003168-late-sulfide-dose
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: The late sulfide stock dose has a mass unit and wrong stage
  description: Represent the primary late 3% sulfide stock as its explicit 10 ml per
    litre receiving dose after A/B combination. Stored 10 G_PER_L and provider placement
    under B do not preserve that primary instruction. Keep the source percent convention
    unresolved rather than calculate a mass dose.
  target_ids:
  - CultureMech:003168
  field_paths:
  - ingredients[14].concentration
  - preparation_steps[2]
  evidence_ids:
  - jcm824
  - apiJ824
  - quantities
  rule_id: custom/liquid-stock-dose-and-stage
  native_severity: P2
  normalization_reason: 'Custom exact-source rule: liquid stock dose and receiving-stage
    mismatch; normalized major without redefining a narrower native rubric rule.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-003168-nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate is linked to anhydrous nickel chloride
  description: The primary and provider specify NiCl2·6H2O, while both current chemical
    slots assert anhydrous CHEBI:34887. Correct both supplied-form assertions after
    exact ID/label verification; CHEBI:53542 has the hexahydrate formula. Preserve
    the supported trace-stock mass. Catalogue spelling NiCl2 x 6 H2O has a REJECTED
    preferred row (6703), while Nickel (II) chloride hexahydrate is MAPPED (6668)
    and the former spelling is also a mapped synonym (6704); these lexical statuses
    do not reject the whole chemical identifier.
  target_ids:
  - CultureMech:003168
  field_paths:
  - ingredients[22].term
  - ingredients[22].mediaingredientmech_chebi_term
  evidence_ids:
  - jcm187
  - apiJ824
  - chebi53542
  - groundings
  - mim
  rule_id: custom/supplied-hydrate-identity
  native_severity: P2
  normalization_reason: 'Custom exact-source rule: supplied hydrate mismatch; normalized
    major without redefining a narrower native rubric rule.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml
    role: maintained normalized contributor
- finding_id: f5
  issue_key: culturemech-003168-preparation-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Retained preparation lacks solution bindings and complete stock context
  description: Keep the three supported preparation texts while restoring separate
    A/B autoclaving, A-specific pH adjustment and the complete final stock addition.
    Record the page default only for the autoclave steps. Current MediaDive step collection
    concatenates all solution steps without labels, so it must preserve source stage
    context when regenerated.
  target_ids:
  - CultureMech:003168
  field_paths:
  - preparation_steps
  - ph_value
  evidence_ids:
  - jcm824
  - apiJ824
  - writer-mediadive
  - quantities
  rule_id: custom/preparation-stage-completeness
  native_severity: P2
  normalization_reason: 'Custom exact-source rule: loss of explicit preparation scope;
    normalized major without redefining a narrower native rubric rule.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current API composition, stock and preparation writer
- finding_id: f6
  issue_key: culturemech-003168-claim-evidence
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Source-backed quantities and preparation have no attached claims
  description: Attach exact primary/provider excerpts at valid ingredient evidence
    fields for ingredient assertions and root evidence with explicit field/stage scope
    for solution doses, pH and preparation. Historical reports contain authenticatable
    current source bytes but the selected records themselves have no attached claims.
    Keep those layers distinct; do not add nonexistent concentration.evidence or solution.evidence
    fields.
  target_ids:
  - CultureMech:003168
  field_paths:
  - ingredients[*].evidence
  - evidence
  evidence_ids:
  - old-claims
  - historical-source-joins
  - jcm824
  - apiJ824
  rule_id: custom/claim-evidence-placement
  native_severity: P3
  normalization_reason: 'Custom exact-source rule: bounded claim-evidence completeness;
    normalized minor without redefining a narrower native rubric rule.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml
    role: maintained normalized contributor
actions:
- action_id: a1
  description: Restore the explicit JCM824 Solution A/B structure and the JCM187 iron/trace
    stock scopes. Existing provider g_l numbers for A (902 ml), B (110 ml) and stocks
    (1000 ml) are scoped computational rates, not measured final-medium values. Credit
    those literal rates while correcting their root placement. Preserve the HCl reagent
    volume/25%/7.7 M annotations without endorsing the provider 2.5 g_l conversion.
    The current importer only inspects an empty first API recipe here and falls back
    to separately cached composition or a placeholder; reconcile this exact nested
    source before regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003168
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current API composition, stock and preparation writer
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a2
  description: Correct ingredients[10] from the unsupported 3 G_PER_L representation
    to the exact primary 3 microgram Solution A batch quantity, retaining the pentahydrate
    identity. The API unit is corrupted; current unknown-unit fallback is a present
    risk, not proof of the historical execution. Establish a denominator before any
    per-litre conversion.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003168
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current API composition, stock and preparation writer
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a3
  description: Represent the primary late 3% sulfide stock as its explicit 10 ml per
    litre receiving dose after A/B combination. Stored 10 G_PER_L and provider placement
    under B do not preserve that primary instruction. Keep the source percent convention
    unresolved rather than calculate a mass dose.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003168
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml
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
  description: The primary and provider specify NiCl2·6H2O, while both current chemical
    slots assert anhydrous CHEBI:34887. Correct both supplied-form assertions after
    exact ID/label verification; CHEBI:53542 has the hexahydrate formula. Preserve
    the supported trace-stock mass. Catalogue spelling NiCl2 x 6 H2O has a REJECTED
    preferred row (6703), while Nickel (II) chloride hexahydrate is MAPPED (6668)
    and the former spelling is also a mapped synonym (6704); these lexical statuses
    do not reject the whole chemical identifier.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:003168
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml
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
  description: Keep the three supported preparation texts while restoring separate
    A/B autoclaving, A-specific pH adjustment and the complete final stock addition.
    Record the page default only for the autoclave steps. Current MediaDive step collection
    concatenates all solution steps without labels, so it must preserve source stage
    context when regenerated.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:003168
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current API composition, stock and preparation writer
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a6
  description: Attach exact primary/provider excerpts at valid ingredient evidence
    fields for ingredient assertions and root evidence with explicit field/stage scope
    for solution doses, pH and preparation. Historical reports contain authenticatable
    current source bytes but the selected records themselves have no attached claims.
    Keep those layers distinct; do not add nonexistent concentration.evidence or solution.evidence
    fields.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:003168
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J824_DESULFOHALOBIUM_MEDIUM.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
limitations:
- Only JCM187 iron and trace definitions are used; its main formulation, vitamins,
  receiving doses and organism context are excluded. The exact primary supplies no
  explicit measured final make-up volume for JCM824 A/B.
- Provider mmol_l conversions are not validated or used; the scope is exact primary
  amounts, explicit provider g_l and the supplied forms. The HCl provider mass conversion
  is specifically not endorsed.
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
