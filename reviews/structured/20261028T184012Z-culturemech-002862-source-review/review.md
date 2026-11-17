# Scientific review: DESULFOBULBUS MEDIUM

- Review: 20261028T184012Z-culturemech-002862-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T18:07:21.956551Z
- Finished UTC: 2026-10-28T18:40:12.415103Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact J511 identity, eight basal provider rates and existing preparation are supported. Three liquid additions and nineteen stock entries remain misrepresented as direct masses or final-medium concentrations; bounded hydrate, source-attribute and current molar-stock-parser corrections are required. Existing scoped M180/M190 batch repairs and evidence are preserved.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch074 index 10
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002862 | data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml | generated | desulfobulbus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:002862 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:002862 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:002862 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:002862 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Current source and owner identity

identity: supported. Targets: CultureMech:002862.

The current target is generated from exactly one JCM J511 owner. Earlier reports describing a three-source group are historical context, not the current ownership contract. JCM187 iron/trace and JCM197 vitamin subsections are explicit source references; only those dependency sections transfer.

### Nonquantity assertions and retained metadata

consistency: supported. Targets: CultureMech:002862.

DEFINED composition and LIQUID state agree with the named chemical formulation; generic cultivation application establishes no organism growth. The provider pH point is within the already-retained primary range. Names, source identity and current one-source merge provenance are consistent.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:002862.

