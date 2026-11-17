# Scientific review: CYS MEDIUM FOR YMO722

- Review: 20261028T132113Z-culturemech-002966-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T13:11:30.762120Z
- Finished UTC: 2026-10-28T13:21:13.592151Z
- Reviewer: Codex batch006_validation (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The maintained JCM 618/619 records already preserve the explicit salinity override and stock hierarchy. The generated YMO722 target is stale: its main rates use initial-water normalization, its trace rows turn 100 µL doses into 100 G_PER_L, and nickel loses the corrected hydrate. Preserve the distinct parent/variant scopes and supported owner repairs while adding exact claim evidence and regenerating conservatively.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch068 index 02
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002966 | data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml | generated | cys_medium_for_ymo722 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:002966 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:002966 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:002966 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:002966 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Source and maintained repair boundaries

identity: concern. Targets: CultureMech:002966.

Exact JCM 619 wrapper identity and environmental YMO722 catalog identity are resolved. The parent and variant are distinct; no strain-growth assertion is copied from a catalogue.

### Current repair credit

representation: supported. Targets: CultureMech:002966.

The two maintained owners correctly preserve distinct NaCl overrides, main masses, stock strengths/doses, pH, initial water and preparation. This credit does not certify missing attached evidence or the stale generated record.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:002966.

58 current concentration fields are covered by 41 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b068-quantity-inventory-v1","target":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","quantity_field_count":58,"decisions":[{"quantity_id":"q1","label":"Generated N-Z-Case","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3.33333","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The generated value reproduces the API normalization to the initial 900 mL. The primary explicitly makes the completed medium to 1.0 L, so the current final-medium rate is wrong. Credit the provider digits only on their declared initial-volume basis; preserve the source mass and supported corrected owner rate.","source_stage":"Generated stale main-medium concentration","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 0 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; N-Z-Case (Wako)                                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"N-Z-Case\",\n                        \"compound_id\": 1829,\n                        \"attribute\": \"Wako\",\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.33333,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"Generated Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2.22222","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The generated value reproduces the API normalization to the initial 900 mL. The primary explicitly makes the completed medium to 1.0 L, so the current final-medium rate is wrong. Credit the provider digits only on their declared initial-volume basis; preserve the source mass and supported corrected owner rate.","source_stage":"Generated stale main-medium concentration","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 1 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Yeast extract (BD-Difco)                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.22222,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"Generated Starch","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1.11111","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The generated value reproduces the API normalization to the initial 900 mL. The primary explicitly makes the completed medium to 1.0 L, so the current final-medium rate is wrong. Credit the provider digits only on their declared initial-volume basis; preserve the source mass and supported corrected owner rate.","source_stage":"Generated stale main-medium concentration","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 2 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Soluble starch (BD-Difco)                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Starch\",\n                        \"compound_id\": 199,\n                        \"attribute\": \"BD-Difco, soluble\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.11111,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"Generated NaCl","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[3].concentration","stored":{"value":"22.2222","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The generated 22.2222 g/L derives from the parent API 20 g normalized to 900 mL, while the exact JCM 619 wrapper explicitly requires 16.0 g/L final NaCl. Neither the parent 20 g/L nor its API initial-volume normalization may replace the selected variant override.","source_stage":"Generated stale main-medium concentration","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 3 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 22.2222,\n                        \"mmol_l\": 380.257,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q5","label":"Generated MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.138889","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The generated value reproduces the API normalization to the initial 900 mL. The primary explicitly makes the completed medium to 1.0 L, so the current final-medium rate is wrong. Credit the provider digits only on their declared initial-volume basis; preserve the source mass and supported corrected owner rate.","source_stage":"Generated stale main-medium concentration","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 4 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.125&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.125,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.138889,\n                        \"mmol_l\": 0.683162,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"Generated CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.0277778","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The generated value reproduces the API normalization to the initial 900 mL. The primary explicitly makes the completed medium to 1.0 L, so the current final-medium rate is wrong. Credit the provider digits only on their declared initial-volume basis; preserve the source mass and supported corrected owner rate.","source_stage":"Generated stale main-medium concentration","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 5 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.025&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.025,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0277778,\n                        \"mmol_l\": 0.188945,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"Generated FeSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.0111111","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The generated value reproduces the API normalization to the initial 900 mL. The primary explicitly makes the completed medium to 1.0 L, so the current final-medium rate is wrong. Credit the provider digits only on their declared initial-volume basis; preserve the source mass and supported corrected owner rate.","source_stage":"Generated stale main-medium concentration","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 6 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0111111,\n                        \"mmol_l\": 0.0399659,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Generated trace row Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[7].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source specifies a 100 µL stock addition, with its own parenthesized g/L stock strength. The current 100 G_PER_L is neither that stock strength nor a receiving-medium rate. The API unit is corrupted text, so the literal primary µL row establishes the dimension. Preserve the repaired owners separate stock and dose objects.","source_stage":"Stock receiving volume, not solute mass","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 8 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O (12 g/L)                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"attribute\": \"12 g/L\",\n                        \"amount\": 100,\n                        \"unit\": \"\\u00ef\\u00bf\\u00bdl\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q9","label":"Generated trace row VOSO4 x n H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[8].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source specifies a 100 µL stock addition, with its own parenthesized g/L stock strength. The current 100 G_PER_L is neither that stock strength nor a receiving-medium rate. The API unit is corrupted text, so the literal primary µL row establishes the dimension. Preserve the repaired owners separate stock and dose objects.","source_stage":"Stock receiving volume, not solute mass","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 9 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; VOSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;&lt;I&gt;x&lt;/I&gt;H&lt;sub&gt;2&lt;/sub&gt;O (1 g/L)                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"VOSO4 x n H2O\",\n                        \"compound_id\": 1062,\n                        \"attribute\": \"1 g/L\",\n                        \"amount\": 100,\n                        \"unit\": \"\\u00ef\\u00bf\\u00bdl\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q10","label":"Generated trace row MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[9].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source specifies a 100 µL stock addition, with its own parenthesized g/L stock strength. The current 100 G_PER_L is neither that stock strength nor a receiving-medium rate. The API unit is corrupted text, so the literal primary µL row establishes the dimension. Preserve the repaired owners separate stock and dose objects.","source_stage":"Stock receiving volume, not solute mass","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 10 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O (5.0 g/L in 0.01 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;)  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"attribute\": \"5.0 g/L in 0.01 N H2SO4\",\n                        \"amount\": 100,\n                        \"unit\": \"\\u00ef\\u00bf\\u00bdl\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q11","label":"Generated trace row ZnSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[10].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source specifies a 100 µL stock addition, with its own parenthesized g/L stock strength. The current 100 G_PER_L is neither that stock strength nor a receiving-medium rate. The API unit is corrupted text, so the literal primary µL row establishes the dimension. Preserve the repaired owners separate stock and dose objects.","source_stage":"Stock receiving volume, not solute mass","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O (0.6 g/L in 0.01 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;) &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"attribute\": \"0.6 g/L in 0.01 N H2SO4\",\n                        \"amount\": 100,\n                        \"unit\": \"\\u00ef\\u00bf\\u00bdl\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q12","label":"Generated trace row CuSO4 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[11].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source specifies a 100 µL stock addition, with its own parenthesized g/L stock strength. The current 100 G_PER_L is neither that stock strength nor a receiving-medium rate. The API unit is corrupted text, so the literal primary µL row establishes the dimension. Preserve the repaired owners separate stock and dose objects.","source_stage":"Stock receiving volume, not solute mass","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 12 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;5H&lt;sub&gt;2&lt;/sub&gt;O (0.15 g/L in 0.01 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;) &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"attribute\": \"0.15 g/L in 0.01 N H2SO4\",\n                        \"amount\": 100,\n                        \"unit\": \"\\u00ef\\u00bf\\u00bdl\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q13","label":"Generated trace row CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[12].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source specifies a 100 µL stock addition, with its own parenthesized g/L stock strength. The current 100 G_PER_L is neither that stock strength nor a receiving-medium rate. The API unit is corrupted text, so the literal primary µL row establishes the dimension. Preserve the repaired owners separate stock and dose objects.","source_stage":"Stock receiving volume, not solute mass","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 13 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O (8.0 g/L in 0.01 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;) &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"attribute\": \"8.0 g/L in 0.01 N H2SO4\",\n                        \"amount\": 100,\n                        \"unit\": \"\\u00ef\\u00bf\\u00bdl\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q14","label":"Generated trace row NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[13].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source specifies a 100 µL stock addition, with its own parenthesized g/L stock strength. The current 100 G_PER_L is neither that stock strength nor a receiving-medium rate. The API unit is corrupted text, so the literal primary µL row establishes the dimension. Preserve the repaired owners separate stock and dose objects.","source_stage":"Stock receiving volume, not solute mass","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 14 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O (0.2 g/L in 0.01 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;) &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\": 15,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"attribute\": \"0.2 g/L in 0.01 N H2SO4\",\n                        \"amount\": 100,\n                        \"unit\": \"\\u00ef\\u00bf\\u00bdl\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q15","label":"Maintained N-Z-Case (Wako)","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both maintained owners preserve the primary batch mass divided by its explicit final 1.0 L. This is supported and needs exact attached claim evidence; current source/reference text alone is not an EvidenceItem. The inherited JCM 619 base is authorized by its explicit wrapper.","source_stage":"JCM base or explicit variant final1L, water initial-stage qualified","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 0 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; N-Z-Case (Wako)                                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q16","label":"Maintained Yeast extract (BD-Difco)","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both maintained owners preserve the primary batch mass divided by its explicit final 1.0 L. This is supported and needs exact attached claim evidence; current source/reference text alone is not an EvidenceItem. The inherited JCM 619 base is authorized by its explicit wrapper.","source_stage":"JCM base or explicit variant final1L, water initial-stage qualified","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 1 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Yeast extract (BD-Difco)                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q17","label":"Maintained Soluble starch (BD-Difco)","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both maintained owners preserve the primary batch mass divided by its explicit final 1.0 L. This is supported and needs exact attached claim evidence; current source/reference text alone is not an EvidenceItem. The inherited JCM 619 base is authorized by its explicit wrapper.","source_stage":"JCM base or explicit variant final1L, water initial-stage qualified","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 2 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Soluble starch (BD-Difco)                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q18","label":"Maintained NaCl","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"ingredients[3].concentration","stored":{"value":"16.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The base owner correctly preserves 20 g/L; the selected variant owner correctly preserves the explicit 16.0 g/L override. Both are supported within their own distinct source scopes and must not be merged into one interchangeable identity.","source_stage":"JCM base or explicit variant final1L, water initial-stage qualified","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 3 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q19","label":"Maintained MgCl2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.125","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.125","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both maintained owners preserve the primary batch mass divided by its explicit final 1.0 L. This is supported and needs exact attached claim evidence; current source/reference text alone is not an EvidenceItem. The inherited JCM 619 base is authorized by its explicit wrapper.","source_stage":"JCM base or explicit variant final1L, water initial-stage qualified","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 4 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.125&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q20","label":"Maintained CaCl2 x 2 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.025","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.025","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both maintained owners preserve the primary batch mass divided by its explicit final 1.0 L. This is supported and needs exact attached claim evidence; current source/reference text alone is not an EvidenceItem. The inherited JCM 619 base is authorized by its explicit wrapper.","source_stage":"JCM base or explicit variant final1L, water initial-stage qualified","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 5 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.025&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q21","label":"Maintained FeSO4 x 7 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both maintained owners preserve the primary batch mass divided by its explicit final 1.0 L. This is supported and needs exact attached claim evidence; current source/reference text alone is not an EvidenceItem. The inherited JCM 619 base is authorized by its explicit wrapper.","source_stage":"JCM base or explicit variant final1L, water initial-stage qualified","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 6 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q22","label":"Maintained Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"900.0","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"ingredients[7].concentration","stored":{"value":"900.0","unit":"ML_PER_L"}}],"decision":"evidence_only","rationale":"The 900 mL/L value describes initial solvent per final 1 L; the owner notes correctly retain initial-stage context. It is not 900 mL final volume or a dissolved-solute concentration. Retain that distinction and attach root preparation evidence.","source_stage":"JCM base or explicit variant final1L, water initial-stage qualified","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;900.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q23","label":"Na2MoO4 x 2 H2O stock receiving dose","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[0].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}}],"decision":"evidence_only","rationale":"The exact primary specifies 100 µL of this stock in the final 1.0 L recipe: 100 µL = 0.1 mL, so 0.1 ML_PER_L is supported. Attach evidence at the enclosing root with this full solution path; do not invent nested solution evidence fields.","source_stage":"Receiving dose in final medium","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 8 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O (12 g/L)                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q24","label":"Na2MoO4 x 2 H2O stock composition","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[0].composition[0].concentration","stored":{"value":"12.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[0].composition[0].concentration","stored":{"value":"12.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The primary explicitly reports this stock strength in g/L. Preserve it as stock composition rather than final-medium concentration. The five acidified stock notes correctly preserve 0.01 N H2SO4; no acid mass or molarity conversion is inferred. Vanadyl hydration number remains unspecified where the primary uses x.","source_stage":"Separate stock strength","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 8 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O (12 g/L)                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q25","label":"VOSO4 x n H2O stock receiving dose","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[1].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}}],"decision":"evidence_only","rationale":"The exact primary specifies 100 µL of this stock in the final 1.0 L recipe: 100 µL = 0.1 mL, so 0.1 ML_PER_L is supported. Attach evidence at the enclosing root with this full solution path; do not invent nested solution evidence fields.","source_stage":"Receiving dose in final medium","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 9 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; VOSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;&lt;I&gt;x&lt;/I&gt;H&lt;sub&gt;2&lt;/sub&gt;O (1 g/L)                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q26","label":"VOSO4 x n H2O stock composition","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The primary explicitly reports this stock strength in g/L. Preserve it as stock composition rather than final-medium concentration. The five acidified stock notes correctly preserve 0.01 N H2SO4; no acid mass or molarity conversion is inferred. Vanadyl hydration number remains unspecified where the primary uses x.","source_stage":"Separate stock strength","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 9 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; VOSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;&lt;I&gt;x&lt;/I&gt;H&lt;sub&gt;2&lt;/sub&gt;O (1 g/L)                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q27","label":"MnCl2 x 4 H2O stock receiving dose","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[2].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[2].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}}],"decision":"evidence_only","rationale":"The exact primary specifies 100 µL of this stock in the final 1.0 L recipe: 100 µL = 0.1 mL, so 0.1 ML_PER_L is supported. Attach evidence at the enclosing root with this full solution path; do not invent nested solution evidence fields.","source_stage":"Receiving dose in final medium","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 10 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O (5.0 g/L in 0.01 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;)  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q28","label":"MnCl2 x 4 H2O stock composition","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[2].composition[0].concentration","stored":{"value":"5.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[2].composition[0].concentration","stored":{"value":"5.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The primary explicitly reports this stock strength in g/L. Preserve it as stock composition rather than final-medium concentration. The five acidified stock notes correctly preserve 0.01 N H2SO4; no acid mass or molarity conversion is inferred. Vanadyl hydration number remains unspecified where the primary uses x.","source_stage":"Separate stock strength","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 10 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O (5.0 g/L in 0.01 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;)  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q29","label":"ZnSO4 x 7 H2O stock receiving dose","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[3].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[3].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}}],"decision":"evidence_only","rationale":"The exact primary specifies 100 µL of this stock in the final 1.0 L recipe: 100 µL = 0.1 mL, so 0.1 ML_PER_L is supported. Attach evidence at the enclosing root with this full solution path; do not invent nested solution evidence fields.","source_stage":"Receiving dose in final medium","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O (0.6 g/L in 0.01 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;) &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q30","label":"ZnSO4 x 7 H2O stock composition","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[3].composition[0].concentration","stored":{"value":"0.6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[3].composition[0].concentration","stored":{"value":"0.6","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The primary explicitly reports this stock strength in g/L. Preserve it as stock composition rather than final-medium concentration. The five acidified stock notes correctly preserve 0.01 N H2SO4; no acid mass or molarity conversion is inferred. Vanadyl hydration number remains unspecified where the primary uses x.","source_stage":"Separate stock strength","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O (0.6 g/L in 0.01 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;) &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q31","label":"CuSO4 x 5 H2O stock receiving dose","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[4].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[4].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}}],"decision":"evidence_only","rationale":"The exact primary specifies 100 µL of this stock in the final 1.0 L recipe: 100 µL = 0.1 mL, so 0.1 ML_PER_L is supported. Attach evidence at the enclosing root with this full solution path; do not invent nested solution evidence fields.","source_stage":"Receiving dose in final medium","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 12 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;5H&lt;sub&gt;2&lt;/sub&gt;O (0.15 g/L in 0.01 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;) &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q32","label":"CuSO4 x 5 H2O stock composition","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[4].composition[0].concentration","stored":{"value":"0.15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[4].composition[0].concentration","stored":{"value":"0.15","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The primary explicitly reports this stock strength in g/L. Preserve it as stock composition rather than final-medium concentration. The five acidified stock notes correctly preserve 0.01 N H2SO4; no acid mass or molarity conversion is inferred. Vanadyl hydration number remains unspecified where the primary uses x.","source_stage":"Separate stock strength","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 12 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;5H&lt;sub&gt;2&lt;/sub&gt;O (0.15 g/L in 0.01 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;) &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q33","label":"CoCl2 x 6 H2O stock receiving dose","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[5].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[5].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}}],"decision":"evidence_only","rationale":"The exact primary specifies 100 µL of this stock in the final 1.0 L recipe: 100 µL = 0.1 mL, so 0.1 ML_PER_L is supported. Attach evidence at the enclosing root with this full solution path; do not invent nested solution evidence fields.","source_stage":"Receiving dose in final medium","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 13 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O (8.0 g/L in 0.01 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;) &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q34","label":"CoCl2 x 6 H2O stock composition","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[5].composition[0].concentration","stored":{"value":"8.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[5].composition[0].concentration","stored":{"value":"8.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The primary explicitly reports this stock strength in g/L. Preserve it as stock composition rather than final-medium concentration. The five acidified stock notes correctly preserve 0.01 N H2SO4; no acid mass or molarity conversion is inferred. Vanadyl hydration number remains unspecified where the primary uses x.","source_stage":"Separate stock strength","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 13 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O (8.0 g/L in 0.01 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;) &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q35","label":"NiCl2 x 6 H2O stock receiving dose","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[6].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[6].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}}],"decision":"evidence_only","rationale":"The exact primary specifies 100 µL of this stock in the final 1.0 L recipe: 100 µL = 0.1 mL, so 0.1 ML_PER_L is supported. Attach evidence at the enclosing root with this full solution path; do not invent nested solution evidence fields.","source_stage":"Receiving dose in final medium","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 14 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O (0.2 g/L in 0.01 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;) &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q36","label":"NiCl2 x 6 H2O stock composition","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[6].composition[0].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[6].composition[0].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The primary explicitly reports this stock strength in g/L. Preserve it as stock composition rather than final-medium concentration. The five acidified stock notes correctly preserve 0.01 N H2SO4; no acid mass or molarity conversion is inferred. Vanadyl hydration number remains unspecified where the primary uses x.","source_stage":"Separate stock strength","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 14 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O (0.2 g/L in 0.01 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;) &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; &amp;#181;l  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q37","label":"Generated wrapper instruction","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"preparation_steps","stored":[{"step_number":1,"action":"MIX","description":"Use Medium No. 618 with 16.0 g/L (final) NaCl."}]}],"decision":"evidence_only","rationale":"The exact existing wrapper sentence is supported, but it does not make the stale copied ingredients correct. Retain the wrapper and expand only the explicitly inherited JCM 618 preparation under the 16 g/L override.","source_stage":"Wrapper instruction","sources":[{"evidence_id":"apiJ619","reference":"https://mediadive.dsmz.de/rest/medium/J619","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ619.bin","raw_sha256":"cdfe8fd1ab5b227b0afe1b5fa6081f9933c0ade6b08d8b7d37bfaa410ad10d2a","text_sha256":"04811f69f27d3668ee21d1831afa0b587930ccd6ba7480766cc56343efdd50f8","accessed_at":"2026-10-28T13:11:53.703728Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Use Medium No. 618 with 16.0 g/L (final) NaCl.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]},{"quantity_id":"q38","label":"Maintained preparation sequence","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"preparation_steps","stored":[{"step_number":1,"action":"MIX","description":"Add the base components to 900 ml distilled water and mix thoroughly."},{"step_number":2,"action":"MIX","description":"Add each trace-metal stock solution at 0.1 ml/L in the listed order."},{"step_number":3,"action":"ADJUST_PH","description":"Adjust pH to 7.5, bring the volume to 1.0 L with distilled water, and autoclave."},{"step_number":4,"action":"HEAT","description":"Inoculate into the medium prewarmed to the optimal growth temperature."}]},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"preparation_steps","stored":[{"step_number":1,"action":"MIX","description":"Add the base components to 900 ml distilled water and mix thoroughly."},{"step_number":2,"action":"MIX","description":"Add each trace-metal stock solution at 0.1 ml/L in the listed order."},{"step_number":3,"action":"ADJUST_PH","description":"Adjust pH to 7.5, bring the volume to 1.0 L with distilled water, and autoclave."},{"step_number":4,"action":"HEAT","description":"Inoculate into the medium prewarmed to the optimal growth temperature."}]}],"decision":"evidence_only","rationale":"The owners preserve initial 900 mL, ordered stock additions, pH 7.5 and explicit final 1 L, autoclaving and the unquantified prewarming instruction. No specific incubation temperature is supplied or inferred.","source_stage":"Source preparation","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Mix/order sentence","quote":"Add components to distilled water and mix thoroughly.  Then, add the following solutions in order listed:","quote_basis":"derivative text"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Exact qualitative prewarming comment","quote":"Comment: Inoculate into the medium prewarmed to the optimal growth temperature.","quote_basis":"derivative text"}]},{"quantity_id":"q39","label":"Maintained sterilization","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"sterilization","stored":{"method":"AUTOCLAVE","temperature":{"value":121.0,"unit":"CELSIUS"},"duration":"15 min","notes":"JCM's default instruction is to autoclave media at 121 C for 15 min."}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"sterilization","stored":{"method":"AUTOCLAVE","temperature":{"value":121.0,"unit":"CELSIUS"},"duration":"15 min","notes":"JCM's default instruction is to autoclave media at 121 C for 15 min."}}],"decision":"evidence_only","rationale":"The current JCM page default explicitly supplies 121°C for 15 min unless otherwise stated; the wrapper contains no conflicting override. Retain the owners default attribution.","source_stage":"Default sterilization attribution","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Current page default","quote":"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Current wrapper page default","quote":"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q40","label":"Maintained pH","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"ph_value","stored":7.5},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"ph_value","stored":7.5}],"decision":"evidence_only","rationale":"Both owner pH values agree with the inherited JCM 618 instruction; the generated target lacks ph_value.","source_stage":"Recipe pH","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled water and autoclave.","quote_basis":"derivative text"}]},{"quantity_id":"q41","label":"Liquid physical state","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"physical_state","stored":"LIQUID"},{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"physical_state","stored":"LIQUID"},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"physical_state","stored":"LIQUID"}],"decision":"evidence_only","rationale":"The exact JCM 618 base and 619 wrapper include no agar or Gelrite; liquid classification is consistent with this source scope. The DSM CYS Gelrite formulation is a different source and is not transferred.","source_stage":"Exact JCM source scope","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 0 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; N-Z-Case (Wako)                                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 1 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Yeast extract (BD-Difco)                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 2 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Soluble starch (BD-Difco)                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 3 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 4 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.125&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 5 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.025&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 6 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;900.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml":null,"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:002966.

