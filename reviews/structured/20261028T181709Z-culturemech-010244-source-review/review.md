# Scientific review: Desulfitocella Medium

- Review: 20261028T181709Z-culturemech-010244-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T18:06:48.064965Z
- Finished UTC: 2026-10-28T18:17:09.697988Z
- Reviewer: Codex batch006_validation (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM796 identity and source batch amounts are supported, but water, resazurin and six stock additions have incorrect units and other local per-litre bases remain unproven. The exact JCM483 microelements, supplied forms and staged preparation need scoped curation. Truthful unquantified placeholders and correct retained identities are credited; all four original diagnostics passed.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch074 index 02
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010244 | data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml | generated | desulfitocella_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:010244 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:010244 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:010244 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:010244 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### JCM796 and scoped JCM483 identity

identity: supported. Targets: CultureMech:010244.

The exact JCM796 title and complete tables agree with TOGO M830. Its trace reference resolves to JCM483 / TOGO M484 microelements only; the parent recipe and receiving dose are excluded.

### Complex liquid medium

scope: supported. Targets: CultureMech:010244.

Yeast extract and branded Trypticase support complex/undefined classification; no gelling agent is supplied. No organism-growth claim is inferred.

### Source batches, stocks and absent claims

evidence: concern. Targets: CultureMech:010244.

All exact source rows are retained. Wrong units, unsupported local per-litre bases, empty scoped stock and absent preparation require curation; truthful gas/KOH placeholders and correct chemical identities are credited.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:010244.

50 current concentration fields are covered by 32 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b074-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","quantity_field_count":50,"decisions":[{"quantity_id":"q1","label":"Distilled water","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"925","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"925","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source specifies 925 ml input water, not 925 g/L. Correct the quantity representation as source batch volume without assuming water density or a measured final medium volume.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 925,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML table row 12 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;925.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 925,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The source specifies 925 ml input water, not 925 g/L. Correct the quantity representation as source batch volume without assuming water density or a measured final medium volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The source specifies 925 ml input water, not 925 g/L. Correct the quantity representation as source batch volume without assuming water density or a measured final medium volume."}]},{"quantity_id":"q2","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\": \"Yeast extract\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\": \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\": \"Nutrient source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML table row 8 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Yeast extract                                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.999001,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."}]},{"quantity_id":"q3","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML table row 3 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.999001,\n                        \"mmol_l\": 17.0945,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."}]},{"quantity_id":"q4","label":"CaCl2・2H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML table row 5 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0999001,\n                        \"mmol_l\": 0.679523,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."}]},{"quantity_id":"q5","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 0.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML table row 0 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.3&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2997,\n                        \"mmol_l\": 2.20229,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."}]},{"quantity_id":"q6","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\": \"NH4Cl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\": \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML table row 2 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NH&lt;sub&gt;4&lt;/sub&gt;Cl                                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.999001,\n                        \"mmol_l\": 18.6764,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."}]},{"quantity_id":"q7","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\": \"K2HPO4\",\n          \"volume\": 0.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\": \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML table row 1 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; K&lt;sub&gt;2&lt;/sub&gt;HPO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.3&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2997,\n                        \"mmol_l\": 1.72068,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."}]},{"quantity_id":"q8","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact primary and TOGO source specify 1 mg resazurin, not 1 g/L. Preserve the batch mass and neutral resazurin identity; APIJ796 separately declares 0.000999001 g_l on its computational 1001 ml basis.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\": \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\": \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent redox indicator\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Resazurin                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.000999001,\n                        \"mmol_l\": 0.00435883,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"correct","rationale":"The exact primary and TOGO source specify 1 mg resazurin, not 1 g/L. Preserve the batch mass and neutral resazurin identity; APIJ796 separately declares 0.000999001 g_l on its computational 1001 ml basis."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[7].concentration","decision":"correct","rationale":"The exact primary and TOGO source specify 1 mg resazurin, not 1 g/L. Preserve the batch mass and neutral resazurin identity; APIJ796 separately declares 0.000999001 g_l on its computational 1001 ml basis."}]},{"quantity_id":"q9","label":"MgCl2・6H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\": \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML table row 4 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.499501,\n                        \"mmol_l\": 2.45693,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."}]},{"quantity_id":"q10","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\": \"KCl\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\": \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML table row 6 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; KCl                                                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0999001,\n                        \"mmol_l\": 1.34004,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."}]},{"quantity_id":"q11","label":"Trypticase peptone (BD-BBL)","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\": \"Trypticase peptone (BD-BBL)\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001097\",\n          \"gmo_id\": \"GMO_001097\",\n          \"label\": \"BBL &amp;trade; Trypticase peptone\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML table row 9 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trypticase peptone (BD-BBL)                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\": 124,\n                        \"attribute\": \"BD-BBL\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.999001,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."}]},{"quantity_id":"q12","label":"L--Cysteine・HCl・H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[11]","quote":"{\n          \"component_name\": \"L--Cysteine・HCl・H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001205\",\n          \"gmo_id\": \"GMO_001205\",\n          \"label\": \"L-Cysteine hydrochloride monohydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML table row 10 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; L-Cysteine&amp;#183;HCl&amp;#183;H&lt;sub&gt;2&lt;/sub&gt;O                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.499501,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"The printed batch mass is supported, but its stored G_PER_L basis is not established by the primary water input. Current APIJ796 declares a separate 1001 ml computational normalization with a different g_l; do not silently transfer that provider rate or claim measured final volume. Retain the exact primary batch mass and qualify the local denominator."}]},{"quantity_id":"q13","label":"KOH","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"The VARIABLE amount truthfully represents an unquantified source addition. Retain it and attach the exact preparation context; KOH pH adjustment and the 4:1 N2/CO2 gas ratio do not specify a reagent mass or gas volume.","source_stage":"main preparation","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[13]","quote":"{\n          \"component_name\": \"KOH\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001903\",\n          \"gmo_id\": \"GMO_001903\",\n          \"label\": \"Potassium hydroxide solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly, adjust pH to 7.0 with KOH, distribute the medium into culture vessels under a N2--CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per 925 ml the following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"evidence_only","rationale":"The VARIABLE amount truthfully represents an unquantified source addition. Retain it and attach the exact preparation context; KOH pH adjustment and the 4:1 N2/CO2 gas ratio do not specify a reagent mass or gas volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[12].concentration","decision":"evidence_only","rationale":"The VARIABLE amount truthfully represents an unquantified source addition. Retain it and attach the exact preparation context; KOH pH adjustment and the 4:1 N2/CO2 gas ratio do not specify a reagent mass or gas volume."}]},{"quantity_id":"q14","label":"Carbon dioxide gas","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"The VARIABLE amount truthfully represents an unquantified source addition. Retain it and attach the exact preparation context; KOH pH adjustment and the 4:1 N2/CO2 gas ratio do not specify a reagent mass or gas volume.","source_stage":"main preparation","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[14]","quote":"{\n          \"component_name\": \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\": \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly, adjust pH to 7.0 with KOH, distribute the medium into culture vessels under a N2--CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per 925 ml the following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"evidence_only","rationale":"The VARIABLE amount truthfully represents an unquantified source addition. Retain it and attach the exact preparation context; KOH pH adjustment and the 4:1 N2/CO2 gas ratio do not specify a reagent mass or gas volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[13].concentration","decision":"evidence_only","rationale":"The VARIABLE amount truthfully represents an unquantified source addition. Retain it and attach the exact preparation context; KOH pH adjustment and the 4:1 N2/CO2 gas ratio do not specify a reagent mass or gas volume."}]},{"quantity_id":"q15","label":"Nitrogen gas","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"The VARIABLE amount truthfully represents an unquantified source addition. Retain it and attach the exact preparation context; KOH pH adjustment and the 4:1 N2/CO2 gas ratio do not specify a reagent mass or gas volume.","source_stage":"main preparation","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[15]","quote":"{\n          \"component_name\": \"Nitrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly, adjust pH to 7.0 with KOH, distribute the medium into culture vessels under a N2--CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per 925 ml the following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"evidence_only","rationale":"The VARIABLE amount truthfully represents an unquantified source addition. Retain it and attach the exact preparation context; KOH pH adjustment and the 4:1 N2/CO2 gas ratio do not specify a reagent mass or gas volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[14].concentration","decision":"evidence_only","rationale":"The VARIABLE amount truthfully represents an unquantified source addition. Retain it and attach the exact preparation context; KOH pH adjustment and the 4:1 N2/CO2 gas ratio do not specify a reagent mass or gas volume."}]},{"quantity_id":"q16","label":"Microelement solution (see Medium [M484])","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source supplies a stock addition in ml, not a mass concentration. Preserve this exact batch addition and its separately stated stock strength; do not convert bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and 100 mg/L strengths are explicit and distinct from addition volumes.","source_stage":"receiving stock addition","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[12]","quote":"{\n          \"component_name\": \"Microelement solution (see Medium [M484])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M484\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=483\"&gt;483&lt;/a&gt;)           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Trace element solution\",\n                        \"compound_id\": 96,\n                        \"attribute\": \"see Medium No. 483\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[0].concentration","decision":"correct","rationale":"The source supplies a stock addition in ml, not a mass concentration. Preserve this exact batch addition and its separately stated stock strength; do not convert bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and 100 mg/L strengths are explicit and distinct from addition volumes."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[0].concentration","decision":"correct","rationale":"The source supplies a stock addition in ml, not a mass concentration. Preserve this exact batch addition and its separately stated stock strength; do not convert bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and 100 mg/L strengths are explicit and distinct from addition volumes."}]},{"quantity_id":"q17","label":"8% NaHCO3 solution*","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"25","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"25","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source supplies a stock addition in ml, not a mass concentration. Preserve this exact batch addition and its separately stated stock strength; do not convert bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and 100 mg/L strengths are explicit and distinct from addition volumes.","source_stage":"receiving stock addition","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"8% NaHCO3 solution*\",\n          \"volume\": 25,\n          \"unit\": \"ml\",\n          \"conc_value\": 8,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001119\",\n          \"gmo_id\": \"GMO_001119\",\n          \"label\": \"Sodium bicarbonate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML table row 13 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 8% NaHCO3 solution*                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;25.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"attribute\": \"*, 8%\",\n                        \"amount\": 25,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[1].concentration","decision":"correct","rationale":"The source supplies a stock addition in ml, not a mass concentration. Preserve this exact batch addition and its separately stated stock strength; do not convert bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and 100 mg/L strengths are explicit and distinct from addition volumes."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[1].concentration","decision":"correct","rationale":"The source supplies a stock addition in ml, not a mass concentration. Preserve this exact batch addition and its separately stated stock strength; do not convert bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and 100 mg/L strengths are explicit and distinct from addition volumes."}]},{"quantity_id":"q18","label":"0.1 M Sodium sulfite solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[2].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source supplies a stock addition in ml, not a mass concentration. Preserve this exact batch addition and its separately stated stock strength; do not convert bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and 100 mg/L strengths are explicit and distinct from addition volumes.","source_stage":"receiving stock addition","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"0.1 M Sodium sulfite solution\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"conc_value\": 0.1,\n          \"conc_unit\": \"M\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001452\",\n          \"gmo_id\": \"GMO_001452\",\n          \"label\": \"Sodium sulfite solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing agent\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML table row 14 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 0.1 M Sodium sulfite solution                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Sodium sulfite\",\n                        \"compound_id\": 1897,\n                        \"attribute\": \"0.1 M\",\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[2].concentration","decision":"correct","rationale":"The source supplies a stock addition in ml, not a mass concentration. Preserve this exact batch addition and its separately stated stock strength; do not convert bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and 100 mg/L strengths are explicit and distinct from addition volumes."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[2].concentration","decision":"correct","rationale":"The source supplies a stock addition in ml, not a mass concentration. Preserve this exact batch addition and its separately stated stock strength; do not convert bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and 100 mg/L strengths are explicit and distinct from addition volumes."}]},{"quantity_id":"q19","label":"1 M Sodium pyruvate solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[3].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source supplies a stock addition in ml, not a mass concentration. Preserve this exact batch addition and its separately stated stock strength; do not convert bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and 100 mg/L strengths are explicit and distinct from addition volumes.","source_stage":"receiving stock addition","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"1 M Sodium pyruvate solution\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001475\",\n          \"gmo_id\": \"GMO_001475\",\n          \"label\": \"Sodium pyruvate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML table row 15 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 1 M Sodium pyruvate solution                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[15]","quote":"{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Sodium pyruvate\",\n                        \"compound_id\": 438,\n                        \"attribute\": \"1 M\",\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[3].concentration","decision":"correct","rationale":"The source supplies a stock addition in ml, not a mass concentration. Preserve this exact batch addition and its separately stated stock strength; do not convert bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and 100 mg/L strengths are explicit and distinct from addition volumes."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[3].concentration","decision":"correct","rationale":"The source supplies a stock addition in ml, not a mass concentration. Preserve this exact batch addition and its separately stated stock strength; do not convert bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and 100 mg/L strengths are explicit and distinct from addition volumes."}]},{"quantity_id":"q20","label":"5% Na2S・9H2O solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[4].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[4].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source supplies a stock addition in ml, not a mass concentration. Preserve this exact batch addition and its separately stated stock strength; do not convert bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and 100 mg/L strengths are explicit and distinct from addition volumes.","source_stage":"receiving stock addition","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\": \"5% Na2S・9H2O solution\",\n          \"volume\": 8,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001494\",\n          \"gmo_id\": \"GMO_001494\",\n          \"label\": \"Sodium sulfide nonahydrate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing agent\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML table row 17 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O solution                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;8.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[17]","quote":"{\n                        \"recipe_order\": 18,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"attribute\": \"5%\",\n                        \"amount\": 8,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[4].concentration","decision":"correct","rationale":"The source supplies a stock addition in ml, not a mass concentration. Preserve this exact batch addition and its separately stated stock strength; do not convert bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and 100 mg/L strengths are explicit and distinct from addition volumes."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[4].concentration","decision":"correct","rationale":"The source supplies a stock addition in ml, not a mass concentration. Preserve this exact batch addition and its separately stated stock strength; do not convert bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and 100 mg/L strengths are explicit and distinct from addition volumes."}]},{"quantity_id":"q21","label":"Sodium dithionite solution (100 mg/L)*","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[5].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[5].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source supplies a stock addition in ml, not a mass concentration. Preserve this exact batch addition and its separately stated stock strength; do not convert bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and 100 mg/L strengths are explicit and distinct from addition volumes.","source_stage":"receiving stock addition","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\": \"Sodium dithionite solution (100 mg/L)*\",\n          \"volume\": 2,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001721\",\n          \"gmo_id\": \"GMO_001721\",\n          \"label\": \"Sodium dithionite solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Sodium dithionite solution (100 mg/L)*                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[16]","quote":"{\n                        \"recipe_order\": 17,\n                        \"compound\": \"Sodium dithionite\",\n                        \"compound_id\": 1676,\n                        \"attribute\": \"*, 100 mg/L\",\n                        \"amount\": 2,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[5].concentration","decision":"correct","rationale":"The source supplies a stock addition in ml, not a mass concentration. Preserve this exact batch addition and its separately stated stock strength; do not convert bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and 100 mg/L strengths are explicit and distinct from addition volumes."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[5].concentration","decision":"correct","rationale":"The source supplies a stock addition in ml, not a mass concentration. Preserve this exact batch addition and its separately stated stock strength; do not convert bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and 100 mg/L strengths are explicit and distinct from addition volumes."}]},{"quantity_id":"q22","label":"CaCl2・2H2O in JCM483 microelements","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact component mass belongs to the referenced microelement stock, not the parent final medium or the selected receiving medium. Its source uses 1 L water input without explicit final makeup. Preserve that stock batch mass and the selected 1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated parent formulation.","source_stage":"scoped microelement stock","sources":[{"evidence_id":"togo484","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo484.bin","raw_sha256":"e62611edbbc4fc289ee902fff57465f53c1927debe72108c19794f91a51e7fd1","text_sha256":"c3815e3fdd2177b3d03bc60b4e8abe1bb110de33e4f5d7d5fa74f693d276c8e6","accessed_at":"2026-10-28T18:07:26.264203Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm483","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm483.bin","raw_sha256":"4fbd01bff716d5389eca921b496534346d6281dd72c8cc23f7fdef3d806e5fa1","text_sha256":"5e110f4f2ca7a8043e25abb292824049c8d50ba0344ad43d9a557c243de48ca8","accessed_at":"2026-10-28T18:07:26.041708Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The exact component mass belongs to the referenced microelement stock, not the parent final medium or the selected receiving medium. Its source uses 1 L water input without explicit final makeup. Preserve that stock batch mass and the selected 1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated parent formulation."}]},{"quantity_id":"q23","label":"Na2MoO4・2H2O in JCM483 microelements","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact component mass belongs to the referenced microelement stock, not the parent final medium or the selected receiving medium. Its source uses 1 L water input without explicit final makeup. Preserve that stock batch mass and the selected 1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated parent formulation.","source_stage":"scoped microelement stock","sources":[{"evidence_id":"togo484","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo484.bin","raw_sha256":"e62611edbbc4fc289ee902fff57465f53c1927debe72108c19794f91a51e7fd1","text_sha256":"c3815e3fdd2177b3d03bc60b4e8abe1bb110de33e4f5d7d5fa74f693d276c8e6","accessed_at":"2026-10-28T18:07:26.264203Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm483","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm483.bin","raw_sha256":"4fbd01bff716d5389eca921b496534346d6281dd72c8cc23f7fdef3d806e5fa1","text_sha256":"5e110f4f2ca7a8043e25abb292824049c8d50ba0344ad43d9a557c243de48ca8","accessed_at":"2026-10-28T18:07:26.041708Z","locator":"HTML table row 17 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"The exact component mass belongs to the referenced microelement stock, not the parent final medium or the selected receiving medium. Its source uses 1 L water input without explicit final makeup. Preserve that stock batch mass and the selected 1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated parent formulation."}]},{"quantity_id":"q24","label":"H3BO3 in JCM483 microelements","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact component mass belongs to the referenced microelement stock, not the parent final medium or the selected receiving medium. Its source uses 1 L water input without explicit final makeup. Preserve that stock batch mass and the selected 1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated parent formulation.","source_stage":"scoped microelement stock","sources":[{"evidence_id":"togo484","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo484.bin","raw_sha256":"e62611edbbc4fc289ee902fff57465f53c1927debe72108c19794f91a51e7fd1","text_sha256":"c3815e3fdd2177b3d03bc60b4e8abe1bb110de33e4f5d7d5fa74f693d276c8e6","accessed_at":"2026-10-28T18:07:26.264203Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm483","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm483.bin","raw_sha256":"4fbd01bff716d5389eca921b496534346d6281dd72c8cc23f7fdef3d806e5fa1","text_sha256":"5e110f4f2ca7a8043e25abb292824049c8d50ba0344ad43d9a557c243de48ca8","accessed_at":"2026-10-28T18:07:26.041708Z","locator":"HTML table row 14 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[12].concentration","decision":"unsupported","rationale":"The exact component mass belongs to the referenced microelement stock, not the parent final medium or the selected receiving medium. Its source uses 1 L water input without explicit final makeup. Preserve that stock batch mass and the selected 1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated parent formulation."}]},{"quantity_id":"q25","label":"CoCl2・6H2O in JCM483 microelements","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact component mass belongs to the referenced microelement stock, not the parent final medium or the selected receiving medium. Its source uses 1 L water input without explicit final makeup. Preserve that stock batch mass and the selected 1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated parent formulation.","source_stage":"scoped microelement stock","sources":[{"evidence_id":"togo484","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo484.bin","raw_sha256":"e62611edbbc4fc289ee902fff57465f53c1927debe72108c19794f91a51e7fd1","text_sha256":"c3815e3fdd2177b3d03bc60b4e8abe1bb110de33e4f5d7d5fa74f693d276c8e6","accessed_at":"2026-10-28T18:07:26.264203Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm483","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm483.bin","raw_sha256":"4fbd01bff716d5389eca921b496534346d6281dd72c8cc23f7fdef3d806e5fa1","text_sha256":"5e110f4f2ca7a8043e25abb292824049c8d50ba0344ad43d9a557c243de48ca8","accessed_at":"2026-10-28T18:07:26.041708Z","locator":"HTML table row 18 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.2&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[13].concentration","decision":"unsupported","rationale":"The exact component mass belongs to the referenced microelement stock, not the parent final medium or the selected receiving medium. Its source uses 1 L water input without explicit final makeup. Preserve that stock batch mass and the selected 1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated parent formulation."}]},{"quantity_id":"q26","label":"ZnSO4・7H2O in JCM483 microelements","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact component mass belongs to the referenced microelement stock, not the parent final medium or the selected receiving medium. Its source uses 1 L water input without explicit final makeup. Preserve that stock batch mass and the selected 1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated parent formulation.","source_stage":"scoped microelement stock","sources":[{"evidence_id":"togo484","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo484.bin","raw_sha256":"e62611edbbc4fc289ee902fff57465f53c1927debe72108c19794f91a51e7fd1","text_sha256":"c3815e3fdd2177b3d03bc60b4e8abe1bb110de33e4f5d7d5fa74f693d276c8e6","accessed_at":"2026-10-28T18:07:26.264203Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 0.05,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001023\",\n          \"gmo_id\": \"GMO_001023\",\n          \"label\": \"Zinc sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm483","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm483.bin","raw_sha256":"4fbd01bff716d5389eca921b496534346d6281dd72c8cc23f7fdef3d806e5fa1","text_sha256":"5e110f4f2ca7a8043e25abb292824049c8d50ba0344ad43d9a557c243de48ca8","accessed_at":"2026-10-28T18:07:26.041708Z","locator":"HTML table row 13 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.05&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[14].concentration","decision":"unsupported","rationale":"The exact component mass belongs to the referenced microelement stock, not the parent final medium or the selected receiving medium. Its source uses 1 L water input without explicit final makeup. Preserve that stock batch mass and the selected 1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated parent formulation."}]},{"quantity_id":"q27","label":"AlK(SO4)2・12H2O in JCM483 microelements","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact component mass belongs to the referenced microelement stock, not the parent final medium or the selected receiving medium. Its source uses 1 L water input without explicit final makeup. Preserve that stock batch mass and the selected 1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated parent formulation.","source_stage":"scoped microelement stock","sources":[{"evidence_id":"togo484","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo484.bin","raw_sha256":"e62611edbbc4fc289ee902fff57465f53c1927debe72108c19794f91a51e7fd1","text_sha256":"c3815e3fdd2177b3d03bc60b4e8abe1bb110de33e4f5d7d5fa74f693d276c8e6","accessed_at":"2026-10-28T18:07:26.264203Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\": \"AlK(SO4)2・12H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001051\",\n          \"gmo_id\": \"GMO_001051\",\n          \"label\": \"Aluminum potassium sulfate dodecahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm483","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm483.bin","raw_sha256":"4fbd01bff716d5389eca921b496534346d6281dd72c8cc23f7fdef3d806e5fa1","text_sha256":"5e110f4f2ca7a8043e25abb292824049c8d50ba0344ad43d9a557c243de48ca8","accessed_at":"2026-10-28T18:07:26.041708Z","locator":"HTML table row 19 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; AlK(SO&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;&amp;#183;12H&lt;sub&gt;2&lt;/sub&gt;O                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[15].concentration","decision":"unsupported","rationale":"The exact component mass belongs to the referenced microelement stock, not the parent final medium or the selected receiving medium. Its source uses 1 L water input without explicit final makeup. Preserve that stock batch mass and the selected 1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated parent formulation."}]},{"quantity_id":"q28","label":"Nitrilotriacetic acid in JCM483 microelements","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"4.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact component mass belongs to the referenced microelement stock, not the parent final medium or the selected receiving medium. Its source uses 1 L water input without explicit final makeup. Preserve that stock batch mass and the selected 1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated parent formulation.","source_stage":"scoped microelement stock","sources":[{"evidence_id":"togo484","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo484.bin","raw_sha256":"e62611edbbc4fc289ee902fff57465f53c1927debe72108c19794f91a51e7fd1","text_sha256":"c3815e3fdd2177b3d03bc60b4e8abe1bb110de33e4f5d7d5fa74f693d276c8e6","accessed_at":"2026-10-28T18:07:26.264203Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\": \"Nitrilotriacetic acid\",\n          \"volume\": 4.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001053\",\n          \"gmo_id\": \"GMO_001053\",\n          \"label\": \"Nitrilotriacetic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm483","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm483.bin","raw_sha256":"4fbd01bff716d5389eca921b496534346d6281dd72c8cc23f7fdef3d806e5fa1","text_sha256":"5e110f4f2ca7a8043e25abb292824049c8d50ba0344ad43d9a557c243de48ca8","accessed_at":"2026-10-28T18:07:26.041708Z","locator":"HTML table row 15 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Nitrilotriacetic acid                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;4.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[16].concentration","decision":"unsupported","rationale":"The exact component mass belongs to the referenced microelement stock, not the parent final medium or the selected receiving medium. Its source uses 1 L water input without explicit final makeup. Preserve that stock batch mass and the selected 1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated parent formulation."}]},{"quantity_id":"q29","label":"MnSO4・xH2O in JCM483 microelements","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact component mass belongs to the referenced microelement stock, not the parent final medium or the selected receiving medium. Its source uses 1 L water input without explicit final makeup. Preserve that stock batch mass and the selected 1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated parent formulation.","source_stage":"scoped microelement stock","sources":[{"evidence_id":"togo484","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo484.bin","raw_sha256":"e62611edbbc4fc289ee902fff57465f53c1927debe72108c19794f91a51e7fd1","text_sha256":"c3815e3fdd2177b3d03bc60b4e8abe1bb110de33e4f5d7d5fa74f693d276c8e6","accessed_at":"2026-10-28T18:07:26.264203Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\": \"MnSO4・xH2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001065\",\n          \"gmo_id\": \"GMO_001065\",\n          \"label\": \"Manganese sulfate n-hydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm483","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm483.bin","raw_sha256":"4fbd01bff716d5389eca921b496534346d6281dd72c8cc23f7fdef3d806e5fa1","text_sha256":"5e110f4f2ca7a8043e25abb292824049c8d50ba0344ad43d9a557c243de48ca8","accessed_at":"2026-10-28T18:07:26.041708Z","locator":"HTML table row 12 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;&lt;I&gt;x&lt;/I&gt;H&lt;sub&gt;2&lt;/sub&gt;O                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[17].concentration","decision":"unsupported","rationale":"The exact component mass belongs to the referenced microelement stock, not the parent final medium or the selected receiving medium. Its source uses 1 L water input without explicit final makeup. Preserve that stock batch mass and the selected 1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated parent formulation."}]},{"quantity_id":"q30","label":"Microelement stock solvent","local_fields":[],"decision":"evidence_only","rationale":"Preserve the stock-specific 1 L water input; the collapsed parent water row mixes other stages and is intentionally outside dependency scope. Input water is not explicit final makeup.","source_stage":"source-only microelement stock","sources":[{"evidence_id":"togo484","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo484.bin","raw_sha256":"e62611edbbc4fc289ee902fff57465f53c1927debe72108c19794f91a51e7fd1","text_sha256":"c3815e3fdd2177b3d03bc60b4e8abe1bb110de33e4f5d7d5fa74f693d276c8e6","accessed_at":"2026-10-28T18:07:26.264203Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm483","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm483.bin","raw_sha256":"4fbd01bff716d5389eca921b496534346d6281dd72c8cc23f7fdef3d806e5fa1","text_sha256":"5e110f4f2ca7a8043e25abb292824049c8d50ba0344ad43d9a557c243de48ca8","accessed_at":"2026-10-28T18:07:26.041708Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q31","label":"Main pH, atmosphere and staged preparation","local_fields":[],"decision":"evidence_only","rationale":"Retain pH 7.0 with KOH, N2/CO2 4:1 v/v, butyl-rubber closure, autoclaving followed by cooling and anaerobic stock additions per 925 ml. The starred bicarbonate and dithionite stocks are filter-sterilized. This source sequence is absent locally; no quantitative gas addition is inferred.","source_stage":"source-only main preparation","sources":[{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"jcm796.txt lines 65-69","quote":"Mix components thoroughly, adjust pH to 7.0 with KOH, distribute the medium into culture vessels under a N\n2\n-CO\n2\n(4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave.  After cooling, add per 925 ml the following solutions from anaerobic stocks (autoclaved or *filter-sterilized):","quote_basis":"derivative text"},{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly, adjust pH to 7.0 with KOH, distribute the medium into culture vessels under a N2--CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per 925 ml the following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\": 14,\n                        \"step\": \"Mix components thoroughly, adjust pH to 7.0 with KOH, distribute the medium into culture vessels under a N2-CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per 925 ml the following solutions from anaerobic stocks (autoclaved or *filter-sterilized): \"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q32","label":"JCM page-wide autoclave default","local_fields":[],"decision":"evidence_only","rationale":"The page explicitly supplies 121°C for 15 min unless otherwise stated. Apply only to the inherited autoclave steps, not the separately starred filter-sterilized stocks; retain this as a page-default claim with explicit scope.","source_stage":"source-only default preparation","sources":[{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"jcm796.txt lines 4-4","quote":"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.","quote_basis":"derivative text"}],"layer_assessments":[]}],"document_scopes":{"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml":null,"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml":["ingredients[10]","ingredients[11]","ingredients[12]","ingredients[13]","ingredients[14]","ingredients[15]","ingredients[16]","ingredients[17]"]},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:010244.

Every selected and explicitly scoped dependency slot is checked against fresh OLS and exact packaged MIM rows. Primary cobalt hexahydrate conflicts with anhydrous35696; the manganese x-hydrate remains unresolved. Selected neutral resazurin8806, magnesium hexahydrate86345, calcium dihydrate86158 and L-cysteine hydrochloride monohydrate91248 match the source forms. Yeast FOODON03315426 is a whole-mixture candidate; branded peptone equivalence is not invented. Missing secondary links are recorded separately from canonical-label and supplied-form validity.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:010244.

All current target/owner/dependency events and four complete historical reports were read. The neighboring DSM merged record is comparison context only. Historical reports have zero external source checks and do not supply authenticated source objects or selected parent repair rows here. No local attached claims exist. Current TOGO stock separation, unit mapping and comment extraction are credited, while their remaining denominator and mixed-step limitations are explicit; current behavior is not proof of historical execution.

## Findings

### f1: Correct batch units and qualify concentration bases

major / open / confirmed; issue key: culturemech-010244-batch-units-and-denominators.

Water is 925 ml and resazurin is 1 mg in the primary; all six stock additions are ml. Their stored G_PER_L representations are wrong. The other batch masses are correctly transcribed but lack explicit final-volume support for their current per-litre basis. Current APIJ796 independently declares normalization on 1001 ml, rather than establishing measured final volume. Preserve original source amounts and distinguish any provider basis.

### f2: Resolve the referenced microelement stock within its exact scope

major / open / confirmed; issue key: culturemech-010244-microelement-stock-scope.

The empty M484 reference points to JCM483 microelements. Only its eight microelement ingredients are relevant; they are flattened into the parent main list. Represent the scoped stock and selected 1 ml receiving addition without transferring the parent 10 ml dose, main formulation, vitamins or parent pH. Keep the five separately named late-stock strengths and receiving volumes; a supplied molarity or bare percentage is not a complete mass recipe.

### f3: Add the exact pH and anaerobic preparation sequence

major / open / confirmed; issue key: culturemech-010244-missing-staged-preparation.

Both selected layers omit pH 7.0 and all preparation steps. Preserve the supported KOH and gas VARIABLE placeholders while adding their actual pH/ratio context, autoclave/cooling order, closure and separately sterilized stock additions. Scope the page-wide 121°C/15 min default to autoclaving and exclude starred filtration.

### f4: Reconcile scoped cobalt and unresolved manganese hydrate

major / open / confirmed; issue key: culturemech-010244-microelement-hydrate-grounding.

The scoped M484 cobalt hexahydrate is linked to anhydrous CHEBI:35696. Resolve the supplied hexahydrate without changing its source mass. MnSO4·xH2O is not fully specified by the anhydrous CHEBI:86360 assertion; preserve the unknown hydrate number and do not choose a convenient fixed hydrate. Selected calcium/magnesium hydrates, L-cysteine hydrochloride monohydrate and neutral resazurin are supported. Their identities do not validate the current quantity units.

### f5: Replace placeholder names and attach source-scoped claims

minor / open / confirmed; issue key: culturemech-010244-stock-names-and-claim-linkage.

All six solutions retain the literal name Unknown solution despite distinct preferred terms, and no attached claims exist. Use exact source-specific stock names; attach ingredient evidence and schema-root evidence for receiving amounts/preparation. Yeast extract has a verified whole-mixture FOODON candidate; the branded Trypticase mixture must not be replaced with an assumed pure compound or unsupported product equivalent.

## Recommended Actions And Acceptance Checks

### a1

Water is 925 ml and resazurin is 1 mg in the primary; all six stock additions are ml. Their stored G_PER_L representations are wrong. The other batch masses are correctly transcribed but lack explicit final-volume support for their current per-litre basis. Current APIJ796 independently declares normalization on 1001 ml, rather than establishing measured final volume. Preserve original source amounts and distinguish any provider basis.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

The empty M484 reference points to JCM483 microelements. Only its eight microelement ingredients are relevant; they are flattened into the parent main list. Represent the scoped stock and selected 1 ml receiving addition without transferring the parent 10 ml dose, main formulation, vitamins or parent pH. Keep the five separately named late-stock strengths and receiving volumes; a supplied molarity or bare percentage is not a complete mass recipe.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

Both selected layers omit pH 7.0 and all preparation steps. Preserve the supported KOH and gas VARIABLE placeholders while adding their actual pH/ratio context, autoclave/cooling order, closure and separately sterilized stock additions. Scope the page-wide 121°C/15 min default to autoclaving and exclude starred filtration.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

The scoped M484 cobalt hexahydrate is linked to anhydrous CHEBI:35696. Resolve the supplied hexahydrate without changing its source mass. MnSO4·xH2O is not fully specified by the anhydrous CHEBI:86360 assertion; preserve the unknown hydrate number and do not choose a convenient fixed hydrate. Selected calcium/magnesium hydrates, L-cysteine hydrochloride monohydrate and neutral resazurin are supported. Their identities do not validate the current quantity units.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

All six solutions retain the literal name Unknown solution despite distinct preferred terms, and no attached claims exist. Use exact source-specific stock names; attach ingredient evidence and schema-root evidence for receiving amounts/preparation. Yeast extract has a verified whole-mixture FOODON candidate; the branded Trypticase mixture must not be replaced with an assumed pure compound or unsupported product equivalent.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| jcm796 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796; REVIEW_WORK/batch074/source01-03-supplement/jcm796.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| jcm483 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483; REVIEW_WORK/batch074/source01-03-supplement/jcm483.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| togo830 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830; REVIEW_WORK/batch074/source01-03-supplement/togo830.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| togo484 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484; REVIEW_WORK/batch074/source01-03-supplement/togo484.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| apiJ796 | https://mediadive.dsmz.de/rest/medium/J796; REVIEW_WORK/batch074/source01-03-supplement/apiJ796.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| foodon03315426 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON:03315426; REVIEW_WORK/batch074/source01-03-supplement/foodon03315426.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| target | data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-17 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFITOCELLA_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-18 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfitocella_medium__430186b9.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-19 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-20 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch074/record02/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch074/record02/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch074/record02/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| writer-togo | src/culturemech/import/togo_importer.py; _extract_primary_components; _solution_from_item; _local_batch_volume_ml; _parse_unit; _extract_ph; _extract_preparation_steps | context_only | Current _extract_primary_components separates named local stocks; _solution_from_item retains a local stock without composition if its basis is insufficient. _parse_unit now maps mg to MG_PER_L and ml to ML_PER_L, but bare g still becomes G_PER_L and bare percent becomes PERCENT_W_V without independently proving final volume or percent basis. _extract_ph reads root ph, while these API payloads provide meta.ph. _extract_preparation_steps retains comments but its classifier checks autoclave before filtration and does not split mixed-process paragraphs. These are current behaviors, not proof of historical execution. |
| writer-cleanup | scripts/cleanup_media_quality.py; MediaQualityFixer._merge_ingredient_group | context_only | Current _merge_ingredient_group keeps identical duplicate amounts and flags disagreements; it no longer sums duplicate quantities. It cannot establish compatible stock/main bases or repair a historical flattened sum. |
| microelement-owner | data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml; ingredients[10:18] | context_only | Only ingredients[10:18] are the referenced JCM483 microelement composition. The parent main formulation, vitamins, pH and receiving doses are excluded. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377; REVIEW_WORK/batch074/source01-03-supplement/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch074/source01-03-supplement/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158; REVIEW_WORK/batch074/source01-03-supplement/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; REVIEW_WORK/batch074/source01-03-supplement/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch074/source01-03-supplement/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527; REVIEW_WORK/batch074/source01-03-supplement/chebi131527.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; REVIEW_WORK/batch074/source01-03-supplement/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; REVIEW_WORK/batch074/source01-03-supplement/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; REVIEW_WORK/batch074/source01-03-supplement/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91248; REVIEW_WORK/batch074/source01-03-supplement/chebi91248.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32035 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32035; REVIEW_WORK/batch074/source01-03-supplement/chebi32035.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16526; REVIEW_WORK/batch074/source01-03-supplement/chebi16526.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17997; REVIEW_WORK/batch074/source01-03-supplement/chebi17997.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch074/source01-03-supplement/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch074/source01-03-supplement/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:35696; REVIEW_WORK/batch074/source01-03-supplement/chebi35696.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312; REVIEW_WORK/batch074/source01-03-supplement/chebi32312.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86465; REVIEW_WORK/batch074/source01-03-supplement/chebi86465.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:44557; REVIEW_WORK/batch074/source01-03-supplement/chebi44557.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86360 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86360; REVIEW_WORK/batch074/source01-03-supplement/chebi86360.json; exact original raw/text/hash/time metadata | context_only | Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| quantities | REVIEW_WORK/batch074/record02/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch074/record02/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch074/record02/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch074/record02/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch074/record02/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch074/record02/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch074/record02/existing-claim-authentication.json; Complete sidecar | context_only | No attached claims to authenticate; historical source objects are separately assessed in historical-source-joins.json. |
| historical-source-joins | REVIEW_WORK/batch074/record02/historical-source-joins.json; Every literal/decoded historical source-object row and exact current-source match | context_only | Historical quoted source content and raw-digest equality where actually matched; independent of attached local claims and original access-event recovery. |
| check-schema | REVIEW_WORK/batch074/record02/validate-schema.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch074/record02/validate-strict.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch074/record02/validate-terms.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch074/record02/validate-references.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Only M484 ingredients[10:18] are scientifically assessed as the referenced microelement composition; all other parent quantities and vitamins are excluded.
- The JCM796 primary specifies additions per 925 ml, with a separate 1 ml trace addition. APIJ796 uses 1001 ml computational normalization; neither establishes measured final main volume.
- The JCM483 stock specifies 1 L water input, not explicit final makeup. MnSO4 hydration number and bare 8%/5% bases remain unresolved.
- Unused provider mmol_l and manufacturer-specific peptone equivalence are not certified.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T181709Z-culturemech-010244-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: Desulfitocella Medium'
started_at: '2026-10-28T18:06:48.064965Z'
finished_at: '2026-10-28T18:17:09.697988Z'
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
summary: JCM796 identity and source batch amounts are supported, but water, resazurin
  and six stock additions have incorrect units and other local per-litre bases remain
  unproven. The exact JCM483 microelements, supplied forms and staged preparation
  need scoped curation. Truthful unquantified placeholders and correct retained identities
  are credited; all four original diagnostics passed.
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
  - path: data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml
    sha256: fba98da9a1b6e720d9b3435a44931144cc542c6b1f9a372c7762d834c50864b8
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml
    sha256: c2295a61c7802b3af7be9fd73d34152b04527cdbbdcae25a9e96b2f8958f8d22
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml
    sha256: 7f55d8a36c729c40d6aabf20eae70dcda0cf1f5bbb471d6d42d818b85fa861df
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFITOCELLA_MEDIUM.md
    sha256: 648ea0439696baa3e54daa71d11ec07f4f2f9677409b7e2861274480d791e8a8
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfitocella_medium__430186b9.md
    sha256: b23779a1d219753c155d3eda47be734b8a08324cf1e7471b764e2a5d4d4822a8
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.md
    sha256: 8b51dde1f26fa31a00822462906b02737378e2fa78c66359e9bea0d001649b9d
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.md
    sha256: 2fd8ec5051dcc5f7ed68abb532b1a483869a511f6cf4dc939813178a9aa88f3d
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
  selection: Authoritative batch074 index 02
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010244
targets:
- target_id: CultureMech:010244
  path: data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml
  label: desulfitocella_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml
    role: maintained normalized contributor
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:010244
  command: just validate-schema data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml
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
  - CultureMech:010244
  command: just validate-strict data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml
    --out REVIEW_WORK/batch074/record02/strict.tsv --workers 1 --quiet
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
  - CultureMech:010244
  command: just validate-terms data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml
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
  - CultureMech:010244
  command: just validate-references data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: jcm796
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796
  accessed_at: '2026-10-28T18:07:25.969580Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/jcm796.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd
- evidence_id: jcm483
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483
  accessed_at: '2026-10-28T18:07:26.041708Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/jcm483.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4fbd01bff716d5389eca921b496534346d6281dd72c8cc23f7fdef3d806e5fa1
- evidence_id: togo830
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830
  accessed_at: '2026-10-28T18:07:26.236052Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/togo830.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b
- evidence_id: togo484
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484
  accessed_at: '2026-10-28T18:07:26.264203Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/togo484.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e62611edbbc4fc289ee902fff57465f53c1927debe72108c19794f91a51e7fd1
- evidence_id: apiJ796
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J796
  accessed_at: '2026-10-28T18:07:26.498732Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/apiJ796.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae
- evidence_id: foodon03315426
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON:03315426
  accessed_at: '2026-10-28T18:07:36.392497Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/foodon03315426.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 7812dff5a532367bf78b3a0fa93571cc657e52ec5f4b86f296a4e245aa75ba9b
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T18:17:09.600033Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: fba98da9a1b6e720d9b3435a44931144cc542c6b1f9a372c7762d834c50864b8
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T18:17:09.600184Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 7f55d8a36c729c40d6aabf20eae70dcda0cf1f5bbb471d6d42d818b85fa861df
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T18:17:09.600214Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T18:17:09.600528Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T18:17:09.600557Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T18:17:09.600579Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-17
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFITOCELLA_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T18:17:09.600605Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 648ea0439696baa3e54daa71d11ec07f4f2f9677409b7e2861274480d791e8a8
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfitocella_medium__430186b9.md
  locator: Complete report
  accessed_at: '2026-10-28T18:17:09.600634Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: b23779a1d219753c155d3eda47be734b8a08324cf1e7471b764e2a5d4d4822a8
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T18:17:09.600657Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 8b51dde1f26fa31a00822462906b02737378e2fa78c66359e9bea0d001649b9d
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T18:17:09.600681Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 2fd8ec5051dcc5f7ed68abb532b1a483869a511f6cf4dc939813178a9aa88f3d
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch074/record02/historical-reading.json
  accessed_at: '2026-10-28T18:17:09.600707Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: e7952cb848f1e64a1725d9050d81d9240b354653e185f58d2aed8cf269304041
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch074/record02/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T18:17:09.600942Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch074/record02/complete-document-reader.json
  accessed_at: '2026-10-28T18:17:09.601085Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 8c13bd52933968f18ad0aa554d76e8b80f25d6b5d224583a2be4ad1187919405
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T18:17:09.601297Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_primary_components; _solution_from_item; _local_batch_volume_ml;
    _parse_unit; _extract_ph; _extract_preparation_steps
  accessed_at: '2026-10-28T18:17:09.601324Z'
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
  accessed_at: '2026-10-28T18:17:09.601360Z'
  support: context_only
  summary: Current _merge_ingredient_group keeps identical duplicate amounts and flags
    disagreements; it no longer sums duplicate quantities. It cannot establish compatible
    stock/main bases or repair a historical flattened sum.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: microelement-owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml
  locator: ingredients[10:18]
  accessed_at: '2026-10-28T18:17:09.607360Z'
  support: context_only
  summary: Only ingredients[10:18] are the referenced JCM483 microelement composition.
    The parent main formulation, vitamins, pH and receiving doses are excluded.
  snapshot_sha256: c2295a61c7802b3af7be9fd73d34152b04527cdbbdcae25a9e96b2f8958f8d22
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377
  accessed_at: '2026-10-28T18:07:28.023786Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi15377.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: a5ab66402b598c137daa8e5c8ba95811f1619db3e0f8b4f9bd0214161bafa0fe
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  accessed_at: '2026-10-28T18:07:30.080063Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi26710.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158
  accessed_at: '2026-10-28T18:07:34.672414Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi86158.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: eacf58308fa876cb17661b82d08a64d9be24814fde8014ac82da7696b3684841
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  accessed_at: '2026-10-28T18:07:34.074001Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi63036.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  accessed_at: '2026-10-28T18:07:30.964074Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi31206.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527
  accessed_at: '2026-10-28T18:07:27.588305Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi131527.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 0a5297c84ea9dd82508960482211f6b3c993fd8e2b83fe755dd2b23316cc4068
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806
  accessed_at: '2026-10-28T18:07:35.822503Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi8806.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f2530ec9c15f59a3d132a466c9c3a899497bab0f85b996d3e27bef8612f89982
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345
  accessed_at: '2026-10-28T18:07:35.228269Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi86345.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 94b600ced6e98743e2d1b02c73e1756f8f81b639407a8fdd080c96d8fa563c70
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  accessed_at: '2026-10-28T18:07:32.177572Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi32588.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi91248
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91248
  accessed_at: '2026-10-28T18:07:35.881884Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi91248.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d0959ac455ece32a6e94c13fd8e592403109201b6c61144dccfe0d58f1916380
- evidence_id: chebi32035
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32035
  accessed_at: '2026-10-28T18:07:31.315631Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi32035.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d0537d7c65cf63693a87f126d0f0f13501f6519f98fe7ca64fb07d469079571c
- evidence_id: chebi16526
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16526
  accessed_at: '2026-10-28T18:07:28.668244Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi16526.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1fc9ed85cc20ea796dc5884bab2961c0cb13288fec88089767d5ca0349e6ab66
- evidence_id: chebi17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17997
  accessed_at: '2026-10-28T18:07:29.766752Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi17997.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: c4f240d59927c0f5c6c8d29c14830d0f278cfeabc4ed924be5c2b6bbe1039c05
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  accessed_at: '2026-10-28T18:07:34.368132Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi75213.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  accessed_at: '2026-10-28T18:07:32.513363Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi33118.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi35696
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:35696
  accessed_at: '2026-10-28T18:07:32.784097Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi35696.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 22f49067d1405baa8e2bbd7c4405035d8663c69aa045b7bbacf363bb30729244
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312
  accessed_at: '2026-10-28T18:07:31.929544Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi32312.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 19bbc18dfc582e76457c6f08d51bb777a2f7a2cbd2f810cb3b58bdb0004b4d60
- evidence_id: chebi86465
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86465
  accessed_at: '2026-10-28T18:07:35.780437Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi86465.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 76cce7fa8230c57138e3569858ecf6a79119be85281bd5d2864ada3223785dc1
- evidence_id: chebi44557
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:44557
  accessed_at: '2026-10-28T18:07:32.792087Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi44557.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 25e8fb689e4dfc294e2823ca36290cdce6d21ad174238e0e958ebe09d4c1262b
- evidence_id: chebi86360
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86360
  accessed_at: '2026-10-28T18:07:35.271668Z'
  locator: REVIEW_WORK/batch074/source01-03-supplement/chebi86360.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch074 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 857672fb1b6a33f508924cdc2e4dfcbdf365a0e54d96fc8379d6ee61aa16cb31
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch074/record02/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:17:09.696035Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: be05ee6983f4aa2a9773d960c28af853ebb78347fabeec02a8f5fc2616209a44
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch074/record02/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:17:09.696128Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 017561252c08cd111bfe2acff4f62cd04eb42dbc24cdb3df029fabf198c3b05e
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch074/record02/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:17:09.696221Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 6b461fc370e761aa6c1166238588b77f4e95fe8646560f8d19f070ef77677ebb
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch074/record02/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:17:09.696290Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: de48599d1d007ffdf6e1c97dff76f04c187b662f4354a82f09576f9dd0e6c987
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch074/record02/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:17:09.696378Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 55c49e87f17c4704f14fd75ac7c6a80c7f02d9fe0173b1526e49f4ab9c962bce
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch074/record02/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:17:09.696424Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 0113226f7d7064dfa23d9da3aff272e22c5390ae46c2ec2eed62e020eb647934
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch074/record02/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:17:09.696454Z'
  support: context_only
  summary: No attached claims to authenticate; historical source objects are separately
    assessed in historical-source-joins.json.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: historical-source-joins
  kind: record_content
  reference: REVIEW_WORK/batch074/record02/historical-source-joins.json
  locator: Every literal/decoded historical source-object row and exact current-source
    match
  accessed_at: '2026-10-28T18:17:09.696475Z'
  support: context_only
  summary: Historical quoted source content and raw-digest equality where actually
    matched; independent of attached local claims and original access-event recovery.
  snapshot_sha256: 61bced656119bda5e5707658364e1bfe5a734d7e745cc42bf2e8c9996bd657a2
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch074/record02/validate-schema.json
  accessed_at: '2026-10-28T18:06:49.083304Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: ee451ca5b36befe0e6538cd7f5b5001dedc6894eb96852c89c5c743b85fabb90
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch074/record02/validate-strict.json
  accessed_at: '2026-10-28T18:06:50.014612Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: a3e7a72c94942f4f3678269b310d8f03b0e1208572f53bcc299e705e10bea86c
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch074/record02/validate-terms.json
  accessed_at: '2026-10-28T18:06:51.027644Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 39b8852e8ac3beab2043d4eb32892b761a3bec1eee600f366093969df8578b3c
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch074/record02/validate-references.json
  accessed_at: '2026-10-28T18:06:51.736711Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: c4b47e41c0203fa68ad43b2bd114e46cdf48a4f92c67e08e8484cd10e80e9d80
assessments:
- assessment_id: identity
  area: identity
  topic: JCM796 and scoped JCM483 identity
  outcome: supported
  summary: The exact JCM796 title and complete tables agree with TOGO M830. Its trace
    reference resolves to JCM483 / TOGO M484 microelements only; the parent recipe
    and receiving dose are excluded.
  target_ids:
  - CultureMech:010244
  evidence_ids:
  - jcm796
  - jcm483
  - togo830
  - togo484
- assessment_id: classification
  area: scope
  topic: Complex liquid medium
  outcome: supported
  summary: Yeast extract and branded Trypticase support complex/undefined classification;
    no gelling agent is supplied. No organism-growth claim is inferred.
  target_ids:
  - CultureMech:010244
  evidence_ids:
  - jcm796
  - target
- assessment_id: evidence
  area: evidence
  topic: Source batches, stocks and absent claims
  outcome: concern
  summary: All exact source rows are retained. Wrong units, unsupported local per-litre
    bases, empty scoped stock and absent preparation require curation; truthful gas/KOH
    placeholders and correct chemical identities are credited.
  target_ids:
  - CultureMech:010244
  evidence_ids:
  - quantities
  - old-claims
  - jcm796
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 50 current concentration fields are covered by 32 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:010244
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b074-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","quantity_field_count":50,"decisions":[{"quantity_id":"q1","label":"Distilled
    water","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"925","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"925","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source specifies 925 ml input water, not 925 g/L. Correct the quantity representation
    as source batch volume without assuming water density or a measured final medium
    volume.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 925,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML
    table row 12 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;925.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 925,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The
    source specifies 925 ml input water, not 925 g/L. Correct the quantity representation
    as source batch volume without assuming water density or a measured final medium
    volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The
    source specifies 925 ml input water, not 925 g/L. Correct the quantity representation
    as source batch volume without assuming water density or a measured final medium
    volume."}]},{"quantity_id":"q2","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\":
    \"Yeast extract\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\":
    \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\":
    \"Nutrient source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML
    table row 8 (zero-based)","quote":"<TR><TD WIDTH=75%> Yeast extract                                           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.999001,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."}]},{"quantity_id":"q3","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\":
    \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\":
    \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML
    table row 3 (zero-based)","quote":"<TR><TD WIDTH=75%> NaCl                                                    </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.999001,\n                        \"mmol_l\":
    17.0945,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."}]},{"quantity_id":"q4","label":"CaCl2・2H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\":
    \"CaCl2・2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\":
    \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML
    table row 5 (zero-based)","quote":"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0999001,\n                        \"mmol_l\":
    0.679523,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."}]},{"quantity_id":"q5","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\":
    \"KH2PO4\",\n          \"volume\": 0.3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\":
    \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\":
    \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML
    table row 0 (zero-based)","quote":"<TR><TD WIDTH=75%> KH<sub>2</sub>PO<sub>4</sub>                                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.3&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2997,\n                        \"mmol_l\":
    2.20229,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."}]},{"quantity_id":"q6","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\":
    \"NH4Cl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\":
    \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\":
    \"Nitrogen source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML
    table row 2 (zero-based)","quote":"<TR><TD WIDTH=75%> NH<sub>4</sub>Cl                                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.999001,\n                        \"mmol_l\":
    18.6764,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."}]},{"quantity_id":"q7","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\":
    \"K2HPO4\",\n          \"volume\": 0.3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\":
    \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\":
    \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML
    table row 1 (zero-based)","quote":"<TR><TD WIDTH=75%> K<sub>2</sub>HPO<sub>4</sub>                                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.3&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2997,\n                        \"mmol_l\":
    1.72068,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."}]},{"quantity_id":"q8","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact primary and TOGO source specify 1 mg resazurin, not 1 g/L. Preserve the
    batch mass and neutral resazurin identity; APIJ796 separately declares 0.000999001
    g_l on its computational 1001 ml basis.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\":
    \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\":
    \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\":
    \"pH dependent redox indicator\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> Resazurin                                               </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\":
    25,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.000999001,\n                        \"mmol_l\":
    0.00435883,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"correct","rationale":"The
    exact primary and TOGO source specify 1 mg resazurin, not 1 g/L. Preserve the
    batch mass and neutral resazurin identity; APIJ796 separately declares 0.000999001
    g_l on its computational 1001 ml basis."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[7].concentration","decision":"correct","rationale":"The
    exact primary and TOGO source specify 1 mg resazurin, not 1 g/L. Preserve the
    batch mass and neutral resazurin identity; APIJ796 separately declares 0.000999001
    g_l on its computational 1001 ml basis."}]},{"quantity_id":"q9","label":"MgCl2・6H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\":
    \"MgCl2・6H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\":
    \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML
    table row 4 (zero-based)","quote":"<TR><TD WIDTH=75%> MgCl<sub>2</sub>&#183;6H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.499501,\n                        \"mmol_l\":
    2.45693,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."}]},{"quantity_id":"q10","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\":
    \"KCl\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\":
    \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML
    table row 6 (zero-based)","quote":"<TR><TD WIDTH=75%> KCl                                                     </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0999001,\n                        \"mmol_l\":
    1.34004,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."}]},{"quantity_id":"q11","label":"Trypticase peptone (BD-BBL)","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\":
    \"Trypticase peptone (BD-BBL)\",\n          \"volume\": 1,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001097\",\n          \"gmo_id\":
    \"GMO_001097\",\n          \"label\": \"BBL &trade; Trypticase peptone\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML
    table row 9 (zero-based)","quote":"<TR><TD WIDTH=75%> Trypticase peptone (BD-BBL)                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\":
    124,\n                        \"attribute\": \"BD-BBL\",\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.999001,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."}]},{"quantity_id":"q12","label":"L--Cysteine・HCl・H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator.","source_stage":"main batch","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[11]","quote":"{\n          \"component_name\":
    \"L--Cysteine・HCl・H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001205\",\n          \"gmo_id\": \"GMO_001205\",\n          \"label\":
    \"L-Cysteine hydrochloride monohydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML
    table row 10 (zero-based)","quote":"<TR><TD WIDTH=75%> L-Cysteine&#183;HCl&#183;H<sub>2</sub>O                      </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\":
    770,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.499501,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"The
    printed batch mass is supported, but its stored G_PER_L basis is not established
    by the primary water input. Current APIJ796 declares a separate 1001 ml computational
    normalization with a different g_l; do not silently transfer that provider rate
    or claim measured final volume. Retain the exact primary batch mass and qualify
    the local denominator."}]},{"quantity_id":"q13","label":"KOH","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"The
    VARIABLE amount truthfully represents an unquantified source addition. Retain
    it and attach the exact preparation context; KOH pH adjustment and the 4:1 N2/CO2
    gas ratio do not specify a reagent mass or gas volume.","source_stage":"main preparation","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[13]","quote":"{\n          \"component_name\":
    \"KOH\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001903\",\n          \"gmo_id\":
    \"GMO_001903\",\n          \"label\": \"Potassium hydroxide solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix components thoroughly, adjust pH to 7.0 with KOH,
    distribute the medium into culture vessels under a N2--CO2 (4:1, v/v) gas mixture,
    seal with butyl rubber stoppers and autoclave. After cooling, add per 925 ml the
    following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"evidence_only","rationale":"The
    VARIABLE amount truthfully represents an unquantified source addition. Retain
    it and attach the exact preparation context; KOH pH adjustment and the 4:1 N2/CO2
    gas ratio do not specify a reagent mass or gas volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[12].concentration","decision":"evidence_only","rationale":"The
    VARIABLE amount truthfully represents an unquantified source addition. Retain
    it and attach the exact preparation context; KOH pH adjustment and the 4:1 N2/CO2
    gas ratio do not specify a reagent mass or gas volume."}]},{"quantity_id":"q14","label":"Carbon
    dioxide gas","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"The
    VARIABLE amount truthfully represents an unquantified source addition. Retain
    it and attach the exact preparation context; KOH pH adjustment and the 4:1 N2/CO2
    gas ratio do not specify a reagent mass or gas volume.","source_stage":"main preparation","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[14]","quote":"{\n          \"component_name\":
    \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\":
    \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix components thoroughly, adjust pH to 7.0 with KOH,
    distribute the medium into culture vessels under a N2--CO2 (4:1, v/v) gas mixture,
    seal with butyl rubber stoppers and autoclave. After cooling, add per 925 ml the
    following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"evidence_only","rationale":"The
    VARIABLE amount truthfully represents an unquantified source addition. Retain
    it and attach the exact preparation context; KOH pH adjustment and the 4:1 N2/CO2
    gas ratio do not specify a reagent mass or gas volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[13].concentration","decision":"evidence_only","rationale":"The
    VARIABLE amount truthfully represents an unquantified source addition. Retain
    it and attach the exact preparation context; KOH pH adjustment and the 4:1 N2/CO2
    gas ratio do not specify a reagent mass or gas volume."}]},{"quantity_id":"q15","label":"Nitrogen
    gas","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"The
    VARIABLE amount truthfully represents an unquantified source addition. Retain
    it and attach the exact preparation context; KOH pH adjustment and the 4:1 N2/CO2
    gas ratio do not specify a reagent mass or gas volume.","source_stage":"main preparation","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[15]","quote":"{\n          \"component_name\":
    \"Nitrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\":
    \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix components thoroughly, adjust pH to 7.0 with KOH,
    distribute the medium into culture vessels under a N2--CO2 (4:1, v/v) gas mixture,
    seal with butyl rubber stoppers and autoclave. After cooling, add per 925 ml the
    following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"evidence_only","rationale":"The
    VARIABLE amount truthfully represents an unquantified source addition. Retain
    it and attach the exact preparation context; KOH pH adjustment and the 4:1 N2/CO2
    gas ratio do not specify a reagent mass or gas volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"ingredients[14].concentration","decision":"evidence_only","rationale":"The
    VARIABLE amount truthfully represents an unquantified source addition. Retain
    it and attach the exact preparation context; KOH pH adjustment and the 4:1 N2/CO2
    gas ratio do not specify a reagent mass or gas volume."}]},{"quantity_id":"q16","label":"Microelement
    solution (see Medium [M484])","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source supplies a stock addition in ml, not a mass concentration. Preserve this
    exact batch addition and its separately stated stock strength; do not convert
    bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and
    100 mg/L strengths are explicit and distinct from addition volumes.","source_stage":"receiving
    stock addition","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[0].items[12]","quote":"{\n          \"component_name\":
    \"Microelement solution (see Medium [M484])\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M484\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution (see
    Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=483\">483</a>)           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Trace element solution\",\n                        \"compound_id\":
    96,\n                        \"attribute\": \"see Medium No. 483\",\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[0].concentration","decision":"correct","rationale":"The
    source supplies a stock addition in ml, not a mass concentration. Preserve this
    exact batch addition and its separately stated stock strength; do not convert
    bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and
    100 mg/L strengths are explicit and distinct from addition volumes."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[0].concentration","decision":"correct","rationale":"The
    source supplies a stock addition in ml, not a mass concentration. Preserve this
    exact batch addition and its separately stated stock strength; do not convert
    bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and
    100 mg/L strengths are explicit and distinct from addition volumes."}]},{"quantity_id":"q17","label":"8%
    NaHCO3 solution*","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"25","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"25","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source supplies a stock addition in ml, not a mass concentration. Preserve this
    exact batch addition and its separately stated stock strength; do not convert
    bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and
    100 mg/L strengths are explicit and distinct from addition volumes.","source_stage":"receiving
    stock addition","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
    \"8% NaHCO3 solution*\",\n          \"volume\": 25,\n          \"unit\": \"ml\",\n          \"conc_value\":
    8,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001119\",\n          \"gmo_id\":
    \"GMO_001119\",\n          \"label\": \"Sodium bicarbonate solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML
    table row 13 (zero-based)","quote":"<TR><TD WIDTH=75%> 8% NaHCO3 solution*                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;25.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"attribute\": \"*, 8%\",\n                        \"amount\":
    25,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[1].concentration","decision":"correct","rationale":"The
    source supplies a stock addition in ml, not a mass concentration. Preserve this
    exact batch addition and its separately stated stock strength; do not convert
    bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and
    100 mg/L strengths are explicit and distinct from addition volumes."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[1].concentration","decision":"correct","rationale":"The
    source supplies a stock addition in ml, not a mass concentration. Preserve this
    exact batch addition and its separately stated stock strength; do not convert
    bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and
    100 mg/L strengths are explicit and distinct from addition volumes."}]},{"quantity_id":"q18","label":"0.1
    M Sodium sulfite solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[2].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source supplies a stock addition in ml, not a mass concentration. Preserve this
    exact batch addition and its separately stated stock strength; do not convert
    bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and
    100 mg/L strengths are explicit and distinct from addition volumes.","source_stage":"receiving
    stock addition","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
    \"0.1 M Sodium sulfite solution\",\n          \"volume\": 20,\n          \"unit\":
    \"ml\",\n          \"conc_value\": 0.1,\n          \"conc_unit\": \"M\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001452\",\n          \"gmo_id\": \"GMO_001452\",\n          \"label\":
    \"Sodium sulfite solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\":
    \"Reducing agent\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML
    table row 14 (zero-based)","quote":"<TR><TD WIDTH=75%> 0.1 M Sodium sulfite solution                          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Sodium sulfite\",\n                        \"compound_id\":
    1897,\n                        \"attribute\": \"0.1 M\",\n                        \"amount\":
    20,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[2].concentration","decision":"correct","rationale":"The
    source supplies a stock addition in ml, not a mass concentration. Preserve this
    exact batch addition and its separately stated stock strength; do not convert
    bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and
    100 mg/L strengths are explicit and distinct from addition volumes."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[2].concentration","decision":"correct","rationale":"The
    source supplies a stock addition in ml, not a mass concentration. Preserve this
    exact batch addition and its separately stated stock strength; do not convert
    bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and
    100 mg/L strengths are explicit and distinct from addition volumes."}]},{"quantity_id":"q19","label":"1
    M Sodium pyruvate solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[3].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source supplies a stock addition in ml, not a mass concentration. Preserve this
    exact batch addition and its separately stated stock strength; do not convert
    bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and
    100 mg/L strengths are explicit and distinct from addition volumes.","source_stage":"receiving
    stock addition","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
    \"1 M Sodium pyruvate solution\",\n          \"volume\": 20,\n          \"unit\":
    \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001475\",\n          \"gmo_id\": \"GMO_001475\",\n          \"label\":
    \"Sodium pyruvate solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\":
    \"Carbon source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML
    table row 15 (zero-based)","quote":"<TR><TD WIDTH=75%> 1 M Sodium pyruvate solution                           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[15]","quote":"{\n                        \"recipe_order\":
    16,\n                        \"compound\": \"Sodium pyruvate\",\n                        \"compound_id\":
    438,\n                        \"attribute\": \"1 M\",\n                        \"amount\":
    20,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[3].concentration","decision":"correct","rationale":"The
    source supplies a stock addition in ml, not a mass concentration. Preserve this
    exact batch addition and its separately stated stock strength; do not convert
    bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and
    100 mg/L strengths are explicit and distinct from addition volumes."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[3].concentration","decision":"correct","rationale":"The
    source supplies a stock addition in ml, not a mass concentration. Preserve this
    exact batch addition and its separately stated stock strength; do not convert
    bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and
    100 mg/L strengths are explicit and distinct from addition volumes."}]},{"quantity_id":"q20","label":"5%
    Na2S・9H2O solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[4].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[4].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source supplies a stock addition in ml, not a mass concentration. Preserve this
    exact batch addition and its separately stated stock strength; do not convert
    bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and
    100 mg/L strengths are explicit and distinct from addition volumes.","source_stage":"receiving
    stock addition","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\":
    \"5% Na2S・9H2O solution\",\n          \"volume\": 8,\n          \"unit\": \"ml\",\n          \"conc_value\":
    5,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001494\",\n          \"gmo_id\":
    \"GMO_001494\",\n          \"label\": \"Sodium sulfide nonahydrate solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\":
    \"Reducing agent\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML
    table row 17 (zero-based)","quote":"<TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O
    solution                      </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;8.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[17]","quote":"{\n                        \"recipe_order\":
    18,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"attribute\": \"5%\",\n                        \"amount\":
    8,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[4].concentration","decision":"correct","rationale":"The
    source supplies a stock addition in ml, not a mass concentration. Preserve this
    exact batch addition and its separately stated stock strength; do not convert
    bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and
    100 mg/L strengths are explicit and distinct from addition volumes."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[4].concentration","decision":"correct","rationale":"The
    source supplies a stock addition in ml, not a mass concentration. Preserve this
    exact batch addition and its separately stated stock strength; do not convert
    bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and
    100 mg/L strengths are explicit and distinct from addition volumes."}]},{"quantity_id":"q21","label":"Sodium
    dithionite solution (100 mg/L)*","local_fields":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[5].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[5].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source supplies a stock addition in ml, not a mass concentration. Preserve this
    exact batch addition and its separately stated stock strength; do not convert
    bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and
    100 mg/L strengths are explicit and distinct from addition volumes.","source_stage":"receiving
    stock addition","sources":[{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\":
    \"Sodium dithionite solution (100 mg/L)*\",\n          \"volume\": 2,\n          \"unit\":
    \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001721\",\n          \"gmo_id\":
    \"GMO_001721\",\n          \"label\": \"Sodium dithionite solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> Sodium dithionite solution
    (100 mg/L)*                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].recipe[16]","quote":"{\n                        \"recipe_order\":
    17,\n                        \"compound\": \"Sodium dithionite\",\n                        \"compound_id\":
    1676,\n                        \"attribute\": \"*, 100 mg/L\",\n                        \"amount\":
    2,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml","field_path":"solutions[5].concentration","decision":"correct","rationale":"The
    source supplies a stock addition in ml, not a mass concentration. Preserve this
    exact batch addition and its separately stated stock strength; do not convert
    bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and
    100 mg/L strengths are explicit and distinct from addition volumes."},{"path":"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml","field_path":"solutions[5].concentration","decision":"correct","rationale":"The
    source supplies a stock addition in ml, not a mass concentration. Preserve this
    exact batch addition and its separately stated stock strength; do not convert
    bare 8% or 5% into w/v or infer a final medium denominator. The 0.1 M, 1 M and
    100 mg/L strengths are explicit and distinct from addition volumes."}]},{"quantity_id":"q22","label":"CaCl2・2H2O
    in JCM483 microelements","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact component mass belongs to the referenced microelement stock, not the parent
    final medium or the selected receiving medium. Its source uses 1 L water input
    without explicit final makeup. Preserve that stock batch mass and the selected
    1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated
    parent formulation.","source_stage":"scoped microelement stock","sources":[{"evidence_id":"togo484","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo484.bin","raw_sha256":"e62611edbbc4fc289ee902fff57465f53c1927debe72108c19794f91a51e7fd1","text_sha256":"c3815e3fdd2177b3d03bc60b4e8abe1bb110de33e4f5d7d5fa74f693d276c8e6","accessed_at":"2026-10-28T18:07:26.264203Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
    \"CaCl2・2H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\":
    \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm483","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm483.bin","raw_sha256":"4fbd01bff716d5389eca921b496534346d6281dd72c8cc23f7fdef3d806e5fa1","text_sha256":"5e110f4f2ca7a8043e25abb292824049c8d50ba0344ad43d9a557c243de48ca8","accessed_at":"2026-10-28T18:07:26.041708Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The
    exact component mass belongs to the referenced microelement stock, not the parent
    final medium or the selected receiving medium. Its source uses 1 L water input
    without explicit final makeup. Preserve that stock batch mass and the selected
    1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated
    parent formulation."}]},{"quantity_id":"q23","label":"Na2MoO4・2H2O in JCM483 microelements","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact component mass belongs to the referenced microelement stock, not the parent
    final medium or the selected receiving medium. Its source uses 1 L water input
    without explicit final makeup. Preserve that stock batch mass and the selected
    1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated
    parent formulation.","source_stage":"scoped microelement stock","sources":[{"evidence_id":"togo484","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo484.bin","raw_sha256":"e62611edbbc4fc289ee902fff57465f53c1927debe72108c19794f91a51e7fd1","text_sha256":"c3815e3fdd2177b3d03bc60b4e8abe1bb110de33e4f5d7d5fa74f693d276c8e6","accessed_at":"2026-10-28T18:07:26.264203Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
    \"Na2MoO4・2H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\":
    \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm483","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm483.bin","raw_sha256":"4fbd01bff716d5389eca921b496534346d6281dd72c8cc23f7fdef3d806e5fa1","text_sha256":"5e110f4f2ca7a8043e25abb292824049c8d50ba0344ad43d9a557c243de48ca8","accessed_at":"2026-10-28T18:07:26.041708Z","locator":"HTML
    table row 17 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"The
    exact component mass belongs to the referenced microelement stock, not the parent
    final medium or the selected receiving medium. Its source uses 1 L water input
    without explicit final makeup. Preserve that stock batch mass and the selected
    1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated
    parent formulation."}]},{"quantity_id":"q24","label":"H3BO3 in JCM483 microelements","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact component mass belongs to the referenced microelement stock, not the parent
    final medium or the selected receiving medium. Its source uses 1 L water input
    without explicit final makeup. Preserve that stock batch mass and the selected
    1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated
    parent formulation.","source_stage":"scoped microelement stock","sources":[{"evidence_id":"togo484","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo484.bin","raw_sha256":"e62611edbbc4fc289ee902fff57465f53c1927debe72108c19794f91a51e7fd1","text_sha256":"c3815e3fdd2177b3d03bc60b4e8abe1bb110de33e4f5d7d5fa74f693d276c8e6","accessed_at":"2026-10-28T18:07:26.264203Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\":
    \"H3BO3\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\":
    \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm483","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm483.bin","raw_sha256":"4fbd01bff716d5389eca921b496534346d6281dd72c8cc23f7fdef3d806e5fa1","text_sha256":"5e110f4f2ca7a8043e25abb292824049c8d50ba0344ad43d9a557c243de48ca8","accessed_at":"2026-10-28T18:07:26.041708Z","locator":"HTML
    table row 14 (zero-based)","quote":"<TR><TD WIDTH=75%> H<sub>3</sub>BO<sub>3</sub>                                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[12].concentration","decision":"unsupported","rationale":"The
    exact component mass belongs to the referenced microelement stock, not the parent
    final medium or the selected receiving medium. Its source uses 1 L water input
    without explicit final makeup. Preserve that stock batch mass and the selected
    1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated
    parent formulation."}]},{"quantity_id":"q25","label":"CoCl2・6H2O in JCM483 microelements","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact component mass belongs to the referenced microelement stock, not the parent
    final medium or the selected receiving medium. Its source uses 1 L water input
    without explicit final makeup. Preserve that stock batch mass and the selected
    1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated
    parent formulation.","source_stage":"scoped microelement stock","sources":[{"evidence_id":"togo484","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo484.bin","raw_sha256":"e62611edbbc4fc289ee902fff57465f53c1927debe72108c19794f91a51e7fd1","text_sha256":"c3815e3fdd2177b3d03bc60b4e8abe1bb110de33e4f5d7d5fa74f693d276c8e6","accessed_at":"2026-10-28T18:07:26.264203Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\":
    \"CoCl2・6H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\":
    \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm483","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm483.bin","raw_sha256":"4fbd01bff716d5389eca921b496534346d6281dd72c8cc23f7fdef3d806e5fa1","text_sha256":"5e110f4f2ca7a8043e25abb292824049c8d50ba0344ad43d9a557c243de48ca8","accessed_at":"2026-10-28T18:07:26.041708Z","locator":"HTML
    table row 18 (zero-based)","quote":"<TR><TD WIDTH=75%> CoCl<sub>2</sub>&#183;6H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.2&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[13].concentration","decision":"unsupported","rationale":"The
    exact component mass belongs to the referenced microelement stock, not the parent
    final medium or the selected receiving medium. Its source uses 1 L water input
    without explicit final makeup. Preserve that stock batch mass and the selected
    1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated
    parent formulation."}]},{"quantity_id":"q26","label":"ZnSO4・7H2O in JCM483 microelements","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact component mass belongs to the referenced microelement stock, not the parent
    final medium or the selected receiving medium. Its source uses 1 L water input
    without explicit final makeup. Preserve that stock batch mass and the selected
    1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated
    parent formulation.","source_stage":"scoped microelement stock","sources":[{"evidence_id":"togo484","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo484.bin","raw_sha256":"e62611edbbc4fc289ee902fff57465f53c1927debe72108c19794f91a51e7fd1","text_sha256":"c3815e3fdd2177b3d03bc60b4e8abe1bb110de33e4f5d7d5fa74f693d276c8e6","accessed_at":"2026-10-28T18:07:26.264203Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\":
    \"ZnSO4・7H2O\",\n          \"volume\": 0.05,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001023\",\n          \"gmo_id\": \"GMO_001023\",\n          \"label\":
    \"Zinc sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm483","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm483.bin","raw_sha256":"4fbd01bff716d5389eca921b496534346d6281dd72c8cc23f7fdef3d806e5fa1","text_sha256":"5e110f4f2ca7a8043e25abb292824049c8d50ba0344ad43d9a557c243de48ca8","accessed_at":"2026-10-28T18:07:26.041708Z","locator":"HTML
    table row 13 (zero-based)","quote":"<TR><TD WIDTH=75%> ZnSO<sub>4</sub>&#183;7H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.05&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[14].concentration","decision":"unsupported","rationale":"The
    exact component mass belongs to the referenced microelement stock, not the parent
    final medium or the selected receiving medium. Its source uses 1 L water input
    without explicit final makeup. Preserve that stock batch mass and the selected
    1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated
    parent formulation."}]},{"quantity_id":"q27","label":"AlK(SO4)2・12H2O in JCM483
    microelements","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact component mass belongs to the referenced microelement stock, not the parent
    final medium or the selected receiving medium. Its source uses 1 L water input
    without explicit final makeup. Preserve that stock batch mass and the selected
    1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated
    parent formulation.","source_stage":"scoped microelement stock","sources":[{"evidence_id":"togo484","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo484.bin","raw_sha256":"e62611edbbc4fc289ee902fff57465f53c1927debe72108c19794f91a51e7fd1","text_sha256":"c3815e3fdd2177b3d03bc60b4e8abe1bb110de33e4f5d7d5fa74f693d276c8e6","accessed_at":"2026-10-28T18:07:26.264203Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\":
    \"AlK(SO4)2・12H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001051\",\n          \"gmo_id\": \"GMO_001051\",\n          \"label\":
    \"Aluminum potassium sulfate dodecahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm483","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm483.bin","raw_sha256":"4fbd01bff716d5389eca921b496534346d6281dd72c8cc23f7fdef3d806e5fa1","text_sha256":"5e110f4f2ca7a8043e25abb292824049c8d50ba0344ad43d9a557c243de48ca8","accessed_at":"2026-10-28T18:07:26.041708Z","locator":"HTML
    table row 19 (zero-based)","quote":"<TR><TD WIDTH=75%> AlK(SO<sub>4</sub>)<sub>2</sub>&#183;12H<sub>2</sub>O                          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[15].concentration","decision":"unsupported","rationale":"The
    exact component mass belongs to the referenced microelement stock, not the parent
    final medium or the selected receiving medium. Its source uses 1 L water input
    without explicit final makeup. Preserve that stock batch mass and the selected
    1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated
    parent formulation."}]},{"quantity_id":"q28","label":"Nitrilotriacetic acid in
    JCM483 microelements","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"4.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact component mass belongs to the referenced microelement stock, not the parent
    final medium or the selected receiving medium. Its source uses 1 L water input
    without explicit final makeup. Preserve that stock batch mass and the selected
    1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated
    parent formulation.","source_stage":"scoped microelement stock","sources":[{"evidence_id":"togo484","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo484.bin","raw_sha256":"e62611edbbc4fc289ee902fff57465f53c1927debe72108c19794f91a51e7fd1","text_sha256":"c3815e3fdd2177b3d03bc60b4e8abe1bb110de33e4f5d7d5fa74f693d276c8e6","accessed_at":"2026-10-28T18:07:26.264203Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\":
    \"Nitrilotriacetic acid\",\n          \"volume\": 4.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001053\",\n          \"gmo_id\": \"GMO_001053\",\n          \"label\":
    \"Nitrilotriacetic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm483","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm483.bin","raw_sha256":"4fbd01bff716d5389eca921b496534346d6281dd72c8cc23f7fdef3d806e5fa1","text_sha256":"5e110f4f2ca7a8043e25abb292824049c8d50ba0344ad43d9a557c243de48ca8","accessed_at":"2026-10-28T18:07:26.041708Z","locator":"HTML
    table row 15 (zero-based)","quote":"<TR><TD WIDTH=75%> Nitrilotriacetic acid                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;4.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[16].concentration","decision":"unsupported","rationale":"The
    exact component mass belongs to the referenced microelement stock, not the parent
    final medium or the selected receiving medium. Its source uses 1 L water input
    without explicit final makeup. Preserve that stock batch mass and the selected
    1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated
    parent formulation."}]},{"quantity_id":"q29","label":"MnSO4・xH2O in JCM483 microelements","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact component mass belongs to the referenced microelement stock, not the parent
    final medium or the selected receiving medium. Its source uses 1 L water input
    without explicit final makeup. Preserve that stock batch mass and the selected
    1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated
    parent formulation.","source_stage":"scoped microelement stock","sources":[{"evidence_id":"togo484","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo484.bin","raw_sha256":"e62611edbbc4fc289ee902fff57465f53c1927debe72108c19794f91a51e7fd1","text_sha256":"c3815e3fdd2177b3d03bc60b4e8abe1bb110de33e4f5d7d5fa74f693d276c8e6","accessed_at":"2026-10-28T18:07:26.264203Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\":
    \"MnSO4・xH2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001065\",\n          \"gmo_id\": \"GMO_001065\",\n          \"label\":
    \"Manganese sulfate n-hydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm483","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm483.bin","raw_sha256":"4fbd01bff716d5389eca921b496534346d6281dd72c8cc23f7fdef3d806e5fa1","text_sha256":"5e110f4f2ca7a8043e25abb292824049c8d50ba0344ad43d9a557c243de48ca8","accessed_at":"2026-10-28T18:07:26.041708Z","locator":"HTML
    table row 12 (zero-based)","quote":"<TR><TD WIDTH=75%> MnSO<sub>4</sub>&#183;<I>x</I>H<sub>2</sub>O                           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml","field_path":"ingredients[17].concentration","decision":"unsupported","rationale":"The
    exact component mass belongs to the referenced microelement stock, not the parent
    final medium or the selected receiving medium. Its source uses 1 L water input
    without explicit final makeup. Preserve that stock batch mass and the selected
    1 ml addition separately; exclude the parent 10 ml receiving dose and unrelated
    parent formulation."}]},{"quantity_id":"q30","label":"Microelement stock solvent","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    the stock-specific 1 L water input; the collapsed parent water row mixes other
    stages and is intentionally outside dependency scope. Input water is not explicit
    final makeup.","source_stage":"source-only microelement stock","sources":[{"evidence_id":"togo484","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M484","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo484.bin","raw_sha256":"e62611edbbc4fc289ee902fff57465f53c1927debe72108c19794f91a51e7fd1","text_sha256":"c3815e3fdd2177b3d03bc60b4e8abe1bb110de33e4f5d7d5fa74f693d276c8e6","accessed_at":"2026-10-28T18:07:26.264203Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm483","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=483","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm483.bin","raw_sha256":"4fbd01bff716d5389eca921b496534346d6281dd72c8cc23f7fdef3d806e5fa1","text_sha256":"5e110f4f2ca7a8043e25abb292824049c8d50ba0344ad43d9a557c243de48ca8","accessed_at":"2026-10-28T18:07:26.041708Z","locator":"HTML
    table row 20 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L  </TD></TR>","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q31","label":"Main
    pH, atmosphere and staged preparation","local_fields":[],"decision":"evidence_only","rationale":"Retain
    pH 7.0 with KOH, N2/CO2 4:1 v/v, butyl-rubber closure, autoclaving followed by
    cooling and anaerobic stock additions per 925 ml. The starred bicarbonate and
    dithionite stocks are filter-sterilized. This source sequence is absent locally;
    no quantitative gas addition is inferred.","source_stage":"source-only main preparation","sources":[{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"jcm796.txt
    lines 65-69","quote":"Mix components thoroughly, adjust pH to 7.0 with KOH, distribute
    the medium into culture vessels under a N\n2\n-CO\n2\n(4:1, v/v) gas mixture,
    seal with butyl rubber stoppers and autoclave.  After cooling, add per 925 ml
    the following solutions from anaerobic stocks (autoclaved or *filter-sterilized):","quote_basis":"derivative
    text"},{"evidence_id":"togo830","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M830","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/togo830.bin","raw_sha256":"88ae3c0d3c9bd9d9ad93d17977ce7b7d5848e6ffecdddf821f54b5b639995a9b","text_sha256":"18548c236821de91c882da41efc93e57603e75357fb147e87eef5a3b7ef2817e","accessed_at":"2026-10-28T18:07:26.236052Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix components thoroughly, adjust pH to 7.0 with KOH,
    distribute the medium into culture vessels under a N2--CO2 (4:1, v/v) gas mixture,
    seal with butyl rubber stoppers and autoclave. After cooling, add per 925 ml the
    following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ796","reference":"https://mediadive.dsmz.de/rest/medium/J796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/apiJ796.bin","raw_sha256":"4811c05ede9dd5fa52d7765dba69ae7468e7de8715d7839066a0e2114fb0dbae","text_sha256":"71929b38034dded575f8f905e054e98c9d5e4095920b93aedc4b60867b6937ce","accessed_at":"2026-10-28T18:07:26.498732Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"step\": \"Mix components thoroughly, adjust pH
    to 7.0 with KOH, distribute the medium into culture vessels under a N2-CO2 (4:1,
    v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling,
    add per 925 ml the following solutions from anaerobic stocks (autoclaved or *filter-sterilized):
    \"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q32","label":"JCM
    page-wide autoclave default","local_fields":[],"decision":"evidence_only","rationale":"The
    page explicitly supplies 121°C for 15 min unless otherwise stated. Apply only
    to the inherited autoclave steps, not the separately starred filter-sterilized
    stocks; retain this as a page-default claim with explicit scope.","source_stage":"source-only
    default preparation","sources":[{"evidence_id":"jcm796","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=796","raw_path":"REVIEW_WORK/batch074/source01-03-supplement/jcm796.bin","raw_sha256":"7bf93d053d70aa8e1ebbee1837673ed7e832196728d5f24017c9327c2ffb2ddd","text_sha256":"ab967de282583a2be76ffb93b326477f3b3e6c53612fe8105a01fc25f478d0e3","accessed_at":"2026-10-28T18:07:25.969580Z","locator":"jcm796.txt
    lines 4-4","quote":"Unless otherwise stated, sterilize media by autoclaving at
    121°C for 15 min.","quote_basis":"derivative text"}],"layer_assessments":[]}],"document_scopes":{"data/merge_yaml/merged/DESULFITOCELLA_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml":null,"data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml":["ingredients[10]","ingredients[11]","ingredients[12]","ingredients[13]","ingredients[14]","ingredients[15]","ingredients[16]","ingredients[17]"]},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: Every selected and explicitly scoped dependency slot is checked against
    fresh OLS and exact packaged MIM rows. Primary cobalt hexahydrate conflicts with
    anhydrous35696; the manganese x-hydrate remains unresolved. Selected neutral resazurin8806,
    magnesium hexahydrate86345, calcium dihydrate86158 and L-cysteine hydrochloride
    monohydrate91248 match the source forms. Yeast FOODON03315426 is a whole-mixture
    candidate; branded peptone equivalence is not invented. Missing secondary links
    are recorded separately from canonical-label and supplied-form validity.
  target_ids:
  - CultureMech:010244
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: All current target/owner/dependency events and four complete historical
    reports were read. The neighboring DSM merged record is comparison context only.
    Historical reports have zero external source checks and do not supply authenticated
    source objects or selected parent repair rows here. No local attached claims exist.
    Current TOGO stock separation, unit mapping and comment extraction are credited,
    while their remaining denominator and mixed-step limitations are explicit; current
    behavior is not proof of historical execution.
  target_ids:
  - CultureMech:010244
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-010244-batch-units-and-denominators
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Correct batch units and qualify concentration bases
  description: Water is 925 ml and resazurin is 1 mg in the primary; all six stock
    additions are ml. Their stored G_PER_L representations are wrong. The other batch
    masses are correctly transcribed but lack explicit final-volume support for their
    current per-litre basis. Current APIJ796 independently declares normalization
    on 1001 ml, rather than establishing measured final volume. Preserve original
    source amounts and distinguish any provider basis.
  target_ids:
  - CultureMech:010244
  field_paths:
  - ingredients[0].concentration
  - ingredients[7].concentration
  - ingredients
  - solutions
  evidence_ids:
  - jcm796
  - togo830
  - apiJ796
  - quantities
  - writer-togo
  rule_id: review-yaml-record/custom-batch-units-and-denominators
  native_severity: P2
  normalization_reason: 'Custom quantity rule: material source-unit, stock-stage,
    preparation or supplied-form defect.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-010244-microelement-stock-scope
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Resolve the referenced microelement stock within its exact scope
  description: The empty M484 reference points to JCM483 microelements. Only its eight
    microelement ingredients are relevant; they are flattened into the parent main
    list. Represent the scoped stock and selected 1 ml receiving addition without
    transferring the parent 10 ml dose, main formulation, vitamins or parent pH. Keep
    the five separately named late-stock strengths and receiving volumes; a supplied
    molarity or bare percentage is not a complete mass recipe.
  target_ids:
  - CultureMech:010244
  field_paths:
  - solutions[0].composition
  - solutions[0].notes
  - data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml::ingredients[10].concentration
  - data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml::ingredients[11].concentration
  - data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml::ingredients[12].concentration
  - data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml::ingredients[13].concentration
  - data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml::ingredients[14].concentration
  - data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml::ingredients[15].concentration
  - data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml::ingredients[16].concentration
  - data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml::ingredients[17].concentration
  evidence_ids:
  - jcm796
  - jcm483
  - togo830
  - togo484
  - microelement-owner
  - quantities
  rule_id: review-yaml-record/custom-microelement-stock-scope
  native_severity: P2
  normalization_reason: 'Custom representation rule: material source-unit, stock-stage,
    preparation or supplied-form defect.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml
    role: scoped dependency
- finding_id: f3
  issue_key: culturemech-010244-missing-staged-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Add the exact pH and anaerobic preparation sequence
  description: Both selected layers omit pH 7.0 and all preparation steps. Preserve
    the supported KOH and gas VARIABLE placeholders while adding their actual pH/ratio
    context, autoclave/cooling order, closure and separately sterilized stock additions.
    Scope the page-wide 121°C/15 min default to autoclaving and exclude starred filtration.
  target_ids:
  - CultureMech:010244
  field_paths:
  - ph_value
  - preparation_steps
  - evidence
  evidence_ids:
  - jcm796
  - togo830
  - apiJ796
  - quantities
  - writer-togo
  rule_id: review-yaml-record/custom-missing-staged-preparation
  native_severity: P2
  normalization_reason: 'Custom completeness rule: material source-unit, stock-stage,
    preparation or supplied-form defect.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-010244-microelement-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile scoped cobalt and unresolved manganese hydrate
  description: The scoped M484 cobalt hexahydrate is linked to anhydrous CHEBI:35696.
    Resolve the supplied hexahydrate without changing its source mass. MnSO4·xH2O
    is not fully specified by the anhydrous CHEBI:86360 assertion; preserve the unknown
    hydrate number and do not choose a convenient fixed hydrate. Selected calcium/magnesium
    hydrates, L-cysteine hydrochloride monohydrate and neutral resazurin are supported.
    Their identities do not validate the current quantity units.
  target_ids:
  - CultureMech:010244
  field_paths:
  - data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml::ingredients[13].term
  - data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml::ingredients[17].term
  evidence_ids:
  - jcm483
  - togo484
  - groundings
  - mim
  rule_id: review-yaml-record/custom-microelement-hydrate-grounding
  native_severity: P2
  normalization_reason: 'Custom grounding rule: material source-unit, stock-stage,
    preparation or supplied-form defect.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml
    role: scoped dependency
- finding_id: f5
  issue_key: culturemech-010244-stock-names-and-claim-linkage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Replace placeholder names and attach source-scoped claims
  description: All six solutions retain the literal name Unknown solution despite
    distinct preferred terms, and no attached claims exist. Use exact source-specific
    stock names; attach ingredient evidence and schema-root evidence for receiving
    amounts/preparation. Yeast extract has a verified whole-mixture FOODON candidate;
    the branded Trypticase mixture must not be replaced with an assumed pure compound
    or unsupported product equivalent.
  target_ids:
  - CultureMech:010244
  field_paths:
  - solutions[*].name
  - ingredients[*].evidence
  - evidence
  - ingredients[1]
  - ingredients[10]
  evidence_ids:
  - old-claims
  - jcm796
  - jcm483
  - foodon03315426
  - mim
  rule_id: review-yaml-record/custom-stock-names-and-claim-linkage
  native_severity: P3
  normalization_reason: 'Custom completeness rule: bounded name, linkage and evidence
    follow-up with native schema shape already passing.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml
    role: maintained normalized contributor
actions:
- action_id: a1
  description: Water is 925 ml and resazurin is 1 mg in the primary; all six stock
    additions are ml. Their stored G_PER_L representations are wrong. The other batch
    masses are correctly transcribed but lack explicit final-volume support for their
    current per-litre basis. Current APIJ796 independently declares normalization
    on 1001 ml, rather than establishing measured final volume. Preserve original
    source amounts and distinguish any provider basis.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010244
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml
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
  description: The empty M484 reference points to JCM483 microelements. Only its eight
    microelement ingredients are relevant; they are flattened into the parent main
    list. Represent the scoped stock and selected 1 ml receiving addition without
    transferring the parent 10 ml dose, main formulation, vitamins or parent pH. Keep
    the five separately named late-stock strengths and receiving volumes; a supplied
    molarity or bare percentage is not a complete mass recipe.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010244
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml
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
  description: Both selected layers omit pH 7.0 and all preparation steps. Preserve
    the supported KOH and gas VARIABLE placeholders while adding their actual pH/ratio
    context, autoclave/cooling order, closure and separately sterilized stock additions.
    Scope the page-wide 121°C/15 min default to autoclaving and exclude starred filtration.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010244
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml
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
  description: The scoped M484 cobalt hexahydrate is linked to anhydrous CHEBI:35696.
    Resolve the supplied hexahydrate without changing its source mass. MnSO4·xH2O
    is not fully specified by the anhydrous CHEBI:86360 assertion; preserve the unknown
    hydrate number and do not choose a convenient fixed hydrate. Selected calcium/magnesium
    hydrates, L-cysteine hydrochloride monohydrate and neutral resazurin are supported.
    Their identities do not validate the current quantity units.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:010244
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M484_Ethanologenbacterium_Medium.yaml
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
  description: All six solutions retain the literal name Unknown solution despite
    distinct preferred terms, and no attached claims exist. Use exact source-specific
    stock names; attach ingredient evidence and schema-root evidence for receiving
    amounts/preparation. Yeast extract has a verified whole-mixture FOODON candidate;
    the branded Trypticase mixture must not be replaced with an assumed pure compound
    or unsupported product equivalent.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:010244
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M830_Desulfitocella_Medium.yaml
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
- Only M484 ingredients[10:18] are scientifically assessed as the referenced microelement
  composition; all other parent quantities and vitamins are excluded.
- The JCM796 primary specifies additions per 925 ml, with a separate 1 ml trace addition.
  APIJ796 uses 1001 ml computational normalization; neither establishes measured final
  main volume.
- The JCM483 stock specifies 1 L water input, not explicit final makeup. MnSO4 hydration
  number and bare 8%/5% bases remain unresolved.
- Unused provider mmol_l and manufacturer-specific peptone equivalence are not certified.
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
