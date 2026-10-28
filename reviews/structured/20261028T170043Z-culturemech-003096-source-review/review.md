# Scientific review: DEHALOSPIRILLUM MEDIUM

- Review: 20261028T170043Z-culturemech-003096-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T16:15:27.890356Z
- Finished UTC: 2026-10-28T17:00:43.375443Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full bounded scientific review identifies three major stock, dependency-unit and supplied-form issues plus a minor evidence-completeness follow-up. Existing preparation, declared provider rates and repaired dependency batch claims are credited with exact source scope.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch072 index 10
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003096 | data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml | generated | dehalospirillum_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:003096 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:003096 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:003096 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:003096 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact original recipe and scoped dependency identity

identity: supported. Targets: CultureMech:003096.

The maintained JCM_J753 owner, current original JCM753 and current official APIJ753 identify the same source. Both current sources refer to separate JCM187 iron/trace, JCM431 selenium, JCM197 vitamins and JCM403 B12 stocks; no source-version conflict is inferred from the older flattened local representation.

### Original diagnostics and classification

schema: supported. Targets: CultureMech:003096.

All four original canonical checks passed; reference validation reports zero checks. LIQUID and COMPLEX/UNDEFINED are consistent with the aqueous yeast-containing medium. Passing native shape/label checks does not validate concentrations or supplied hydrates.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:003096.