All current ontology IDs resolve and the captured canonical labels agree; correct MgCl2 hexahydrate, CaCl2 dihydrate, Fe/Zn/Cu/Mn/Co hydrates and variable vanadyl hydration are preserved. The generated nickel anhydrous identity conflicts with the source and repaired owners. MIM preferred cobalt/nickel hexahydrate rows retain their observed REJECTED status despite other mapped label rows; this snapshot status is distinct from OLS supplied-form identity. N-Z-Case brand remains intentionally unresolved; generic yeast/starch terms do not certify BD-Difco grade.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:002966.

Five exact-header reports were read and all 19 historical API snippets and both cited raw hashes match current captures. Prior bulk reports left stock topology unresolved; current primary evidence now supports the repaired owners, while the generated target remains stale. The September repair event and current repair_record implementation agree structurally; no historical execution is replayed. The current conservative merger rejects the parent/variant differences.

## Findings

### f1: The target combines parent and salinity-variant identities

major / open / confirmed; issue key: culturemech-002966-salinity-variant-merge.

Keep JCM 618 and JCM 619 as distinct salinity variants. The primary parent has 20 g/L final NaCl; the explicit YMO722 wrapper changes it to 16 g/L. Current maintained records correctly represent this relationship. The generated target retains both contributors and stale 22.2222 g/L NaCl; regenerate from compatible source-specific formulations after curating remaining evidence.