65 current concentration fields are covered by 65 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b074-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","quantity_field_count":65,"decisions":[{"quantity_id":"q1","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.9703","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.9703","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current value agrees, within displayed rounding, with the explicit provider main-stage g_l normalized on its declared 1010 mL basis. The primary batch mass and source water/additions agree with that nominal recipe basis. This supports the existing rate without asserting measured final volume or an already-attached claim.","source_stage":"main medium, declared provider basis","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.9703,\n                        \"mmol_l\": 20.9117,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML table row 0 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt; &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.19802","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.19802","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current value agrees, within displayed rounding, with the explicit provider main-stage g_l normalized on its declared 1010 mL basis. The primary batch mass and source water/additions agree with that nominal recipe basis. This supports the existing rate without asserting measured final volume or an already-attached claim.","source_stage":"main medium, declared provider basis","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.19802,\n                        \"mmol_l\": 1.45511,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML table row 1 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt; &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.2&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.29703","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.29703","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current value agrees, within displayed rounding, with the explicit provider main-stage g_l normalized on its declared 1010 mL basis. The primary batch mass and source water/additions agree with that nominal recipe basis. This supports the existing rate without asserting measured final volume or an already-attached claim.","source_stage":"main medium, declared provider basis","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.29703,\n                        \"mmol_l\": 5.553,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML table row 2 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NH&lt;sub&gt;4&lt;/sub&gt;Cl &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.3&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20.7921","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20.7921","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current value agrees, within displayed rounding, with the explicit provider main-stage g_l normalized on its declared 1010 mL basis. The primary batch mass and source water/additions agree with that nominal recipe basis. This supports the existing rate without asserting measured final volume or an already-attached claim.","source_stage":"main medium, declared provider basis","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 21,\n                        \"unit\": \"g\",\n                        \"g_l\": 20.7921,\n                        \"mmol_l\": 355.785,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML table row 3 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;21.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"3.06931","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"3.06931","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current value agrees, within displayed rounding, with the explicit provider main-stage g_l normalized on its declared 1010 mL basis. The primary batch mass and source water/additions agree with that nominal recipe basis. This supports the existing rate without asserting measured final volume or an already-attached claim.","source_stage":"main medium, declared provider basis","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 3.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.06931,\n                        \"mmol_l\": 15.0972,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML table row 4 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.49505","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.49505","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current value agrees, within displayed rounding, with the explicit provider main-stage g_l normalized on its declared 1010 mL basis. The primary batch mass and source water/additions agree with that nominal recipe basis. This supports the existing rate without asserting measured final volume or an already-attached claim.","source_stage":"main medium, declared provider basis","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.49505,\n                        \"mmol_l\": 6.6405,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML table row 5 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; KCl &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.148515","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.148515","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current value agrees, within displayed rounding, with the explicit provider main-stage g_l normalized on its declared 1010 mL basis. The primary batch mass and source water/additions agree with that nominal recipe basis. This supports the existing rate without asserting measured final volume or an already-attached claim.","source_stage":"main medium, declared provider basis","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.148515,\n                        \"mmol_l\": 1.0102,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML table row 6 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.15&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000990099","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000990099","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current value agrees, within displayed rounding, with the explicit provider main-stage g_l normalized on its declared 1010 mL basis. The primary batch mass and source water/additions agree with that nominal recipe basis. This supports the existing rate without asserting measured final volume or an already-attached claim.","source_stage":"main medium, declared provider basis","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.000990099,\n                        \"mmol_l\": 0.00431999,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML table row 9 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Resazurin &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"Sodium propionate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"15","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored G_PER_L value copies a liquid stock dose in mL. Retain the receiving amount, source stock strength and late-addition handling separately. Sodium propionate is explicitly 1.0 M and filter-sterilized; do not treat 15 mL as 15 g/L.","source_stage":"post-cooling receiving stock dose","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Sodium propionate\",\n                        \"compound_id\": 1778,\n                        \"attribute\": \"*, 1.0 M\",\n                        \"amount\": 15,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 1.0 M Sodium propionate solution* &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;15.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"60","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"60","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored G_PER_L value copies a liquid stock dose in mL. Retain the receiving amount, source stock strength and late-addition handling separately. The 8% bicarbonate stock is filter-sterilized, but the percent basis is unstated; do not derive a mass from it.","source_stage":"post-cooling receiving stock dose","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"attribute\": \"*, 8%\",\n                        \"amount\": 60,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML table row 13 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 8% NaHCO&lt;sub&gt;3&lt;/sub&gt; solution* &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;60.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored G_PER_L value copies a liquid stock dose in mL. Retain the receiving amount, source stock strength and late-addition handling separately. The 5% sodium sulfide nonahydrate stock is autoclaved, but the percent basis is unstated; do not derive a mass from it.","source_stage":"post-cooling receiving stock dose","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"attribute\": \"5%\",\n                        \"amount\": 8,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML table row 14 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O solution &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;8.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml   &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider reports 2.5 g/L for a 10 mL 25%/7.7 M HCl reagent in the iron stock, but the percentage basis is unstated. The retained direct-medium 2.5 g/L is unsupported in both stage and mass basis; preserve the explicitly supported reagent strength and input dose instead.","source_stage":"iron stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"7.7 M, 25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 25% HCl (7.7 M)                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"This number is the declared concentration within a named iron, trace-element or vitamin stock, not the final receiving medium. Restore the source stock and receiving dose; retain the supported stock batch input and do not infer a measured final-stock volume from water alone.","source_stage":"iron stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML table row 17 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"This number is the declared concentration within a named iron, trace-element or vitamin stock, not the final receiving medium. Restore the source stock and receiving dose; retain the supported stock batch input and do not infer a measured final-stock volume from water alone.","source_stage":"trace-element stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML table row 19 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnCl&lt;sub&gt;2&lt;/sub&gt;                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;70.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This number is the declared concentration within a named iron, trace-element or vitamin stock, not the final receiving medium. Restore the source stock and receiving dose; retain the supported stock batch input and do not infer a measured final-stock volume from water alone.","source_stage":"trace-element stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"This number is the declared concentration within a named iron, trace-element or vitamin stock, not the final receiving medium. Restore the source stock and receiving dose; retain the supported stock batch input and do not infer a measured final-stock volume from water alone.","source_stage":"trace-element stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;6.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q17","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"This number is the declared concentration within a named iron, trace-element or vitamin stock, not the final receiving medium. Restore the source stock and receiving dose; retain the supported stock batch input and do not infer a measured final-stock volume from water alone.","source_stage":"trace-element stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML table row 22 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;190.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q18","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"This number is the declared concentration within a named iron, trace-element or vitamin stock, not the final receiving medium. Restore the source stock and receiving dose; retain the supported stock batch input and do not infer a measured final-stock volume from water alone.","source_stage":"trace-element stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[2].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML table row 23 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q19","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"This number is the declared concentration within a named iron, trace-element or vitamin stock, not the final receiving medium. Restore the source stock and receiving dose; retain the supported stock batch input and do not infer a measured final-stock volume from water alone.","source_stage":"trace-element stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[2].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML table row 24 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;24.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q20","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"This number is the declared concentration within a named iron, trace-element or vitamin stock, not the final receiving medium. Restore the source stock and receiving dose; retain the supported stock batch input and do not infer a measured final-stock volume from water alone.","source_stage":"trace-element stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[2].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML table row 25 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;36.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q21","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"This number is the declared concentration within a named iron, trace-element or vitamin stock, not the final receiving medium. Restore the source stock and receiving dose; retain the supported stock batch input and do not infer a measured final-stock volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML table row 15 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Biotin                                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"This number is the declared concentration within a named iron, trace-element or vitamin stock, not the final receiving medium. Restore the source stock and receiving dose; retain the supported stock batch input and do not infer a measured final-stock volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Folic acid                                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"Pyridoxine hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"correct","rationale":"This number is the declared concentration within a named iron, trace-element or vitamin stock, not the final receiving medium. Restore the source stock and receiving dose; retain the supported stock batch input and do not infer a measured final-stock volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML table row 17 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Pyridoxine&amp;#183;HCl                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"Thiamine HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This number is the declared concentration within a named iron, trace-element or vitamin stock, not the final receiving medium. Restore the source stock and receiving dose; retain the supported stock batch input and do not infer a measured final-stock volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML table row 18 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Thiamine&amp;#183;HCl                                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This number is the declared concentration within a named iron, trace-element or vitamin stock, not the final receiving medium. Restore the source stock and receiving dose; retain the supported stock batch input and do not infer a measured final-stock volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML table row 19 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Riboflavin                                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This number is the declared concentration within a named iron, trace-element or vitamin stock, not the final receiving medium. Restore the source stock and receiving dose; retain the supported stock batch input and do not infer a measured final-stock volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Nicotinic acid                                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"Calcium pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This number is the declared concentration within a named iron, trace-element or vitamin stock, not the final receiving medium. Restore the source stock and receiving dose; retain the supported stock batch input and do not infer a measured final-stock volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0104925,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Calcium pantothenate                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.0001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.0001","unit":"G_PER_L"}}],"decision":"correct","rationale":"This number is the declared concentration within a named iron, trace-element or vitamin stock, not the final receiving medium. Restore the source stock and receiving dose; retain the supported stock batch input and do not infer a measured final-stock volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 0.1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0001,\n                        \"mmol_l\": 7.3779e-5,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML table row 22 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin B&lt;sub&gt;1&lt;/sub&gt;&lt;sub&gt;2&lt;/sub&gt;                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This number is the declared concentration within a named iron, trace-element or vitamin stock, not the final receiving medium. Restore the source stock and receiving dose; retain the supported stock batch input and do not infer a measured final-stock volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML table row 23 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; &lt;I&gt;p&lt;/I&gt;-Aminobenzoic acid                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"Lipoic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This number is the declared concentration within a named iron, trace-element or vitamin stock, not the final receiving medium. Restore the source stock and receiving dose; retain the supported stock batch input and do not infer a measured final-stock volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Lipoic acid\",\n                        \"compound_id\": 368,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.024233,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML table row 24 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Lipoic acid                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"Main water","local_fields":[],"decision":"evidence_only","rationale":"Preserve this exact source input or receiving dose in its named stage. Input water is not a measured final volume, and parent-medium doses of linked dependency documents are excluded.","source_stage":"source-only main water","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 915,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML table row 10 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;915.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml   &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q32","label":"Iron-stock receiving dose","local_fields":[],"decision":"evidence_only","rationale":"Preserve this exact source input or receiving dose in its named stage. Input water is not a measured final volume, and parent-medium doses of linked dependency documents are excluded.","source_stage":"source-only iron-stock receiving dose","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"solution\": \"FeCl2 solution\",\n                        \"solution_id\": 3846,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeCl&lt;sub&gt;2&lt;/sub&gt; solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;) &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q33","label":"Trace-stock receiving dose","local_fields":[],"decision":"evidence_only","rationale":"Preserve this exact source input or receiving dose in its named stage. Input water is not a measured final volume, and parent-medium doses of linked dependency documents are excluded.","source_stage":"source-only trace-stock receiving dose","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 3847,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML table row 8 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;) &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q34","label":"Vitamin-stock receiving dose","local_fields":[],"decision":"evidence_only","rationale":"Preserve this exact source input or receiving dose in its named stage. Input water is not a measured final volume, and parent-medium doses of linked dependency documents are excluded.","source_stage":"source-only vitamin-stock receiving dose","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\": 3861,\n                        \"attribute\": \"*\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML table row 12 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace vitamins* (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=197\"&gt;197&lt;/a&gt;) &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q35","label":"Iron-stock input water","local_fields":[],"decision":"evidence_only","rationale":"Preserve this exact source input or receiving dose in its named stage. Input water is not a measured final volume, and parent-medium doses of linked dependency documents are excluded.","source_stage":"source-only iron-stock input water","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML table row 18 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q36","label":"Trace-stock input water","local_fields":[],"decision":"evidence_only","rationale":"Preserve this exact source input or receiving dose in its named stage. Input water is not a measured final volume, and parent-medium doses of linked dependency documents are excluded.","source_stage":"source-only trace-stock input water","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[2].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML table row 26 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q37","label":"Vitamin-stock input water","local_fields":[],"decision":"evidence_only","rationale":"Preserve this exact source input or receiving dose in its named stage. Input water is not a measured final volume, and parent-medium doses of linked dependency documents are excluded.","source_stage":"source-only vitamin-stock input water","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML table row 25 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q38","label":"Retained main preparation","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"preparation_steps[0].description","stored":"Mix components thoroughly and autoclave under a N2-CO2 (4:1, v/v) gas atmosphere. After cooling, aseptically and anaerobically add the following solutions (autoclaved or *filter-sterilized):"},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"preparation_steps[0].description","stored":"Mix components thoroughly and autoclave under a N2-CO2 (4:1, v/v) gas atmosphere. After cooling, aseptically and anaerobically add the following solutions (autoclaved or *filter-sterilized):"}],"decision":"evidence_only","rationale":"The complete existing sentence retains the 4:1 N2/CO2 atmosphere, cooling, aseptic anaerobic addition and distinction between autoclaved or starred filter-sterilized stocks. Credit that text; restoring each missing stock attribute makes its starred references usable.","source_stage":"main preparation","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\": 12,\n                        \"step\": \"Mix components thoroughly and autoclave under a N2-CO2 (4:1, v/v) gas atmosphere. After cooling, aseptically and anaerobically add the following solutions (autoclaved or *filter-sterilized): \"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"Retained pH instruction","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"preparation_steps[1].description","stored":"Adjust pH to 7.1 - 7.4, if necessary."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"preparation_steps[1].description","stored":"Adjust pH to 7.1 - 7.4, if necessary."}],"decision":"evidence_only","rationale":"The existing conditional pH 7.1–7.4 instruction matches the primary and provider step. Preserve the whole range and if-necessary qualification.","source_stage":"main preparation","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\": \"Adjust pH to 7.1 - 7.4, if necessary.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q40","label":"Current pH point","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ph_value","stored":7.2}],"decision":"evidence_only","rationale":"The provider metadata gives pH 7.2, within the primary conditional 7.1–7.4 range already retained in preparation. Keep its provider-point provenance separate from the broader primary range.","source_stage":"provider metadata and primary range","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.medium","quote":"{\n            \"id\": \"J511\",\n            \"name\": \"DESULFOBULBUS MEDIUM\",\n            \"complex_medium\": \"no\",\n            \"min_pH\": 7.2,\n            \"max_pH\": 7.2,\n            \"source\": \"JCM\",\n            \"link\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511\"\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\": \"Adjust pH to 7.1 - 7.4, if necessary.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q41","label":"JCM default sterilization","local_fields":[],"decision":"evidence_only","rationale":"The primary default states 121 C for 15 min unless otherwise specified. Add it only with its default scope; explicit starred filter-sterilized stocks remain separate.","source_stage":"source-only default sterilization","sources":[{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"jcm511.txt lines 4-4","quote":"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q42","label":"Retained M180 Distilled water","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[0].concentration","stored":{"value":"0.99","unit":"L"}}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 990,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q43","label":"Retained M180 FeCl2・4H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[1].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 1.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"FeCl2・4H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001548\",\n          \"gmo_id\": \"GMO_001548\",\n          \"label\": \"Iron(II) chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q44","label":"Retained M180 Distilled water","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q45","label":"Retained M180 Na2MoO4・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 36 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q46","label":"Retained M180 H3BO3","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 6 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q47","label":"Retained M180 MnCl2・4H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 100 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q48","label":"Retained M180 CoCl2・6H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 190 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q49","label":"Retained M180 NiCl2・6H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 24 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q50","label":"Retained M180 CuCl2・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\": \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q51","label":"Retained M180 ZnCl2","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 70 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\": \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\": \"GMO_001035\",\n          \"label\": \"Zinc chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q52","label":"Retained nested HCl solutions[0].solutions[0].composition[0].concentration","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].composition[0].concentration","stored":{"value":"7.7","unit":"MOLAR"}}],"decision":"verified","rationale":"Explicit 7.7 M reagent strength is supported by its attached exact claim; the accompanying 25% basis is unspecified.","source_stage":"M180 iron-stock nested reagent","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q53","label":"Retained nested HCl solutions[0].solutions[0].concentration","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].concentration","stored":{"value":"0.01","unit":"L"}}],"decision":"verified","rationale":"The root evidence contains an additional exact HCl excerpt and this nested descriptor locator, authenticating 10 mL = 0.01 L into the iron stock; it is not the excluded parent-medium receiving dose.","source_stage":"M180 iron-stock nested reagent","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q54","label":"Retained HCl input-dose note","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].notes","stored":"Source stock addition: 10 ml = 0.01 L per receiving batch, not grams per liter or a dose per final liter."}],"decision":"verified","rationale":"The retained numeric note has the same exact scoped root attachment as the nested descriptor; no new dose or final concentration is inferred.","source_stage":"M180 nested HCl","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q55","label":"Retained vitamin Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"The attached exact source claim and digest authenticate this retained batch input. Preserve the repaired water unit or mass note without restoring unsupported g/L or transferring the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q56","label":"Retained vitamin Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The attached exact source claim and digest authenticate this retained batch input. Preserve the repaired water unit or mass note without restoring unsupported g/L or transferring the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q57","label":"Retained vitamin p--Aminobenzoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The attached exact source claim and digest authenticate this retained batch input. Preserve the repaired water unit or mass note without restoring unsupported g/L or transferring the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q58","label":"Retained vitamin Thiamine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The attached exact source claim and digest authenticate this retained batch input. Preserve the repaired water unit or mass note without restoring unsupported g/L or transferring the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\": \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q59","label":"Retained vitamin Calcium pantothenate","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The attached exact source claim and digest authenticate this retained batch input. Preserve the repaired water unit or mass note without restoring unsupported g/L or transferring the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\",\n          \"gmo_id\": \"GMO_001028\",\n          \"label\": \"Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q60","label":"Retained vitamin Pyridoxine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 10 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The attached exact source claim and digest authenticate this retained batch input. Preserve the repaired water unit or mass note without restoring unsupported g/L or transferring the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q61","label":"Retained vitamin Folic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The attached exact source claim and digest authenticate this retained batch input. Preserve the repaired water unit or mass note without restoring unsupported g/L or transferring the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\": \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q62","label":"Retained vitamin Vitamin B12","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 0.1 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The attached exact source claim and digest authenticate this retained batch input. Preserve the repaired water unit or mass note without restoring unsupported g/L or transferring the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q63","label":"Retained vitamin Riboflavin","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[8].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The attached exact source claim and digest authenticate this retained batch input. Preserve the repaired water unit or mass note without restoring unsupported g/L or transferring the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\": \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q64","label":"Retained vitamin Nicotinic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[9].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The attached exact source claim and digest authenticate this retained batch input. Preserve the repaired water unit or mass note without restoring unsupported g/L or transferring the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q65","label":"Retained vitamin Lipoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[10].notes","stored":"Role: Growth factor; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The attached exact source claim and digest authenticate this retained batch input. Preserve the repaired water unit or mass note without restoring unsupported g/L or transferring the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[10]","quote":"{\n          \"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\": \"GMO_001699\",\n          \"label\": \"Lipoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml":null,"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml":["solutions[0].composition","solutions[0].solutions","solutions[1].composition"],"data/normalized_yaml/bacterial/togo_medium_m190.yaml":["solutions[1].composition","solutions[1].preferred_term"]},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:002862.

