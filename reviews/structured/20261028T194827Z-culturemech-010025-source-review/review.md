# Scientific review: Desulfomicrobium Medium

- Review: 20261028T194827Z-culturemech-010025-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T19:40:28.168919Z
- Finished UTC: 2026-10-28T19:48:27.005594Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact JCM616 identity is supported, but stock flattening, mg-to-g unit errors, liquid-dose representation, stale water generation, two supplied-hydrate IDs and missing preparation context require curation. Existing owner repair and valid source forms are explicitly credited.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch076 index 07
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010025 | data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml | generated | desulfomicrobium_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:010025 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:010025 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:010025 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:010025 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact source identity

identity: supported. Targets: CultureMech:010025.

The selected target and sole owner explicitly identify TOGO M625 and JCM616. Fresh JCM616, TOGO M625 and APIJ616 agree on the named formulation and stock topology. The distinct MediaDive comparison record in older reports is context only; no automatic merge or strain-growth assertion follows.

### Native structure and scoped completeness

schema: supported. Targets: CultureMech:010025.

All four original canonical diagnostics passed. This does not authenticate formulation science; reference validation reported zero checks. Every target/owner field and all concentrations were read.

### Classification and descriptive flags

consistency: concern. Targets: CultureMech:010025.

The complete named-chemical formulation and provider complex_medium=no support revisiting COMPLEX/UNDEFINED; LIQUID is supported. The inherited high_metal flag has no inspected threshold or organism claim and is not independently certified.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:010025.