### f2: Generated concentrations and stock topology are stale

major / open / confirmed; issue key: culturemech-002966-stale-volume-stock-expansion.

Replace the generated stale 900 mL-normalized main rates and seven false 100 G_PER_L rows through maintained-input regeneration, preserving the already-correct owner masses, explicit final 1 L, seven stock strengths and 0.1 mL/L additions. Restore owner water, pH and preparation context. The current importer still accepts these unit-corrupted compound rows and prioritizes API g_l, so a blind import is not a source-validating repair.

### f3: Generated nickel grounding lost the corrected hydrate

major / open / confirmed; issue key: culturemech-002966-stale-nickel-hydrate.

The generated NiCl2·6H2O row still uses CHEBI:34887 nickel dichloride in both asserted slots. Both maintained stock components correctly use CHEBI:53542 nickel chloride hexahydrate. Preserve that repaired supplied-form grounding during source-specific regeneration; do not reinterpret the source amount as anhydrous mass. The magnesium and calcium hydrates already agree with this exact JCM source.

### f4: Supported owner repairs still lack claim-level evidence

minor / open / confirmed; issue key: culturemech-002966-claim-history-provenance.

Attach exact JCM primary snippets to the maintained ingredients and root evidence for the solution doses/preparation. Preserve current repairs and all earlier events byte-for-byte, including the old naive copy event; append only a new verified event. The current repair writer replaces matching curator/action events, so its rerun is not an append-only history operation. Historical API byte matches authenticate content, not earlier execution or the scientifically correct final-volume basis.

## Recommended Actions And Acceptance Checks

### a1

Keep JCM 618 and JCM 619 as distinct salinity variants. The primary parent has 20 g/L final NaCl; the explicit YMO722 wrapper changes it to 16 g/L. Current maintained records correctly represent this relationship. The generated target retains both contributors and stale 22.2222 g/L NaCl; regenerate from compatible source-specific formulations after curating remaining evidence.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Replace the generated stale 900 mL-normalized main rates and seven false 100 G_PER_L rows through maintained-input regeneration, preserving the already-correct owner masses, explicit final 1 L, seven stock strengths and 0.1 mL/L additions. Restore owner water, pH and preparation context. The current importer still accepts these unit-corrupted compound rows and prioritizes API g_l, so a blind import is not a source-validating repair.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The generated NiCl2·6H2O row still uses CHEBI:34887 nickel dichloride in both asserted slots. Both maintained stock components correctly use CHEBI:53542 nickel chloride hexahydrate. Preserve that repaired supplied-form grounding during source-specific regeneration; do not reinterpret the source amount as anhydrous mass. The magnesium and calcium hydrates already agree with this exact JCM source.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