All selected and scoped dependency primary/secondary slots and preferred-name lookups are joined to current OLS and the exact MIM snapshot. Selected nickel and scoped M180 cobalt/nickel supplied-form contradictions are confirmed; selected cobalt, other named hydrates and sodium propionate are compatible. Generic calcium pantothenate does not establish D stereochemistry and generic vitamin B12 does not establish a specific vitamer. Canonical labels are assessed separately from supplied-form support and linkage denominators.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:002862.

All 11 historical reports are read via lossless current cells: 865 exact personally previously read cells are reused under an explicit proof, and 69 new cells were read now. The J511 plan retains 69 claims, including 39 exact current API objects; its unchanged owner hash and raw digest match current bytes, but no earlier retrieval event or blanket conflict verdict is reenacted. Both stock-repair plan rows match previously read exact rows. Existing scoped batch and root HCl attachments are credited. Current importer behavior is assessed directly, including its bounded molar-stock gap, without attributing historical execution from current code.

## Findings

### f1: Restore liquid stock doses and explicit strengths

major / open / confirmed; issue key: culturemech-002862-liquid-stocks.

The maintained J511 owner and generated target encode 15 mL of 1.0 M sodium propionate, 60 mL of 8% bicarbonate and 8 mL of 5% sodium sulfide nonahydrate as 15, 60 and 8 G_PER_L. Restore the source liquid additions and strengths with their filter/autoclave distinctions, preserving unspecified percent bases. The eight existing basal g/L rates agree with explicit provider main-stage normalization and should not be rejected together with the stock rows.

### f2: Restore iron, trace and vitamin stock boundaries

major / open / confirmed; issue key: culturemech-002862-stock-stages.

Nineteen HCl, iron, trace and vitamin entries retain stock-level numbers as direct-medium g/L. The source instead adds separate iron, trace and vitamin stocks. Restore those stages and receiving doses, retain stock input water and distinguish the HCl 25% mass-basis ambiguity from its explicit 7.7 M reagent strength. Scoped M180/M190 already preserve authenticated batch water, notes and nested HCl; keep those repairs and exclude their parent receiving doses.

### f3: Correct exact nickel and scoped cobalt hydrate mappings

major / open / confirmed; issue key: culturemech-002862-supplied-hydrates.

Selected ingredients[18] names nickel hexahydrate but asserts anhydrous CHEBI:34887 in primary and secondary slots. Scoped M180 trace composition[4] and [5] likewise assert anhydrous cobalt/nickel IDs for explicit hexahydrates. Fresh OLS distinguishes CHEBI:53503 and CHEBI:53542. The selected cobalt hexahydrate mapping is already correct; preserve it and all amounts.

### f4: Complete source attributes while crediting retained preparation

minor / open / confirmed; issue key: culturemech-002862-preparation-evidence.

Both documents already retain the main 4:1 atmosphere, cooling/sterile additions and conditional pH range. Preserve those descriptions and compatible action codes. Add the scoped JCM sterilization default and exact stock attributes lost from the flattened ingredients, attach claim-level evidence to supported existing values, and replace scoped M180 Unknown solution names from their existing preferred terms. No generic claim that preparation is absent is warranted.

### f5: Extend the current importer only for the demonstrated molar-stock case

minor / open / confirmed; issue key: culturemech-002862-current-stock-parser.

Current MediaDive parsing now preserves named and percent-labelled stock additions and limits primary ingredients to the main solution, so it is more conservative than this legacy flattening. Its _is_api_stock_addition recognizes a solution_id or mL with a percent attribute, but the actual J511 sodium-propionate row has a molar attribute and no solution_id. That row remains an ingredient and loses its 1.0 M attribute under _parse_api_composition. Add source-tested handling for this demonstrated molar stock while preserving existing stage guards; bare mL must not be treated as a supported per-final-liter dose.

## Recommended Actions And Acceptance Checks

### a1

The maintained J511 owner and generated target encode 15 mL of 1.0 M sodium propionate, 60 mL of 8% bicarbonate and 8 mL of 5% sodium sulfide nonahydrate as 15, 60 and 8 G_PER_L. Restore the source liquid additions and strengths with their filter/autoclave distinctions, preserving unspecified percent bases. The eight existing basal g/L rates agree with explicit provider main-stage normalization and should not be rejected together with the stock rows.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Nineteen HCl, iron, trace and vitamin entries retain stock-level numbers as direct-medium g/L. The source instead adds separate iron, trace and vitamin stocks. Restore those stages and receiving doses, retain stock input water and distinguish the HCl 25% mass-basis ambiguity from its explicit 7.7 M reagent strength. Scoped M180/M190 already preserve authenticated batch water, notes and nested HCl; keep those repairs and exclude their parent receiving doses.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

Selected ingredients[18] names nickel hexahydrate but asserts anhydrous CHEBI:34887 in primary and secondary slots. Scoped M180 trace composition[4] and [5] likewise assert anhydrous cobalt/nickel IDs for explicit hexahydrates. Fresh OLS distinguishes CHEBI:53503 and CHEBI:53542. The selected cobalt hexahydrate mapping is already correct; preserve it and all amounts.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

Both documents already retain the main 4:1 atmosphere, cooling/sterile additions and conditional pH range. Preserve those descriptions and compatible action codes. Add the scoped JCM sterilization default and exact stock attributes lost from the flattened ingredients, attach claim-level evidence to supported existing values, and replace scoped M180 Unknown solution names from their existing preferred terms. No generic claim that preparation is absent is warranted.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

Current MediaDive parsing now preserves named and percent-labelled stock additions and limits primary ingredients to the main solution, so it is more conservative than this legacy flattening. Its _is_api_stock_addition recognizes a solution_id or mL with a percent attribute, but the actual J511 sodium-propionate row has a molar attribute and no solution_id. That row remains an ingredient and loses its 1.0 M attribute under _parse_api_composition. Add source-tested handling for this demonstrated molar stock while preserving existing stage guards; bare mL must not be treated as a supported per-final-liter dose.