60 current concentration fields are covered by 34 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b076-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","quantity_field_count":60,"decisions":[{"quantity_id":"q1","label":"Main and stock waters; generated stale duplicate sum","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"The owner repair reduced the identical-duplicate sum from 3.0 to 1.0 and is credited; the generated target remains stale at 3.0. Both retain G_PER_L for a source liquid input. Distinguish the main 1 L water from each stock water, without treating input water as measured final medium.","source_stage":"Main input versus separate stocks","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 8 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 29 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"MgSO4・7H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The literal JCM batch mass is supported and retained numerically, but its local G_PER_L denominator is not established by 1 L input water followed by stock additions. APIJ616 separately declares a 1033 mL main volume and its own explicit g_l rate; that provider normalization is evidence, not proof of measured final volume or authority to silently replace this JCM recipe basis.","source_stage":"Main batch mass; provider normalization separate","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 3 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.484027,\n                        \"mmol_l\": 1.96379,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"CaCl2・2H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The literal JCM batch mass is supported and retained numerically, but its local G_PER_L denominator is not established by 1 L input water followed by stock additions. APIJ616 separately declares a 1033 mL main volume and its own explicit g_l rate; that provider normalization is evidence, not proof of measured final volume or authority to silently replace this JCM recipe basis.","source_stage":"Main batch mass; provider normalization separate","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 2 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.05&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0484027,\n                        \"mmol_l\": 0.329237,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.25","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.25","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The literal JCM batch mass is supported and retained numerically, but its local G_PER_L denominator is not established by 1 L input water followed by stock additions. APIJ616 separately declares a 1033 mL main volume and its own explicit g_l rate; that provider normalization is evidence, not proof of measured final volume or authority to silently replace this JCM recipe basis.","source_stage":"Main batch mass; provider normalization separate","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 0 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.25&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.242014,\n                        \"mmol_l\": 1.77839,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The literal JCM batch mass is supported and retained numerically, but its local G_PER_L denominator is not established by 1 L input water followed by stock additions. APIJ616 separately declares a 1033 mL main volume and its own explicit g_l rate; that provider normalization is evidence, not proof of measured final volume or authority to silently replace this JCM recipe basis.","source_stage":"Main batch mass; provider normalization separate","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 1 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NH&lt;sub&gt;4&lt;/sub&gt;Cl                                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.484027,\n                        \"mmol_l\": 9.04893,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The literal JCM batch mass is supported and retained numerically, but its local G_PER_L denominator is not established by 1 L input water followed by stock additions. APIJ616 separately declares a 1033 mL main volume and its own explicit g_l rate; that provider normalization is evidence, not proof of measured final volume or authority to silently replace this JCM recipe basis.","source_stage":"Main batch mass; provider normalization separate","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 4 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; KCl                                                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.484027,\n                        \"mmol_l\": 6.49265,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"1.42","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"1.42","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The literal JCM batch mass is supported and retained numerically, but its local G_PER_L denominator is not established by 1 L input water followed by stock additions. APIJ616 separately declares a 1033 mL main volume and its own explicit g_l rate; that provider normalization is evidence, not proof of measured final volume or authority to silently replace this JCM recipe basis.","source_stage":"Main batch mass; provider normalization separate","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 5 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.42&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 1.42,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.37464,\n                        \"mmol_l\": 9.67782,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Sodium lactate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1.12","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1.12","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The literal JCM batch mass is supported and retained numerically, but its local G_PER_L denominator is not established by 1 L input water followed by stock additions. APIJ616 separately declares a 1033 mL main volume and its own explicit g_l rate; that provider normalization is evidence, not proof of measured final volume or authority to silently replace this JCM recipe basis.","source_stage":"Main batch mass; provider normalization separate","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 6 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Sodium lactate                                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.12&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Sodium lactate\",\n                        \"compound_id\": 1392,\n                        \"amount\": 1.12,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.08422,\n                        \"mmol_l\": 9.67536,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"Carbon dioxide gas","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE truthfully leaves a dissolved concentration unquantified. The explicit N2/CO2 4:1 v/v gas-phase mixture belongs in preparation context and cannot be substituted for a liquid concentration.","source_stage":"Gas phase versus unquantified dissolved amount","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"jcm616.txt lines 49-53","quote":"Mix ingredients and autoclave.  Cool under a N\n2\n-CO\n2\ngas mixture (4:1, v/v) and add the following solutions from sterile stocks:","quote_basis":"derivative text"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Mix ingredients and autoclave. Cool under a N2-CO2 gas mixture (4:1, v/v) and add the following solutions from sterile stocks: \"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"Nitrogen gas","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE truthfully leaves a dissolved concentration unquantified. The explicit N2/CO2 4:1 v/v gas-phase mixture belongs in preparation context and cannot be substituted for a liquid concentration.","source_stage":"Gas phase versus unquantified dissolved amount","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"jcm616.txt lines 49-53","quote":"Mix ingredients and autoclave.  Cool under a N\n2\n-CO\n2\ngas mixture (4:1, v/v) and add the following solutions from sterile stocks:","quote_basis":"derivative text"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Mix ingredients and autoclave. Cool under a N2-CO2 gas mixture (4:1, v/v) and add the following solutions from sterile stocks: \"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"Na2MoO4・2H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"18","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is a component of SL12B, not a direct main-medium concentration. The API explicitly supports its own stock g_l basis; source water alone is not measured final stock volume. Preserve the printed batch amount and receiving dose separately. The stored number is the printed mg amount mislabeled G_PER_L, creating a further thousand-fold mass-unit error before any stock dilution.","source_stage":"SL12B stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 18 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;18.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 18,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.018,\n                        \"mmol_l\": 0.0743955,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"300","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"300","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is a component of SL12B, not a direct main-medium concentration. The API explicitly supports its own stock g_l basis; source water alone is not measured final stock volume. Preserve the printed batch amount and receiving dose separately. The stored number is the printed mg amount mislabeled G_PER_L, creating a further thousand-fold mass-unit error before any stock dilution.","source_stage":"SL12B stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 19 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;300.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 300,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"FeSO4・7H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is a component of SL12B, not a direct main-medium concentration. The API explicitly supports its own stock g_l basis; source water alone is not measured final stock volume. Preserve the printed batch amount and receiving dose separately.","source_stage":"SL12B stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 13 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.10&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 1.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.1,\n                        \"mmol_l\": 3.95662,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"MnCl4・4H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is a component of SL12B, not a direct main-medium concentration. The API explicitly supports its own stock g_l basis; source water alone is not measured final stock volume. Preserve the printed batch amount and receiving dose separately. The stored number is the printed mg amount mislabeled G_PER_L, creating a further thousand-fold mass-unit error before any stock dilution. The primary and current provider both literally print MnCl4·4H2O; resolve that source identity instead of silently substituting MnCl2.","source_stage":"SL12B stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 15 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnCl&lt;sub&gt;4&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;50.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl4 x 4 H2O\",\n                        \"compound_id\": 1828,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"CoCl2・6H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"190","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"190","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is a component of SL12B, not a direct main-medium concentration. The API explicitly supports its own stock g_l basis; source water alone is not measured final stock volume. Preserve the printed batch amount and receiving dose separately. The stored number is the printed mg amount mislabeled G_PER_L, creating a further thousand-fold mass-unit error before any stock dilution.","source_stage":"SL12B stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 14 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;190.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"NiCl2・6H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"24","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"24","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is a component of SL12B, not a direct main-medium concentration. The API explicitly supports its own stock g_l basis; source water alone is not measured final stock volume. Preserve the printed batch amount and receiving dose separately. The stored number is the printed mg amount mislabeled G_PER_L, creating a further thousand-fold mass-unit error before any stock dilution.","source_stage":"SL12B stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 17 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;24.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q17","label":"CuCl2・2H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is a component of SL12B, not a direct main-medium concentration. The API explicitly supports its own stock g_l basis; source water alone is not measured final stock volume. Preserve the printed batch amount and receiving dose separately. The stored number is the printed mg amount mislabeled G_PER_L, creating a further thousand-fold mass-unit error before any stock dilution.","source_stage":"SL12B stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q18","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"42","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"42","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is a component of SL12B, not a direct main-medium concentration. The API explicitly supports its own stock g_l basis; source water alone is not measured final stock volume. Preserve the printed batch amount and receiving dose separately. The stored number is the printed mg amount mislabeled G_PER_L, creating a further thousand-fold mass-unit error before any stock dilution.","source_stage":"SL12B stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnCl&lt;sub&gt;2&lt;/sub&gt;                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;42.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 42,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.042,\n                        \"mmol_l\": 0.308144,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q19","label":"EDTA・2Na","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"correct","rationale":"This is a component of SL12B, not a direct main-medium concentration. The API explicitly supports its own stock g_l basis; source water alone is not measured final stock volume. Preserve the printed batch amount and receiving dose separately.","source_stage":"SL12B stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 12 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; EDTA&amp;#183;2Na                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2-EDTA\",\n                        \"compound_id\": 34,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q20","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"This printed mg amount belongs to the vitamin stock; it is neither the same number in grams nor a direct main-medium g/L concentration. Credit the explicit API stock g_l declaration separately, preserving its source stage and the 1 mL receiving dose. Listed 1 L water does not independently measure final stock volume.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 24 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Biotin                                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q21","label":"p--Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"80","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"80","unit":"G_PER_L"}}],"decision":"correct","rationale":"This printed mg amount belongs to the vitamin stock; it is neither the same number in grams nor a direct main-medium g/L concentration. Credit the explicit API stock g_l declaration separately, preserving its source stage and the 1 mL receiving dose. Listed 1 L water does not independently measure final stock volume.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 23 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; &lt;I&gt;p&lt;/I&gt;-Aminobenzoic acid                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;80.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 80,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\": 0.583345,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"Thiamine・HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"200","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"200","unit":"G_PER_L"}}],"decision":"correct","rationale":"This printed mg amount belongs to the vitamin stock; it is neither the same number in grams nor a direct main-medium g/L concentration. Credit the explicit API stock g_l declaration separately, preserving its source stage and the 1 mL receiving dose. Listed 1 L water does not independently measure final stock volume.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 28 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Thiamine&amp;#183;HCl                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;200.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[2].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"Pyridoxine・HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"300","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"300","unit":"G_PER_L"}}],"decision":"correct","rationale":"This printed mg amount belongs to the vitamin stock; it is neither the same number in grams nor a direct main-medium g/L concentration. Credit the explicit API stock g_l declaration separately, preserving its source stage and the 1 mL receiving dose. Listed 1 L water does not independently measure final stock volume.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 27 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Pyridoxine&amp;#183;HCl                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;300.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[2].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 300,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.3,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"This printed mg amount belongs to the vitamin stock; it is neither the same number in grams nor a direct main-medium g/L concentration. Credit the explicit API stock g_l declaration separately, preserving its source stage and the 1 mL receiving dose. Listed 1 L water does not independently measure final stock volume.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 22 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin B&lt;sub&gt;1&lt;/sub&gt;&lt;sub&gt;2&lt;/sub&gt;                                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"200","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"200","unit":"G_PER_L"}}],"decision":"correct","rationale":"This printed mg amount belongs to the vitamin stock; it is neither the same number in grams nor a direct main-medium g/L concentration. Credit the explicit API stock g_l declaration separately, preserving its source stage and the 1 mL receiving dose. Listed 1 L water does not independently measure final stock volume.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 25 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Nicotinic acid                                        &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;200.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.62456,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"DL--Calcium pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"This printed mg amount belongs to the vitamin stock; it is neither the same number in grams nor a direct main-medium g/L concentration. Credit the explicit API stock g_l declaration separately, preserving its source stage and the 1 mL receiving dose. Listed 1 L water does not independently measure final stock volume.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 26 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; DL-Calcium pantothenate                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[2].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"DL-Calcium pantothenate\",\n                        \"compound_id\": 1720,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.209864,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"Trace element solution SL12B (see below)","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The literal mL stock addition is incorrectly stored as G_PER_L. Preserve its receiving-batch amount and named stock; an ML_PER_L denominator also needs an explicit recipe basis. The retained preferred_term already names this stock, so replace the Unknown solution name without losing that credit.","source_stage":"Main receiving dose","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution SL12B (see below)                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Trace element solution SL12B\",\n                        \"solution_id\": 4477,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"8% NaHCO3 solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"30","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"correct","rationale":"The literal mL stock addition is incorrectly stored as G_PER_L. Preserve its receiving-batch amount and named stock; an ML_PER_L denominator also needs an explicit recipe basis. The retained preferred_term already names this stock, so replace the Unknown solution name without losing that credit. The source percentage lacks an explicit mass/volume, mass/mass or volume/volume basis; do not infer a density or solute mass.","source_stage":"Main receiving dose","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 9 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 8% NaHCO&lt;sub&gt;3&lt;/sub&gt; solution                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;30.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"attribute\": \"8%\",\n                        \"amount\": 30,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"5% Na2S・9H2O solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The literal mL stock addition is incorrectly stored as G_PER_L. Preserve its receiving-batch amount and named stock; an ML_PER_L denominator also needs an explicit recipe basis. The retained preferred_term already names this stock, so replace the Unknown solution name without losing that credit. The source percentage lacks an explicit mass/volume, mass/mass or volume/volume basis; do not infer a density or solute mass.","source_stage":"Main receiving dose","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 10 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O solution                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"attribute\": \"5%\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"Vitamin solution (see below)","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"solutions[3].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The literal mL stock addition is incorrectly stored as G_PER_L. Preserve its receiving-batch amount and named stock; an ML_PER_L denominator also needs an explicit recipe basis. The retained preferred_term already names this stock, so replace the Unknown solution name without losing that credit.","source_stage":"Main receiving dose","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin solution (see below)                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Vitamin solution\",\n                        \"solution_id\": 4478,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"Stock water 1","local_fields":[],"decision":"evidence_only","rationale":"The source lists 1 L water for this separate stock. Retain as a batch liquid input; there is no explicit make-up-to instruction in this JCM stock table.","source_stage":"Separate stock water","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q32","label":"Stock water 2","local_fields":[],"decision":"evidence_only","rationale":"The source lists 1 L water for this separate stock. Retain as a batch liquid input; there is no explicit make-up-to instruction in this JCM stock table.","source_stage":"Separate stock water","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML table row 29 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[2].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q33","label":"JCM default sterilization","local_fields":[],"decision":"evidence_only","rationale":"The exact JCM page states 121°C for 15 min unless otherwise stated; preserve this source-default provenance with the recipe-specific stock sequencing rather than inventing a strain condition.","source_stage":"Source default","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"jcm616.txt lines 4-4","quote":"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q34","label":"Main preparation, gas ratio and conditional pH","local_fields":[],"decision":"evidence_only","rationale":"The source explicitly separates autoclaving, cooling under N2/CO2 4:1 v/v, sterile stock additions, distribution/sealing and conditional pH 7.0–7.2. Neither current local document preserves these controls. API midpoint 7.1 must not replace the printed range.","source_stage":"Main preparation","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"jcm616.txt lines 49-69","quote":"Mix ingredients and autoclave.  Cool under a N\n2\n-CO\n2\ngas mixture (4:1, v/v) and add the following solutions from sterile stocks:\n8% NaHCO\n3\nsolution\n30.0\nml\n5% Na\n2\nS·9H\n2\nO solution\n1.0\nml\nVitamin solution (see below)\n1.0\nml\nDistribute the medium into culture vessels under the same gas mixture and seal with butyl rubber stoppers. Adjust pH to 7.0 - 7.2, if necessary.","quote_basis":"derivative text"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Mix ingredients and autoclave. Cool under a N2-CO2 gas mixture (4:1, v/v) and add the following solutions from sterile stocks: \"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\": \"Distribute the medium into culture vessels under the same gas mixture and seal with butyl rubber stoppers. Adjust pH to 7.0 - 7.2, if necessary.\"\n                    }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:010025.