Attach exact JCM primary snippets to the maintained ingredients and root evidence for the solution doses/preparation. Preserve current repairs and all earlier events byte-for-byte, including the old naive copy event; append only a new verified event. The current repair writer replaces matching curator/action events, so its rerun is not an append-only history operation. Historical API byte matches authenticate content, not earlier execution or the scientifically correct final-volume basis.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| jcm618 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618; REVIEW_WORK/batch068/source01-03/jcm618.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| jcm619 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619; REVIEW_WORK/batch068/source01-03/jcm619.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| apiJ618 | https://mediadive.dsmz.de/rest/medium/J618; REVIEW_WORK/batch068/source01-03/apiJ618.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| apiJ619 | https://mediadive.dsmz.de/rest/medium/J619; REVIEW_WORK/batch068/source01-03/apiJ619.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| identityDSM45224 | https://www.dsmz.de/collection/catalogue/details/culture/DSM-45224; REVIEW_WORK/batch068/source01-03/identityDSM45224.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887; REVIEW_WORK/batch068/source01-03/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53542; REVIEW_WORK/batch068/source01-03/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| target | data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| owner-2 | data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| report-19 | reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-20 | reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/JCM_J618_CYS_MEDIUM.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/cys_medium_for_ymo722.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-22 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CYS_Medium_For_YMO722.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cys_medium_for_ymo722.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch068/record02/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch068/record02/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch068/record02/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser keeps only primary compounds and separately preserves referenced stocks. It still prioritizes provider g_l and normalizes bare g/ml/% to per-litre/w-v enums without independently establishing the basis; the action classifier tests temperature before cool. Current behavior is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| writer-repair | scripts/repair_togo_m627_m628_score15.py; repair_record, _base_ingredients, _solutions, _append_event | context_only | Current repair_record preserves the JCM 618/619 salinity distinction, reconstructs explicit stock composition and receiving doses, restores final-volume/preparation context and links related TOGO records. _append_event replaces a matching curator/action event instead of always appending; do not rerun it as an append-only history fix. |
| history-auth | REVIEW_WORK/batch068/record02/historical-source-authentication.json; Complete artifact | supports | All 19 selected historical source objects and both current API response hashes match the original cited bytes; original retrieval events are not replayed. |
| internal-links | REVIEW_WORK/batch068/record02/internal-reference-identity.json; Complete artifact | supports | All exact referenced paths and IDs resolve. Sibling TOGO records are identity links, not additional maintained owners of this selected generated target. |
| chebi28017 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_28017; REVIEW_WORK/batch068/source01-03/chebi28017.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710; REVIEW_WORK/batch068/source01-03/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86345; REVIEW_WORK/batch068/source01-03/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158; REVIEW_WORK/batch068/source01-03/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836; REVIEW_WORK/batch068/source01-03/chebi75836.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213; REVIEW_WORK/batch068/source01-03/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi87020 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_87020; REVIEW_WORK/batch068/source01-03/chebi87020.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86368; REVIEW_WORK/batch068/source01-03/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312; REVIEW_WORK/batch068/source01-03/chebi32312.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31440; REVIEW_WORK/batch068/source01-03/chebi31440.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503; REVIEW_WORK/batch068/source01-03/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| foodon03315426 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http://purl.obolibrary.org/obo/FOODON_03315426; REVIEW_WORK/batch068/source01-03/foodon03315426.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15377; REVIEW_WORK/batch068/source01-03/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Fresh batch068 capture. Exact selected source or existing ontology assertion; identityDSM captures used for scope identity only. |
| quantities | REVIEW_WORK/batch068/record02/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch068/record02/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch068/record02/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch068/record02/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch068/record02/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch068/record02/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch068/record02/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch068/record02/validate-schema.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch068/record02/validate-strict.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch068/record02/validate-terms.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch068/record02/validate-references.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- API J618 reports main rates on a 900 mL normalization and corrupted microliter units; exact current JCM primary final-volume and stock rows take precedence within this source scope, with the discrepancy retained.
- The copy_referenced_compositions writer was not found in the current scripts/src tree by ignored-inclusive rg; its exact historical implementation is not reconstructed from the event.
- No DSM 1108/1108a formulation or stock ambiguity is transferred into this JCM-specific review. The linked TOGO siblings are checked for path/ID identity only.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T132113Z-culturemech-002966-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: CYS MEDIUM FOR YMO722'
started_at: '2026-10-28T13:11:30.762120Z'
finished_at: '2026-10-28T13:21:13.592151Z'
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
summary: 'The maintained JCM 618/619 records already preserve the explicit salinity
  override and stock hierarchy. The generated YMO722 target is stale: its main rates
  use initial-water normalization, its trace rows turn 100 µL doses into 100 G_PER_L,
  and nickel loses the corrected hydrate. Preserve the distinct parent/variant scopes
  and supported owner repairs while adding exact claim evidence and regenerating conservatively.'
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
  - path: data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml
    sha256: 836727957aec0e86b1940306a6c7348a9a7b3b2d1c15bc9a8a6bb652815a560f
    role: target
  - path: data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml
    sha256: 4b70152ab176bf7babc0987463f471a375ab473d9f13ca22184167e87f7a5a4a
    role: context
  - path: data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml
    sha256: 737700abffd6d9b9068fca1c2250af0578b0e5cc3101531244f3265be4ac1920
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
  - path: reports/archive/media_variant_isp_cys_pfennig_methylobacterium_review.md
    sha256: ecbbbc5604eb39c8765827eccc3da4e6421cf3cfa91dfbaff72a146080f4dc77
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/plan.json
    sha256: 1db6b2b69fb7a9a131c95c22d837d6a4c5f10dab810921069496169a06d6f5c2
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/JCM_J618_CYS_MEDIUM.yaml.md
    sha256: 8993e7fdf8a170a6dbe9e0e19ae590bcc5d9d7d1f485fc6210edd2f97f55e68b
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/cys_medium_for_ymo722.yaml.md
    sha256: fa37391c3565eaa9727ae78d00ddf0cd239037459b746fb4a9780a288c42eed5
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CYS_Medium_For_YMO722.md
    sha256: 484f7915ae28da16262bf647f901608845144a6787902c817684517c92302138
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.md
    sha256: ae599210752c3382607a62f6ea72d5accb180fe27817eeed7d2338561bfbc891
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cys_medium_for_ymo722.md
    sha256: dbd0016f2f423bc5d24438daf5b44422f13280a21dde5002072ec9058ce3b783
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
    role: context
  - path: scripts/repair_togo_m627_m628_score15.py
    sha256: ba292a1e8404ad3e69d82ce9af1115a2bcecf5c77209ed84b7b35c530553b7e5
    role: context
  - path: scripts/validate_media_variant_links.py
    sha256: d18ef71320a0c50abe085e151d0d0d4d963007d1e1c9afbefab97581a983e31e
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
  selection: Authoritative batch068 index 02
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:002966
targets:
- target_id: CultureMech:002966
  path: data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml
  label: cys_medium_for_ymo722
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml
    role: maintained normalized contributor
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:002966
  command: just validate-schema data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml
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
  - CultureMech:002966
  command: just validate-strict data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml
    --out REVIEW_WORK/batch068/record02/strict.tsv --workers 1 --quiet
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
  - CultureMech:002966
  command: just validate-terms data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml
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
  - CultureMech:002966
  command: just validate-references data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: jcm618
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618
  accessed_at: '2026-10-28T13:11:53.281925Z'
  locator: REVIEW_WORK/batch068/source01-03/jcm618.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414
- evidence_id: jcm619
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619
  accessed_at: '2026-10-28T13:11:53.421663Z'
  locator: REVIEW_WORK/batch068/source01-03/jcm619.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641
- evidence_id: apiJ618
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J618
  accessed_at: '2026-10-28T13:11:53.300880Z'
  locator: REVIEW_WORK/batch068/source01-03/apiJ618.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9
- evidence_id: apiJ619
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J619
  accessed_at: '2026-10-28T13:11:53.703728Z'
  locator: REVIEW_WORK/batch068/source01-03/apiJ619.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: cdfe8fd1ab5b227b0afe1b5fa6081f9933c0ade6b08d8b7d37bfaa410ad10d2a
- evidence_id: identityDSM45224
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-45224
  accessed_at: '2026-10-28T13:11:55.299899Z'
  locator: REVIEW_WORK/batch068/source01-03/identityDSM45224.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 12702ce24f16ba6a0744f5552d0ffa3e205cb0dc09fc3b4f35c3cfdacf4aec60
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887
  accessed_at: '2026-10-28T13:11:56.609061Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi34887.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: a43b8268f70ae50c4cfbc53e12bbd195618c521619cfab8f71d3704b338af95b
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53542
  accessed_at: '2026-10-28T13:11:56.960579Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi53542.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 1e444345efd33c02d5050deadd66637cc6dae004c55e6962c62abd172291e526
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:21:13.427912Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 836727957aec0e86b1940306a6c7348a9a7b3b2d1c15bc9a8a6bb652815a560f
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:21:13.428186Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 4b70152ab176bf7babc0987463f471a375ab473d9f13ca22184167e87f7a5a4a
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T13:21:13.428273Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T13:21:13.428721Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T13:21:13.428765Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T13:21:13.428801Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:21:13.428873Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: 737700abffd6d9b9068fca1c2250af0578b0e5cc3101531244f3265be4ac1920
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T13:21:13.428918Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 1db6b2b69fb7a9a131c95c22d837d6a4c5f10dab810921069496169a06d6f5c2
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/JCM_J618_CYS_MEDIUM.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T13:21:13.435579Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 8993e7fdf8a170a6dbe9e0e19ae590bcc5d9d7d1f485fc6210edd2f97f55e68b
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/cys_medium_for_ymo722.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T13:21:13.435726Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: fa37391c3565eaa9727ae78d00ddf0cd239037459b746fb4a9780a288c42eed5
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CYS_Medium_For_YMO722.md
  locator: Complete report
  accessed_at: '2026-10-28T13:21:13.435776Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 484f7915ae28da16262bf647f901608845144a6787902c817684517c92302138
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T13:21:13.435928Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: ae599210752c3382607a62f6ea72d5accb180fe27817eeed7d2338561bfbc891
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cys_medium_for_ymo722.md
  locator: Complete report
  accessed_at: '2026-10-28T13:21:13.435977Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: dbd0016f2f423bc5d24438daf5b44422f13280a21dde5002072ec9058ce3b783
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch068/record02/historical-reading.json
  accessed_at: '2026-10-28T13:21:13.436014Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 13cdda4ccddb818c7be24fe565581474526d6a875c217e738a94c0bab2f07d95
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch068/record02/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T13:21:13.436268Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 0d075a9c0538bcd83a691eb986c2610d1b40c32eb6b63fd8613c919a51d1c0aa
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch068/record02/complete-document-reader.json
  accessed_at: '2026-10-28T13:21:13.436519Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 8c8e9458720b30ce42303702f842683372464c2c4d9191e4cc7b0a36cd481cf4
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T13:21:13.436741Z'
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
  accessed_at: '2026-10-28T13:21:13.436888Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer-repair
  kind: record_content
  reference: scripts/repair_togo_m627_m628_score15.py
  locator: repair_record, _base_ingredients, _solutions, _append_event
  accessed_at: '2026-10-28T13:21:13.436958Z'
  support: context_only
  summary: Current repair_record preserves the JCM 618/619 salinity distinction, reconstructs
    explicit stock composition and receiving doses, restores final-volume/preparation
    context and links related TOGO records. _append_event replaces a matching curator/action
    event instead of always appending; do not rerun it as an append-only history fix.
  snapshot_sha256: ba292a1e8404ad3e69d82ce9af1115a2bcecf5c77209ed84b7b35c530553b7e5
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch068/record02/historical-source-authentication.json
  locator: Complete artifact
  accessed_at: '2026-10-28T13:21:13.437002Z'
  support: supports
  summary: All 19 selected historical source objects and both current API response
    hashes match the original cited bytes; original retrieval events are not replayed.
  snapshot_sha256: e0250165e5332ad08c786c3d19077d55fdb9a999e52b5e989d71420d762d3b8c
- evidence_id: internal-links
  kind: record_content
  reference: REVIEW_WORK/batch068/record02/internal-reference-identity.json
  locator: Complete artifact
  accessed_at: '2026-10-28T13:21:13.437324Z'
  support: supports
  summary: All exact referenced paths and IDs resolve. Sibling TOGO records are identity
    links, not additional maintained owners of this selected generated target.
  snapshot_sha256: 8a12edf3c9ef5cd717dc41d2850b902ec34fca67cf40d3571343105727ca27ba
- evidence_id: chebi28017
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_28017
  accessed_at: '2026-10-28T13:11:56.351368Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi28017.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 97d3317b987b817f798f2968ae77d2d550be0f98d072c054f7effa98c58f9d1a
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710
  accessed_at: '2026-10-28T13:11:55.982175Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi26710.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: b145f4ff9b90ebb993ff576d9ab35a6c10b7c42a3b99e18feffcc8d75c0e1e50
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86345
  accessed_at: '2026-10-28T13:11:57.870221Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi86345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 015a33a158257cc5cba8a8e62de382053399be060366af5d95074883bb22b86e
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158
  accessed_at: '2026-10-28T13:11:58.560452Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi86158.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: df8f702eb5b9d3e50209bfa2b0c4b6f1db30c116e56a58e348cbd4bf3bc0ebc1
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836
  accessed_at: '2026-10-28T13:11:57.905294Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi75836.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: e12b865122aab78645385260e1e83ff28f3c45365cb67c9181166628f68974b3
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213
  accessed_at: '2026-10-28T13:11:57.255273Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi75213.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 0271a149a298ff837ad8f690ce8cb0acf111f5d25c5efaf6fa828401ab951d56