- Verify the exact J511 molar-stock row retains its source strength, liquid dose and stage without affecting named/percent-stock guards.
- Preserve current explicit g_l and conservative merge behavior; add source-specific regression coverage for molar stock attributes.
- Regenerate only after maintained input curation and verify full source-stage equality; do not infer historical execution from current code.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| jcm511 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511; REVIEW_WORK/batch074/source07-08-10/jcm511.json; exact original raw/text/hash/time metadata | context_only | Exact selected JCM511 primary, all printed stocks and main preparation. |
| apiJ511 | https://mediadive.dsmz.de/rest/medium/J511; REVIEW_WORK/batch074/source07-08-10/apiJ511.json; exact original raw/text/hash/time metadata | context_only | Exact providerJ511 underlying selected source. |
| jcm187 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187; REVIEW_WORK/batch074/source07-08-10-shared/jcm187.json; exact original raw/text/hash/time metadata | context_only | JCM187 iron and trace stocks only; parent medium excluded. |
| currentTogo180 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180; REVIEW_WORK/batch074/source07-08-10-shared/currentTogo180.json; exact original raw/text/hash/time metadata | context_only | Exact M180 current iron/trace subsections; parent receiving doses excluded. |
| jcm197 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; REVIEW_WORK/batch074/source07-08-10-shared/jcm197.json; exact original raw/text/hash/time metadata | context_only | JCM197 trace-vitamin stock only; basal parent medium excluded. |
| currentTogo190 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; REVIEW_WORK/batch074/source07-08-10-shared/currentTogo190.json; exact original raw/text/hash/time metadata | context_only | Exact M190 trace-vitamin subsection; parent receiving doses excluded. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; REVIEW_WORK/batch074/source07-08-10/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; REVIEW_WORK/batch074/source07-08-10/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| target | data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/desulfobulbus_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-19 | reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-20 | reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/desulfobulbus_medium.yaml.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-22 | reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M180.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M190.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOBULBUS_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFUROCOCCUS_AMYLOLYTICUS_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-26 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfurococcus_amylolyticus_medium__88cf0911.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-27 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/togo_medium_m190.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-28 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-29 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfobulbus_medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-30 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-31 | reports/yaml_record_review/20260923T163955Z-jcm_medium_no_197.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| dependency-M180 | data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml; solutions[0/1] composition and nested HCl | context_only | Only iron/trace-stock composition, retained batch notes and nested HCl reagent; parent-medium quantities and receiving doses are excluded. Full history is provenance only. |
| dependency-M190 | data/normalized_yaml/bacterial/togo_medium_m190.yaml; solutions[1].composition | context_only | Only trace-vitamin composition and retained batch notes; the parent medium, mineral stock, preparation and receiving dose are excluded. |
| writer-stock-repair | scripts/repair_jcm_stock_preparations.py; Source guards and M180/M190 repair construction | context_only | The current guarded repair preserves stock batch inputs and exact evidence, including nested HCl. Its resulting M180/M190 fields are independently credited; parent formulations are not transferred. |
| historical-reading | REVIEW_WORK/batch074/record10/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch074/record10/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch074/record10/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser excludes percent-stock additions from primary ingredients, preserves referenced stock amounts/attributes separately and prioritizes explicit provider g_l. It skips source water; bare units alone do not establish a final-volume basis. Current code is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| historical-object-joins | REVIEW_WORK/batch074/record10/historical-current-object-joins.json; Complete exact decoded-object comparisons | context_only | Historical object correspondence is distinct from raw-response authentication. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; REVIEW_WORK/batch074/source07-08-10/chebi32149.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; REVIEW_WORK/batch074/source07-08-10/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; REVIEW_WORK/batch074/source07-08-10/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; REVIEW_WORK/batch074/source07-08-10/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; REVIEW_WORK/batch074/source07-08-10/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; REVIEW_WORK/batch074/source07-08-10/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; REVIEW_WORK/batch074/source07-08-10/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; REVIEW_WORK/batch074/source07-08-10/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi132106 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132106; REVIEW_WORK/batch074/source07-08-10/chebi132106.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; REVIEW_WORK/batch074/source07-08-10/chebi32139.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; REVIEW_WORK/batch074/source07-08-10/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; REVIEW_WORK/batch074/source07-08-10/chebi17883.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; REVIEW_WORK/batch074/source07-08-10/chebi86249.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; REVIEW_WORK/batch074/source07-08-10/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; REVIEW_WORK/batch074/source07-08-10/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; REVIEW_WORK/batch074/source07-08-10/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; REVIEW_WORK/batch074/source07-08-10/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; REVIEW_WORK/batch074/source07-08-10/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; REVIEW_WORK/batch074/source07-08-10/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; REVIEW_WORK/batch074/source07-08-10/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; REVIEW_WORK/batch074/source07-08-10/chebi27470.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; REVIEW_WORK/batch074/source07-08-10/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; REVIEW_WORK/batch074/source07-08-10/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; REVIEW_WORK/batch074/source07-08-10/chebi17015.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; REVIEW_WORK/batch074/source07-08-10/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; REVIEW_WORK/batch074/source07-08-10/chebi31345.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; REVIEW_WORK/batch074/source07-08-10/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; REVIEW_WORK/batch074/source07-08-10/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; REVIEW_WORK/batch074/source07-08-10/chebi16494.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; REVIEW_WORK/batch074/source07-08-10/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; REVIEW_WORK/batch074/source07-08-10/chebi35696.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| quantities | REVIEW_WORK/batch074/record10/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch074/record10/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch074/record10/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch074/record10/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch074/record10/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch074/record10/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch074/record10/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch074/record10/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch074/record10/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch074/record10/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch074/record10/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- The current source supports a declared 1010 mL provider normalization, not an independently measured final volume. No unselected historical KOMODO/TOGO sibling formulation or parent-stock receiving dose is transferred. The HCl and late percent-stock mass bases remain unstated.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T184012Z-culturemech-002862-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: DESULFOBULBUS MEDIUM'
started_at: '2026-10-28T18:07:21.956551Z'
finished_at: '2026-10-28T18:40:12.415103Z'
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
summary: The exact J511 identity, eight basal provider rates and existing preparation
  are supported. Three liquid additions and nineteen stock entries remain misrepresented
  as direct masses or final-medium concentrations; bounded hydrate, source-attribute
  and current molar-stock-parser corrections are required. Existing scoped M180/M190
  batch repairs and evidence are preserved.
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
  - path: data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml
    sha256: 655311cb901102709ee383534cfb1b9bbf12e32b2ecb926a55d13097c270b326
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
    role: context
  - path: data/normalized_yaml/bacterial/desulfobulbus_medium.yaml
    sha256: ca6ed643e35f51908de55bcb785b78a17afe0e537f66b9d953a2d604305a6fea
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/desulfobulbus_medium.yaml.md
    sha256: 644c7e39e1ad7dbac49387c766d182f8158beccf3bcd453e6f1e2e6e308fe266
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOBULBUS_MEDIUM.md
    sha256: cecdf8c4926e98bc8d2481f6baba420f058344a8f85580c9307b246acb3a3067
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFUROCOCCUS_AMYLOLYTICUS_MEDIUM.md
    sha256: 432876a053b21f5ac650332fd411f8fb3ee09f57f3321f215d1d174ade488f46
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfobulbus_medium.md
    sha256: 13527fc99094239fbd1eac5b88acd7c2efa8c83dd4abb1336923dc3b280482ac
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md
    sha256: d29c2d8798f20259a253d2b17745d675b4a789de94bdcef5279332d086383022
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
  selection: Authoritative batch074 index 10
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:002862
targets:
- target_id: CultureMech:002862
  path: data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml
  label: desulfobulbus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_medium.yaml
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
  - CultureMech:002862
  command: just validate-schema data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml
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
  - CultureMech:002862
  command: just validate-strict data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml --out
    REVIEW_WORK/batch074/record10/strict.tsv --workers 1 --quiet
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
  - CultureMech:002862
  command: just validate-terms data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml
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
  - CultureMech:002862
  command: just validate-references data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: jcm511
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511
  accessed_at: '2026-10-28T18:07:07.801954Z'
  locator: REVIEW_WORK/batch074/source07-08-10/jcm511.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact selected JCM511 primary, all printed stocks and main preparation.
  snapshot_sha256: ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04
- evidence_id: apiJ511
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J511
  accessed_at: '2026-10-28T18:07:08.090022Z'
  locator: REVIEW_WORK/batch074/source07-08-10/apiJ511.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact providerJ511 underlying selected source.
  snapshot_sha256: 887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6
- evidence_id: jcm187
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187
  accessed_at: '2026-10-28T18:06:53.192282Z'
  locator: REVIEW_WORK/batch074/source07-08-10-shared/jcm187.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: JCM187 iron and trace stocks only; parent medium excluded.
  snapshot_sha256: e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804
- evidence_id: currentTogo180
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180
  accessed_at: '2026-10-28T18:06:53.336358Z'
  locator: REVIEW_WORK/batch074/source07-08-10-shared/currentTogo180.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Exact M180 current iron/trace subsections; parent receiving doses excluded.
  snapshot_sha256: a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba
- evidence_id: jcm197
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  accessed_at: '2026-10-28T18:10:04.175492Z'
  locator: REVIEW_WORK/batch074/source07-08-10-shared/jcm197.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: JCM197 trace-vitamin stock only; basal parent medium excluded.
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: currentTogo190
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  accessed_at: '2026-10-28T18:10:04.334776Z'
  locator: REVIEW_WORK/batch074/source07-08-10-shared/currentTogo190.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Exact M190 trace-vitamin subsection; parent receiving doses excluded.
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  accessed_at: '2026-10-28T18:07:14.309634Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi53503.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  accessed_at: '2026-10-28T18:07:14.366920Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi53542.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T18:29:31.905119Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 655311cb901102709ee383534cfb1b9bbf12e32b2ecb926a55d13097c270b326
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfobulbus_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T18:29:31.905283Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: ca6ed643e35f51908de55bcb785b78a17afe0e537f66b9d953a2d604305a6fea
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T18:29:31.905314Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T18:29:31.905613Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T18:29:31.905642Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T18:29:31.905664Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T18:29:31.905690Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 1db6b2b69fb7a9a131c95c22d837d6a4c5f10dab810921069496169a06d6f5c2
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/desulfobulbus_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T18:29:31.910540Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 644c7e39e1ad7dbac49387c766d182f8158beccf3bcd453e6f1e2e6e308fe266
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T18:29:31.910620Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 00113dc0b556486b52084f2508b061b9a188423d479f8aa102511ec55074ebd5
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M180.md
  locator: Complete report
  accessed_at: '2026-10-28T18:29:31.911018Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 92add964ce82b4d35cd58f93897f8bea6420fd3ce37ce77049e8449173263c30
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M190.md
  locator: Complete report
  accessed_at: '2026-10-28T18:29:31.911067Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 89725cdcefc5da88b06931c4db253e065a5f48c2d2b9c8c0a9bc07f6fdc157e8
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOBULBUS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T18:29:31.911101Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: cecdf8c4926e98bc8d2481f6baba420f058344a8f85580c9307b246acb3a3067
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFUROCOCCUS_AMYLOLYTICUS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T18:29:31.911129Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 432876a053b21f5ac650332fd411f8fb3ee09f57f3321f215d1d174ade488f46
- evidence_id: report-26
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfurococcus_amylolyticus_medium__88cf0911.md
  locator: Complete report
  accessed_at: '2026-10-28T18:29:31.911152Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 7ba8b4c2ac4a371fab0ad69230c1b53376bdcb648cfa0cea53896e1c59ebcdae
- evidence_id: report-27
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/togo_medium_m190.md
  locator: Complete report
  accessed_at: '2026-10-28T18:29:31.911174Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 4ee172b59b8f9a19921c300ecf394dc632e301c0f375a6e86adfade6ec86a619
- evidence_id: report-28
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T18:29:31.911197Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: f7fa9416148a602515b571aedb11d7794ccdd4b2cce57bed8b84b78fc355a46e
- evidence_id: report-29
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfobulbus_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T18:29:31.911220Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 13527fc99094239fbd1eac5b88acd7c2efa8c83dd4abb1336923dc3b280482ac
- evidence_id: report-30
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md
  locator: Complete report
  accessed_at: '2026-10-28T18:29:31.911242Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: d29c2d8798f20259a253d2b17745d675b4a789de94bdcef5279332d086383022
- evidence_id: report-31
  kind: prior_review
  reference: reports/yaml_record_review/20260923T163955Z-jcm_medium_no_197.md
  locator: Complete report
  accessed_at: '2026-10-28T18:29:31.911264Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 6497a50f712e4169a8f7a7cf4ae62d97e909b6695d86b7c522679b8f08909d7f
- evidence_id: dependency-M180
  kind: record_content
  reference: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
  locator: solutions[0/1] composition and nested HCl
  accessed_at: '2026-10-28T18:29:31.935899Z'
  support: context_only
  summary: Only iron/trace-stock composition, retained batch notes and nested HCl
    reagent; parent-medium quantities and receiving doses are excluded. Full history
    is provenance only.
  snapshot_sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
- evidence_id: dependency-M190
  kind: record_content
  reference: data/normalized_yaml/bacterial/togo_medium_m190.yaml
  locator: solutions[1].composition
  accessed_at: '2026-10-28T18:29:31.956889Z'
  support: context_only
  summary: Only trace-vitamin composition and retained batch notes; the parent medium,
    mineral stock, preparation and receiving dose are excluded.
  snapshot_sha256: b1924e7eb436d56c5bd4826f07cafff130341054acfd808fb1c9e5bca914e3fa