Every asserted ontology and secondary slot was joined to fresh OLS scientific objects and exact packaged MIM rows, retaining mapping_status rather than equating every row with an accepted mapping. Cobalt/nickel supplied hydrates conflict with their primary IDs. The manganese formula remains literally ambiguous in the primary/provider. EDTA disodium hydration is unspecified. DL-calcium-pantothenate retains legacy 000926 with no exact current index membership; D-calcium CHEBI:31345 is not a DL substitute. Correct MgSO4 heptahydrate and other matching supplied forms are credited; absence of an exact preferred spelling is distinct from absence of an asserted identifier.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:010025.

All four exact historical reports were read in full, including the two explicitly scoped comparison-record reports. October5 zero source-check counts are historical limitations, not current checks. The owner’s September water repair is credited and the stale generated water is separately identified. Current repair_ingredient/repair_record only collapse identical parts; current cleanup does not sum unequal values. Current TOGO code separates stock sections, so this legacy flattened output is not proof of current flattening. The comparison report’s broad merge recommendation is not adopted: the current formulation comparator includes complete scientific fields and notes.

## Findings

### f1: Stock components and mg amounts were flattened

major / open / confirmed; issue key: culturemech-010025-stock-stage-mass.

Restore the exact SL12B and vitamin stock boundaries in the maintained owner. The direct ingredient array contains nine SL12B and seven vitamin components; fourteen printed mg amounts are stored with the same number as G_PER_L. Preserve source batch amounts, explicit provider stock rates and receiving doses as distinct claims; do not derive final-medium concentrations from input-water volumes. Resolve literal MnCl4·4H2O with authoritative source clarification rather than an assumed correction.

### f2: Liquid inputs and doses have mass units; target misses owner repair

major / open / confirmed; issue key: culturemech-010025-water-dose-stale.

Credit the maintained owner’s September duplicate repair: its water is 1.0 while the generated target remains 3.0. Correct the surviving water G_PER_L representation and the four stock additions currently expressed as G_PER_L; retain the exact source mL amounts and separate stock waters. Review main mass denominators explicitly: the primary lists input water while APIJ616 declares 1033 mL and different main g_l values. Regenerate only after those maintained-input issues are resolved.

### f3: Cobalt and nickel hexahydrates map to anhydrous compounds

major / open / confirmed; issue key: culturemech-010025-supplied-hydrates.

The source and both local supplied names specify CoCl2·6H2O and NiCl2·6H2O, but primary terms CHEBI:35696 and CHEBI:34887 represent the anhydrous salts. Reconcile those exact primary slots using the fresh hexahydrate objects CHEBI:53503 and CHEBI:53542 and attach source evidence. Do not extend this correction to the unresolved manganese source formula or unspecified EDTA hydration.

### f4: Source preparation and pH context are absent

major / open / confirmed; issue key: culturemech-010025-preparation-ph.

Preserve the source-specific preparation sequence, gas-phase ratio, sterile stock additions, conditional pH range and JCM sterilization default in the maintained owner. Current TOGO JSON stores meta.ph, whereas _extract_ph reads root ph; repair that exact current parser boundary and preserve comments through generation. The existing VARIABLE gas placeholders are truthful unquantified dissolved amounts and need no gas-ratio substitution.

### f5: Defined formulation and existing stock names are obscured

minor / open / confirmed; issue key: culturemech-010025-classification-names.

Review COMPLEX/UNDEFINED against the chemically specified source and explicit API complex_medium=no; LIQUID is supported. Replace each Unknown solution name from its already-retained preferred_term. Resolve legacy MediaIngredientMech:000926 only with an exact DL-calcium-pantothenate identity; current CHEBI:31345 explicitly describes D stereochemistry and cannot certify the DL supplied form.

## Recommended Actions And Acceptance Checks

### a1

Restore the exact SL12B and vitamin stock boundaries in the maintained owner. The direct ingredient array contains nine SL12B and seven vitamin components; fourteen printed mg amounts are stored with the same number as G_PER_L. Preserve source batch amounts, explicit provider stock rates and receiving doses as distinct claims; do not derive final-medium concentrations from input-water volumes. Resolve literal MnCl4·4H2O with authoritative source clarification rather than an assumed correction.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Credit the maintained owner’s September duplicate repair: its water is 1.0 while the generated target remains 3.0. Correct the surviving water G_PER_L representation and the four stock additions currently expressed as G_PER_L; retain the exact source mL amounts and separate stock waters. Review main mass denominators explicitly: the primary lists input water while APIJ616 declares 1033 mL and different main g_l values. Regenerate only after those maintained-input issues are resolved.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The source and both local supplied names specify CoCl2·6H2O and NiCl2·6H2O, but primary terms CHEBI:35696 and CHEBI:34887 represent the anhydrous salts. Reconcile those exact primary slots using the fresh hexahydrate objects CHEBI:53503 and CHEBI:53542 and attach source evidence. Do not extend this correction to the unresolved manganese source formula or unspecified EDTA hydration.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

Preserve the source-specific preparation sequence, gas-phase ratio, sterile stock additions, conditional pH range and JCM sterilization default in the maintained owner. Current TOGO JSON stores meta.ph, whereas _extract_ph reads root ph; repair that exact current parser boundary and preserve comments through generation. The existing VARIABLE gas placeholders are truthful unquantified dissolved amounts and need no gas-ratio substitution.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

