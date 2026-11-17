# Scientific review: DESULFOBULBUS MEDIUM WITH LACTATE

- Review: 20261028T190432Z-culturemech-003092-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T18:55:03.402571Z
- Finished UTC: 2026-10-28T19:04:32.322663Z
- Reviewer: Codex batch006_validation (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact JCM749 supports eight declared-basis main rates and retained preparation/pH, but three liquid additions and nineteen stock entries are misrepresented. Correct stock topology and nickel/scoped cobalt hydrates, preserve repaired dependency evidence, and qualify pantothenate specificity.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch075 index 01
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003092 | data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml | generated | desulfobulbus_medium_with_lactate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:003092 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:003092 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:003092 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:003092 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact JCM749 identity and maintained ownership

identity: supported. Targets: CultureMech:003092.

The exact JCM749 title, APIJ749 accession and sole maintained owner agree. JCM187 iron/trace and JCM197 vitamins are scoped stock definitions only; their parent media are not alternative formulations. No strain-growth claim is inferred.

### Retained scientific fields

representation: supported. Targets: CultureMech:003092.

DEFINED/DEFINED and LIQUID are consistent with the named chemical formulation. Both preparation steps and pH 7.2 are supported. The current singleton merge copies maintained scientific fields; it does not establish their source correctness.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:003092.

65 current concentration fields are covered by 59 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b075-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","quantity_field_count":65,"decisions":[{"quantity_id":"q1","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.9703","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.9703","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them.","source_stage":"declared provider main solution","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.9703,\n                        \"mmol_l\": 20.9117,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML table row 0 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt; &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them."}]},{"quantity_id":"q2","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.19802","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.19802","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them.","source_stage":"declared provider main solution","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.19802,\n                        \"mmol_l\": 1.45511,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML table row 1 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt; &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.2&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them."}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.29703","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.29703","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them.","source_stage":"declared provider main solution","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.29703,\n                        \"mmol_l\": 5.553,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML table row 2 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NH&lt;sub&gt;4&lt;/sub&gt;Cl &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.3&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them."}]},{"quantity_id":"q4","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20.7921","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20.7921","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them.","source_stage":"declared provider main solution","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 21,\n                        \"unit\": \"g\",\n                        \"g_l\": 20.7921,\n                        \"mmol_l\": 355.785,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML table row 3 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;21.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them."}]},{"quantity_id":"q5","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[4].concentration","stored":{"value":"3.06931","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[4].concentration","stored":{"value":"3.06931","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them.","source_stage":"declared provider main solution","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 3.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.06931,\n                        \"mmol_l\": 15.0972,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML table row 4 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them."}]},{"quantity_id":"q6","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.49505","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.49505","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them.","source_stage":"declared provider main solution","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.49505,\n                        \"mmol_l\": 6.6405,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML table row 5 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; KCl &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them."}]},{"quantity_id":"q7","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.148515","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.148515","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them.","source_stage":"declared provider main solution","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.148515,\n                        \"mmol_l\": 1.0102,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML table row 6 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.15&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them."}]},{"quantity_id":"q8","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000990099","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000990099","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them.","source_stage":"declared provider main solution","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.000990099,\n                        \"mmol_l\": 0.00431999,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML table row 9 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Resazurin &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The current value exactly matches explicit provider g_l for main solution J749 on its declared 1010 ml computational basis. Preserve that qualified provider rate and exact primary batch mass; primary 910 ml input water does not independently establish measured final volume. No attached field-level claim currently links them."}]},{"quantity_id":"q9","label":"Sodium lactate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[8].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[8].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source number is an ml addition of a separately prepared stock, not g/L of the compound. Retain the exact receiving-batch dose and stock strength separately; 1.0 M lactate is explicit, while 8% bicarbonate and 5% sulfide have unspecified percent bases. Do not invent measured final volume or percentage conversion.","source_stage":"post-cooling stock addition","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Sodium lactate\",\n                        \"compound_id\": 1392,\n                        \"attribute\": \"1.0 M\",\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 1.0 M Sodium lactate solution &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[8].concentration","decision":"correct","rationale":"The source number is an ml addition of a separately prepared stock, not g/L of the compound. Retain the exact receiving-batch dose and stock strength separately; 1.0 M lactate is explicit, while 8% bicarbonate and 5% sulfide have unspecified percent bases. Do not invent measured final volume or percentage conversion."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[8].concentration","decision":"correct","rationale":"The source number is an ml addition of a separately prepared stock, not g/L of the compound. Retain the exact receiving-batch dose and stock strength separately; 1.0 M lactate is explicit, while 8% bicarbonate and 5% sulfide have unspecified percent bases. Do not invent measured final volume or percentage conversion."}]},{"quantity_id":"q10","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[9].concentration","stored":{"value":"60","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[9].concentration","stored":{"value":"60","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source number is an ml addition of a separately prepared stock, not g/L of the compound. Retain the exact receiving-batch dose and stock strength separately; 1.0 M lactate is explicit, while 8% bicarbonate and 5% sulfide have unspecified percent bases. Do not invent measured final volume or percentage conversion.","source_stage":"post-cooling stock addition","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"attribute\": \"*, 8%\",\n                        \"amount\": 60,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML table row 13 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 8% NaHCO&lt;sub&gt;3&lt;/sub&gt; solution* &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;60.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[9].concentration","decision":"correct","rationale":"The source number is an ml addition of a separately prepared stock, not g/L of the compound. Retain the exact receiving-batch dose and stock strength separately; 1.0 M lactate is explicit, while 8% bicarbonate and 5% sulfide have unspecified percent bases. Do not invent measured final volume or percentage conversion."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[9].concentration","decision":"correct","rationale":"The source number is an ml addition of a separately prepared stock, not g/L of the compound. Retain the exact receiving-batch dose and stock strength separately; 1.0 M lactate is explicit, while 8% bicarbonate and 5% sulfide have unspecified percent bases. Do not invent measured final volume or percentage conversion."}]},{"quantity_id":"q11","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[10].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[10].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source number is an ml addition of a separately prepared stock, not g/L of the compound. Retain the exact receiving-batch dose and stock strength separately; 1.0 M lactate is explicit, while 8% bicarbonate and 5% sulfide have unspecified percent bases. Do not invent measured final volume or percentage conversion.","source_stage":"post-cooling stock addition","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"attribute\": \"5%\",\n                        \"amount\": 8,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML table row 14 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O solution &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;8.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml   &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[10].concentration","decision":"correct","rationale":"The source number is an ml addition of a separately prepared stock, not g/L of the compound. Retain the exact receiving-batch dose and stock strength separately; 1.0 M lactate is explicit, while 8% bicarbonate and 5% sulfide have unspecified percent bases. Do not invent measured final volume or percentage conversion."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[10].concentration","decision":"correct","rationale":"The source number is an ml addition of a separately prepared stock, not g/L of the compound. Retain the exact receiving-batch dose and stock strength separately; 1.0 M lactate is explicit, while 8% bicarbonate and 5% sulfide have unspecified percent bases. Do not invent measured final volume or percentage conversion."}]},{"quantity_id":"q12","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source specifies 10 ml of 25% HCl (7.7 M) in the iron stock. Provider 2.5 g_l is not accepted as a conversion of bare25% or as a main-medium amount. Preserve reagent strength, dose, and stock placement without assuming percentage basis/density.","source_stage":"iron stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"7.7 M, 25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 25% HCl (7.7 M)                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The source specifies 10 ml of 25% HCl (7.7 M) in the iron stock. Provider 2.5 g_l is not accepted as a conversion of bare25% or as a main-medium amount. Preserve reagent strength, dose, and stock placement without assuming percentage basis/density."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The source specifies 10 ml of 25% HCl (7.7 M) in the iron stock. Provider 2.5 g_l is not accepted as a conversion of bare25% or as a main-medium amount. Preserve reagent strength, dose, and stock placement without assuming percentage basis/density."}]},{"quantity_id":"q13","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup.","source_stage":"iron stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 17 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q14","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup.","source_stage":"trace stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 19 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnCl&lt;sub&gt;2&lt;/sub&gt;                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;70.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q15","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup.","source_stage":"trace stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q16","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup.","source_stage":"trace stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;6.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q17","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup.","source_stage":"trace stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 22 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;190.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q18","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup.","source_stage":"trace stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[2].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 23 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q19","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup.","source_stage":"trace stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[2].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 24 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;24.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q20","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup.","source_stage":"trace stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[2].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 25 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;36.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q21","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 15 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Biotin                                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q22","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Folic acid                                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q23","label":"Pyridoxine hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 17 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Pyridoxine&amp;#183;HCl                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q24","label":"Thiamine HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 18 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Thiamine&amp;#183;HCl                                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[23].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[23].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q25","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 19 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Riboflavin                                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[24].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[24].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q26","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Nicotinic acid                                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[25].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[25].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q27","label":"Calcium pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0104925,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Calcium pantothenate                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[26].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[26].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q28","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.0001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.0001","unit":"G_PER_L"}}],"decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 0.1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0001,\n                        \"mmol_l\": 7.3779e-5,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 22 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin B&lt;sub&gt;1&lt;/sub&gt;&lt;sub&gt;2&lt;/sub&gt;                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[27].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[27].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q29","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 23 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; &lt;I&gt;p&lt;/I&gt;-Aminobenzoic acid                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[28].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[28].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q30","label":"Lipoic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Lipoic acid\",\n                        \"compound_id\": 368,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.024233,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 24 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Lipoic acid                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[29].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[29].concentration","decision":"correct","rationale":"This current direct ingredient is a stock-recipe entry placed at the main-medium level. The provider g_l is explicitly a stock normalization, not the concentration after the stock dose. Preserve the primary stock batch amount and receiving dose separately. Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q31","label":"iron stock receiving dose","local_fields":[],"decision":"evidence_only","rationale":"Source-only missing structural control: preserve the exact JCM749 batch input and stage. It is not an independent final-volume measurement or a parent JCM187/197 receiving dose.","source_stage":"JCM749 basal","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"solution\": \"FeCl2 solution\",\n                        \"solution_id\": 3846,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeCl&lt;sub&gt;2&lt;/sub&gt; solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;) &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q32","label":"trace stock receiving dose","local_fields":[],"decision":"evidence_only","rationale":"Source-only missing structural control: preserve the exact JCM749 batch input and stage. It is not an independent final-volume measurement or a parent JCM187/197 receiving dose.","source_stage":"JCM749 basal","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 3847,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML table row 8 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;) &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q33","label":"basal water input","local_fields":[],"decision":"evidence_only","rationale":"Source-only missing structural control: preserve the exact JCM749 batch input and stage. It is not an independent final-volume measurement or a parent JCM187/197 receiving dose.","source_stage":"JCM749 basal","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 910,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML table row 10 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;910.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml   &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q34","label":"vitamin stock receiving dose","local_fields":[],"decision":"evidence_only","rationale":"Source-only missing structural control: preserve the exact JCM749 batch input and stage. It is not an independent final-volume measurement or a parent JCM187/197 receiving dose.","source_stage":"JCM749 post-cooling","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\": 3861,\n                        \"attribute\": \"*\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML table row 12 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace vitamins* (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=197\"&gt;197&lt;/a&gt;) &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q35","label":"retained preparation and pH","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"preparation_steps","stored":[{"step_number":1,"action":"AUTOCLAVE","description":"Mix components thoroughly and autoclave under a N2-CO2 (4:1, v/v) gas atmosphere. After cooling, aseptically and anaerobically add the following solutions (autoclaved or *filter-sterilized):"},{"step_number":2,"action":"ADJUST_PH","description":"Adjust pH to 7.1 - 7.4, if necessary."}]},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"preparation_steps","stored":[{"step_number":1,"action":"AUTOCLAVE","description":"Mix components thoroughly and autoclave under a N2-CO2 (4:1, v/v) gas atmosphere. After cooling, aseptically and anaerobically add the following solutions (autoclaved or *filter-sterilized):"},{"step_number":2,"action":"ADJUST_PH","description":"Adjust pH to 7.1 - 7.4, if necessary."}]},{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ph_value","stored":7.2}],"decision":"evidence_only","rationale":"Both existing steps and pH 7.2 are supported by the exact source; 7.2 lies within 7.1–7.4. The first paragraph retains 4:1(v/v), cooling and aseptic/anaerobic addition. Preserve it, but connect its missing following stock table and distinguish filtered vitamin/bicarbonate from autoclaved additions.","source_stage":"main preparation","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\": 12,\n                        \"step\": \"Mix components thoroughly and autoclave under a N2-CO2 (4:1, v/v) gas atmosphere. After cooling, aseptically and anaerobically add the following solutions (autoclaved or *filter-sterilized): \"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\": \"Adjust pH to 7.1 - 7.4, if necessary.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"Complete preparation including following stock table and pH","quote":"Mix components thoroughly and autoclave under a N\n2\n-CO\n2\n(4:1, v/v) gas atmosphere.  After cooling, aseptically and anaerobically add the following solutions (autoclaved or *filter-sterilized):\n1.0 M Sodium lactate solution\n20.0\nml\nTrace vitamins* (see Medium No.\n197\n)\n10.0\nml\n8% NaHCO\n3\nsolution*\n60.0\nml\n5% Na\n2\nS·9H\n2\nO solution\n8.0\nml\nAdjust pH to 7.1 - 7.4, if necessary.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"preparation_steps","decision":"evidence_only","rationale":"Both existing steps and pH 7.2 are supported by the exact source; 7.2 lies within 7.1–7.4. The first paragraph retains 4:1(v/v), cooling and aseptic/anaerobic addition. Preserve it, but connect its missing following stock table and distinguish filtered vitamin/bicarbonate from autoclaved additions."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"preparation_steps","decision":"evidence_only","rationale":"Both existing steps and pH 7.2 are supported by the exact source; 7.2 lies within 7.1–7.4. The first paragraph retains 4:1(v/v), cooling and aseptic/anaerobic addition. Preserve it, but connect its missing following stock table and distinguish filtered vitamin/bicarbonate from autoclaved additions."},{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"Both existing steps and pH 7.2 are supported by the exact source; 7.2 lies within 7.1–7.4. The first paragraph retains 4:1(v/v), cooling and aseptic/anaerobic addition. Preserve it, but connect its missing following stock table and distinguish filtered vitamin/bicarbonate from autoclaved additions."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"Both existing steps and pH 7.2 are supported by the exact source; 7.2 lies within 7.1–7.4. The first paragraph retains 4:1(v/v), cooling and aseptic/anaerobic addition. Preserve it, but connect its missing following stock table and distinguish filtered vitamin/bicarbonate from autoclaved additions."}]},{"quantity_id":"q36","label":"page-wide autoclave control","local_fields":[],"decision":"evidence_only","rationale":"The primary default 121°C for 15 min applies only where autoclaving is specified and no exception is stated. It does not replace the explicit later filtration instructions.","source_stage":"autoclave steps only","sources":[{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"Page-wide default","quote":"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q37","label":"Distilled water scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[0].concentration","stored":{"value":"0.99","unit":"L"}}],"decision":"verified","rationale":"The current scoped water input is supported and already has an exact attached TOGO claim; water input is not final makeup.","source_stage":"JCM187 iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 990,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 18 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[0].concentration","decision":"verified","rationale":"The current scoped water input is supported and already has an exact attached TOGO claim; water input is not final makeup."}]},{"quantity_id":"q38","label":"FeCl2・4H2O scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[1].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 1.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM187 iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"FeCl2・4H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001548\",\n          \"gmo_id\": \"GMO_001548\",\n          \"label\": \"Iron(II) chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 17 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[1].notes","decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording."}]},{"quantity_id":"q39","label":"Distilled water scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"The current scoped water input is supported and already has an exact attached TOGO claim; water input is not final makeup.","source_stage":"JCM187 iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 26 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[0].concentration","decision":"verified","rationale":"The current scoped water input is supported and already has an exact attached TOGO claim; water input is not final makeup."}]},{"quantity_id":"q40","label":"Na2MoO4・2H2O scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 36 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM187 iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 25 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;36.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[1].notes","decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording."}]},{"quantity_id":"q41","label":"H3BO3 scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 6 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM187 iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;6.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[2].notes","decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording."}]},{"quantity_id":"q42","label":"MnCl2・4H2O scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 100 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM187 iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[3].notes","decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording."}]},{"quantity_id":"q43","label":"CoCl2・6H2O scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 190 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM187 iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 22 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;190.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[4].notes","decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording."}]},{"quantity_id":"q44","label":"NiCl2・6H2O scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 24 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM187 iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 24 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;24.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[5].notes","decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording."}]},{"quantity_id":"q45","label":"CuCl2・2H2O scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM187 iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\": \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 23 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[6].notes","decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording."}]},{"quantity_id":"q46","label":"ZnCl2 scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 70 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM187 iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\": \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\": \"GMO_001035\",\n          \"label\": \"Zinc chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 19 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnCl&lt;sub&gt;2&lt;/sub&gt;                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;70.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[7].notes","decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording."}]},{"quantity_id":"q47","label":"Distilled water scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"The current scoped water input is supported and already has an exact attached TOGO claim; water input is not final makeup.","source_stage":"JCM197 vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 25 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[0].concentration","decision":"verified","rationale":"The current scoped water input is supported and already has an exact attached TOGO claim; water input is not final makeup."}]},{"quantity_id":"q48","label":"Biotin scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197 vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 15 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Biotin                                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[1].notes","decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording."}]},{"quantity_id":"q49","label":"p--Aminobenzoic acid scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197 vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 23 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; &lt;I&gt;p&lt;/I&gt;-Aminobenzoic acid                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[2].notes","decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording."}]},{"quantity_id":"q50","label":"Thiamine・HCl scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197 vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\": \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 18 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Thiamine&amp;#183;HCl                                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[3].notes","decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording."}]},{"quantity_id":"q51","label":"Calcium pantothenate scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197 vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\",\n          \"gmo_id\": \"GMO_001028\",\n          \"label\": \"Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Calcium pantothenate                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[4].notes","decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording."}]},{"quantity_id":"q52","label":"Pyridoxine・HCl scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 10 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197 vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 17 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Pyridoxine&amp;#183;HCl                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[5].notes","decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording."}]},{"quantity_id":"q53","label":"Folic acid scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197 vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\": \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Folic acid                                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[6].notes","decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording."}]},{"quantity_id":"q54","label":"Vitamin B12 scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 0.1 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197 vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 22 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin B&lt;sub&gt;1&lt;/sub&gt;&lt;sub&gt;2&lt;/sub&gt;                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[7].notes","decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording."}]},{"quantity_id":"q55","label":"Riboflavin scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[8].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197 vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\": \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 19 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Riboflavin                                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[8].notes","decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording."}]},{"quantity_id":"q56","label":"Nicotinic acid scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[9].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197 vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Nicotinic acid                                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[9].notes","decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording."}]},{"quantity_id":"q57","label":"Lipoic acid scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[10].notes","stored":"Role: Growth factor; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197 vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[10]","quote":"{\n          \"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\": \"GMO_001699\",\n          \"label\": \"Lipoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML table row 24 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Lipoic acid                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[10].notes","decision":"verified","rationale":"The current note correctly retains the source batch mass without asserting g/L. Its attached TOGO excerpt and exact current raw digest authenticate this quantity at the stock stage, not a receiving-medium dose. Source-only API g_l may separately describe the provider stock normalization; it does not invalidate conservative batch-mass wording."}]},{"quantity_id":"q58","label":"HCl reagent dose","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].concentration","stored":{"value":"0.01","unit":"L"}}],"decision":"verified","rationale":"10 ml = 0.01 L is the iron-stock reagent dose. The existing root evidence contains this exact additional excerpt and explicitly names this field; the leading parent-medium dose excerpt is excluded. No 25% basis or mass concentration is inferred.","source_stage":"iron stock reagent addition","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 25% HCl (7.7 M)                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].concentration","decision":"verified","rationale":"10 ml = 0.01 L is the iron-stock reagent dose. The existing root evidence contains this exact additional excerpt and explicitly names this field; the leading parent-medium dose excerpt is excluded. No 25% basis or mass concentration is inferred."}]},{"quantity_id":"q59","label":"HCl reagent strength","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].composition[0].concentration","stored":{"value":"7.7","unit":"MOLAR"}}],"decision":"verified","rationale":"Existing 7.7 M reagent strength and attached exact TOGO evidence are supported. This is neither the stock nor receiving-medium final HCl concentration. The bare25% remains unconverted.","source_stage":"HCl reagent strength","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 25% HCl (7.7 M)                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].composition[0].concentration","decision":"verified","rationale":"Existing 7.7 M reagent strength and attached exact TOGO evidence are supported. This is neither the stock nor receiving-medium final HCl concentration. The bare25% remains unconverted."}]}],"document_scopes":{"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml":null,"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml":null,"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml":["solutions[0].composition","solutions[0].solutions","solutions[1].composition"],"data/normalized_yaml/bacterial/togo_medium_m190.yaml":["solutions[1].composition"]},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:003092.

All asserted scoped ontology objects are current and were checked for supplied salt/hydrate and stereochemical specificity. Neutral resazurin is not relabelled sodium resazurin because these sources say only resazurin. Nickel CHEBI:34887 and scoped M180 cobalt CHEBI:35696 are anhydrous despite explicit hexahydrates. Current CHEBI:53542/53503 support the respective hexahydrates. MIM preferred NiCl2 x 6 H2O and CoCl2 x 6 H2O rows are REJECTED; the distinct preferred Nickel (II) chloride hexahydrate row is MAPPED, so no generic catalogue approval/rejection is inferred. Calcium pantothenate CHEBI:31345 has D stereochemistry, while the recipe gives a generic name: specificity remains unverified. Lipoic acid CHEBI:16494 is non-stereospecific and Vitamin B12 CHEBI:176843 is a vitamer class, consistent with the generic source wording. Exact slot/link coverage is reported separately from chemical validity.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:003092.

All six exact historical reports and selected parent rows were read. October 5 zero-source-check triage is not scientific verification. October 7 J749 69 claims left the record unchanged; exact current API objects/raw digest authenticate the quoted content, not the original access event. Scoped October 8 M180/M190 repairs preserve batch masses, stock water and HCl evidence and deserve explicit credit; other parent-medium claims are excluded. Current parser/cleanup/conservative merger behavior is distinguished from historical execution.

## Findings

### f1: Separate liquid additions and nineteen stock entries

major / open / confirmed; issue key: culturemech-003092-stock-stage-and-dose.

The selected target and owner flatten iron, trace and vitamin stock concentrations into main ingredients and encode 20/60/8 ml additions as g/L. Reconstruct exact JCM749 stocks and receiving-batch doses, including basal water 910 ml and iron/trace 1 ml each; retain the eight explicit provider main g_l values only on the declared 1010 ml basis. Preserve 1.0 M lactate and unspecified 8%/5% bases. Current importer no longer flattens later API stocks but still misses the molar-only lactate row; curate that exact predicate without claiming it caused the old import.

### f2: Correct explicit nickel and scoped cobalt hydrate assertions

major / open / confirmed; issue key: culturemech-003092-hydrate-grounding.

Selected nickel has CHEBI:34887 in both primary and secondary slots, although source NiCl2·6H2O is a hexahydrate. Scoped M180 trace cobalt and nickel similarly retain anhydrous CHEBI:35696/34887. Verify exact hexahydrate terms 53503/53542 against current OLS; preserve the independently supported amounts and current MIM spelling-specific statuses. Selected cobalt 53503 is already correct.

### f3: Attach field and stage evidence while crediting existing stock repairs

minor / open / confirmed; issue key: culturemech-003092-scoped-evidence.

Selected ingredients and preparation lack scoped attached source claims. Attach ingredient claims at ingredients[i].evidence and solution/preparation claims at root evidence with exact field/stage locators. Existing M180/M190 stock notes, water inputs and nested HCl evidence are already supported and must be retained; do not reclassify those repaired quantities as absent evidence. Include the scoped 121°C/15min page default without applying it to filtration.

### f4: Qualify unverified pantothenate stereochemistry

minor / open / provisional; issue key: culturemech-003092-pantothenate-specificity.

The source specifies generic calcium pantothenate while CHEBI:31345 encodes D stereochemistry. Retain the amount and generic source wording; recover exact supplied-form evidence before claiming that specificity or changing identifiers. This is an unresolved specificity limit, not a confirmed wrong-chemical assertion.

## Recommended Actions And Acceptance Checks

### a1

The selected target and owner flatten iron, trace and vitamin stock concentrations into main ingredients and encode 20/60/8 ml additions as g/L. Reconstruct exact JCM749 stocks and receiving-batch doses, including basal water 910 ml and iron/trace 1 ml each; retain the eight explicit provider main g_l values only on the declared 1010 ml basis. Preserve 1.0 M lactate and unspecified 8%/5% bases. Current importer no longer flattens later API stocks but still misses the molar-only lactate row; curate that exact predicate without claiming it caused the old import.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Selected nickel has CHEBI:34887 in both primary and secondary slots, although source NiCl2·6H2O is a hexahydrate. Scoped M180 trace cobalt and nickel similarly retain anhydrous CHEBI:35696/34887. Verify exact hexahydrate terms 53503/53542 against current OLS; preserve the independently supported amounts and current MIM spelling-specific statuses. Selected cobalt 53503 is already correct.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

Selected ingredients and preparation lack scoped attached source claims. Attach ingredient claims at ingredients[i].evidence and solution/preparation claims at root evidence with exact field/stage locators. Existing M180/M190 stock notes, water inputs and nested HCl evidence are already supported and must be retained; do not reclassify those repaired quantities as absent evidence. Include the scoped 121°C/15min page default without applying it to filtration.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

The source specifies generic calcium pantothenate while CHEBI:31345 encodes D stereochemistry. Retain the amount and generic source wording; recover exact supplied-form evidence before claiming that specificity or changing identifiers. This is an unresolved specificity limit, not a confirmed wrong-chemical assertion.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| jcm749 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749; REVIEW_WORK/batch075/source01-03-supplement/jcm749.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| apiJ749 | https://mediadive.dsmz.de/rest/medium/J749; REVIEW_WORK/batch075/source01-03-supplement/apiJ749.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| jcm187 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187; REVIEW_WORK/batch075/validation-authors/jcm187-metadata-adapter.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh batch075 capture shared from publisher with original access metadata; only exact named stock sections apply, parent-medium doses and conditions excluded. |
| jcm197 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; REVIEW_WORK/batch075/validation-authors/jcm197-metadata-adapter.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh batch075 capture shared from publisher with original access metadata; only exact named stock sections apply, parent-medium doses and conditions excluded. |
| togo180 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180; REVIEW_WORK/batch075/validation-authors/togo180-metadata-adapter.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh batch075 capture shared from publisher with original access metadata; only exact named stock sections apply, parent-medium doses and conditions excluded. |
| togo190 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; REVIEW_WORK/batch075/validation-authors/togo190-metadata-adapter.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh batch075 capture shared from publisher with original access metadata; only exact named stock sections apply, parent-medium doses and conditions excluded. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542; REVIEW_WORK/batch075/source01-03-supplement/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; REVIEW_WORK/batch075/source01-03-supplement/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| target | data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-18 | reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-19 | reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/desulfobulbus_medium_with_lactate.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-20 | reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-21 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-22 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/togo_medium_m190.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch075/record01/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch075/record01/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch075/record01/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| writer-togo | src/culturemech/import/togo_importer.py; _extract_primary_components; _solution_from_item; _local_batch_volume_ml; _parse_unit; _extract_ph; _extract_preparation_steps | context_only | Current _extract_primary_components separates named local stocks; _solution_from_item retains a local stock without composition if its basis is insufficient. _parse_unit now maps mg to MG_PER_L and ml to ML_PER_L, but bare g still becomes G_PER_L and bare percent becomes PERCENT_W_V without independently proving final volume or percent basis. _extract_ph reads root ph, while these API payloads provide meta.ph. _extract_preparation_steps retains comments but its classifier checks autoclave before filtration and does not split mixed-process paragraphs. These are current behaviors, not proof of historical execution. |
| writer-cleanup | scripts/cleanup_media_quality.py; MediaQualityFixer._merge_ingredient_group | context_only | Current _merge_ingredient_group keeps identical duplicate amounts and flags disagreements; it no longer sums duplicate quantities. It cannot establish compatible stock/main bases or repair a historical flattened sum. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; MediaDiveImporter._parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _normalize_unit | context_only | Current _parse_api_composition reads only the first solution, excludes water and rows classified as stock additions, and prefers explicit g_l. _parse_api_solutions preserves references/percent-labelled additions. _is_api_stock_addition recognizes solution_id or an ml row with a percentage attribute, but not a molar-only attribute such as 1.0 M lactate. _normalize_unit preserves mg/ml dimensions as per-litre enums without establishing a denominator. This is current code behavior, not proof of historical execution. |
| stock180 | data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml; solutions[0].composition/solutions[0].solutions (iron if scoped); solutions[1].composition | context_only | Only JCM187 iron/trace definitions named by the selected source; parent receiving doses, medium ingredients and preparation are excluded. |
| stock190 | data/normalized_yaml/bacterial/togo_medium_m190.yaml; solutions[1].composition | context_only | Only JCM197 trace-vitamin stock. M190 is the TOGO namespace counterpart, not JCM medium190. Parent receiving doses and trace-mineral stock are excluded. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149; REVIEW_WORK/batch075/source01-03-supplement/chebi32149.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; REVIEW_WORK/batch075/source01-03-supplement/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch075/source01-03-supplement/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch075/source01-03-supplement/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; REVIEW_WORK/batch075/source01-03-supplement/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; REVIEW_WORK/batch075/source01-03-supplement/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158; REVIEW_WORK/batch075/source01-03-supplement/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; REVIEW_WORK/batch075/source01-03-supplement/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75228 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75228; REVIEW_WORK/batch075/source01-03-supplement/chebi75228.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139; REVIEW_WORK/batch075/source01-03-supplement/chebi32139.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209; REVIEW_WORK/batch075/source01-03-supplement/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883; REVIEW_WORK/batch075/source01-03-supplement/chebi17883.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249; REVIEW_WORK/batch075/source01-03-supplement/chebi86249.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976; REVIEW_WORK/batch075/source01-03-supplement/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; REVIEW_WORK/batch075/source01-03-supplement/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch075/source01-03-supplement/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; REVIEW_WORK/batch075/source01-03-supplement/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; REVIEW_WORK/batch075/source01-03-supplement/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch075/source01-03-supplement/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956; REVIEW_WORK/batch075/source01-03-supplement/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470; REVIEW_WORK/batch075/source01-03-supplement/chebi27470.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961; REVIEW_WORK/batch075/source01-03-supplement/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105; REVIEW_WORK/batch075/source01-03-supplement/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015; REVIEW_WORK/batch075/source01-03-supplement/chebi17015.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940; REVIEW_WORK/batch075/source01-03-supplement/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345; REVIEW_WORK/batch075/source01-03-supplement/chebi31345.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843; REVIEW_WORK/batch075/source01-03-supplement/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753; REVIEW_WORK/batch075/source01-03-supplement/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494; REVIEW_WORK/batch075/source01-03-supplement/chebi16494.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377; REVIEW_WORK/batch075/source01-03-supplement/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:35696; REVIEW_WORK/batch075/source01-03-supplement/chebi35696.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| quantities | REVIEW_WORK/batch075/record01/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch075/record01/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch075/record01/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch075/record01/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch075/record01/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch075/record01/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch075/record01/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| historical-source-joins | REVIEW_WORK/batch075/record01/historical-source-joins.json; Every literal/decoded historical source-object row and exact current-source match | context_only | Historical quoted source content and raw-digest equality where actually matched; independent of attached local claims and original access-event recovery. |
| check-schema | REVIEW_WORK/batch075/record01/validate-schema.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch075/record01/validate-strict.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch075/record01/validate-terms.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch075/record01/validate-references.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Calcium pantothenate stereochemistry remains unverified; provider mmol_l conversions and catalog synonym chemistry are not blanket certified. Parent M180/M190 receiving doses, main-medium conditions and unrelated compounds are outside scope.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T190432Z-culturemech-003092-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: DESULFOBULBUS MEDIUM WITH LACTATE'
started_at: '2026-10-28T18:55:03.402571Z'
finished_at: '2026-10-28T19:04:32.322663Z'
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
summary: Exact JCM749 supports eight declared-basis main rates and retained preparation/pH,
  but three liquid additions and nineteen stock entries are misrepresented. Correct
  stock topology and nickel/scoped cobalt hydrates, preserve repaired dependency evidence,
  and qualify pantothenate specificity.
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
  - path: data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml
    sha256: 113c9d6d45940c3591718a810d7a57a5fc1c584e85f1ed59fb6ceac105f4ba2f
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
    role: context
  - path: data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml
    sha256: 8cf1804e13ad18dbc6036abd7b2ee11cf73185857ab7c6a00fa26f30d22217e4
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/desulfobulbus_medium_with_lactate.yaml.md
    sha256: e3c85400f7895329781ebaab82d4113a6a12c1a3ccd22a47154d1f0d19e1d4c2
    role: context
  - path: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/plan.json
    sha256: 00113dc0b556486b52084f2508b061b9a188423d479f8aa102511ec55074ebd5
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.md
    sha256: 34cd57ce0a2eb510be3a43e9ee8014090111ab3f3c4eefe7e16adcef707f9343
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/togo_medium_m190.md
    sha256: 4ee172b59b8f9a19921c300ecf394dc632e301c0f375a6e86adfade6ec86a619
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.md
    sha256: f7fa9416148a602515b571aedb11d7794ccdd4b2cce57bed8b84b78fc355a46e
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.md
    sha256: 528acbfbf6f6d4b6637f53a91efb96869ec282f1c1c4d496751afad27a902c61
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md
    sha256: d29c2d8798f20259a253d2b17745d675b4a789de94bdcef5279332d086383022
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
  selection: Authoritative batch075 index 01
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003092
targets:
- target_id: CultureMech:003092
  path: data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml
  label: desulfobulbus_medium_with_lactate
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml
    role: maintained normalized contributor
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:003092
  command: just validate-schema data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml
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
  - CultureMech:003092
  command: just validate-strict data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml
    --out REVIEW_WORK/batch075/record01/strict.tsv --workers 1 --quiet
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
  - CultureMech:003092
  command: just validate-terms data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml
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
  - CultureMech:003092
  command: just validate-references data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: jcm749
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749
  accessed_at: '2026-10-28T18:55:35.358203Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/jcm749.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31
- evidence_id: apiJ749
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J749
  accessed_at: '2026-10-28T18:55:35.305313Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/apiJ749.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf
- evidence_id: jcm187
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187
  accessed_at: '2026-10-28T18:56:03.575661Z'
  locator: REVIEW_WORK/batch075/validation-authors/jcm187-metadata-adapter.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh batch075 capture shared from publisher with
    original access metadata; only exact named stock sections apply, parent-medium
    doses and conditions excluded.
  snapshot_sha256: e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804
- evidence_id: jcm197
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  accessed_at: '2026-10-28T18:56:04.601366Z'
  locator: REVIEW_WORK/batch075/validation-authors/jcm197-metadata-adapter.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh batch075 capture shared from publisher with
    original access metadata; only exact named stock sections apply, parent-medium
    doses and conditions excluded.
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: togo180
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180
  accessed_at: '2026-10-28T18:56:05.236822Z'
  locator: REVIEW_WORK/batch075/validation-authors/togo180-metadata-adapter.json;
    exact original raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh batch075 capture shared from publisher with
    original access metadata; only exact named stock sections apply, parent-medium
    doses and conditions excluded.
  snapshot_sha256: a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba
- evidence_id: togo190
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  accessed_at: '2026-10-28T18:56:05.258322Z'
  locator: REVIEW_WORK/batch075/validation-authors/togo190-metadata-adapter.json;
    exact original raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh batch075 capture shared from publisher with
    original access metadata; only exact named stock sections apply, parent-medium
    doses and conditions excluded.
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542
  accessed_at: '2026-10-28T18:55:43.326276Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi53542.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1e44a068cfe6b98d7bb3b0240ffdc0611e1be59f2d3dab9f04e4162ed94e4444
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503
  accessed_at: '2026-10-28T18:55:43.327411Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi53503.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: a626d2aa210aafd9572221d4893cd206310d5df507e474e1528997048f522250
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml
  locator: Complete file
  accessed_at: '2026-10-28T19:04:32.092392Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 113c9d6d45940c3591718a810d7a57a5fc1c584e85f1ed59fb6ceac105f4ba2f
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml
  locator: Complete file
  accessed_at: '2026-10-28T19:04:32.092550Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 8cf1804e13ad18dbc6036abd7b2ee11cf73185857ab7c6a00fa26f30d22217e4
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T19:04:32.092575Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T19:04:32.092869Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T19:04:32.092892Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T19:04:32.092912Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T19:04:32.092936Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 1db6b2b69fb7a9a131c95c22d837d6a4c5f10dab810921069496169a06d6f5c2
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/desulfobulbus_medium_with_lactate.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T19:04:32.098008Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: e3c85400f7895329781ebaab82d4113a6a12c1a3ccd22a47154d1f0d19e1d4c2
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T19:04:32.098072Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 00113dc0b556486b52084f2508b061b9a188423d479f8aa102511ec55074ebd5
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.md
  locator: Complete report
  accessed_at: '2026-10-28T19:04:32.098498Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 34cd57ce0a2eb510be3a43e9ee8014090111ab3f3c4eefe7e16adcef707f9343
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/togo_medium_m190.md
  locator: Complete report
  accessed_at: '2026-10-28T19:04:32.098527Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 4ee172b59b8f9a19921c300ecf394dc632e301c0f375a6e86adfade6ec86a619
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T19:04:32.098551Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: f7fa9416148a602515b571aedb11d7794ccdd4b2cce57bed8b84b78fc355a46e
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.md
  locator: Complete report
  accessed_at: '2026-10-28T19:04:32.098576Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 528acbfbf6f6d4b6637f53a91efb96869ec282f1c1c4d496751afad27a902c61
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md
  locator: Complete report
  accessed_at: '2026-10-28T19:04:32.098604Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: d29c2d8798f20259a253d2b17745d675b4a789de94bdcef5279332d086383022
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch075/record01/historical-reading.json
  accessed_at: '2026-10-28T19:04:32.098634Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 7e204111fbb86974f6bbdaf348ac0bc55af292f66d621fedd87203a0a5d262bb
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch075/record01/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T19:04:32.098892Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 68b4f7b72b5ed25a9430f7c9b194a4701ae9298e7ffc6be2adfda24bbf0b7bc9
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch075/record01/complete-document-reader.json
  accessed_at: '2026-10-28T19:04:32.099261Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: df2aead8366750f3e928097b06efb66d7f08c6c66d35fceae6d4422402d8e672
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T19:04:32.099544Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_primary_components; _solution_from_item; _local_batch_volume_ml;
    _parse_unit; _extract_ph; _extract_preparation_steps
  accessed_at: '2026-10-28T19:04:32.099571Z'
  support: context_only
  summary: Current _extract_primary_components separates named local stocks; _solution_from_item
    retains a local stock without composition if its basis is insufficient. _parse_unit
    now maps mg to MG_PER_L and ml to ML_PER_L, but bare g still becomes G_PER_L and
    bare percent becomes PERCENT_W_V without independently proving final volume or
    percent basis. _extract_ph reads root ph, while these API payloads provide meta.ph.
    _extract_preparation_steps retains comments but its classifier checks autoclave
    before filtration and does not split mixed-process paragraphs. These are current
    behaviors, not proof of historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: MediaQualityFixer._merge_ingredient_group
  accessed_at: '2026-10-28T19:04:32.099612Z'
  support: context_only
  summary: Current _merge_ingredient_group keeps identical duplicate amounts and flags
    disagreements; it no longer sums duplicate quantities. It cannot establish compatible
    stock/main bases or repair a historical flattened sum.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: MediaDiveImporter._parse_api_composition; _is_api_stock_addition; _parse_api_solutions;
    _normalize_unit
  accessed_at: '2026-10-28T19:04:32.099639Z'
  support: context_only
  summary: Current _parse_api_composition reads only the first solution, excludes
    water and rows classified as stock additions, and prefers explicit g_l. _parse_api_solutions
    preserves references/percent-labelled additions. _is_api_stock_addition recognizes
    solution_id or an ml row with a percentage attribute, but not a molar-only attribute
    such as 1.0 M lactate. _normalize_unit preserves mg/ml dimensions as per-litre
    enums without establishing a denominator. This is current code behavior, not proof
    of historical execution.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: stock180
  kind: record_content
  reference: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
  locator: solutions[0].composition/solutions[0].solutions (iron if scoped); solutions[1].composition
  accessed_at: '2026-10-28T19:04:32.143086Z'
  support: context_only
  summary: Only JCM187 iron/trace definitions named by the selected source; parent
    receiving doses, medium ingredients and preparation are excluded.
  snapshot_sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
- evidence_id: stock190
  kind: record_content
  reference: data/normalized_yaml/bacterial/togo_medium_m190.yaml
  locator: solutions[1].composition
  accessed_at: '2026-10-28T19:04:32.143170Z'
  support: context_only
  summary: Only JCM197 trace-vitamin stock. M190 is the TOGO namespace counterpart,
    not JCM medium190. Parent receiving doses and trace-mineral stock are excluded.
  snapshot_sha256: b1924e7eb436d56c5bd4826f07cafff130341054acfd808fb1c9e5bca914e3fa
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149
  accessed_at: '2026-10-28T18:55:41.464122Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi32149.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 96b73aef765e4edc893460a376cfedd136930f253bbeac639827b1daddb65d71
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  accessed_at: '2026-10-28T18:55:43.321302Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi63036.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  accessed_at: '2026-10-28T18:55:40.854422Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi31206.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  accessed_at: '2026-10-28T18:55:40.160956Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi26710.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345
  accessed_at: '2026-10-28T18:55:45.225062Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi86345.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 94b600ced6e98743e2d1b02c73e1756f8f81b639407a8fdd080c96d8fa563c70
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  accessed_at: '2026-10-28T18:55:42.007602Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi32588.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158
  accessed_at: '2026-10-28T18:55:44.532538Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi86158.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: eacf58308fa876cb17661b82d08a64d9be24814fde8014ac82da7696b3684841
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806
  accessed_at: '2026-10-28T18:55:45.219334Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi8806.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f2530ec9c15f59a3d132a466c9c3a899497bab0f85b996d3e27bef8612f89982
- evidence_id: chebi75228
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75228
  accessed_at: '2026-10-28T18:55:43.930231Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi75228.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 02869dcf8cd74aa7f8b975f2590e5bdbd4512df6c748979a72d5337751ae5774
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139
  accessed_at: '2026-10-28T18:55:41.437028Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi32139.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 51709e2510736d0b63369147b10ec6ffe80d5d5c3a40605381de9b3ed78634c3
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209
  accessed_at: '2026-10-28T18:55:44.456870Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi76209.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4896ec517123ebeb1afcbac7bc30a7103976f03891af0c86c992196b5f0db969
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883
  accessed_at: '2026-10-28T18:55:39.682097Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi17883.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e5ab164ef9ff955da1a504ca34ab4d3b69539d9bf721936c9dd563ccbbd0e3b0
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249
  accessed_at: '2026-10-28T18:55:44.578308Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi86249.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4d7f48f88badcba85a62e59842c6ec921f5478eb76695098b17847ed62c8530a
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976
  accessed_at: '2026-10-28T18:55:43.254967Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi49976.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d3bdc4c6f01d01422fafe433df4e4011e01cf7e55e0329ab341a60ece780946f
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  accessed_at: '2026-10-28T18:55:45.221456Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi86368.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  accessed_at: '2026-10-28T18:55:42.067236Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi33118.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318
  accessed_at: '2026-10-28T18:55:45.229921Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi86318.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: bd88e1499f370a9f474b29fa7a9a83aa5c42c69d0b6772ece8c89d646dfda8d8
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  accessed_at: '2026-10-28T18:55:42.629892Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi34887.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 3a37ef35991d24faf578286a7d7557ee1b0646c286dd3f8a555d833e6bf82a57
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  accessed_at: '2026-10-28T18:55:43.920444Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi75213.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956
  accessed_at: '2026-10-28T18:55:38.978288Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi15956.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 5135a39e8b52c878896db22443f00507125db80e5ce4bb1dcc97914b9bdd7316
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470
  accessed_at: '2026-10-28T18:55:40.276650Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi27470.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e1820a7a704794fa20995eea5037e03c2b22b847817c28bb2f45f80762c275d1
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961
  accessed_at: '2026-10-28T18:55:40.797121Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi30961.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 855ea2cf0e89d25ab4a560ab1c2dab6ac861d215bc5473cb4d3a0a2d4cdff438
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105
  accessed_at: '2026-10-28T18:55:42.708607Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi49105.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f9dbae8cd2dcbd38d914abb99730e341ff280d3a44f20f95b2663e47664780cf
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015
  accessed_at: '2026-10-28T18:55:39.561648Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi17015.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 17f7ac7c03d75b85a96f951321902906266f3ce8fa44faea4814fac46560e3e6
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940
  accessed_at: '2026-10-28T18:55:38.833836Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi15940.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: c291a1c1bb0d6af05ac4005af0957534f430db47e7df9cec874f8a94d961dba1
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345
  accessed_at: '2026-10-28T18:55:40.879626Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi31345.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: c3341e7cf8a7ea0768d505265376c1514f161c9048b6e878314e204341d702eb
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843
  accessed_at: '2026-10-28T18:55:39.575252Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi176843.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9c73ea31864abce6b9ed6328e9ed491bc1cad2ba27f40adb5c00f0f192838e63
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753
  accessed_at: '2026-10-28T18:55:40.801873Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi30753.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1340e054634ce960494b9388f6e3fd231d9e7d66969c3c11932ee2058171fd2c
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494
  accessed_at: '2026-10-28T18:55:39.014241Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi16494.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 192c51f672f633c6071a3397d5785fb2bca6eaf8f9b787f7aaaa6c2aeb3b1a2f
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377
  accessed_at: '2026-10-28T18:55:38.386363Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi15377.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: a5ab66402b598c137daa8e5c8ba95811f1619db3e0f8b4f9bd0214161bafa0fe
- evidence_id: chebi35696
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:35696
  accessed_at: '2026-10-28T18:55:42.703221Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi35696.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 22f49067d1405baa8e2bbd7c4405035d8663c69aa045b7bbacf363bb30729244
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch075/record01/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:04:32.320357Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 520bfa7588f7a21df36ce1f4561df1ef23fd681109fa003aca64b216a5889076
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch075/record01/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:04:32.320490Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 4178fbe2b1b8a05538f18d71aca740441972a2cfd1a8ede71af66df3f4c63560
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch075/record01/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:04:32.320668Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: c16095852806cd2a8de81ee5dd61dfd55268ba03d09ad1b04d686320697e5f17
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch075/record01/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:04:32.320842Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 3d9802ddcdbac9967d182256251349fb85c3fcc3e0ca6bf12e73c46226f7550d
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch075/record01/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:04:32.320997Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: e6d3c2b2025488a23d7ba9e6d0c0080c35a77509aca111d8a5c9d295da217b1a
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch075/record01/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:04:32.321039Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 17339da8dc730f0001feefac6fa8e0d497db8f506757fb406d5a9ce7adc99b6d
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch075/record01/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:04:32.321061Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 81e0455a9e8f315380b9b65f0cec0f2327511c4346659e424ffe7ffb9a6e663d
- evidence_id: historical-source-joins
  kind: record_content
  reference: REVIEW_WORK/batch075/record01/historical-source-joins.json
  locator: Every literal/decoded historical source-object row and exact current-source
    match
  accessed_at: '2026-10-28T19:04:32.321095Z'
  support: context_only
  summary: Historical quoted source content and raw-digest equality where actually
    matched; independent of attached local claims and original access-event recovery.
  snapshot_sha256: a2dab26b3d0c3876e92f366f22ff05e83ab3fb95346ba855b91d01439573bbd6
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch075/record01/validate-schema.json
  accessed_at: '2026-10-28T18:55:04.749758Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 813ff90895f247e7fc8300e0e6cc272208cec39fbcf929963e593d5a0f7b0dc6
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch075/record01/validate-strict.json
  accessed_at: '2026-10-28T18:55:05.841343Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 68092ec6b435497edc620bb5a29d7e8a12f7dae6f2da1ea41477309279bdefd7
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch075/record01/validate-terms.json
  accessed_at: '2026-10-28T18:55:07.525832Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 1f375e4c548ce45349734b8086dca2fa11fd6479662c223befac5bb8ffa8d8eb
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch075/record01/validate-references.json
  accessed_at: '2026-10-28T18:55:08.473131Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: f420701a9edde9fc8ac615e9f7f9f39e632553cea52bffed7319a7cc91039fc1
assessments:
- assessment_id: identity
  area: identity
  topic: Exact JCM749 identity and maintained ownership
  outcome: supported
  summary: The exact JCM749 title, APIJ749 accession and sole maintained owner agree.
    JCM187 iron/trace and JCM197 vitamins are scoped stock definitions only; their
    parent media are not alternative formulations. No strain-growth claim is inferred.
  target_ids:
  - CultureMech:003092
  evidence_ids:
  - target
  - owner
  - jcm749
  - apiJ749
- assessment_id: representation
  area: representation
  topic: Retained scientific fields
  outcome: supported
  summary: DEFINED/DEFINED and LIQUID are consistent with the named chemical formulation.
    Both preparation steps and pH 7.2 are supported. The current singleton merge copies
    maintained scientific fields; it does not establish their source correctness.
  target_ids:
  - CultureMech:003092
  evidence_ids:
  - target
  - jcm749
  - writer-merger
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 65 current concentration fields are covered by 59 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:003092
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b075-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","quantity_field_count":65,"decisions":[{"quantity_id":"q1","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.9703","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.9703","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them.","source_stage":"declared provider main solution","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.9703,\n                        \"mmol_l\":
    20.9117,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML
    table row 0 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>SO<sub>4</sub>
    </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them."}]},{"quantity_id":"q2","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.19802","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.19802","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them.","source_stage":"declared provider main solution","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.19802,\n                        \"mmol_l\":
    1.45511,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML
    table row 1 (zero-based)","quote":"<TR><TD WIDTH=75%> KH<sub>2</sub>PO<sub>4</sub>
    </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.2&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them."}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.29703","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.29703","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them.","source_stage":"declared provider main solution","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.29703,\n                        \"mmol_l\":
    5.553,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML
    table row 2 (zero-based)","quote":"<TR><TD WIDTH=75%> NH<sub>4</sub>Cl </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.3&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them."}]},{"quantity_id":"q4","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20.7921","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20.7921","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them.","source_stage":"declared provider main solution","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 21,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 20.7921,\n                        \"mmol_l\":
    355.785,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML
    table row 3 (zero-based)","quote":"<TR><TD WIDTH=75%> NaCl </TD><TD WIDTH=15%
    ALIGN=RIGHT><font size=+1><tt>&nbsp;21.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them."}]},{"quantity_id":"q5","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[4].concentration","stored":{"value":"3.06931","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[4].concentration","stored":{"value":"3.06931","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them.","source_stage":"declared provider main solution","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 3.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.06931,\n                        \"mmol_l\":
    15.0972,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML
    table row 4 (zero-based)","quote":"<TR><TD WIDTH=75%> MgCl<sub>2</sub>&#183;6H<sub>2</sub>O
    </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them."}]},{"quantity_id":"q6","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.49505","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.49505","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them.","source_stage":"declared provider main solution","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.49505,\n                        \"mmol_l\":
    6.6405,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML
    table row 5 (zero-based)","quote":"<TR><TD WIDTH=75%> KCl </TD><TD WIDTH=15% ALIGN=RIGHT><font
    size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10% ALIGN=RIGHT>
    g  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them."}]},{"quantity_id":"q7","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.148515","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.148515","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them.","source_stage":"declared provider main solution","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.148515,\n                        \"mmol_l\":
    1.0102,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML
    table row 6 (zero-based)","quote":"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O
    </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.15&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them."}]},{"quantity_id":"q8","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000990099","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000990099","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them.","source_stage":"declared provider main solution","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\":
    25,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.000990099,\n                        \"mmol_l\":
    0.00431999,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML
    table row 9 (zero-based)","quote":"<TR><TD WIDTH=75%> Resazurin </TD><TD WIDTH=15%
    ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"The
    current value exactly matches explicit provider g_l for main solution J749 on
    its declared 1010 ml computational basis. Preserve that qualified provider rate
    and exact primary batch mass; primary 910 ml input water does not independently
    establish measured final volume. No attached field-level claim currently links
    them."}]},{"quantity_id":"q9","label":"Sodium lactate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[8].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[8].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source number is an ml addition of a separately prepared stock, not g/L of the
    compound. Retain the exact receiving-batch dose and stock strength separately;
    1.0 M lactate is explicit, while 8% bicarbonate and 5% sulfide have unspecified
    percent bases. Do not invent measured final volume or percentage conversion.","source_stage":"post-cooling
    stock addition","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Sodium lactate\",\n                        \"compound_id\":
    1392,\n                        \"attribute\": \"1.0 M\",\n                        \"amount\":
    20,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> 1.0 M Sodium lactate solution
    </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[8].concentration","decision":"correct","rationale":"The
    source number is an ml addition of a separately prepared stock, not g/L of the
    compound. Retain the exact receiving-batch dose and stock strength separately;
    1.0 M lactate is explicit, while 8% bicarbonate and 5% sulfide have unspecified
    percent bases. Do not invent measured final volume or percentage conversion."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[8].concentration","decision":"correct","rationale":"The
    source number is an ml addition of a separately prepared stock, not g/L of the
    compound. Retain the exact receiving-batch dose and stock strength separately;
    1.0 M lactate is explicit, while 8% bicarbonate and 5% sulfide have unspecified
    percent bases. Do not invent measured final volume or percentage conversion."}]},{"quantity_id":"q10","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[9].concentration","stored":{"value":"60","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[9].concentration","stored":{"value":"60","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source number is an ml addition of a separately prepared stock, not g/L of the
    compound. Retain the exact receiving-batch dose and stock strength separately;
    1.0 M lactate is explicit, while 8% bicarbonate and 5% sulfide have unspecified
    percent bases. Do not invent measured final volume or percentage conversion.","source_stage":"post-cooling
    stock addition","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"attribute\": \"*, 8%\",\n                        \"amount\":
    60,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML
    table row 13 (zero-based)","quote":"<TR><TD WIDTH=75%> 8% NaHCO<sub>3</sub> solution*
    </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;60.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[9].concentration","decision":"correct","rationale":"The
    source number is an ml addition of a separately prepared stock, not g/L of the
    compound. Retain the exact receiving-batch dose and stock strength separately;
    1.0 M lactate is explicit, while 8% bicarbonate and 5% sulfide have unspecified
    percent bases. Do not invent measured final volume or percentage conversion."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[9].concentration","decision":"correct","rationale":"The
    source number is an ml addition of a separately prepared stock, not g/L of the
    compound. Retain the exact receiving-batch dose and stock strength separately;
    1.0 M lactate is explicit, while 8% bicarbonate and 5% sulfide have unspecified
    percent bases. Do not invent measured final volume or percentage conversion."}]},{"quantity_id":"q11","label":"Na2S
    x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[10].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[10].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source number is an ml addition of a separately prepared stock, not g/L of the
    compound. Retain the exact receiving-batch dose and stock strength separately;
    1.0 M lactate is explicit, while 8% bicarbonate and 5% sulfide have unspecified
    percent bases. Do not invent measured final volume or percentage conversion.","source_stage":"post-cooling
    stock addition","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"attribute\": \"5%\",\n                        \"amount\":
    8,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML
    table row 14 (zero-based)","quote":"<TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O
    solution </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;8.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml   </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[10].concentration","decision":"correct","rationale":"The
    source number is an ml addition of a separately prepared stock, not g/L of the
    compound. Retain the exact receiving-batch dose and stock strength separately;
    1.0 M lactate is explicit, while 8% bicarbonate and 5% sulfide have unspecified
    percent bases. Do not invent measured final volume or percentage conversion."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[10].concentration","decision":"correct","rationale":"The
    source number is an ml addition of a separately prepared stock, not g/L of the
    compound. Retain the exact receiving-batch dose and stock strength separately;
    1.0 M lactate is explicit, while 8% bicarbonate and 5% sulfide have unspecified
    percent bases. Do not invent measured final volume or percentage conversion."}]},{"quantity_id":"q12","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source specifies 10 ml of 25% HCl (7.7 M) in the iron stock. Provider 2.5 g_l
    is not accepted as a conversion of bare25% or as a main-medium amount. Preserve
    reagent strength, dose, and stock placement without assuming percentage basis/density.","source_stage":"iron
    stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"7.7 M, 25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> 25% HCl (7.7 M)                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The
    source specifies 10 ml of 25% HCl (7.7 M) in the iron stock. Provider 2.5 g_l
    is not accepted as a conversion of bare25% or as a main-medium amount. Preserve
    reagent strength, dose, and stock placement without assuming percentage basis/density."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The
    source specifies 10 ml of 25% HCl (7.7 M) in the iron stock. Provider 2.5 g_l
    is not accepted as a conversion of bare25% or as a main-medium amount. Preserve
    reagent strength, dose, and stock placement without assuming percentage basis/density."}]},{"quantity_id":"q13","label":"FeCl2
    x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup.","source_stage":"iron
    stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 17 (zero-based)","quote":"<TR><TD WIDTH=75%> FeCl<sub>2</sub>&#183;4H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q14","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup.","source_stage":"trace
    stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 19 (zero-based)","quote":"<TR><TD WIDTH=75%> ZnCl<sub>2</sub>                                               </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;70.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q15","label":"MnCl2
    x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup.","source_stage":"trace
    stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 20 (zero-based)","quote":"<TR><TD WIDTH=75%> MnCl<sub>2</sub>&#183;4H<sub>2</sub>O                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q16","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup.","source_stage":"trace
    stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 21 (zero-based)","quote":"<TR><TD WIDTH=75%> H<sub>3</sub>BO<sub>3</sub>                                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;6.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q17","label":"CoCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup.","source_stage":"trace
    stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 22 (zero-based)","quote":"<TR><TD WIDTH=75%> CoCl<sub>2</sub>&#183;6H<sub>2</sub>O                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;190.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q18","label":"CuCl2
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup.","source_stage":"trace
    stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[2].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 23 (zero-based)","quote":"<TR><TD WIDTH=75%> CuCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q19","label":"NiCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup.","source_stage":"trace
    stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[2].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 24 (zero-based)","quote":"<TR><TD WIDTH=75%> NiCl<sub>2</sub>&#183;6H<sub>2</sub>O                                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;24.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q20","label":"Na2MoO4
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup.","source_stage":"trace
    stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[2].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 25 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;36.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q21","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup.","source_stage":"vitamin
    stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.00818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 15 (zero-based)","quote":"<TR><TD WIDTH=75%> Biotin                                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q22","label":"Folic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup.","source_stage":"vitamin
    stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.00453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> Folic acid                                              </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q23","label":"Pyridoxine
    hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup.","source_stage":"vitamin
    stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 10,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 17 (zero-based)","quote":"<TR><TD WIDTH=75%> Pyridoxine&#183;HCl                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q24","label":"Thiamine
    HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup.","source_stage":"vitamin
    stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 18 (zero-based)","quote":"<TR><TD WIDTH=75%> Thiamine&#183;HCl                                      </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[23].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[23].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q25","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup.","source_stage":"vitamin
    stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 19 (zero-based)","quote":"<TR><TD WIDTH=75%> Riboflavin                                              </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[24].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[24].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q26","label":"Nicotinic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup.","source_stage":"vitamin
    stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 20 (zero-based)","quote":"<TR><TD WIDTH=75%> Nicotinic acid                                          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[25].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[25].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q27","label":"Calcium
    pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup.","source_stage":"vitamin
    stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\":
    518,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0104925,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 21 (zero-based)","quote":"<TR><TD WIDTH=75%> Calcium pantothenate                                    </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[26].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[26].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q28","label":"Vitamin
    B12","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.0001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.0001","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup.","source_stage":"vitamin
    stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0001,\n                        \"mmol_l\":
    7.3779e-5,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 22 (zero-based)","quote":"<TR><TD WIDTH=75%> Vitamin B<sub>1</sub><sub>2</sub>                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[27].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[27].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q29","label":"p-Aminobenzoic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup.","source_stage":"vitamin
    stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 23 (zero-based)","quote":"<TR><TD WIDTH=75%> <I>p</I>-Aminobenzoic acid                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[28].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[28].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q30","label":"Lipoic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup.","source_stage":"vitamin
    stock","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[3].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Lipoic acid\",\n                        \"compound_id\":
    368,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.024233,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 24 (zero-based)","quote":"<TR><TD WIDTH=75%> Lipoic acid                                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ingredients[29].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ingredients[29].concentration","decision":"correct","rationale":"This
    current direct ingredient is a stock-recipe entry placed at the main-medium level.
    The provider g_l is explicitly a stock normalization, not the concentration after
    the stock dose. Preserve the primary stock batch amount and receiving dose separately.
    Primary stock water input is not independently measured final makeup."}]},{"quantity_id":"q31","label":"iron
    stock receiving dose","local_fields":[],"decision":"evidence_only","rationale":"Source-only
    missing structural control: preserve the exact JCM749 batch input and stage. It
    is not an independent final-volume measurement or a parent JCM187/197 receiving
    dose.","source_stage":"JCM749 basal","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"FeCl2 solution\",\n                        \"solution_id\":
    3846,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> FeCl<sub>2</sub> solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>) </TD><TD WIDTH=15%
    ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q32","label":"trace
    stock receiving dose","local_fields":[],"decision":"evidence_only","rationale":"Source-only
    missing structural control: preserve the exact JCM749 batch input and stage. It
    is not an independent final-volume measurement or a parent JCM187/197 receiving
    dose.","source_stage":"JCM749 basal","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\":
    3847,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML
    table row 8 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution (see
    Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>) </TD><TD WIDTH=15%
    ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q33","label":"basal
    water input","local_fields":[],"decision":"evidence_only","rationale":"Source-only
    missing structural control: preserve the exact JCM749 batch input and stage. It
    is not an independent final-volume measurement or a parent JCM187/197 receiving
    dose.","source_stage":"JCM749 basal","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 910,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML
    table row 10 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;910.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml   </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q34","label":"vitamin
    stock receiving dose","local_fields":[],"decision":"evidence_only","rationale":"Source-only
    missing structural control: preserve the exact JCM749 batch input and stage. It
    is not an independent final-volume measurement or a parent JCM187/197 receiving
    dose.","source_stage":"JCM749 post-cooling","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\":
    3861,\n                        \"attribute\": \"*\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"HTML
    table row 12 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace vitamins* (see Medium
    No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=197\">197</a>) </TD><TD WIDTH=15% ALIGN=RIGHT><font
    size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10% ALIGN=RIGHT>
    ml  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q35","label":"retained
    preparation and pH","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"preparation_steps","stored":[{"step_number":1,"action":"AUTOCLAVE","description":"Mix
    components thoroughly and autoclave under a N2-CO2 (4:1, v/v) gas atmosphere.
    After cooling, aseptically and anaerobically add the following solutions (autoclaved
    or *filter-sterilized):"},{"step_number":2,"action":"ADJUST_PH","description":"Adjust
    pH to 7.1 - 7.4, if necessary."}]},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"preparation_steps","stored":[{"step_number":1,"action":"AUTOCLAVE","description":"Mix
    components thoroughly and autoclave under a N2-CO2 (4:1, v/v) gas atmosphere.
    After cooling, aseptically and anaerobically add the following solutions (autoclaved
    or *filter-sterilized):"},{"step_number":2,"action":"ADJUST_PH","description":"Adjust
    pH to 7.1 - 7.4, if necessary."}]},{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ph_value","stored":7.2}],"decision":"evidence_only","rationale":"Both
    existing steps and pH 7.2 are supported by the exact source; 7.2 lies within 7.1–7.4.
    The first paragraph retains 4:1(v/v), cooling and aseptic/anaerobic addition.
    Preserve it, but connect its missing following stock table and distinguish filtered
    vitamin/bicarbonate from autoclaved additions.","source_stage":"main preparation","sources":[{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"step\": \"Mix components thoroughly and autoclave
    under a N2-CO2 (4:1, v/v) gas atmosphere. After cooling, aseptically and anaerobically
    add the following solutions (autoclaved or *filter-sterilized): \"\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ749","reference":"https://mediadive.dsmz.de/rest/medium/J749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/apiJ749.bin","raw_sha256":"23a8c032027d4a6cb2dfe638ee006df3e803c07cc04bf8bc584feb918158ffcf","text_sha256":"282bb6055b6ac5da8f192e929a0a8468b4b19f8feeaa0709b7e9e7bf70a56136","accessed_at":"2026-10-28T18:55:35.305313Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\":
    \"Adjust pH to 7.1 - 7.4, if necessary.\"\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"Complete
    preparation including following stock table and pH","quote":"Mix components thoroughly
    and autoclave under a N\n2\n-CO\n2\n(4:1, v/v) gas atmosphere.  After cooling,
    aseptically and anaerobically add the following solutions (autoclaved or *filter-sterilized):\n1.0
    M Sodium lactate solution\n20.0\nml\nTrace vitamins* (see Medium No.\n197\n)\n10.0\nml\n8%
    NaHCO\n3\nsolution*\n60.0\nml\n5% Na\n2\nS·9H\n2\nO solution\n8.0\nml\nAdjust
    pH to 7.1 - 7.4, if necessary.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"preparation_steps","decision":"evidence_only","rationale":"Both
    existing steps and pH 7.2 are supported by the exact source; 7.2 lies within 7.1–7.4.
    The first paragraph retains 4:1(v/v), cooling and aseptic/anaerobic addition.
    Preserve it, but connect its missing following stock table and distinguish filtered
    vitamin/bicarbonate from autoclaved additions."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"preparation_steps","decision":"evidence_only","rationale":"Both
    existing steps and pH 7.2 are supported by the exact source; 7.2 lies within 7.1–7.4.
    The first paragraph retains 4:1(v/v), cooling and aseptic/anaerobic addition.
    Preserve it, but connect its missing following stock table and distinguish filtered
    vitamin/bicarbonate from autoclaved additions."},{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"Both
    existing steps and pH 7.2 are supported by the exact source; 7.2 lies within 7.1–7.4.
    The first paragraph retains 4:1(v/v), cooling and aseptic/anaerobic addition.
    Preserve it, but connect its missing following stock table and distinguish filtered
    vitamin/bicarbonate from autoclaved additions."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"Both
    existing steps and pH 7.2 are supported by the exact source; 7.2 lies within 7.1–7.4.
    The first paragraph retains 4:1(v/v), cooling and aseptic/anaerobic addition.
    Preserve it, but connect its missing following stock table and distinguish filtered
    vitamin/bicarbonate from autoclaved additions."}]},{"quantity_id":"q36","label":"page-wide
    autoclave control","local_fields":[],"decision":"evidence_only","rationale":"The
    primary default 121°C for 15 min applies only where autoclaving is specified and
    no exception is stated. It does not replace the explicit later filtration instructions.","source_stage":"autoclave
    steps only","sources":[{"evidence_id":"jcm749","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=749","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/jcm749.bin","raw_sha256":"ec29ae1e2d36cefa094c1c9dfdfe41cdb388ead59032c4aca2c4d64ccfd60e31","text_sha256":"d0230668887a3c70552d168f5688a09bd8c5644c8270899b95215ba019aa2923","accessed_at":"2026-10-28T18:55:35.358203Z","locator":"Page-wide
    default","quote":"Unless otherwise stated, sterilize media by autoclaving at 121°C
    for 15 min.","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q37","label":"Distilled
    water scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[0].concentration","stored":{"value":"0.99","unit":"L"}}],"decision":"verified","rationale":"The
    current scoped water input is supported and already has an exact attached TOGO
    claim; water input is not final makeup.","source_stage":"JCM187 iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 18 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[0].concentration","decision":"verified","rationale":"The
    current scoped water input is supported and already has an exact attached TOGO
    claim; water input is not final makeup."}]},{"quantity_id":"q38","label":"FeCl2・4H2O
    scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[1].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 1.5 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The current note correctly
    retains the source batch mass without asserting g/L. Its attached TOGO excerpt
    and exact current raw digest authenticate this quantity at the stock stage, not
    a receiving-medium dose. Source-only API g_l may separately describe the provider
    stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM187
    iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 17 (zero-based)","quote":"<TR><TD WIDTH=75%> FeCl<sub>2</sub>&#183;4H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[1].notes","decision":"verified","rationale":"The
    current note correctly retains the source batch mass without asserting g/L. Its
    attached TOGO excerpt and exact current raw digest authenticate this quantity
    at the stock stage, not a receiving-medium dose. Source-only API g_l may separately
    describe the provider stock normalization; it does not invalidate conservative
    batch-mass wording."}]},{"quantity_id":"q39","label":"Distilled water scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"The
    current scoped water input is supported and already has an exact attached TOGO
    claim; water input is not final makeup.","source_stage":"JCM187 iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 26 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L        </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[0].concentration","decision":"verified","rationale":"The
    current scoped water input is supported and already has an exact attached TOGO
    claim; water input is not final makeup."}]},{"quantity_id":"q40","label":"Na2MoO4・2H2O
    scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 36 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The current note correctly
    retains the source batch mass without asserting g/L. Its attached TOGO excerpt
    and exact current raw digest authenticate this quantity at the stock stage, not
    a receiving-medium dose. Source-only API g_l may separately describe the provider
    stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM187
    iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 25 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;36.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[1].notes","decision":"verified","rationale":"The
    current note correctly retains the source batch mass without asserting g/L. Its
    attached TOGO excerpt and exact current raw digest authenticate this quantity
    at the stock stage, not a receiving-medium dose. Source-only API g_l may separately
    describe the provider stock normalization; it does not invalidate conservative
    batch-mass wording."}]},{"quantity_id":"q41","label":"H3BO3 scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 6 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The current note correctly
    retains the source batch mass without asserting g/L. Its attached TOGO excerpt
    and exact current raw digest authenticate this quantity at the stock stage, not
    a receiving-medium dose. Source-only API g_l may separately describe the provider
    stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM187
    iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 21 (zero-based)","quote":"<TR><TD WIDTH=75%> H<sub>3</sub>BO<sub>3</sub>                                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;6.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[2].notes","decision":"verified","rationale":"The
    current note correctly retains the source batch mass without asserting g/L. Its
    attached TOGO excerpt and exact current raw digest authenticate this quantity
    at the stock stage, not a receiving-medium dose. Source-only API g_l may separately
    describe the provider stock normalization; it does not invalidate conservative
    batch-mass wording."}]},{"quantity_id":"q42","label":"MnCl2・4H2O scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 100 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The current note correctly
    retains the source batch mass without asserting g/L. Its attached TOGO excerpt
    and exact current raw digest authenticate this quantity at the stock stage, not
    a receiving-medium dose. Source-only API g_l may separately describe the provider
    stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM187
    iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 20 (zero-based)","quote":"<TR><TD WIDTH=75%> MnCl<sub>2</sub>&#183;4H<sub>2</sub>O                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[3].notes","decision":"verified","rationale":"The
    current note correctly retains the source batch mass without asserting g/L. Its
    attached TOGO excerpt and exact current raw digest authenticate this quantity
    at the stock stage, not a receiving-medium dose. Source-only API g_l may separately
    describe the provider stock normalization; it does not invalidate conservative
    batch-mass wording."}]},{"quantity_id":"q43","label":"CoCl2・6H2O scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 190 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The current note correctly
    retains the source batch mass without asserting g/L. Its attached TOGO excerpt
    and exact current raw digest authenticate this quantity at the stock stage, not
    a receiving-medium dose. Source-only API g_l may separately describe the provider
    stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM187
    iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 22 (zero-based)","quote":"<TR><TD WIDTH=75%> CoCl<sub>2</sub>&#183;6H<sub>2</sub>O                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;190.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[4].notes","decision":"verified","rationale":"The
    current note correctly retains the source batch mass without asserting g/L. Its
    attached TOGO excerpt and exact current raw digest authenticate this quantity
    at the stock stage, not a receiving-medium dose. Source-only API g_l may separately
    describe the provider stock normalization; it does not invalidate conservative
    batch-mass wording."}]},{"quantity_id":"q44","label":"NiCl2・6H2O scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 24 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The current note correctly
    retains the source batch mass without asserting g/L. Its attached TOGO excerpt
    and exact current raw digest authenticate this quantity at the stock stage, not
    a receiving-medium dose. Source-only API g_l may separately describe the provider
    stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM187
    iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 24 (zero-based)","quote":"<TR><TD WIDTH=75%> NiCl<sub>2</sub>&#183;6H<sub>2</sub>O                                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;24.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[5].notes","decision":"verified","rationale":"The
    current note correctly retains the source batch mass without asserting g/L. Its
    attached TOGO excerpt and exact current raw digest authenticate this quantity
    at the stock stage, not a receiving-medium dose. Source-only API g_l may separately
    describe the provider stock normalization; it does not invalidate conservative
    batch-mass wording."}]},{"quantity_id":"q45","label":"CuCl2・2H2O scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 2 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The current note correctly
    retains the source batch mass without asserting g/L. Its attached TOGO excerpt
    and exact current raw digest authenticate this quantity at the stock stage, not
    a receiving-medium dose. Source-only API g_l may separately describe the provider
    stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM187
    iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 23 (zero-based)","quote":"<TR><TD WIDTH=75%> CuCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[6].notes","decision":"verified","rationale":"The
    current note correctly retains the source batch mass without asserting g/L. Its
    attached TOGO excerpt and exact current raw digest authenticate this quantity
    at the stock stage, not a receiving-medium dose. Source-only API g_l may separately
    describe the provider stock normalization; it does not invalidate conservative
    batch-mass wording."}]},{"quantity_id":"q46","label":"ZnCl2 scoped stock","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 70 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The current note correctly
    retains the source batch mass without asserting g/L. Its attached TOGO excerpt
    and exact current raw digest authenticate this quantity at the stock stage, not
    a receiving-medium dose. Source-only API g_l may separately describe the provider
    stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM187
    iron/trace stock","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 19 (zero-based)","quote":"<TR><TD WIDTH=75%> ZnCl<sub>2</sub>                                               </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;70.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[7].notes","decision":"verified","rationale":"The
    current note correctly retains the source batch mass without asserting g/L. Its
    attached TOGO excerpt and exact current raw digest authenticate this quantity
    at the stock stage, not a receiving-medium dose. Source-only API g_l may separately
    describe the provider stock normalization; it does not invalidate conservative
    batch-mass wording."}]},{"quantity_id":"q47","label":"Distilled water scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"The
    current scoped water input is supported and already has an exact attached TOGO
    claim; water input is not final makeup.","source_stage":"JCM197 vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 25 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[0].concentration","decision":"verified","rationale":"The
    current scoped water input is supported and already has an exact attached TOGO
    claim; water input is not final makeup."}]},{"quantity_id":"q48","label":"Biotin
    scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 2 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The current note correctly
    retains the source batch mass without asserting g/L. Its attached TOGO excerpt
    and exact current raw digest authenticate this quantity at the stock stage, not
    a receiving-medium dose. Source-only API g_l may separately describe the provider
    stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197
    vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 15 (zero-based)","quote":"<TR><TD WIDTH=75%> Biotin                                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[1].notes","decision":"verified","rationale":"The
    current note correctly retains the source batch mass without asserting g/L. Its
    attached TOGO excerpt and exact current raw digest authenticate this quantity
    at the stock stage, not a receiving-medium dose. Source-only API g_l may separately
    describe the provider stock normalization; it does not invalidate conservative
    batch-mass wording."}]},{"quantity_id":"q49","label":"p--Aminobenzoic acid scoped
    stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The current note correctly
    retains the source batch mass without asserting g/L. Its attached TOGO excerpt
    and exact current raw digest authenticate this quantity at the stock stage, not
    a receiving-medium dose. Source-only API g_l may separately describe the provider
    stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197
    vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 23 (zero-based)","quote":"<TR><TD WIDTH=75%> <I>p</I>-Aminobenzoic acid                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[2].notes","decision":"verified","rationale":"The
    current note correctly retains the source batch mass without asserting g/L. Its
    attached TOGO excerpt and exact current raw digest authenticate this quantity
    at the stock stage, not a receiving-medium dose. Source-only API g_l may separately
    describe the provider stock normalization; it does not invalidate conservative
    batch-mass wording."}]},{"quantity_id":"q50","label":"Thiamine・HCl scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The current note correctly
    retains the source batch mass without asserting g/L. Its attached TOGO excerpt
    and exact current raw digest authenticate this quantity at the stock stage, not
    a receiving-medium dose. Source-only API g_l may separately describe the provider
    stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197
    vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 18 (zero-based)","quote":"<TR><TD WIDTH=75%> Thiamine&#183;HCl                                      </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[3].notes","decision":"verified","rationale":"The
    current note correctly retains the source batch mass without asserting g/L. Its
    attached TOGO excerpt and exact current raw digest authenticate this quantity
    at the stock stage, not a receiving-medium dose. Source-only API g_l may separately
    describe the provider stock normalization; it does not invalidate conservative
    batch-mass wording."}]},{"quantity_id":"q51","label":"Calcium pantothenate scoped
    stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The current note correctly
    retains the source batch mass without asserting g/L. Its attached TOGO excerpt
    and exact current raw digest authenticate this quantity at the stock stage, not
    a receiving-medium dose. Source-only API g_l may separately describe the provider
    stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197
    vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 21 (zero-based)","quote":"<TR><TD WIDTH=75%> Calcium pantothenate                                    </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[4].notes","decision":"verified","rationale":"The
    current note correctly retains the source batch mass without asserting g/L. Its
    attached TOGO excerpt and exact current raw digest authenticate this quantity
    at the stock stage, not a receiving-medium dose. Source-only API g_l may separately
    describe the provider stock normalization; it does not invalidate conservative
    batch-mass wording."}]},{"quantity_id":"q52","label":"Pyridoxine・HCl scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 10 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The current note correctly
    retains the source batch mass without asserting g/L. Its attached TOGO excerpt
    and exact current raw digest authenticate this quantity at the stock stage, not
    a receiving-medium dose. Source-only API g_l may separately describe the provider
    stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197
    vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 17 (zero-based)","quote":"<TR><TD WIDTH=75%> Pyridoxine&#183;HCl                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[5].notes","decision":"verified","rationale":"The
    current note correctly retains the source batch mass without asserting g/L. Its
    attached TOGO excerpt and exact current raw digest authenticate this quantity
    at the stock stage, not a receiving-medium dose. Source-only API g_l may separately
    describe the provider stock normalization; it does not invalidate conservative
    batch-mass wording."}]},{"quantity_id":"q53","label":"Folic acid scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 2 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The current note correctly
    retains the source batch mass without asserting g/L. Its attached TOGO excerpt
    and exact current raw digest authenticate this quantity at the stock stage, not
    a receiving-medium dose. Source-only API g_l may separately describe the provider
    stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197
    vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> Folic acid                                              </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[6].notes","decision":"verified","rationale":"The
    current note correctly retains the source batch mass without asserting g/L. Its
    attached TOGO excerpt and exact current raw digest authenticate this quantity
    at the stock stage, not a receiving-medium dose. Source-only API g_l may separately
    describe the provider stock normalization; it does not invalidate conservative
    batch-mass wording."}]},{"quantity_id":"q54","label":"Vitamin B12 scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 0.1 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The current note correctly
    retains the source batch mass without asserting g/L. Its attached TOGO excerpt
    and exact current raw digest authenticate this quantity at the stock stage, not
    a receiving-medium dose. Source-only API g_l may separately describe the provider
    stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197
    vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 22 (zero-based)","quote":"<TR><TD WIDTH=75%> Vitamin B<sub>1</sub><sub>2</sub>                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[7].notes","decision":"verified","rationale":"The
    current note correctly retains the source batch mass without asserting g/L. Its
    attached TOGO excerpt and exact current raw digest authenticate this quantity
    at the stock stage, not a receiving-medium dose. Source-only API g_l may separately
    describe the provider stock normalization; it does not invalidate conservative
    batch-mass wording."}]},{"quantity_id":"q55","label":"Riboflavin scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[8].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The current note correctly
    retains the source batch mass without asserting g/L. Its attached TOGO excerpt
    and exact current raw digest authenticate this quantity at the stock stage, not
    a receiving-medium dose. Source-only API g_l may separately describe the provider
    stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197
    vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 19 (zero-based)","quote":"<TR><TD WIDTH=75%> Riboflavin                                              </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[8].notes","decision":"verified","rationale":"The
    current note correctly retains the source batch mass without asserting g/L. Its
    attached TOGO excerpt and exact current raw digest authenticate this quantity
    at the stock stage, not a receiving-medium dose. Source-only API g_l may separately
    describe the provider stock normalization; it does not invalidate conservative
    batch-mass wording."}]},{"quantity_id":"q56","label":"Nicotinic acid scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[9].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The current note correctly
    retains the source batch mass without asserting g/L. Its attached TOGO excerpt
    and exact current raw digest authenticate this quantity at the stock stage, not
    a receiving-medium dose. Source-only API g_l may separately describe the provider
    stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197
    vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 20 (zero-based)","quote":"<TR><TD WIDTH=75%> Nicotinic acid                                          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[9].notes","decision":"verified","rationale":"The
    current note correctly retains the source batch mass without asserting g/L. Its
    attached TOGO excerpt and exact current raw digest authenticate this quantity
    at the stock stage, not a receiving-medium dose. Source-only API g_l may separately
    describe the provider stock normalization; it does not invalidate conservative
    batch-mass wording."}]},{"quantity_id":"q57","label":"Lipoic acid scoped stock","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[10].notes","stored":"Role:
    Growth factor; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The current note correctly
    retains the source batch mass without asserting g/L. Its attached TOGO excerpt
    and exact current raw digest authenticate this quantity at the stock stage, not
    a receiving-medium dose. Source-only API g_l may separately describe the provider
    stock normalization; it does not invalidate conservative batch-mass wording.","source_stage":"JCM197
    vitamin stock","sources":[{"evidence_id":"togo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch075/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:56:05.258322Z","locator":"components[1].items[10]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:56:04.601366Z","locator":"HTML
    table row 24 (zero-based)","quote":"<TR><TD WIDTH=75%> Lipoic acid                                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[10].notes","decision":"verified","rationale":"The
    current note correctly retains the source batch mass without asserting g/L. Its
    attached TOGO excerpt and exact current raw digest authenticate this quantity
    at the stock stage, not a receiving-medium dose. Source-only API g_l may separately
    describe the provider stock normalization; it does not invalidate conservative
    batch-mass wording."}]},{"quantity_id":"q58","label":"HCl reagent dose","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].concentration","stored":{"value":"0.01","unit":"L"}}],"decision":"verified","rationale":"10
    ml = 0.01 L is the iron-stock reagent dose. The existing root evidence contains
    this exact additional excerpt and explicitly names this field; the leading parent-medium
    dose excerpt is excluded. No 25% basis or mass concentration is inferred.","source_stage":"iron
    stock reagent addition","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> 25% HCl (7.7 M)                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].concentration","decision":"verified","rationale":"10
    ml = 0.01 L is the iron-stock reagent dose. The existing root evidence contains
    this exact additional excerpt and explicitly names this field; the leading parent-medium
    dose excerpt is excluded. No 25% basis or mass concentration is inferred."}]},{"quantity_id":"q59","label":"HCl
    reagent strength","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].composition[0].concentration","stored":{"value":"7.7","unit":"MOLAR"}}],"decision":"verified","rationale":"Existing
    7.7 M reagent strength and attached exact TOGO evidence are supported. This is
    neither the stock nor receiving-medium final HCl concentration. The bare25% remains
    unconverted.","source_stage":"HCl reagent strength","sources":[{"evidence_id":"togo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch075/publish-sources/togo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:56:05.236822Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch075/publish-sources/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T18:56:03.575661Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> 25% HCl (7.7 M)                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].composition[0].concentration","decision":"verified","rationale":"Existing
    7.7 M reagent strength and attached exact TOGO evidence are supported. This is
    neither the stock nor receiving-medium final HCl concentration. The bare25% remains
    unconverted."}]}],"document_scopes":{"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM_WITH_LACTATE.yaml":null,"data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml":null,"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml":["solutions[0].composition","solutions[0].solutions","solutions[1].composition"],"data/normalized_yaml/bacterial/togo_medium_m190.yaml":["solutions[1].composition"]},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: 'All asserted scoped ontology objects are current and were checked for
    supplied salt/hydrate and stereochemical specificity. Neutral resazurin is not
    relabelled sodium resazurin because these sources say only resazurin. Nickel CHEBI:34887
    and scoped M180 cobalt CHEBI:35696 are anhydrous despite explicit hexahydrates.
    Current CHEBI:53542/53503 support the respective hexahydrates. MIM preferred NiCl2
    x 6 H2O and CoCl2 x 6 H2O rows are REJECTED; the distinct preferred Nickel (II)
    chloride hexahydrate row is MAPPED, so no generic catalogue approval/rejection
    is inferred. Calcium pantothenate CHEBI:31345 has D stereochemistry, while the
    recipe gives a generic name: specificity remains unverified. Lipoic acid CHEBI:16494
    is non-stereospecific and Vitamin B12 CHEBI:176843 is a vitamer class, consistent
    with the generic source wording. Exact slot/link coverage is reported separately
    from chemical validity.'
  target_ids:
  - CultureMech:003092
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: All six exact historical reports and selected parent rows were read. October
    5 zero-source-check triage is not scientific verification. October 7 J749 69 claims
    left the record unchanged; exact current API objects/raw digest authenticate the
    quoted content, not the original access event. Scoped October 8 M180/M190 repairs
    preserve batch masses, stock water and HCl evidence and deserve explicit credit;
    other parent-medium claims are excluded. Current parser/cleanup/conservative merger
    behavior is distinguished from historical execution.
  target_ids:
  - CultureMech:003092
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
  - historical-source-joins
  - historical-selected-parent-rows
  - writer-mediadive
  - writer-cleanup