- evidence_id: writer-stock-repair
  kind: record_content
  reference: scripts/repair_jcm_stock_preparations.py
  locator: Source guards and M180/M190 repair construction
  accessed_at: '2026-10-28T18:29:31.960638Z'
  support: context_only
  summary: The current guarded repair preserves stock batch inputs and exact evidence,
    including nested HCl. Its resulting M180/M190 fields are independently credited;
    parent formulations are not transferred.
  snapshot_sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch074/record10/historical-reading.json
  accessed_at: '2026-10-28T18:29:31.966381Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: e8926282b45567d51bece4c01f6b1ed7df51b2feb572ab559d0f5e64c1004121
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch074/record10/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T18:29:31.966472Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: b0edce0e09e0bde3d78efa2282369da6e28fc286c8b2a78578f5630337397fe0
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch074/record10/complete-document-reader.json
  accessed_at: '2026-10-28T18:29:31.966833Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: d8d0b20a3f0b6022996bdab606477627d1e4f95aa6c01c9891d6b69fc39cfe98
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T18:29:31.966931Z'
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
  accessed_at: '2026-10-28T18:29:31.966974Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: historical-object-joins
  kind: prior_review
  reference: REVIEW_WORK/batch074/record10/historical-current-object-joins.json
  accessed_at: '2026-10-28T18:29:31.967001Z'
  locator: Complete exact decoded-object comparisons
  support: context_only
  summary: Historical object correspondence is distinct from raw-response authentication.
  snapshot_sha256: ae40865f197604b88588730026253e38b8bc8fc90370f42bc391728374ff11d3
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  accessed_at: '2026-10-28T18:07:13.055617Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi32149.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  accessed_at: '2026-10-28T18:07:14.823259Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi63036.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  accessed_at: '2026-10-28T18:07:12.374274Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi31206.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  accessed_at: '2026-10-28T18:07:11.327883Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi26710.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  accessed_at: '2026-10-28T18:07:15.868993Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi86345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  accessed_at: '2026-10-28T18:07:13.126059Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi32588.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  accessed_at: '2026-10-28T18:07:15.506811Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi86158.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  accessed_at: '2026-10-28T18:07:16.076032Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi8806.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi132106
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132106
  accessed_at: '2026-10-28T18:07:09.399981Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi132106.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: fea2db167b20ccb8e0c62a8571314d91d82c864498b75845a6b6347742ee61d0
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  accessed_at: '2026-10-28T18:07:12.752137Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi32139.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  accessed_at: '2026-10-28T18:07:15.246812Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi76209.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  accessed_at: '2026-10-28T18:07:11.107138Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi17883.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  accessed_at: '2026-10-28T18:07:15.494430Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi86249.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  accessed_at: '2026-10-28T18:07:14.285143Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi49976.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  accessed_at: '2026-10-28T18:07:16.024226Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi86368.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  accessed_at: '2026-10-28T18:07:13.572705Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi33118.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  accessed_at: '2026-10-28T18:07:15.559311Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi86318.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  accessed_at: '2026-10-28T18:07:13.718230Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi34887.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  accessed_at: '2026-10-28T18:07:14.906947Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi75213.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  accessed_at: '2026-10-28T18:07:10.001292Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi15956.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  accessed_at: '2026-10-28T18:07:11.775913Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi27470.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  accessed_at: '2026-10-28T18:07:12.133229Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi30961.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  accessed_at: '2026-10-28T18:07:14.183412Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi49105.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  accessed_at: '2026-10-28T18:07:10.727692Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi17015.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  accessed_at: '2026-10-28T18:07:09.998984Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi15940.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  accessed_at: '2026-10-28T18:07:12.449836Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi31345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  accessed_at: '2026-10-28T18:07:10.636940Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi176843.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  accessed_at: '2026-10-28T18:07:11.948816Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi30753.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  accessed_at: '2026-10-28T18:07:10.033218Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi16494.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  accessed_at: '2026-10-28T18:07:09.866311Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi15377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi35696
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  accessed_at: '2026-10-28T18:07:13.749665Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi35696.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch074/record10/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:29:32.102092Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 05cc434e039d1deeffa8b098e422038ea87db7263c2e3ef2c36494973244355a
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch074/record10/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:29:32.102178Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: f86fed4564ff90543b7be080e3d940d74e8a3daa91ae6dc0770ac18d8d826359
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch074/record10/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:29:32.102319Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 9c01a21c9cbf1ccfa6959a9fe7d2e1d791ec0b458a7d87f385d3b13a4153f946
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch074/record10/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:29:32.102462Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 6d822e523366038ee69945041140c58a45182da6265f8553ae4c14f79d163b95
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch074/record10/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:29:32.102596Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 501639552bdd3b1f9b3e473888a83fefcf0d72648bb42c74414788c9c526e6fe
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch074/record10/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:29:32.102628Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: d72cc0342098f285670d786e2ad94d2312838f8f9225fe30ac02b6c16dd6d788
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch074/record10/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:29:32.102649Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 0c20d32d7b2476a22017f78bbf4927d8124c9d0f96883902de433ab7dfbb7db5
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch074/record10/schema-result.json
  accessed_at: '2026-10-28T18:07:23.000808Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: cd7615947c5fc98f3bee808405e4122ea970a0fe473878bcbe3bf46bbaadaa6a
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch074/record10/strict-result.json
  accessed_at: '2026-10-28T18:07:23.931835Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 18a95ba3d9c320fd5c12154104a13fe1d3557dcc406fd193d554b270978cf439
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch074/record10/terms-result.json
  accessed_at: '2026-10-28T18:07:24.954582Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 1e8adebbbfc714157653dbce97e9e2045776de0ca91dfe77433c37ab2424d0a0
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch074/record10/references-result.json
  accessed_at: '2026-10-28T18:07:25.696866Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: c54740efd08a7400eb5f89d3aa15b2faccc34e765529db86a8f6ba6aec2d29d4
assessments:
- assessment_id: identity
  area: identity
  topic: Current source and owner identity
  outcome: supported
  summary: The current target is generated from exactly one JCM J511 owner. Earlier
    reports describing a three-source group are historical context, not the current
    ownership contract. JCM187 iron/trace and JCM197 vitamin subsections are explicit
    source references; only those dependency sections transfer.
  target_ids:
  - CultureMech:002862
  evidence_ids:
  - target
  - owner
  - jcm511
  - apiJ511
  - historical-reading