Review COMPLEX/UNDEFINED against the chemically specified source and explicit API complex_medium=no; LIQUID is supported. Replace each Unknown solution name from its already-retained preferred_term. Resolve legacy MediaIngredientMech:000926 only with an exact DL-calcium-pantothenate identity; current CHEBI:31345 explicitly describes D stereochemistry and cannot certify the DL supplied form.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| jcm616 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616; REVIEW_WORK/batch076/source07-08-10/jcm616.json; exact original raw/text/hash/time metadata | context_only | Exact selected JCM616 primary identity and formulation; embedded sections retain their distinct stages. |
| currentTogo625 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M625; REVIEW_WORK/batch076/source07-08-10/currentTogo625.json; exact original raw/text/hash/time metadata | context_only | Exact current selected TOGO M625 provider JSON. |
| apiJ616 | https://mediadive.dsmz.de/rest/medium/J616; REVIEW_WORK/batch076/source07-08-10/apiJ616.json; exact original raw/text/hash/time metadata | context_only | Exact current provider J616 identity and stage-specific composition. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; REVIEW_WORK/batch076/source07-08-10/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; REVIEW_WORK/batch076/source07-08-10/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; REVIEW_WORK/batch076/source07-08-10/chebi31345.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| target | data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-17 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-18 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfomicrobium_medium__3dc5367b.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-19 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-20 | reports/yaml_record_review/20260922T191530Z-desulfomicrobium_medium__3dc5367b.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| writer-togo | src/culturemech/import/togo_importer.py; _extract_primary_components, _extract_assembled_solutions, _local_batch_volume_ml, _parse_unit, _extract_ph, _extract_preparation_steps | context_only | Current parser separates assembled primary and stock sections and reads root ph, whereas this current source stores meta.ph. Bare mass units still do not establish final-volume denominators. |
| writer-repair | scripts/repair_merged_duplicates.py; repair_ingredient, repair_record | context_only | Current repair collapses only identical merged parts; the owner water repair is credited without treating the surviving water unit as correct. |
| writer-cleanup | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group does not sum unequal concentrations; present historical sums do not establish that the current function still sums them. |
| historical-reading | REVIEW_WORK/batch076/record07/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch076/record07/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch076/record07/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser excludes percent-stock additions from primary ingredients, preserves referenced stock amounts/attributes separately and prioritizes explicit provider g_l. It skips source water; bare units alone do not establish a final-volume basis. Current code is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| historical-object-joins | REVIEW_WORK/batch076/record07/historical-current-object-joins.json; Complete exact decoded-object comparisons | context_only | Historical object correspondence is distinct from raw-response authentication. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; REVIEW_WORK/batch076/source07-08-10/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; REVIEW_WORK/batch076/source07-08-10/chebi31795.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; REVIEW_WORK/batch076/source07-08-10/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; REVIEW_WORK/batch076/source07-08-10/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; REVIEW_WORK/batch076/source07-08-10/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; REVIEW_WORK/batch076/source07-08-10/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; REVIEW_WORK/batch076/source07-08-10/chebi32149.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi75228 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75228; REVIEW_WORK/batch076/source07-08-10/chebi75228.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; REVIEW_WORK/batch076/source07-08-10/chebi16526.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; REVIEW_WORK/batch076/source07-08-10/chebi17997.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; REVIEW_WORK/batch076/source07-08-10/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; REVIEW_WORK/batch076/source07-08-10/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; REVIEW_WORK/batch076/source07-08-10/chebi75836.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; REVIEW_WORK/batch076/source07-08-10/chebi35696.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; REVIEW_WORK/batch076/source07-08-10/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; REVIEW_WORK/batch076/source07-08-10/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; REVIEW_WORK/batch076/source07-08-10/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi64734 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64734; REVIEW_WORK/batch076/source07-08-10/chebi64734.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; REVIEW_WORK/batch076/source07-08-10/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; REVIEW_WORK/batch076/source07-08-10/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; REVIEW_WORK/batch076/source07-08-10/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; REVIEW_WORK/batch076/source07-08-10/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; REVIEW_WORK/batch076/source07-08-10/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; REVIEW_WORK/batch076/source07-08-10/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| quantities | REVIEW_WORK/batch076/record07/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch076/record07/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch076/record07/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch076/record07/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch076/record07/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch076/record07/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch076/record07/existing-claim-authentication.json; Complete sidecar | context_only | No attached claims in this scoped sidecar; historical object joins are separate evidence. |
| check-schema | REVIEW_WORK/batch076/record07/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch076/record07/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch076/record07/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch076/record07/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- MnCl4·4H2O is a literal source ambiguity; this review supplies no guessed manganese replacement.
- The distinct MediaDive J616 record appears only in prior comparison context and is not an additional curation target.
- The 8% bicarbonate and 5% sulfide stock labels do not state a percentage basis.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T194827Z-culturemech-010025-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: Desulfomicrobium Medium'
started_at: '2026-10-28T19:40:28.168919Z'
finished_at: '2026-10-28T19:48:27.005594Z'
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
summary: The exact JCM616 identity is supported, but stock flattening, mg-to-g unit
  errors, liquid-dose representation, stale water generation, two supplied-hydrate
  IDs and missing preparation context require curation. Existing owner repair and
  valid source forms are explicitly credited.
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
  - path: data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml
    sha256: cf3224999de84da7557b343c3348633de692051d2ccb3c35a31e5a84d52a8560
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml
    sha256: cce5bc656114e7d979ee38b604e295d1d940cfb83c8cb439d2b829ffaf8d8616
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.md
    sha256: d1752e66f94a24692b51898c696652d4d2683eb9c3eb89f182dea6b1c4ca25a0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfomicrobium_medium__3dc5367b.md
    sha256: bf57963f0f21a661745f2a48c5f56f09c690b3dc815121a3e0638d3ae6a24eef
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.md
    sha256: 0ecc8759d81125bdc5f1a7cc7aba3e84d36660155affa0c4a123e9da6a3beddc
    role: context
  - path: reports/yaml_record_review/20260922T191530Z-desulfomicrobium_medium__3dc5367b.md
    sha256: 084d34afc0ae0da4fc993f64ed01bdf414266f7a806e5d7601d5549d885ef5b2
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
  selection: Authoritative batch076 index 07
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010025
targets:
- target_id: CultureMech:010025
  path: data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml
  label: desulfomicrobium_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml
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
  - CultureMech:010025
  command: just validate-schema data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml
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
  - CultureMech:010025
  command: just validate-strict data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml
    --out REVIEW_WORK/batch076/record07/strict.tsv --workers 1 --quiet
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
  - CultureMech:010025
  command: just validate-terms data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml
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
  - CultureMech:010025
  command: just validate-references data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: jcm616
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616
  accessed_at: '2026-10-28T19:40:26.263337Z'
  locator: REVIEW_WORK/batch076/source07-08-10/jcm616.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact selected JCM616 primary identity and formulation; embedded sections
    retain their distinct stages.
  snapshot_sha256: d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb
- evidence_id: currentTogo625
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M625
  accessed_at: '2026-10-28T19:40:26.407909Z'
  locator: REVIEW_WORK/batch076/source07-08-10/currentTogo625.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Exact current selected TOGO M625 provider JSON.
  snapshot_sha256: 2bbf96b9cfebc513e7ddf173cf7b8c944f6770bba634005cad639d62ef9e91a7
- evidence_id: apiJ616
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J616
  accessed_at: '2026-10-28T19:40:26.223626Z'
  locator: REVIEW_WORK/batch076/source07-08-10/apiJ616.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current provider J616 identity and stage-specific composition.
  snapshot_sha256: 4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  accessed_at: '2026-10-28T19:40:32.044686Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi53503.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  accessed_at: '2026-10-28T19:40:32.046901Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi53542.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  accessed_at: '2026-10-28T19:40:29.645981Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi31345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T19:48:06.369692Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: cf3224999de84da7557b343c3348633de692051d2ccb3c35a31e5a84d52a8560
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T19:48:06.369856Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: cce5bc656114e7d979ee38b604e295d1d940cfb83c8cb439d2b829ffaf8d8616
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T19:48:06.369886Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T19:48:06.370201Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T19:48:06.370226Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T19:48:06.370248Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-17
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T19:48:06.370273Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: d1752e66f94a24692b51898c696652d4d2683eb9c3eb89f182dea6b1c4ca25a0
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfomicrobium_medium__3dc5367b.md
  locator: Complete report
  accessed_at: '2026-10-28T19:48:06.370304Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: bf57963f0f21a661745f2a48c5f56f09c690b3dc815121a3e0638d3ae6a24eef
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T19:48:06.370327Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 0ecc8759d81125bdc5f1a7cc7aba3e84d36660155affa0c4a123e9da6a3beddc
- evidence_id: report-20
  kind: prior_review
  reference: reports/yaml_record_review/20260922T191530Z-desulfomicrobium_medium__3dc5367b.md
  locator: Complete report
  accessed_at: '2026-10-28T19:48:06.370354Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 084d34afc0ae0da4fc993f64ed01bdf414266f7a806e5d7601d5549d885ef5b2
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_primary_components, _extract_assembled_solutions, _local_batch_volume_ml,
    _parse_unit, _extract_ph, _extract_preparation_steps
  accessed_at: '2026-10-28T19:48:06.370386Z'
  support: context_only
  summary: Current parser separates assembled primary and stock sections and reads
    root ph, whereas this current source stores meta.ph. Bare mass units still do
    not establish final-volume denominators.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-repair
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: repair_ingredient, repair_record
  accessed_at: '2026-10-28T19:48:06.370418Z'
  support: context_only
  summary: Current repair collapses only identical merged parts; the owner water repair
    is credited without treating the surviving water unit as correct.
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T19:48:06.370439Z'
  support: context_only
  summary: Current _merge_ingredient_group does not sum unequal concentrations; present
    historical sums do not establish that the current function still sums them.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch076/record07/historical-reading.json
  accessed_at: '2026-10-28T19:48:06.372104Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 077aba7e6fddd6066d12fd0a579922d3927ddcbaeb9549598fa5e4cc946ee12b
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch076/record07/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T19:48:06.372143Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch076/record07/complete-document-reader.json
  accessed_at: '2026-10-28T19:48:06.372275Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 2873b1c6861586b0150b701b450214dde8cb0c4426e16bbcd6499f84a841f3bd
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T19:48:06.372312Z'
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
  accessed_at: '2026-10-28T19:48:06.372343Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: historical-object-joins
  kind: prior_review
  reference: REVIEW_WORK/batch076/record07/historical-current-object-joins.json
  accessed_at: '2026-10-28T19:48:06.372366Z'
  locator: Complete exact decoded-object comparisons
  support: context_only
  summary: Historical object correspondence is distinct from raw-response authentication.
  snapshot_sha256: 3dddbcbd047b9d183ff8d3ccb2a5f88569220c57c45bcc7d0dc102686d947586
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  accessed_at: '2026-10-28T19:40:27.162976Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi15377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  accessed_at: '2026-10-28T19:40:30.088231Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi31795.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  accessed_at: '2026-10-28T19:40:33.256487Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi86158.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  accessed_at: '2026-10-28T19:40:32.506340Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi63036.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  accessed_at: '2026-10-28T19:40:29.643732Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi31206.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  accessed_at: '2026-10-28T19:40:30.726069Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi32588.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  accessed_at: '2026-10-28T19:40:30.237352Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi32149.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: chebi75228
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75228
  accessed_at: '2026-10-28T19:40:32.824099Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi75228.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 725fbc04444c481cec25519a6f632470427a7020613af93e84e05b5f23d66ccf