findings:
- finding_id: f1
  issue_key: culturemech-003092-stock-stage-and-dose
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Separate liquid additions and nineteen stock entries
  description: The selected target and owner flatten iron, trace and vitamin stock
    concentrations into main ingredients and encode 20/60/8 ml additions as g/L. Reconstruct
    exact JCM749 stocks and receiving-batch doses, including basal water 910 ml and
    iron/trace 1 ml each; retain the eight explicit provider main g_l values only
    on the declared 1010 ml basis. Preserve 1.0 M lactate and unspecified 8%/5% bases.
    Current importer no longer flattens later API stocks but still misses the molar-only
    lactate row; curate that exact predicate without claiming it caused the old import.
  target_ids:
  - CultureMech:003092
  field_paths:
  - ingredients[8].concentration
  - ingredients[9].concentration
  - ingredients[10].concentration
  - ingredients[11].concentration
  - ingredients[12].concentration
  - ingredients[13].concentration
  - ingredients[14].concentration
  - ingredients[15].concentration
  - ingredients[16].concentration
  - ingredients[17].concentration
  - ingredients[18].concentration
  - ingredients[19].concentration
  - ingredients[20].concentration
  - ingredients[21].concentration
  - ingredients[22].concentration
  - ingredients[23].concentration
  - ingredients[24].concentration
  - ingredients[25].concentration
  - ingredients[26].concentration
  - ingredients[27].concentration
  - ingredients[28].concentration
  - ingredients[29].concentration
  - solutions
  - ingredients
  evidence_ids:
  - quantities
  - jcm749
  - apiJ749
  - jcm187
  - jcm197
  - writer-mediadive
  rule_id: culturemech-scientific-review/stock-stage-and-dose
  native_severity: P2
  normalization_reason: Custom source-stage, dimensional or supplied-form requirement
    normalized to major because it changes the scientific interpretation.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current molar-stock classification writer