- assessment_id: classification
  area: consistency
  topic: Nonquantity assertions and retained metadata
  outcome: supported
  summary: DEFINED composition and LIQUID state agree with the named chemical formulation;
    generic cultivation application establishes no organism growth. The provider pH
    point is within the already-retained primary range. Names, source identity and
    current one-source merge provenance are consistent.
  target_ids:
  - CultureMech:002862
  evidence_ids:
  - target
  - owner
  - jcm511
  - apiJ511
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 65 current concentration fields are covered by 65 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:002862
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b074-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","quantity_field_count":65,"decisions":[{"quantity_id":"q1","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.9703","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.9703","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current value agrees, within displayed rounding, with the explicit provider main-stage
    g_l normalized on its declared 1010 mL basis. The primary batch mass and source
    water/additions agree with that nominal recipe basis. This supports the existing
    rate without asserting measured final volume or an already-attached claim.","source_stage":"main
    medium, declared provider basis","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.9703,\n                        \"mmol_l\":
    20.9117,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML
    table row 0 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>SO<sub>4</sub>
    </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.19802","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.19802","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current value agrees, within displayed rounding, with the explicit provider main-stage
    g_l normalized on its declared 1010 mL basis. The primary batch mass and source
    water/additions agree with that nominal recipe basis. This supports the existing
    rate without asserting measured final volume or an already-attached claim.","source_stage":"main
    medium, declared provider basis","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.19802,\n                        \"mmol_l\":
    1.45511,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML
    table row 1 (zero-based)","quote":"<TR><TD WIDTH=75%> KH<sub>2</sub>PO<sub>4</sub>
    </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.2&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.29703","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.29703","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current value agrees, within displayed rounding, with the explicit provider main-stage
    g_l normalized on its declared 1010 mL basis. The primary batch mass and source
    water/additions agree with that nominal recipe basis. This supports the existing
    rate without asserting measured final volume or an already-attached claim.","source_stage":"main
    medium, declared provider basis","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.29703,\n                        \"mmol_l\":
    5.553,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML
    table row 2 (zero-based)","quote":"<TR><TD WIDTH=75%> NH<sub>4</sub>Cl </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.3&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20.7921","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20.7921","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current value agrees, within displayed rounding, with the explicit provider main-stage
    g_l normalized on its declared 1010 mL basis. The primary batch mass and source
    water/additions agree with that nominal recipe basis. This supports the existing
    rate without asserting measured final volume or an already-attached claim.","source_stage":"main
    medium, declared provider basis","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 21,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 20.7921,\n                        \"mmol_l\":
    355.785,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML
    table row 3 (zero-based)","quote":"<TR><TD WIDTH=75%> NaCl </TD><TD WIDTH=15%
    ALIGN=RIGHT><font size=+1><tt>&nbsp;21.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"MgCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"3.06931","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"3.06931","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current value agrees, within displayed rounding, with the explicit provider main-stage
    g_l normalized on its declared 1010 mL basis. The primary batch mass and source
    water/additions agree with that nominal recipe basis. This supports the existing
    rate without asserting measured final volume or an already-attached claim.","source_stage":"main
    medium, declared provider basis","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 3.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.06931,\n                        \"mmol_l\":
    15.0972,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML
    table row 4 (zero-based)","quote":"<TR><TD WIDTH=75%> MgCl<sub>2</sub>&#183;6H<sub>2</sub>O
    </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.49505","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.49505","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current value agrees, within displayed rounding, with the explicit provider main-stage
    g_l normalized on its declared 1010 mL basis. The primary batch mass and source
    water/additions agree with that nominal recipe basis. This supports the existing
    rate without asserting measured final volume or an already-attached claim.","source_stage":"main
    medium, declared provider basis","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.49505,\n                        \"mmol_l\":
    6.6405,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML
    table row 5 (zero-based)","quote":"<TR><TD WIDTH=75%> KCl </TD><TD WIDTH=15% ALIGN=RIGHT><font
    size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10% ALIGN=RIGHT>
    g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"CaCl2
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.148515","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.148515","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current value agrees, within displayed rounding, with the explicit provider main-stage
    g_l normalized on its declared 1010 mL basis. The primary batch mass and source
    water/additions agree with that nominal recipe basis. This supports the existing
    rate without asserting measured final volume or an already-attached claim.","source_stage":"main
    medium, declared provider basis","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.148515,\n                        \"mmol_l\":
    1.0102,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML
    table row 6 (zero-based)","quote":"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O
    </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.15&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000990099","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000990099","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current value agrees, within displayed rounding, with the explicit provider main-stage
    g_l normalized on its declared 1010 mL basis. The primary batch mass and source
    water/additions agree with that nominal recipe basis. This supports the existing
    rate without asserting measured final volume or an already-attached claim.","source_stage":"main
    medium, declared provider basis","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\":
    25,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.000990099,\n                        \"mmol_l\":
    0.00431999,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML
    table row 9 (zero-based)","quote":"<TR><TD WIDTH=75%> Resazurin </TD><TD WIDTH=15%
    ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"Sodium
    propionate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"15","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored G_PER_L value copies a liquid stock dose in mL. Retain the receiving amount,
    source stock strength and late-addition handling separately. Sodium propionate
    is explicitly 1.0 M and filter-sterilized; do not treat 15 mL as 15 g/L.","source_stage":"post-cooling
    receiving stock dose","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Sodium propionate\",\n                        \"compound_id\":
    1778,\n                        \"attribute\": \"*, 1.0 M\",\n                        \"amount\":
    15,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> 1.0 M Sodium propionate
    solution* </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;15.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"60","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"60","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored G_PER_L value copies a liquid stock dose in mL. Retain the receiving amount,
    source stock strength and late-addition handling separately. The 8% bicarbonate
    stock is filter-sterilized, but the percent basis is unstated; do not derive a
    mass from it.","source_stage":"post-cooling receiving stock dose","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"attribute\": \"*, 8%\",\n                        \"amount\":
    60,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML
    table row 13 (zero-based)","quote":"<TR><TD WIDTH=75%> 8% NaHCO<sub>3</sub> solution*
    </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;60.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"Na2S
    x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored G_PER_L value copies a liquid stock dose in mL. Retain the receiving amount,
    source stock strength and late-addition handling separately. The 5% sodium sulfide
    nonahydrate stock is autoclaved, but the percent basis is unstated; do not derive
    a mass from it.","source_stage":"post-cooling receiving stock dose","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"attribute\": \"5%\",\n                        \"amount\":
    8,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML
    table row 14 (zero-based)","quote":"<TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O
    solution </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;8.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml   </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider reports 2.5 g/L for a 10 mL 25%/7.7 M HCl reagent in the iron stock,
    but the percentage basis is unstated. The retained direct-medium 2.5 g/L is unsupported
    in both stage and mass basis; preserve the explicitly supported reagent strength
    and input dose instead.","source_stage":"iron stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"7.7 M, 25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> 25% HCl (7.7 M)                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"FeCl2
    x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    number is the declared concentration within a named iron, trace-element or vitamin
    stock, not the final receiving medium. Restore the source stock and receiving
    dose; retain the supported stock batch input and do not infer a measured final-stock
    volume from water alone.","source_stage":"iron stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML
    table row 17 (zero-based)","quote":"<TR><TD WIDTH=75%> FeCl<sub>2</sub>&#183;4H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    number is the declared concentration within a named iron, trace-element or vitamin
    stock, not the final receiving medium. Restore the source stock and receiving
    dose; retain the supported stock batch input and do not infer a measured final-stock
    volume from water alone.","source_stage":"trace-element stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML
    table row 19 (zero-based)","quote":"<TR><TD WIDTH=75%> ZnCl<sub>2</sub>                                               </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;70.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"MnCl2
    x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    number is the declared concentration within a named iron, trace-element or vitamin
    stock, not the final receiving medium. Restore the source stock and receiving
    dose; retain the supported stock batch input and do not infer a measured final-stock
    volume from water alone.","source_stage":"trace-element stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML
    table row 20 (zero-based)","quote":"<TR><TD WIDTH=75%> MnCl<sub>2</sub>&#183;4H<sub>2</sub>O                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    number is the declared concentration within a named iron, trace-element or vitamin
    stock, not the final receiving medium. Restore the source stock and receiving
    dose; retain the supported stock batch input and do not infer a measured final-stock
    volume from water alone.","source_stage":"trace-element stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML
    table row 21 (zero-based)","quote":"<TR><TD WIDTH=75%> H<sub>3</sub>BO<sub>3</sub>                                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;6.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q17","label":"CoCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    number is the declared concentration within a named iron, trace-element or vitamin
    stock, not the final receiving medium. Restore the source stock and receiving
    dose; retain the supported stock batch input and do not infer a measured final-stock
    volume from water alone.","source_stage":"trace-element stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML
    table row 22 (zero-based)","quote":"<TR><TD WIDTH=75%> CoCl<sub>2</sub>&#183;6H<sub>2</sub>O                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;190.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q18","label":"CuCl2
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    number is the declared concentration within a named iron, trace-element or vitamin
    stock, not the final receiving medium. Restore the source stock and receiving
    dose; retain the supported stock batch input and do not infer a measured final-stock
    volume from water alone.","source_stage":"trace-element stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[2].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML
    table row 23 (zero-based)","quote":"<TR><TD WIDTH=75%> CuCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q19","label":"NiCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    number is the declared concentration within a named iron, trace-element or vitamin
    stock, not the final receiving medium. Restore the source stock and receiving
    dose; retain the supported stock batch input and do not infer a measured final-stock
    volume from water alone.","source_stage":"trace-element stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[2].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML
    table row 24 (zero-based)","quote":"<TR><TD WIDTH=75%> NiCl<sub>2</sub>&#183;6H<sub>2</sub>O                                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;24.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q20","label":"Na2MoO4
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    number is the declared concentration within a named iron, trace-element or vitamin
    stock, not the final receiving medium. Restore the source stock and receiving
    dose; retain the supported stock batch input and do not infer a measured final-stock
    volume from water alone.","source_stage":"trace-element stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[2].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML
    table row 25 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;36.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q21","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    number is the declared concentration within a named iron, trace-element or vitamin
    stock, not the final receiving medium. Restore the source stock and receiving
    dose; retain the supported stock batch input and do not infer a measured final-stock
    volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.00818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML
    table row 15 (zero-based)","quote":"<TR><TD WIDTH=75%> Biotin                                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"Folic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    number is the declared concentration within a named iron, trace-element or vitamin
    stock, not the final receiving medium. Restore the source stock and receiving
    dose; retain the supported stock batch input and do not infer a measured final-stock
    volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.00453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> Folic acid                                              </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"Pyridoxine
    hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    number is the declared concentration within a named iron, trace-element or vitamin
    stock, not the final receiving medium. Restore the source stock and receiving
    dose; retain the supported stock batch input and do not infer a measured final-stock
    volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 10,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML
    table row 17 (zero-based)","quote":"<TR><TD WIDTH=75%> Pyridoxine&#183;HCl                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"Thiamine
    HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    number is the declared concentration within a named iron, trace-element or vitamin
    stock, not the final receiving medium. Restore the source stock and receiving
    dose; retain the supported stock batch input and do not infer a measured final-stock
    volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML
    table row 18 (zero-based)","quote":"<TR><TD WIDTH=75%> Thiamine&#183;HCl                                      </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    number is the declared concentration within a named iron, trace-element or vitamin
    stock, not the final receiving medium. Restore the source stock and receiving
    dose; retain the supported stock batch input and do not infer a measured final-stock
    volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML
    table row 19 (zero-based)","quote":"<TR><TD WIDTH=75%> Riboflavin                                              </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"Nicotinic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    number is the declared concentration within a named iron, trace-element or vitamin
    stock, not the final receiving medium. Restore the source stock and receiving
    dose; retain the supported stock batch input and do not infer a measured final-stock
    volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML
    table row 20 (zero-based)","quote":"<TR><TD WIDTH=75%> Nicotinic acid                                          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"Calcium
    pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    number is the declared concentration within a named iron, trace-element or vitamin
    stock, not the final receiving medium. Restore the source stock and receiving
    dose; retain the supported stock batch input and do not infer a measured final-stock
    volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\":
    518,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0104925,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML
    table row 21 (zero-based)","quote":"<TR><TD WIDTH=75%> Calcium pantothenate                                    </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Vitamin
    B12","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.0001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.0001","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    number is the declared concentration within a named iron, trace-element or vitamin
    stock, not the final receiving medium. Restore the source stock and receiving
    dose; retain the supported stock batch input and do not infer a measured final-stock
    volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0001,\n                        \"mmol_l\":
    7.3779e-5,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML
    table row 22 (zero-based)","quote":"<TR><TD WIDTH=75%> Vitamin B<sub>1</sub><sub>2</sub>                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"p-Aminobenzoic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    number is the declared concentration within a named iron, trace-element or vitamin
    stock, not the final receiving medium. Restore the source stock and receiving
    dose; retain the supported stock batch input and do not infer a measured final-stock
    volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML
    table row 23 (zero-based)","quote":"<TR><TD WIDTH=75%> <I>p</I>-Aminobenzoic acid                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"Lipoic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.005","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    number is the declared concentration within a named iron, trace-element or vitamin
    stock, not the final receiving medium. Restore the source stock and receiving
    dose; retain the supported stock batch input and do not infer a measured final-stock
    volume from water alone.","source_stage":"vitamin stock","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Lipoic acid\",\n                        \"compound_id\":
    368,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.024233,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML
    table row 24 (zero-based)","quote":"<TR><TD WIDTH=75%> Lipoic acid                                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"Main
    water","local_fields":[],"decision":"evidence_only","rationale":"Preserve this
    exact source input or receiving dose in its named stage. Input water is not a
    measured final volume, and parent-medium doses of linked dependency documents
    are excluded.","source_stage":"source-only main water","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 915,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML
    table row 10 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;915.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml   </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q32","label":"Iron-stock
    receiving dose","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this exact source input or receiving dose in its named stage. Input water is not
    a measured final volume, and parent-medium doses of linked dependency documents
    are excluded.","source_stage":"source-only iron-stock receiving dose","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"FeCl2 solution\",\n                        \"solution_id\":
    3846,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> FeCl<sub>2</sub> solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>) </TD><TD WIDTH=15%
    ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q33","label":"Trace-stock
    receiving dose","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this exact source input or receiving dose in its named stage. Input water is not
    a measured final volume, and parent-medium doses of linked dependency documents
    are excluded.","source_stage":"source-only trace-stock receiving dose","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\":
    3847,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML
    table row 8 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution (see
    Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>) </TD><TD WIDTH=15%
    ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q34","label":"Vitamin-stock
    receiving dose","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this exact source input or receiving dose in its named stage. Input water is not
    a measured final volume, and parent-medium doses of linked dependency documents
    are excluded.","source_stage":"source-only vitamin-stock receiving dose","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\":
    3861,\n                        \"attribute\": \"*\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"HTML
    table row 12 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace vitamins* (see Medium
    No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=197\">197</a>) </TD><TD WIDTH=15% ALIGN=RIGHT><font
    size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10% ALIGN=RIGHT>
    ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q35","label":"Iron-stock
    input water","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this exact source input or receiving dose in its named stage. Input water is not
    a measured final volume, and parent-medium doses of linked dependency documents
    are excluded.","source_stage":"source-only iron-stock input water","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 990,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML
    table row 18 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q36","label":"Trace-stock
    input water","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this exact source input or receiving dose in its named stage. Input water is not
    a measured final volume, and parent-medium doses of linked dependency documents
    are excluded.","source_stage":"source-only trace-stock input water","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[2].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch074/source09-extra/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"646cb82d9d6720cfffadaf74b7f5194e027f05b937c0011b24b8004b301cc27f","accessed_at":"2026-10-28T18:06:53.192282Z","locator":"HTML
    table row 26 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L        </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q37","label":"Vitamin-stock
    input water","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    this exact source input or receiving dose in its named stage. Input water is not
    a measured final volume, and parent-medium doses of linked dependency documents
    are excluded.","source_stage":"source-only vitamin-stock input water","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[3].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch074/publish-sources/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T18:10:04.175492Z","locator":"HTML
    table row 25 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q38","label":"Retained
    main preparation","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"preparation_steps[0].description","stored":"Mix
    components thoroughly and autoclave under a N2-CO2 (4:1, v/v) gas atmosphere.
    After cooling, aseptically and anaerobically add the following solutions (autoclaved
    or *filter-sterilized):"},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"preparation_steps[0].description","stored":"Mix
    components thoroughly and autoclave under a N2-CO2 (4:1, v/v) gas atmosphere.
    After cooling, aseptically and anaerobically add the following solutions (autoclaved
    or *filter-sterilized):"}],"decision":"evidence_only","rationale":"The complete
    existing sentence retains the 4:1 N2/CO2 atmosphere, cooling, aseptic anaerobic
    addition and distinction between autoclaved or starred filter-sterilized stocks.
    Credit that text; restoring each missing stock attribute makes its starred references
    usable.","source_stage":"main preparation","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"step\": \"Mix components thoroughly and autoclave
    under a N2-CO2 (4:1, v/v) gas atmosphere. After cooling, aseptically and anaerobically
    add the following solutions (autoclaved or *filter-sterilized): \"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q39","label":"Retained pH instruction","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"preparation_steps[1].description","stored":"Adjust
    pH to 7.1 - 7.4, if necessary."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"preparation_steps[1].description","stored":"Adjust
    pH to 7.1 - 7.4, if necessary."}],"decision":"evidence_only","rationale":"The
    existing conditional pH 7.1–7.4 instruction matches the primary and provider step.
    Preserve the whole range and if-necessary qualification.","source_stage":"main
    preparation","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\":
    \"Adjust pH to 7.1 - 7.4, if necessary.\"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q40","label":"Current pH point","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml","field_path":"ph_value","stored":7.2}],"decision":"evidence_only","rationale":"The
    provider metadata gives pH 7.2, within the primary conditional 7.1–7.4 range already
    retained in preparation. Keep its provider-point provenance separate from the
    broader primary range.","source_stage":"provider metadata and primary range","sources":[{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.medium","quote":"{\n            \"id\":
    \"J511\",\n            \"name\": \"DESULFOBULBUS MEDIUM\",\n            \"complex_medium\":
    \"no\",\n            \"min_pH\": 7.2,\n            \"max_pH\": 7.2,\n            \"source\":
    \"JCM\",\n            \"link\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511\"\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ511","reference":"https://mediadive.dsmz.de/rest/medium/J511","raw_path":"REVIEW_WORK/batch074/source07-08-10/apiJ511.raw","raw_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","text_sha256":"887c2bd25645490fef73a584d90a554b4c53ead71c55a8126560813745184bf6","accessed_at":"2026-10-28T18:07:08.090022Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\":
    \"Adjust pH to 7.1 - 7.4, if necessary.\"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q41","label":"JCM default sterilization","local_fields":[],"decision":"evidence_only","rationale":"The
    primary default states 121 C for 15 min unless otherwise specified. Add it only
    with its default scope; explicit starred filter-sterilized stocks remain separate.","source_stage":"source-only
    default sterilization","sources":[{"evidence_id":"jcm511","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=511","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm511.raw","raw_sha256":"ab691429875920f14cd15501e79fc3fd85cb44c6239cca92a79038d1f4a3fe04","text_sha256":"5a29baf0848f0a3a25afeda6bedb626ec5a22d341c0ce0ddf273675b39c7dd7c","accessed_at":"2026-10-28T18:07:07.801954Z","locator":"jcm511.txt
    lines 4-4","quote":"Unless otherwise stated, sterilize media by autoclaving at
    121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q42","label":"Retained
    M180 Distilled water","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[0].concentration","stored":{"value":"0.99","unit":"L"}}],"decision":"verified","rationale":"Existing
    attached literal source claim and its original digest match the current source
    bytes. Retain this exact stock batch input, not a measured final-volume concentration;
    historical duplicate notes are superseded context.","source_stage":"M180 iron
    or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q43","label":"Retained
    M180 FeCl2・4H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[1].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 1.5 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing attached literal
    source claim and its original digest match the current source bytes. Retain this
    exact stock batch input, not a measured final-volume concentration; historical
    duplicate notes are superseded context.","source_stage":"M180 iron or trace stock
    only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q44","label":"Retained
    M180 Distilled water","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"Existing
    attached literal source claim and its original digest match the current source
    bytes. Retain this exact stock batch input, not a measured final-volume concentration;
    historical duplicate notes are superseded context.","source_stage":"M180 iron
    or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q45","label":"Retained
    M180 Na2MoO4・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 36 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing attached literal
    source claim and its original digest match the current source bytes. Retain this
    exact stock batch input, not a measured final-volume concentration; historical
    duplicate notes are superseded context.","source_stage":"M180 iron or trace stock
    only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q46","label":"Retained
    M180 H3BO3","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 6 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing attached literal
    source claim and its original digest match the current source bytes. Retain this
    exact stock batch input, not a measured final-volume concentration; historical
    duplicate notes are superseded context.","source_stage":"M180 iron or trace stock
    only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q47","label":"Retained
    M180 MnCl2・4H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 100 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing attached literal
    source claim and its original digest match the current source bytes. Retain this
    exact stock batch input, not a measured final-volume concentration; historical
    duplicate notes are superseded context.","source_stage":"M180 iron or trace stock
    only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q48","label":"Retained
    M180 CoCl2・6H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 190 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing attached literal
    source claim and its original digest match the current source bytes. Retain this
    exact stock batch input, not a measured final-volume concentration; historical
    duplicate notes are superseded context.","source_stage":"M180 iron or trace stock
    only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q49","label":"Retained
    M180 NiCl2・6H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 24 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing attached literal
    source claim and its original digest match the current source bytes. Retain this
    exact stock batch input, not a measured final-volume concentration; historical
    duplicate notes are superseded context.","source_stage":"M180 iron or trace stock
    only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q50","label":"Retained
    M180 CuCl2・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 2 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing attached literal
    source claim and its original digest match the current source bytes. Retain this
    exact stock batch input, not a measured final-volume concentration; historical
    duplicate notes are superseded context.","source_stage":"M180 iron or trace stock
    only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q51","label":"Retained
    M180 ZnCl2","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 70 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing attached literal
    source claim and its original digest match the current source bytes. Retain this
    exact stock batch input, not a measured final-volume concentration; historical
    duplicate notes are superseded context.","source_stage":"M180 iron or trace stock
    only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q52","label":"Retained
    nested HCl solutions[0].solutions[0].composition[0].concentration","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].composition[0].concentration","stored":{"value":"7.7","unit":"MOLAR"}}],"decision":"verified","rationale":"Explicit
    7.7 M reagent strength is supported by its attached exact claim; the accompanying
    25% basis is unspecified.","source_stage":"M180 iron-stock nested reagent","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q53","label":"Retained
    nested HCl solutions[0].solutions[0].concentration","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].concentration","stored":{"value":"0.01","unit":"L"}}],"decision":"verified","rationale":"The
    root evidence contains an additional exact HCl excerpt and this nested descriptor
    locator, authenticating 10 mL = 0.01 L into the iron stock; it is not the excluded
    parent-medium receiving dose.","source_stage":"M180 iron-stock nested reagent","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q54","label":"Retained
    HCl input-dose note","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].notes","stored":"Source
    stock addition: 10 ml = 0.01 L per receiving batch, not grams per liter or a dose
    per final liter."}],"decision":"verified","rationale":"The retained numeric note
    has the same exact scoped root attachment as the nested descriptor; no new dose
    or final concentration is inferred.","source_stage":"M180 nested HCl","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q55","label":"Retained
    vitamin Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"The
    attached exact source claim and digest authenticate this retained batch input.
    Preserve the repaired water unit or mass note without restoring unsupported g/L
    or transferring the parent receiving dose.","source_stage":"M190 vitamin stock
    only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    vitamin Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 2 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The attached exact source
    claim and digest authenticate this retained batch input. Preserve the repaired
    water unit or mass note without restoring unsupported g/L or transferring the
    parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q57","label":"Retained vitamin p--Aminobenzoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The attached exact source
    claim and digest authenticate this retained batch input. Preserve the repaired
    water unit or mass note without restoring unsupported g/L or transferring the
    parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q58","label":"Retained vitamin Thiamine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The attached exact source
    claim and digest authenticate this retained batch input. Preserve the repaired
    water unit or mass note without restoring unsupported g/L or transferring the
    parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q59","label":"Retained vitamin Calcium pantothenate","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The attached exact source
    claim and digest authenticate this retained batch input. Preserve the repaired
    water unit or mass note without restoring unsupported g/L or transferring the
    parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q60","label":"Retained vitamin Pyridoxine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 10 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The attached exact source
    claim and digest authenticate this retained batch input. Preserve the repaired
    water unit or mass note without restoring unsupported g/L or transferring the
    parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q61","label":"Retained vitamin Folic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 2 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The attached exact source
    claim and digest authenticate this retained batch input. Preserve the repaired
    water unit or mass note without restoring unsupported g/L or transferring the
    parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q62","label":"Retained vitamin Vitamin B12","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 0.1 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The attached exact source
    claim and digest authenticate this retained batch input. Preserve the repaired
    water unit or mass note without restoring unsupported g/L or transferring the
    parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q63","label":"Retained vitamin Riboflavin","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[8].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The attached exact source
    claim and digest authenticate this retained batch input. Preserve the repaired
    water unit or mass note without restoring unsupported g/L or transferring the
    parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q64","label":"Retained vitamin Nicotinic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[9].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The attached exact source
    claim and digest authenticate this retained batch input. Preserve the repaired
    water unit or mass note without restoring unsupported g/L or transferring the
    parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q65","label":"Retained vitamin Lipoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[10].notes","stored":"Role:
    Growth factor; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The attached exact source
    claim and digest authenticate this retained batch input. Preserve the repaired
    water unit or mass note without restoring unsupported g/L or transferring the
    parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[10]","quote":"{\n          \"component_name\":
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
    UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/DESULFOBULBUS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/desulfobulbus_medium.yaml":null,"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml":["solutions[0].composition","solutions[0].solutions","solutions[1].composition"],"data/normalized_yaml/bacterial/togo_medium_m190.yaml":["solutions[1].composition","solutions[1].preferred_term"]},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All selected and scoped dependency primary/secondary slots and preferred-name
    lookups are joined to current OLS and the exact MIM snapshot. Selected nickel
    and scoped M180 cobalt/nickel supplied-form contradictions are confirmed; selected
    cobalt, other named hydrates and sodium propionate are compatible. Generic calcium
    pantothenate does not establish D stereochemistry and generic vitamin B12 does
    not establish a specific vitamer. Canonical labels are assessed separately from
    supplied-form support and linkage denominators.
  target_ids:
  - CultureMech:002862
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: 'All 11 historical reports are read via lossless current cells: 865 exact
    personally previously read cells are reused under an explicit proof, and 69 new
    cells were read now. The J511 plan retains 69 claims, including 39 exact current
    API objects; its unchanged owner hash and raw digest match current bytes, but
    no earlier retrieval event or blanket conflict verdict is reenacted. Both stock-repair
    plan rows match previously read exact rows. Existing scoped batch and root HCl
    attachments are credited. Current importer behavior is assessed directly, including
    its bounded molar-stock gap, without attributing historical execution from current
    code.'
  target_ids:
  - CultureMech:002862
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
  - historical-object-joins
  - writer-mediadive
findings:
- finding_id: f1
  issue_key: culturemech-002862-liquid-stocks
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore liquid stock doses and explicit strengths
  description: The maintained J511 owner and generated target encode 15 mL of 1.0
    M sodium propionate, 60 mL of 8% bicarbonate and 8 mL of 5% sodium sulfide nonahydrate
    as 15, 60 and 8 G_PER_L. Restore the source liquid additions and strengths with
    their filter/autoclave distinctions, preserving unspecified percent bases. The
    eight existing basal g/L rates agree with explicit provider main-stage normalization
    and should not be rejected together with the stock rows.
  target_ids:
  - CultureMech:002862
  field_paths:
  - ingredients[8].concentration
  - ingredients[9].concentration
  - ingredients[10].concentration
  evidence_ids:
  - jcm511
  - apiJ511
  - quantities
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-002862-stock-stages
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore iron, trace and vitamin stock boundaries
  description: Nineteen HCl, iron, trace and vitamin entries retain stock-level numbers
    as direct-medium g/L. The source instead adds separate iron, trace and vitamin
    stocks. Restore those stages and receiving doses, retain stock input water and
    distinguish the HCl 25% mass-basis ambiguity from its explicit 7.7 M reagent strength.
    Scoped M180/M190 already preserve authenticated batch water, notes and nested
    HCl; keep those repairs and exclude their parent receiving doses.
  target_ids:
  - CultureMech:002862
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - jcm511
  - jcm187
  - jcm197
  - apiJ511
  - quantities
  - old-claims
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/togo_medium_m190.yaml
    role: scoped dependency
- finding_id: f3
  issue_key: culturemech-002862-supplied-hydrates
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Correct exact nickel and scoped cobalt hydrate mappings
  description: Selected ingredients[18] names nickel hexahydrate but asserts anhydrous
    CHEBI:34887 in primary and secondary slots. Scoped M180 trace composition[4] and
    [5] likewise assert anhydrous cobalt/nickel IDs for explicit hexahydrates. Fresh
    OLS distinguishes CHEBI:53503 and CHEBI:53542. The selected cobalt hexahydrate
    mapping is already correct; preserve it and all amounts.
  target_ids:
  - CultureMech:002862
  field_paths:
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[1].composition[4].term
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[1].composition[5].term
  evidence_ids:
  - jcm187
  - apiJ511
  - currentTogo180
  - chebi34887
  - chebi35696
  - chebi53503
  - chebi53542
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    role: scoped dependency
- finding_id: f4
  issue_key: culturemech-002862-preparation-evidence
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Complete source attributes while crediting retained preparation
  description: Both documents already retain the main 4:1 atmosphere, cooling/sterile
    additions and conditional pH range. Preserve those descriptions and compatible
    action codes. Add the scoped JCM sterilization default and exact stock attributes
    lost from the flattened ingredients, attach claim-level evidence to supported
    existing values, and replace scoped M180 Unknown solution names from their existing
    preferred terms. No generic claim that preparation is absent is warranted.
  target_ids:
  - CultureMech:002862
  field_paths:
  - preparation_steps
  - sterilization
  - evidence
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[0].name
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[1].name
  evidence_ids:
  - jcm511
  - apiJ511
  - quantities
  - old-claims
  rule_id: review-yaml-record/completeness
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    role: scoped dependency
- finding_id: f5
  issue_key: culturemech-002862-current-stock-parser
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Extend the current importer only for the demonstrated molar-stock case
  description: Current MediaDive parsing now preserves named and percent-labelled
    stock additions and limits primary ingredients to the main solution, so it is
    more conservative than this legacy flattening. Its _is_api_stock_addition recognizes
    a solution_id or mL with a percent attribute, but the actual J511 sodium-propionate
    row has a molar attribute and no solution_id. That row remains an ingredient and
    loses its 1.0 M attribute under _parse_api_composition. Add source-tested handling
    for this demonstrated molar stock while preserving existing stage guards; bare
    mL must not be treated as a supported per-final-liter dose.
  target_ids:
  - CultureMech:002862
  field_paths:
  - ingredients[8]
  - src/culturemech/import/mediadive_importer.py::_is_api_stock_addition
  evidence_ids:
  - apiJ511
  - writer-mediadive
  rule_id: review-yaml-record/representation
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: maintained importer
actions:
- action_id: a1
  description: The maintained J511 owner and generated target encode 15 mL of 1.0
    M sodium propionate, 60 mL of 8% bicarbonate and 8 mL of 5% sodium sulfide nonahydrate
    as 15, 60 and 8 G_PER_L. Restore the source liquid additions and strengths with
    their filter/autoclave distinctions, preserving unspecified percent bases. The
    eight existing basal g/L rates agree with explicit provider main-stage normalization
    and should not be rejected together with the stock rows.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002862
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_medium.yaml
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
  description: Nineteen HCl, iron, trace and vitamin entries retain stock-level numbers
    as direct-medium g/L. The source instead adds separate iron, trace and vitamin
    stocks. Restore those stages and receiving doses, retain stock input water and
    distinguish the HCl 25% mass-basis ambiguity from its explicit 7.7 M reagent strength.
    Scoped M180/M190 already preserve authenticated batch water, notes and nested
    HCl; keep those repairs and exclude their parent receiving doses.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002862
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    role: scoped dependency
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
- action_id: a3
  description: Selected ingredients[18] names nickel hexahydrate but asserts anhydrous
    CHEBI:34887 in primary and secondary slots. Scoped M180 trace composition[4] and
    [5] likewise assert anhydrous cobalt/nickel IDs for explicit hexahydrates. Fresh
    OLS distinguishes CHEBI:53503 and CHEBI:53542. The selected cobalt hexahydrate
    mapping is already correct; preserve it and all amounts.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002862
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_medium.yaml
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
  description: Both documents already retain the main 4:1 atmosphere, cooling/sterile
    additions and conditional pH range. Preserve those descriptions and compatible
    action codes. Add the scoped JCM sterilization default and exact stock attributes
    lost from the flattened ingredients, attach claim-level evidence to supported
    existing values, and replace scoped M180 Unknown solution names from their existing
    preferred terms. No generic claim that preparation is absent is warranted.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:002862
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_medium.yaml
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
- action_id: a5
  description: Current MediaDive parsing now preserves named and percent-labelled
    stock additions and limits primary ingredients to the main solution, so it is
    more conservative than this legacy flattening. Its _is_api_stock_addition recognizes
    a solution_id or mL with a percent attribute, but the actual J511 sodium-propionate
    row has a molar attribute and no solution_id. That row remains an ingredient and
    loses its 1.0 M attribute under _parse_api_composition. Add source-tested handling
    for this demonstrated molar stock while preserving existing stage guards; bare
    mL must not be treated as a supported per-final-liter dose.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:002862
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: maintained importer
  acceptance_checks:
  - Verify the exact J511 molar-stock row retains its source strength, liquid dose
    and stage without affecting named/percent-stock guards.
  - Preserve current explicit g_l and conservative merge behavior; add source-specific
    regression coverage for molar stock attributes.
  - Regenerate only after maintained input curation and verify full source-stage equality;
    do not infer historical execution from current code.
  generator: Maintained MediaDive importer
limitations:
- The current source supports a declared 1010 mL provider normalization, not an independently
  measured final volume. No unselected historical KOMODO/TOGO sibling formulation
  or parent-stock receiving dose is transferred. The HCl and late percent-stock mass
  bases remain unstated.
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