- evidence_id: chebi87020
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_87020
  accessed_at: '2026-10-28T13:11:58.458997Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi87020.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: af4736e5e35f6007e25b37cc600bbad18a073377d92fc942ae3703c8e208f957
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86368
  accessed_at: '2026-10-28T13:11:58.198058Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi86368.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 2bb4588e6734285b5536bdac78701f9800fdb8d17236d12cf5a1c30490f1614d
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312
  accessed_at: '2026-10-28T13:11:56.238355Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi32312.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 6bf1390236046f1cb7b21e2fc324fccba6e6eac2bc4e519f12d998f0edce671b
- evidence_id: chebi31440
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31440
  accessed_at: '2026-10-28T13:11:55.965879Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi31440.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 453e496e1e59b82bb42cd3252d410b9dc77d0c11e49f3da70496a82978e80505
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503
  accessed_at: '2026-10-28T13:11:56.849008Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi53503.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 31dc996638b0cc1341ed24fcb38ec344af726c99d376ac94e952210fcb9ed583
- evidence_id: foodon03315426
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http://purl.obolibrary.org/obo/FOODON_03315426
  accessed_at: '2026-10-28T13:11:58.495368Z'
  locator: REVIEW_WORK/batch068/source01-03/foodon03315426.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 73e813d7b7d5a59707f5f316566e11b00d2bb1d74b01d54f9e419edd632da9e0
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15377
  accessed_at: '2026-10-28T13:11:54.337160Z'
  locator: REVIEW_WORK/batch068/source01-03/chebi15377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Fresh batch068 capture. Exact selected source or existing ontology assertion;
    identityDSM captures used for scope identity only.
  snapshot_sha256: 42561686e12ba0831d99216248ea8c0b3338b461b0b77dd988f3096ad8678e59
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch068/record02/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:21:13.588548Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 4dfdcc34a330887a4c10a2a6ec2f428797897e3be9efaa8f0f15f96adbc5501a
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch068/record02/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:21:13.588736Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: d8ae1b5f52867e0ad71f76b89884503b1fb0eabde6389c5b046832a9f50107d8
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch068/record02/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:21:13.589061Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: f7d365d046556faec7b8f162282a95241a03655e87ee40a5e679c1d17660fe9a
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch068/record02/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:21:13.589235Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 42bbe3eb9a500b49282132c5d770f8b8f7e45729ca7a19f767c7d2c52c19e453
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch068/record02/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:21:13.589392Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: ffbb017c829ee64e982ffa835fd156829de6ab5917ba86faef9db48d0a39f682
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch068/record02/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:21:13.589466Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: cd16bfdacd82b24c895585338708b0d360335f1058b9db32612d3442fd2d61a8
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch068/record02/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:21:13.589542Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch068/record02/validate-schema.json
  accessed_at: '2026-10-28T13:11:31.810279Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 15538a16dd782f5032d9677f03eb1958c40fd3dfe779cfb8c1e80a4ce2d39bda
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch068/record02/validate-strict.json
  accessed_at: '2026-10-28T13:11:32.760970Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 6ff757adba10b0c0e0a6e379353286177aba459559ee574f3ad74b87317c73ad
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch068/record02/validate-terms.json
  accessed_at: '2026-10-28T13:11:33.802959Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 0ea6986674080a96be1cd86014537661ba7ee3c6e15d1237eabb4f0b205c59ab
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch068/record02/validate-references.json
  accessed_at: '2026-10-28T13:11:34.471387Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: b3d514fba82b8860e8fa01c46321231f052ca2727516e5a608bfbc4f66468a8b
assessments:
- assessment_id: identity
  area: identity
  topic: Source and maintained repair boundaries
  outcome: concern
  summary: Exact JCM 619 wrapper identity and environmental YMO722 catalog identity
    are resolved. The parent and variant are distinct; no strain-growth assertion
    is copied from a catalogue.
  target_ids:
  - CultureMech:002966
  evidence_ids:
  - jcm619
  - jcm618
  - identityDSM45224
  - internal-links