- evidence_id: chebi16526
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  accessed_at: '2026-10-28T19:40:27.776476Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi16526.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: chebi17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  accessed_at: '2026-10-28T19:40:28.493553Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi17997.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  accessed_at: '2026-10-28T19:40:32.669688Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi75213.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  accessed_at: '2026-10-28T19:40:30.840133Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi33118.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  accessed_at: '2026-10-28T19:40:33.115496Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi75836.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi35696
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  accessed_at: '2026-10-28T19:40:31.347865Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi35696.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  accessed_at: '2026-10-28T19:40:31.295602Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi34887.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  accessed_at: '2026-10-28T19:40:33.411707Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi86318.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  accessed_at: '2026-10-28T19:40:31.588549Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi49976.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi64734
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64734
  accessed_at: '2026-10-28T19:40:32.685772Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi64734.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 95b7557b1867dcce37a69714dbad0a6a6a6c11c66dde39c6793a2307a7fb0e1c
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  accessed_at: '2026-10-28T19:40:27.631883Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi15956.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  accessed_at: '2026-10-28T19:40:29.484850Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi30753.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  accessed_at: '2026-10-28T19:40:31.450132Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi49105.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  accessed_at: '2026-10-28T19:40:29.503180Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi30961.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  accessed_at: '2026-10-28T19:40:28.239467Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi176843.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  accessed_at: '2026-10-28T19:40:27.477267Z'
  locator: REVIEW_WORK/batch076/source07-08-10/chebi15940.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch076/record07/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:48:06.467778Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 0b213b06c071f896cc06dee8667a0645531439e21d7a97f0455c021987d9c7a3
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch076/record07/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:48:06.467842Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 6d8b095c56019b35672dd6a3950fd172e322e7d94b070fe709d4b88a67ff072b
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch076/record07/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:48:06.467941Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 42dc450f369d8a67499900d7e50d525fe0016f2f4e1237cd8c40b6e0fc85f72e
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch076/record07/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:48:06.467994Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 8f1abcf99207014f0b7d7733a5a299c5aa1057caa84dbd6f4640d281aae7b7e5
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch076/record07/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:48:06.468039Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: d0deeb80e2c8007406bca9789b1e73a9ad3728650897717f5971794038a2e0bb
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch076/record07/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:48:06.468062Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 74512eff3f71dc379ee91728a5ac5179463e6972d22a690280eca08d39159e69
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch076/record07/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:48:06.468080Z'
  support: context_only
  summary: No attached claims in this scoped sidecar; historical object joins are
    separate evidence.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch076/record07/schema-result.json
  accessed_at: '2026-10-28T19:40:29.410106Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 4b86392c97d733a6ed13557ba1bacc498dd3578e0bf671b251fbaca77a58605b
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch076/record07/strict-result.json
  accessed_at: '2026-10-28T19:40:30.403971Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 199929622188c5abdaab7e2b5baa1446f0ece25839f2e0b0fa26c105078e4f31
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch076/record07/terms-result.json
  accessed_at: '2026-10-28T19:40:31.850325Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: b90829f36e62d17f57f5b9b278eab278874354cec34eb8de55a9b2a0a7c45dbf
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch076/record07/references-result.json
  accessed_at: '2026-10-28T19:40:32.691836Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: ab36149c904fc1c8d7257c86e306dec4fcebcb78595e79f2d5c47aab6cc35c40
assessments:
- assessment_id: identity
  area: identity
  topic: Exact source identity
  outcome: supported
  summary: The selected target and sole owner explicitly identify TOGO M625 and JCM616.
    Fresh JCM616, TOGO M625 and APIJ616 agree on the named formulation and stock topology.
    The distinct MediaDive comparison record in older reports is context only; no
    automatic merge or strain-growth assertion follows.
  target_ids:
  - CultureMech:010025
  evidence_ids:
  - target
  - owner
  - jcm616
  - currentTogo625
  - apiJ616
- assessment_id: structure
  area: schema
  topic: Native structure and scoped completeness
  outcome: supported
  summary: All four original canonical diagnostics passed. This does not authenticate
    formulation science; reference validation reported zero checks. Every target/owner
    field and all concentrations were read.
  target_ids:
  - CultureMech:010025
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
  - census