- finding_id: f2
  issue_key: culturemech-003092-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Correct explicit nickel and scoped cobalt hydrate assertions
  description: Selected nickel has CHEBI:34887 in both primary and secondary slots,
    although source NiCl2·6H2O is a hexahydrate. Scoped M180 trace cobalt and nickel
    similarly retain anhydrous CHEBI:35696/34887. Verify exact hexahydrate terms 53503/53542
    against current OLS; preserve the independently supported amounts and current
    MIM spelling-specific statuses. Selected cobalt 53503 is already correct.
  target_ids:
  - CultureMech:003092
  field_paths:
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[1].composition[4].term
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[1].composition[5].term
  evidence_ids:
  - jcm187
  - chebi53542
  - chebi53503
  - groundings
  rule_id: culturemech-scientific-review/hydrate-grounding
  native_severity: P2
  normalization_reason: Custom source-stage, dimensional or supplied-form requirement
    normalized to major because it changes the scientific interpretation.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    role: scoped dependency
- finding_id: f3
  issue_key: culturemech-003092-scoped-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Attach field and stage evidence while crediting existing stock repairs
  description: Selected ingredients and preparation lack scoped attached source claims.
    Attach ingredient claims at ingredients[i].evidence and solution/preparation claims
    at root evidence with exact field/stage locators. Existing M180/M190 stock notes,
    water inputs and nested HCl evidence are already supported and must be retained;
    do not reclassify those repaired quantities as absent evidence. Include the scoped
    121°C/15min page default without applying it to filtration.
  target_ids:
  - CultureMech:003092
  field_paths:
  - ingredients[*].evidence
  - evidence
  - preparation_steps
  evidence_ids:
  - quantities
  - old-claims
  - jcm749
  rule_id: culturemech-scientific-review/scoped-evidence
  native_severity: P3
  normalization_reason: Custom evidence/completeness or unresolved-specificity requirement
    normalized to minor because supported recipe content is retained and no numerical
    replacement is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-003092-pantothenate-specificity
  category: grounding
  severity: minor
  status: open
  certainty: provisional
  title: Qualify unverified pantothenate stereochemistry
  description: The source specifies generic calcium pantothenate while CHEBI:31345
    encodes D stereochemistry. Retain the amount and generic source wording; recover
    exact supplied-form evidence before claiming that specificity or changing identifiers.
    This is an unresolved specificity limit, not a confirmed wrong-chemical assertion.
  target_ids:
  - CultureMech:003092
  field_paths:
  - ingredients[26].term
  - ingredients[26].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/togo_medium_m190.yaml::solutions[1].composition[4].term
  - data/normalized_yaml/bacterial/togo_medium_m190.yaml::solutions[1].composition[4].mediaingredientmech_chebi_term
  evidence_ids:
  - jcm197
  - groundings
  rule_id: culturemech-scientific-review/pantothenate-specificity
  native_severity: P3
  normalization_reason: Custom evidence/completeness or unresolved-specificity requirement
    normalized to minor because supported recipe content is retained and no numerical
    replacement is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/togo_medium_m190.yaml
    role: scoped dependency