- assessment_id: representation
  area: representation
  topic: Current repair credit
  outcome: supported
  summary: The two maintained owners correctly preserve distinct NaCl overrides, main
    masses, stock strengths/doses, pH, initial water and preparation. This credit
    does not certify missing attached evidence or the stale generated record.
  target_ids:
  - CultureMech:002966
  evidence_ids:
  - owner
  - owner-2
  - writer-repair
  - jcm618
  - jcm619
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 58 current concentration fields are covered by 41 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:002966
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b068-quantity-inventory-v1","target":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","quantity_field_count":58,"decisions":[{"quantity_id":"q1","label":"Generated
    N-Z-Case","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3.33333","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    generated value reproduces the API normalization to the initial 900 mL. The primary
    explicitly makes the completed medium to 1.0 L, so the current final-medium rate
    is wrong. Credit the provider digits only on their declared initial-volume basis;
    preserve the source mass and supported corrected owner rate.","source_stage":"Generated
    stale main-medium concentration","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 0 (zero-based)","quote":"<TR><TD WIDTH=75%> N-Z-Case (Wako)                                          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"N-Z-Case\",\n                        \"compound_id\":
    1829,\n                        \"attribute\": \"Wako\",\n                        \"amount\":
    3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    3.33333,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q2","label":"Generated Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2.22222","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    generated value reproduces the API normalization to the initial 900 mL. The primary
    explicitly makes the completed medium to 1.0 L, so the current final-medium rate
    is wrong. Credit the provider digits only on their declared initial-volume basis;
    preserve the source mass and supported corrected owner rate.","source_stage":"Generated
    stale main-medium concentration","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 1 (zero-based)","quote":"<TR><TD WIDTH=75%> Yeast extract (BD-Difco)                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\":
    2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    2.22222,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q3","label":"Generated Starch","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1.11111","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    generated value reproduces the API normalization to the initial 900 mL. The primary
    explicitly makes the completed medium to 1.0 L, so the current final-medium rate
    is wrong. Credit the provider digits only on their declared initial-volume basis;
    preserve the source mass and supported corrected owner rate.","source_stage":"Generated
    stale main-medium concentration","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 2 (zero-based)","quote":"<TR><TD WIDTH=75%> Soluble starch (BD-Difco)                               </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Starch\",\n                        \"compound_id\":
    199,\n                        \"attribute\": \"BD-Difco, soluble\",\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1.11111,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q4","label":"Generated NaCl","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[3].concentration","stored":{"value":"22.2222","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    generated 22.2222 g/L derives from the parent API 20 g normalized to 900 mL, while
    the exact JCM 619 wrapper explicitly requires 16.0 g/L final NaCl. Neither the
    parent 20 g/L nor its API initial-volume normalization may replace the selected
    variant override.","source_stage":"Generated stale main-medium concentration","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 3 (zero-based)","quote":"<TR><TD WIDTH=75%> NaCl                                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 20,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 22.2222,\n                        \"mmol_l\":
    380.257,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q5","label":"Generated MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.138889","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    generated value reproduces the API normalization to the initial 900 mL. The primary
    explicitly makes the completed medium to 1.0 L, so the current final-medium rate
    is wrong. Credit the provider digits only on their declared initial-volume basis;
    preserve the source mass and supported corrected owner rate.","source_stage":"Generated
    stale main-medium concentration","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 4 (zero-based)","quote":"<TR><TD WIDTH=75%> MgCl<sub>2</sub>&#183;6H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.125&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.125,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.138889,\n                        \"mmol_l\":
    0.683162,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q6","label":"Generated CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.0277778","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    generated value reproduces the API normalization to the initial 900 mL. The primary
    explicitly makes the completed medium to 1.0 L, so the current final-medium rate
    is wrong. Credit the provider digits only on their declared initial-volume basis;
    preserve the source mass and supported corrected owner rate.","source_stage":"Generated
    stale main-medium concentration","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 5 (zero-based)","quote":"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.025&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.025,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0277778,\n                        \"mmol_l\":
    0.188945,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q7","label":"Generated FeSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.0111111","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    generated value reproduces the API normalization to the initial 900 mL. The primary
    explicitly makes the completed medium to 1.0 L, so the current final-medium rate
    is wrong. Credit the provider digits only on their declared initial-volume basis;
    preserve the source mass and supported corrected owner rate.","source_stage":"Generated
    stale main-medium concentration","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 6 (zero-based)","quote":"<TR><TD WIDTH=75%> FeSO<sub>4</sub>&#183;7H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0111111,\n                        \"mmol_l\":
    0.0399659,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q8","label":"Generated trace row Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[7].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source specifies a 100 µL stock addition, with its own parenthesized g/L stock
    strength. The current 100 G_PER_L is neither that stock strength nor a receiving-medium
    rate. The API unit is corrupted text, so the literal primary µL row establishes
    the dimension. Preserve the repaired owners separate stock and dose objects.","source_stage":"Stock
    receiving volume, not solute mass","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 8 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O
    (12 g/L)                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"attribute\": \"12 g/L\",\n                        \"amount\":
    100,\n                        \"unit\": \"\\u00ef\\u00bf\\u00bdl\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q9","label":"Generated trace row VOSO4 x n H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[8].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source specifies a 100 µL stock addition, with its own parenthesized g/L stock
    strength. The current 100 G_PER_L is neither that stock strength nor a receiving-medium
    rate. The API unit is corrupted text, so the literal primary µL row establishes
    the dimension. Preserve the repaired owners separate stock and dose objects.","source_stage":"Stock
    receiving volume, not solute mass","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 9 (zero-based)","quote":"<TR><TD WIDTH=75%> VOSO<sub>4</sub>&#183;<I>x</I>H<sub>2</sub>O
    (1 g/L)                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"VOSO4 x n H2O\",\n                        \"compound_id\":
    1062,\n                        \"attribute\": \"1 g/L\",\n                        \"amount\":
    100,\n                        \"unit\": \"\\u00ef\\u00bf\\u00bdl\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q10","label":"Generated trace row MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[9].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source specifies a 100 µL stock addition, with its own parenthesized g/L stock
    strength. The current 100 G_PER_L is neither that stock strength nor a receiving-medium
    rate. The API unit is corrupted text, so the literal primary µL row establishes
    the dimension. Preserve the repaired owners separate stock and dose objects.","source_stage":"Stock
    receiving volume, not solute mass","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 10 (zero-based)","quote":"<TR><TD WIDTH=75%> MnCl<sub>2</sub>&#183;4H<sub>2</sub>O
    (5.0 g/L in 0.01 N H<sub>2</sub>SO<sub>4</sub>)  </TD><TD WIDTH=15% ALIGN=RIGHT><font
    size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%
    ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"attribute\": \"5.0 g/L in 0.01 N H2SO4\",\n                        \"amount\":
    100,\n                        \"unit\": \"\\u00ef\\u00bf\\u00bdl\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q11","label":"Generated trace row ZnSO4 x 7 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[10].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source specifies a 100 µL stock addition, with its own parenthesized g/L stock
    strength. The current 100 G_PER_L is neither that stock strength nor a receiving-medium
    rate. The API unit is corrupted text, so the literal primary µL row establishes
    the dimension. Preserve the repaired owners separate stock and dose objects.","source_stage":"Stock
    receiving volume, not solute mass","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> ZnSO<sub>4</sub>&#183;7H<sub>2</sub>O
    (0.6 g/L in 0.01 N H<sub>2</sub>SO<sub>4</sub>) </TD><TD WIDTH=15% ALIGN=RIGHT><font
    size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%
    ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":
    35,\n                        \"attribute\": \"0.6 g/L in 0.01 N H2SO4\",\n                        \"amount\":
    100,\n                        \"unit\": \"\\u00ef\\u00bf\\u00bdl\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q12","label":"Generated trace row CuSO4 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[11].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source specifies a 100 µL stock addition, with its own parenthesized g/L stock
    strength. The current 100 G_PER_L is neither that stock strength nor a receiving-medium
    rate. The API unit is corrupted text, so the literal primary µL row establishes
    the dimension. Preserve the repaired owners separate stock and dose objects.","source_stage":"Stock
    receiving volume, not solute mass","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 12 (zero-based)","quote":"<TR><TD WIDTH=75%> CuSO<sub>4</sub>&#183;5H<sub>2</sub>O
    (0.15 g/L in 0.01 N H<sub>2</sub>SO<sub>4</sub>) </TD><TD WIDTH=15% ALIGN=RIGHT><font
    size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%
    ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\":
    121,\n                        \"attribute\": \"0.15 g/L in 0.01 N H2SO4\",\n                        \"amount\":
    100,\n                        \"unit\": \"\\u00ef\\u00bf\\u00bdl\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q13","label":"Generated trace row CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[12].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source specifies a 100 µL stock addition, with its own parenthesized g/L stock
    strength. The current 100 G_PER_L is neither that stock strength nor a receiving-medium
    rate. The API unit is corrupted text, so the literal primary µL row establishes
    the dimension. Preserve the repaired owners separate stock and dose objects.","source_stage":"Stock
    receiving volume, not solute mass","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 13 (zero-based)","quote":"<TR><TD WIDTH=75%> CoCl<sub>2</sub>&#183;6H<sub>2</sub>O
    (8.0 g/L in 0.01 N H<sub>2</sub>SO<sub>4</sub>) </TD><TD WIDTH=15% ALIGN=RIGHT><font
    size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%
    ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"attribute\": \"8.0 g/L in 0.01 N H2SO4\",\n                        \"amount\":
    100,\n                        \"unit\": \"\\u00ef\\u00bf\\u00bdl\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q14","label":"Generated trace row NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"ingredients[13].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source specifies a 100 µL stock addition, with its own parenthesized g/L stock
    strength. The current 100 G_PER_L is neither that stock strength nor a receiving-medium
    rate. The API unit is corrupted text, so the literal primary µL row establishes
    the dimension. Preserve the repaired owners separate stock and dose objects.","source_stage":"Stock
    receiving volume, not solute mass","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 14 (zero-based)","quote":"<TR><TD WIDTH=75%> NiCl<sub>2</sub>&#183;6H<sub>2</sub>O
    (0.2 g/L in 0.01 N H<sub>2</sub>SO<sub>4</sub>) </TD><TD WIDTH=15% ALIGN=RIGHT><font
    size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%
    ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"apiJ618","reference":"https://mediadive.dsmz.de/rest/medium/J618","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ618.bin","raw_sha256":"bde347fe857bd5fca7999f045fab6db74090c21e0e4b3a1bcd9b8cfd9cfaecd9","text_sha256":"946e7b1ed374cb4ab02785c1c688e0903bb146efb991cd8fbbaec34975daa901","accessed_at":"2026-10-28T13:11:53.300880Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"attribute\": \"0.2 g/L in 0.01 N H2SO4\",\n                        \"amount\":
    100,\n                        \"unit\": \"\\u00ef\\u00bf\\u00bdl\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q15","label":"Maintained N-Z-Case (Wako)","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both
    maintained owners preserve the primary batch mass divided by its explicit final
    1.0 L. This is supported and needs exact attached claim evidence; current source/reference
    text alone is not an EvidenceItem. The inherited JCM 619 base is authorized by
    its explicit wrapper.","source_stage":"JCM base or explicit variant final1L, water
    initial-stage qualified","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 0 (zero-based)","quote":"<TR><TD WIDTH=75%> N-Z-Case (Wako)                                          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q16","label":"Maintained Yeast extract (BD-Difco)","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both
    maintained owners preserve the primary batch mass divided by its explicit final
    1.0 L. This is supported and needs exact attached claim evidence; current source/reference
    text alone is not an EvidenceItem. The inherited JCM 619 base is authorized by
    its explicit wrapper.","source_stage":"JCM base or explicit variant final1L, water
    initial-stage qualified","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 1 (zero-based)","quote":"<TR><TD WIDTH=75%> Yeast extract (BD-Difco)                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q17","label":"Maintained Soluble starch (BD-Difco)","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both
    maintained owners preserve the primary batch mass divided by its explicit final
    1.0 L. This is supported and needs exact attached claim evidence; current source/reference
    text alone is not an EvidenceItem. The inherited JCM 619 base is authorized by
    its explicit wrapper.","source_stage":"JCM base or explicit variant final1L, water
    initial-stage qualified","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 2 (zero-based)","quote":"<TR><TD WIDTH=75%> Soluble starch (BD-Difco)                               </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q18","label":"Maintained NaCl","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"ingredients[3].concentration","stored":{"value":"16.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    base owner correctly preserves 20 g/L; the selected variant owner correctly preserves
    the explicit 16.0 g/L override. Both are supported within their own distinct source
    scopes and must not be merged into one interchangeable identity.","source_stage":"JCM
    base or explicit variant final1L, water initial-stage qualified","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 3 (zero-based)","quote":"<TR><TD WIDTH=75%> NaCl                                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q19","label":"Maintained MgCl2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.125","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.125","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both
    maintained owners preserve the primary batch mass divided by its explicit final
    1.0 L. This is supported and needs exact attached claim evidence; current source/reference
    text alone is not an EvidenceItem. The inherited JCM 619 base is authorized by
    its explicit wrapper.","source_stage":"JCM base or explicit variant final1L, water
    initial-stage qualified","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 4 (zero-based)","quote":"<TR><TD WIDTH=75%> MgCl<sub>2</sub>&#183;6H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.125&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q20","label":"Maintained CaCl2 x 2 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.025","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.025","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both
    maintained owners preserve the primary batch mass divided by its explicit final
    1.0 L. This is supported and needs exact attached claim evidence; current source/reference
    text alone is not an EvidenceItem. The inherited JCM 619 base is authorized by
    its explicit wrapper.","source_stage":"JCM base or explicit variant final1L, water
    initial-stage qualified","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 5 (zero-based)","quote":"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.025&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q21","label":"Maintained FeSO4 x 7 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both
    maintained owners preserve the primary batch mass divided by its explicit final
    1.0 L. This is supported and needs exact attached claim evidence; current source/reference
    text alone is not an EvidenceItem. The inherited JCM 619 base is authorized by
    its explicit wrapper.","source_stage":"JCM base or explicit variant final1L, water
    initial-stage qualified","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 6 (zero-based)","quote":"<TR><TD WIDTH=75%> FeSO<sub>4</sub>&#183;7H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q22","label":"Maintained Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"900.0","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"ingredients[7].concentration","stored":{"value":"900.0","unit":"ML_PER_L"}}],"decision":"evidence_only","rationale":"The
    900 mL/L value describes initial solvent per final 1 L; the owner notes correctly
    retain initial-stage context. It is not 900 mL final volume or a dissolved-solute
    concentration. Retain that distinction and attach root preparation evidence.","source_stage":"JCM
    base or explicit variant final1L, water initial-stage qualified","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;900.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q23","label":"Na2MoO4 x 2 H2O stock receiving dose","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[0].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact primary specifies 100 µL of this stock in the final 1.0 L recipe: 100 µL
    = 0.1 mL, so 0.1 ML_PER_L is supported. Attach evidence at the enclosing root
    with this full solution path; do not invent nested solution evidence fields.","source_stage":"Receiving
    dose in final medium","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 8 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O
    (12 g/L)                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q24","label":"Na2MoO4 x 2 H2O stock composition","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[0].composition[0].concentration","stored":{"value":"12.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[0].composition[0].concentration","stored":{"value":"12.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    primary explicitly reports this stock strength in g/L. Preserve it as stock composition
    rather than final-medium concentration. The five acidified stock notes correctly
    preserve 0.01 N H2SO4; no acid mass or molarity conversion is inferred. Vanadyl
    hydration number remains unspecified where the primary uses x.","source_stage":"Separate
    stock strength","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 8 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O
    (12 g/L)                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q25","label":"VOSO4 x n H2O stock receiving dose","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[1].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact primary specifies 100 µL of this stock in the final 1.0 L recipe: 100 µL
    = 0.1 mL, so 0.1 ML_PER_L is supported. Attach evidence at the enclosing root
    with this full solution path; do not invent nested solution evidence fields.","source_stage":"Receiving
    dose in final medium","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 9 (zero-based)","quote":"<TR><TD WIDTH=75%> VOSO<sub>4</sub>&#183;<I>x</I>H<sub>2</sub>O
    (1 g/L)                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q26","label":"VOSO4 x n H2O stock composition","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    primary explicitly reports this stock strength in g/L. Preserve it as stock composition
    rather than final-medium concentration. The five acidified stock notes correctly
    preserve 0.01 N H2SO4; no acid mass or molarity conversion is inferred. Vanadyl
    hydration number remains unspecified where the primary uses x.","source_stage":"Separate
    stock strength","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 9 (zero-based)","quote":"<TR><TD WIDTH=75%> VOSO<sub>4</sub>&#183;<I>x</I>H<sub>2</sub>O
    (1 g/L)                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q27","label":"MnCl2 x 4 H2O stock receiving dose","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[2].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[2].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact primary specifies 100 µL of this stock in the final 1.0 L recipe: 100 µL
    = 0.1 mL, so 0.1 ML_PER_L is supported. Attach evidence at the enclosing root
    with this full solution path; do not invent nested solution evidence fields.","source_stage":"Receiving
    dose in final medium","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 10 (zero-based)","quote":"<TR><TD WIDTH=75%> MnCl<sub>2</sub>&#183;4H<sub>2</sub>O
    (5.0 g/L in 0.01 N H<sub>2</sub>SO<sub>4</sub>)  </TD><TD WIDTH=15% ALIGN=RIGHT><font
    size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%
    ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q28","label":"MnCl2 x 4 H2O stock composition","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[2].composition[0].concentration","stored":{"value":"5.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[2].composition[0].concentration","stored":{"value":"5.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    primary explicitly reports this stock strength in g/L. Preserve it as stock composition
    rather than final-medium concentration. The five acidified stock notes correctly
    preserve 0.01 N H2SO4; no acid mass or molarity conversion is inferred. Vanadyl
    hydration number remains unspecified where the primary uses x.","source_stage":"Separate
    stock strength","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 10 (zero-based)","quote":"<TR><TD WIDTH=75%> MnCl<sub>2</sub>&#183;4H<sub>2</sub>O
    (5.0 g/L in 0.01 N H<sub>2</sub>SO<sub>4</sub>)  </TD><TD WIDTH=15% ALIGN=RIGHT><font
    size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%
    ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q29","label":"ZnSO4 x 7 H2O stock receiving dose","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[3].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[3].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact primary specifies 100 µL of this stock in the final 1.0 L recipe: 100 µL
    = 0.1 mL, so 0.1 ML_PER_L is supported. Attach evidence at the enclosing root
    with this full solution path; do not invent nested solution evidence fields.","source_stage":"Receiving
    dose in final medium","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> ZnSO<sub>4</sub>&#183;7H<sub>2</sub>O
    (0.6 g/L in 0.01 N H<sub>2</sub>SO<sub>4</sub>) </TD><TD WIDTH=15% ALIGN=RIGHT><font
    size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%
    ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q30","label":"ZnSO4 x 7 H2O stock composition","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[3].composition[0].concentration","stored":{"value":"0.6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[3].composition[0].concentration","stored":{"value":"0.6","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    primary explicitly reports this stock strength in g/L. Preserve it as stock composition
    rather than final-medium concentration. The five acidified stock notes correctly
    preserve 0.01 N H2SO4; no acid mass or molarity conversion is inferred. Vanadyl
    hydration number remains unspecified where the primary uses x.","source_stage":"Separate
    stock strength","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> ZnSO<sub>4</sub>&#183;7H<sub>2</sub>O
    (0.6 g/L in 0.01 N H<sub>2</sub>SO<sub>4</sub>) </TD><TD WIDTH=15% ALIGN=RIGHT><font
    size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%
    ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q31","label":"CuSO4 x 5 H2O stock receiving dose","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[4].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[4].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact primary specifies 100 µL of this stock in the final 1.0 L recipe: 100 µL
    = 0.1 mL, so 0.1 ML_PER_L is supported. Attach evidence at the enclosing root
    with this full solution path; do not invent nested solution evidence fields.","source_stage":"Receiving
    dose in final medium","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 12 (zero-based)","quote":"<TR><TD WIDTH=75%> CuSO<sub>4</sub>&#183;5H<sub>2</sub>O
    (0.15 g/L in 0.01 N H<sub>2</sub>SO<sub>4</sub>) </TD><TD WIDTH=15% ALIGN=RIGHT><font
    size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%
    ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q32","label":"CuSO4 x 5 H2O stock composition","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[4].composition[0].concentration","stored":{"value":"0.15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[4].composition[0].concentration","stored":{"value":"0.15","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    primary explicitly reports this stock strength in g/L. Preserve it as stock composition
    rather than final-medium concentration. The five acidified stock notes correctly
    preserve 0.01 N H2SO4; no acid mass or molarity conversion is inferred. Vanadyl
    hydration number remains unspecified where the primary uses x.","source_stage":"Separate
    stock strength","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 12 (zero-based)","quote":"<TR><TD WIDTH=75%> CuSO<sub>4</sub>&#183;5H<sub>2</sub>O
    (0.15 g/L in 0.01 N H<sub>2</sub>SO<sub>4</sub>) </TD><TD WIDTH=15% ALIGN=RIGHT><font
    size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%
    ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q33","label":"CoCl2 x 6 H2O stock receiving dose","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[5].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[5].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact primary specifies 100 µL of this stock in the final 1.0 L recipe: 100 µL
    = 0.1 mL, so 0.1 ML_PER_L is supported. Attach evidence at the enclosing root
    with this full solution path; do not invent nested solution evidence fields.","source_stage":"Receiving
    dose in final medium","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 13 (zero-based)","quote":"<TR><TD WIDTH=75%> CoCl<sub>2</sub>&#183;6H<sub>2</sub>O
    (8.0 g/L in 0.01 N H<sub>2</sub>SO<sub>4</sub>) </TD><TD WIDTH=15% ALIGN=RIGHT><font
    size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%
    ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q34","label":"CoCl2 x 6 H2O stock composition","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[5].composition[0].concentration","stored":{"value":"8.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[5].composition[0].concentration","stored":{"value":"8.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    primary explicitly reports this stock strength in g/L. Preserve it as stock composition
    rather than final-medium concentration. The five acidified stock notes correctly
    preserve 0.01 N H2SO4; no acid mass or molarity conversion is inferred. Vanadyl
    hydration number remains unspecified where the primary uses x.","source_stage":"Separate
    stock strength","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 13 (zero-based)","quote":"<TR><TD WIDTH=75%> CoCl<sub>2</sub>&#183;6H<sub>2</sub>O
    (8.0 g/L in 0.01 N H<sub>2</sub>SO<sub>4</sub>) </TD><TD WIDTH=15% ALIGN=RIGHT><font
    size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%
    ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q35","label":"NiCl2 x 6 H2O stock receiving dose","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[6].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[6].concentration","stored":{"value":"0.1","unit":"ML_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact primary specifies 100 µL of this stock in the final 1.0 L recipe: 100 µL
    = 0.1 mL, so 0.1 ML_PER_L is supported. Attach evidence at the enclosing root
    with this full solution path; do not invent nested solution evidence fields.","source_stage":"Receiving
    dose in final medium","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 14 (zero-based)","quote":"<TR><TD WIDTH=75%> NiCl<sub>2</sub>&#183;6H<sub>2</sub>O
    (0.2 g/L in 0.01 N H<sub>2</sub>SO<sub>4</sub>) </TD><TD WIDTH=15% ALIGN=RIGHT><font
    size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%
    ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q36","label":"NiCl2 x 6 H2O stock composition","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"solutions[6].composition[0].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"solutions[6].composition[0].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    primary explicitly reports this stock strength in g/L. Preserve it as stock composition
    rather than final-medium concentration. The five acidified stock notes correctly
    preserve 0.01 N H2SO4; no acid mass or molarity conversion is inferred. Vanadyl
    hydration number remains unspecified where the primary uses x.","source_stage":"Separate
    stock strength","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 14 (zero-based)","quote":"<TR><TD WIDTH=75%> NiCl<sub>2</sub>&#183;6H<sub>2</sub>O
    (0.2 g/L in 0.01 N H<sub>2</sub>SO<sub>4</sub>) </TD><TD WIDTH=15% ALIGN=RIGHT><font
    size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%
    ALIGN=RIGHT> &#181;l  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q37","label":"Generated wrapper instruction","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"preparation_steps","stored":[{"step_number":1,"action":"MIX","description":"Use
    Medium No. 618 with 16.0 g/L (final) NaCl."}]}],"decision":"evidence_only","rationale":"The
    exact existing wrapper sentence is supported, but it does not make the stale copied
    ingredients correct. Retain the wrapper and expand only the explicitly inherited
    JCM 618 preparation under the 16 g/L override.","source_stage":"Wrapper instruction","sources":[{"evidence_id":"apiJ619","reference":"https://mediadive.dsmz.de/rest/medium/J619","raw_path":"REVIEW_WORK/batch068/source01-03/apiJ619.bin","raw_sha256":"cdfe8fd1ab5b227b0afe1b5fa6081f9933c0ade6b08d8b7d37bfaa410ad10d2a","text_sha256":"04811f69f27d3668ee21d1831afa0b587930ccd6ba7480766cc56343efdd50f8","accessed_at":"2026-10-28T13:11:53.703728Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Use Medium No. 618 with 16.0 g/L (final) NaCl.\"\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]},{"quantity_id":"q38","label":"Maintained preparation sequence","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"preparation_steps","stored":[{"step_number":1,"action":"MIX","description":"Add
    the base components to 900 ml distilled water and mix thoroughly."},{"step_number":2,"action":"MIX","description":"Add
    each trace-metal stock solution at 0.1 ml/L in the listed order."},{"step_number":3,"action":"ADJUST_PH","description":"Adjust
    pH to 7.5, bring the volume to 1.0 L with distilled water, and autoclave."},{"step_number":4,"action":"HEAT","description":"Inoculate
    into the medium prewarmed to the optimal growth temperature."}]},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"preparation_steps","stored":[{"step_number":1,"action":"MIX","description":"Add
    the base components to 900 ml distilled water and mix thoroughly."},{"step_number":2,"action":"MIX","description":"Add
    each trace-metal stock solution at 0.1 ml/L in the listed order."},{"step_number":3,"action":"ADJUST_PH","description":"Adjust
    pH to 7.5, bring the volume to 1.0 L with distilled water, and autoclave."},{"step_number":4,"action":"HEAT","description":"Inoculate
    into the medium prewarmed to the optimal growth temperature."}]}],"decision":"evidence_only","rationale":"The
    owners preserve initial 900 mL, ordered stock additions, pH 7.5 and explicit final
    1 L, autoclaving and the unquantified prewarming instruction. No specific incubation
    temperature is supplied or inferred.","source_stage":"Source preparation","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Mix/order
    sentence","quote":"Add components to distilled water and mix thoroughly.  Then,
    add the following solutions in order listed:","quote_basis":"derivative text"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Exact
    qualitative prewarming comment","quote":"Comment: Inoculate into the medium prewarmed
    to the optimal growth temperature.","quote_basis":"derivative text"}]},{"quantity_id":"q39","label":"Maintained
    sterilization","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"sterilization","stored":{"method":"AUTOCLAVE","temperature":{"value":121.0,"unit":"CELSIUS"},"duration":"15
    min","notes":"JCM''s default instruction is to autoclave media at 121 C for 15
    min."}},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"sterilization","stored":{"method":"AUTOCLAVE","temperature":{"value":121.0,"unit":"CELSIUS"},"duration":"15
    min","notes":"JCM''s default instruction is to autoclave media at 121 C for 15
    min."}}],"decision":"evidence_only","rationale":"The current JCM page default
    explicitly supplies 121°C for 15 min unless otherwise stated; the wrapper contains
    no conflicting override. Retain the owners default attribution.","source_stage":"Default
    sterilization attribution","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Current
    page default","quote":"Unless otherwise stated, sterilize media by autoclaving
    at 121°C for 15 min.","quote_basis":"derivative text"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Current
    wrapper page default","quote":"Unless otherwise stated, sterilize media by autoclaving
    at 121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q40","label":"Maintained
    pH","local_fields":[{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"ph_value","stored":7.5},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"ph_value","stored":7.5}],"decision":"evidence_only","rationale":"Both
    owner pH values agree with the inherited JCM 618 instruction; the generated target
    lacks ph_value.","source_stage":"Recipe pH","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"Final-volume
    and pH instruction","quote":"Adjust pH to 7.5, bring volume to 1.0 L with distilled
    water and autoclave.","quote_basis":"derivative text"}]},{"quantity_id":"q41","label":"Liquid
    physical state","local_fields":[{"path":"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml","field_path":"physical_state","stored":"LIQUID"},{"path":"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml","field_path":"physical_state","stored":"LIQUID"},{"path":"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml","field_path":"physical_state","stored":"LIQUID"}],"decision":"evidence_only","rationale":"The
    exact JCM 618 base and 619 wrapper include no agar or Gelrite; liquid classification
    is consistent with this source scope. The DSM CYS Gelrite formulation is a different
    source and is not transferred.","source_stage":"Exact JCM source scope","sources":[{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 0 (zero-based)","quote":"<TR><TD WIDTH=75%> N-Z-Case (Wako)                                          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 1 (zero-based)","quote":"<TR><TD WIDTH=75%> Yeast extract (BD-Difco)                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 2 (zero-based)","quote":"<TR><TD WIDTH=75%> Soluble starch (BD-Difco)                               </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 3 (zero-based)","quote":"<TR><TD WIDTH=75%> NaCl                                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 4 (zero-based)","quote":"<TR><TD WIDTH=75%> MgCl<sub>2</sub>&#183;6H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.125&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 5 (zero-based)","quote":"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.025&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 6 (zero-based)","quote":"<TR><TD WIDTH=75%> FeSO<sub>4</sub>&#183;7H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm618","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618","raw_path":"REVIEW_WORK/batch068/source01-03/jcm618.bin","raw_sha256":"0a38d8f9dca301bc19742d18f4be04c0c30281290d503b7ad4e8227a2781f414","text_sha256":"d20d9418ed2360b9074c5e4872980acc357164dfb4738b024f34cfe1a68c205f","accessed_at":"2026-10-28T13:11:53.281925Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;900.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm619","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619","raw_path":"REVIEW_WORK/batch068/source01-03/jcm619.bin","raw_sha256":"b390f3a5458ec82d50b3d649769511c366b076ea810b0d88ac99e917142a6641","text_sha256":"ae83dece9e4794cbebcb9443a14b4af7f709a2d828c345ca07d295c73ee0ea04","accessed_at":"2026-10-28T13:11:53.421663Z","locator":"Exact
    wrapper override","quote":"with 16.0 g/L (final) NaCl.","quote_basis":"derivative
    text"}]}],"document_scopes":{"data/merge_yaml/merged/CYS_Medium_For_YMO722.yaml":null,"data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All current ontology IDs resolve and the captured canonical labels agree;
    correct MgCl2 hexahydrate, CaCl2 dihydrate, Fe/Zn/Cu/Mn/Co hydrates and variable
    vanadyl hydration are preserved. The generated nickel anhydrous identity conflicts
    with the source and repaired owners. MIM preferred cobalt/nickel hexahydrate rows
    retain their observed REJECTED status despite other mapped label rows; this snapshot
    status is distinct from OLS supplied-form identity. N-Z-Case brand remains intentionally
    unresolved; generic yeast/starch terms do not certify BD-Difco grade.
  target_ids:
  - CultureMech:002966
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: Five exact-header reports were read and all 19 historical API snippets
    and both cited raw hashes match current captures. Prior bulk reports left stock
    topology unresolved; current primary evidence now supports the repaired owners,
    while the generated target remains stale. The September repair event and current
    repair_record implementation agree structurally; no historical execution is replayed.
    The current conservative merger rejects the parent/variant differences.
  target_ids:
  - CultureMech:002966
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-002966-salinity-variant-merge
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The target combines parent and salinity-variant identities
  description: Keep JCM 618 and JCM 619 as distinct salinity variants. The primary
    parent has 20 g/L final NaCl; the explicit YMO722 wrapper changes it to 16 g/L.
    Current maintained records correctly represent this relationship. The generated
    target retains both contributors and stale 22.2222 g/L NaCl; regenerate from compatible
    source-specific formulations after curating remaining evidence.
  target_ids:
  - CultureMech:002966
  field_paths:
  - merged_from
  - synonyms
  - ingredients[3].concentration
  - parent_media
  evidence_ids:
  - jcm618
  - jcm619
  - apiJ618
  - apiJ619
  - writer-repair
  - writer-formulation
  rule_id: review-yaml-record/salinity-variant-merge
  native_severity: P2
  normalization_reason: Custom source identity, quantity-stage or supplied-form rule
    normalized major (native priority P2); no nonexistent numbered rubric is claimed.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-002966-stale-volume-stock-expansion
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Generated concentrations and stock topology are stale
  description: Replace the generated stale 900 mL-normalized main rates and seven
    false 100 G_PER_L rows through maintained-input regeneration, preserving the already-correct
    owner masses, explicit final 1 L, seven stock strengths and 0.1 mL/L additions.
    Restore owner water, pH and preparation context. The current importer still accepts
    these unit-corrupted compound rows and prioritizes API g_l, so a blind import
    is not a source-validating repair.
  target_ids:
  - CultureMech:002966
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
  - ingredients[10].concentration
  - ingredients[11].concentration
  - ingredients[12].concentration
  - ingredients[13].concentration
  - solutions
  - ph_value
  - preparation_steps
  evidence_ids:
  - jcm618
  - jcm619
  - apiJ618
  - writer-mediadive
  - writer-repair
  rule_id: review-yaml-record/stale-volume-stock-expansion
  native_severity: P2
  normalization_reason: Custom source identity, quantity-stage or supplied-form rule
    normalized major (native priority P2); no nonexistent numbered rubric is claimed.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-002966-stale-nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Generated nickel grounding lost the corrected hydrate
  description: The generated NiCl2·6H2O row still uses CHEBI:34887 nickel dichloride
    in both asserted slots. Both maintained stock components correctly use CHEBI:53542
    nickel chloride hexahydrate. Preserve that repaired supplied-form grounding during
    source-specific regeneration; do not reinterpret the source amount as anhydrous
    mass. The magnesium and calcium hydrates already agree with this exact JCM source.
  target_ids:
  - CultureMech:002966
  field_paths:
  - ingredients[13].term
  - ingredients[13].mediaingredientmech_chebi_term
  evidence_ids:
  - jcm618
  - chebi34887
  - chebi53542
  - owner
  - owner-2
  rule_id: review-yaml-record/stale-nickel-hydrate
  native_severity: P2
  normalization_reason: Custom source identity, quantity-stage or supplied-form rule
    normalized major (native priority P2); no nonexistent numbered rubric is claimed.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-002966-claim-history-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Supported owner repairs still lack claim-level evidence
  description: Attach exact JCM primary snippets to the maintained ingredients and
    root evidence for the solution doses/preparation. Preserve current repairs and
    all earlier events byte-for-byte, including the old naive copy event; append only
    a new verified event. The current repair writer replaces matching curator/action
    events, so its rerun is not an append-only history operation. Historical API byte
    matches authenticate content, not earlier execution or the scientifically correct
    final-volume basis.
  target_ids:
  - CultureMech:002966
  field_paths:
  - evidence
  - references
  - curation_history
  evidence_ids:
  - jcm618
  - jcm619
  - history-auth
  - writer-repair
  rule_id: review-yaml-record/claim-history-provenance
  native_severity: P3
  normalization_reason: Custom claim/event-provenance rule normalized minor (native
    priority P3); corrected owner science is preserved.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml
    role: maintained normalized contributor
actions:
- action_id: a1
  description: Keep JCM 618 and JCM 619 as distinct salinity variants. The primary
    parent has 20 g/L final NaCl; the explicit YMO722 wrapper changes it to 16 g/L.
    Current maintained records correctly represent this relationship. The generated
    target retains both contributors and stale 22.2222 g/L NaCl; regenerate from compatible
    source-specific formulations after curating remaining evidence.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002966
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml
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
  description: Replace the generated stale 900 mL-normalized main rates and seven
    false 100 G_PER_L rows through maintained-input regeneration, preserving the already-correct
    owner masses, explicit final 1 L, seven stock strengths and 0.1 mL/L additions.
    Restore owner water, pH and preparation context. The current importer still accepts
    these unit-corrupted compound rows and prioritizes API g_l, so a blind import
    is not a source-validating repair.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002966
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml
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
  description: The generated NiCl2·6H2O row still uses CHEBI:34887 nickel dichloride
    in both asserted slots. Both maintained stock components correctly use CHEBI:53542
    nickel chloride hexahydrate. Preserve that repaired supplied-form grounding during
    source-specific regeneration; do not reinterpret the source amount as anhydrous
    mass. The magnesium and calcium hydrates already agree with this exact JCM source.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002966
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml
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
  description: Attach exact JCM primary snippets to the maintained ingredients and
    root evidence for the solution doses/preparation. Preserve current repairs and
    all earlier events byte-for-byte, including the old naive copy event; append only
    a new verified event. The current repair writer replaces matching curator/action
    events, so its rerun is not an append-only history operation. Historical API byte
    matches authenticate content, not earlier execution or the scientifically correct
    final-volume basis.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:002966
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J618_CYS_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cys_medium_for_ymo722.yaml
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
- API J618 reports main rates on a 900 mL normalization and corrupted microliter units;
  exact current JCM primary final-volume and stock rows take precedence within this
  source scope, with the discrepancy retained.
- The copy_referenced_compositions writer was not found in the current scripts/src
  tree by ignored-inclusive rg; its exact historical implementation is not reconstructed
  from the event.
- No DSM 1108/1108a formulation or stock ambiguity is transferred into this JCM-specific
  review. The linked TOGO siblings are checked for path/ID identity only.
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