- assessment_id: classification
  area: consistency
  topic: Classification and descriptive flags
  outcome: concern
  summary: The complete named-chemical formulation and provider complex_medium=no
    support revisiting COMPLEX/UNDEFINED; LIQUID is supported. The inherited high_metal
    flag has no inspected threshold or organism claim and is not independently certified.
  target_ids:
  - CultureMech:010025
  evidence_ids:
  - jcm616
  - apiJ616
  - target
  - owner
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 60 current concentration fields are covered by 34 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:010025
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b076-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","quantity_field_count":60,"decisions":[{"quantity_id":"q1","label":"Main
    and stock waters; generated stale duplicate sum","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    owner repair reduced the identical-duplicate sum from 3.0 to 1.0 and is credited;
    the generated target remains stale at 3.0. Both retain G_PER_L for a source liquid
    input. Distinguish the main 1 L water from each stock water, without treating
    input water as measured final medium.","source_stage":"Main input versus separate
    stocks","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 8 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 21 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 29 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L        </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q2","label":"MgSO4・7H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    literal JCM batch mass is supported and retained numerically, but its local G_PER_L
    denominator is not established by 1 L input water followed by stock additions.
    APIJ616 separately declares a 1033 mL main volume and its own explicit g_l rate;
    that provider normalization is evidence, not proof of measured final volume or
    authority to silently replace this JCM recipe basis.","source_stage":"Main batch
    mass; provider normalization separate","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 3 (zero-based)","quote":"<TR><TD WIDTH=75%> MgSO<sub>4</sub>&#183;7H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.484027,\n                        \"mmol_l\":
    1.96379,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q3","label":"CaCl2・2H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    literal JCM batch mass is supported and retained numerically, but its local G_PER_L
    denominator is not established by 1 L input water followed by stock additions.
    APIJ616 separately declares a 1033 mL main volume and its own explicit g_l rate;
    that provider normalization is evidence, not proof of measured final volume or
    authority to silently replace this JCM recipe basis.","source_stage":"Main batch
    mass; provider normalization separate","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 2 (zero-based)","quote":"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.05&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.05,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0484027,\n                        \"mmol_l\":
    0.329237,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q4","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.25","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.25","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    literal JCM batch mass is supported and retained numerically, but its local G_PER_L
    denominator is not established by 1 L input water followed by stock additions.
    APIJ616 separately declares a 1033 mL main volume and its own explicit g_l rate;
    that provider normalization is evidence, not proof of measured final volume or
    authority to silently replace this JCM recipe basis.","source_stage":"Main batch
    mass; provider normalization separate","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 0 (zero-based)","quote":"<TR><TD WIDTH=75%> KH<sub>2</sub>PO<sub>4</sub>                                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.25&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.242014,\n                        \"mmol_l\":
    1.77839,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q5","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    literal JCM batch mass is supported and retained numerically, but its local G_PER_L
    denominator is not established by 1 L input water followed by stock additions.
    APIJ616 separately declares a 1033 mL main volume and its own explicit g_l rate;
    that provider normalization is evidence, not proof of measured final volume or
    authority to silently replace this JCM recipe basis.","source_stage":"Main batch
    mass; provider normalization separate","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 1 (zero-based)","quote":"<TR><TD WIDTH=75%> NH<sub>4</sub>Cl                                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.484027,\n                        \"mmol_l\":
    9.04893,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q6","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    literal JCM batch mass is supported and retained numerically, but its local G_PER_L
    denominator is not established by 1 L input water followed by stock additions.
    APIJ616 separately declares a 1033 mL main volume and its own explicit g_l rate;
    that provider normalization is evidence, not proof of measured final volume or
    authority to silently replace this JCM recipe basis.","source_stage":"Main batch
    mass; provider normalization separate","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 4 (zero-based)","quote":"<TR><TD WIDTH=75%> KCl                                                     </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.484027,\n                        \"mmol_l\":
    6.49265,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q7","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"1.42","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"1.42","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    literal JCM batch mass is supported and retained numerically, but its local G_PER_L
    denominator is not established by 1 L input water followed by stock additions.
    APIJ616 separately declares a 1033 mL main volume and its own explicit g_l rate;
    that provider normalization is evidence, not proof of measured final volume or
    authority to silently replace this JCM recipe basis.","source_stage":"Main batch
    mass; provider normalization separate","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 5 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>SO<sub>4</sub>                                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.42&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 1.42,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.37464,\n                        \"mmol_l\":
    9.67782,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q8","label":"Sodium lactate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1.12","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1.12","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    literal JCM batch mass is supported and retained numerically, but its local G_PER_L
    denominator is not established by 1 L input water followed by stock additions.
    APIJ616 separately declares a 1033 mL main volume and its own explicit g_l rate;
    that provider normalization is evidence, not proof of measured final volume or
    authority to silently replace this JCM recipe basis.","source_stage":"Main batch
    mass; provider normalization separate","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 6 (zero-based)","quote":"<TR><TD WIDTH=75%> Sodium lactate                                          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.12&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Sodium lactate\",\n                        \"compound_id\":
    1392,\n                        \"amount\": 1.12,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.08422,\n                        \"mmol_l\":
    9.67536,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q9","label":"Carbon dioxide gas","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE
    truthfully leaves a dissolved concentration unquantified. The explicit N2/CO2
    4:1 v/v gas-phase mixture belongs in preparation context and cannot be substituted
    for a liquid concentration.","source_stage":"Gas phase versus unquantified dissolved
    amount","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"jcm616.txt
    lines 49-53","quote":"Mix ingredients and autoclave.  Cool under a N\n2\n-CO\n2\ngas
    mixture (4:1, v/v) and add the following solutions from sterile stocks:","quote_basis":"derivative
    text"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Mix ingredients and autoclave. Cool under a N2-CO2 gas mixture (4:1, v/v) and
    add the following solutions from sterile stocks: \"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q10","label":"Nitrogen gas","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE
    truthfully leaves a dissolved concentration unquantified. The explicit N2/CO2
    4:1 v/v gas-phase mixture belongs in preparation context and cannot be substituted
    for a liquid concentration.","source_stage":"Gas phase versus unquantified dissolved
    amount","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"jcm616.txt
    lines 49-53","quote":"Mix ingredients and autoclave.  Cool under a N\n2\n-CO\n2\ngas
    mixture (4:1, v/v) and add the following solutions from sterile stocks:","quote_basis":"derivative
    text"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Mix ingredients and autoclave. Cool under a N2-CO2 gas mixture (4:1, v/v) and
    add the following solutions from sterile stocks: \"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q11","label":"Na2MoO4・2H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"18","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is a component of SL12B, not a direct main-medium concentration. The API explicitly
    supports its own stock g_l basis; source water alone is not measured final stock
    volume. Preserve the printed batch amount and receiving dose separately. The stored
    number is the printed mg amount mislabeled G_PER_L, creating a further thousand-fold
    mass-unit error before any stock dilution.","source_stage":"SL12B stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 18 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;18.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 18,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.018,\n                        \"mmol_l\":
    0.0743955,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q12","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"300","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"300","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is a component of SL12B, not a direct main-medium concentration. The API explicitly
    supports its own stock g_l basis; source water alone is not measured final stock
    volume. Preserve the printed batch amount and receiving dose separately. The stored
    number is the printed mg amount mislabeled G_PER_L, creating a further thousand-fold
    mass-unit error before any stock dilution.","source_stage":"SL12B stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 19 (zero-based)","quote":"<TR><TD WIDTH=75%> H<sub>3</sub>BO<sub>3</sub>                                           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;300.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 300,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    4.85123,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q13","label":"FeSO4・7H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is a component of SL12B, not a direct main-medium concentration. The API explicitly
    supports its own stock g_l basis; source water alone is not measured final stock
    volume. Preserve the printed batch amount and receiving dose separately.","source_stage":"SL12B
    stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 13 (zero-based)","quote":"<TR><TD WIDTH=75%> FeSO<sub>4</sub>&#183;7H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.10&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 1.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.1,\n                        \"mmol_l\":
    3.95662,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q14","label":"MnCl4・4H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is a component of SL12B, not a direct main-medium concentration. The API explicitly
    supports its own stock g_l basis; source water alone is not measured final stock
    volume. Preserve the printed batch amount and receiving dose separately. The stored
    number is the printed mg amount mislabeled G_PER_L, creating a further thousand-fold
    mass-unit error before any stock dilution. The primary and current provider both
    literally print MnCl4·4H2O; resolve that source identity instead of silently substituting
    MnCl2.","source_stage":"SL12B stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 15 (zero-based)","quote":"<TR><TD WIDTH=75%> MnCl<sub>4</sub>&#183;4H<sub>2</sub>O                                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;50.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl4 x 4 H2O\",\n                        \"compound_id\":
    1828,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"CoCl2・6H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"190","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"190","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is a component of SL12B, not a direct main-medium concentration. The API explicitly
    supports its own stock g_l basis; source water alone is not measured final stock
    volume. Preserve the printed batch amount and receiving dose separately. The stored
    number is the printed mg amount mislabeled G_PER_L, creating a further thousand-fold
    mass-unit error before any stock dilution.","source_stage":"SL12B stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 14 (zero-based)","quote":"<TR><TD WIDTH=75%> CoCl<sub>2</sub>&#183;6H<sub>2</sub>O                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;190.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q16","label":"NiCl2・6H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"24","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"24","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is a component of SL12B, not a direct main-medium concentration. The API explicitly
    supports its own stock g_l basis; source water alone is not measured final stock
    volume. Preserve the printed batch amount and receiving dose separately. The stored
    number is the printed mg amount mislabeled G_PER_L, creating a further thousand-fold
    mass-unit error before any stock dilution.","source_stage":"SL12B stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 17 (zero-based)","quote":"<TR><TD WIDTH=75%> NiCl<sub>2</sub>&#183;6H<sub>2</sub>O                                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;24.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q17","label":"CuCl2・2H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is a component of SL12B, not a direct main-medium concentration. The API explicitly
    supports its own stock g_l basis; source water alone is not measured final stock
    volume. Preserve the printed batch amount and receiving dose separately. The stored
    number is the printed mg amount mislabeled G_PER_L, creating a further thousand-fold
    mass-unit error before any stock dilution.","source_stage":"SL12B stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 20 (zero-based)","quote":"<TR><TD WIDTH=75%> CuCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q18","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"42","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"42","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is a component of SL12B, not a direct main-medium concentration. The API explicitly
    supports its own stock g_l basis; source water alone is not measured final stock
    volume. Preserve the printed batch amount and receiving dose separately. The stored
    number is the printed mg amount mislabeled G_PER_L, creating a further thousand-fold
    mass-unit error before any stock dilution.","source_stage":"SL12B stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> ZnCl<sub>2</sub>                                               </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;42.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 42,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.042,\n                        \"mmol_l\":
    0.308144,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q19","label":"EDTA・2Na","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    is a component of SL12B, not a direct main-medium concentration. The API explicitly
    supports its own stock g_l basis; source water alone is not measured final stock
    volume. Preserve the printed batch amount and receiving dose separately.","source_stage":"SL12B
    stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 12 (zero-based)","quote":"<TR><TD WIDTH=75%> EDTA&#183;2Na                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2-EDTA\",\n                        \"compound_id\":
    34,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q20","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    printed mg amount belongs to the vitamin stock; it is neither the same number
    in grams nor a direct main-medium g/L concentration. Credit the explicit API stock
    g_l declaration separately, preserving its source stage and the 1 mL receiving
    dose. Listed 1 L water does not independently measure final stock volume.","source_stage":"Vitamin
    stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 24 (zero-based)","quote":"<TR><TD WIDTH=75%> Biotin                                                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q21","label":"p--Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"80","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"80","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    printed mg amount belongs to the vitamin stock; it is neither the same number
    in grams nor a direct main-medium g/L concentration. Credit the explicit API stock
    g_l declaration separately, preserving its source stage and the 1 mL receiving
    dose. Listed 1 L water does not independently measure final stock volume.","source_stage":"Vitamin
    stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 23 (zero-based)","quote":"<TR><TD WIDTH=75%> <I>p</I>-Aminobenzoic acid                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;80.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 80,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\":
    0.583345,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q22","label":"Thiamine・HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"200","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"200","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    printed mg amount belongs to the vitamin stock; it is neither the same number
    in grams nor a direct main-medium g/L concentration. Credit the explicit API stock
    g_l declaration separately, preserving its source stage and the 1 mL receiving
    dose. Listed 1 L water does not independently measure final stock volume.","source_stage":"Vitamin
    stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 28 (zero-based)","quote":"<TR><TD WIDTH=75%> Thiamine&#183;HCl                                    </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;200.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[2].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"Pyridoxine・HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"300","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"300","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    printed mg amount belongs to the vitamin stock; it is neither the same number
    in grams nor a direct main-medium g/L concentration. Credit the explicit API stock
    g_l declaration separately, preserving its source stage and the 1 mL receiving
    dose. Listed 1 L water does not independently measure final stock volume.","source_stage":"Vitamin
    stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 27 (zero-based)","quote":"<TR><TD WIDTH=75%> Pyridoxine&#183;HCl                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;300.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[2].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 300,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.3,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"Vitamin
    B12","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    printed mg amount belongs to the vitamin stock; it is neither the same number
    in grams nor a direct main-medium g/L concentration. Credit the explicit API stock
    g_l declaration separately, preserving its source stage and the 1 mL receiving
    dose. Listed 1 L water does not independently measure final stock volume.","source_stage":"Vitamin
    stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 22 (zero-based)","quote":"<TR><TD WIDTH=75%> Vitamin B<sub>1</sub><sub>2</sub>                                     </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q25","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"200","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"200","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    printed mg amount belongs to the vitamin stock; it is neither the same number
    in grams nor a direct main-medium g/L concentration. Credit the explicit API stock
    g_l declaration separately, preserving its source stage and the 1 mL receiving
    dose. Listed 1 L water does not independently measure final stock volume.","source_stage":"Vitamin
    stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 25 (zero-based)","quote":"<TR><TD WIDTH=75%> Nicotinic acid                                        </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;200.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.62456,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q26","label":"DL--Calcium pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    printed mg amount belongs to the vitamin stock; it is neither the same number
    in grams nor a direct main-medium g/L concentration. Credit the explicit API stock
    g_l declaration separately, preserving its source stage and the 1 mL receiving
    dose. Listed 1 L water does not independently measure final stock volume.","source_stage":"Vitamin
    stock","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 26 (zero-based)","quote":"<TR><TD WIDTH=75%> DL-Calcium pantothenate                              </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[2].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"DL-Calcium pantothenate\",\n                        \"compound_id\":
    1720,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.209864,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q27","label":"Trace element solution SL12B (see below)","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    literal mL stock addition is incorrectly stored as G_PER_L. Preserve its receiving-batch
    amount and named stock; an ML_PER_L denominator also needs an explicit recipe
    basis. The retained preferred_term already names this stock, so replace the Unknown
    solution name without losing that credit.","source_stage":"Main receiving dose","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution SL12B
    (see below)                </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"Trace element solution SL12B\",\n                        \"solution_id\":
    4477,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q28","label":"8% NaHCO3 solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"30","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    literal mL stock addition is incorrectly stored as G_PER_L. Preserve its receiving-batch
    amount and named stock; an ML_PER_L denominator also needs an explicit recipe
    basis. The retained preferred_term already names this stock, so replace the Unknown
    solution name without losing that credit. The source percentage lacks an explicit
    mass/volume, mass/mass or volume/volume basis; do not infer a density or solute
    mass.","source_stage":"Main receiving dose","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 9 (zero-based)","quote":"<TR><TD WIDTH=75%> 8% NaHCO<sub>3</sub> solution                                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;30.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"attribute\": \"8%\",\n                        \"amount\":
    30,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"5%
    Na2S・9H2O solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    literal mL stock addition is incorrectly stored as G_PER_L. Preserve its receiving-batch
    amount and named stock; an ML_PER_L denominator also needs an explicit recipe
    basis. The retained preferred_term already names this stock, so replace the Unknown
    solution name without losing that credit. The source percentage lacks an explicit
    mass/volume, mass/mass or volume/volume basis; do not infer a density or solute
    mass.","source_stage":"Main receiving dose","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 10 (zero-based)","quote":"<TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O
    solution                      </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"attribute\": \"5%\",\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"Vitamin
    solution (see below)","local_fields":[{"path":"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml","field_path":"solutions[3].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    literal mL stock addition is incorrectly stored as G_PER_L. Preserve its receiving-batch
    amount and named stock; an ML_PER_L denominator also needs an explicit recipe
    basis. The retained preferred_term already names this stock, so replace the Unknown
    solution name without losing that credit.","source_stage":"Main receiving dose","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> Vitamin solution (see below)                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Vitamin solution\",\n                        \"solution_id\":
    4478,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q31","label":"Stock water 1","local_fields":[],"decision":"evidence_only","rationale":"The
    source lists 1 L water for this separate stock. Retain as a batch liquid input;
    there is no explicit make-up-to instruction in this JCM stock table.","source_stage":"Separate
    stock water","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 21 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q32","label":"Stock water 2","local_fields":[],"decision":"evidence_only","rationale":"The
    source lists 1 L water for this separate stock. Retain as a batch liquid input;
    there is no explicit make-up-to instruction in this JCM stock table.","source_stage":"Separate
    stock water","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"HTML
    table row 29 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L        </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[2].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q33","label":"JCM default sterilization","local_fields":[],"decision":"evidence_only","rationale":"The
    exact JCM page states 121°C for 15 min unless otherwise stated; preserve this
    source-default provenance with the recipe-specific stock sequencing rather than
    inventing a strain condition.","source_stage":"Source default","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"jcm616.txt
    lines 4-4","quote":"Unless otherwise stated, sterilize media by autoclaving at
    121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q34","label":"Main
    preparation, gas ratio and conditional pH","local_fields":[],"decision":"evidence_only","rationale":"The
    source explicitly separates autoclaving, cooling under N2/CO2 4:1 v/v, sterile
    stock additions, distribution/sealing and conditional pH 7.0–7.2. Neither current
    local document preserves these controls. API midpoint 7.1 must not replace the
    printed range.","source_stage":"Main preparation","sources":[{"evidence_id":"jcm616","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=616","raw_path":"REVIEW_WORK/batch076/source07-08-10/jcm616.raw","raw_sha256":"d60651f69593907ce9e7e5c4e133f7af72e64b186693d099f8b81932696256fb","text_sha256":"b2b443e6c2cabe08851705fa7bf52007b50c9624af3560bc292d7fee0461b3ac","accessed_at":"2026-10-28T19:40:26.263337Z","locator":"jcm616.txt
    lines 49-69","quote":"Mix ingredients and autoclave.  Cool under a N\n2\n-CO\n2\ngas
    mixture (4:1, v/v) and add the following solutions from sterile stocks:\n8% NaHCO\n3\nsolution\n30.0\nml\n5%
    Na\n2\nS·9H\n2\nO solution\n1.0\nml\nVitamin solution (see below)\n1.0\nml\nDistribute
    the medium into culture vessels under the same gas mixture and seal with butyl
    rubber stoppers. Adjust pH to 7.0 - 7.2, if necessary.","quote_basis":"derivative
    text"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Mix ingredients and autoclave. Cool under a N2-CO2 gas mixture (4:1, v/v) and
    add the following solutions from sterile stocks: \"\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ616","reference":"https://mediadive.dsmz.de/rest/medium/J616","raw_path":"REVIEW_WORK/batch076/source07-08-10/apiJ616.raw","raw_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","text_sha256":"4ee12aa5fa985962ad9d2cbe8e3e00286ef24f2752979e4b1ba7c02b17650caa","accessed_at":"2026-10-28T19:40:26.223626Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\":
    \"Distribute the medium into culture vessels under the same gas mixture and seal
    with butyl rubber stoppers. Adjust pH to 7.0 - 7.2, if necessary.\"\n                    }","quote_basis":"raw
    UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/DESULFOMICROBIUM_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: Every asserted ontology and secondary slot was joined to fresh OLS scientific
    objects and exact packaged MIM rows, retaining mapping_status rather than equating
    every row with an accepted mapping. Cobalt/nickel supplied hydrates conflict with
    their primary IDs. The manganese formula remains literally ambiguous in the primary/provider.
    EDTA disodium hydration is unspecified. DL-calcium-pantothenate retains legacy
    000926 with no exact current index membership; D-calcium CHEBI:31345 is not a
    DL substitute. Correct MgSO4 heptahydrate and other matching supplied forms are
    credited; absence of an exact preferred spelling is distinct from absence of an
    asserted identifier.
  target_ids:
  - CultureMech:010025
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: 'All four exact historical reports were read in full, including the two
    explicitly scoped comparison-record reports. October5 zero source-check counts
    are historical limitations, not current checks. The owner’s September water repair
    is credited and the stale generated water is separately identified. Current repair_ingredient/repair_record
    only collapse identical parts; current cleanup does not sum unequal values. Current
    TOGO code separates stock sections, so this legacy flattened output is not proof
    of current flattening. The comparison report’s broad merge recommendation is not
    adopted: the current formulation comparator includes complete scientific fields
    and notes.'
  target_ids:
  - CultureMech:010025
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - historical-object-joins
  - writer-mediadive
  - writer-formulation
  - writer-merger
  - writer-togo
  - writer-repair
  - writer-cleanup