67 current concentration fields are covered by 68 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b072-quantity-inventory-v1","target":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","quantity_field_count":67,"decisions":[{"quantity_id":"q1","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.683594","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.683594","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The existing rate matches the explicit current provider g_l on its declared main volume1024 basis. The primary independently supports the exact batch mass, but 900 mL input water plus later additions does not independently establish that denominator. Retain this qualified support without recalculating or inventing final volume.","source_stage":"main provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 0 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.7&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 0.7,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.683594,\n                        \"mmol_l\": 4.81269,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.195312","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.195312","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The existing rate matches the explicit current provider g_l on its declared main volume1024 basis. The primary independently supports the exact batch mass, but 900 mL input water plus later additions does not independently establish that denominator. Retain this qualified support without recalculating or inventing final volume.","source_stage":"main provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 1 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; K&lt;sub&gt;2&lt;/sub&gt;HPO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.2&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.195312,\n                        \"mmol_l\": 1.12135,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.244141","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.244141","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The existing rate matches the explicit current provider g_l on its declared main volume1024 basis. The primary independently supports the exact batch mass, but 900 mL input water plus later additions does not independently establish that denominator. Retain this qualified support without recalculating or inventing final volume.","source_stage":"main provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 2 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NH&lt;sub&gt;4&lt;/sub&gt;Cl                                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.25&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.244141,\n                        \"mmol_l\": 4.56423,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.244141","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.244141","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The existing rate matches the explicit current provider g_l on its declared main volume1024 basis. The primary independently supports the exact batch mass, but 900 mL input water plus later additions does not independently establish that denominator. Retain this qualified support without recalculating or inventing final volume.","source_stage":"main provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 3 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.25&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.244141,\n                        \"mmol_l\": 4.17763,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.390625","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.390625","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The existing rate matches the explicit current provider g_l on its declared main volume1024 basis. The primary independently supports the exact batch mass, but 900 mL input water plus later additions does not independently establish that denominator. Retain this qualified support without recalculating or inventing final volume.","source_stage":"main provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 4 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.4&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.390625,\n                        \"mmol_l\": 1.92139,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.488281","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.488281","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The existing rate matches the explicit current provider g_l on its declared main volume1024 basis. The primary independently supports the exact batch mass, but 900 mL input water plus later additions does not independently establish that denominator. Retain this qualified support without recalculating or inventing final volume.","source_stage":"main provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 5 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; KCl                                                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.488281,\n                        \"mmol_l\": 6.54972,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.146484","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.146484","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The existing rate matches the explicit current provider g_l on its declared main volume1024 basis. The primary independently supports the exact batch mass, but 900 mL input water plus later additions does not independently establish that denominator. Retain this qualified support without recalculating or inventing final volume.","source_stage":"main provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 6 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.15&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.146484,\n                        \"mmol_l\": 0.996391,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000488281","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000488281","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The existing rate matches the explicit current provider g_l on its declared main volume1024 basis. The primary independently supports the exact batch mass, but 900 mL input water plus later additions does not independently establish that denominator. Retain this qualified support without recalculating or inventing final volume.","source_stage":"main provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Resazurin                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 0.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.000488281,\n                        \"mmol_l\": 0.00213046,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1.95312","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1.95312","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The existing rate matches the explicit current provider g_l on its declared main volume1024 basis. The primary independently supports the exact batch mass, but 900 mL input water plus later additions does not independently establish that denominator. Retain this qualified support without recalculating or inventing final volume.","source_stage":"main provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 8 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Yeast extract                                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.95312,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"L-Cysteine HCl x H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.0488281","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.0488281","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The existing rate matches the explicit current provider g_l on its declared main volume1024 basis. The primary independently supports the exact batch mass, but 900 mL input water plus later additions does not independently establish that denominator. Retain this qualified support without recalculating or inventing final volume.","source_stage":"main provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 12 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; L-Cysteine&amp;#183;HCl&amp;#183;H&lt;sub&gt;2&lt;/sub&gt;O                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.05&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0488281,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"FeSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.0244141","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.0244141","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The existing rate matches the explicit current provider g_l on its declared main volume1024 basis. The primary independently supports the exact batch mass, but 900 mL input water plus later additions does not independently establish that denominator. Retain this qualified support without recalculating or inventing final volume.","source_stage":"main provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 13 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.025&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.025,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0244141,\n                        \"mmol_l\": 0.0878156,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"Potassium phosphate buffer","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is a volume addition per liter (final), not the same numeric G_PER_L. Preserve the stock identity, explicit strength and specified sterilization marker.","source_stage":"post-sterilization receiving-medium stock addition","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 15 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 0.1 M Potassium phosphate buffer, pH 7.5               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt lines 100-100","quote":"atmosphere, then, seal butyl rubber stoppers and autoclave.  Aseptically and anaerobically add per liter (final) the following sterile solutions (autoclaved or *filter-sterilized) from anaerobic stocks:","quote_basis":"derivative text"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[15]","quote":"{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Potassium phosphate buffer\",\n                        \"compound_id\": 275,\n                        \"condition\": \" pH 7.5\",\n                        \"attribute\": \"0.1 M\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"Trace vitamins (see Medium No. 197)","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is a volume addition per liter (final), not the same numeric G_PER_L. Preserve the stock identity, explicit strength and specified sterilization marker.","source_stage":"post-sterilization receiving-medium stock addition","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace vitamins (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=197\"&gt;197&lt;/a&gt;)*                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt lines 100-100","quote":"atmosphere, then, seal butyl rubber stoppers and autoclave.  Aseptically and anaerobically add per liter (final) the following sterile solutions (autoclaved or *filter-sterilized) from anaerobic stocks:","quote_basis":"derivative text"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[16]","quote":"{\n                        \"recipe_order\": 17,\n                        \"compound\": \"Trace vitamins (see Medium No. 197)\",\n                        \"compound_id\": 1784,\n                        \"attribute\": \"*\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"42","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"42","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is a volume addition per liter (final), not the same numeric G_PER_L. Preserve the stock identity, explicit strength and specified sterilization marker. The percentage basis is unspecified, so no density or percent-to-mass conversion is justified.","source_stage":"post-sterilization receiving-medium stock addition","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 18 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 8% NaHCO&lt;sub&gt;3&lt;/sub&gt; solution*                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;42.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt lines 100-100","quote":"atmosphere, then, seal butyl rubber stoppers and autoclave.  Aseptically and anaerobically add per liter (final) the following sterile solutions (autoclaved or *filter-sterilized) from anaerobic stocks:","quote_basis":"derivative text"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[18]","quote":"{\n                        \"recipe_order\": 19,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"attribute\": \"*, 8%\",\n                        \"amount\": 42,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"Sodium pyruvate","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"18","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is a volume addition per liter (final), not the same numeric G_PER_L. Preserve the stock identity, explicit strength and specified sterilization marker. The percentage basis is unspecified, so no density or percent-to-mass conversion is justified.","source_stage":"post-sterilization receiving-medium stock addition","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 19 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 25% Sodium pyruvate solution*                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;18.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt lines 100-100","quote":"atmosphere, then, seal butyl rubber stoppers and autoclave.  Aseptically and anaerobically add per liter (final) the following sterile solutions (autoclaved or *filter-sterilized) from anaerobic stocks:","quote_basis":"derivative text"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[19]","quote":"{\n                        \"recipe_order\": 20,\n                        \"compound\": \"Sodium pyruvate\",\n                        \"compound_id\": 438,\n                        \"attribute\": \"*, 25%\",\n                        \"amount\": 18,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"Sodium fumarate","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"40","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"40","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is a volume addition per liter (final), not the same numeric G_PER_L. Preserve the stock identity, explicit strength and specified sterilization marker. The percentage basis is unspecified, so no density or percent-to-mass conversion is justified.","source_stage":"post-sterilization receiving-medium stock addition","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 16% Sodium fumarate solution*                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;40.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt lines 100-100","quote":"atmosphere, then, seal butyl rubber stoppers and autoclave.  Aseptically and anaerobically add per liter (final) the following sterile solutions (autoclaved or *filter-sterilized) from anaerobic stocks:","quote_basis":"derivative text"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[20]","quote":"{\n                        \"recipe_order\": 21,\n                        \"compound\": \"Sodium fumarate\",\n                        \"compound_id\": 1752,\n                        \"attribute\": \"*, 16%\",\n                        \"amount\": 40,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q17","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider places this amount/rate inside a separate iron, trace-element or selenium stock. It is flattened as a direct medium ingredient locally. Restore its source stock and independently represented receiving dose; the provider stock rate is not a final-medium rate. The HCl row also carries 7.7 M and 25% reagent attributes with 10 mL input. Its g_l=2.5 is not independently endorsed without an explicit percentage basis; retain the supported reagent strength and dose instead.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"7.7 M, 25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q18","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider places this amount/rate inside a separate iron, trace-element or selenium stock. It is flattened as a direct medium ingredient locally. Restore its source stock and independently represented receiving dose; the provider stock rate is not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q19","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider places this amount/rate inside a separate iron, trace-element or selenium stock. It is flattened as a direct medium ingredient locally. Restore its source stock and independently represented receiving dose; the provider stock rate is not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q20","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider places this amount/rate inside a separate iron, trace-element or selenium stock. It is flattened as a direct medium ingredient locally. Restore its source stock and independently represented receiving dose; the provider stock rate is not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q21","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider places this amount/rate inside a separate iron, trace-element or selenium stock. It is flattened as a direct medium ingredient locally. Restore its source stock and independently represented receiving dose; the provider stock rate is not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider places this amount/rate inside a separate iron, trace-element or selenium stock. It is flattened as a direct medium ingredient locally. Restore its source stock and independently represented receiving dose; the provider stock rate is not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[3].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider places this amount/rate inside a separate iron, trace-element or selenium stock. It is flattened as a direct medium ingredient locally. Restore its source stock and independently represented receiving dose; the provider stock rate is not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[3].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider places this amount/rate inside a separate iron, trace-element or selenium stock. It is flattened as a direct medium ingredient locally. Restore its source stock and independently represented receiving dose; the provider stock rate is not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[3].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider places this amount/rate inside a separate iron, trace-element or selenium stock. It is flattened as a direct medium ingredient locally. Restore its source stock and independently represented receiving dose; the provider stock rate is not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[3].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"NaOH","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.4","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.4","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider places this amount/rate inside a separate iron, trace-element or selenium stock. It is flattened as a direct medium ingredient locally. Restore its source stock and independently represented receiving dose; the provider stock rate is not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[4].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.4,\n                        \"mmol_l\": 10.0007,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"Na2SeO3 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider places this amount/rate inside a separate iron, trace-element or selenium stock. It is flattened as a direct medium ingredient locally. Restore its source stock and independently represented receiving dose; the provider stock rate is not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[4].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0228125,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Na2WO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.008","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.008","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider places this amount/rate inside a separate iron, trace-element or selenium stock. It is flattened as a direct medium ingredient locally. Restore its source stock and independently represented receiving dose; the provider stock rate is not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[4].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 8,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.008,\n                        \"mmol_l\": 0.0242534,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"B12 receiving dose","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary explicitly calls for 1 mL per liter (final) of the separately defined B12 stock, filter-sterilized; 1 G_PER_L does not represent this dose. The empty composition and Unknown solution name do not resolve the cross-reference.","source_stage":"B12 receiving addition","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 17 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin B&lt;sub&gt;1&lt;/sub&gt;&lt;sub&gt;2&lt;/sub&gt; solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=403\"&gt;403&lt;/a&gt;)*      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt lines 100-100","quote":"atmosphere, then, seal butyl rubber stoppers and autoclave.  Aseptically and anaerobically add per liter (final) the following sterile solutions (autoclaved or *filter-sterilized) from anaerobic stocks:","quote_basis":"derivative text"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[17]","quote":"{\n                        \"recipe_order\": 18,\n                        \"compound\": \"Vitamin B12 solution (see Medium No. 403)\",\n                        \"compound_id\": 1845,\n                        \"attribute\": \"*\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"Source-only iron dose","local_fields":[],"decision":"evidence_only","rationale":"Preserve this explicitly stated initial batch volume in its own receiving stage. It is not a final-liter normalization, a stock recipe volume, or an inferred mass.","source_stage":"initial receiving batch","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 9 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeCl&lt;sub&gt;2&lt;/sub&gt; solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"solution\": \"FeCl2 solution\",\n                        \"solution_id\": 3846,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"Source-only trace dose","local_fields":[],"decision":"evidence_only","rationale":"Preserve this explicitly stated initial batch volume in its own receiving stage. It is not a final-liter normalization, a stock recipe volume, or an inferred mass.","source_stage":"initial receiving batch","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 10 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 3847,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q32","label":"Source-only selenium dose","local_fields":[],"decision":"evidence_only","rationale":"Preserve this explicitly stated initial batch volume in its own receiving stage. It is not a final-liter normalization, a stock recipe volume, or an inferred mass.","source_stage":"initial receiving batch","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Selenite-tungstate solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=431\"&gt;431&lt;/a&gt;)     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 4172,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q33","label":"Source-only main water","local_fields":[],"decision":"evidence_only","rationale":"Preserve this explicitly stated initial batch volume in its own receiving stage. It is not a final-liter normalization, a stock recipe volume, or an inferred mass.","source_stage":"initial receiving batch","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 14 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;900.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[14]","quote":"{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 900,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q34","label":"Retained buffer pH note","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[11].notes","stored":" ( pH 7.5)"},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[11].notes","stored":" ( pH 7.5)"}],"decision":"evidence_only","rationale":"The retained pH7.5 note accurately belongs to the potassium-phosphate buffer. The missing 0.1 M stock strength and volume-unit defect are addressed separately.","source_stage":"buffer reagent","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML table row 15 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 0.1 M Potassium phosphate buffer, pH 7.5               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[15]","quote":"{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Potassium phosphate buffer\",\n                        \"compound_id\": 275,\n                        \"condition\": \" pH 7.5\",\n                        \"attribute\": \"0.1 M\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q35","label":"Retained preparation 1","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"preparation_steps[0].description","stored":"Mix components except L-cysteine x HCl x H2O and FeSO4 x 7H2O. Bring to a boil for a few seconds and cool down under a N2 atmosphere. While gassing with N2, add L-cysteine x HCl x H2O and FeSO4 x 7H2O to the solution, distribute into culture vessels (e.g., 18 ml in 50 ml serum bottles) under a N2 atmosphere, then, seal butyl rubber stoppers and autoclave. Aseptically and anaerobically add per liter (final) the following sterile solutions (autoclaved or *filter-sterilized) from anaerobic stocks:"},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"preparation_steps[0].description","stored":"Mix components except L-cysteine x HCl x H2O and FeSO4 x 7H2O. Bring to a boil for a few seconds and cool down under a N2 atmosphere. While gassing with N2, add L-cysteine x HCl x H2O and FeSO4 x 7H2O to the solution, distribute into culture vessels (e.g., 18 ml in 50 ml serum bottles) under a N2 atmosphere, then, seal butyl rubber stoppers and autoclave. Aseptically and anaerobically add per liter (final) the following sterile solutions (autoclaved or *filter-sterilized) from anaerobic stocks:"}],"decision":"evidence_only","rationale":"The complete retained description is supported, including its vessel example, gas context, sequential addition or final pH range. Credit this existing text; the unresolved stock table representation does not mean all preparation is absent.","source_stage":"retained receiving preparation","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"recipe_order\": 16,\n                        \"step\": \"Mix components except L-cysteine x HCl x H2O and FeSO4 x 7H2O. Bring to a boil for a few seconds and cool down under a N2 atmosphere. While gassing with N2, add L-cysteine x HCl x H2O and FeSO4 x 7H2O to the solution, distribute into culture vessels (e.g., 18 ml in 50 ml serum bottles) under a N2 atmosphere, then, seal butyl rubber stoppers and autoclave. Aseptically and anaerobically add per liter (final) the following sterile solutions (autoclaved or *filter-sterilized) from anaerobic stocks: \"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt lines 82-100","quote":"Mix components except L-cysteine·HCl·H\n2\nO and FeSO\n4\n·7H\n2\nO. Bring to a boil for a few seconds and cool down under a N\n2\natmosphere. While gassing with N\n2\n, add L-cysteine·HCl·H\n2\nO and FeSO\n4\n·7H\n2\nO to the solution, distribute into culture vessels (e.g., 18 ml in 50 ml serum bottles) under a N\n2\natmosphere, then, seal butyl rubber stoppers and autoclave.  Aseptically and anaerobically add per liter (final) the following sterile solutions (autoclaved or *filter-sterilized) from anaerobic stocks:","quote_basis":"derivative text"}]},{"quantity_id":"q36","label":"Retained preparation 2","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"preparation_steps[1].description","stored":"Adjust pH of the medium to 7.3 - 7.7, if necessary."},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"preparation_steps[1].description","stored":"Adjust pH of the medium to 7.3 - 7.7, if necessary."}],"decision":"evidence_only","rationale":"The complete retained description is supported, including its vessel example, gas context, sequential addition or final pH range. Credit this existing text; the unresolved stock table representation does not mean all preparation is absent.","source_stage":"retained receiving preparation","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].steps[1]","quote":"{\n                        \"step\": \"Adjust pH of the medium to 7.3 - 7.7, if necessary.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt lines 128-128","quote":"Adjust pH of the medium to 7.3 - 7.7, if necessary.","quote_basis":"derivative text"}]},{"quantity_id":"q37","label":"Retained representative pH","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ph_value","stored":7.5},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ph_value","stored":7.5}],"decision":"evidence_only","rationale":"7.5 matches provider metadata and lies within the original 7.3–7.7 range already retained in preparation. It is a representative scalar, not proof that the source requires exactly7.5.","source_stage":"receiving-medium pH","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.medium","quote":"{\n            \"id\": \"J753\",\n            \"name\": \"DEHALOSPIRILLUM MEDIUM\",\n            \"complex_medium\": \"yes\",\n            \"min_pH\": 7.5,\n            \"max_pH\": 7.5,\n            \"source\": \"JCM\",\n            \"link\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753\"\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt lines 128-128","quote":"Adjust pH of the medium to 7.3 - 7.7, if necessary.","quote_basis":"derivative text"}]},{"quantity_id":"q38","label":"JCM default autoclave control","local_fields":[],"decision":"evidence_only","rationale":"The site explicitly supplies 121°C for15min unless otherwise stated. Preserve this default only for applicable autoclave steps; explicitly asterisked filter additions retain their override.","source_stage":"source-only preparation control","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt lines 4-4","quote":"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q39","label":"Retained M180 Distilled water","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[0].concentration","stored":{"value":"0.99","unit":"L"}}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 990,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q40","label":"Retained M180 FeCl2・4H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[1].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 1.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"FeCl2・4H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001548\",\n          \"gmo_id\": \"GMO_001548\",\n          \"label\": \"Iron(II) chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q41","label":"Retained M180 Distilled water","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q42","label":"Retained M180 Na2MoO4・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 36 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q43","label":"Retained M180 H3BO3","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 6 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q44","label":"Retained M180 MnCl2・4H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 100 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q45","label":"Retained M180 CoCl2・6H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 190 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q46","label":"Retained M180 NiCl2・6H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 24 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q47","label":"Retained M180 CuCl2・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\": \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q48","label":"Retained M180 ZnCl2","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 70 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\": \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\": \"GMO_001035\",\n          \"label\": \"Zinc chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q49","label":"Retained nested HCl solutions[0].solutions[0].composition[0].concentration","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].composition[0].concentration","stored":{"value":"7.7","unit":"MOLAR"}}],"decision":"verified","rationale":"Explicit 7.7 M reagent strength is supported by its attached exact claim; the accompanying 25% basis is unspecified.","source_stage":"M180 iron-stock nested reagent","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q50","label":"Retained nested HCl solutions[0].solutions[0].concentration","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].concentration","stored":{"value":"0.01","unit":"L"}}],"decision":"verified","rationale":"The root evidence contains an additional exact HCl excerpt and this nested descriptor locator, authenticating 10 mL = 0.01 L into the iron stock; it is not the excluded parent-medium receiving dose.","source_stage":"M180 iron-stock nested reagent","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q51","label":"Retained HCl input-dose note","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].notes","stored":"Source stock addition: 10 ml = 0.01 L per receiving batch, not grams per liter or a dose per final liter."}],"decision":"verified","rationale":"The retained numeric note has the same exact scoped root attachment as the nested descriptor; no new dose or final concentration is inferred.","source_stage":"M180 nested HCl","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q52","label":"Scoped M431 Na2SeO3・5H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"6","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source lists 6 mg in the selenite-tungstate stock with 1 L input water. The stored g/L copies a milligram number and loses stock stage. Do not transfer the parent medium dose or collapsed shared water.","source_stage":"selenite-tungstate stock","sources":[{"evidence_id":"togo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T16:13:14.150946Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\": \"Na2SeO3・5H2O\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001046\",\n          \"gmo_id\": \"GMO_001046\",\n          \"label\": \"Sodium selenite pentahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q53","label":"Scoped M431 Na2WO4・2H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source lists 8 mg in the selenite-tungstate stock with 1 L input water. The stored g/L copies a milligram number and loses stock stage. Do not transfer the parent medium dose or collapsed shared water.","source_stage":"selenite-tungstate stock","sources":[{"evidence_id":"togo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T16:13:14.150946Z","locator":"components[3].items[2]","quote":"{\n          \"component_name\": \"Na2WO4・2H2O\",\n          \"volume\": 8,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001057\",\n          \"gmo_id\": \"GMO_001057\",\n          \"label\": \"Sodium tungstate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q54","label":"Scoped M431 NaOH","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.4","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The source lists 0.4 g in the selenite-tungstate stock with 1 L input water. The numeric gram input is supported, but the current g/L assertion lacks an explicit final-stock-volume basis. Do not transfer the parent medium dose or collapsed shared water.","source_stage":"selenite-tungstate stock","sources":[{"evidence_id":"togo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T16:13:14.150946Z","locator":"components[3].items[3]","quote":"{\n          \"component_name\": \"NaOH\",\n          \"volume\": 0.4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001078\",\n          \"gmo_id\": \"GMO_001078\",\n          \"label\": \"Sodium hydroxide\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q55","label":"Selenite stock water","local_fields":[],"decision":"evidence_only","rationale":"The source 1 L is stock input water, not the local collapsed water row and not measured final volume.","source_stage":"source-only selenite stock","sources":[{"evidence_id":"togo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T16:13:14.150946Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q56","label":"Retained M190 Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"The retained stock batch input has an exact attached literal claim and digest matching the current TOGO bytes, corroborated by the original JCM vitamin row. Preserve this batch note or water volume; no absent final-stock concentration is asserted.","source_stage":"M190 trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML table row 25 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q57","label":"Retained M190 Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained stock batch input has an exact attached literal claim and digest matching the current TOGO bytes, corroborated by the original JCM vitamin row. Preserve this batch note or water volume; no absent final-stock concentration is asserted.","source_stage":"M190 trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML table row 15 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Biotin                                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q58","label":"Retained M190 p--Aminobenzoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained stock batch input has an exact attached literal claim and digest matching the current TOGO bytes, corroborated by the original JCM vitamin row. Preserve this batch note or water volume; no absent final-stock concentration is asserted.","source_stage":"M190 trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML table row 23 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; &lt;I&gt;p&lt;/I&gt;-Aminobenzoic acid                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q59","label":"Retained M190 Thiamine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained stock batch input has an exact attached literal claim and digest matching the current TOGO bytes, corroborated by the original JCM vitamin row. Preserve this batch note or water volume; no absent final-stock concentration is asserted.","source_stage":"M190 trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\": \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML table row 18 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Thiamine&amp;#183;HCl                                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q60","label":"Retained M190 Calcium pantothenate","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained stock batch input has an exact attached literal claim and digest matching the current TOGO bytes, corroborated by the original JCM vitamin row. Preserve this batch note or water volume; no absent final-stock concentration is asserted.","source_stage":"M190 trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\",\n          \"gmo_id\": \"GMO_001028\",\n          \"label\": \"Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Calcium pantothenate                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q61","label":"Retained M190 Pyridoxine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 10 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained stock batch input has an exact attached literal claim and digest matching the current TOGO bytes, corroborated by the original JCM vitamin row. Preserve this batch note or water volume; no absent final-stock concentration is asserted.","source_stage":"M190 trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML table row 17 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Pyridoxine&amp;#183;HCl                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q62","label":"Retained M190 Folic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained stock batch input has an exact attached literal claim and digest matching the current TOGO bytes, corroborated by the original JCM vitamin row. Preserve this batch note or water volume; no absent final-stock concentration is asserted.","source_stage":"M190 trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\": \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Folic acid                                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q63","label":"Retained M190 Vitamin B12","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 0.1 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained stock batch input has an exact attached literal claim and digest matching the current TOGO bytes, corroborated by the original JCM vitamin row. Preserve this batch note or water volume; no absent final-stock concentration is asserted.","source_stage":"M190 trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML table row 22 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin B&lt;sub&gt;1&lt;/sub&gt;&lt;sub&gt;2&lt;/sub&gt;                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q64","label":"Retained M190 Riboflavin","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[8].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained stock batch input has an exact attached literal claim and digest matching the current TOGO bytes, corroborated by the original JCM vitamin row. Preserve this batch note or water volume; no absent final-stock concentration is asserted.","source_stage":"M190 trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\": \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML table row 19 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Riboflavin                                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q65","label":"Retained M190 Nicotinic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[9].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained stock batch input has an exact attached literal claim and digest matching the current TOGO bytes, corroborated by the original JCM vitamin row. Preserve this batch note or water volume; no absent final-stock concentration is asserted.","source_stage":"M190 trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Nicotinic acid                                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q66","label":"Retained M190 Lipoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[10].notes","stored":"Role: Growth factor; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained stock batch input has an exact attached literal claim and digest matching the current TOGO bytes, corroborated by the original JCM vitamin row. Preserve this batch note or water volume; no absent final-stock concentration is asserted.","source_stage":"M190 trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[10]","quote":"{\n          \"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\": \"GMO_001699\",\n          \"label\": \"Lipoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML table row 24 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Lipoic acid                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q67","label":"M401 B12 stock batch amount","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact referenced B12 stock contains5mg with100mL input water, not5g/L. Restore milligram batch amount inside the named stock; input water alone does not certify measured final100mL or a calculated final-stock concentration.","source_stage":"B12 stock only","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch072/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T16:14:44.975240Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T16:14:44.172479Z","locator":"HTML table row 26 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin B&lt;sub&gt;1&lt;/sub&gt;&lt;sub&gt;2&lt;/sub&gt;                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q68","label":"B12 stock input water","local_fields":[],"decision":"evidence_only","rationale":"The stock lists100mL water; exclude M401 collapsed shared water101G_PER_L and parent receiving dose. No final-volume assertion is substituted.","source_stage":"B12 stock only","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch072/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T16:14:44.975240Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T16:14:44.172479Z","locator":"HTML table row 27 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml":null,"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml":["solutions[0].composition","solutions[0].solutions","solutions[1].composition"],"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml":["ingredients[27]","ingredients[28]","ingredients[29]","solutions[1].name","solutions[1].preferred_term","solutions[1].composition"],"data/normalized_yaml/bacterial/togo_medium_m190.yaml":["solutions[1].composition"],"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml":["ingredients[25]","solutions[3].name","solutions[3].preferred_term","solutions[3].composition"]},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:003096.

Fresh asserted ontology objects, formulas, stereochemistry and synonyms were read with exact current MIM identifier and preferred-term rows. Selected CoCl2 hexahydrate is already correctly53503; nickel is not. Scoped M180 cobalt/nickel mismatch is separate. Generic source calcium pantothenate in M190 does not resolve the stereochemistry represented by31345, so this is an explicit uncertainty rather than a confirmed wrong-ID claim. Neutral resazurin is compatible with its unqualified source name; generic vitamin B12 remains generic. Canonical labels and MIM membership do not certify supplied form.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:003096.

All22 input reports were read completely through lossless pooled cells; repeated08 cells were reused by exact equality and all687 new cells read separately. Exact JCM753 current API digest matches the cited October7 response, and matching decoded objects authenticate current content without recovering the original access event. The October source-unchecked diagnostic and earlier broad merge recommendations are not scientific evidence by themselves. M180/M190 applied repair reports and exact attached current claims receive field-specific credit; M401, M431 and neighboring generated records remain scoped dependency context. Current importer and conservative formulation gate fixes are credited separately from historical generated data.

## Findings

### f1: Restore explicit receiving doses and separate stock formulations

major / open / confirmed; issue key: culturemech-003096-stock-topology.

The target and maintained owner flatten the iron, trace-element and selenium stock rows as direct medium ingredients and omit their three initial batch doses. Later buffer, vitamin, bicarbonate, pyruvate, fumarate and B12 additions are volumes per liter (final), not matching numeric G_PER_L. Preserve the provider-declared main rates only on their declared1024mL basis; restore the900mL input water and named stock graph without inferred final-volume arithmetic. Retain unspecified percentage bases and explicit filter overrides.

### f2: Resolve named vitamin and selenium dependencies with source-specific scope

major / open / confirmed; issue key: culturemech-003096-scoped-dependency-units.

M180 iron/trace and M190 trace-vitamin repairs already preserve supported batch inputs and attached source claims, including nested HCl. Reuse only those subsections. The M431 selenium/tungstate numbers still confuse milligrams with grams per liter, and M401 B12 remains5G_PER_L instead of the source5mg stock batch input. Correct only those scoped compositions; preserve stock input water, exclude parent receiving doses and unrelated recipes, and replace Unknown solution placeholders with their already-known identities.

### f3: Resolve exact nickel hydrate and scoped inherited cobalt form

major / open / confirmed; issue key: culturemech-003096-nickel-hydrate.

Both selected records name NiCl2 hexahydrate but assert anhydrous CHEBI:34887 in primary and secondary slots. Current OLS independently identifies hydrate candidate53542; current MIM rows are not acceptance evidence for that candidate. The scoped M180 trace stock also retains anhydrous cobalt35696/nickel34887 assignments under hexahydrate names. Correct supplied forms only after exact term review; do not infer hydrate equivalence from label agreement or convert amounts.

### f4: Attach current support while retaining existing preparation credit

minor / open / confirmed; issue key: culturemech-003096-claim-completeness.

The selected records preserve two substantive preparation descriptions and a representative pH scalar, but lack attached claim-level evidence for the supported provider rates and procedure. Preserve the exact7.3–7.7 range, buffer pH7.5 distinction, source default autoclave controls and filter overrides when curating. Append a new actual history event; historical raw equality authenticates content, not a replayed access event.

## Recommended Actions And Acceptance Checks

### a1

The target and maintained owner flatten the iron, trace-element and selenium stock rows as direct medium ingredients and omit their three initial batch doses. Later buffer, vitamin, bicarbonate, pyruvate, fumarate and B12 additions are volumes per liter (final), not matching numeric G_PER_L. Preserve the provider-declared main rates only on their declared1024mL basis; restore the900mL input water and named stock graph without inferred final-volume arithmetic. Retain unspecified percentage bases and explicit filter overrides.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

M180 iron/trace and M190 trace-vitamin repairs already preserve supported batch inputs and attached source claims, including nested HCl. Reuse only those subsections. The M431 selenium/tungstate numbers still confuse milligrams with grams per liter, and M401 B12 remains5G_PER_L instead of the source5mg stock batch input. Correct only those scoped compositions; preserve stock input water, exclude parent receiving doses and unrelated recipes, and replace Unknown solution placeholders with their already-known identities.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

Both selected records name NiCl2 hexahydrate but assert anhydrous CHEBI:34887 in primary and secondary slots. Current OLS independently identifies hydrate candidate53542; current MIM rows are not acceptance evidence for that candidate. The scoped M180 trace stock also retains anhydrous cobalt35696/nickel34887 assignments under hexahydrate names. Correct supplied forms only after exact term review; do not infer hydrate equivalence from label agreement or convert amounts.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

The selected records preserve two substantive preparation descriptions and a representative pH scalar, but lack attached claim-level evidence for the supported provider rates and procedure. Preserve the exact7.3–7.7 range, buffer pH7.5 distinction, source default autoclave controls and filter overrides when curating. Append a new actual history event; historical raw equality authenticates content, not a replayed access event.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| jcm753 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753; REVIEW_WORK/batch072/source07-08-10/jcm753.json; exact original raw/text/hash/time metadata | context_only | Current original JCM753 complete recipe and preparation, with exact linked iron/trace, selenium, trace-vitamin and B12 identities. |
| apiJ753 | https://mediadive.dsmz.de/rest/medium/J753; REVIEW_WORK/batch072/source07-08-10/apiJ753.json; exact original raw/text/hash/time metadata | context_only | Current official provider copy of JCM753; its declared main volume1024 and explicit rates remain a provider normalization, not an independently measured primary final volume. |
| jcm187 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187; REVIEW_WORK/batch072/source07-08-10-shared/jcm187.json; exact original raw/text/hash/time metadata | context_only | Current original JCM187; only its iron and trace-element stocks transfer through the exact JCM753 references. |
| jcm431 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431; REVIEW_WORK/batch072/source07-08-10-shared/jcm431.json; exact original raw/text/hash/time metadata | context_only | Current original JCM431; only the selenite-tungstate stock is assessed. |
| jcm197 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; REVIEW_WORK/batch072/source07-08-10-shared/jcm197.json; exact original raw/text/hash/time metadata | context_only | Current original JCM197; only the trace-vitamin composition is assessed. |
| jcm403 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403; REVIEW_WORK/batch072/source07-08-10/jcm403.json; exact original raw/text/hash/time metadata | context_only | Current original JCM403; only the separately named Vitamin B12 solution is assessed. |
| togo180 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180; REVIEW_WORK/batch072/source07-08-10-shared/togo180.json; exact original raw/text/hash/time metadata | context_only | Current TOGO M180 copy of JCM187, scoped to repaired iron/trace composition and nested HCl, excluding parent receiving doses. |
| togo431 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431; REVIEW_WORK/batch072/source07-08-10-shared/togo431.json; exact original raw/text/hash/time metadata | context_only | Current TOGO M431 copy of JCM431, scoped to selenite-tungstate composition only. |
| togo190 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; REVIEW_WORK/batch072/source07-08-10-shared/togo190.json; exact original raw/text/hash/time metadata | context_only | Current TOGO M190 copy of JCM197, scoped to repaired trace-vitamin composition only. |
| currentTogo401 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401; REVIEW_WORK/batch072/source07-08-10/currentTogo401.json; exact original raw/text/hash/time metadata | context_only | Current TOGO M401 copy of JCM403, scoped to Vitamin B12 solution only. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; REVIEW_WORK/batch072/source07-08-10/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| target | data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-21 | reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-22 | reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-24 | reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M180.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M190.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-26 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/ACETOBACTERIUM_SUBMARINUS_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-27 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BN3_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-28 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-29 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFUROCOCCUS_AMYLOLYTICUS_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-30 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/acetobacterium_submarinus_medium__9fed26ec.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-31 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/bn3_medium__59600ad0.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-32 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/dehalospirillum_medium__ff011652.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-33 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfurococcus_amylolyticus_medium__88cf0911.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-34 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/togo_medium_m190.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-35 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-36 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-37 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-38 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-39 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-40 | reports/yaml_record_review/20260921T083439Z-ACETOBACTERIUM_SUBMARINUS_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-41 | reports/yaml_record_review/20260921T131114Z-anoxic_medium_for_strain_acbe2_1.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-42 | reports/yaml_record_review/20260921T230801Z-BN3_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-43 | reports/yaml_record_review/20260921T231153Z-bn3_medium__59600ad0.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-44 | reports/yaml_record_review/20260923T163955Z-jcm_medium_no_197.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| dependency-M180 | data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml; solutions[0/1] composition and nested HCl | context_only | Only iron/trace-stock composition, retained batch notes and nested HCl reagent; parent-medium quantities and receiving doses are excluded. Full history is provenance only. |
| dependency-M431 | data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml; ingredients[27:30], solutions[1] excluding concentration | context_only | Only selenite-tungstate composition identity and its empty descriptor; basal medium, other trace stocks, shared collapsed water and parent receiving doses are excluded. |
| dependency-M190 | data/normalized_yaml/bacterial/togo_medium_m190.yaml; solutions[1].composition | context_only | Only trace-vitamin composition with retained batch notes and water evidence; other parent quantities, receiving doses, preparation and trace minerals are excluded. Full history is provenance context. |
| dependency-M401 | data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml; ingredients[25], solutions[3] excluding concentration | context_only | Only B12 stock composition identity is assessed; collapsed shared water, other vitamins, main medium and parent receiving dose are excluded. |
| writer-stock | scripts/repair_jcm_stock_preparations.py; Review.claim, leaf, stock, fill, stages, procedures; build | context_only | The current guarded repair retains source batch inputs and explicitly scoped root descriptor claims; M180 nested HCl and M190 vitamin repairs receive direct evidence credit. It preserves existing chemical annotations without recertifying them. |
| writer-togo | src/culturemech/import/togo_importer.py; _extract_primary_components, _solution_from_item, _parse_unit, _extract_preparation_steps | context_only | Current primary-section/stock extraction preserves topology and comments, unlike older flattened dependency records. Its unit enum and percentage fallback still do not establish final-volume or percentage bases. |
| historical-reading | REVIEW_WORK/batch072/record10/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch072/record10/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch072/record10/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser excludes percent-stock additions from primary ingredients, preserves referenced stock amounts/attributes separately and prioritizes explicit provider g_l. It skips source water; bare units alone do not establish a final-volume basis. Current code is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| historical-object-joins | REVIEW_WORK/batch072/record10/historical-current-object-joins.json; Complete exact decoded-object comparisons | context_only | Historical object correspondence is distinct from raw-response authentication. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; REVIEW_WORK/batch072/source07-08-10/chebi32149.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; REVIEW_WORK/batch072/source07-08-10/chebi131527.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; REVIEW_WORK/batch072/source07-08-10/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; REVIEW_WORK/batch072/source07-08-10/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; REVIEW_WORK/batch072/source07-08-10/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; REVIEW_WORK/batch072/source07-08-10/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; REVIEW_WORK/batch072/source07-08-10/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; REVIEW_WORK/batch072/source07-08-10/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; REVIEW_WORK/batch072/source07-08-10/chebi91248.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; REVIEW_WORK/batch072/source07-08-10/chebi75836.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; REVIEW_WORK/batch072/source07-08-10/chebi32139.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi50144 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144; REVIEW_WORK/batch072/source07-08-10/chebi50144.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi115156 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_115156; REVIEW_WORK/batch072/source07-08-10/chebi115156.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; REVIEW_WORK/batch072/source07-08-10/chebi17883.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; REVIEW_WORK/batch072/source07-08-10/chebi86249.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; REVIEW_WORK/batch072/source07-08-10/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; REVIEW_WORK/batch072/source07-08-10/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; REVIEW_WORK/batch072/source07-08-10/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; REVIEW_WORK/batch072/source07-08-10/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; REVIEW_WORK/batch072/source07-08-10/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; REVIEW_WORK/batch072/source07-08-10/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; REVIEW_WORK/batch072/source07-08-10/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; REVIEW_WORK/batch072/source07-08-10/chebi32145.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; REVIEW_WORK/batch072/source07-08-10/chebi131361.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; REVIEW_WORK/batch072/source07-08-10/chebi63939.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; REVIEW_WORK/batch072/source07-08-10/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; REVIEW_WORK/batch072/source07-08-10/chebi35696.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; REVIEW_WORK/batch072/source07-08-10/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; REVIEW_WORK/batch072/source07-08-10/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; REVIEW_WORK/batch072/source07-08-10/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; REVIEW_WORK/batch072/source07-08-10/chebi31345.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; REVIEW_WORK/batch072/source07-08-10/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; REVIEW_WORK/batch072/source07-08-10/chebi27470.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; REVIEW_WORK/batch072/source07-08-10/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; REVIEW_WORK/batch072/source07-08-10/chebi17015.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; REVIEW_WORK/batch072/source07-08-10/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; REVIEW_WORK/batch072/source07-08-10/chebi16494.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| quantities | REVIEW_WORK/batch072/record10/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch072/record10/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch072/record10/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch072/record10/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch072/record10/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch072/record10/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch072/record10/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch072/record10/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch072/record10/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch072/record10/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch072/record10/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Current provider volume1024 and its explicit main rates are retained as declared provider normalization; the primary900mL input and later per-liter additions do not independently establish measured final volume.
- Only M180 iron/trace, M190 trace vitamins, M431 selenium-tungstate and M401 B12 composition are scientifically assessed. Parent quantities and parent receiving instructions are excluded.
- Generic calcium-pantothenate stereochemistry, unspecified percentage bases and generic hydrate wording remain unresolved; no molar or mass conversion is inferred from ontology labels.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T170043Z-culturemech-003096-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: DEHALOSPIRILLUM MEDIUM'
started_at: '2026-10-28T16:15:27.890356Z'
finished_at: '2026-10-28T17:00:43.375443Z'
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
summary: Full bounded scientific review identifies three major stock, dependency-unit
  and supplied-form issues plus a minor evidence-completeness follow-up. Existing
  preparation, declared provider rates and repaired dependency batch claims are credited
  with exact source scope.
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
  - path: data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml
    sha256: 1bdfbcf81f130c31c951a6ea6dbee0546df929016ed301734ba3f735ccd5513d
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
    role: context
  - path: data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml
    sha256: e15e684ac336a9f0af121a26255448d28b73114a2ece07929ff553abda4b7750
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml
    sha256: 16bfd52c74b4968fb71d19de9eeec863417b8f1e5711a8e1413b7b0917cae25c
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    sha256: 35c2b3264b82cf435135a02583fb7e004fe58bc46d6c0906db454950ea333cdc
    role: context
  - path: data/normalized_yaml/bacterial/togo_medium_m190.yaml
    sha256: b1924e7eb436d56c5bd4826f07cafff130341054acfd808fb1c9e5bca914e3fa
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml.md
    sha256: e34f8dd0b39e3a55134ca98759be5803eedeefe81caacd9b32cb7cc51d360887
    role: context
  - path: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/plan.json
    sha256: 00113dc0b556486b52084f2508b061b9a188423d479f8aa102511ec55074ebd5
    role: context
  - path: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M180.md
    sha256: 92add964ce82b4d35cd58f93897f8bea6420fd3ce37ce77049e8449173263c30
    role: context
  - path: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M190.md
    sha256: 89725cdcefc5da88b06931c4db253e065a5f48c2d2b9c8c0a9bc07f6fdc157e8
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/ACETOBACTERIUM_SUBMARINUS_MEDIUM.md
    sha256: 56c93a375dbd090f5c559648722a46359964a01d1b6b9ab3225281a08d8d2b40
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BN3_MEDIUM.md
    sha256: fe4feab50de92089379d903e0b47e6e7a2e92dc6f4822f4f7a81297f177c8dc4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.md
    sha256: 0545081a3b5918ec1b30f573c4c5979737f71ad2b93e71f66d33dbc596ee3dbc
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFUROCOCCUS_AMYLOLYTICUS_MEDIUM.md
    sha256: 432876a053b21f5ac650332fd411f8fb3ee09f57f3321f215d1d174ade488f46
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/acetobacterium_submarinus_medium__9fed26ec.md
    sha256: 621b5623818337fb8c650369b29975144ef31d41449a02885ea8ec7652da9d63
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/bn3_medium__59600ad0.md
    sha256: 089a797d0ea2b3ddc0a978f5aae488e26d54b8124a1aafcc992cf6032108cc49
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/dehalospirillum_medium__ff011652.md
    sha256: a5dd56ab9772d9d1c55693be772132eb9d7715682b0ba4a2301df57a0f290ccc
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfurococcus_amylolyticus_medium__88cf0911.md
    sha256: 7ba8b4c2ac4a371fab0ad69230c1b53376bdcb648cfa0cea53896e1c59ebcdae
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/togo_medium_m190.md
    sha256: 4ee172b59b8f9a19921c300ecf394dc632e301c0f375a6e86adfade6ec86a619
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.md
    sha256: f7fa9416148a602515b571aedb11d7794ccdd4b2cce57bed8b84b78fc355a46e
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.md
    sha256: 183a8e8f5afeede25ea589c233889d2333b4c1d23e7378809ef16b78e19a9036
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.md
    sha256: 59f87cd1f3b048e72411c775bb1c80c7bea3287c1c0ba712a3bcfe5c84d18abe
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.md
    sha256: 1601590034c9aa40373c939b94267fbeddc72ae5b0f15de48f380cba97d1b965
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md
    sha256: d29c2d8798f20259a253d2b17745d675b4a789de94bdcef5279332d086383022
    role: context
  - path: reports/yaml_record_review/20260921T083439Z-ACETOBACTERIUM_SUBMARINUS_MEDIUM.md
    sha256: 1f5db491b2f11f287acd60655a5b0b44466da08a39cbd2a57fb467bf31ea2610
    role: context
  - path: reports/yaml_record_review/20260921T131114Z-anoxic_medium_for_strain_acbe2_1.md
    sha256: 84e487ca27d245977a3572b823e5d447a44bbb8daa8a8715e49b7084e880b07c
    role: context
  - path: reports/yaml_record_review/20260921T230801Z-BN3_MEDIUM.md
    sha256: f7b264f4b7f3aa84c40ec049d8d89f48d67f8bd0cb7f723e250de0ecdc068b0a
    role: context
  - path: reports/yaml_record_review/20260921T231153Z-bn3_medium__59600ad0.md
    sha256: 9c4941a859f60a9fc2adc04147052815d6fcf04f9e0453326d98a5732260de19
    role: context
  - path: reports/yaml_record_review/20260923T163955Z-jcm_medium_no_197.md
    sha256: 6497a50f712e4169a8f7a7cf4ae62d97e909b6695d86b7c522679b8f08909d7f
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
  selection: Authoritative batch072 index 10
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003096
targets:
- target_id: CultureMech:003096
  path: data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml
  label: dehalospirillum_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml
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
  - CultureMech:003096
  command: just validate-schema data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml
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
  - CultureMech:003096
  command: just validate-strict data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml
    --out REVIEW_WORK/batch072/record10/strict.tsv --workers 1 --quiet
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
  - CultureMech:003096
  command: just validate-terms data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml
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
  - CultureMech:003096
  command: just validate-references data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: jcm753
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753
  accessed_at: '2026-10-28T16:14:43.703086Z'
  locator: REVIEW_WORK/batch072/source07-08-10/jcm753.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Current original JCM753 complete recipe and preparation, with exact linked
    iron/trace, selenium, trace-vitamin and B12 identities.
  snapshot_sha256: 951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972
- evidence_id: apiJ753
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J753
  accessed_at: '2026-10-28T16:14:44.272325Z'
  locator: REVIEW_WORK/batch072/source07-08-10/apiJ753.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Current official provider copy of JCM753; its declared main volume1024
    and explicit rates remain a provider normalization, not an independently measured
    primary final volume.
  snapshot_sha256: 0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91
- evidence_id: jcm187
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187
  accessed_at: '2026-10-28T16:13:12.981041Z'
  locator: REVIEW_WORK/batch072/source07-08-10-shared/jcm187.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current original JCM187; only its iron and trace-element stocks transfer
    through the exact JCM753 references.
  snapshot_sha256: e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804
- evidence_id: jcm431
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431
  accessed_at: '2026-10-28T16:13:13.401026Z'
  locator: REVIEW_WORK/batch072/source07-08-10-shared/jcm431.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current original JCM431; only the selenite-tungstate stock is assessed.
  snapshot_sha256: cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50
- evidence_id: jcm197
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  accessed_at: '2026-10-28T16:13:13.544054Z'
  locator: REVIEW_WORK/batch072/source07-08-10-shared/jcm197.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current original JCM197; only the trace-vitamin composition is assessed.
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: jcm403
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403
  accessed_at: '2026-10-28T16:14:44.172479Z'
  locator: REVIEW_WORK/batch072/source07-08-10/jcm403.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Current original JCM403; only the separately named Vitamin B12 solution
    is assessed.
  snapshot_sha256: b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61
- evidence_id: togo180
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180
  accessed_at: '2026-10-28T16:13:13.892859Z'
  locator: REVIEW_WORK/batch072/source07-08-10-shared/togo180.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current TOGO M180 copy of JCM187, scoped to repaired iron/trace composition
    and nested HCl, excluding parent receiving doses.
  snapshot_sha256: a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba
- evidence_id: togo431
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431
  accessed_at: '2026-10-28T16:13:14.150946Z'
  locator: REVIEW_WORK/batch072/source07-08-10-shared/togo431.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current TOGO M431 copy of JCM431, scoped to selenite-tungstate composition
    only.
  snapshot_sha256: e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570
- evidence_id: togo190
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  accessed_at: '2026-10-28T16:13:13.927889Z'
  locator: REVIEW_WORK/batch072/source07-08-10-shared/togo190.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current TOGO M190 copy of JCM197, scoped to repaired trace-vitamin composition
    only.
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
- evidence_id: currentTogo401
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401
  accessed_at: '2026-10-28T16:14:44.975240Z'
  locator: REVIEW_WORK/batch072/source07-08-10/currentTogo401.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current TOGO M401 copy of JCM403, scoped to Vitamin B12 solution only.
  snapshot_sha256: 380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1
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
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T16:35:09.965538Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 1bdfbcf81f130c31c951a6ea6dbee0546df929016ed301734ba3f735ccd5513d
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T16:35:09.965723Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: e15e684ac336a9f0af121a26255448d28b73114a2ece07929ff553abda4b7750
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T16:35:09.965754Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T16:35:09.966052Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T16:35:09.966075Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T16:35:09.966102Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T16:35:09.966128Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 1db6b2b69fb7a9a131c95c22d837d6a4c5f10dab810921069496169a06d6f5c2
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.971158Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: e34f8dd0b39e3a55134ca98759be5803eedeefe81caacd9b32cb7cc51d360887
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T16:35:09.971216Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 00113dc0b556486b52084f2508b061b9a188423d479f8aa102511ec55074ebd5
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M180.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.971617Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 92add964ce82b4d35cd58f93897f8bea6420fd3ce37ce77049e8449173263c30
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M190.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.971660Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 89725cdcefc5da88b06931c4db253e065a5f48c2d2b9c8c0a9bc07f6fdc157e8
- evidence_id: report-26
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/ACETOBACTERIUM_SUBMARINUS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.971700Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 56c93a375dbd090f5c559648722a46359964a01d1b6b9ab3225281a08d8d2b40
- evidence_id: report-27
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BN3_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.971728Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: fe4feab50de92089379d903e0b47e6e7a2e92dc6f4822f4f7a81297f177c8dc4
- evidence_id: report-28
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.971751Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 0545081a3b5918ec1b30f573c4c5979737f71ad2b93e71f66d33dbc596ee3dbc
- evidence_id: report-29
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFUROCOCCUS_AMYLOLYTICUS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.971773Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 432876a053b21f5ac650332fd411f8fb3ee09f57f3321f215d1d174ade488f46
- evidence_id: report-30
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/acetobacterium_submarinus_medium__9fed26ec.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.971795Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 621b5623818337fb8c650369b29975144ef31d41449a02885ea8ec7652da9d63
- evidence_id: report-31
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/bn3_medium__59600ad0.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.971820Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 089a797d0ea2b3ddc0a978f5aae488e26d54b8124a1aafcc992cf6032108cc49
- evidence_id: report-32
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/dehalospirillum_medium__ff011652.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.971841Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: a5dd56ab9772d9d1c55693be772132eb9d7715682b0ba4a2301df57a0f290ccc
- evidence_id: report-33
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfurococcus_amylolyticus_medium__88cf0911.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.971864Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 7ba8b4c2ac4a371fab0ad69230c1b53376bdcb648cfa0cea53896e1c59ebcdae
- evidence_id: report-34
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/togo_medium_m190.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.971886Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 4ee172b59b8f9a19921c300ecf394dc632e301c0f375a6e86adfade6ec86a619
- evidence_id: report-35
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.971908Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: f7fa9416148a602515b571aedb11d7794ccdd4b2cce57bed8b84b78fc355a46e
- evidence_id: report-36
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.971931Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 183a8e8f5afeede25ea589c233889d2333b4c1d23e7378809ef16b78e19a9036
- evidence_id: report-37
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.971955Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 59f87cd1f3b048e72411c775bb1c80c7bea3287c1c0ba712a3bcfe5c84d18abe
- evidence_id: report-38
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.971978Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 1601590034c9aa40373c939b94267fbeddc72ae5b0f15de48f380cba97d1b965
- evidence_id: report-39
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.972001Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: d29c2d8798f20259a253d2b17745d675b4a789de94bdcef5279332d086383022
- evidence_id: report-40
  kind: prior_review
  reference: reports/yaml_record_review/20260921T083439Z-ACETOBACTERIUM_SUBMARINUS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.972023Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 1f5db491b2f11f287acd60655a5b0b44466da08a39cbd2a57fb467bf31ea2610
- evidence_id: report-41
  kind: prior_review
  reference: reports/yaml_record_review/20260921T131114Z-anoxic_medium_for_strain_acbe2_1.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.972047Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 84e487ca27d245977a3572b823e5d447a44bbb8daa8a8715e49b7084e880b07c
- evidence_id: report-42
  kind: prior_review
  reference: reports/yaml_record_review/20260921T230801Z-BN3_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.972068Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: f7b264f4b7f3aa84c40ec049d8d89f48d67f8bd0cb7f723e250de0ecdc068b0a
- evidence_id: report-43
  kind: prior_review
  reference: reports/yaml_record_review/20260921T231153Z-bn3_medium__59600ad0.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.972090Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 9c4941a859f60a9fc2adc04147052815d6fcf04f9e0453326d98a5732260de19
- evidence_id: report-44
  kind: prior_review
  reference: reports/yaml_record_review/20260923T163955Z-jcm_medium_no_197.md
  locator: Complete report
  accessed_at: '2026-10-28T16:35:09.972111Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 6497a50f712e4169a8f7a7cf4ae62d97e909b6695d86b7c522679b8f08909d7f
- evidence_id: dependency-M180
  kind: record_content
  reference: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
  locator: solutions[0/1] composition and nested HCl
  accessed_at: '2026-10-28T16:35:09.996440Z'
  support: context_only
  summary: Only iron/trace-stock composition, retained batch notes and nested HCl
    reagent; parent-medium quantities and receiving doses are excluded. Full history
    is provenance only.
  snapshot_sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
- evidence_id: dependency-M431
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
  locator: ingredients[27:30], solutions[1] excluding concentration
  accessed_at: '2026-10-28T16:35:10.006533Z'
  support: context_only
  summary: Only selenite-tungstate composition identity and its empty descriptor;
    basal medium, other trace stocks, shared collapsed water and parent receiving
    doses are excluded.
  snapshot_sha256: 35c2b3264b82cf435135a02583fb7e004fe58bc46d6c0906db454950ea333cdc
- evidence_id: dependency-M190
  kind: record_content
  reference: data/normalized_yaml/bacterial/togo_medium_m190.yaml
  locator: solutions[1].composition
  accessed_at: '2026-10-28T16:35:10.026303Z'
  support: context_only
  summary: Only trace-vitamin composition with retained batch notes and water evidence;
    other parent quantities, receiving doses, preparation and trace minerals are excluded.
    Full history is provenance context.
  snapshot_sha256: b1924e7eb436d56c5bd4826f07cafff130341054acfd808fb1c9e5bca914e3fa
- evidence_id: dependency-M401
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml
  locator: ingredients[25], solutions[3] excluding concentration
  accessed_at: '2026-10-28T16:35:10.036502Z'
  support: context_only
  summary: Only B12 stock composition identity is assessed; collapsed shared water,
    other vitamins, main medium and parent receiving dose are excluded.
  snapshot_sha256: 16bfd52c74b4968fb71d19de9eeec863417b8f1e5711a8e1413b7b0917cae25c
- evidence_id: writer-stock
  kind: record_content
  reference: scripts/repair_jcm_stock_preparations.py
  locator: Review.claim, leaf, stock, fill, stages, procedures; build
  accessed_at: '2026-10-28T16:35:10.037243Z'
  support: context_only
  summary: The current guarded repair retains source batch inputs and explicitly scoped
    root descriptor claims; M180 nested HCl and M190 vitamin repairs receive direct
    evidence credit. It preserves existing chemical annotations without recertifying
    them.
  snapshot_sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_primary_components, _solution_from_item, _parse_unit, _extract_preparation_steps
  accessed_at: '2026-10-28T16:35:10.037286Z'
  support: context_only
  summary: Current primary-section/stock extraction preserves topology and comments,
    unlike older flattened dependency records. Its unit enum and percentage fallback
    still do not establish final-volume or percentage bases.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch072/record10/historical-reading.json
  accessed_at: '2026-10-28T16:35:10.045927Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: cfc637328e18be39705ad771cbb6299d61013da90ebd785c91de8ffcb2b5dd39
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch072/record10/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T16:35:10.046063Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 251fea00b6a925c2c5611a739c3eacd067c737f0bda602920d1d2369e3741d18
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch072/record10/complete-document-reader.json
  accessed_at: '2026-10-28T16:35:10.046465Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: c776c762459a48d526e39f0531ec6c371ea2a2dd6f08bfeaa701c5ba1be48798
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T16:35:10.046587Z'
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
  accessed_at: '2026-10-28T16:35:10.046628Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: historical-object-joins
  kind: prior_review
  reference: REVIEW_WORK/batch072/record10/historical-current-object-joins.json
  accessed_at: '2026-10-28T16:35:10.046660Z'
  locator: Complete exact decoded-object comparisons
  support: context_only
  summary: Historical object correspondence is distinct from raw-response authentication.
  snapshot_sha256: cc800e160025fa1ed5c70c71bb62726402bc5f4ee2a4f5460ce4c1c699bbd432
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  accessed_at: '2026-10-28T16:14:48.650889Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi32149.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
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
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  accessed_at: '2026-10-28T16:14:50.697987Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi75836.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  accessed_at: '2026-10-28T16:14:48.249245Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi32139.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi50144
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144
  accessed_at: '2026-10-28T16:14:49.975535Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi50144.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 457ed29adfdea68c420ea0c094d7d75593958fc70f908f6809348e4e12e7e15d
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
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  accessed_at: '2026-10-28T16:14:48.628799Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi32145.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  accessed_at: '2026-10-28T16:14:44.975339Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi131361.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  accessed_at: '2026-10-28T16:14:50.572703Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi63939.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  accessed_at: '2026-10-28T16:14:45.588632Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi15377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi35696
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  accessed_at: '2026-10-28T16:14:49.455881Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi35696.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  accessed_at: '2026-10-28T16:14:45.637464Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi15956.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  accessed_at: '2026-10-28T16:14:47.601459Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi30753.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  accessed_at: '2026-10-28T16:14:49.939212Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi49105.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  accessed_at: '2026-10-28T16:14:48.167345Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi31345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  accessed_at: '2026-10-28T16:14:47.919472Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi30961.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  accessed_at: '2026-10-28T16:14:47.617892Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi27470.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  accessed_at: '2026-10-28T16:14:46.334847Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi176843.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  accessed_at: '2026-10-28T16:14:46.351547Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi17015.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  accessed_at: '2026-10-28T16:14:45.735781Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi15940.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  accessed_at: '2026-10-28T16:14:45.621818Z'
  locator: REVIEW_WORK/batch072/source07-08-10/chebi16494.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch072/record10/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:00:43.375443Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 170629c05d6d29f095949f49de8b85b7485507341f3b9101636995259cb5739c
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch072/record10/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:35:10.190362Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 1bf48ecb27dd67c12e8fe672547969440a272e6ca2eb73bab19c5a2852a149c4
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch072/record10/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:35:10.190531Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 08d84d100df82bdb4240be9d6b27a1c2797ff0401baa6633f7f45de1c52549a0
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch072/record10/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:35:10.190719Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 87f68095e08f2fd66cfc6300a9403b270a492c6b9919eb58bc0dad1315a18972
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch072/record10/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:35:10.190881Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 1c021de05b903edb03729ba06c13cdeccede050a4e344e9125d18e9531bbbead
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch072/record10/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:35:10.190923Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 5fe29cae76d5bbbf632a4d702769a1a6fcabea90714bce440fbd51251915fe8f
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch072/record10/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:35:10.190951Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 9aed2889e8766aeb41c2c3e9119b6c48a4b1af6cdc87d3910d9f30bcf68e15dc
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch072/record10/schema-result.json
  accessed_at: '2026-10-28T16:15:28.913241Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: aa8933de526d8d6b2bb00416abfd23ef80f53b69ad864abbe420a57305c190e1
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch072/record10/strict-result.json
  accessed_at: '2026-10-28T16:15:29.832757Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 121c49e40c4ac35db15ec632c7d8b1a55531ef6e946034dc8c746b7f3556b738
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch072/record10/terms-result.json
  accessed_at: '2026-10-28T16:15:30.841107Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 0ab3d2303e4417c64e2af57dd61e1f9df8a87ae274fbba1564446e7d59646068
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch072/record10/references-result.json
  accessed_at: '2026-10-28T16:15:31.557185Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: db544306d7428d2a6e5514ea153e5ee42e0744956f4123eced1bcff0150d84fb
assessments:
- assessment_id: identity
  area: identity
  topic: Exact original recipe and scoped dependency identity
  outcome: supported
  summary: The maintained JCM_J753 owner, current original JCM753 and current official
    APIJ753 identify the same source. Both current sources refer to separate JCM187
    iron/trace, JCM431 selenium, JCM197 vitamins and JCM403 B12 stocks; no source-version
    conflict is inferred from the older flattened local representation.
  target_ids:
  - CultureMech:003096
  evidence_ids:
  - jcm753
  - apiJ753
  - jcm187
  - jcm431
  - jcm197
  - jcm403
- assessment_id: structure
  area: schema
  topic: Original diagnostics and classification
  outcome: supported
  summary: All four original canonical checks passed; reference validation reports
    zero checks. LIQUID and COMPLEX/UNDEFINED are consistent with the aqueous yeast-containing
    medium. Passing native shape/label checks does not validate concentrations or
    supplied hydrates.
  target_ids:
  - CultureMech:003096
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
  - jcm753
  - apiJ753
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 67 current concentration fields are covered by 68 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:003096
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b072-quantity-inventory-v1","target":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","quantity_field_count":67,"decisions":[{"quantity_id":"q1","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.683594","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.683594","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    existing rate matches the explicit current provider g_l on its declared main volume1024
    basis. The primary independently supports the exact batch mass, but 900 mL input
    water plus later additions does not independently establish that denominator.
    Retain this qualified support without recalculating or inventing final volume.","source_stage":"main
    provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 0 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>SO<sub>4</sub>                                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.7&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 0.7,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.683594,\n                        \"mmol_l\":
    4.81269,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q2","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.195312","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.195312","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    existing rate matches the explicit current provider g_l on its declared main volume1024
    basis. The primary independently supports the exact batch mass, but 900 mL input
    water plus later additions does not independently establish that denominator.
    Retain this qualified support without recalculating or inventing final volume.","source_stage":"main
    provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 1 (zero-based)","quote":"<TR><TD WIDTH=75%> K<sub>2</sub>HPO<sub>4</sub>                                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.2&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.195312,\n                        \"mmol_l\":
    1.12135,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.244141","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.244141","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    existing rate matches the explicit current provider g_l on its declared main volume1024
    basis. The primary independently supports the exact batch mass, but 900 mL input
    water plus later additions does not independently establish that denominator.
    Retain this qualified support without recalculating or inventing final volume.","source_stage":"main
    provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 2 (zero-based)","quote":"<TR><TD WIDTH=75%> NH<sub>4</sub>Cl                                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.25&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.244141,\n                        \"mmol_l\":
    4.56423,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q4","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.244141","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.244141","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    existing rate matches the explicit current provider g_l on its declared main volume1024
    basis. The primary independently supports the exact batch mass, but 900 mL input
    water plus later additions does not independently establish that denominator.
    Retain this qualified support without recalculating or inventing final volume.","source_stage":"main
    provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 3 (zero-based)","quote":"<TR><TD WIDTH=75%> NaCl                                                    </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.25&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.244141,\n                        \"mmol_l\":
    4.17763,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q5","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.390625","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.390625","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    existing rate matches the explicit current provider g_l on its declared main volume1024
    basis. The primary independently supports the exact batch mass, but 900 mL input
    water plus later additions does not independently establish that denominator.
    Retain this qualified support without recalculating or inventing final volume.","source_stage":"main
    provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 4 (zero-based)","quote":"<TR><TD WIDTH=75%> MgCl<sub>2</sub>&#183;6H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.4&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.390625,\n                        \"mmol_l\":
    1.92139,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q6","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.488281","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.488281","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    existing rate matches the explicit current provider g_l on its declared main volume1024
    basis. The primary independently supports the exact batch mass, but 900 mL input
    water plus later additions does not independently establish that denominator.
    Retain this qualified support without recalculating or inventing final volume.","source_stage":"main
    provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 5 (zero-based)","quote":"<TR><TD WIDTH=75%> KCl                                                     </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.488281,\n                        \"mmol_l\":
    6.54972,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q7","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.146484","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.146484","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    existing rate matches the explicit current provider g_l on its declared main volume1024
    basis. The primary independently supports the exact batch mass, but 900 mL input
    water plus later additions does not independently establish that denominator.
    Retain this qualified support without recalculating or inventing final volume.","source_stage":"main
    provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 6 (zero-based)","quote":"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.15&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.146484,\n                        \"mmol_l\":
    0.996391,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q8","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000488281","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000488281","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    existing rate matches the explicit current provider g_l on its declared main volume1024
    basis. The primary independently supports the exact batch mass, but 900 mL input
    water plus later additions does not independently establish that denominator.
    Retain this qualified support without recalculating or inventing final volume.","source_stage":"main
    provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Resazurin                                               </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\":
    25,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.000488281,\n                        \"mmol_l\":
    0.00213046,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q9","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1.95312","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1.95312","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    existing rate matches the explicit current provider g_l on its declared main volume1024
    basis. The primary independently supports the exact batch mass, but 900 mL input
    water plus later additions does not independently establish that denominator.
    Retain this qualified support without recalculating or inventing final volume.","source_stage":"main
    provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 8 (zero-based)","quote":"<TR><TD WIDTH=75%> Yeast extract                                           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.95312,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"L-Cysteine
    HCl x H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.0488281","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.0488281","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    existing rate matches the explicit current provider g_l on its declared main volume1024
    basis. The primary independently supports the exact batch mass, but 900 mL input
    water plus later additions does not independently establish that denominator.
    Retain this qualified support without recalculating or inventing final volume.","source_stage":"main
    provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 12 (zero-based)","quote":"<TR><TD WIDTH=75%> L-Cysteine&#183;HCl&#183;H<sub>2</sub>O                      </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.05&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\":
    770,\n                        \"amount\": 0.05,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0488281,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"FeSO4
    x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.0244141","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.0244141","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    existing rate matches the explicit current provider g_l on its declared main volume1024
    basis. The primary independently supports the exact batch mass, but 900 mL input
    water plus later additions does not independently establish that denominator.
    Retain this qualified support without recalculating or inventing final volume.","source_stage":"main
    provider normalization; primary batch input","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 13 (zero-based)","quote":"<TR><TD WIDTH=75%> FeSO<sub>4</sub>&#183;7H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.025&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.025,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0244141,\n                        \"mmol_l\":
    0.0878156,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q12","label":"Potassium phosphate buffer","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is a volume addition per liter (final), not the same numeric G_PER_L. Preserve
    the stock identity, explicit strength and specified sterilization marker.","source_stage":"post-sterilization
    receiving-medium stock addition","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 15 (zero-based)","quote":"<TR><TD WIDTH=75%> 0.1 M Potassium phosphate
    buffer, pH 7.5               </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt
    lines 100-100","quote":"atmosphere, then, seal butyl rubber stoppers and autoclave.  Aseptically
    and anaerobically add per liter (final) the following sterile solutions (autoclaved
    or *filter-sterilized) from anaerobic stocks:","quote_basis":"derivative text"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[15]","quote":"{\n                        \"recipe_order\":
    16,\n                        \"compound\": \"Potassium phosphate buffer\",\n                        \"compound_id\":
    275,\n                        \"condition\": \" pH 7.5\",\n                        \"attribute\":
    \"0.1 M\",\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q13","label":"Trace vitamins (see Medium No. 197)","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is a volume addition per liter (final), not the same numeric G_PER_L. Preserve
    the stock identity, explicit strength and specified sterilization marker.","source_stage":"post-sterilization
    receiving-medium stock addition","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace vitamins (see Medium
    No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=197\">197</a>)*                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt
    lines 100-100","quote":"atmosphere, then, seal butyl rubber stoppers and autoclave.  Aseptically
    and anaerobically add per liter (final) the following sterile solutions (autoclaved
    or *filter-sterilized) from anaerobic stocks:","quote_basis":"derivative text"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[16]","quote":"{\n                        \"recipe_order\":
    17,\n                        \"compound\": \"Trace vitamins (see Medium No. 197)\",\n                        \"compound_id\":
    1784,\n                        \"attribute\": \"*\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"42","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"42","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is a volume addition per liter (final), not the same numeric G_PER_L. Preserve
    the stock identity, explicit strength and specified sterilization marker. The
    percentage basis is unspecified, so no density or percent-to-mass conversion is
    justified.","source_stage":"post-sterilization receiving-medium stock addition","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 18 (zero-based)","quote":"<TR><TD WIDTH=75%> 8% NaHCO<sub>3</sub> solution*                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;42.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt
    lines 100-100","quote":"atmosphere, then, seal butyl rubber stoppers and autoclave.  Aseptically
    and anaerobically add per liter (final) the following sterile solutions (autoclaved
    or *filter-sterilized) from anaerobic stocks:","quote_basis":"derivative text"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[18]","quote":"{\n                        \"recipe_order\":
    19,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"attribute\": \"*, 8%\",\n                        \"amount\":
    42,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"Sodium
    pyruvate","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"18","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is a volume addition per liter (final), not the same numeric G_PER_L. Preserve
    the stock identity, explicit strength and specified sterilization marker. The
    percentage basis is unspecified, so no density or percent-to-mass conversion is
    justified.","source_stage":"post-sterilization receiving-medium stock addition","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 19 (zero-based)","quote":"<TR><TD WIDTH=75%> 25% Sodium pyruvate solution*                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;18.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt
    lines 100-100","quote":"atmosphere, then, seal butyl rubber stoppers and autoclave.  Aseptically
    and anaerobically add per liter (final) the following sterile solutions (autoclaved
    or *filter-sterilized) from anaerobic stocks:","quote_basis":"derivative text"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[19]","quote":"{\n                        \"recipe_order\":
    20,\n                        \"compound\": \"Sodium pyruvate\",\n                        \"compound_id\":
    438,\n                        \"attribute\": \"*, 25%\",\n                        \"amount\":
    18,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"Sodium
    fumarate","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"40","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"40","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is a volume addition per liter (final), not the same numeric G_PER_L. Preserve
    the stock identity, explicit strength and specified sterilization marker. The
    percentage basis is unspecified, so no density or percent-to-mass conversion is
    justified.","source_stage":"post-sterilization receiving-medium stock addition","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 20 (zero-based)","quote":"<TR><TD WIDTH=75%> 16% Sodium fumarate solution*                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;40.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt
    lines 100-100","quote":"atmosphere, then, seal butyl rubber stoppers and autoclave.  Aseptically
    and anaerobically add per liter (final) the following sterile solutions (autoclaved
    or *filter-sterilized) from anaerobic stocks:","quote_basis":"derivative text"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[20]","quote":"{\n                        \"recipe_order\":
    21,\n                        \"compound\": \"Sodium fumarate\",\n                        \"compound_id\":
    1752,\n                        \"attribute\": \"*, 16%\",\n                        \"amount\":
    40,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q17","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider places this amount/rate inside a separate iron, trace-element or selenium
    stock. It is flattened as a direct medium ingredient locally. Restore its source
    stock and independently represented receiving dose; the provider stock rate is
    not a final-medium rate. The HCl row also carries 7.7 M and 25% reagent attributes
    with 10 mL input. Its g_l=2.5 is not independently endorsed without an explicit
    percentage basis; retain the supported reagent strength and dose instead.","source_stage":"separate
    provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"7.7 M, 25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q18","label":"FeCl2
    x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider places this amount/rate inside a separate iron, trace-element or selenium
    stock. It is flattened as a direct medium ingredient locally. Restore its source
    stock and independently represented receiving dose; the provider stock rate is
    not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q19","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider places this amount/rate inside a separate iron, trace-element or selenium
    stock. It is flattened as a direct medium ingredient locally. Restore its source
    stock and independently represented receiving dose; the provider stock rate is
    not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q20","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider places this amount/rate inside a separate iron, trace-element or selenium
    stock. It is flattened as a direct medium ingredient locally. Restore its source
    stock and independently represented receiving dose; the provider stock rate is
    not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q21","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider places this amount/rate inside a separate iron, trace-element or selenium
    stock. It is flattened as a direct medium ingredient locally. Restore its source
    stock and independently represented receiving dose; the provider stock rate is
    not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q22","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider places this amount/rate inside a separate iron, trace-element or selenium
    stock. It is flattened as a direct medium ingredient locally. Restore its source
    stock and independently represented receiving dose; the provider stock rate is
    not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[3].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q23","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider places this amount/rate inside a separate iron, trace-element or selenium
    stock. It is flattened as a direct medium ingredient locally. Restore its source
    stock and independently represented receiving dose; the provider stock rate is
    not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[3].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q24","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider places this amount/rate inside a separate iron, trace-element or selenium
    stock. It is flattened as a direct medium ingredient locally. Restore its source
    stock and independently represented receiving dose; the provider stock rate is
    not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[3].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q25","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider places this amount/rate inside a separate iron, trace-element or selenium
    stock. It is flattened as a direct medium ingredient locally. Restore its source
    stock and independently represented receiving dose; the provider stock rate is
    not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[3].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q26","label":"NaOH","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.4","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.4","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider places this amount/rate inside a separate iron, trace-element or selenium
    stock. It is flattened as a direct medium ingredient locally. Restore its source
    stock and independently represented receiving dose; the provider stock rate is
    not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[4].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.4,\n                        \"mmol_l\":
    10.0007,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q27","label":"Na2SeO3 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider places this amount/rate inside a separate iron, trace-element or selenium
    stock. It is flattened as a direct medium ingredient locally. Restore its source
    stock and independently represented receiving dose; the provider stock rate is
    not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[4].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0228125,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q28","label":"Na2WO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.008","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.008","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider places this amount/rate inside a separate iron, trace-element or selenium
    stock. It is flattened as a direct medium ingredient locally. Restore its source
    stock and independently represented receiving dose; the provider stock rate is
    not a final-medium rate.","source_stage":"separate provider stock","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[4].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 8,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.008,\n                        \"mmol_l\":
    0.0242534,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q29","label":"B12 receiving dose","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary explicitly calls for 1 mL per liter (final) of the separately defined
    B12 stock, filter-sterilized; 1 G_PER_L does not represent this dose. The empty
    composition and Unknown solution name do not resolve the cross-reference.","source_stage":"B12
    receiving addition","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 17 (zero-based)","quote":"<TR><TD WIDTH=75%> Vitamin B<sub>1</sub><sub>2</sub>
    solution (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=403\">403</a>)*      </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt
    lines 100-100","quote":"atmosphere, then, seal butyl rubber stoppers and autoclave.  Aseptically
    and anaerobically add per liter (final) the following sterile solutions (autoclaved
    or *filter-sterilized) from anaerobic stocks:","quote_basis":"derivative text"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[17]","quote":"{\n                        \"recipe_order\":
    18,\n                        \"compound\": \"Vitamin B12 solution (see Medium
    No. 403)\",\n                        \"compound_id\": 1845,\n                        \"attribute\":
    \"*\",\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q30","label":"Source-only iron dose","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this explicitly stated initial batch volume in its own receiving stage. It is
    not a final-liter normalization, a stock recipe volume, or an inferred mass.","source_stage":"initial
    receiving batch","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 9 (zero-based)","quote":"<TR><TD WIDTH=75%> FeCl<sub>2</sub> solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>)                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"solution\": \"FeCl2 solution\",\n                        \"solution_id\":
    3846,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q31","label":"Source-only trace dose","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this explicitly stated initial batch volume in its own receiving stage. It is
    not a final-liter normalization, a stock recipe volume, or an inferred mass.","source_stage":"initial
    receiving batch","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 10 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>)           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\":
    3847,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q32","label":"Source-only selenium dose","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this explicitly stated initial batch volume in its own receiving stage. It is
    not a final-liter normalization, a stock recipe volume, or an inferred mass.","source_stage":"initial
    receiving batch","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> Selenite-tungstate solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=431\">431</a>)     </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    4172,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q33","label":"Source-only main water","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this explicitly stated initial batch volume in its own receiving stage. It is
    not a final-liter normalization, a stock recipe volume, or an inferred mass.","source_stage":"initial
    receiving batch","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 14 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;900.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[14]","quote":"{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 900,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q34","label":"Retained buffer pH note","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[11].notes","stored":"
    ( pH 7.5)"},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ingredients[11].notes","stored":"
    ( pH 7.5)"}],"decision":"evidence_only","rationale":"The retained pH7.5 note accurately
    belongs to the potassium-phosphate buffer. The missing 0.1 M stock strength and
    volume-unit defect are addressed separately.","source_stage":"buffer reagent","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"HTML
    table row 15 (zero-based)","quote":"<TR><TD WIDTH=75%> 0.1 M Potassium phosphate
    buffer, pH 7.5               </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].recipe[15]","quote":"{\n                        \"recipe_order\":
    16,\n                        \"compound\": \"Potassium phosphate buffer\",\n                        \"compound_id\":
    275,\n                        \"condition\": \" pH 7.5\",\n                        \"attribute\":
    \"0.1 M\",\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q35","label":"Retained preparation 1","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"preparation_steps[0].description","stored":"Mix
    components except L-cysteine x HCl x H2O and FeSO4 x 7H2O. Bring to a boil for
    a few seconds and cool down under a N2 atmosphere. While gassing with N2, add
    L-cysteine x HCl x H2O and FeSO4 x 7H2O to the solution, distribute into culture
    vessels (e.g., 18 ml in 50 ml serum bottles) under a N2 atmosphere, then, seal
    butyl rubber stoppers and autoclave. Aseptically and anaerobically add per liter
    (final) the following sterile solutions (autoclaved or *filter-sterilized) from
    anaerobic stocks:"},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"preparation_steps[0].description","stored":"Mix
    components except L-cysteine x HCl x H2O and FeSO4 x 7H2O. Bring to a boil for
    a few seconds and cool down under a N2 atmosphere. While gassing with N2, add
    L-cysteine x HCl x H2O and FeSO4 x 7H2O to the solution, distribute into culture
    vessels (e.g., 18 ml in 50 ml serum bottles) under a N2 atmosphere, then, seal
    butyl rubber stoppers and autoclave. Aseptically and anaerobically add per liter
    (final) the following sterile solutions (autoclaved or *filter-sterilized) from
    anaerobic stocks:"}],"decision":"evidence_only","rationale":"The complete retained
    description is supported, including its vessel example, gas context, sequential
    addition or final pH range. Credit this existing text; the unresolved stock table
    representation does not mean all preparation is absent.","source_stage":"retained
    receiving preparation","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"recipe_order\":
    16,\n                        \"step\": \"Mix components except L-cysteine x HCl
    x H2O and FeSO4 x 7H2O. Bring to a boil for a few seconds and cool down under
    a N2 atmosphere. While gassing with N2, add L-cysteine x HCl x H2O and FeSO4 x
    7H2O to the solution, distribute into culture vessels (e.g., 18 ml in 50 ml serum
    bottles) under a N2 atmosphere, then, seal butyl rubber stoppers and autoclave.
    Aseptically and anaerobically add per liter (final) the following sterile solutions
    (autoclaved or *filter-sterilized) from anaerobic stocks: \"\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt
    lines 82-100","quote":"Mix components except L-cysteine·HCl·H\n2\nO and FeSO\n4\n·7H\n2\nO.
    Bring to a boil for a few seconds and cool down under a N\n2\natmosphere. While
    gassing with N\n2\n, add L-cysteine·HCl·H\n2\nO and FeSO\n4\n·7H\n2\nO to the
    solution, distribute into culture vessels (e.g., 18 ml in 50 ml serum bottles)
    under a N\n2\natmosphere, then, seal butyl rubber stoppers and autoclave.  Aseptically
    and anaerobically add per liter (final) the following sterile solutions (autoclaved
    or *filter-sterilized) from anaerobic stocks:","quote_basis":"derivative text"}]},{"quantity_id":"q36","label":"Retained
    preparation 2","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"preparation_steps[1].description","stored":"Adjust
    pH of the medium to 7.3 - 7.7, if necessary."},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"preparation_steps[1].description","stored":"Adjust
    pH of the medium to 7.3 - 7.7, if necessary."}],"decision":"evidence_only","rationale":"The
    complete retained description is supported, including its vessel example, gas
    context, sequential addition or final pH range. Credit this existing text; the
    unresolved stock table representation does not mean all preparation is absent.","source_stage":"retained
    receiving preparation","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.solutions[1].steps[1]","quote":"{\n                        \"step\":
    \"Adjust pH of the medium to 7.3 - 7.7, if necessary.\"\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt
    lines 128-128","quote":"Adjust pH of the medium to 7.3 - 7.7, if necessary.","quote_basis":"derivative
    text"}]},{"quantity_id":"q37","label":"Retained representative pH","local_fields":[{"path":"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ph_value","stored":7.5},{"path":"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml","field_path":"ph_value","stored":7.5}],"decision":"evidence_only","rationale":"7.5
    matches provider metadata and lies within the original 7.3–7.7 range already retained
    in preparation. It is a representative scalar, not proof that the source requires
    exactly7.5.","source_stage":"receiving-medium pH","sources":[{"evidence_id":"apiJ753","reference":"https://mediadive.dsmz.de/rest/medium/J753","raw_path":"REVIEW_WORK/batch072/source07-08-10/apiJ753.raw","raw_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","text_sha256":"0c24e5b2776ca3253393a2106c9483fb0031a6992b1b51f4c5e6b094c1efcd91","accessed_at":"2026-10-28T16:14:44.272325Z","locator":"data.medium","quote":"{\n            \"id\":
    \"J753\",\n            \"name\": \"DEHALOSPIRILLUM MEDIUM\",\n            \"complex_medium\":
    \"yes\",\n            \"min_pH\": 7.5,\n            \"max_pH\": 7.5,\n            \"source\":
    \"JCM\",\n            \"link\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753\"\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt
    lines 128-128","quote":"Adjust pH of the medium to 7.3 - 7.7, if necessary.","quote_basis":"derivative
    text"}]},{"quantity_id":"q38","label":"JCM default autoclave control","local_fields":[],"decision":"evidence_only","rationale":"The
    site explicitly supplies 121°C for15min unless otherwise stated. Preserve this
    default only for applicable autoclave steps; explicitly asterisked filter additions
    retain their override.","source_stage":"source-only preparation control","sources":[{"evidence_id":"jcm753","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=753","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm753.raw","raw_sha256":"951b851e297e5b1db5efc4475d36f682c16518ee5fb8d9224b20a1d75ffdf972","text_sha256":"9f1c1194aafc8114468b14ad0432130b515acef605bdfb6c4c584c5dd9eff66f","accessed_at":"2026-10-28T16:14:43.703086Z","locator":"jcm753.txt
    lines 4-4","quote":"Unless otherwise stated, sterilize media by autoclaving at
    121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q39","label":"Retained
    M180 Distilled water","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[0].concentration","stored":{"value":"0.99","unit":"L"}}],"decision":"verified","rationale":"Existing
    attached literal source claim and its original digest match the current source
    bytes. Retain this exact stock batch input, not a measured final-volume concentration;
    historical duplicate notes are superseded context.","source_stage":"M180 iron
    or trace stock only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 990,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q40","label":"Retained
    M180 FeCl2・4H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[1].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 1.5 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing attached literal
    source claim and its original digest match the current source bytes. Retain this
    exact stock batch input, not a measured final-volume concentration; historical
    duplicate notes are superseded context.","source_stage":"M180 iron or trace stock
    only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
    \"FeCl2・4H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001548\",\n          \"gmo_id\": \"GMO_001548\",\n          \"label\":
    \"Iron(II) chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q41","label":"Retained
    M180 Distilled water","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"Existing
    attached literal source claim and its original digest match the current source
    bytes. Retain this exact stock batch input, not a measured final-volume concentration;
    historical duplicate notes are superseded context.","source_stage":"M180 iron
    or trace stock only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q42","label":"Retained
    M180 Na2MoO4・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 36 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing attached literal
    source claim and its original digest match the current source bytes. Retain this
    exact stock batch input, not a measured final-volume concentration; historical
    duplicate notes are superseded context.","source_stage":"M180 iron or trace stock
    only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\":
    \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\":
    \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q43","label":"Retained
    M180 H3BO3","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 6 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing attached literal
    source claim and its original digest match the current source bytes. Retain this
    exact stock batch input, not a measured final-volume concentration; historical
    duplicate notes are superseded context.","source_stage":"M180 iron or trace stock
    only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\":
    \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\":
    \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q44","label":"Retained
    M180 MnCl2・4H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 100 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing attached literal
    source claim and its original digest match the current source bytes. Retain this
    exact stock batch input, not a measured final-volume concentration; historical
    duplicate notes are superseded context.","source_stage":"M180 iron or trace stock
    only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\":
    \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\":
    \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q45","label":"Retained
    M180 CoCl2・6H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 190 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing attached literal
    source claim and its original digest match the current source bytes. Retain this
    exact stock batch input, not a measured final-volume concentration; historical
    duplicate notes are superseded context.","source_stage":"M180 iron or trace stock
    only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\":
    \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\":
    \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q46","label":"Retained
    M180 NiCl2・6H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 24 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing attached literal
    source claim and its original digest match the current source bytes. Retain this
    exact stock batch input, not a measured final-volume concentration; historical
    duplicate notes are superseded context.","source_stage":"M180 iron or trace stock
    only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
    \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\":
    \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q47","label":"Retained
    M180 CuCl2・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 2 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing attached literal
    source claim and its original digest match the current source bytes. Retain this
    exact stock batch input, not a measured final-volume concentration; historical
    duplicate notes are superseded context.","source_stage":"M180 iron or trace stock
    only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
    \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\":
    \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q48","label":"Retained
    M180 ZnCl2","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 70 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing attached literal
    source claim and its original digest match the current source bytes. Retain this
    exact stock batch input, not a measured final-volume concentration; historical
    duplicate notes are superseded context.","source_stage":"M180 iron or trace stock
    only","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\":
    \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\": \"GMO_001035\",\n          \"label\":
    \"Zinc chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q49","label":"Retained
    nested HCl solutions[0].solutions[0].composition[0].concentration","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].composition[0].concentration","stored":{"value":"7.7","unit":"MOLAR"}}],"decision":"verified","rationale":"Explicit
    7.7 M reagent strength is supported by its attached exact claim; the accompanying
    25% basis is unspecified.","source_stage":"M180 iron-stock nested reagent","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
    \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\":
    25,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\":
    \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q50","label":"Retained
    nested HCl solutions[0].solutions[0].concentration","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].concentration","stored":{"value":"0.01","unit":"L"}}],"decision":"verified","rationale":"The
    root evidence contains an additional exact HCl excerpt and this nested descriptor
    locator, authenticating 10 mL = 0.01 L into the iron stock; it is not the excluded
    parent-medium receiving dose.","source_stage":"M180 iron-stock nested reagent","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
    \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\":
    25,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\":
    \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q51","label":"Retained
    HCl input-dose note","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].notes","stored":"Source
    stock addition: 10 ml = 0.01 L per receiving batch, not grams per liter or a dose
    per final liter."}],"decision":"verified","rationale":"The retained numeric note
    has the same exact scoped root attachment as the nested descriptor; no new dose
    or final concentration is inferred.","source_stage":"M180 nested HCl","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T16:13:13.892859Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
    \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\":
    25,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\":
    \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q52","label":"Scoped
    M431 Na2SeO3・5H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"6","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source lists 6 mg in the selenite-tungstate stock with 1 L input water. The stored
    g/L copies a milligram number and loses stock stage. Do not transfer the parent
    medium dose or collapsed shared water.","source_stage":"selenite-tungstate stock","sources":[{"evidence_id":"togo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T16:13:14.150946Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\":
    \"Na2SeO3・5H2O\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001046\",\n          \"gmo_id\": \"GMO_001046\",\n          \"label\":
    \"Sodium selenite pentahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q53","label":"Scoped
    M431 Na2WO4・2H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source lists 8 mg in the selenite-tungstate stock with 1 L input water. The stored
    g/L copies a milligram number and loses stock stage. Do not transfer the parent
    medium dose or collapsed shared water.","source_stage":"selenite-tungstate stock","sources":[{"evidence_id":"togo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T16:13:14.150946Z","locator":"components[3].items[2]","quote":"{\n          \"component_name\":
    \"Na2WO4・2H2O\",\n          \"volume\": 8,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001057\",\n          \"gmo_id\": \"GMO_001057\",\n          \"label\":
    \"Sodium tungstate dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q54","label":"Scoped
    M431 NaOH","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.4","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    source lists 0.4 g in the selenite-tungstate stock with 1 L input water. The numeric
    gram input is supported, but the current g/L assertion lacks an explicit final-stock-volume
    basis. Do not transfer the parent medium dose or collapsed shared water.","source_stage":"selenite-tungstate
    stock","sources":[{"evidence_id":"togo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T16:13:14.150946Z","locator":"components[3].items[3]","quote":"{\n          \"component_name\":
    \"NaOH\",\n          \"volume\": 0.4,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001078\",\n          \"gmo_id\": \"GMO_001078\",\n          \"label\":
    \"Sodium hydroxide\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q55","label":"Selenite stock water","local_fields":[],"decision":"evidence_only","rationale":"The
    source 1 L is stock input water, not the local collapsed water row and not measured
    final volume.","source_stage":"source-only selenite stock","sources":[{"evidence_id":"togo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T16:13:14.150946Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q56","label":"Retained
    M190 Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"The
    retained stock batch input has an exact attached literal claim and digest matching
    the current TOGO bytes, corroborated by the original JCM vitamin row. Preserve
    this batch note or water volume; no absent final-stock concentration is asserted.","source_stage":"M190
    trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML
    table row 25 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q57","label":"Retained
    M190 Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 2 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained stock batch
    input has an exact attached literal claim and digest matching the current TOGO
    bytes, corroborated by the original JCM vitamin row. Preserve this batch note
    or water volume; no absent final-stock concentration is asserted.","source_stage":"M190
    trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
    \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\":
    \"Biotin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML
    table row 15 (zero-based)","quote":"<TR><TD WIDTH=75%> Biotin                                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q58","label":"Retained
    M190 p--Aminobenzoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained stock batch
    input has an exact attached literal claim and digest matching the current TOGO
    bytes, corroborated by the original JCM vitamin row. Preserve this batch note
    or water volume; no absent final-stock concentration is asserted.","source_stage":"M190
    trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
    \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\":
    \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML
    table row 23 (zero-based)","quote":"<TR><TD WIDTH=75%> <I>p</I>-Aminobenzoic acid                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q59","label":"Retained
    M190 Thiamine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained stock batch
    input has an exact attached literal claim and digest matching the current TOGO
    bytes, corroborated by the original JCM vitamin row. Preserve this batch note
    or water volume; no absent final-stock concentration is asserted.","source_stage":"M190
    trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\":
    \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\":
    \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML
    table row 18 (zero-based)","quote":"<TR><TD WIDTH=75%> Thiamine&#183;HCl                                      </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q60","label":"Retained
    M190 Calcium pantothenate","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained stock batch
    input has an exact attached literal claim and digest matching the current TOGO
    bytes, corroborated by the original JCM vitamin row. Preserve this batch note
    or water volume; no absent final-stock concentration is asserted.","source_stage":"M190
    trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\":
    \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001028\",\n          \"gmo_id\": \"GMO_001028\",\n          \"label\":
    \"Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML
    table row 21 (zero-based)","quote":"<TR><TD WIDTH=75%> Calcium pantothenate                                    </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q61","label":"Retained
    M190 Pyridoxine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 10 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained stock batch
    input has an exact attached literal claim and digest matching the current TOGO
    bytes, corroborated by the original JCM vitamin row. Preserve this batch note
    or water volume; no absent final-stock concentration is asserted.","source_stage":"M190
    trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\":
    \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\":
    \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML
    table row 17 (zero-based)","quote":"<TR><TD WIDTH=75%> Pyridoxine&#183;HCl                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q62","label":"Retained
    M190 Folic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 2 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained stock batch
    input has an exact attached literal claim and digest matching the current TOGO
    bytes, corroborated by the original JCM vitamin row. Preserve this batch note
    or water volume; no absent final-stock concentration is asserted.","source_stage":"M190
    trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\":
    \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\":
    \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> Folic acid                                              </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q63","label":"Retained
    M190 Vitamin B12","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 0.1 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained stock batch
    input has an exact attached literal claim and digest matching the current TOGO
    bytes, corroborated by the original JCM vitamin row. Preserve this batch note
    or water volume; no absent final-stock concentration is asserted.","source_stage":"M190
    trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\":
    \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\":
    \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML
    table row 22 (zero-based)","quote":"<TR><TD WIDTH=75%> Vitamin B<sub>1</sub><sub>2</sub>                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q64","label":"Retained
    M190 Riboflavin","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[8].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained stock batch
    input has an exact attached literal claim and digest matching the current TOGO
    bytes, corroborated by the original JCM vitamin row. Preserve this batch note
    or water volume; no absent final-stock concentration is asserted.","source_stage":"M190
    trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\":
    \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\":
    \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML
    table row 19 (zero-based)","quote":"<TR><TD WIDTH=75%> Riboflavin                                              </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q65","label":"Retained
    M190 Nicotinic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[9].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained stock batch
    input has an exact attached literal claim and digest matching the current TOGO
    bytes, corroborated by the original JCM vitamin row. Preserve this batch note
    or water volume; no absent final-stock concentration is asserted.","source_stage":"M190
    trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\":
    \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\":
    \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML
    table row 20 (zero-based)","quote":"<TR><TD WIDTH=75%> Nicotinic acid                                          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q66","label":"Retained
    M190 Lipoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[10].notes","stored":"Role:
    Growth factor; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained stock batch
    input has an exact attached literal claim and digest matching the current TOGO
    bytes, corroborated by the original JCM vitamin row. Preserve this batch note
    or water volume; no absent final-stock concentration is asserted.","source_stage":"M190
    trace-vitamin stock only","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T16:13:13.927889Z","locator":"components[1].items[10]","quote":"{\n          \"component_name\":
    \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\": \"GMO_001699\",\n          \"label\":
    \"Lipoic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch072/publish-source-preflight/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T16:13:13.544054Z","locator":"HTML
    table row 24 (zero-based)","quote":"<TR><TD WIDTH=75%> Lipoic acid                                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q67","label":"M401
    B12 stock batch amount","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact referenced B12 stock contains5mg with100mL input water, not5g/L. Restore
    milligram batch amount inside the named stock; input water alone does not certify
    measured final100mL or a calculated final-stock concentration.","source_stage":"B12
    stock only","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch072/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T16:14:44.975240Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\":
    \"Vitamin B12\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\":
    \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T16:14:44.172479Z","locator":"HTML
    table row 26 (zero-based)","quote":"<TR><TD WIDTH=75%> Vitamin B<sub>1</sub><sub>2</sub>                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q68","label":"B12
    stock input water","local_fields":[],"decision":"evidence_only","rationale":"The
    stock lists100mL water; exclude M401 collapsed shared water101G_PER_L and parent
    receiving dose. No final-volume assertion is substituted.","source_stage":"B12
    stock only","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch072/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T16:14:44.975240Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch072/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T16:14:44.172479Z","locator":"HTML
    table row 27 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/DEHALOSPIRILLUM_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml":null,"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml":["solutions[0].composition","solutions[0].solutions","solutions[1].composition"],"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml":["ingredients[27]","ingredients[28]","ingredients[29]","solutions[1].name","solutions[1].preferred_term","solutions[1].composition"],"data/normalized_yaml/bacterial/togo_medium_m190.yaml":["solutions[1].composition"],"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml":["ingredients[25]","solutions[3].name","solutions[3].preferred_term","solutions[3].composition"]},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: Fresh asserted ontology objects, formulas, stereochemistry and synonyms
    were read with exact current MIM identifier and preferred-term rows. Selected
    CoCl2 hexahydrate is already correctly53503; nickel is not. Scoped M180 cobalt/nickel
    mismatch is separate. Generic source calcium pantothenate in M190 does not resolve
    the stereochemistry represented by31345, so this is an explicit uncertainty rather
    than a confirmed wrong-ID claim. Neutral resazurin is compatible with its unqualified
    source name; generic vitamin B12 remains generic. Canonical labels and MIM membership
    do not certify supplied form.
  target_ids:
  - CultureMech:003096
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: All22 input reports were read completely through lossless pooled cells;
    repeated08 cells were reused by exact equality and all687 new cells read separately.
    Exact JCM753 current API digest matches the cited October7 response, and matching
    decoded objects authenticate current content without recovering the original access
    event. The October source-unchecked diagnostic and earlier broad merge recommendations
    are not scientific evidence by themselves. M180/M190 applied repair reports and
    exact attached current claims receive field-specific credit; M401, M431 and neighboring
    generated records remain scoped dependency context. Current importer and conservative
    formulation gate fixes are credited separately from historical generated data.
  target_ids:
  - CultureMech:003096
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-003096-stock-topology
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore explicit receiving doses and separate stock formulations
  description: The target and maintained owner flatten the iron, trace-element and
    selenium stock rows as direct medium ingredients and omit their three initial
    batch doses. Later buffer, vitamin, bicarbonate, pyruvate, fumarate and B12 additions
    are volumes per liter (final), not matching numeric G_PER_L. Preserve the provider-declared
    main rates only on their declared1024mL basis; restore the900mL input water and
    named stock graph without inferred final-volume arithmetic. Retain unspecified
    percentage bases and explicit filter overrides.
  target_ids:
  - CultureMech:003096
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  evidence_ids:
  - jcm753
  - apiJ753
  - quantities
  - writer-mediadive
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-003096-scoped-dependency-units
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Resolve named vitamin and selenium dependencies with source-specific scope
  description: M180 iron/trace and M190 trace-vitamin repairs already preserve supported
    batch inputs and attached source claims, including nested HCl. Reuse only those
    subsections. The M431 selenium/tungstate numbers still confuse milligrams with
    grams per liter, and M401 B12 remains5G_PER_L instead of the source5mg stock batch
    input. Correct only those scoped compositions; preserve stock input water, exclude
    parent receiving doses and unrelated recipes, and replace Unknown solution placeholders
    with their already-known identities.
  target_ids:
  - CultureMech:003096
  field_paths:
  - solutions[0].composition
  - solutions[0].name
  - data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml::ingredients[27].concentration
  - data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml::ingredients[28].concentration
  - data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml::ingredients[25].concentration
  - data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml::solutions[3].name
  evidence_ids:
  - jcm403
  - currentTogo401
  - jcm431
  - togo431
  - togo180
  - togo190
  - quantities
  - old-claims
  - writer-stock
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/togo_medium_m190.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml
    role: scoped dependency
- finding_id: f3
  issue_key: culturemech-003096-nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Resolve exact nickel hydrate and scoped inherited cobalt form
  description: Both selected records name NiCl2 hexahydrate but assert anhydrous CHEBI:34887
    in primary and secondary slots. Current OLS independently identifies hydrate candidate53542;
    current MIM rows are not acceptance evidence for that candidate. The scoped M180
    trace stock also retains anhydrous cobalt35696/nickel34887 assignments under hexahydrate
    names. Correct supplied forms only after exact term review; do not infer hydrate
    equivalence from label agreement or convert amounts.
  target_ids:
  - CultureMech:003096
  field_paths:
  - ingredients[23].term
  - ingredients[23].mediaingredientmech_chebi_term
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[1].composition[4].term
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[1].composition[5].term
  evidence_ids:
  - jcm187
  - apiJ753
  - chebi53542
  - groundings
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    role: scoped dependency
- finding_id: f4
  issue_key: culturemech-003096-claim-completeness
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Attach current support while retaining existing preparation credit
  description: The selected records preserve two substantive preparation descriptions
    and a representative pH scalar, but lack attached claim-level evidence for the
    supported provider rates and procedure. Preserve the exact7.3–7.7 range, buffer
    pH7.5 distinction, source default autoclave controls and filter overrides when
    curating. Append a new actual history event; historical raw equality authenticates
    content, not a replayed access event.
  target_ids:
  - CultureMech:003096
  field_paths:
  - evidence
  - preparation_steps
  - ph_value
  - curation_history
  evidence_ids:
  - jcm753
  - apiJ753
  - quantities
  - old-reports
  - historical-object-joins
  rule_id: review-yaml-record/evidence
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml
    role: maintained source
actions:
- action_id: a1
  description: The target and maintained owner flatten the iron, trace-element and
    selenium stock rows as direct medium ingredients and omit their three initial
    batch doses. Later buffer, vitamin, bicarbonate, pyruvate, fumarate and B12 additions
    are volumes per liter (final), not matching numeric G_PER_L. Preserve the provider-declared
    main rates only on their declared1024mL basis; restore the900mL input water and
    named stock graph without inferred final-volume arithmetic. Retain unspecified
    percentage bases and explicit filter overrides.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003096
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml
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
  description: M180 iron/trace and M190 trace-vitamin repairs already preserve supported
    batch inputs and attached source claims, including nested HCl. Reuse only those
    subsections. The M431 selenium/tungstate numbers still confuse milligrams with
    grams per liter, and M401 B12 remains5G_PER_L instead of the source5mg stock batch
    input. Correct only those scoped compositions; preserve stock input water, exclude
    parent receiving doses and unrelated recipes, and replace Unknown solution placeholders
    with their already-known identities.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003096
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/togo_medium_m190.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml
    role: scoped dependency
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a3
  description: Both selected records name NiCl2 hexahydrate but assert anhydrous CHEBI:34887
    in primary and secondary slots. Current OLS independently identifies hydrate candidate53542;
    current MIM rows are not acceptance evidence for that candidate. The scoped M180
    trace stock also retains anhydrous cobalt35696/nickel34887 assignments under hexahydrate
    names. Correct supplied forms only after exact term review; do not infer hydrate
    equivalence from label agreement or convert amounts.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003096
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    role: scoped dependency
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a4
  description: The selected records preserve two substantive preparation descriptions
    and a representative pH scalar, but lack attached claim-level evidence for the
    supported provider rates and procedure. Preserve the exact7.3–7.7 range, buffer
    pH7.5 distinction, source default autoclave controls and filter overrides when
    curating. Append a new actual history event; historical raw equality authenticates
    content, not a replayed access event.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:003096
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J753_DEHALOSPIRILLUM_MEDIUM.yaml
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
- Current provider volume1024 and its explicit main rates are retained as declared
  provider normalization; the primary900mL input and later per-liter additions do
  not independently establish measured final volume.
- Only M180 iron/trace, M190 trace vitamins, M431 selenium-tungstate and M401 B12
  composition are scientifically assessed. Parent quantities and parent receiving
  instructions are excluded.
- Generic calcium-pantothenate stereochemistry, unspecified percentage bases and generic
  hydrate wording remain unresolved; no molar or mass conversion is inferred from
  ontology labels.
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