actions:
- action_id: a1
  description: The selected target and owner flatten iron, trace and vitamin stock
    concentrations into main ingredients and encode 20/60/8 ml additions as g/L. Reconstruct
    exact JCM749 stocks and receiving-batch doses, including basal water 910 ml and
    iron/trace 1 ml each; retain the eight explicit provider main g_l values only
    on the declared 1010 ml basis. Preserve 1.0 M lactate and unspecified 8%/5% bases.
    Current importer no longer flattens later API stocks but still misses the molar-only
    lactate row; curate that exact predicate without claiming it caused the old import.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003092
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current molar-stock classification writer
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a2
  description: Selected nickel has CHEBI:34887 in both primary and secondary slots,
    although source NiCl2·6H2O is a hexahydrate. Scoped M180 trace cobalt and nickel
    similarly retain anhydrous CHEBI:35696/34887. Verify exact hexahydrate terms 53503/53542
    against current OLS; preserve the independently supported amounts and current
    MIM spelling-specific statuses. Selected cobalt 53503 is already correct.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003092
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml
    role: maintained normalized contributor
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
- action_id: a3
  description: Selected ingredients and preparation lack scoped attached source claims.
    Attach ingredient claims at ingredients[i].evidence and solution/preparation claims
    at root evidence with exact field/stage locators. Existing M180/M190 stock notes,
    water inputs and nested HCl evidence are already supported and must be retained;
    do not reclassify those repaired quantities as absent evidence. Include the scoped
    121°C/15min page default without applying it to filtration.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003092
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml
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
  description: The source specifies generic calcium pantothenate while CHEBI:31345
    encodes D stereochemistry. Retain the amount and generic source wording; recover
    exact supplied-form evidence before claiming that specificity or changing identifiers.
    This is an unresolved specificity limit, not a confirmed wrong-chemical assertion.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:003092
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_medium_with_lactate.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/togo_medium_m190.yaml
    role: scoped dependency
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
limitations:
- Calcium pantothenate stereochemistry remains unverified; provider mmol_l conversions
  and catalog synonym chemistry are not blanket certified. Parent M180/M190 receiving
  doses, main-medium conditions and unrelated compounds are outside scope.
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