findings:
- finding_id: f1
  issue_key: culturemech-010025-stock-stage-mass
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Stock components and mg amounts were flattened
  description: Restore the exact SL12B and vitamin stock boundaries in the maintained
    owner. The direct ingredient array contains nine SL12B and seven vitamin components;
    fourteen printed mg amounts are stored with the same number as G_PER_L. Preserve
    source batch amounts, explicit provider stock rates and receiving doses as distinct
    claims; do not derive final-medium concentrations from input-water volumes. Resolve
    literal MnCl4·4H2O with authoritative source clarification rather than an assumed
    correction.
  target_ids:
  - CultureMech:010025
  field_paths:
  - ingredients[10]
  - ingredients[25]
  - solutions[0].composition
  - solutions[3].composition
  evidence_ids:
  - jcm616
  - currentTogo625
  - apiJ616
  - quantities
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-010025-water-dose-stale
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Liquid inputs and doses have mass units; target misses owner repair
  description: 'Credit the maintained owner’s September duplicate repair: its water
    is 1.0 while the generated target remains 3.0. Correct the surviving water G_PER_L
    representation and the four stock additions currently expressed as G_PER_L; retain
    the exact source mL amounts and separate stock waters. Review main mass denominators
    explicitly: the primary lists input water while APIJ616 declares 1033 mL and different
    main g_l values. Regenerate only after those maintained-input issues are resolved.'
  target_ids:
  - CultureMech:010025
  field_paths:
  - ingredients[0].concentration
  - ingredients[1].concentration
  - solutions[0].concentration
  - solutions[3].concentration
  evidence_ids:
  - owner
  - target
  - jcm616
  - apiJ616
  - writer-repair
  - quantities
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-010025-supplied-hydrates
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Cobalt and nickel hexahydrates map to anhydrous compounds
  description: The source and both local supplied names specify CoCl2·6H2O and NiCl2·6H2O,
    but primary terms CHEBI:35696 and CHEBI:34887 represent the anhydrous salts. Reconcile
    those exact primary slots using the fresh hexahydrate objects CHEBI:53503 and
    CHEBI:53542 and attach source evidence. Do not extend this correction to the unresolved
    manganese source formula or unspecified EDTA hydration.
  target_ids:
  - CultureMech:010025
  field_paths:
  - ingredients[14].term
  - ingredients[15].term
  evidence_ids:
  - jcm616
  - groundings
  - chebi53503
  - chebi53542
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-010025-preparation-ph
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source preparation and pH context are absent
  description: Preserve the source-specific preparation sequence, gas-phase ratio,
    sterile stock additions, conditional pH range and JCM sterilization default in
    the maintained owner. Current TOGO JSON stores meta.ph, whereas _extract_ph reads
    root ph; repair that exact current parser boundary and preserve comments through
    generation. The existing VARIABLE gas placeholders are truthful unquantified dissolved
    amounts and need no gas-ratio substitution.
  target_ids:
  - CultureMech:010025
  field_paths:
  - preparation_steps
  - ph_range
  - sterilization
  evidence_ids:
  - jcm616
  - currentTogo625
  - writer-togo
  - quantities
  rule_id: review-yaml-record/completeness
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/togo_importer.py
    role: maintained importer
- finding_id: f5
  issue_key: culturemech-010025-classification-names
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Defined formulation and existing stock names are obscured
  description: Review COMPLEX/UNDEFINED against the chemically specified source and
    explicit API complex_medium=no; LIQUID is supported. Replace each Unknown solution
    name from its already-retained preferred_term. Resolve legacy MediaIngredientMech:000926
    only with an exact DL-calcium-pantothenate identity; current CHEBI:31345 explicitly
    describes D stereochemistry and cannot certify the DL supplied form.
  target_ids:
  - CultureMech:010025
  field_paths:
  - medium_type
  - composition_type
  - solutions[0].name
  - solutions[1].name
  - solutions[2].name
  - solutions[3].name
  - ingredients[25].mediaingredientmech_term
  evidence_ids:
  - jcm616
  - apiJ616
  - groundings
  - mim
  rule_id: review-yaml-record/consistency
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml
    role: maintained source
actions:
- action_id: a1
  description: Restore the exact SL12B and vitamin stock boundaries in the maintained
    owner. The direct ingredient array contains nine SL12B and seven vitamin components;
    fourteen printed mg amounts are stored with the same number as G_PER_L. Preserve
    source batch amounts, explicit provider stock rates and receiving doses as distinct
    claims; do not derive final-medium concentrations from input-water volumes. Resolve
    literal MnCl4·4H2O with authoritative source clarification rather than an assumed
    correction.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010025
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml
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
  description: 'Credit the maintained owner’s September duplicate repair: its water
    is 1.0 while the generated target remains 3.0. Correct the surviving water G_PER_L
    representation and the four stock additions currently expressed as G_PER_L; retain
    the exact source mL amounts and separate stock waters. Review main mass denominators
    explicitly: the primary lists input water while APIJ616 declares 1033 mL and different
    main g_l values. Regenerate only after those maintained-input issues are resolved.'
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010025
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml
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
  description: The source and both local supplied names specify CoCl2·6H2O and NiCl2·6H2O,
    but primary terms CHEBI:35696 and CHEBI:34887 represent the anhydrous salts. Reconcile
    those exact primary slots using the fresh hexahydrate objects CHEBI:53503 and
    CHEBI:53542 and attach source evidence. Do not extend this correction to the unresolved
    manganese source formula or unspecified EDTA hydration.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010025
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml
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
  description: Preserve the source-specific preparation sequence, gas-phase ratio,
    sterile stock additions, conditional pH range and JCM sterilization default in
    the maintained owner. Current TOGO JSON stores meta.ph, whereas _extract_ph reads
    root ph; repair that exact current parser boundary and preserve comments through
    generation. The existing VARIABLE gas placeholders are truthful unquantified dissolved
    amounts and need no gas-ratio substitution.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:010025
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/togo_importer.py
    role: maintained importer
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation; src/culturemech/import/togo_importer.py parser
    correction and conservative regeneration
- action_id: a5
  description: Review COMPLEX/UNDEFINED against the chemically specified source and
    explicit API complex_medium=no; LIQUID is supported. Replace each Unknown solution
    name from its already-retained preferred_term. Resolve legacy MediaIngredientMech:000926
    only with an exact DL-calcium-pantothenate identity; current CHEBI:31345 explicitly
    describes D stereochemistry and cannot certify the DL supplied form.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:010025
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M625_Desulfomicrobium_Medium.yaml
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
- MnCl4·4H2O is a literal source ambiguity; this review supplies no guessed manganese
  replacement.
- The distinct MediaDive J616 record appears only in prior comparison context and
  is not an additional curation target.
- The 8% bicarbonate and 5% sulfide stock labels do not state a percentage basis.
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
